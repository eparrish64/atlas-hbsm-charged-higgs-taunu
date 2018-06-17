# stdlib imports
import multiprocessing
from multiprocessing.managers import SyncManager
    

import random, time, os 
from collections import namedtuple

# local imports
from . import log
from . import samples
from .samples.sample import Sample
from .dataset_hists import dataset_hists

#from .samples import Higgs
from .categories import TAUID_MEDIUM, ANTI_TAU
from .cluster.parallel import FuncWorker, run_pool, map_pool
from .config import Configuration
import ROOT

##---------------------------------------------------------------------------------
## consts

##---------------------------------------------------------------------------------
## 
class Analysis(object):

    """ main analysis class.
    Attributes
    ----------
    use_embedding : bool(default=True)
                if True will use the tau-embedded ztautau for z-background,

    random_mu: bool(default=False)
            whether to set signal strength randomly or not, 
    mu:float(default=1.) 
     signal strength

    suffix: str
         specific suffix for analysis to be added to the output files name.
    
    norm_field: str
             variable used to normalize qcd, ztt
    """
    __HERE = os.path.dirname(os.path.abspath(__file__))
    CXX_MACROS = [
    "FakeFactors/QCD/GetFF02_QCD.C",
    "FakeFactors/QCD/GetFF01_QCD.C",
    "FakeFactors/QCD/GetFF03_QCD.C",
    "FakeFactors/WCR/GetFF02_WCR.C",
    "FakeFactors/WCR/GetFF01_WCR.C",
    "FakeFactors/WCR/GetFF03_WCR.C",
    "FakeFactors/GetFFCombined.C",
    "FakeFactors/GetFFCombined_up.C",
    "FakeFactors/GetFFCombined_dn.C",
    "FakeFactors/GetElFakeSF.C",
        
    "TriggerEfficiency/ApplyEff.C",
    "GetTopPtWeight.C",
    ]
    CXX_MACROS = [os.path.join(__HERE, "cxxmacros", cm) for cm in CXX_MACROS]
    
    def __init__(self, config,
                 suffix=None,
                 use_embedding=False,
                 random_mu=False,
                 compile_cxx=False,
                 mu=1.):
        # - - - - - - - - main configurer 
        self.config = config 

        # - - - - - - - - loading and compiling cxx macros
        if compile_cxx:
            self.compile_cxx()
            
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
                name='Wtaunu',
                label='W#rightarrow#tau#nu',
                color=16)
        else:
            self.wtaunu = samples.Sh_Wtaunu(
                self.config,
                name='Wtaunu',
                label='W#rightarrow#tau#nu',
                color=16)
        self.wlnu = samples.Sh_Wlnu(
            self.config,
            name='Wlnu',
            label='W#rightarrow l#nu',
            color=14)
        
        self.ztautau = samples.Sh_Ztautau(
            self.config, 
            name='Ztautau',
            label='Z#rightarrow#tau#tau',
            color=ROOT.kYellow-1)
        self.zll = samples.Sh_Zll(
            self.config,
            name='Zll',
            label='Z#rightarrow ll',
            color=ROOT.kYellow-3)

        self.others = samples.Others(
            self.config, 
            name='Others',
            label='Others',
            color=ROOT.kViolet-2)
        self.diboson = samples.Diboson(
            self.config,
            name='DiBoson',
            label='DiBoson',
            color=ROOT.kViolet)
        
        self.ttbar = samples.TTbar(
            self.config,
            name='TTbar',
            label='t#bar{t}',
            pt_weighted=False,
            color=ROOT.kYellow)

        self.single_top = samples.Single_Top(
            self.config,
            name='SingleTop',
            label='single top',
            pt_weighted=False,
            color=ROOT.kOrange)
        
        # - - - - - - - - MC BKG components 
        self.mc = [
            self.ttbar,
            self.single_top,
            self.wtaunu,
            self.ztautau,
            self.diboson,
            self.zll, 
            self.wlnu,
            self.others, #<! super small
            ]
        
        # - - - - - - - - DATA 
        self.data = samples.Data(
            self.config,
            name='Data',
            label='Data',
            markersize=1.2,
            blind=False,
            linewidth=1)
        
        # - - - - - - - - jets faking a tau
        self.qcd = samples.QCD(
            self.config, self.data, self.mc,
            name='QCD',
            label='jet #rightarrow #tau',
            color=ROOT.kAzure-9)

        # - - - - - - - - leptons faking a tau
        self.lepfakes = samples.LepFake(
            self.config, self.mc[:], #<! defensive copy 
            name='LepFakes',
            label='lep #rightarrow #tau',
            color=ROOT.kGreen+3)
        
        self.backgrounds = [
            self.lepfakes,
            self.qcd,
            self.ttbar,
            self.single_top,
            self.wtaunu,
            self.ztautau,
            self.diboson,] 
        
        #WIP - - - - - - - - signals 
        self.signals = [] #self.get_signals(masses=self.config.signal_masses)
        
        self.samples = [self.qcd, self.lepfakes] + self.mc + self.signals + [self.data]  

    def compile_cxx(self):
        log.info("loading cxx macros ...")
        for cm in Analysis.CXX_MACROS:
            ROOT.gROOT.ProcessLine(".L %s"%cm)

        
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

    def workers(self, samples=[], categories=[], fields=[], systematics=[]):
        """
        """
        
        if not samples:
            samples = self.samples
            
        if not fields:
            fields = self.config.variables
            
        if not categories:
            categories = self.config.categories
            
        if not systematics:
            systematics = ["NOMINAL"]
            
        _workers  = []
        for sample in samples:
            _workers += sample.workers(
                fields=fields,
                categories=categories,
                systematics=systematics)
                
        return _workers
    
    
    def merge_hists(self, samples=[], **kwargs):
        if samples:
            samples = filter(lambda s: s.name in samples, self.samples)
        else:
            samples = self.samples
            
        for sample in samples:
            sample.merge_hists(**kwargs)
            
        return 

    def cache_ffs(self,
                  template_var=None,
                  template_var_bins = [
                      30, 35, 40, 45, 50, 60, 75,
                      90, 105, 120, 140, 160, 200, 300, 3500],
                  target_regions=[],
                  control_regions=[],
                  tauid=None,
                  antitau=None):
        """ calculate and cache the fake factors.
        Parameters
        - - - - - 
        template_var: 
            Variable type; see .variables.py
        template_var_bins:
            list type; bins for template fit
        target_regions:
            [Categories] type; see .categories.py.
        control_regions:
            [Categories] type; contorl regions for the FF extraction.
        tauid:
            {ROOT.TCut()} type; tauID selection cut
        antitau:
            {ROOT.TCut()} type; anti tau selection cut
        """
        
        if not target_regions:
            target_regions = self.config.categories

        if not control_regions:
            control_regions = filter(lambda cat: cat.name in ["QCD", "BVETO"], self.config.categories)
            
        if not template_var:
            template_var = self.config.variables[0]
        else:
            assert template_var.name in [v.name for v in self.config.variables], "%r is not defined!"%template_var

        if not tauid:
            tauid = self.config.tauid
            
        if not antitau:
            antitau = self.config.antitau

        pool = multiprocessing.Pool()
        # - - DATA workers
        data_tau_workers = self.data.workers(fields=[template_var],
                                             categories=control_regions,
                                             tauid=tauid)
        data_antitau_workers = self.data.workers(fields=[template_var],
                                                 categories=control_regions,
                                                 tauid=antitau)
        # - - MC workers
        mc_workers = []
        for mc in self.mc:
            mc_workers += mc.workers(fields=[template_var],categories=control_regions, tauid=tauid)
            
        # - - - - taus (passing tau ID) in data
        data_tau_results = [pool.apply_async(dataset_hists, args=(dw,)) for dw in data_tau_workers[:100]]
        data_tau_hists = []
        for hs in data_tau_results:
            data_tau_hists += hs.get()
        data_tau_hsum = reduce(lambda h1, h2: h1 + h2, [dh.hist for dh in data_tau_hists])

        # - - - - antitau in data
        data_antitau_results = [pool.apply_async(dataset_hists, args=(dw,)) for dw in data_antitau_workers[:100]]
        data_antitau_hists = []
        for hs in data_antitau_results:
            data_antitau_hists += hs.get()
        data_antitau_hsum = reduce(lambda h1, h2: h1 + h2, [dh.hist for dh in data_antitau_hists])

        #WIP:
        raise RuntimeError("not fully implemented yet!")
