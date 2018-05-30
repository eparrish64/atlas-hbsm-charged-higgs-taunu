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
class Analysis:

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
        self.compile_cxx = compile_cxx
        if self.compile_cxx:
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
        
        self.top = samples.Top(
            self.config,
            name='Top',
            label='Top',
            pt_weighted=False,
            color=ROOT.kYellow)
        
        # - - - - - - - - MC BKG components 
        self.mc = [
            self.top,
            self.wtaunu,
            self.ztautau,
            self.diboson,
            # self.others, #<! super small
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
            self.config, self.mc,
            name='LepFakes',
            label='lep #rightarrow #tau',
            color=ROOT.kGreen+3)
        
        self.backgrounds = [self.qcd, self.lepfakes] + self.mc 
        
        #WIP - - - - - - - - signals 
        self.signals = []#self.get_signals(masses=self.config.signal_masses)
        
        
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
    def process(sample, category, systematic, fields=[], **kwargs):
        return sample.hists(category,
                            fields=fields,
                            systematic=systematic,
                            **kwargs)
    
    def run(self, categories=[], fields=[], systematics=[],
            write_hists = True, ofile=None, overwrite=True, **kwargs):
        """run the analysis and produce the histograms.
        """
        if not categories:
            categories = self.config.categories
        if not fields:
            fields = self.config.variables
        if not systematics:
            systematics = ["NOMINAL"]
        if not ofile:
            ofile = self.config.hists_file

        samples = [self.data] + self.backgrounds 
        log.info(" running the analysis with ...")
        log.info(" systematics: {}\n".format(systematics))
        log.info(" selections categories: {}\n".format(categories))
        log.info(" common MC weights: {}\n".format(self.wtaunu.weights ) )
        log.info(" variables: {}\n".format(fields) )

        #WIP: make it better
        workers = []
        for sample in samples:
            for systematic in systematics:
                for cat in categories:
                    workers.append(FuncWorker(Analysis.process, sample, cat, systematic,
                                              fields=fields, **kwargs))
                    
        log.info(" submitting %i jobs . . ."%len(workers))
        start = float(time.time())
        run_pool(workers, n_jobs=-1)
        hist_sets = [w.output for w in workers]
        hists = [item for sublist in hist_sets for item in sublist]

        if write_hists:
            log.info(" writing hist to disk . . . ")
            self.write_hists(hists, ofile, overwrite=overwrite)
                
        done = float(time.time())
        log.info(" all jobs are done in {:0.2f} mins".format((done - start)/60.) )


    def write_hists(self, hist_set, ofile, overwrite=True):
        """
        """
        tf = ROOT.TFile(ofile, "UPDATE")
        for hs in hist_set:
            hist = hs.hist
            systematic = hs.systematic
            sysdir = systematic
            if not tf.GetDirectory(sysdir):
                tf.mkdir(sysdir)
            tf.cd(sysdir)
            
            if overwrite:
                log.debug(" overwriting the existing hist")
                hist.Write(hist.GetName(), ROOT.TObject.kOverwrite)
            else:
                hist.Write(hist.GetName())
        tf.Close()
            
        return 
