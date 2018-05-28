# local imports
import ROOT 

from .sample import Sample, Histset
from .. import log

##---------------------------------------------------------------------------------------
## jets faking a tau background 
class QCD(Sample):
    ANTI_TAU = ROOT.TCut(
        "tau_0_jet_bdt_score_sig > 0.02 && tau_0_jet_bdt_loose==0")
    
    #WIP: - - - - - - - -  Fake-Factor weights are different for different selection categories
    FF_TYPES = {
        "taujet": {
            "PRESELECTION":1,
            "BVETO":2,
            "TTBAR":3,
            "SR_TAUJET":3,
            "QCD":111,},
        "taulep":{
            "BVETO":6,
            "TTBar":3,
            "ZEE":4,
            "SR_TAUMU":7,
            "SR_TAUEL":7,
            "SR_TAULEP":7,
        }
    }

    FF_WCR = "GetFF02_WCR({0}, {1})"
    FF_QCD = "GetFF02_QCD({0}, {1})"
    TEMPLATE_VARS = {
        "default": ("tau_0_p4->Pt()/1000.", "tau_0_n_charged_tracks"),
        "2016": ("tau_0_pt/1000.", "tau_0_n_tracks"),}
    
    rQCD = "GetFFCombined({0}, {1}, {2}, {3}, {4})"
    
    
    @staticmethod
    def sample_compatibility(data, mc):
        if not isinstance(mc, (list, tuple)):
            raise TypeError("mc must be a list or tuple of MC samples")
        if not mc:
            raise ValueError("mc must contain at least one MC sample")
    
    def __init__(self, config, data, mc, name="QCD", label="fakes", **kwargs):
        
        # - - - - quick sanity check
        QCD.sample_compatibility(data, mc)

        # - - - - instantiate base 
        super(QCD, self).__init__(config, name=name, label=label, **kwargs)
        
        self.config = config
        self.data = data
        self.mc = mc
        self.tauid = QCD.ANTI_TAU
        
    def cuts(self, **kwargs):
        """ fakes tauID MEDIUM corresponds to 
        QCD.ANTI_TAU * FF(tau_0_pt, tau_0_n_tracks) 
        """
        tauid = kwargs.pop("tauid", self.tauid)
        selection = super(QCD, self).cuts(tauid=tauid, **kwargs)
        log.debug(selection)
        return selection
    
    def weights(self, **kwargs):
        """ FF weights for QCD need special treatment.
        """
        if not "category" in kwargs:
            raise RuntimeError(
                "in order to extract FF weights for fakes a category is needed!")

        category = kwargs["category"]
        if self.config.year in QCD.TEMPLATE_VARS:
            v0, v1 = QCD.TEMPLATE_VARS[self.config.year]
        else:
            v0, v1 = QCD.TEMPLATE_VARS["default"]

        ff_wcr = QCD.FF_WCR.format(v0, v1)
        ff_qcd = QCD.FF_QCD.format(v0, v1)
        ff_weight_index = QCD.FF_TYPES[self.config.channel][category.name.upper()]
            
        ff_weight = QCD.rQCD.format(v0, v1, ff_qcd, ff_wcr, ff_weight_index)
        
        return [ff_weight]
    
        
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
        """
        log.info("processing %s tree from %s ; category: %s"%(
            systematic, self.name, category.name))
        # - - - - - - - - it's a data-deriven approach --> no systematics tree for fakes
        if systematic != "NOMINAL":
            return []
        
        extra_weight = ROOT.TCut("1")
        for w in self.weights(category=category):
            extra_weight *= w
            
        # - - - - - - - - mc with truth tau, but failing tau ID 
        mc_hists = []
        for m in self.mc:
            mc_hists += m.hists(
                category,
                fields=fields,
                tauid=QCD.ANTI_TAU,
                extra_cuts=extra_cuts,
                extra_weight=extra_weight,
                weighted=weighted,
                trigger=trigger)
                
        # - - - - - - - - data: shouldn't blind data for QCD calculations
        self.data.blind = False
        data_hists = self.data.hists(
            category,
            fields=fields,
            tauid=QCD.ANTI_TAU,
            extra_weight=extra_weight,
            trigger=trigger)
        
        # - - - - - - - - subtract sum of mc from data
        fakes_hist_set = []
        for var in fields:
            h_data = filter(lambda h: h.variable==var.name, data_hists)
            h_data = h_data[0].hist

            h_mc = filter(lambda h: h.variable==var.name, mc_hists)
            h_mc = [h.hist for h in h_mc]
            h_mc_sum = reduce(lambda h1, h2: h1+h2, h_mc)

            # - - - - get the fakes hist and set it's name
            h_fakes = h_data - h_mc_sum
            fname = self.hist_name_template.format(self.name, category.name, var.name)
            h_fakes.SetName(fname)
            h_fakes.SetTitle(fname)
            h_fakes.SetXTitle(var.title)
            
            fakes_hist_set.append(Histset(
                sample=self.name,
                variable=var.name,
                category=category.name,
                hist=h_fakes,
                systematic=systematic) )
        log.info("proccessed %s tree from %s ; category=%s"%(
            systematic, self.name, category.name))
        
        return fakes_hist_set

    
    
##---------------------------------------------------------------------------------------
## leptons faking a tau 
class LepFake(Sample):
    TAU_IS_LEP = ROOT.TCut(
        "abs(tau_0_truth_universal_pdgId)==11||abs(tau_0_truth_universal_pdgId)==13")
        
    def __init__(self, config, mc, name="LepFake", label="l->#tau", **kwargs):
        # - - - - instantiate base 
        super(LepFake, self).__init__(config, name=name, label=label, **kwargs)
        
        self.config = config
        self.mc = mc
        self.name = name
        self.label = label
        
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
        """
        log.info("processing %s tree from %s ; category: %s"%(
            systematic, self.name, category.name))
    
        # - - - - a lepton which passes tau ID  
        if not extra_cuts:
            extra_cuts = LepFake.TAU_IS_LEP
        else:
            extra_cuts += LepFake.TAU_IS_LEP
            
        # - - - - - - - - mc 
        mc_hists = []
        for m in self.mc:
            # - - - - turn off truth matching 
            m.truth_match_tau = False
            mc_hists += m.hists(
                category,
                fields=fields,
                extra_cuts=extra_cuts,
                weighted=weighted,
                trigger=trigger)
        
        # - - - - - - - - 
        lepfake_hist_set = []
        for var in fields:
            h_mc = filter(lambda h: h.variable==var.name, mc_hists)
            h_mc = [h.hist for h in h_mc]
            h_mc_sum = reduce(lambda h1, h2: h1+h2, h_mc)

            # - - - - get the fakes hist and set it's name
            fname = self.hist_name_template.format(self.name, category.name, var.name)
            h_mc_sum.SetName(fname)
            h_mc_sum.SetTitle(fname)
            h_mc_sum.SetXTitle(var.title)
            
            lepfake_hist_set.append(Histset(
                sample=self.name,
                variable=var.name,
                category=category.name,
                hist=h_mc_sum,
                systematic=systematic) )
            
        log.info("proccessed %s tree from %s ; category=%s"%(
            systematic, self.name, category.name))

        return lepfake_hist_set
        
