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

# ROOT
import ROOT

# PyPI
import yaml

# local
from . import log
from .decorators import cached_property
from .yaml_utils import Serializable
from . import xsec
from .. import EVENTS_CUTFLOW_HIST, EVENTS_CUTFLOW_BIN, MC_CAMPAIGN 

# ATLAS 
USE_PYAMI = False
try:
    from pyAMI.client import AMIClient
    from pyAMI.query import get_dataset_xsec_effic, \
                            get_dataset_info, \
                            get_datasets, \
                            get_provenance, \
                            get_periods, \
                            get_runs
    from pyAMI import query
    from pyAMI.auth import AMI_CONFIG, create_auth_config
except ImportError:
    USE_PYAMI = False
    log.warning("pyAMI is not installed. "
                "Cross section retrieval will be disabled.")

##--------------------------------------------------------------------------------
## consts
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

## deprecated ! used for 18v01 production 
# MC_NTUP_PATTERN= re.compile(
#     '^(?P<prefix>(group.phys-higgs|user))'
#     '\.(?P<uname>\w+)'
#     '\.(mc16_13TeV)'
#     '\.(?P<id>\d+)'
#     '\.(?P<name>\w+)'
#     '\.(?P<derivation>\w+)'
#     '\.(?P<tag>\w+)'
#     '\.(?P<version>\w+)'
#     '\_hist$')

# DATA_NTUP_PATTERN = re.compile(
#     '^(?P<prefix>(group.phys-higgs|user))'
#     '\.(?P<uname>\w+)'
#     '\.(?P<jo>\w+)'
#     '\.(?P<id>\d+)'
#     '\.(?P<tag>\w+)'
#     '\.(?P<suffix>\w+)$'
# )

NTUP_PATTERN_2018 = re.compile(
    '^(?P<prefix>(group.phys-higgs|user))'
    '\.(?P<uname>\w+)'
    '\.((mc16|data(15|16|17|18))_13TeV)'
    '\.(?P<id>\d+)'
    '\.(?P<name>\w+)'
    '\.(?P<derivation>\w+)'
    '\.(?P<tag>\w+)'
    '\.(?P<version>\w+)'
    '\_hist$')



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
    'mc16e': {'reco': (),
              'merge': ()},
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
        log.info("Loading cross section cache in %s ..." % XSEC_CACHE_FILE)
        XSEC_CACHE = pickle.load(cache)

if USE_PYAMI:
    amiclient = AMIClient()
    if not os.path.exists(AMI_CONFIG):
        create_auth_config()
    amiclient.read_config(AMI_CONFIG)



