## stdlib imports
import multiprocessing
from multiprocessing.managers import SyncManager
from  array import array    
import random, time, os 
from collections import namedtuple

## pypi
import yaml

## local imports
from . import log
from . import samples
from .samples.sample import Sample
from .dataset_hists import dataset_hists

from .samples import Higgs
from .categories import TAUID_MEDIUM, ANTI_TAU
from .cluster.parallel import FuncWorker, run_pool, map_pool
from .config import Configuration
import ROOT


##---------------------------------------------------------------------------------
## main analysis class
##---------------------------------------------------------------------------------
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
        
    "FakeFactors/CorrectUpsilon.C",
    "FakeFactors/CorrectUpsilon_1D_WCR.C",
    "FakeFactors/CorrectUpsilon_1D_QCD.C",    
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
        self.signals = self.get_signals(masses=[90, 110, 400])
        
        self.samples = [self.qcd, self.lepfakes] + self.mc + self.signals + [self.data]  

    def compile_cxx(self):
        log.info("loading cxx macros ...")
        for cm in Analysis.CXX_MACROS:
            ROOT.gROOT.ProcessLine(".L %s"%cm)

        
    def get_signals(self, masses=[], scale=1):

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
        if not masses:
            masses = Higgs.MASSES.keys()
        if not isinstance(masses, (list, tuple)):
            masses = [masses]
            
        signals = []
        colors = [ROOT.kRed, ROOT.kGreen, ROOT.kBlue]
        for i, mass in enumerate(masses):
            signals.append(samples.Higgs(self.config,
                                         mass=mass,
                                         scale=scale,
                                         color=colors[i], line_style=2*i))
            
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

    def workers(self, samples=[], categories=[], fields=[], systematics=[], **kwargs):
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
            _workers += sample.workers(fields=fields, categories=categories, systematics=systematics, **kwargs)
                
        return _workers
    
    def hists(self, samples=[], categories=[], fields=[], systematics=[], **kwargs):
        """
        """
        workers = self.workers(samples=samples, categories=categories, fields=fields, systematics=systematics, **kwargs)
        log.debug(workers)

        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = [pool.apply_async(dataset_hists, (wk,)) for wk in workers]
        hists = []
        for res in results:
            hists += res.get()
            
        # - - - - merge hists
        merged_hists = []
        for sample in samples:
            merged_hists += sample.merge_hists(hist_set=hists, write=False)
            
        return merged_hists
    
    def merge_hists(self, samples=[], hist_set=[],**kwargs):
        if samples:
            samples = filter(lambda s: s.name in samples, self.samples)
        else:
            samples = self.samples

        merged_hists = []
        for sample in samples:
            merged_hists += sample.merge_hists(hist_set=hist_set, **kwargs)
            
        return merged_hists

    def cache_ffs(self,
                  template_var=None,
                  template_var_bins=[],
                  target_regions=[],
                  control_regions=[],
                  min_tau_jet_bdt_score_trans=0.01,
                  tau_jet_bdt_score_trans_var="tau_jet_bdt_score_trans",
                  n_charged_tracks=None, 
                  tauid=None, 
                  antitau=None,
                  cache_file=None):
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

        # - - - - FF s are different for 1p/3p taus
        if not n_charged_tracks:
            raise RuntimeError("you have to specify the number of charged tracks cut")
            
        # - - - - tau jet bdt score signal transformed cut threshold
        tau_jet_bdt_score_trans_cut = ROOT.TCut("{0} > {1}".format(
            tau_jet_bdt_score_trans_var, min_tau_jet_bdt_score_trans))
        
        if not target_regions:
            target_regions = self.config.categories

        if not control_regions:
            control_regions = self.config.ff_cr_regions

        # - - - -  deep copy control_regions as we want to update the cuts attribute on them
        control_regions = copy.deepcopy(control_regions)
        
        if not tauid:
            tauid = self.config.tauid
            
        if not antitau:
            antitau = self.config.antitau
            
        if not template_var:
            template_var = self.config.variables[0]
        else:
            assert template_var.name in [v.name for v in self.config.variables], "%r is not defined!"%template_var
        if not template_var_bins:
            # - - default for tau pt 
            template_var_bins = [30, 35, 40, 45, 50, 60, 75, 90, 105, 120, 140, 160, 200, 300, 3500]
        template_var.bins = template_var_bins

        # - - - - parallel processing
        pool = multiprocessing.Pool()
        workers = []
        
        # - - - - DATA workers
        data_tau_workers = self.data.workers(fields=[template_var], categories=control_regions, tauid=tauid)
        # - - make workers names unique 
        for w in data_tau_workers:
            w.name += "_TAU"
        workers += data_tau_workers
            
        data_antitau_workers = self.data.workers(fields=[template_var], categories=control_regions, tauid=antitau)
        for w in data_antitau_workers:
            w.name += "_ANTITAU"
        workers += data_antitau_workers
                
        # - - - - MC workers
        mc_tau_workers = []
        mc_antitau_workers = []
        for mc in self.mc:
            mc_tau_workers += mc.workers(fields=[template_var],categories=control_regions, tauid=tauid)
            mc_antitau_workers += mc.workers(fields=[template_var],categories=control_regions, tauid=antitau)

        # add mc tau/antitau  workers to the list of all workers
        for w in mc_tau_workers:
            w.name += "_TAU"
        workers += mc_tau_workers

        for w in mc_antitau_workers:
            w.name += "_ANTITAU"
        workers += mc_antitau_workers

        # - - - - workers do some work please :D
        rand_workers = [ workers[i] for i in sorted(random.sample(xrange(len(workers)), 20)) ]
        results = [pool.apply_async(dataset_hists, args=(w,)) for w in rand_workers]

        hist_sets = [r.get() for r in results]
        hist_sets = [item for sublist in hist_sets for item in sublist]

        # - - - -  organize the output
        data_tau_hists = filter(lambda hs: hs.name.startswith(self.data.name) and hs.name.endswith("TAU"), hist_sets)
        data_antitau_hists = filter(lambda hs: hs.name.startswith(self.data.name) and hs.name.endswith("ANTITAU"), hist_sets)
        
        mc_tau_hists = filter(lambda hs: not hs.name.startswith(self.data.name) and hs.name.endswith("TAU"), hist_sets)
        mc_antitau_hists = filter(lambda hs: not hs.name.startswith(self.data.name) and hs.name.endswith("ANTITAU"), hist_sets)

        # - - - - add up the histograms for each CR region 
        hists = {}
        for cr in control_regions:
            cr_name = cr.name
            hists[cr_name] = {"TAU":{}, "ANTITAU":{}}
                
            # - - data tau
            data_tau_hists_cat = filter(lambda hs: hs.category==cr_name, data_tau_hists)
            assert data_tau_hists_cat, "no (TAU) %s hist for %s CR"%(self.data.name, cr_name)
            data_tau_hsum = reduce(lambda h1, h2: h1 + h2, [dh.hist for dh in data_tau_hists])
            
            # - - data antitau
            data_antitau_hists_cat = filter(lambda hs: hs.category==cr_name, data_antitau_hists)
            assert data_antitau_hists_cat, "no (ANTITAU) %s hist for %s CR"%(self.data.name, cr_name)
            data_antitau_hsum = reduce(lambda h1, h2: h1 + h2, [dh.hist for dh in data_antitau_hists])
            
            # - - mc tau
            mc_tau_hists_cat = filter(lambda hs: hs.category==cr_name, mc_tau_hists)
            assert mc_tau_hists_cat, "no (TAU) %s hist for %s CR"%("MC", cr_name)
            mc_tau_hsum = reduce(lambda h1, h2: h1 + h2, [dh.hist for dh in mc_tau_hists])

            # - - mc antitau
            mc_antitau_hists_cat = filter(lambda hs: hs.category==cr_name, mc_antitau_hists)
            assert mc_antitau_hists_cat, "no (ANTITAU) %s hist for %s CR"%("MC", cr_name)
            mc_antitau_hsum = reduce(lambda h1, h2: h1 + h2, [dh.hist for dh in mc_antitau_hists])
            
            # - - subtract MC from DATA
            hists[cr_name]["TAU"] = data_tau_hsum - mc_tau_hsum
            hists[cr_name]["ANTITAU"] = data_antitau_hsum - mc_antitau_hsum

        # - - - - rebin the histograms 
        rebinned_hists = {}
        for cr, tp  in hists.iteritems():
            rebinned_hists[cr] = {"TAU":{}, "ANTITAU":{}}
            for t, h in tp.iteritems():
                hr = h.Rebin(len(template_var_bins) -1, h.GetName(), array("d", template_var_bins))
                rebinned_hists[cr][t] = hr 

        ffs_dict = {}
        for cr in [c.name for c in control_regions]:
            ffs_dict[cr] = {}
            for i, cbin in enumerate(template_var_bins):
                # - - get the ratio of tau to antitau for this bin
                tau_bin = rebinned_hists[cr]["TAU"].GetBinContent(i)
                antitau_bin = rebinned_hists[cr]["ANTITAU"].GetBinContent(i)
                if antitau_bin==0:
                    log.warning("% i bin for antitau is empty!"%cbin)
                    tau_antitau_ratio = 1
                else:
                    tau_antitau_ratio = tau_bin/antitau_bin
                ffs_dict[cr][cbin] = tau_antitau_ratio

        if not cache_file:
            cache_file = os.path.join(Analysis.__HERE, "cache", "FF_CR.pkl")
            if not os.path.isdir("%s/cache"%(Analysis.__HERE)):
                os.system("mkdir -p %s/cache"%Analysis.__HERE)
            
        with open (cache_file, "w") as cache:
            log.info("caching the fake factors")
            pickle.dump(ffs_dict, cache)
        
        return ffs_dict 
    
