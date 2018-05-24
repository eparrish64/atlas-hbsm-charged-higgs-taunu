# local imports
import ROOT 

from .sample import Sample
from .. import log

class Fakes(Sample):
    #WIP: - - - - - - - -  Fake-Factor weights are different for different selection categories
    FF_TYPES = {
        "taujet": {
            "PRESELECTION":1,
            "WJET_CR":2,
            "TTBAR_CR":3,
            "SR_TAUJET":3,
            "QCD_CR":111,},
        "taulep":{
            "WZ_CR":2,
            "TTBar_CR":3,
            "SR_TAUEMU":7,
            "SR_TAUEL":7,
            "SR_TAULEP":7,
            "ZEE_CR":4,
            "BVETO_TAULEP":6,}
    }

    FF_WCR = "GetFF02_WCR({0}, {1})"
    FF_QCD = "GetFF02_QCD({0}, {1})"
    TEMPLATE_VARS = {
        "default": ("tau_0_p4->Pt()/1000.", "tau_0_n_charged_tracks"),
        "2016": ("tau_0_pt/1000.", "tau_0_n_tracks"),}
    rQCD = "GetFFCombined({0}, {1}, {2}, {3}, {4})"
    ANTI_TAU = ROOT.TCut("tau_0_jet_bdt_score_sig > 0.02 && tau_0_jet_bdt_loose==0")
    
    @staticmethod
    def sample_compatibility(data, mc):
        log.info("mc: {}".format([m.name for m in mc]))
        if not isinstance(mc, (list, tuple)):
            raise TypeError("mc must be a list or tuple of MC samples")
        if not mc:
            raise ValueError("mc must contain at least one MC sample")
    
    def __init__(self, config, data, mc, **kwargs):
        
        # - - - - quick sanity check
        Fakes.sample_compatibility(data, mc)

        # - - - - instantiate base 
        super(Fakes, self).__init__(config, **kwargs)
        
        self.config = config
        self.data = data
        self.mc = mc
        self.tauid = Fakes.ANTI_TAU
        
    def cuts(self, **kwargs):
        tauid = kwargs.pop("tauid", self.tauid)
        selection = super(Fakes, self).cuts(tauid=tauid, **kwargs)
        log.info(selection)
        return selection
    
    def weights(self, **kwargs):
        """ FF weights for Fakes need special treatment.
        """
        if not "category" in kwargs:
            raise RuntimeError(
                "in order to extract FF weights for fakes a category is needed!")

        category = kwargs["category"]
        if self.config.year in Fakes.TEMPLATE_VARS:
            v0, v1 = Fakes.TEMPLATE_VARS[self.config.year]
        else:
            v0, v1 = Fakes.TEMPLATE_VARS["default"]

        ff_wcr = Fakes.FF_WCR.format(v0, v1)
        ff_qcd = Fakes.FF_QCD.format(v0, v1)
        ff_weight_index = Fakes.FF_TYPES[self.config.channel][category.name.upper()]
            
        ff_weight = Fakes.rQCD.format(v0, v1, ff_qcd, ff_wcr, ff_weight_index)
        
        return [ff_weight]
    
    def events(self, **kwargs):
        """ 
        """
        tauid = kwargs.pop("tauid", Fakes.ANTI_TAU)
        weighted = kwargs.pop("weighted", True)
        extra_weight = kwargs.pop("extra_weight", ROOT.TCut("1"))
        for w in self.weights(**kwargs):
            extra_weight *= w
        
        mc_events = 0
        data_events = self.data.events(tauid=tauid, extra_weight=extra_weight, **kwargs)
        for m in self.mc[3:5]:
            m_events = m.events(tauid=tauid, extra_weight=extra_weight, **kwargs)
            log.debug("mc: {0}; events: {1:0.2f}".format(m.name, m_events))
            mc_events += m_events
        
        log.debug("DATA: {0:0.2f};  MC: {1:0.2f}".format(data_events, mc_events))
        
        return data_events - mc_events
        
        
    def hist(self, **kwargs):
        """
        
        """
        
    
    
