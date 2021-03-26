"""
This module generates a database of all MC and data datasets
"""

# stdlib
import os, sys, re, glob
from operator import itemgetter
import logging
import cPickle as pickle
import atexit
import fnmatch
from collections import namedtuple
from  multiprocessing import Pool, cpu_count

# PyPI
import yaml

# local
from . import log
from .decorators import cached_property
from .yaml_utils import Serializable
from . import xsec
from .. import EVENTS_CUTFLOW_HIST, EVENTS_CUTFLOW_BIN, MC_CAMPAIGN 

# ROOT
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.SetSignalPolicy(ROOT.kSignalFast)

try:
    import pyAMI
    import pyAMI.client 
    import pyAMI.atlas.api as AtlasAPI

    amiclient = pyAMI.client.Client('atlas')
    AtlasAPI.init()
    
    from pyAMI.atlas.api import get_dataset_info, get_dataset_prov, get_file
except ImportError:
    pass

##--------------------------------------------------------------------------------
## consts
##--------------------------------------------------------------------------------
# Maximum files per Dataset; otherwise Dataset will be broken to sub-Dataset in order to speed up the analysis
N_DS_FILES = 10 
METADATA_TTREE_MERGED = False
if not METADATA_TTREE_MERGED:
    log.debug("Assuming that metadata and TTrees are written to different TFiles (v06 ntuples); see hpana.db.dataset.py!")

DATA, MC, EMBED, MCEMBED = range(4)
TYPES = {
    'DATA':    DATA,
    'MC':      MC,
    'EMBED':   EMBED,
    'MCEMBED': MCEMBED,
}

DATA15_RUNS_RANGE = (276262, 284484) #<! with 00 prefix 
DATA16_RUNS_RANGE = (297730, 311481)
DATA17_RUNS_RANGE = (325713, 338349)

#MC15_NTUP_PATTERN = re.compile("^(?P<id>(\d+))")
MC16_NTUP_PATTERN = re.compile(
    '^(?P<prefix>(group.phys-higgs|user))'
    '\.(?P<uname>\w+)'
    '\.(?P<jo>\w+)'
    '\.(?P<id>\d+)'
    '\.(?P<tag>\w+)'
    '\.(?P<suffix>\w+)$'
)
NTUP_PATTERN = re.compile(
    '^(?P<prefix>(group.phys-higgs)|(user\.\w+))'
    '((\.\w+)|)'
    '\.(?P<type>mc|data)'
    '(?P<stream>15|16|17|18)_13TeV'
    '\.(?P<id>\d+)'
    '\.(?P<name>\w+)'
    '\.(?P<derivation>D1|D2)'
    '\.(?P<tag>\w+)'
    '\.(?P<version>\w+)'
    '_(BS)$'
    )


AOD_TAG_PATTERN = re.compile(
    '^e(?P<evnt>\d+)_'
    's(?P<digi>\d+)_'
    's(?P<digimerge>\d+)_'
    'r(?P<reco>\d+)_'
    'r(?P<recomerge>\d+)$')

DAOD_TAG_PATTERN = re.compile(
    '^e(?P<evnt>\d+)_'
    's(?P<digi>\d+)_'
    's(?P<digimerge>\d+)_'
    'r(?P<reco>\d+)_'
    'r(?P<recomerge>\d+)_'
    'p(?P<derivation>\d+)$')

"""
# MC[15|16][a|b|c|...] categories are defined here
# Each MC dataset is automatically classified
# acccording to these categories by matching the reco
# and merge tags of the dataset name.
# Order by decreasing preference:
"""

MC_CATEGORIES = {
    'mc15a': {'reco': (6768, 6765, 6725, 6771, 7042, 7049, 7051, 6869, 7509),
              'merge': (6282,)},
    'mc15b': {'reco': (7267, 7326, 7360),
              'merge': (6282,)},
    'mc15c': {'reco': (7772, 7725),
              'merge': (7676,)},

# https://twiki.cern.ch/twiki/bin/view/AtlasProtected/AtlasProductionGroupMC16    
    'mc16a': {'reco': (9364,),
              'merge': (9294, 9315)},
    'mc16b': {'reco': (),
              'merge': ()},
    'mc16c': {'reco': (9781,),
              'merge': (9778, 10009)},
    'mc16d': {'reco': (10201,),
              'merge': (10210,)},
    'mc16e': {'reco': (10724),
              'merge': (10726)},
    'mc16f': {'reco': (),
              'merge': ()}
}


