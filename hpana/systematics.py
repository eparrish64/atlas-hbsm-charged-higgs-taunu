"""
* Base class for systematics types. 
* Systematic class mainly encapsulated systematics info for different types.
* Systematic Objects, can then be passed to the anlaysis workers in order to 
* do histograms depending on the type and source of systematics
* NOTE: that minor systematics are comment out by default (making the code very slow), uncomment them if you with to include
* all systematics in the analysis.
* @author : sina.bahrasemani@cern.ch
"""

# local imports
from hpana import log
from hpana.weights import WEIGHTS

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
class Variation(object):
    def __init__(self, name, title=None, _type="TREE"):
        if not title:
            self.title = name
        else:
            self.title = title
        self.name = name 
        self._type = _type

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
class Systematic(object):
    TYPES = ["TREE", "WEIGHT", "THEORY"]

    # systematics with dedicated TTree
    SOURCES = {"taujet": {}, "taulep": {}}

    # taujet specific
    SOURCES["taujet"] = {
        "TAU": {
            "TAUS_TRUEHADTAU_SME_TES_DETECTOR":(
                "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1up",
                "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1down",
            ),

            "TAUS_TRUEHADTAU_SME_TES_INSITU":(
                "TAUS_TRUEHADTAU_SME_TES_INSITUEXP_1up",
                "TAUS_TRUEHADTAU_SME_TES_INSITUEXP_1down",
                "TAUS_TRUEHADTAU_SME_TES_INSITUFIT_1up",
                "TAUS_TRUEHADTAU_SME_TES_INSITUFIT_1down",
            ),

            "TAUS_TRUEHADTAU_SME_TES_MODEL":(
                "TAUS_TRUEHADTAU_SME_TES_MODEL_CLOSURE_1up",
                "TAUS_TRUEHADTAU_SME_TES_MODEL_CLOSURE_1down",
            ),
            
            "TAUS_TRUEHADTAU_SME_TES_PHYSICSLIST":(
                "TAUS_TRUEHADTAU_SME_TES_PHYSICSLIST_1up",
                "TAUS_TRUEHADTAU_SME_TES_PHYSICSLIST_1down",
            ),
        }, #<! END tau

        "JET": {
            "JET_BJES_Response":(
                "JET_BJES_Response_1down",
                "JET_BJES_Response_1up",
            ),

            "JET_EffectiveNP":(
                "JET_EffectiveNP_1_1down",
                "JET_EffectiveNP_1_1up",
                "JET_EffectiveNP_2_1down",
                "JET_EffectiveNP_2_1up",
                "JET_EffectiveNP_3_1down",
                "JET_EffectiveNP_3_1up",
                "JET_EffectiveNP_4_1down",
                "JET_EffectiveNP_4_1up",
                "JET_EffectiveNP_5_1down",
                "JET_EffectiveNP_5_1up",
                "JET_EffectiveNP_6_1down",
                "JET_EffectiveNP_6_1up",
                "JET_EffectiveNP_7_1down",
                "JET_EffectiveNP_7_1up",
                "JET_EffectiveNP_8restTerm_1down",
                "JET_EffectiveNP_8restTerm_1up",
            ),

            "JET_EtaIntercalibration_Modelling":(
                "JET_EtaIntercalibration_Modelling_1down",
                "JET_EtaIntercalibration_Modelling_1up",
            ),

            "JET_EtaIntercalibration_NonClosure":(
                "JET_EtaIntercalibration_NonClosure_highE_1down",
                "JET_EtaIntercalibration_NonClosure_highE_1up",
                "JET_EtaIntercalibration_NonClosure_negEta_1down",
                "JET_EtaIntercalibration_NonClosure_negEta_1up",
                "JET_EtaIntercalibration_NonClosure_posEta_1down",
                "JET_EtaIntercalibration_NonClosure_posEta_1up",
                "JET_EtaIntercalibration_NonClosure_2018data_1down",
                "JET_EtaIntercalibration_NonClosure_2018data_1up",
            ),

            "JET_EtaIntercalibration_TotalStat":(                
                "JET_EtaIntercalibration_TotalStat_1down",
                "JET_EtaIntercalibration_TotalStat_1up",
            ),

            "JET_Flavor_Composition":(
                "JET_Flavor_Composition_1down",
                "JET_Flavor_Composition_1up",
            ),

            "JET_Flavor_Response":(
                "JET_Flavor_Response_1down",
                "JET_Flavor_Response_1up",
            ),

            "JET_JER_DataVsMC":(
                "JET_JER_DataVsMC_AFII_1down",
                "JET_JER_DataVsMC_AFII_1up",
                "JET_JER_DataVsMC_MC16_1down",
                "JET_JER_DataVsMC_MC16_1up",
            ),

            "JET_JER_EffectiveNP":(
                "JET_JER_EffectiveNP_1_1down",
                "JET_JER_EffectiveNP_1_1up",
                "JET_JER_EffectiveNP_2_1down",
                "JET_JER_EffectiveNP_2_1up",
                "JET_JER_EffectiveNP_3_1down",
                "JET_JER_EffectiveNP_3_1up",
                "JET_JER_EffectiveNP_4_1down",
                "JET_JER_EffectiveNP_4_1up",
                "JET_JER_EffectiveNP_5_1down",
                "JET_JER_EffectiveNP_5_1up",
                "JET_JER_EffectiveNP_6_1down",
                "JET_JER_EffectiveNP_6_1up",
                "JET_JER_EffectiveNP_7restTerm_1down",
                "JET_JER_EffectiveNP_7restTerm_1up",
            ),

            "JET_Pileup_OffsetMu":(
                "JET_Pileup_OffsetMu_1down",
                "JET_Pileup_OffsetMu_1up",
            ),

            "JET_Pileup_OffsetNPV":(
                "JET_Pileup_OffsetNPV_1down",
                "JET_Pileup_OffsetNPV_1up",
            ),

            "JET_Pileup_PtTerm":(
                "JET_Pileup_PtTerm_1down",
                "JET_Pileup_PtTerm_1up",
            ),

            "JET_Pileup_RhoTopology":(
                "JET_Pileup_RhoTopology_1down",
                "JET_Pileup_RhoTopology_1up",
            ),

            "JET_PunchThrough":(
                "JET_PunchThrough_MC16_1down",
                "JET_PunchThrough_MC16_1up",
                "JET_PunchThrough_AFII_1down",
        	"JET_PunchThrough_AFII_1up",
                
            ),

            "JET_RelativeNonClosure":(
                "JET_RelativeNonClosure_AFII_1down",
        	"JET_RelativeNonClosure_AFII_1up",
            ),

            "JET_SingleParticle_HighPt":(
                "JET_SingleParticle_HighPt_1down",
                "JET_SingleParticle_HighPt_1up",
            ),

            "JET_TILECORR_Uncertainty":(
                "JET_TILECORR_Uncertainty_1down",
                "JET_TILECORR_Uncertainty_1up",
            ),
        }, #<! END jet

        "MET": {
            "MET_SoftTrk":( 
                "MET_SoftTrk_ResoPara",
                "MET_SoftTrk_ResoPerp",
                "MET_SoftTrk_Scale_1down",
                "MET_SoftTrk_Scale_1up",
            )
        },
    }

    # taulep specific
   SOURCES["taulep"]["TAU"] = SOURCES["taujet"]["TAU"]
   SOURCES["taulep"]["JET"] = SOURCES["taujet"]["JET"]
   SOURCES["taulep"]["MET"] = SOURCES["taujet"]["MET"]
    SOURCES["taulep"]["MUON"] = {
        "MUON_ID":(
            "MUON_ID_1down",
            "MUON_ID_1up",
        ),

        "MUON_MS":(
            "MUON_MS_1down",
            "MUON_MS_1up",
        ),

        "MUON_SAGITTA":(
            "MUON_SAGITTA_RESBIAS_1down",
            "MUON_SAGITTA_RESBIAS_1up",
            "MUON_SAGITTA_RHO_1down",
            "MUON_SAGITTA_RHO_1up",
        ),

        "MUON_SCALE":(
            "MUON_SCALE_1down",
            "MUON_SCALE_1up",
        ),
    }
    SOURCES["taulep"]["ELECTRON"] = {
        "EG_RESOLUTION_ALL":(
            "EG_RESOLUTION_ALL_1down",
            "EG_RESOLUTION_ALL_1up",
        ),

        # "EG_SCALE_AF2":(
        #     "EG_SCALE_AF2_1down",
        #     "EG_SCALE_AF2_1up",
        # ),

        "EG_SCALE_ALL":(
            "EG_SCALE_ALL_1down",
            "EG_SCALE_ALL_1up",
        ),
    }
