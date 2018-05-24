# stdlib imports
import multiprocessing
from multiprocessing.managers import SyncManager
    

import random, time, os 
from collections import namedtuple

# local imports
from . import log
from . import samples
#from .samples import Higgs

from .cluster.parallel import FuncWorker, run_pool, map_pool

from .config import Configuration
import ROOT

##---------------------------------------------------------------------------------
## consts

##---------------------------------------------------------------------------------
## 
class Analysis():

    """ main analysis class.
    Attributes
    ----------
    use_embedding : bool(default=True)
                if True will use the tau-embedded ztautau for z-background,
    trigger : bool(default=True) 
          if True will use trigger.
    target_region: str(default='OS_ISOL')
                analysis signal region. see .region/* for more.  
    fakes_region: str(default='nOS_ISOL') 
               region for the fakes
    
    decouple_qcd_shape : bool(default=False)
                     if True, do the qcd shape systematics separately,
                     
    coherent_qcd_shape: bool(default=False)
                     if True, do the qcd shape systematics along side others.

    qcd_workspace_norm: float 
                     Val for qcd systmatics.

    ztt_workspace_norm: float 
                     Val,  for qcd systmatics.
                     
    constrain_norms: bool(default=False)
                  asks whether to set Low, High for systmatics.

    random_mu: bool(default=False)
            whether to set signal strength randomly or not, 
    mu:float(default=1.) 
     signal strength

    ggf_weight: bool(default=True)
             if True, weights the systematics.

    suffix: str
         specific suffix for analysis to be added to the output files name.
    
    norm_field: str
             variable used to normalize qcd, ztt
    """
    __HERE = os.path.dirname(os.path.abspath(__file__))
    CXX_MACROS = [
    "cxxmacros/FakeFactors/QCD/GetFF02_QCD.C",
    "cxxmacros/FakeFactors/QCD/GetFF01_QCD.C",
    "cxxmacros/FakeFactors/QCD/GetFF03_QCD.C",
    "cxxmacros/FakeFactors/WCR/GetFF02_WCR.C",
    "cxxmacros/FakeFactors/WCR/GetFF01_WCR.C",
    "cxxmacros/FakeFactors/WCR/GetFF03_WCR.C",
    "cxxmacros/FakeFactors/GetFFCombined.C",
    "cxxmacros/FakeFactors/GetFFCombined_up.C",
    "cxxmacros/FakeFactors/GetFFCombined_dn.C",
    "cxxmacros/FakeFactors/GetElFakeSF.C",
    ]
    CXX_MACROS = [os.path.join(__HERE, cm) for cm in CXX_MACROS]
    
    def __init__(self, config,
                 qcd_workspace_norm=None,
                 ztt_workspace_norm=None,
                 suffix=None,
                 use_embedding=False,
                 decouple_qcd_shape=False,
                 coherent_qcd_shape=True,
                 constrain_norms=False,
                 qcd_shape_systematic=True,
                 random_mu=False,
                 mu=1.):
        # - - - - - - - - main configurer 
        self.config = config 

        # - - - - - - - - loading and compiling cxx macros
        log.info("loading cxx macros ...")
        for cm in Analysis.CXX_MACROS:
            ROOT.gROOT.ProcessLine(".L %s"%cm)
        
        # - - - - - - - - some basic flags
        self.use_embedding = use_embedding
        self.suffix = suffix
        if random_mu:
            log.info("using a random mu (signal strength)")
            self.mu = random.uniform(10, 1000)
        else:
            log.info("using a mu (signal strength) of {0:.1f}".format(mu))
            self.mu = mu

        # - - - - - - - - analysis MC samples 
        if use_embedding:
            raise RuntimeError("Embedding is not ready yet!")
            log.info("Using embedded Ztautau")
            self.wtaunu = samples.Embedded_Wtaunu(
                self.config,
                workspace_norm=ztt_workspace_norm,
                constrain_norm=constrain_norms,
                color='#00A3FF')
        else:
            self.wtaunu = samples.Sh_Wtaunu(
                self.config,
                name='Wtaunu',
                label='W#rightarrow#tau#nu',
                color='#B00B71')
        self.ztautau = samples.Sh_Ztautau(
            self.config, 
            name='ZTauTau',
            label='Z#rightarrow#tau#tau',
            workspace_norm=ztt_workspace_norm,
            constrain_norm=constrain_norms,
            color='#157991')

        self.others = samples.Others(
            self.config, 
            name='Others',
            label='Others',
            color='#8A0F0F')
        self.diboson = samples.Diboson(
            self.config,
            name='DiBoson',
            label='DiBoson',
            color='#7D560C')
        
        self.top = samples.Top(self.config,
            name='Top',
            label='Top',
            color='#B0AF0B')
        
        self.zll = samples.Sh_Zll(
            self.config,
            name='Zll',
            label='Z#rightarrow ll',
            color='#061c44')
        
        self.wlnu = samples.Sh_Wlnu(
            self.config,
            name='Wlnu',
            label='W#rightarrow l#nu',
            color='#B00B71')
        
        # - - - - - - - - MC BKG components 
        self.mc = [
            self.top,
            self.wtaunu,
            self.zll,
            self.wlnu,
            self.ztautau,
            self.diboson,
            self.others,
            ]
        
        # - - - - - - - - DATA 
        self.data = samples.Data(self.config,
            name='Data1516',
            label='Data',
            markersize=1.2,
            linewidth=1)
        
        #WIP - - - - - - - - Fakes drived from FF method
        self.fakes = samples.Fakes(
            self.config, self.data, self.mc,
            name='Fakes',
            label='fakes',
            color='#f8970c')

        self.backgrounds = self.mc + [self.fakes]
        

        #WIP - - - - - - - - signals 
        #self.signals = self.get_signals(masses=self.config.signal_masses)
        
        
    def get_signals(self, masses=[], mode=None, scale=False):

        """ prepare signals for the analysis.
        Parameters
        ----------
        mass : list (default=[])
           signals masses.
        mode : str(default=None)
        scale : bool,(default=False)
                should we scale signal ?.

        Returns
        -------
        signals : a list of samples.Higgs objects.
        """
        signals = []
        if not isinstance(masses, list):
            masses = [masses]
        for m in masses:
            signals.append(samples.Higgs(
                year=self.config.year,
                channel=self.config.channel,
                mass=m,
                mode=mode,
                systematics=self.config.systematics,
                scale=self.mu,
                ggf_weight=self.ggf_weight))
            
        return signals

    def normalize(self, category):
        """ normalize qcd, ztautau.
        Parameters:
        -----------
        category : Category object, for more see ../catgories/__init__.py

        Returns
        -------
        self : updated object
        """
        
        return

    def iter_categories(self, category_names=None):
        """ A generator To iterate over categories, print the categories name and cuts on fly.
        Parameters
        ----------
        category_names: list
                  list of categorie names.
        Yiels:
        -------
        category : Category object
        """
        
        categories = self.config.categories

        for cat in categories:
            if category_names:
                if cat.name not in category_names:
                    continue
            log.debug("Selections & Weights ")
            log.debug("=" * 80)
            log.debug(cat)
            log.debug("Overl event weight: %r"%self.config.event_total_weight)
            log.debug("=" * 80)
                
            #self.normalize(category)
            yield cat

    def get_suffix(self):
        """ To prepare a string suffix for the final results/plots for each specific analysis.
        Parameters
        -----------
        year: bool(default=True); to label data11 as data12

        Returns
        --------
         output_suffix: str; output suffix
        """
        
        output_suffix += '_%d' % (self.config.year % 1000)
        if not self.config.systematics:
            output_suffix += '_stat'
        return  output_suffix

    
    def fit_norms(self, field, template, category,
                  max_iter=10, thresh=1e-7):
        """Derive the normalizations of ttbar and Wjets from a fit of some variable
        """
        raise RuntimeError("not implemented yet")
    

    @staticmethod
    def process(sample, category, systematic, fields=[], write_hists=True, **kwargs):
        return sample.hists(category,
                            fields=fields,
                            systematic=systematic,
                            write=write_hists)
    
    def run(self, categories=[], fields=[], systematics=[], write_hists=True):
        """run the analysis and produce the histograms.
        """
        if not categories:
            categories = self.config.categories
            log.info("processing all categories: {}".format(categories))

        if not fields:
            fields = self.config.varibales
            log.info("processing all variables: {}".format(fields))
        
        workers = []
        for sample in [self.data] + self.backgrounds:
            for systematic in ["NOMINAL"]:
                for cat in self.config.categories:
                    workers.append(FuncWorker(Analysis.process, sample, cat, systematic,
                                              fields=fields,write_hists=write_hists) )
                    
        log.info("submitting %i jobs . . ."%len(workers))
        start = float(time.time())
        run_pool(workers, n_jobs=-1)
        done = float(time.time())
        log.info("all jobs are done in {:0.2f} mins".format((done - start)/60.) )

