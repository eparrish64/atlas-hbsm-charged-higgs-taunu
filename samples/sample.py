# -*- coding: utf-8 -*-

# std lib imports
import os
import sys
import pickle
from operator import add, itemgetter
from collections import namedtuple

# numpy imports
import numpy as np
#from numpy.lib import recfunctions
from matplotlib.mlab import rec_append_fields

# mpl imports
from matplotlib import mlab

# rootpy imports
import ROOT
from rootpy.plotting import Hist, Hist2D, Canvas, HistStack
from rootpy.plotting.hist import _HistBase
from rootpy.tree import Tree, Cut
from rootpy.stats import histfactory
from rootpy import asrootpy

# root_numpy imports
from root_numpy import rec2array, stack, fill_hist

# higgstautau imports
from hhdb import samples as samples_db, datasets

# local imports
from . import log; log = log[__name__]
from ..variables import *
from .. import LH_REGIONS, HH_REGIONS, LH_REGIONS_SYSTEMATICS, HH_REGIONS_SYSTEMATICS
from .. import NTUPLE_PATH, DEFAULT_STUDENT, ETC_DIR, CACHE_DIR
from ..utils import print_hist, ravel_hist, uniform_hist
from ..classify import histogram_scores, Classifier
from mva.defaults import TRIGGER_TYPE
from mva.regressor import BRT_FEATURES
from ..systematics import (
    get_systematics, SYSTEMATICS_BY_WEIGHT,
    iter_systematics, systematic_name)
from ..lumi import LUMI, get_lumi_uncert
from .db import TEMPFILE, get_file #, DB
from ..cachedtable import CachedTable
from mva.categories import get_trigger
from mva.categories.lephad import cutYearRunNum
try:
    from moments import HCM
except:
    log.warning('moments module is not installed')


##---------------------------------------------------------------------------------------
## consts
BCH_UNCERT = pickle.load(open(os.path.join(CACHE_DIR, 'bch_cleaning.cache')))
YEAR_ENERGY = {"2011": 7, "2012": 8 , "2015": 13, "2016": 13, "2017": 13, "2018": 13}

##---------------------------------------------------------------------------------------
## 
class Dataset(namedtuple('Dataset',
                         ('ds', 'tables', 'events',
                          'xs', 'kfact', 'effic'))):
    @property
    def name(self):
        return self.ds.name

