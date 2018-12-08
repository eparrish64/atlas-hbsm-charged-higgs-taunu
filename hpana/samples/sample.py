# -*- coding: utf-8 -*-

# std lib imports
import os, sys, pickle, string, glob, copy, re 
from operator import add, itemgetter
from collections import namedtuple
import random 
import datetime
import multiprocessing

## ROOT imorts 
import ROOT

## local imports
from hpana import log
from hpana.dataset_hists import dataset_hists
from hpana.db import samples as samples_db
from hpana.db import datasets
from hpana.db.decorators import cached_property
from hpana.categories import TAU_IS_TRUE, Category
from hpana.containers import Histset, HistWorker    

##---------------------------------------------------------------------------------------
## - - base analysis sample class
##---------------------------------------------------------------------------------------
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

    def __init__(self, config, name='Sample', label='Sample', **kwargs):
        ## the main configuration object check ../config.py
        self.config = config
        self.name = name
        self.label = label
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

    def triggers(self, categories=[], dtype="MC"):
        """ trigger could be different for different selection categories, 
        and also it could be different for DATA and MC.
        Parameters
        -----------
        categories:
             list(Category type): selection categories. 

        """
        trigger_dict = {} 
        for cat in categories:
            trigger_dict[cat.name] = self.config.trigger(dtype=dtype, category=cat)
        return trigger_dict
    
    def cuts(self,
             category=None,
             trigger=None,
             tauid=None,
             extra_cuts=None,
             truth_match_tau=None,
             **kwargs):
        """ this method is for applying the overall selection. 
        It will update the cuts list of the category with different trigger, tauid, etc. cuts.
        
        Parameters
        ----------
        category: 
            Category type;
        trigger: 
            ROOT.TCut type; trigger selection
        tauid: 
            ROOT.TCut type; tau ID selection
        truth_match_tau: 
            ROOT.TCut type; truth matchig selection

        Returns
        -------
        cuts: ROOT.TCut object
        """

        cuts = ROOT.TCut("")
        if category:
            cuts += category.cuts
        if not trigger:
            cuts += self.config.trigger(dtype="MC", category=category)
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
        """ MC scale factors.
        The weights could in general be dependent on the category selection.
        """

        # - - - - defensive copy
        weight_fields = self.config.weight_fields[:]
        # - - - - MC common weights
        if not categories:
            categories = self.config.categories
        weights_dict = {}

        for category in categories:
            weights_dict[category.name] = [w.title for w in weight_fields]
        
        return weights_dict

    @property
    def systematics(self):
        return self.config.systematics

    def data_lumi(self, data_streams):
        """
        lumi for the given data streams
        """
        return sum([self.config.data_lumi[ds] for ds in data_streams])
        
    def events(self, categories, **kwargs):
        """ get event counts using hists method
        """
        nevents = {}
        field = self.config.variables[0]
        hist_set =  self.hists(categories=categories,fields=[field], **kwargs)

        hist = hist_set[0].hist
        for cat in categories:
            hcat = filter(lambda hs: hs.category==cat.name, hist_set)
            hist = hcat[0].hist
            # - - - - add the events from overflow bin too 
            nbins = hist.GetNbinsX() + 2
            nevents[cat.name] = hist.Integral(0, nbins)
            log.info("# of events from %s tree of %s sample in category %s: %0.4f"%(
                systematic, self.name, cat.name, nevents[cat.name]))
        
        return nevents

    def cutflow(self, cuts, **kwargs):
        """

        """
        categories = []
        cuts_list = []
        for name, cut in cuts.iteritems():
            cuts_list += [cut]
            categories.append(Category(name, cuts_list=cuts_list, mc_camp=self.config.mc_camp))
        field = kwargs.pop("field", self.config.variables[0])
        hists = self.hists(categories=categories, fields=[field], **kwargs)
        return hists
    
    def workers(self, categories=[],
                fields=[],
                systematics=[],
                trigger=None,
                extra_cuts=None,
                extra_weight=None,
                weighted=True,
                hist_templates=None,
                **kwargs):
        """ list of workers to submit jobs.
        each worker is basically assigned a histogram to fill, one hist per systematic pre dataset.
        please note that additional selections like trigger are applied here and 
        selection string is passed to the worker. Furtheremore for each selection category a weight is also 
        assigned.
        """
        if not systematics:
            systematics = self.config.systematics[:1] #<! NOMINAL
        else: #<! sanity check 
            systematics = filter(lambda s: s.name in [st.name for st in self.systematics], systematics)

        if not fields:
            fields = self.config.variables
        if not categories:
            categories = self.config.categories

        # - - - - same trigger for all selection categories ?
        if not trigger:
            triggers = self.triggers(categories)

        # - - - - defensive copy 
        categories_cp = copy.deepcopy(categories)
        for category in categories_cp:
            category.cuts += trigger if trigger else triggers[category.name]
            if extra_cuts:
                category.cuts += extra_cuts
            
        # - - - - one worker per dataset per systematic
        workers = set()
        for ds in self.datasets:
            if isinstance(self, MC):
                ## - - just do the datasets for the requested data streams
                sts = set(ds.stream) - set(self.config.data_streams)
                if len(sts)>0:
                    continue
                
            # - - - - one worker per dataset
            # weights list per category
            weights = self.weights(categories=categories)

            for category in categories_cp:
                # - - - - lumi, MC and extra weights  
                if weighted:
                    # - - lumi weight
                    if ds.events !=0:
                        lumi_weight = self.data_lumi(ds.stream) * reduce(
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

            worker = HistWorker(
                name="%s.%s"%(self.name, ds.name),
                sample=self.name,
                dataset=ds,
                fields=fields,
                categories=categories_cp,
                weights=weights,
                systematics=systematics,
                hist_templates=hist_templates,
                channel=self.config.channel) 

            workers.add(worker)

        return list(workers)


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

        hist_sets = []
        # - - - - prepare the workers
        workers = self.workers(
            categories=categories,
            fields=fields,
            systematics=systematics,
            **kwargs)

        log.info(
            "************** processing %s sample hists in parallel, njobs=%i ************"%(self.name, len(workers) ) )
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = [pool.apply_async(dataset_hists, (wk,)) for wk in workers]
        for res in results:
            hist_sets += res.get(3600) #<! without the timeout this blocking call ignores all signals.

        # - - - - merge all the hists for this sample
        merged_hist_set = []
        for systematic in systematics:
            for var in fields:
                for cat in categories:
                    hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var.name and hs.category==cat.name), hist_sets)
                    hsum = hists[0].hist
                    for hs in hists[1:]:
                        hsum.Add(hs.hist)
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    hsum.SetTitle(outname)
                    hsum.SetName(outname)
                    merged_hist_set.append(Histset(sample=self.name, category=cat.name, variable=var.name, hist=hsum) )
        canvas.Close()
        return merged_hist_set
    
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
    
    def merge_hists(self, hist_set=[], histsdir=None, hists_file=None, write=False, **kwargs):
        """ collect histograms for this sample and add them up properly.
        read the hist from the disk or get them on the fly.
        """
        log.info("merging %s hists"%self.name)

        if not hist_set:
            log.info("reading dataset hists from %s"%histsdir)
            assert histsdir, "hists dir is not provided!"
            # - - - - retrieve the samples hists
            hfiles = glob.glob("%s/%s.*"%(histsdir, self.name))

            if not hfiles:
                log.warning("no hists found for the %s in %s dir"%(self.name, histsdir))
                return []

            # - - - - extract the hists 
            fields = set()
            categories = set()
            systematics = []
            hist_set = []
            for hf in hfiles:
                htf = ROOT.TFile(hf, "READ")
                systematics = [k.GetName() for k in htf.GetListOfKeys()]
                for systematic in systematics:
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
        else:
            # - - - - get list of categories and fields available in hist_set
            fields = list(set([hs.variable for hs in hist_set] ) )
            categories = list(set([hs.category for hs in hist_set] ) )
            systematics = list(set([hs.systematic for hs in hist_set]))

        if write:
            # - - - - output file
            if not hists_file:
                hists_file = self.config.hists_file
            merged_hists_file = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")
        
        # - - - - make sure hists are for this sample
        hist_set = filter(lambda hs: hs.sample.startswith(self.name), hist_set)
        if not hist_set:
            log.warning("no hist is found for %s; skipping the merge!"%self.name)
            return []

        # - - - - add them up
        merged_hist_set = []
        for systematic in systematics:
            for var in fields:
                for cat in categories:
                    hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var and hs.category==cat), hist_set)
                    hsum = hists[0].hist
                    for hs in hists[1:]:
                        hsum.Add(hs.hist)
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    hsum.SetTitle(outname)
                    hsum.SetName(outname)
                    merged_hist_set.append(
                        Histset(sample=self.name, variable=var, category=cat, systematic=systematic, hist=hsum) )

                    if write:
                        # - - write it now
                        rdir = "%s"%(systematic)
                        if not merged_hists_file.GetDirectory(rdir):
                            merged_hists_file.mkdir(rdir)
                        merged_hists_file.cd(rdir)
                        hsum.Write(outname, ROOT.TObject.kOverwrite)
                        
        # - - - - close open streams
        if write:
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
        database = kwargs.pop("database", None)
        
        # - - - - - - - - instantiate the base class
        super(SystematicsSample, self).__init__(*args, database=database, **kwargs)
        
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

    @cached_property
    def datasets(self):
        datasets = []
        # - - - - - - - loop over samples and get datasets for each
        for i, name in enumerate(self.samples):
            log.debug("--"*60)
            log.debug(name)

            if isinstance(self, MC):
                ## - - query on database with dataset ds property which is the same as sample's name
                dss = self.config.database.query(ds=name, streams=self.config.data_streams)
                for ds in dss:
                    xsec, kfact, effic = ds.xsec_kfact_effic
                    log.debug(
                    "dataset: {0}  cross section: {1} [pb] \n"
                        "k-factor: {2} \n"
                        "filtering efficiency: {3}\n"
                        "events {4}".format(
                            ds.name, xsec, kfact, effic, ds.events))
                    datasets.append(ds)

        return datasets

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
    ## mix in 
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




