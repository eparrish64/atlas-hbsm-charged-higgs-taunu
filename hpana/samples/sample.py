# -*- coding: utf-8 -*-

# std lib imports
import os, sys, pickle, string, glob, copy, re 
from operator import add, itemgetter
from collections import namedtuple
import random 
import datetime
import multiprocessing

# ROOT imorts 
import ROOT

# local imports
from . import log

from ..db import samples as samples_db, datasets
from ..db.decorators import cached_property
from ..systematics import get_systematics, iter_systematics, systematic_name
from ..categories import TAU_IS_TRUE
from ..cluster.parallel import FuncWorker, run_pool, map_pool, Job


##---------------------------------------------------------------------------------------
## 
class Dataset(namedtuple('Dataset', ('ds','files', 'events'))):
    """ plain namedtuple to hold Dataset info
    """
    @property
    def name(self):
        return self.ds.name
    
##---------------------------------------------------------------------------------------
## 
class Histset:
    """simple container class for histograms
    """
    def __init__(self,
                 name="Histset",
                 sample=None,
                 variable=None,
                 category=None,
                 hist=None,
                 systematic="NOMINAL",):
        self.sample = sample
        self.name = name
        self.variable =variable
        self.category = category
        self.systematic = systematic
        self.hist = hist

    
    
##---------------------------------------------------------------------------------------
## 
class HistWorker:
    """
    lightweight container class for histogram workers
    """
    def __init__(self, name="HistWorker",
                 sample=None,
                 dataset=None,
                 systematic="NOMINAL",
                 fields=[],
                 categories=[],
                 weights=[]):
        self.name = name
        self.sample = sample
        self.dataset = dataset
        self.fields = fields
        self.categories = categories
        self.systematic = systematic
        self.weights = weights
        
    def __repr__(self):
        return "name=%r, sample=%r, systematic=%r\n"\
            "||variables||=%r\n||categories||=%r\n||weights||=%r\n"%(
                self.name, self.sample, self.systematic,
                self.fields, self.categories, self.weights)
        
        
