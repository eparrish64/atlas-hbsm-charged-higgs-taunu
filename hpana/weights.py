__all__ = ["WEIGHTS"]

from .trigger import TRIGGER_EFFICIENCIES 

class Weight:
    """
    """
    TYPES = {
        "BASE": (
            "weight_mc",), #<! TRAILING COMMA IS NECESSARY FOR ONE ELEMENT TUPLES!
        
        "PILEUP": (
            "weight_total/weight_mc",),
        
        "TAU": (
            "tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium",
            "tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron",
            "tau_0_sf_NOMINAL_TauEffSF_reco"),
        
        "JET": (
            "jet_sf_NOMINAL_central_jets_global_ineffSF_JVT",
            "jet_sf_NOMINAL_central_jets_global_effSF_JVT"),
        
        "BJET": (
            "jet_sf_NOMINAL_global_effSF_MVX",
            "jet_sf_NOMINAL_global_ineffSF_MVX"),

        # - - - - - - - - might be different between the channels
        "MU": {
            "taujet": ("1"),
            "taulep": ("1"),
        },
        
        "EL": {
            "taujet": ("1"),
            "taulep": ("1"),
        },

        #WIP:make it to work per year - - - - trigger 
        "TRIGGER": {
            "taujet": (TRIGGER_EFFICIENCIES["taujet"]["combined"],),
            "taulep": ("1"),
        },
    }
    
    CHANNELS = ["taujet", "taulep"]
    YEARS = ["2015", "2016", "2017", "2018"]

    @classmethod
    def factory(cls):
        """ 
        """
        weights = {}
        for channel in cls.CHANNELS:
            if not channel in weights:
                weights[channel] = {}
            for year in cls.YEARS:
                if not year in weights[channel]:
                    weights[channel][year] = {}
                for wtype, ws in cls.TYPES.iteritems():
                    if not wtype in weights[channel][year]:
                        weights[channel][year][wtype] = []
                    if isinstance(ws, tuple):
                        for w in ws:
                            weights[channel][year][wtype].append(
                                cls(w, wtype=wtype, channel=channel, year=year))
                    elif isinstance(ws, dict):
                        for w in ws[channel]:
                            weights[channel][year][wtype].append(
                                cls(w, wtype=wtype, channel=channel, year=year))
                            
        return weights
    
    def __init__(self, name, wtype="", channel="taujet", year="2017"):
        assert wtype.upper() in self.TYPES, "%s weight is not supported; see weights.Weight"%wtype.upper()
        self.name = name
        self.wtype = wtype
        self.channel = channel
        self.year = year
        
    def variations(self):
        """WIP: get the variations 
        """
        return
    
    def __repr__(self):
        return "WEIGHT:: name=%r, type=%r, channel=%r, year=%r"%(
            self.name, self.wtype, self.channel, self.year)
    

# - - - - - - - - instantiate weights 
WEIGHTS = Weight.factory()

