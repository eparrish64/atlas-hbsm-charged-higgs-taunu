# -*- coding: utf-8 -*-

# std lib imports
import os, sys, pickle, string 
from operator import add, itemgetter
from collections import namedtuple
import random 
import datetime

# ROOT imorts 
import ROOT

# local imports
from . import log

from ..db import samples as samples_db, datasets
from ..db.decorators import cached_property
from ..config import Configuration
from ..lumi import LUMI, get_lumi_uncert
from ..systematics import get_systematics, iter_systematics, systematic_name
from ..cluster.parallel import FuncWorker, run_pool, map_pool


##---------------------------------------------------------------------------------------
## 
class Dataset(namedtuple('Dataset', ('ds','files', 'events'))):
    """ plain namedtuple to hold Dataset inof
    """
    @property
    def name(self):
        return self.ds.name
    
##---------------------------------------------------------------------------------------
## 
class Histset(namedtuple("Histset",
                         ("sample", "variable", "category", "systematic", "hist") ) ):
    """simple namedtuple to hold a histogram info
    """
    pass


##---------------------------------------------------------------------------------------
## 
class Sample(object):
    """
    base class for analysis samples.

    Attributes
    ----------
    year: int, the year daa is taken.
    scale: float (default=1.), to scale the sample. 
    cuts: TCut object; to apply cuts at preparing samples level.
    ntuple_path: string; the path to ntuples
    student: string; default naming scheme for ntuples.
    force_open: bool; whether to force-open ntuples in case needed.
    trigger: bool; should you need to apply trigger
    channel: string; specific channel investigating.
    name: string; sample's name
    label: string; sample's lable (used for plotting, etc.) 
    """

    def __init__(self, config,
                 weight_fields=[],
                 scale=1.,
                 cuts=None,
                 trigger=True,
                 channel='taujet',
                 name='Sample',
                 label='Sample',
                 **kwargs):
        # - - - - - - - - passing main configurations to the sample
        self.config = config

        # - - - - - - - - minimal flags
        self.scale = scale
        self.name = name
        self.label = label
        if cuts is None:
            self._cuts = ROOT.TCut("")
        else:
            self._cuts = cuts
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
             systematic='NOMINAL',
             tauid=None,
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

        cuts = ROOT.TCut(self._cuts)
        if category:
            cuts += category.cuts
        if not trigger:
            cuts += self.config.trigger
        else:
            cuts += trigger

        # - - - - - - - - tauID (for fakes check fakes.Fakes)
        if tauid:
            cuts += tauid
        else:
            cuts += self.config.tauid
        return cuts

    def events(self,
               systematic="NOMINAL",
               category=None,
               region=None,
               trigger=None,
               extra_cuts=None,
               extra_weight=None,
               tauid=False,
               weighted=True,
               scale=1.):
        """ This method returns the number of events selected.  The selection is
        specified by the different arguments.  

        Parameters
        ----------
        category :
            A given analysis category. See categories/__init__.py for the list
        region :
            A given analyis regions based on the sign and isolation of the
            taus. The signal region is 'OS'
        cuts :
            In addition to the category (where cuts are specified), extra
            cuts can be added See categories/common.py for a list of possible
            cuts
        systematic :
            By default look at the nominal tree but could also do it
            on specified syst.
        weighted :
            if True, return the weighted number of events
        scale :
            if specified, multiply the number of events by the given
            scale.
       
        Returns
        -------
        """
        # - - - - - - - - filters 
        base_selection =  self.cuts(
            category=category,
            region=region, trigger=trigger,
            tauid=tauid, systematic=systematic)
        if extra_cuts:
            base_selection &= extra_cuts

        total_events_weighted = 0
        # - - - - - - - - loop over sample's datasets 
        for ds in self.datasets:
            log.debug(ds.events)
            # - - - - - - - - dataset chain 
            ds_chain = ROOT.TChain(systematic)
            for _file in ds.files:
                ds_chain.Add(_file)

            # - - - - - - - - total events
            total_events = 0
            for _file in ds.files:
                try:
                    # - - - - read total number of events for dataset from database (just once)
                    total_events = ds.events
                    break
                except KeyError:
                    # - - - - count them on the fly
                    rfile = ROOT.TFile(_file, "READ")
                    h_metadata = rfile.Get("%s"%self.config.events_cutflow_hist)
                    total_events += h_metadata.GetBinContent(self.config.events_cutflow_bin)
                    rfile.Close()
                    h_metadata.Delete()
                    
            if weighted:
                if total_events !=0:
                    lumi_weight = self.config.data_lumi * reduce(
                        lambda x,y:x*y, ds.xsec_kfact_effic) / total_events
                else:
                    log.warning(" 0 lumi weight for %s"%ds.name)
                    lumi_weight = 0
                    
                weight_branches = self.weights + [str(lumi_weight)]
                selection = base_selection * ROOT.TCut('*'.join(weight_branches))
                if extra_weight:
                    selection *= extra_weight
                    
                log.debug("requesting number of events from %s using cuts: %s"
                          % (ds.name, selection))
            else:
                selection = base_selection
                
            log.info(selection)     
            ds_chain.Draw("1 >> htmp(1, -100, 100)", selection) 
            htmp = ROOT.gPad.GetPrimitive("htmp")
            total_events_weighted += htmp.Integral()
            htmp.Delete()
            ds_chain.Reset()
            
        return total_events_weighted

    @staticmethod
    def hists_from_file(ifile, fields, selection, tree_name="NOMINAL"):
        """
        """
        tfile = ROOT.TFile(ifile, "READ")
        tree = tfile.Get(tree_name)

        field_hists  = {}
        # - - draw histograms
        for var in fields:
            histname = var.name + "_" + ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(13))
            if var.name not in field_hists:
                field_hists[var.name] = {}

            log.debug("{0} >> {1}{2}".format(var.tformula, histname, var.binning))
            log.debug(selection)
            tree.Draw("{0} >> {1}{2}".format(
                var.tformula, histname, var.binning), selection)
            
            htmp = ROOT.gPad.GetPrimitive(histname)
            field_hists[var.name] = htmp.DrawCopy()
            htmp.Delete()
            tree.Reset()
        #tfile.Close()
        return field_hists
    
    def hists(self, category,
              fields=[],
              systematic="NOMINAL",
              extra_cuts=None,
              extra_weight=None,
              weighted=True,
              trigger=None,
              tauid=None,
              suffix=None):
        """
        Parameters
        ----------
        category: 
            Category object; specific category oof analysis.
        fields:
            Variable;  list of variables to get histograms for them
        extra_cuts: 
            TCut objetc; to apply cuts for plotting.
        systematic: 
            str; systematic tree name.
        suffix: 
            string; a lable used for saving plots.
        
        Returns
        -------
        hist_set: fields histograms.
        """
        log.info("processing histograms for %s tree from %s ; category: %s"%(
            systematic, self.name, category.name))
        
        if not fields:
            fields = self.config.variables
            self.debug("creating hists for all the variables {}".format(fields))

        # - - - - - - - - create a default canvas for the TTree.Draw
        canvas = ROOT.TCanvas()
        
        # - - - - - - - - filters
        base_selection = self.cuts(
            category=category,
            trigger=trigger,
            tauid=tauid,
            systematic=systematic)
        if extra_cuts:
            base_selection += extra_cuts
            
        # - - - - - - - - loop over sample's datasets
        hists = {}
        for ds in self.datasets:
            log.debug("dataset {};  total # of events:{} ; lumi: {} ".format(
                ds.name, ds.events, ds.lumi_weight))

            # - - - - - - - - event weight
            if weighted:
                if ds.events !=0:
                    lumi_weight = self.config.data_lumi * reduce(
                        lambda x,y:x*y, ds.xsec_kfact_effic) / ds.events
                else:
                    log.warning(" 0 lumi weight for %s"%ds.name)
                    lumi_weight = 0
                    
                weights = self.weights + [str(lumi_weight)]
                event_weight = "*".join(weights)
                selection = base_selection * ROOT.TCut(event_weight)
                if extra_weight:
                    selection *= extra_weight
            else:
                selection = base_selection
                
            log.debug("requesting number of events from %s using cuts: %s"
                      % (ds.name, selection))

            # - - - - - - - -
            ds_chain = ROOT.TChain(systematic)
            for ifile in ds.files:
                ds_chain.Add(ifile)
                
            for var in fields:
                if not var.name in hists:
                    hists[var.name] = []
                    
                histname = '{0}_channel_{1}_category_{2}_{3}'.format(
                    ds.name, self.config.channel, category.name, var.name)
                if suffix is not None:
                    histname += suffix

                # - - - - randomize hist name to avoid possible memory leak
                histname += ''.join(
                    random.choice(string.ascii_uppercase + string.digits) for _ in range(13))
                
                # - - draw histogram
                ds_chain.Draw("{0} >> {1}{2}".format(var.tformula, histname, var.binning), selection)
                htmp = ROOT.gPad.GetPrimitive(histname)
                log.debug(
                    "TTree.Drawing:: {0} >> {1}{2}; selection: {3}; # integral: {4}".format(
                        var.tformula, histname, var.binning, selection,
                        htmp.Integral(0, htmp.GetNbinsX()+1) ) )
                hists[var.name].append(htmp.Clone())
                
            # - - - - reset the chain and go to the next dataset 
            ds_chain.Reset()

        hist_set = []
        for var in fields:
            hist_list = hists[var.name]
            fname = "%s_%s_%s"%(self.name, category.name, var.name)
            hsum = reduce(lambda x, y: x + y, hist_list)
            hsum.SetName(fname)
            hsum.SetTitle(fname)
            hsum.SetXTitle(var.title)
            
            hist_set.append(Histset(
                sample=self.name,
                variable=var.name,
                category=category,
                hist=hsum,
                systematic=systematic ) )
            
        log.info("processed %s tree from %s sample; category: %s"%(
            systematic, self.name, category.name))
        
        return hist_set
    
    def write_hists(self, hist_set, ofile, systematic="NOMINAL", overwrite=True):
        """
        """
        tf = ROOT.TFile(ofile, "UPDATE")
        rdir = "%s/%s"%(self.config.channel, systematic)
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
            log.debug(name)
            try:
                ds = self.db[name]
            except KeyError:
                log.warning("%s is missing in %s database"%(name, self.db.name))
            xsec, kfact, effic = ds.xsec_kfact_effic
            log.debug(
                "dataset: {0}  cross section: {1} [pb] "
                "k-factor: {2} "
                "filtering efficiency: {3}"
                "events {4}".format(
                    ds.name, xsec, kfact, effic, ds.events))
            #dataset = Dataset(ds=ds, events=self.events)
            self.datasets.append(ds)

    @cached_property
    def weights(self, category=None):
        """ weight vars
        """
        
        # - - - - - - - - MC common weights 
        weight_fields = []
        for wtype, wlist in self.config.weights.items():
            if wtype=="FF":
                continue
            for w in wlist:
                weight_fields.append(w)
        
        return [w.name for w in weight_fields]

            
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

    def systematics(self):
        pass
        


##---------------------------------------------------------------------------------------
## 
class MC(SystematicsSample):

    """ a dedicated Monte Carlo sample class.
    """

    def __init__(self, *args, **kwargs):
        self.pileup_weight = kwargs.pop('pileup_weight', False)
        super(MC, self).__init__(*args, **kwargs)

    def cuts(self, *args, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------


        Returns
        -------
        cut: Cut, updated Cut type.
        """
        cut = super(MC, self).cuts(*args, **kwargs)
        return cut
    


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