##---------------------------------------------------------------------------------------
## 
class Sample(object):
    """
    base class for analysis samples.

    Attributes
    ----------
    config: 
        Configuration; see ../config.py 
    name: 
        string; sample's name
    label: 
        string; sample's lable (used for plotting, etc.) 
    """

    def __init__(self, config,
                 name='Sample',
                 label='Sample',
                 **kwargs):
        # - - - - - - - - passing main configurations to the sample
        self.config = config

        # - - - - - - - - minimal flags
        self.name = name
        self.label = label
        self.hist_name_template = kwargs.pop(
            "hist_name_template", self.config.hist_name_template)
        
        self.color = kwargs.get("color", 1)
        self.hist_decor = kwargs
        
    def decorate(self, name=None, label=None, **hist_decor):
        """update Sample object to decorate hists.
        Parameters
        ---------
        name: string; sample's name
        label: string; sample's lable.
        hist_decor: dict; more lables for drawing histograms.
        
        """
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if hist_decor:
            self.hist_decor.update(hist_decor)
        return self

    def cuts(self,
             category=None,
             trigger=None,
             tauid=None,
             extra_cuts=None,
             truth_match_tau=None,
             **kwargs):
        """ to apply some cuts on the sample.
        
        Parameters
        ----------
        category: Category object;

        region_cut: ROOT.TCut type, CR/SR region
        trigger_Cut: ROOT.TCut type
        systematic: str; systematics type.
      
        Returns
        -------
        cuts: ROOT.TCut object
        """

        cuts = ROOT.TCut("")
        if category:
            cuts += category.cuts
        if not trigger:
            cuts += self.config.trigger
        else:
            cuts += trigger
        
        # - - - - tauID (for fakes check fakes.py)
        if tauid:
            cuts += tauid
        else:
            cuts += self.config.tauid

        # - - - - truth matching (defualt it true tau)
        if truth_match_tau:
            cuts += truth_match_tau
        elif isinstance(self, MC):
            cuts += self.config.true_tau

        # - - - - place holder for any sample specific custs
        if extra_cuts:
            cuts += extra_cuts
            
        return cuts


    def weights(self, categories=[]):
        """ MC scale factors 
        """
        
        # - - - - - - - - MC common weights
        if not categories:
            categories = self.config.categories
        weights = {}
        for category in categories:
            weights[category.name] = self.config.weight_fields

        return weights
    
    @property
    def systematics(self):
        return ["NOMINAL"]
    
    def events(self, category,
               systematic="NOMINAL",
               **kwargs):
        """ get event counts using hists method
        """
        
        field = self.config.variables[0]
        hist_set =  self.hists(categories=[category],
                               fields=[field],
                               systematic=systematic,
                               **kwargs)

        hist = hist_set[0].hist
        # - - - - add the events from overflow bin too 
        nbins = hist.GetNbinsX() + 2
        nevents = hist.Integral(0, nbins)
        log.info("# of events from %s tree of %s sample in category %s: %0.4f"%(
            systematic, self.name, category.name, nevents))
        
        return nevents

    def workers(self, categories=[],
                fields=[],
                systematics=["NOMINAL"],
                extra_cuts=None,
                extra_weight=None,
                weighted=True,
                tauid=None,
                truth_match_tau=None,
                **kwargs):
        """ list of workers to to submit jobs.
        """
        # - - - - defensive copy 
        categories_cp = copy.deepcopy(categories)
        for category in categories_cp:
            # - - - - filters
            category.cuts += self.cuts(tauid=tauid, extra_cuts=extra_cuts, truth_match_tau=truth_match_tau)
            
        # - - - - one worker per dataset per systematic
        workers = []
        for ds in self.datasets:
            # - - selections and weights 
            weights = self.weights(categories=categories)
            for category in categories:
                # - - - - lumi, MC and extra weights  
                if weighted:
                    # - - lumi weight
                    if ds.events !=0:
                        lumi_weight = self.config.data_lumi * reduce(
                            lambda x,y:x*y, ds.xsec_kfact_effic) / ds.events
                    else:
                        log.warning(" 0 lumi weight for %s"%ds.name)
                        lumi_weight = 0
                    weights[category.name] += [str(lumi_weight)]

                    if extra_weight:
                        weights[category.name] += [extra_weight]
                else:
                    weights[category.name] = ["1."]
                    if extra_weight:
                        weights[category.name] += [extra_weight]
            
            # - - - - one worker per systematic per dataset
            for systematic in systematics:
                sname = self.name
                worker = HistWorker(
                    name="%s.%s.%s"%(sname, ds.name, systematic),
                    sample=self.name,
                    dataset=ds,
                    fields=fields,
                    categories=categories_cp,
                    weights=weights,
                    systematic=systematic,)
                
                workers.append(worker)

        return workers


    @staticmethod
    def dataset_hists(hist_worker,
                      outdir="histsdir",
                      **kwargs):
        """ produces histograms for a dataset. 
        This static method is mainly used for parallel processing.
        """
        dataset = hist_worker.dataset
        fields = hist_worker.fields
        categories = hist_worker.categories
        weights = hist_worker.weights
        systematic = hist_worker.systematic
        outname = kwargs.pop("outname", hist_worker.name)
        
        log.debug("*********** processing %s dataset ***********"%dataset.name)
        if not dataset.files:
            log.warning("%s dataset is empty!!"%dataset.name)
            return []
        
        canvas = ROOT.TCanvas()
        hist_set = []
        # - - - - containers for hists
        hist_set = []
        for var in fields:
            for category in categories:
                hset = Histset(
                    sample=dataset.name,
                    variable=var.name,
                    category=category.name,
                    hist=ROOT.TH1F(
                        "category_%s_var_%s"%(category.name, var.name), var.name, *var.binning),
                    systematic=systematic) 
                # - - make sure the newly created hist has no dummy value
                hset.hist.Reset()
                hist_set.append(hset)
        
        # - - loop over dataset's files
        nevents = 0
        for fn in dataset.files:
            fname = fn.split("/")[-1]
            tfile = ROOT.TFile(fn)
            # - - check if the file is healthy
            try:
                entries = tfile.Get(systematic).GetEntries()
                nevents += entries
                if entries==0:
                    log.warning("%s tree in %s is empty, skipping!"%(systematic, fn))
                    continue
            except:
                log.warning("%s has no %s tree!"%(fn, systematic))
                continue
            for category in categories:
                # - - hists for the current category
                cat_hists = filter(lambda hs: hs.category==category.name, hist_set)

                # get the tree 
                tree = tfile.Get(systematic)

                # - - get the list of the events that pass the selections
                selection = category.cuts.GetTitle()
                eventweight = "*".join(weights[category.name])
                tree.Draw(">>eventlist_%s"%category.name, selection)
                eventlist = ROOT.gDirectory.Get("eventlist_%s"%category.name)
                tree.SetEventList(eventlist)
                
                # - - draw all the vars
                for var in fields:
                    histname = "category_%s_%s_%s"%(category.name, var.name, fname)
                    log.debug("{0} >> {1}{2}".format(var.tformula, histname, var.binning))
                    log.debug("({0}) * ({1})".format(selection, eventweight))
                    
                    tree.Draw("{0} >> {1}{2}".format(var.tformula, histname, var.binning), eventweight)
                    htmp = ROOT.gPad.GetPrimitive(histname)
                    hset = filter(lambda hs: hs.variable==var.name, cat_hists)[0]
                    hset.hist += htmp
                    htmp.Delete()
                tree.Delete()
            tfile.Close()
            
        write_hists = kwargs.pop("write_hists", False)
        prefix = kwargs.pop("prefix", outname.split(".")[0]) #<! FIX ME: should give the sample name a better solution 
        if write_hists:
            hname = "%s.root"%outname
            if not os.path.isdir(outdir):
                os.system("mkdir -p %s"%outdir)
                
            hpath = os.path.join(outdir, hname)
            hfile = ROOT.TFile(hpath, "UPDATE")
            
            rdir = "%s"%(systematic)
            if not hfile.GetDirectory(rdir):
                hfile.mkdir(rdir)
            hfile.cd(rdir)
            
            for hset in hist_set:
                hist = hset.hist
                hist.SetTitle(hist.GetName())
                hist.Write("%s_%s"%(prefix, hist.GetName()), ROOT.TObject.kOverwrite)
            hfile.Close()

        canvas.Close()
        log.info("processed %s tree from %s dataset with %i events"%(systematic, dataset.name, nevents))
        return hist_set
        

    def hists(self, categories=[],
              fields=[],
              systematics=["NOMINAL"],
              **kwargs):
        """
        Parameters
        ----------
        category: 
            Category object; specific category oof analysis.
        fields:
            Variable;  list of variables to get histograms for them
        systematics: 
            Systematic; list of systematics 
        
        Returns
        -------
        hist_set: fields histograms.
        """
        
        if not fields:
            raise RuntimeError("no field is selected to produce hists for it")

        if not categories:
            raise RuntimeError("no category is selected to produce hists for it")
        
        # - - - - - - - - create a default canvas for the TTree.Draw
        canvas = ROOT.TCanvas()

        # - - - - prepare the workers
        workers = self.workers(
            categories=categories,
            fields=fields,
            systematics=systematics,
            **kwargs)

        # - - - - assign the jobs to the workers
        jobs = []
        hist_sets = []
        for worker in workers:
            jobs.append(FuncWorker(Sample.dataset_hists, worker,
                                   **kwargs) )
            
        #FIXME:Queue hangs up with FuncWorker! - - - - process samples' datasets in parallel
        parallel = kwargs.pop("parallel", False)    
        if parallel:
            log.info(
                "************** processing %s sample hists in parallel, njobs=%i ************"%(self.name, len(jobs) ) )
            run_pool(jobs, n_jobs=-1)
            
        # - - - - - - - - process datasets one after another
        else:
            log.info("************ processing %s sample hists sequentially ************"%self.name)
            for job in jobs:
                job.start()
                job.join()
    
    def write_hists(self, hist_set, hists_file, systematics=["NOMINAL"], overwrite=True):
        """
        """
        tf = ROOT.TFile(hists_file, "UPDATE")
        for systematic in systematics:
            rdir = "%s"%(systematic)
            if not tf.GetDirectory(rdir):
                tf.mkdir(rdir)
            tf.cd(rdir)
            for hs in hist_set:
                hist = hs.hist
                if overwrite:
                    log.debug("overwriting the existing hist")
                    hist.Write(hist.GetName(), ROOT.TObject.kOverwrite)
                else:
                    hist.Write(hist.GetName())
        tf.Close()
            
        return 
    
    def merge_hists(self, histsdir=None, hists_file=None, overwrite=False, ncpu=1):
        """ collect histograms for this sample and add them up properly.
        """
        log.info("merging %s hists"%self.name)

        assert histsdir, "hists dir is not provided!"
        if not hists_file:
            hists_file = self.config.hists_file
            
        # - - - - retrieve the samples hists
        hfiles = glob.glob("%s/%s.*"%(histsdir, self.name))

        if not hfiles:
            log.warning("no hists found for the %s in %s dir"%(self.name, histsdir))
            return

        # - - - - extract the hists 
        fields = set()
        categories = set()
        hist_set = []
        for hf in hfiles:
            htf = ROOT.TFile(hf, "READ")
            for systematic in self.systematics:
                systdir = htf.Get(systematic)
                for hname in [k.GetName() for k in systdir.GetListOfKeys()]:
                    # - - regex match the hist name
                    match = re.match(self.config.hist_name_regex, hname)
                    if match:
                        sample = match.group("sample")
                        category = match.group("category")
                        variable = match.group("variable")
                        
                        fields.add(variable)
                        categories.add(category)
                        hist = htf.Get("%s/%s"%(systematic, hname))
                        hist.SetDirectory(0) #<! detach from htf
                        hset = Histset(sample=sample, category=category, variable=variable,
                                       systematic=systematic, hist=hist)
                        hist_set.append(hset)
            htf.Close()
            
        # - - - - add them up
        merged_hists_file = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")
        merged_hist_set = []
        for systematic in self.systematics:
            for var in fields:
                for cat in categories:
                    hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var and hs.category==cat), hist_set)
                    hsum = reduce(lambda h1, h2: h1 + h2, [hs.hist for hs in hists])
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    hsum.SetTitle(outname)

                    # - - write it now
                    rdir = "%s"%(systematic)
                    if not merged_hists_file.GetDirectory(rdir):
                        merged_hists_file.mkdir(rdir)
                    merged_hists_file.cd(rdir)
                    hsum.Write(outname, ROOT.TObject.kOverwrite)
                    merged_hist_set.append(hsum)

        merged_hists_file.Close()
        
        return merged_hist_set
    
    