HERE = os.path.dirname(os.path.abspath(__file__))

# Any datasets which don't have the provenance stored properly in AMI
# should be hardcoded here (it happens)
DS_NOPROV = {}

# Cross-sections are cached so that we don't need to keep asking AMI
# for them over and over
XSEC_FILE = os.path.join(HERE, 'xsec',"13TeV.txt")
XSEC_CACHE_FILE = os.path.join(HERE, 'xsec', 'xsec.pkl')
XSEC_CACHE_MODIFIED = False
XSEC_CACHE = {}
if os.path.isfile(XSEC_CACHE_FILE):
    with open(XSEC_CACHE_FILE) as cache:
        log.info("Loading cross sections from %s ..." % XSEC_CACHE_FILE)
        XSEC_CACHE = pickle.load(cache)


# some named ntuples 
Namedset = namedtuple('Namedset','name tags meta properties')
Dataset = namedtuple('Dataset',Namedset._fields + ('datatype',))
Fileset = namedtuple('Fileset',Dataset._fields + ('files', 'treename'))
ATLASFileset = namedtuple('ATLASFileset',Fileset._fields + ('year', 'grl',))

##--------------------------------------------------------------------------------
## 
class DoesNotExist(Exception):
    pass

##--------------------------------------------------------------------------------
## 
class Fileset(Fileset):
    def split(self, partitions):
        files = self.files[:]
        fileset_files = [[] for _ in xrange(partitions)]
        while len(files) > 0:
            for fileset in fileset_files:
                if len(files) > 0:
                    fileset.append(files.pop(0))
                else:
                    break
        mydict = self._asdict()
        filesets = []
        for fileset in fileset_files:
            mydict['files'] = fileset
            filesets.append(Fileset(**mydict))
        return filesets


##--------------------------------------------------------------------------------
## 
class Treeset(namedtuple('Treeset', Dataset._fields + ('trees',))):

    def GetEntries(self, *args, **kwargs):
        return sum([tree.GetEntries(*args, **kwargs) for tree in self.trees])

    def Scale(self, value):
        for tree in self.trees:
            tree.Scale(value)

    def __iter__(self):
        for tree in self.trees:
            yield tree

    def Draw(self, *args, **kwargs):
        for tree in self.trees:
            tree.Draw(*args, **kwargs)