# some named ntuples 
Namedset = namedtuple('Namedset','name tags meta properties')
Dataset = namedtuple('Dataset',Namedset._fields + ('datatype',))
Fileset = namedtuple('Fileset',Dataset._fields + ('files', 'treename'))
ATLASFileset = namedtuple('ATLASFileset',Fileset._fields + ('year', 'grl',))
    
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

    def __init__(self, name='datasets', version="", verbose=False, stream=sys.stdout):
        super(Database, self).__init__()
        self.name = name
        self.verbose = verbose
        self.stream = stream
        self.version = version
        
        # - - - - - - - - where to put the database yml file
        self.filepath = os.path.join(HERE, '%s%s.yml' % (self.name, self.version))
        if os.path.isfile(self.filepath):
            with open(self.filepath) as db:
                log.info("Loading database '%s' ..." % self.name)
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
            if year is not None and info.year != year:
                continue
            if datatype is not None and info.datatype != datatype:
                continue
            if info.datatype == DATA and info.id < 0:
                # only validate data run datasets
                continue
            if pattern is None or fnmatch.fnmatch(name, pattern):
                ds[name] = info
                
        incomplete = []
        for name, info in sorted(ds.items(), key=lambda item: item[0]):
            log.info("Validating %s ..." % name)
            complete = validate_single((name, info), child=False)
            log.info("Complete: %s" % complete)
            log.info('-' * 50)
            if not complete:
                incomplete.append(info.ds)
        #pool = Pool(processes=cpu_count())
        #for result, complete in pool.map(
        #        validate_single, sorted(ds.items(), key=itemgetter(0))):
        #    print result
        #    print "Complete: %s" % complete
        #    print '-'*50
        #    if not complete:
        #        all_complete = False
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
                match  = re.match(NTUP_PATTERN_2018, basename)
                if match:
                    #FIXME: tmp hack  - - - - - - - -  get dataset name from dsid file/ if not available in here
                    # if match.group('type') != 'mc':
                    #     continue
                    try:
                        dsid = match.group('id')
                        name = match.group('name')
                        stream = None #match.group('stream')
                        tag = match.group('tag')
                        version = match.group('version')
                        tag_match = None
                        
                    except:
                        dsid = match.group('id')
                        name = Dataset.get_name(dsid)
                        stream = None #match.group('stream')
                        tag = None
                        version = None
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
                    log.debug((dsid,name, tag, cat, version))

                    # - - - - - - - - update the DB with this dataset
                    dataset = self.get(name, None)
                    if dataset is not None and version == dataset.version:
                        if dir not in dataset.dirs:
                            dataset.dirs.append(dir)
                    else:
                        self[name] = Dataset(
                            name=name,
                            datatype=MC,
                            treename=mc_treename,
                            ds=name,
                            id=int(match.group('id')),
                            category=cat,
                            version=version,
                            tag_pattern=None,
                            tag=tag,
                            dirs=[dir],
                            file_pattern=mc_pattern,
                            year=year,
                            stream=stream)


        # - - - - - - - - EMBEDDING
        if embed_path is not None:
            log.warning('Not ready yet!')

        # - - - - - - - - DATA
        log.info('--------------------------------> DATA')
        if data_path is not None:
            if deep:
                data_dirs = get_all_dirs_under(data_path, prefix=data_prefix)
            else:
                if data_prefix:
                    data_dirs = glob.glob(os.path.join(data_path, data_prefix) + '*')
                else:
                    data_dirs = glob.glob(os.path.join(data_path, '*'))

            # classify dir by stream
            streams = {}
            for dir in data_dirs:
                log.debug(dir)
                dirname, basename = os.path.split(dir)
                match = re.match(NTUP_PATTERN_2018, basename)
                if match:
                    try:
                        if match.group('type') != 'data':
                            continue
                        stream = match.group('name').split('_')[-1]
                        year = match.group('year')
                    except:
                        run = match.group('id')
                        run = int(run[2:]) #< drop 00 prefix
                        if DATA15_RUNS_RANGE[0] <= run <= DATA15_RUNS_RANGE[-1]:
                            stream = "2015"
                            year = "2015"
                        elif DATA16_RUNS_RANGE[0] <= run <= DATA16_RUNS_RANGE[-1]:
                            stream = "2016"
                            year = "2016"
                        elif DATA17_RUNS_RANGE[0] <= run <= DATA17_RUNS_RANGE[-1]:
                            stream = "2017"
                            year = "2017"
                        else:
                            log.error("unknown data run 00%i"%run)
                    # - - - - - - - data dirs per stream
                    if not ("%s-Main"%year in streams):
                        streams["%s-Main"%year] = []
                    streams['%s-Main'%year].append(dir)

                    # elif self.verbose:
                    #     log.warning(
                    #         "not a valid data dataset name: %s" % basename)
                    
                    #for stream, dirs in streams.items():
                    name = 'DATA%s_%s' % (stream, match.group('id'))
                    
                    # add datasets to the database
                    self[name] = Dataset(
                        name=name,
                        datatype=DATA,
                        treename=data_treename,
                        ds=name,
                        id=-1,
                        grl=None,#data_grl,
                        dirs=[dir],
                        stream=stream,
                        file_pattern=data_pattern,
                        year=year)

    def __setitem__(self, name, ds):
        # if self.verbose:
        #     print >> self.stream, str(ds)
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