##---------------------------------------------------------------------------------------
## 
class Signal(object):
    # mixin
    pass


##---------------------------------------------------------------------------------------
## 
class Background(object):
    # mixin
    pass
    

##---------------------------------------------------------------------------------------
## 
class SystematicsSample(Sample):
    """ base class for providing methods specific to the systematics sample
        which inherits from Sample class.
    """
    def __init__(self, *args, **kwargs):

        # - - - - - - - - instantiate the base class
        super(SystematicsSample, self).__init__(*args, **kwargs)

        db = kwargs.pop("db", None) 
        # - - - - - - - - backgrounds
        if isinstance(self, Background):
            sample_key = self.__class__.__name__.lower()
            sample_info = samples_db.get_sample(
                self.config.channel, self.config.year, 'background', sample_key)
            kwargs.setdefault('name', sample_info['name'])
            kwargs.setdefault('label', sample_info['root'])
            if 'color' in sample_info and 'color' not in kwargs:
                kwargs['color'] = sample_info['color']

            # - - - - list of sample components from DataBase
            self.samples = sample_info['samples']
            log.debug(self.samples)
            if (self.samples is None or len(self.samples) < 1):
                log.error("no sample is available for %s"%sample_info['name'])
                raise RuntimeError

        # - - - - - - - - signals    
        elif isinstance(self, Signal):
            # - - - - samples already defined in Signal subclass
            log.debug(self.samples)
            assert len(self.samples) > 0
        else:
            raise TypeError(
                'MC sample %s does not inherit from Signal or Background' %
                self.__class__.__name__)

        self.datasets = []
        self.components = kwargs.pop("components", [])
        self.norms = {}
        
        # - - - - - - - - Database 
        self.db = self.config.database
        
        # - - - - - - - loop over samples and get datasets for each
        for i, name in enumerate(self.samples):
            log.debug("--"*60)
            log.debug(name)
            try:
                ds = self.db[name]
                xsec, kfact, effic = ds.xsec_kfact_effic
                log.debug(
                    "dataset: {0}  cross section: {1} [pb] \n"
                    "k-factor: {2} \n"
                    "filtering efficiency: {3}\n"
                    "events {4}".format(
                        ds.name, xsec, kfact, effic, ds.events))
                self.datasets.append(ds)
            except KeyError:
                log.warning("%s is missing in %s database"%(name, self.db.name))
                

    @classmethod
    def get_sys_term_variation(cls, systematic):
        """ to get the systematic terms and syst variations.
        """
        
        if systematic == 'NOMINAL':
            systerm = None
            variation = 'NOMINAL'
        elif len(systematic) > 1:
            # no support for this yet...
            systerm = None
            variation = 'NOMINAL'
        else:
            systerm, variation = systematic[0].rsplit('_', 1)
        return systerm, variation

        


##---------------------------------------------------------------------------------------
## 
class MC(SystematicsSample):

    """ a dedicated Monte Carlo sample class.
    """
    pass

##---------------------------------------------------------------------------------------
## 
class CompositeSample(object):
    """
    This class adds together the events from a list of samples
    and also return the summed histograms of all of those samples
    for the requested fields
    TODO: Implement a naming from the components.
    
    Parameters
    ----------
    
    samples_list: list;  a list of Sample objects;
    
    name: str; name for the combined samples
    
    label: str; label for the combined samples

    """
    def __init__(self, samples_list,
                 name='Sample',
                 label='Sample'):
        if not isinstance( samples_list, (list,tuple)):
            samples_list = [samples_list]
        if not isinstance (samples_list[0], Sample):
            raise ValueError( "samples_list must be filled with Samples")
        self.samples_list = samples_list
        self.name = name
        self.label = label

    def events(self, *args, **kwargs ):
        """
        Return a one-bin histogram with the total sum of events
        of all the samples
        Parameters:
        - See the events() method of the Sample class
        """
            
        return sum([s.events(*args, **kwargs) for s in self.samples_list])