##--------------------------------------------------------------------------------
## 
class Database(dict):
    """ base class for Database utils

    Attributes
    ----------
    name: str, 
      
    verbose: bool,
      
    stream: out stream (default=sys.stdout)
    """
    @classmethod
    def match_to_ds(cls, match):
        """
        Construct the original NTUP dataset name from a skim match object
        """
        return '%s%s_%sTeV.%s.%s.%s.%s' % (
                match.group('type'),
                match.group('year'),
                match.group('energy'),
                match.group('id'),
                match.group('name'),
                match.group('stream'),
                match.group('tag'))

    def __init__(self, name='DB', version="", verbose=False, stream=sys.stdout, log_level="INFO"):
        super(Database, self).__init__()
        self.name = name
        self.verbose = verbose
        self.stream = stream
        self.version = version
        log.setLevel(log_level)
        log.debug("Initialzing Database ...")

        # - - - - - - - - where to put the database yml file
        self.filepath = os.path.join(HERE, 'DataBase/%s%s.yml' % (self.name, self.version))
        if os.path.isfile(self.filepath):
            with open(self.filepath) as db:
                log.info("Loading database '%s' ..." % self.filepath)
                d = yaml.load(db)
                if d:
                    self.update(d)
        self.modified = False

    def write(self):
        """ write database to yml file
        """
        if self.modified:
            with open(self.filepath, 'w') as db:
                log.info("Saving database '%s' ..." % self.name)
                yaml.dump(dict(self), db)
    def reset(self):
        """cleanup
        """
        return self.clear()

    def clear(self):
        """erase all datasets in database
        """
        log.info("Resetting database '%s' ..." % self.name)
        super(Database, self).clear()
        self.modified = True

    def validate(self,
                 pattern=None,
                 datatype=None,
                 year=None):

        """ check if dataset is complete 
        """
        ds = {}
        for name, info in self.items():
            if datatype is not None and info.datatype != datatype:
                continue
            if year:
                if datatype==0 and int(info.stream) != int(year):
                    continue
                if datatype==1 and (not int(year) in [int(s) for s in info.stream]):
                    continue
                
            if info.datatype == DATA and info.id < 0:
                # only validate data run datasets
                continue
            if pattern is None or fnmatch.fnmatch(name, pattern):
                ds[name] = info
        incomplete = []
        pool = Pool(processes=cpu_count())
        for result, complete in pool.map_async(
                validate_single, sorted(ds.items(), key=itemgetter(0))).get(36000):
           print result
           print "Complete: %s" % complete
           print '-'*50
           if not complete:
               all_complete = False
               incomplete.append(result)
        if not incomplete:
            log.info("ALL DATASETS ARE COMPLETE")
        else:
            log.warning("SOME DATASETS ARE NOT COMPLETE:")
            for ds in incomplete:
                print ds
        return None
    
    def scan(self, year,
             mc_path=None,
             mc_prefix=None,
             mc_pattern=None,
             mc_treename=None,
             mc_sampletype=None,
             data_path=None,
             data_prefix=None,
             data_pattern=None,
             data_treename=None,
             data_sampletype=None,
             data_grl=None,
             data_period_containers=False,
             embed_path=None,
             embed_prefix=None,
             embed_pattern=None,
             embed_treename=None,
             embed_sampletype=None,
             versioned=False,
             deep=False):
        """
        Update the dataset database
        """
        log.info("Updating database '%s' ..." % self.name)
        self.modified = True

        # - - - - - - - - MC
        log.info('--------------------------------> MC')
        if mc_path is not None:
            if deep:
                mc_dirs = get_all_dirs_under(mc_path, prefix=mc_prefix)
            else:
                if mc_prefix:
                    mc_dirs = glob.glob(os.path.join(mc_path, mc_prefix) + '*')
                else:
                    mc_dirs = glob.glob(os.path.join(mc_path, '*'))
            for dir in mc_dirs:
                log.debug(dir)
                dirname, basename = os.path.split(dir)
                match  = re.match(NTUP_PATTERN, basename)                
                if match:
                    if match.group('type') != 'mc':
                        continue
                    dsid = match.group('id')
                    # - - - - get the name from XS file (due to Grid limitations ntuples names are shortend)
                    name = Dataset.get_name(dsid)
                    stream = "mc%s"%match.group('stream')
                    tag = match.group("tag")#re.search("\.e\w+", basename).group()
                    rtag = tag.split("_")[-2].replace("r", "")
                    version = match.group("version")
                    tag_match = None
                    if tag_match:
                        reco_tag = int(tag_match.group('reco'))
                        if reco_tag in MC_CATEGORIES['mc15a']['reco']:
                            cat = 'mc15a'
                        elif reco_tag in MC_CATEGORIES['mc15b']['reco']:
                            cat = 'mc15b'
                        else:
                            cat = 'mc15'
                    else:
                        cat = 'mc16'
                    log.debug((dsid,name, tag, version))

                    ## - - make name unique for different MC campaigns
                    uname = "%s_%s"%(name, rtag)

                    ## - - set stream to data streams based on reco tag
                    if rtag in ["9315", "9364"]:
                        stream = ["2015", "2016"]
                    elif rtag in ["10210", "10201"]:
                        stream = ["2017"]
                    elif rtag in ["10724", "10726"]:
                        stream = ["2018"]    
                    else:
                        log.warning("unknown reco tag %s"%rtag)
                        
                    # - - - - - - - - update the DB with this dataset
                    dataset = self.get(uname, None)
                    if dataset is not None and version == dataset.version:
                        if dir not in dataset.dirs:
                            dataset.dirs.append(dir)
                    else:
                        m_ds = Dataset(
                            name=uname, 
                            datatype=MC,
                            treename=mc_treename,
                            ds=name,
                            ntup_name=basename,
                            id=int(match.group('id')),
                            version=version,
                            tag_pattern=None,
                            tag=rtag,
                            dirs=[dir],
                            file_pattern=mc_pattern,
                            year=year,
                            stream=stream)
                        ## cache some heavy properties here
                        m_ds.files = sorted(m_ds.get_files())

                        ## if a dataset has more than N_DS_FILES files then break it to some sub-datasets in order to boost the analysis
                        num_files = len(m_ds.files)
                        if num_files == 0:
                            # raise NameError("No files were found for %s"%(m_ds.name))
                            log.warning("No files were found for %s"%(m_ds.name))
                        elif  num_files > N_DS_FILES:
                            sub_dss = []
                            log.info("Breaking %s dataset to %i sub-datasets ..."%(uname, 1+num_files/N_DS_FILES))
                            cnt = 0 
                            nf = 1
                            while cnt <= num_files:
                                files = m_ds.files[cnt:cnt+N_DS_FILES]
                                cnt += N_DS_FILES
                                ## now create sub-datasets
                                sub_uname = m_ds.name+"__"+str(nf).zfill(3)
                                nf +=1 
                                s_ds = Dataset(
                                    name=sub_uname, 
                                    datatype=MC,
                                    treename=mc_treename,
                                    ds=name,
                                    ntup_name=basename,
                                    id=int(match.group('id')),
                                    version=version,
                                    tag_pattern=None,
                                    tag=rtag,
                                    dirs=[dir],
                                    file_pattern=mc_pattern,
                                    year=year,
                                    stream=stream)
                                
                                s_ds.files = files
                                s_ds.events = s_ds.get_events()
                                s_ds.xsec_kfact_effic = s_ds.get_xsec_kfact_effic()
                                sub_dss += [s_ds]
                                self[sub_uname] = s_ds
                                log.debug(s_ds)

                            ## LUMI weight: 1/w = 1/w1 + 1/w2 + 1/w3 + ...
                            lumi_weight = 1./(sum([float(d.events)/d.xsec_kfact_effic for d in sub_dss])) 
                            
                            for sd in sub_dss:
                                sd.lumi_weight = lumi_weight
                            log.info("LUMI weight: {}".format(lumi_weight))
                        else:
                            m_ds.events = m_ds.get_events()
                            m_ds.xsec_kfact_effic = m_ds.get_xsec_kfact_effic()
                            if m_ds.events!=0:
                                m_ds.lumi_weight = m_ds.xsec_kfact_effic/float(m_ds.events)
                            self[uname] = m_ds

                        log.info(m_ds)
                else:
                    log.info("No match for %s, %s" %(NTUP_PATTERN, basename))

        # - - - - - - - - DATA
        log.info('--------------------------------> DATA')
        if data_path is not None:
            if deep:
                data_dirs = get_all_dirs_under(data_path, prefix=data_prefix)
            else:
                if data_prefix:
                    data_dirs = glob.glob(os.path.join(data_path, data_prefix) + '*_BS')
                else:
                    data_dirs = glob.glob(os.path.join(data_path, '*'))

            # classify dir by stream
            streams = {}
            for dir in data_dirs:
                log.debug(dir)
                dirname, basename = os.path.split(dir)
                match = re.match(NTUP_PATTERN, basename)
                if match:
                    if match.group('type') != 'data':
                        continue
                    stream = "20%s"%match.group('stream')
                    run = match.group('id')
                    name = match.group('name')
                    tag = match.group('tag')
                    version = match.group('version')
                    tag_match = None
                    # - - - - - - - data dirs per stream
                    if not ("%s-Main"%year in streams):
                        streams["%s-Main"%year] = []
                    streams['%s-Main'%year].append(dir)

                    name = 'DATA%s_%s' % (stream, match.group('id'))
                    
                    # add datasets to the database
                    d_ds = Dataset(
                        name=name,
                        datatype=DATA,
                        treename=data_treename,
                        ds=name,
                        ntup_name=basename,
                        id=run,
                        grl=None,#data_grl,
                        dirs=[dir],
                        stream=stream,
                        tag=tag,
                        version=version,
                        file_pattern=data_pattern,
                        year=year)

                    ## cache some heavy properties  
                    d_ds.files = d_ds.get_files()
                    d_ds.events = -1 #d_ds.get_events() 
                    d_ds.xsec_kfact_effic = 1.

                    self[name] = d_ds
                    
                    log.info(d_ds)

    def __setitem__(self, name, ds):
        super(Database, self).__setitem__(name, ds)

    def search(self, pattern):
        data = []
        patterns = pattern
        if not isinstance(pattern, (list, tuple)):
            patterns = [pattern]
        for name, ds in self.items():
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    data.append(ds)
                    continue
                if not pattern.startswith('^'):
                    pattern = '^' + pattern
                if not pattern.endswith('$'):
                    pattern = pattern + '$'
                if re.match(pattern, name):
                    data.append(ds)
                    continue
        return data
    
    def query(self, name=None, did=None, ds=None, streams=[]):
        """
        """
        datasets = []
        if ds:
            keys = filter(lambda k: ds in k, self.keys())
        else:
            keys = self.keys()

        for nkey in keys:
            info = self[nkey]
            keep = True
            if name:
                keep &= (name==nkey)
            if did:
                keep &= (info.id==did)
            if ds:
                keep &= (info.ds==ds)
            if streams:
                for st in info.stream:
                    keep &= (st in streams)
            if keep:
                datasets += [self[nkey]]

        if not datasets or (len(datasets) < len(streams)-1):
            log.warning("Missing stream for {}: {}".format(name if name else ds, [k.name for k in datasets]))
            
        return datasets
    