##---------------------------------------------------------------------------------------
## 
class Sample(object):

    """
    base class for preparing analysis samples.

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
    def corrections(self, rec):
        return []

    def __init__(self, year,
                 weight_fields=[],
                 scale=1.,
                 cuts=None,
                 ntuple_path=NTUPLE_PATH,
                 student=DEFAULT_STUDENT,
                 force_reopen=False,
                 trigger=True,
                 trigger_type = TRIGGER_TYPE,
                 channel='hadhad',
                 name='Sample',
                 label='Sample',
                 ntuples_version = 'v3',
                 events_cutflow_bin=8,
                 events_cutflow_hist="hmtadata",
                 treename="NOMINAL",
                 **hist_decor):
        
        self.year = year
        self.energy = YEAR_ENERGY[year]

        self.scale = scale
        if cuts is None:
            self._cuts = Cut()
        else:
            self._cuts = cuts
        self.ntuple_path = ntuple_path
        self.student = student
        self.force_reopen = force_reopen
        self.name = name
        self.label = label
        self.hist_decor = hist_decor
        if 'fillstyle' not in hist_decor:
            self.hist_decor['fillstyle'] = 'solid'

        self.trigger = trigger
        self.channel = channel
        
        # - - - - - - - ntuples version
        self.ntuples_version = ntuples_version


        # - - - - - - - analysis configuraion
        self.conf = Configuration(self.channel)

        self.weight_fields = weight_fields
    
    
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

    def get_field_hist(self, fields, category, templates=None):

        """retrieve a histogram for the requested
        variables in the given category
        Parameters
        ----------
        - vars: Variable type (see variables.py)
        - category: Category type; see categories.py
        - template: TH1F; hist template 
        Returns
        -------
        hist: the histogram of the specifid varibale.
        
        """

        fields_hist  = {}
        fields_scale = {}
        for var in fields:
            if templates is not None and field in templates:
                hist = template.Clone(
                    title=self.label, **self.hist_decor)
                fields_hist[var] = hist
                fields_scale[var] = var.scale
                continue
            
            bins = field.binning(self.year, category)
            log.debug("var: %S; binning: %s"%(var, bins))

            hist = Hist(list(bins),
                        title=self.label,
                        type='D',
                        **self.hist_decor)
            fields_hist[var] = hist
            fields_scale[var] = var.scale

        return fields_hist, fields_scale

    def get_hist_array(self,
                       field_hist_template,
                       category, region,
                       cuts=None,
                       clf=None,
                       scores=None,
                       min_score=None,
                       max_score=None,
                       regressor=None,
                       systematics=False,
                       systematics_components=None,
                       suffix=None,
                       field_scale=None,
                       weight_hist=None,
                       weighted=True,
                       bootstrap_data=False):
        """
        
        Parameters
        ----------
        field_hist_template: a dictionary of Histogram templates for different variables.
        category: Category object; specific category oof analysis.
        region: Region object; for dealing with signal or control region.
        cuts: TCut objetc; to apply cuts for plotting.
        clf: trained classifier for separating sig-bkg;
        scores: np array; classifier'e predicted scores.
        min_score: float; min scores
        max_score: float; max scores
        systematics: bool; wethere to do systematics or not.
        systematic_components: specific systematics to be applied.
        suffix: string; a lable used for saving plots.
        field_scale: scaled variable(normalized hists).
        weighted_hist: weighted hist.
        weighted: bool(default True); 
        bootstrap_data: bool; wethere to random sample data with replacement or not for testing purposes

        Returns
        -------
        field_hist: a dictionary of the field histograms.
        rec: mereged-record; table of all fields.
        weights: weights array.
        """
        
        do_systematics = (isinstance(self, SystematicsSample)
                          and self.systematics
                          and systematics)
        if do_systematics and systematics_components is None:
            systematics_components = self.systematics_components()

        histname = '{0}_category_{1}_{2}'.format(self.channel, category.name, self.name)
        if suffix is not None:
            histname += suffix

        field_hist = {}
        for field, hist in field_hist_template.items():
            if isinstance(field, basestring):
                new_hist = hist.Clone(name=histname + '_{0}'.format(field))
            else:
                new_hist = hist.Clone(name=histname)
            new_hist.Reset()
            new_hist.decorate(**self.hist_decor)
            new_hist.title = self.label
            field_hist[field] = new_hist

        return field_hist, rec, weights

    def weights(self, systematic='NOMINAL'):

        """ to weight the fields.

        Parameters
        ----------
        systematics: string; systematics type.

        Returns
        -------
        weight_fields: weighted fields.

        """

        weight_fields = self.weight_fields()
        if isinstance(self, SystematicsSample):
            systerm, variation = \
                SystematicsSample.get_sys_term_variation(systematic)
            for term, variations in self.weight_systematics().items():
                # handle cases like TAU_ID and TAU_ID_STAT
                if (systerm is not None
                    and systerm.startswith(term)
                    and systematic[0][len(term) + 1:] in variations):
                    weight_fields += variations[systematic[0][len(term) + 1:]]
                elif term == systerm:
                    weight_fields += variations[variation]
                else:
                    weight_fields += variations['NOMINAL']
       
        return weight_fields

    def cuts(self,
             category=None,
             region_cut=None,
             trigger_cut=None,
             systematic='NOMINAL',
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
        cuts: TCut object
        
        """

        cuts = ROOT.TCut(self._cuts)
        if category is not None:
            cuts &= category.cuts
        if region is not None:
            cuts &= region
        if self.trigger:
            cuts &= trigger

        if isinstance(self, SystematicsSample):
            systerm, variation = SystematicsSample.get_sys_term_variation(
                systematic)
            for term, variations in self.cut_systematics().items():
                if term == systerm:
                    cuts &= variations[variation]
                else:
                    cuts &= variations['NOMINAL']
        return cuts


    def events(self,
               systematic="NOMINAL",
               category=None,
               region=None,
               cuts=None,
               hist=None,
               weighted=True,
               scale=1.):
        """ see self.events. 
        This method returns the number of events selected.  The selection is
        specified by the different arguments.  By default, the output is a
        one-bin histogram with number of event as content.

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
        hist :
            if specified, fill this histogram. if not create a new one an
            return it.
        scale :
            if specified, multiply the number of events by the given
            scale.
       
        Returns
        -------
        """

        hist = ROOT.TH1F("h", "h", 1, -100, 100)
        total_events_weighted = 0
        tchain = ROOT.TChain("chain")
        for ds in self.datasets:
            # - - - - check if total number of events is cached in database
            try:
                log.info("reading total # of weighted events for %s Dataset from DataBase ..."%ds.name)
                total_events_weighted = ds.total_events_weighted
                
            # - - - - calcualte on the fly 
            except KeyError:
                files = glob.glob("%s/%s"%(ntuples_path, file_pattern))
                for f in files:
                    tchain.Add(f)
                treename = ds.treename
                for _file in files:
                    rfile = ROOT.TFile(_file, "READ")
                    h_metadata = rfile.Get("%s"%events_cutflow_hist)
                    total_events_weighted += h_metadata.GetBinContent(events_cutflow_bin)
                
                selection =  (self.cuts(category, region) & cuts)
                if weighted:
                    lumi_weight = LUMI[self.year] * scale * ds.xs * ds.kfact * ds.effic / total_events_weighted
                    weight_branches = self.weights()
                    selection *= Cut(str(lumi_weight * scale))
                    selection *= Cut('*'.join(weight_branches))
                    log.debug("requesting number of events from %s using cuts: %s"
                              % (ds.name, selection))
                
            
            rfile.Close()
                    
        return total_events_weighted


    def lumi_weight(self):
        """ lumi weight for the MC
        """
        for ds in self.datasets:
            total_events_weighted = (LUMI[self.year] * scale * ds.xs * ds.kfact * ds.effic) /self.events()
        
    

    
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
    def __init__(self, year,
                 db=None,
                 components=["NOMINAL"],
                 weight_systematics=[],
                 channel='lephad',
                 **kwargs):

        # - - - - - - - - instantiate the base class
        super(SystematicsSample, self).__init__(year=year, channel=channel, **kwargs)
        
        if isinstance(self, Background):
            sample_key = self.__class__.__name__.lower()
            sample_info = samples_db.get_sample(
                self.channel, year, 'background', sample_key)
            kwargs.setdefault('name', sample_info['name'])
            kwargs.setdefault('label', sample_info['root'])
            if 'color' in sample_info and 'color' not in kwargs:
                kwargs['color'] = sample_info['color']
            self.samples = sample_info['samples']
            log.debug(self.samples)
            if (self.samples is None or len(self.samples) < 1):
                log.error("no sample is available for %s"%sample_info['name'])
                raise RuntimeError
            
        elif isinstance(self, Signal):
            log.debug(self.samples)
            assert len(self.samples) > 0

        else:
            raise TypeError(
                'MC sample %s does not inherit from Signal or Background' %
                self.__class__.__name__)

        self.datasets = []
        self.components = components
        self.norms = {}
        
        # - - - - - - - - create Database 
        self.db = datasets.Database(self.year,
                                    channel=self.channel, 
                                    version=self.ntuples_version, 
                                    verbose=False)
        rfile = get_file(self.ntuple_path, self.student, force_reopen=self.force_reopen)

        #  - - - - - - - loop over samples and get datasets for each
        for i, name in enumerate(self.samples):
            log.debug(name)
            ds = self.db[name]
            events = {}

            # - - - -  loop over systematics
            for syst in systematics_components:
                try:
                    cutflow_hist = rfile.Get(treename + events_cutflow_hist]
                    events[syst] = cutflow_hist.GetBinContent(events_cutflow_bin)
                except:
                    log.warning(
                        "events cutflow hist %s not found, using events number from database!")
                    events[syst] = ds.nevents

            if hasattr(self, 'xsec_kfact_effic'):
                xs, kfact, effic = self.xsec_kfact_effic(i)
            else:
                xs, kfact, effic = ds.xsec_kfact_effic
            log.debug(
                "dataset: {0}  cross section: {1} [pb] "
                "k-factor: {2} "
                "filtering efficiency: {3} "
                "events {4}".format(
                    ds.name, xs, kfact, effic, events['NOMINAL']))
            dataset = Dataset(ds=ds, tables=tables, events=events,
                              xs=xs, kfact=kfact, effic=effic)
            self.datasets.append(dataset)

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

    def draw(self, field_hist,
             scale=1.,
             category=None,
             region=None,
             cuts=None,
             weighted=True,
             field_scale=None,
             weight_hist=None,
             field_weight_hist=None,
             systematics=False,
             systematics_components=None,
             bootstrap_data=False):
        """
        Parameters
        ----------
        field_hist: field histogram a dictionary {field:hist}.
        category: Category object; specific category oof analysis.
        region: Region object; for dealing with signal or control region.
        cuts: TCut objetc; to apply cuts for plotting.
        systematics: bool; wethere to do systematics or not.
        systematics_components: specific systematics to be applied.
        field_scale: scaled variable(normalized hists).
        weighted_hist: weighted hist.
        weighted: bool(default True); 
        bootstrap_data: bool; wethere to random sample data with replacement or not 

        Returns
        -------
        field_hist: a dictionary of the filled field histogram.

        """

        do_systematics = self.systematics and systematics

        all_sys_hists = {}
        for field, hist in field_hist.items():
            if not hasattr(hist, 'systematics'):
                hist.systematics = {}
            all_sys_hists[field] = hist.systematics

        for systematic in iter_systematics(False,
                year=self.year,
                components=systematics_components):

            sys_field_hist = {}
            for field, hist in field_hist.items():
                if systematic in all_sys_hists[field]:
                    sys_hist = all_sys_hists[field][systematic]
                else:
                    sys_hist = hist.Clone(
                        name=hist.name + '_' + systematic_name(systematic))
                    sys_hist.Reset()
                    all_sys_hists[field][systematic] = sys_hist
                sys_field_hist[field] = sys_hist

            self.draw_array_helper(sys_field_hist, category, region,
                                   cuts=cuts,
                                   weighted=weighted,
                                   field_scale=field_scale,
                                   weight_hist=weight_hist,
                                   field_weight_hist=field_weight_hist,
                                   scores=scores[systematic] if scores else None,
                                   min_score=min_score,
                                   max_score=max_score,
                                   regressor=regressor,
                                   systematic=systematic,
                                   scale=scale)

        return rec, weights


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
        # make sure year is a 4 digits number
        year = self.year % 1000 + 2000
        run_cut = cutYearRunNum[str(year)]['mc']
        cut = super(MC, self).cuts(*args, **kwargs)
        cut &= run_cut
        return cut
    
    def weights(self):
        """ additional weights for MC
        Parameters
        ----------
        
        Returns
        -------
        weights: list, extended weights list
        """
        weights = super(MC, self).weights(*args, **kwargs)

        # - - - - - - - - MC
        mc_weights = ["mc_weight"]

        
        # - - - - - - - - lumi weight
        h_metadata =  
         
        weights 
        
    


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

    def draw_array(self, field_hist_tot, category, region,
                   systematics=False, **kwargs):
        """
        Construct histograms of the sum of all the samples.
        Parameters
        ----------
        field_hist_tot: dictionnary of Histograms that constrain the structure we want to retrieve
        category: the analysis category
        region: the analysis region (for example 'OS')
        systematics: boolean flag
        
        Returns
        -------

        """
        field_hists_list = []
        # -------- Retrieve the histograms dictionnary from each sample and store it into a list
        for s in self.samples_list:
            # field_hists_temp = s.get_hist_array(
            # field_hist_tot, category, region, systematics=systematics,**kwargs)
            field_hists_temp = {}
            for field,hist in field_hist_tot.items():
                field_hists_temp[field] = hist.Clone()
                field_hists_temp[field].Reset()
            s.draw_array(field_hists_temp, category, region, systematics=systematics,**kwargs)
            field_hists_list.append( field_hists_temp )

        ## reset the output histograms
        for field, hist in field_hists_list[0].items():
            hist_tot = hist.Clone()
            hist_tot.Reset()
            field_hist_tot[field] = hist_tot

        ## add the nominal histograms
        for field_hist in field_hists_list:
            for field, hist in field_hist.items():
                field_hist_tot[field].Add( hist )

        ## Systematic Uncertainties block
        if systematics:
            #--- loop over the dictionnary of the summed histograms
            for field,hist in field_hist_tot.items():
                # --- Add a dictionary to the nominal summed histogram
                if not hasattr( hist,'systematics'):
                    hist.systematics = {}
                # --- loop over the systematic uncercainties
                for sys in iter_systematics(self.samples_list[0].year):
                    if sys is 'NOMINAL':
                        continue
                    log.info ( "Fill the %s syst for the field %s" % (sys,field) )
                    # -- Create an histogram for each systematic uncertainty
                    hist.systematics[sys] =  hist.Clone()
                    hist.systematics[sys].Reset()
                    # -- loop over the samples and sum-up the syst-applied histograms
                    for field_hist_sample in field_hists_list:
                        field_hist_syst = field_hist_sample[field].systematics
                        hist.systematics[sys].Add( field_hist_syst[sys] )
        return
