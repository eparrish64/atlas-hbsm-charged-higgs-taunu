__all__ = ["WEIGHTS", "Weight"]

from .trigger import TRIGGER_EFFICIENCIES 
from . import MC_CAMPAIGN

class Weight:
    """
    """
    W_BASE = ("weight_mc",) #<! TRAILING COMMA IS NECESSARY FOR ONE ELEMENT TUPLES!

    W_PILEUP = ("weight_total/weight_mc",)

    W_TAU =  (
        "tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium",
        "tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron",
        "tau_0_sf_NOMINAL_TauEffSF_reco")

    #- - - - - - - - might be different among different MC campaigns (or ntuples versions)
    W_JET = {
        "mc15": ("jet_sf_NOMINAL_central_jets_global_ineffSF_JVT",
                 "jet_sf_NOMINAL_central_jets_global_effSF_JVT"),
        "mc16": ("jet_sf_NOMINAL_central_jets_global_effSF_JVT",
                 "jet_sf_NOMINAL_central_jets_global_ineffSF_JVT"),
    }

    W_BJET = {
        "mc15": ("jet_sf_NOMINAL_global_effSF_MVX",
                 "jet_sf_NOMINAL_global_ineffSF_MVX"),
        "mc16": ("jet_sf_NOMINAL_global_effSF_MV2c10",
                 "jet_sf_NOMINAL_global_ineffSF_MV2c10"),
    }
    # - - - - - - - - might be different between the channels
    W_MU = ("1",)
    W_EL = ("1",)
    
    #WIP:make it to work per year - - - - trigger
    W_TRIGGER_TAUJET = (TRIGGER_EFFICIENCIES["taujet"][MC_CAMPAIGN],)
    W_TRIGGER_TAULEP = ("1",)
    
    TYPES = {
        "taujet":{
            "BASE": W_BASE,
            "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "TRIGGER": W_TRIGGER_TAUJET},
         
        "taulep":{
            "BASE": W_BASE,
            "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "MU": W_MU,
            "EL": W_EL,
            "TRIGGER": W_TRIGGER_TAULEP},
    }
    
    CHANNELS = ["taujet", "taulep"]
    YEARS = ["2015", "2016", "2017", "2018"]

    @classmethod
    def factory(cls, channel="taujet", mc_camp=MC_CAMPAIGN):
        """ 
        """
        weights = []
        for wtype, wo in cls.TYPES[channel].iteritems():
            if isinstance(wo, (tuple, list)):
                for w in wo:
                    weight = cls(w, wtype=wtype, channel=channel, mc_camp=mc_camp)
                    weights.append(weight)
            elif isinstance(wo, dict):
                for w in wo[MC_CAMPAIGN]:
                    weight = cls(w, wtype=wtype, channel=channel, mc_camp=mc_camp)
                    weights.append(weight)
            else:
                raise TypeError("{} must be either a tuple, list or dict type".format(w))
        return weights
    
    def __init__(self, name, wtype="", channel="taujet", mc_camp=MC_CAMPAIGN):
        self.channel = channel
        
        assert wtype.upper() in self.TYPES[self.channel].keys(),\
            "%s weight is not supported; see weights.Weight"%wtype.upper()
        self.name = name
        self.wtype = wtype
        self.mc_camp = mc_camp
        
    def variations(self):
        """WIP: get the variations 
        """
        return
    
    def __repr__(self):
        return "WEIGHT:: name=%r, type=%r, channel=%r, mc_camp=%r"%(
            self.name, self.wtype, self.channel, self.mc_camp)
    

# - - - - - - - - instantiate weights 
WEIGHTS = Weight.factory()

