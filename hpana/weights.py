"""
* Different scale factor weights are put together here. 
* for each weight obj 
"""

__all__ = ["Weight"]

from . import MC_CAMPAIGN

class Weight(object):
    """
    """
    ##FIXME : do nparts==0 & nparts>0*SF returns 0 sometimes! 
    W_STR_FMT = "({0}!=1+({0}==1)*{1})"
    W_PILEUP = {
        "weight_pileup": ("weight_total/weight_mc",) #<! TRAILING COMMA IS NECESSARY FOR ONE ELEMENT TUPLES!
    }
    
    W_BASE = {
        "weight_total": ("weight_total", )
    }

    W_TAU =  {
        "tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium": (
            W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium"), #<! NOMINAL 

            W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1down_TauEffSF_JetBDTmedium"),
            
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1down_TauEffSF_JetBDTmedium"),
            
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1down_TauEffSF_JetBDTmedium"),
            
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR40_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR40_1down_TauEffSF_JetBDTmedium"),
            
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1down_TauEffSF_JetBDTmedium"),
            
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1down_TauEffSF_JetBDTmedium"),
            
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTmedium"),

            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1up_TauEffSF_JetBDTmedium"),
            W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1down_TauEffSF_JetBDTmedium"),
        ),
        
        "tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron": (
            W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron"),

            W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1up_TauEffSF_HadTauEleOLR_tauhad"),
            W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1down_TauEffSF_HadTauEleOLR_tauhad"),
            
            W_STR_FMT.format("n_taus","tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_VeryLooseLlhEleOLR_electron"),
            W_STR_FMT.format("n_taus","tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_VeryLooseLlhEleOLR_electron"),
        ),
        
        "tau_0_sf_NOMINAL_TauEffSF_reco": (
                W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_reco"),
            
                W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco"),
                W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_reco"),
                
                W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_reco"),
                W_STR_FMT.format("tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_reco"),
            ),
    } #<! W_TAU
    
    W_JET = {
        "jet_sf_NOMINAL_central_jets_global_effSF_JVT":(
            "jet_sf_NOMINAL_central_jets_global_effSF_JVT",
        ),
        
        "jet_sf_NOMINAL_central_jets_global_ineffSF_JVT": (
            "NOMINAL": "jet_sf_NOMINAL_central_jets_global_ineffSF_JVT",
        ),
    } #<! W_JET
    
    W_BJET = {
        "jet_sf_NOMINAL_global_ineffSF_MV2c10": (
            "jet_sf_NOMINAL_global_ineffSF_MV2c10",
        ),
    } #<! W_BJET
        
    W_MU = {
        "mu_0_sf_NOMINAL_MuEffSF_TTVA": (
            W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_TTVA"),
        ),
        
        "mu_0_sf_NOMINAL_MuEffSF_IsoFixedCutTight": (
            W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_IsoFixedCutTight"),),
        
        "mu_0_sf_NOMINAL_MuEffSF_Reco_QualTight": (
            W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_Reco_QualTight"),),
        
    } #<! W_MU
    
    W_EL = {
        
        "el_0_sf_NOMINAL_EleEffSF_offline_RecoTrk": (
            W_STR_FMT.format("n_electrons", "el_0_sf_NOMINAL_EleEffSF_offline_RecoTrk"),),
        
        "el_0_sf_NOMINAL_EleEffSF_Isolation_TightLLH_d0z0_v13_isolFixedCutTight": (
            W_STR_FMT.format("n_electrons", "el_0_sf_NOMINAL_EleEffSF_Isolation_TightLLH_d0z0_v13_isolFixedCutTight"),),
        
        "el_0_sf_NOMINAL_EleEffSF_offline_MediumLLH_d0z0_v13": (
            W_STR_FMT.format("n_electrons", "el_0_sf_NOMINAL_EleEffSF_offline_MediumLLH_d0z0_v13"),),
        
        "el_0_sf_NOMINAL_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH": (
            W_STR_FMT.format("n_electrons", "el_0_sf_NOMINAL_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR"\
                             "_e60_lhmedium_OR_e120_lhloose_2016_2017_e26_lhtight_nod0_ivarloose_"\
                             "OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v13_isolFixedCutTight"),),
    )

    W_TRIGGER_TAUJET = {
        "mc15": ("nominal_trig_eff({})".format("met_et/1000."), ),
        "mc16": ("metTrigEff({}, 1000)".format("met_p4->Et()"), ), 
    }
    
    W_TRIGGER_TAULEP = ("1",)
    
    TYPES = {
        "taujet":{
            "BASE": W_BASE,
            "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "TRIGGER": W_TRIGGER_TAUJET
        },
         
        "taulep":{
            "BASE": W_BASE,
            "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "MU": W_MU,
            "EL": W_EL,
            #"TRIGGER": W_TRIGGER_TAULEP
        },
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
                for w in wo[mc_camp]:
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

    
