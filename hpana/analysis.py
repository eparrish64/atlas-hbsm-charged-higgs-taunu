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
from .config import Configuration

## ROOT
import ROOT


##---------------------------------------------------------------------------------
## main analysis class
##---------------------------------------------------------------------------------
class Analysis(object):
    """ main analysis class.
    """
    __HERE = os.path.dirname(os.path.abspath(__file__))
    
    def __init__(self, config, suffix=None, compile_cxx=False,):
        # - - main configuration object 
        self.config = config 
        self.suffix = suffix
        self.cxx_macros = self.config.metTrigEff_macros + self.config.FFs_macros + self.config.upsilon_macros + self.config.effm_taujet_macros + self.config.effm_taulep_macros + self.config.njets_macros

        # - - loading and compiling cxx macros
        if compile_cxx:
            self.compile_cxx()
            # - - copy root config files to working dir
            for rf in [os.path.join(Analysis.__HERE, "cxxmacros", rc) for rc in self.config.root_conf_files]:
                os.system("cp %s %s"%(rf, os.getcwd()))

        ## analysis samples            
        self.wtaunu = samples.Sh_Wtaunu(
            self.config,
            name='Wtaunu',
            label='W#rightarrow#tau#nu',
            njets=True,
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
            color=ROOT.kBlue-10)
        
        self.ttbar = samples.TTbar(
            self.config,
            name='TTbar',
            label='t#bar{t}',
            effm_weighted=True,
            pt_weighted=False,
            color=ROOT.kYellow-7)

        self.single_top = samples.Single_Top(
            self.config,
            name='SingleTop',
            label='single top',
            effm_weighted=False,
            pt_weighted=False,
            color=ROOT.kOrange)
        
        # - - MC with prompt tau BKG components 
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
        
        # - - DATA 
        self.data = samples.Data(
            self.config,
            name='Data',
            label='Data',
            markersize=1.2,
            blind=False,
            linewidth=1)
        
        # - - leptons faking a tau
        self.lepfakes = samples.LepFake(
            self.config, self.mc[:],
            name='LepFakes',
            label='MisID l #rightarrow #tau',
            color=ROOT.kAzure)
        
        # - - jets faking a tau
        self.qcd = samples.QCD(
            self.config, self.data, self.mc[:],
            name='QCD',
            label='MisID j #rightarrow #tau',
            color=ROOT.kMagenta+2,
            correct_upsilon=True)

        self.backgrounds = [
            self.ttbar,
            self.qcd,
            self.single_top,
            self.wtaunu,
            self.lepfakes,
            self.ztautau,
            self.diboson,
            ] 
        
        # - - signals 
        self.signals = self.get_signals() 
        
        self.samples = [
            self.qcd, 
            self.lepfakes,
            self.ttbar,
            self.single_top,
            self.wtaunu,
            self.ztautau,
            self.diboson,            
        ]

        self.samples +=self.signals + [self.data] 
        
        # ---- stored workers
        self._workers=[]

    def compile_cxx(self):
        ostring = "**"*20 + "... Loading & compiling cxx macros ..." +"**"*20
        log.info(ostring)
        log.info("\t FFs macros: %r"%self.config.FFs_macros)
        log.info("\t Upsilon correction macros: %r"%self.config.upsilon_macros)
        log.info("\t MET trigger efficiency macros: %r"%self.config.metTrigEff_macros)
        log.info("*"*len(ostring))

        macros = [os.path.join(Analysis.__HERE, "cxxmacros", cm) for cm in self.cxx_macros]
        for cm in macros:
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
            masses = Higgs.MASSES
        if not isinstance(masses, (list, tuple)):
            masses = [masses]
            
        signals = []
        colors = [ROOT.kRed, ROOT.kGreen, ROOT.kBlue, ROOT.kOrange, ROOT.kMagenta]
        line_styles =range(1, 11)
        while len(masses) > len(colors):
            colors += [c+4 for c in colors]
            line_styles += line_styles

        for i, mass in enumerate(masses):
            signals.append(
                samples.Higgs(self.config, mass=mass, scale=scale, color=colors[i], line_style=line_styles[i]))
            
        return signals

    def normalize(self, category):
        """ normalize qcd, ztautau.
        Parameters:
        -----------
        category : Category object, for more see catgories.py

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
        if not samples:
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
            categories.append(Category(name, cuts_list=cuts_list, tauid=None, mc_camp=self.config.mc_camp))

        if sim_samples:    
            cutflow_hist_sets += self.hists(
                samples=sim_samples, categories=categories, fields=[field], **kwargs)
        
        # - - - - treat QCD seperatly (due to different TAU ID)
        if self.qcd.name in [s.name for s in samples]:
            cutflow_hist_sets += self.qcd.cutflow(cutflow_selections, **kwargs)
            
        if self.data.name in [s.name for s in samples]:
            cutflow_hist_sets += self.data.cutflow(cutflow_selections, **kwargs)
        
        return cutflow_hist_sets
    
    def ffs_workers(self,
                  template_fields=[],
                  template_hist=None,
                  template_hist_bins=[],
                  control_regions=[],
                  tau_jet_rnn_score_trans_wps=[0.01, 0.02, 0.03],
                  n_charged_tracks=[1, 3],
                  trigger=None,
                  tauid=None, 
                  antitau=None,
                  subtract_mc=True,**kwargs):
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
        min_tau_jet_rnn_score_trans_wps: 
            list type; working points for tau_jet_rnn_score_trans 
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
            antitau = ROOT.TCut("tau_0_jet_rnn_loose==0")
            
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
            acr.truth_tau = TAU_IS_LEP_OR_HAD
            
        # - - - - parallel processing
        workers = []
        
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
            # - - - - NOMINAL only 
            systematics = self.config.systematics[:1]
            assert systematics[0].name=="NOMINAL", "FFs should only be evaluated on NOMINAL" 

            # - - - - MC workers
            mc_tau_workers = []
            mc_antitau_workers = []
            for mc in self.mc:
                mc_tau_workers += mc.workers(
                    fields=template_fields[:1], hist_templates=template_hist, systematics=systematics,
                    categories=tau_control_regions, trigger=trigger)

                # - - taus not passing nominal tau ID 
                mc_antitau_workers += mc.workers(
                    fields=template_fields[:1], hist_templates=template_hist, systematics=systematics,
                    categories=antitau_control_regions, trigger=trigger)

            # add mc tau/antitau  workers to the list of all workers
            for w in mc_tau_workers:
                w.name += "_TAU"
            workers += mc_tau_workers

            for w in mc_antitau_workers:
                w.name += "_ANTITAU"
            workers += mc_antitau_workers


        return workers