#jet_sf_NOMINAL_global_effSF_DL1r_FixedCutBEff_70
    def __init__(self, name, title=None, _type="TREE", channel="taujet", variations=[]):
        assert _type in Systematic.TYPES, "systematics of type %s is not supported" % _type
        self._type = _type
        self.channel = channel
        self.name = name
        if not title:
            title = name
        self.title = title
        self.variations = variations

    def __repr__(self):
        return "name=%r, title=%r, type=%r, variations=%r" % (self.name, self.title, self._type, self.variations)

    @classmethod
    def factory(cls, channels=["taujet", "taulep"]):
        """ factroy method for providing analysis wide systematics. 
        """
        systs_dict = {}
        for channel in channels:
            # kinematics systematics (TTrees including NOMINAL! )
            systematics = [cls("NOMINAL", _type="TREE", channel=channel, variations=[Variation("NOMINAL")])]
            for source, ws in cls.SOURCES[channel].iteritems():
                if isinstance(ws, dict):
                    for st, variations in ws.iteritems(): 
                        syst = cls(st, _type="TREE", channel=channel, 
                            variations=[Variation(v, _type="TREE") for v in variations])
                        systematics += [syst]

            # weight systematics
            nom_weights = [nw.name for nw in WEIGHTS[channel]]
            nom_weight = "*".join(nom_weights)
            for weight in WEIGHTS[channel]:
                nom_w = weight.variations[0]
                var_weights = weight.variations[1:]
                if len(var_weights) < 1:
                    continue

                syst_vars = []
                for vw in var_weights:
                    if isinstance(vw, (list, tuple)):
                        vname = vw[0]
                        vtitle = vw[1]
                    else:
                        vname = vw
                        vtitle = vw
                    syst_vars += [(Variation(vname, title="(%s)/(%s)" %(vtitle, nom_w), _type="WEIGHT")) ]

                systematics += [cls(weight.name, _type="WEIGHT", variations=syst_vars)]

            # theory systematics: WIP
            systs_dict[channel] = systematics

        return systs_dict


# prepapre systematic objects
SYSTEMATICS = Systematic.factory()