##--------------------------------------------------------------------------------
## 
class Dataset(Serializable):
    
    yaml_tag = u'!Dataset'

    @classmethod
    def get_name(cls, dsid):
        """ get name of a dsid from the xsec file
        """
        with open(XSEC_FILE, "r") as xsec_file:
            lines = filter(lambda l: l[0].isdigit(), xsec_file.readlines())
        for l in lines:
            if str(dsid)==l.split()[0]:
                return l.split()[1]
        
    def __init__(self, name, datatype, treename, ds, dirs,
                 file_pattern='*.root*',
                 id=None,
                 category=None,
                 version=None,
                 tag_pattern=None,
                 tag=None,
                 grl=None,
                 year=None,
                 stream=None):
        self.name = name
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
        
    @cached_property
    def lumi_weight(self):
        if self.events !=0:
            return reduce(lambda x,y:x*y, self.xsec_kfact_effic) / self.events
        else:
            log.warning(" 0 lumi weight for %s"%self.name)
            return 0.
        
    @cached_property
    def events(self,
               events_cutflow_hist=EVENTS_CUTFLOW_HIST[MC_CAMPAIGN],
               events_cutflow_bin=EVENTS_CUTFLOW_BIN[MC_CAMPAIGN]):
        nevents = 0
        assert (events_cutflow_hist and events_cutflow_bin), "metadata hist info is not provided!"
        for f in self.files:
            rf = ROOT.TFile(f, "READ")
            hmetadata = rf.Get(events_cutflow_hist)
            num = hmetadata.GetBinContent(events_cutflow_bin)
            log.debug("%s, #events: %i"%(f, num))
            nevents += num
            rf.Close()
        return nevents
    
    @cached_property
    def xsec_kfact_effic(self):
        global XSEC_CACHE_MODIFIED
        global XSEC_CACHE
        year = int(self.year) % 1E3
        if self.datatype == DATA:
            return 1., 1., 1.
        if year in XSEC_CACHE and self.id in XSEC_CACHE[year]:
            log.debug("using cached cross section for dataset %s" % self.ds)
            return XSEC_CACHE[year][self.id]
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
            return XSEC_CACHE[year][self.id]
        
        except KeyError:
            log.warning("cross section of dataset %s not available locally. "
                        "Looking it up in AMI instead. AMI cross sections can be very"
                        "wrong! You have been warned!"
                        % self.ds)
        if USE_PYAMI:
            if self.ds in DS_NOPROV:
                xs, effic = get_dataset_xsec_effic(amiclient, DS_NOPROV[self.ds])
            else:
                xs, effic = get_dataset_xsec_effic(amiclient, self.ds)
            if year not in XSEC_CACHE:
                XSEC_CACHE[year] = {}
            XSEC_CACHE[year][self.name] = (xs, 1., effic)
            XSEC_CACHE_MODIFIED = True
            return xs, 1., effic
        
        if self.name is None:
            log.warning("there's a NONE dataset in the database!")
            return 1., 1., 1.
        raise Exception("cross section of dataset %s is not known!" % self.ds)
    
    @cached_property
    def files(self):
        if not self.dirs:
            log.warning(
                "files requested from dataset %s "
                "with an empty list of directories" % self.name)
        _files = []
        for dir in self.dirs:
            if not os.path.exists(dir):
                raise IOError("%s is not readable" % dir)
            for path, dirs, files in os.walk(dir):
                _files += [os.path.join(path, f) for f in
                           fnmatch.filter(files, self.file_pattern)]
        return _files
    
    def __repr__(self):
        return ("%s(name=%r, datatype=%r, treename=%r, "
                "id=%r, ds=%r, category=%r, version=%r, "
                "tag_pattern=%r, tag=%r, dirs=%r, "
                "file_pattern=%r, grl=%r, year=%r, " 
                "stream=%r, files=%r, events=%r, xsec_kfact_effic=%r)") % (
                    self.__class__.__name__,
                    self.name, self.datatype, self.treename,
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
def validate_single(args, child=True):
    if child:
        from cStringIO import StringIO
        sys.stdout = out = StringIO()
        sys.stderr = out
    name = args[0]
    info = args[1]
    complete = True
    try:
        dirs = info.dirs
        root_files = []
        for dir in dirs:
            root_files += glob.glob(os.path.join(dir, info.file_pattern))
        events = 0
        for fname in root_files:
            try:
                with root_open(fname) as rfile:
                    try: # skimmed dataset
                        events += int(rfile.cutflow_event[0])
                    except DoesNotExist: # unskimmed dataset
                        tree = rfile.tau
                        events += tree.GetEntries()
            except IOError:
                log.warning("Currupt file: %s" % fname)
                pass
        # determine events in original ntuples
        # use first dir
        ds_name = info.ds
        log.info('NTUP: ' + ds_name)
        ds_info = get_dataset_info(amiclient, ds_name)
        ntuple_events = int(ds_info.info['totalEvents'])
        try:
            # determine events in AODs
            prov = get_provenance(amiclient, ds_name, type='AOD')
            AOD_ds = prov.values()[0][0].replace('recon', 'merge')
            log.info('AOD: ' + AOD_ds)
            AOD_events = int(get_datasets(amiclient, AOD_ds, fields='events',
                    flatten=True)[0][0])
        except IndexError:
            log.info('AOD: UNKNOWN')
            AOD_events = ntuple_events
        log.info(name)
        log.info("\tevts\tNTUP\tAOD")
        log.info("\t%i\t%i\t%i" % (events, ntuple_events, AOD_events))
        if events != ntuple_events:
            log.warning("NTUP MISMATCH")
        if events != AOD_events:
            log.warning("AOD MISMATCH")
        if events != ntuple_events and (events != AOD_events or AOD_events == 0):
            log.warning("MISSING EVENTS")
            complete = False
        if child:
            return out.getvalue(), complete
        return complete
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
