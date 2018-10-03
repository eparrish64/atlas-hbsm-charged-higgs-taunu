## stdlib imports
import random, time, os , copy, pickle
import multiprocessing
from  array import array    
from collections import namedtuple, OrderedDict

## pypi
import yaml

## local imports
from db.datasets import Database

from . import log
from . import samples
from .samples.sample import Sample
from .dataset_hists import dataset_hists

from .samples import Higgs
from .categories import TAUID_MEDIUM, ANTI_TAU, TAU_IS_TRUE, TAU_IS_LEP_OR_HAD, Category
from .cluster.parallel import close_pool
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
     #FIXME should be exclusive to batch sub    specific suffix for analysis to be added to the output files name.
    
    norm_field: str
             variable used to normalize qcd, ztt
    """
    __HERE = os.path.dirname(os.path.abspath(__file__))
    CXX_MACROS = [
    # "FakeFactors/QCD/GetFF02_QCD.C",
    # "FakeFactors/QCD/GetFF01_QCD.C",
    # "FakeFactors/QCD/GetFF03_QCD.C",
    # "FakeFactors/WCR/GetFF02_WCR.C",
    # "FakeFactors/WCR/GetFF01_WCR.C",
    # "FakeFactors/WCR/GetFF03_WCR.C",
    # #"FakeFactors/GetFFCombined.C",
    # "FakeFactors/GetFFCombined_up.C",
    # "FakeFactors/GetFFCombined_dn.C",
    # "FakeFactors/GetElFakeSF.C",
        
    #"TriggerEfficiency/ApplyEff.C",
    "metTrigEff1516.cxx",
        
    # "GetTopPtWeight.C",

    # - - - - new (derived within the hpana and from r21 ntuples)
    "FakeFactors/FFs_COMBINED151617.cxx",
    "FakeFactors/FFs_CR151617.cxx",    

    # - - - - correction factor for tau polarization(only applied to 1 prong taus, upsilon varibale, and QCD sample)    
    "FakeFactors/CorrectUpsilon.C",
    "FakeFactors/CorrectUpsilon_1D_WCR.C",
    "FakeFactors/CorrectUpsilon_1D_QCD.C",
    ]
    CXX_MACROS = [os.path.join(__HERE, "cxxmacros", cm) for cm in CXX_MACROS]

    ROOT_CONF_FILES = [
        "TriggerEfficiency/met_efficiencies_lcw70.root",
        "TriggerEfficiency/met_efficiencies_mht110.root",
        "TriggerEfficiency/met_efficiencies_mht90.root",
    ]
    ROOT_CONF_FILES = [os.path.join(__HERE, "cxxmacros", cm) for cm in ROOT_CONF_FILES]
    
    def __init__(self, config,
                 suffix=None,
                 use_embedding=False,
                 compile_cxx=False,):
        # - - - - - - - - main configurer 
        self.config = config 

        # - - - - - - - - database
        self.database = Database(
            name="DB_%s"%self.config.channel, version=self.config.db_version, verbose=False)
            
        # - - - - - - - - loading and compiling cxx macros
        if compile_cxx:
            self.compile_cxx()

            # - - - - - - - - copy root config files to working dir
            for rf in Analysis.ROOT_CONF_FILES:
                os.system("cp %s %s"%(rf, os.getcwd()))
                
        # - - - - - - - - some basic flags
        self.use_embedding = use_embedding
        self.suffix = suffix
        
        # - - - - - - - - analysis MC samples 
        if use_embedding:
            raise RuntimeError("Embedding is not ready yet!")
            log.info("Using embedded W --> taunu")
            self.wtaunu = samples.Embedded_Wtaunu(
                self.config,
                database=self.database,
                name='Wtaunu',
                label='W#rightarrow#tau#nu',
                color=16)
        else:
            self.wtaunu = samples.Sh_Wtaunu(
                self.config,
                database=self.database,
                name='Wtaunu',
                label='W#rightarrow#tau#nu',
                color=16)
        self.wlnu = samples.Sh_Wlnu(
            self.config,
            database=self.database,
            name='Wlnu',
            label='W#rightarrow l#nu',
            color=14)
        
        self.ztautau = samples.Sh_Ztautau(
            self.config, 
            database=self.database,
            name='Ztautau',
            label='Z#rightarrow#tau#tau',
            color=ROOT.kYellow-1)
        self.zll = samples.Sh_Zll(
            self.config,
            database=self.database,
            name='Zll',
            label='Z#rightarrow ll',
            color=ROOT.kYellow-3)

        self.others = samples.Others(
            self.config, 
            database=self.database,
            name='Others',
            label='Others',
            color=ROOT.kViolet-2)
        self.diboson = samples.Diboson(
            self.config,
            database=self.database,
            name='DiBoson',
            label='DiBoson',
            color=ROOT.kViolet)
        
        self.ttbar = samples.TTbar(
            self.config,
            database=self.database,
            name='TTbar',
            label='t#bar{t}',
            pt_weighted=False,
            color=ROOT.kYellow)

        self.single_top = samples.Single_Top(
            self.config,
            database=self.database,
            name='SingleTop',
            label='single top',
            pt_weighted=False,
            color=ROOT.kOrange)
        
        # - - - - - - - - MC with prompt tau BKG components 
        self.mc = [
            self.ttbar,
            self.single_top,
            self.wtaunu,
            self.ztautau,
            self.diboson,
            self.zll, 
            self.wlnu,
            #self.others, #<! super small
            ]
        
        # - - - - - - - - DATA 
        self.data = samples.Data(
            self.config,
            database=self.database,
            name='Data',
            label='Data',
            markersize=1.2,
            blind=False,
            linewidth=1)
        
        # - - - - - - - - leptons faking a tau
        self.lepfakes = samples.LepFake(
            self.config, self.mc[:],
            name='LepFakes',
            label='lep #rightarrow #tau',
            color=ROOT.kGreen+3)
        
        # - - - - - - - - jets faking a tau
        self.qcd = samples.QCD(
            self.config, self.data, self.mc,
            name='QCD',
            label='jet #rightarrow #tau',
            color=ROOT.kAzure-9)

        
        self.backgrounds = [
            self.lepfakes,
            self.qcd,
            self.single_top,
            self.wtaunu,
            self.ztautau,
            self.diboson,
            self.ttbar,] 
        
        # - - - - - - - - signals 
        self.signals = self.get_signals(masses=[90, 110, 400])
        
        self.samples = [self.qcd, self.lepfakes] + self.mc + self.signals + [self.data]  
        
        # ---- stored workers
        self._workers=[]


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
        colors = [ROOT.kRed, ROOT.kGreen, ROOT.kBlue, ROOT.kOrange, ROOT.kMagenta]
        while len(masses) > len(colors):
            colors += colors
            
        for i, mass in enumerate(masses):
            signals.append(samples.Higgs(self.config,
                                         database=self.database,
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
    
    def setWorkers(self, samples=[], categories=[], fields=[], systematics=[], **kwargs):
        if len(self._workers)<1:
            self.workers(samples=samples, categories=categories, fields=fields, systematics=systematics, **kwargs)
        return 

    def getWorkers(self):
        if len(self._workers)<1:
            raise Exception("Worker list not defined in pickled analysis object")
        return self._workers

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
            
        self._workers  = []
        for sample in samples:
            self._workers += sample.workers(fields=fields, categories=categories, systematics=systematics, **kwargs)
        
        return self._workers
    
    def hists(self, samples=[], categories=[], fields=[], systematics=[], parallel=True, dry_run=False, **kwargs):
        """
        """
        workers = self.workers(
            samples=samples, categories=categories, fields=fields, systematics=systematics, **kwargs)
        log.debug(workers)
        hists = []
        if dry_run:
            log.info(workers)
            return 
        if parallel:
            log.info(
                "************** submitting %i jobs  ************"%len(workers))
            log.info(
                "***********************************************")

            pool = multiprocessing.Pool(multiprocessing.cpu_count())
            results = [pool.apply_async(dataset_hists, (wk,)) for wk in workers]
            # - - close the pool
            close_pool(pool)
            for res in results:
                hists += res.get(36000) #<! without the timeout this blocking call ignores all signals.
        else:
            for w in workers:
                hists += [dataset_hists(w)]
            
        # - - - - merge hists
        merged_hists = []
        for sample in samples:
            merged_hists += sample.merge_hists(hist_set=hists, write=False)
            
        return merged_hists
    
    def merge_hists(self, samples=[], hist_set=[], **kwargs):
        if samples:
            samples = filter(lambda s: s.name in samples, self.samples)
        else:
            samples = self.samples

        merged_hists = []
        for sample in samples:
            merged_hists += sample.merge_hists(hist_set=hist_set, **kwargs)
            
        return merged_hists

    def cutflow(self, cutflow_selections, samples=[], **kwargs):
        """ cutflow hists sets for different samples.
        """
        # - - - - Histset container
        cutflow_hist_sets = []
        
        field = kwargs.pop("field", self.config.variables[0])
        if not samples:
            samples = self.samples

        # - - - - simulated samples 
        sim_samples =  self.mc + [self.lepfakes] + self.signals
        sim_samples = filter(lambda s: s.name in [s.name for s in samples], sim_samples)
        
        categories = []
        cuts_list = []
        for name, cut in cutflow_selections.iteritems():
            if name.upper()=="TRIGGER":
                cut = {self.config.mc_camp: self.config.trigger(dtype="MC") }
            cuts_list += [cut]
            categories.append(Category(name, cuts_list=cuts_list, mc_camp=self.config.mc_camp))

        if sim_samples:    
            cutflow_hist_sets += self.hists(
                samples=sim_samples, categories=categories, fields=[field], systematics=["NOMINAL"], **kwargs)
        
        # - - - - treat QCD seperatly (due to different TAU ID)
        if self.qcd.name in [s.name for s in samples]:
            cutflow_hist_sets += self.qcd.cutflow(cutflow_selections, **kwargs)
            
        if self.data.name in [s.name for s in samples]:
            cutflow_hist_sets += self.data.cutflow(cutflow_selections, **kwargs)
        
        return cutflow_hist_sets
    
    def cache_ffs(self,
                  template_fields=[],
                  template_hist=None,
                  template_hist_bins=[],
                  control_regions=[],
                  tau_jet_bdt_score_trans_wps=[0.01, 0.02, 0.03],
                  n_charged_tracks=[1, 3],
                  trigger=None,
                  tauid=None, 
                  antitau=None,
                  subtract_mc=True,
                  cache_file=None,
                  write_cxx_macro=True,
                  validation_plots=False,
                  pdir="ffplots"):
        """
        FF = N_tau/N_antitau where N_tau/antitau = N_tau/anittau(DATA) - N_tau/antitau(MC) 
        for MC where tau fails tau ID but is truth matched to an electron or a tau.
        Then 
        These factors then will be evaluated in other selection regions based on the fraction of q/g jets faking taus.

        Parameters
        - - - - - 
        template_hist: 
            Variable type; see .variables.py
        template_hist_bins:
            list type; bins for template fit
        control_regions:
            [Categories] type; contorl regions for the FF extraction.
        tauid:
            {ROOT.TCut()} type; tauID selection cut
        antitau:
            {ROOT.TCut()} type; anti tau selection cut
        min_tau_jet_bdt_score_trans_wps: 
            list type; working points for tau_jet_bdt_score_trans 
        """
        # - - - - set the mc_camp property
        for f in template_fields:
            f.mc_camp = self.config.mc_camp
        
        if not template_hist:
            if template_fields:
                assert len(template_fields)==3, "wrong number of fields"
                template_hist = {
                    #<! PLS NOTE that the tformula order is Z:Y:X and for the binning it's X, Y, Z !
                    template_fields[0].name: ROOT.TH3F("{0} : {1} : {2}".format(*(v.tformula for v in template_fields)),
                                                       "Z%s_Y%s_X%s".format(*(v.name for v in template_fields)),
                                                       100, 0., 1., 4, 0, 4, 800, 0, 4000),}
            else:
                raise ValueError("template_hist or fields arg is needed")
            
        if not tauid:
            tauid = self.config.tauid
            
        if not antitau:
            # - - - - PLEASE NOTE THAT tau_0_jet_bdt_score_sig cut is included in the template hist
            antitau = ROOT.TCut("tau_0_jet_bdt_loose==0")
            
        if not control_regions:
            control_regions = self.config.ff_cr_regions

        # - - - -  deep copy control_regions as we want to update the cuts attribute on them
        tau_control_regions = copy.deepcopy(control_regions)
        antitau_control_regions = copy.deepcopy(control_regions)
        for cr in tau_control_regions:
            cr.tauid = tauid
            cr.truth_tau = TAU_IS_LEP_OR_HAD
        
        for acr in antitau_control_regions:
            acr.tauid = antitau
            acr.truth_tau = TAU_IS_TRUE #<! a true tau that's failing tau ID

            
        # - - - - parallel processing
        workers = []
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        
        # - - - - DATA workers
        data_tau_workers = self.data.workers(
            fields=template_fields[:1], hist_templates=template_hist,
            categories=tau_control_regions, trigger=trigger,)
        # - - make worker names unique 
        for w in data_tau_workers:
            w.name += "_TAU"
        workers += data_tau_workers
            
        data_antitau_workers = self.data.workers(
            fields=template_fields[:1], hist_templates=template_hist,
            categories=antitau_control_regions, trigger=trigger,)
        for w in data_antitau_workers:
            w.name += "_ANTITAU"
        workers += data_antitau_workers
        
        if subtract_mc:
            # - - - - MC workers
            mc_tau_workers = []
            mc_antitau_workers = []
            for mc in self.mc:
                mc_tau_workers += mc.workers(
                    fields=template_fields[:1], hist_templates=template_hist,
                    categories=tau_control_regions, trigger=trigger)

                # - - taus not passing nominal tau ID (medium)
                not_tau = ROOT.TCut("!%s"%self.config.tauid.GetTitle())
                mc_antitau_workers += mc.workers(
                    fields=template_fields[:1], hist_templates=template_hist,
                    categories=antitau_control_regions, trigger=trigger,)

            # add mc tau/antitau  workers to the list of all workers
            for w in mc_tau_workers:
                w.name += "_TAU"
            workers += mc_tau_workers

            for w in mc_antitau_workers:
                w.name += "_ANTITAU"
            workers += mc_antitau_workers

        # - - - - workers do some work please :D
        log.info(
            "************** submitting %i jobs  ************"%len(workers))
        log.info(
            "***********************************************")
        rand_workers = [ workers[i] for i in sorted(random.sample(xrange(len(workers)), min(20, len(workers) ) ) ) ]
        log.debug(rand_workers)
        results = [pool.apply_async(dataset_hists, args=(w,)) for w in workers]
        
        hist_sets = []
        for res in results:
            hist_sets += res.get(36000)
        # - - - - close the pool
        close_pool(pool)

        # - - - -  organize the output
        data_tau_hists = filter(lambda hs: hs.name.startswith(self.data.name) and hs.name.endswith("_TAU"), hist_sets)
        data_antitau_hists = filter(lambda hs: hs.name.startswith(self.data.name) and hs.name.endswith("_ANTITAU"), hist_sets)

        if subtract_mc:
            mc_tau_hists = filter(lambda hs: not hs.name.startswith(self.data.name) and hs.name.endswith("_TAU"), hist_sets)
            mc_antitau_hists = filter(lambda hs: not hs.name.startswith(self.data.name) and hs.name.endswith("_ANTITAU"), hist_sets)
        
        # - - - - add up the histograms for each CR region 
        ffs_dict = {}
        for cr in control_regions:
            cr_name = cr.name
            ffs_dict[cr_name] = OrderedDict()
            
            # - - data tau
            data_tau_hists_cat = filter(lambda hs: hs.category==cr_name, data_tau_hists)
            assert data_tau_hists_cat, "no (TAU) %s hist for %s CR"%(self.data.name, cr_name)
            data_tau_hsum = data_tau_hists_cat[0].hist.Clone()
            if len(data_tau_hists_cat) > 1:
                for hs in data_tau_hists_cat[1:]:
                    data_tau_hsum.Add(hs.hist)
            
            # - - data antitau
            data_antitau_hists_cat = filter(lambda hs: hs.category==cr_name, data_antitau_hists)
            assert data_antitau_hists_cat, "no (ANTITAU) %s hist for %s CR"%(self.data.name, cr_name)
            data_antitau_hsum = data_antitau_hists_cat[0].hist.Clone()
            if len(data_antitau_hists_cat) > 1:
                for hs in data_antitau_hists_cat[1:]:
                    data_antitau_hsum.Add(hs.hist)

            if subtract_mc:
                # - - mc tau
                mc_tau_hists_cat = filter(lambda hs: hs.category==cr_name, mc_tau_hists)
                assert mc_tau_hists_cat, "no (TAU) %s hist for %s CR"%("MC", cr_name)
                mc_tau_hsum = mc_tau_hists_cat[0].hist.Clone()
                for hs in mc_tau_hists_cat[1:]:
                    mc_tau_hsum.Add(hs.hist)

                # - - mc antitau
                mc_antitau_hists_cat = filter(lambda hs: hs.category==cr_name, mc_antitau_hists)
                assert mc_antitau_hists_cat, "no (ANTITAU) %s hist for %s CR"%("MC", cr_name)
                mc_antitau_hsum = mc_antitau_hists_cat[0].hist.Clone()
                for hs in mc_antitau_hists_cat[1:]:
                    mc_antitau_hsum.Add(hs.hist)
                    
            data_mc_tau_h = data_tau_hsum.Clone()
            data_mc_antitau_h = data_antitau_hsum.Clone()
            # - - subtract MC from DATA
            if subtract_mc:
                data_mc_tau_h.Add(mc_tau_hsum, -1)
                data_mc_antitau_h.Add(mc_antitau_hsum, -1)
            
            log.info("TAU events; DATA: {}, MC: {}".format(
                data_tau_hsum.Integral(), mc_tau_hsum.Integral() if subtract_mc else "NAN") )
            log.info("ANTITAU events; DATA: {}, MC: {}".format(
                data_antitau_hsum.Integral(), mc_antitau_hsum.Integral() if subtract_mc else "NAN") )

            htmp_tau = data_mc_tau_h.Clone()
            htmp_antitau = data_mc_antitau_h.Clone()
            
            # - - project along X and Y to get the bins
            htmp_X = htmp_antitau.ProjectionX().Clone()
            htmp_Y = htmp_antitau.ProjectionY().Clone()
            htmp_Z = htmp_antitau.ProjectionZ().Clone()
            
            if validation_plots:
                os.system("mkdir -p %s"%pdir)
                canvas = ROOT.TCanvas()
                
                htmp_tau.Draw("")
                canvas.Print("%s/h3_tau.png"%pdir)
                canvas.Clear()

                htmp_antitau.Draw("")
                canvas.Print("%s/h3_antitau.png"%pdir)
                canvas.Clear()

                htmp_X.Draw()
                canvas.Print("%s/hX_antitau.png"%pdir)
                canvas.Clear()

                htmp_Y.Draw()
                canvas.Print("%s/hY_antitau.png"%pdir)
                canvas.Clear()

                htmp_Z.Draw()
                canvas.Print("%s/hZ_antitau.png"%pdir)
                canvas.Clear()

                canvas.Close()
            
            # - - gather hists per tau pT and ntracks bin and also tau_jet_bdt_score WPs
            for jbs_n, jbs_wp in enumerate(tau_jet_bdt_score_trans_wps):
                jkey = "tauJetBDT_0%i"%(100*jbs_wp)
                ffs_dict[cr_name][jkey] = {}
                for itk_n, itk in enumerate(n_charged_tracks):
                    tkey = "%i"%itk
                    ffs_dict[cr_name][jkey][tkey]= {}
                    
                    # - - keep jet BDT score along X (only a lower cut)
                    x_low = htmp_X.FindBin(jbs_wp)
                    x_high = -1 #<! to include overflow bin too
                    
                    # - - ntracks along Y
                    y_low = htmp_Y.FindBin(itk)
                    y_high = htmp_Y.FindBin(itk)+1
                    
                    # - - fitting bins for the actual shape variable
                    fitting_bins = template_hist_bins[tkey]
                    for _bin in range(1, len(fitting_bins)):
                        pkey = "%i"%fitting_bins[_bin]
                        z_low = htmp_Z.FindBin(fitting_bins[_bin-1])
                        z_high = htmp_Z.FindBin(fitting_bins[_bin])-1

                        tau_bin_cont = htmp_tau.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                        antitau_bin_cont = htmp_antitau.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                        if antitau_bin_cont==0:
                            log.warning("{} bin for antitau is empty, setting tau/antitau to 1!".format(pkey))
                            tau_antitau_ratio = 1.
                        else:
                            tau_antitau_ratio = "%.6f"%(tau_bin_cont/float(antitau_bin_cont))
                        ffs_dict[cr_name][jkey][tkey][pkey] = tau_antitau_ratio
                        
                        log.debug("bins: {}".format((x_low, x_high, y_low, y_high, z_low, z_high)))
                        log.debug("ratio in << {}  >> bin: tau:{}, antitau: {}, ratio: {} ".format(
                            (jkey, tkey, pkey), tau_bin_cont, antitau_bin_cont, tau_antitau_ratio))
                        log.debug("--"*60)
                        
            # - - clean up
            htmp_X.Delete()
            htmp_Y.Delete()
            htmp_Z.Delete()
            htmp_tau.Delete()
            htmp_antitau.Delete()
                    
        if not cache_file:
            cache_file = os.path.join(Analysis.__HERE, "cache", "FFs_CR.yml")
            if not os.path.isdir("%s/cache"%(Analysis.__HERE)):
                os.system("mkdir -p %s/cache"%Analysis.__HERE)
        else:
            yml_file = cache_file
            
        with open (yml_file, "a") as yml_cache:
            log.info("caching the fake factors")
            yaml.dump(ffs_dict, yml_cache, default_flow_style=False)

        log.info("FFs: {} ".format(ffs_dict))

        if write_cxx_macro:
            if yml_file.endswith(".yml"): 
                cxx_file = yml_file.replace(".yml", ".cxx")
            else:
                cxx_file = yml_file + ".cxx"
                
            with open(cxx_file, "a") as cxx_cache:
                cxx_cache.write("#include <iostream>\n")
                for cr in [c.name for c in control_regions]:
                    for jbs_n, jbs_wp in enumerate(tau_jet_bdt_score_trans_wps):
                        jkey = "tauJetBDT_0%i"%(100*jbs_wp)
                        cxx_cache.write("//! tau_0_jet_bdt_score_trans lower cut ({})\n".format(jbs_wp))
                        cxx_cache.write(
                            "float GetFF0{0}_{1}(float pt, int nTracks){{\n".format(int(100*jbs_wp), cr) )
                        for itk in n_charged_tracks:
                            tkey = "%i"%itk
                            cxx_cache.write("\t if(nTracks==%i){\n"%itk)
                            for pT in template_hist_bins[tkey][1:]:
                                pkey = "%i"%pT
                                ff = ffs_dict[cr][jkey][tkey][pkey]
                                cxx_cache.write("\t\t if(pt < {0}) return {1};\n".format(pT, ff))

                            # - - - -  close ntracks block   
                            cxx_cache.write("\t\t else return 0;\n")   
                            cxx_cache.write("\t\t }\n")

                        # - - - - close tauJetBDTscore block
                        cxx_cache.write("\t else return 0;\n")   
                        cxx_cache.write("}\n\n\n")
                 
        return ffs_dict
    