##--------------------------------------------------------------------------------
## 
class Dataset(Serializable):
    
    yaml_tag = u'!Dataset'

    @classmethod
    def get_name(cls, dsid):
        """ get name of a dsid from the xsec file
        if the dsid is missing in the xsec file, give a tmp name and throw a warning.
        """
        with open(XSEC_FILE, "r") as xsec_file:
            lines = filter(lambda l: l[0].isdigit(), xsec_file.readlines())
            
        name = None
        for l in lines:
            if str(dsid)==l.split()[0]:
                name = l.split()[1]
        if not name:
            log.warning("MISSING %s dataset in %s XS file"%(dsid, XSEC_FILE))
            name = "MISSING_IN_XS_%s"%dsid
        return name 
    
    def __init__(self, name, datatype, treename, ds, dirs,
                 ntup_name="",
                 file_pattern='*.root*',
                 id=None,
                 category=None,
                 version=None,
                 tag_pattern=None,
                 tag=None,
                 grl=None,
                 year=None,
                 stream=None, 
                 files=[], 
                 events=0,
                 xsec_kfact_effic=(1., 1., 1.),
                 lumi_weight = None, 
                 ):
        self.name = name
        self.ntup_name = ntup_name
        self.datatype = datatype
        self.treename = treename
        self.id = id
        self.ds = ds
        self.category = category
        self.version = version
        self.tag_pattern = tag_pattern
        self.tag = tag
        self.dirs = dirs
        self.file_pattern = file_pattern
        self.grl = grl
        self.year = year
        self.stream = stream
        self.files = files
        self.events = events
        self.xsec_kfact_effic = xsec_kfact_effic
        self.lumi_weight = lumi_weight

    @cached_property
    def weight(self):
        if self.events !=0:
            return reduce(lambda x,y:x*y, self.xsec_kfact_effic) / self.events
        else:
            log.warning(" 0 lumi weight for %s"%self.name)
            return 0.

    @classmethod
    def count_raw_events(cls, rfile):
        rf = ROOT.TFile("f", "READ")
        events_cutflow_hist = EVENTS_CUTFLOW_HIST[MC_CAMPAIGN]
        events_cutflow_bin = EVENTS_CUTFLOW_BIN[MC_CAMPAIGN]
        return 

    def get_events(self,
        events_cutflow_hist = EVENTS_CUTFLOW_HIST[MC_CAMPAIGN],
        events_cutflow_bin = EVENTS_CUTFLOW_BIN[MC_CAMPAIGN]):
        nevents = 0
        assert (events_cutflow_hist and events_cutflow_bin), "metadata hist info is not provided!"
        for f in self.files:
            rf = ROOT.TFile(f, "READ")
            ## checking ig aux hists are written to a different file
            if not events_cutflow_hist in [k.GetName() for k in rf.GetListOfKeys()]:
                sdir, fname = os.path.split(f)
                if sdir.endswith("_BS"):
                    f = os.path.join(sdir.replace("_BS", "_hist"), fname.replace(".BSM_Hptaunu.", ".hist-output."))
                if not os.path.isfile(f):
                    log.warning("can't retrieve hmetadata (skipping!); missing %s"%f)
                    continue

                ## close the open file and open the one with aux hists    
                rf.Close()    
                rf = ROOT.TFile(f, "READ")

            ## retrieve aux hists     
            hmetadata = rf.Get(events_cutflow_hist)
            num = hmetadata.GetBinContent(events_cutflow_bin)
            log.debug("%s, #events: %i"%(f, num))
            nevents += num
            rf.Close()
        return nevents
    
    def get_xsec_kfact_effic(self):
        global XSEC_CACHE_MODIFIED
        global XSEC_CACHE
        year = int(self.year) % 1E3
        if self.name is None:
            log.warning("there's a NONE dataset in the database!")
            xsec = (1., 1., 1.)
        if self.datatype == DATA:
             xsec = (1.,1., 1.)
        elif year in XSEC_CACHE and self.id in XSEC_CACHE[year]:
            log.debug("using cached cross section for dataset %s" % self.ds)
            xsec = XSEC_CACHE[year][self.id]
        else:
            try:
                XSEC_CACHE[year] = {}
                # - - - - cache XSEC 
                with open(XSEC_FILE, "r") as xfile:
                    for line in xfile:
                        line.strip()
                        if line[0].isdigit():
                            line = line.split()
                            XSEC_CACHE[year][int(line[0])] = (float(line[2]),
                                                            float(line[3]), float(line[4]))
                XSEC_CACHE_MODIFIED = True
                xsec = XSEC_CACHE[year][self.id]
            
            except KeyError:
                log.warning("cross section of dataset %s not available; setting it to 1.!!!"%self.ds)
                xsec = (1.,1., 1.)

        return reduce(lambda x, y: x*y, xsec)

    def get_files(self):
        if not self.dirs:
            log.warning(
                "files requested from dataset %s "
                "with an empty list of directories" % self.name)
        _files = []
        for dir in self.dirs:
            if not os.path.exists(dir):
                raise IOError("%s is not readable" % dir)
            for path, dirs, files in os.walk(dir):

                try:
                    _files += [os.path.realpath(os.path.join(path, f)) for f in
                           fnmatch.filter(files, self.file_pattern)]
                    log.debug("Found symlink for %s! Using absolute real path for files." %(path))
                except:
                    _files += [os.path.join(path, f) for f in
                               fnmatch.filter(files, self.file_pattern)]
        return _files
    
    def __repr__(self):
        return ("%s(name=%r, ntup_name=%r, datatype=%r, treename=%r, "
                "id=%r, ds=%r, category=%r, version=%r, "
                "tag_pattern=%r, tag=%r, dirs=%r, "
                "file_pattern=%r, grl=%r, year=%r, " 
                "stream=%r, files=%r, events=%r, xsec_kfact_effic=%r)") % (
                    self.__class__.__name__,
                    self.name, self.ntup_name, self.datatype, self.treename,
                    self.id, self.ds, self.category, self.version,
                    self.tag_pattern, self.tag, self.dirs,
                    self.file_pattern, self.grl, self.year,
                    self.stream, self.files, self.events, self.xsec_kfact_effic)
    def __str__(self):
        return "%s (%d files):\n\t%s" % (
                self.name,
                len(self.files),
                self.ds)

##--------------------------------------------------------------------------------
## 
def dataset_constructor(loader, node):
    kwargs = loader.construct_mapping(node)
    try:
        return Dataset(**kwargs)
    except:
        fields = '\n'.join('%s = %s' % item for item in kwargs.items())
        log.error("unable to load dataset %s with these fields:\n\n%s\n" %
                  (kwargs['name'], fields))
        raise

yaml.add_constructor(u'!Dataset', dataset_constructor)


##--------------------------------------------------------------------------------
## 
@atexit.register
def write_cache():
    if XSEC_CACHE_MODIFIED:
        with open(XSEC_CACHE_FILE, 'w') as cache:
            log.info("Saving cross-section cache to disk...")
            pickle.dump(XSEC_CACHE, cache)


##--------------------------------------------------------------------------------
## 
def validate_single(args, child=False):
    """

    """
    
    
    if child:
        from cStringIO import StringIO
        sys.stdout = out = StringIO()
        sys.stderr = out
    name = args[0]
    info = args[1]
    complete = True
    log.info("Validating %s . . ."%name )
    
    try:
        dirs = info.dirs
        root_files = []
        for dir in dirs:
            if not METADATA_TTREE_MERGED:
                if dir.endswith("_BS"):
                    root_files += glob.glob(os.path.join(dir.replace("_BS", "_hist"), "*.hist-output.*"))
            else:    
                root_files += glob.glob(os.path.join(dir, info.file_pattern))

        events = 0
        AOD_events = 0
        parent_dAOD = None
        for fname in root_files:
            try:
                rfile = ROOT.TFile(fname, "READ")
                if not parent_dAOD:
                    EL_tree = rfile.Get("EventLoop_FileExecuted")
                    for n, evt, in enumerate(EL_tree):
                        parent_dAOD = str(evt.file) 
                    
                try: # skimmed dataset
                    events += int(rfile.Get(EVENTS_CUTFLOW_HIST[MC_CAMPAIGN]).GetBinContent(2) )
                    AOD_events += int(rfile.Get(EVENTS_CUTFLOW_HIST[MC_CAMPAIGN]).GetBinContent(7) )
                except DoesNotExist: # unskimmed dataset
                    tree = rfile.NOMINAL
                    events += tree.GetEntries()
                rfile.Close()
            except IOError:
                log.warning("Currupt file: %s" % fname)
                pass
            
        ## determine events in original ntuples
        ds_name = info.name
        # log.info(get_file(amiclient, parent_dAOD))
        ds_logical_name  = get_file(amiclient, parent_dAOD)[0]["logicalDatasetName"]
        
        ds_info = get_dataset_info(amiclient, ds_logical_name)[0]
        dAOD_events = int(ds_info['totalEvents'])

        ## quick check to see if all dAODs were fully processed 
        # if ds_info["taskStatus_0"]!="DONE":
        #     log.warning("INCOMPLETE dAOD!")
        try:
            ## determine events in AODs
            prov = get_dataset_prov(amiclient, ds_logical_name)
            log.info('AOD: ' + prov["node"][1]["logicalDatasetName"])
            original_AOD_events = int(prov["node"][1]["events"])
        except IndexError:
            log.info('AOD: UNKNOWN')
            AOD_events = dAOD_events
        log.info('dAOD: ' + ds_logical_name)
        log.info("NTUP: " + info.ntup_name)
        log.info("\tNTUP\tdAOD\tAOD")
        log.info("\t%i\t%i\t%i" % (events, dAOD_events, original_AOD_events))
        if events != dAOD_events:
            log.warning("NTUP MISMATCH! (AMI dAOD, NTUP metadata): (%i, %i)"%(dAOD_events, events))
        if original_AOD_events != AOD_events:
            log.warning("AOD MISMATCH! (AMI AOD, NTUP metadata): (%i, %i)"%(original_AOD_events, AOD_events))
        if events != dAOD_events and (original_AOD_events != AOD_events or AOD_events == 0):
            log.warning("MISSING EVENTS")
            complete = False
        log.info("-"*50)
        if child:
            return out.getvalue(), complete
        return ds_name, complete
    except Exception, e:
        import traceback
        log.warning("dataset %s exception" % name)
        traceback.print_exception(*sys.exc_info())
        if child:
            return out.getvalue(), False
        return False


##--------------------------------------------------------------------------------
## 
def get_all_dirs_under(path, prefix=None):
    """
    Get list of all directories under path
    """
    dirs = []
    for dirpath, dirnames, filenames in os.walk(path):
        _dirnames = []
        for dirname in dirnames:
            fullpath = os.path.join(dirpath, dirname)
            # check if this dir contains other dirs
            subdirs_exist = False
            subdirs = os.listdir(fullpath)
            for subdir in subdirs:
                if os.path.isdir(os.path.join(fullpath, subdir)):
                    subdirs_exist = True
                    break
            if subdirs_exist:
                _dirnames.append(dirname)
            else:
                # this must be a dataset, don't walk into this dir
                if prefix is not None:
                    if not dirname.startswith(prefix):
                        continue
                dirs.append(fullpath)
        # only recurse on directories containing subdirectories
        dirnames = _dirnames
    return dirs
