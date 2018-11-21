
# local imports
from hpana import log
from hpana.weights import WEIGHTS


class SYSTEMATICS_CATEGORIES:
    TAUS, \
        JETS, \
        WEIGHTS, \
        NORMALIZATION = range(4)

# WIP:


class Systematic(object):
    TYPES = ["TREE", "WEIGHT", "THEORY"]

    # systematics with dedicated TTree
    SOURCES = {
        "TAU":
        (
            "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1up",
            "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1down",
            "TAUS_TRUEHADTAU_SME_TES_INSITU_1up",
            "TAUS_TRUEHADTAU_SME_TES_INSITU_1down",
            "TAUS_TRUEHADTAU_SME_TES_MODEL_1up",
            "TAUS_TRUEHADTAU_SME_TES_MODEL_1down",
        ),
        "MUON": (),
        "ELECTRON": (),
        "JET": (),
        "MET": (),

    }

    def __init__(self, name, title=None, _type="TREE", variations=None, channel="taujet"):
        assert _type in Systematic.TYPES, "systematics of type %s is not supported" % _type
        self._type = _type
        self.channel = channel

        if not isinstance(variations, (list, tuple, dict)):
            variations = (variations,)
        elif isinstance(variations, dict):
            variations = (variations["UP"], variations["DOWN"])
        self.variations = variations

        self.name = name
        if not title:
            title = name
        self.title = title

    def __iter__(self):
        for var in self.variations:
            yield '%s_%s' % (self.name, var)

    def __repr__(self):
        return "name=%r, title=%r, type=%r" % (self.name, self.title, self._type)

    @classmethod
    def factory(cls, channel="taujet"):
        # fist systematic TTrees
        systematics = []
        for source, ws in cls.SOURCES.iteritems():
            assert isinstance(ws, (tuple, list)), "must be a tuple or list"
            for w in ws:
                syst = Systematic(w, _type="TREE", channel=channel)
                systematics += [syst]

        # weight systematics
        nom_weights = [nw.name for nw in WEIGHTS[channel]]
        nom_weight = "*".join(nom_weights)
        for weight in WEIGHTS[channel]:
            nom_w = weight.variations[0]
            var_weights = weight.variations[1:]
            for vw in var_weights:
                # FIX ME: better solution ?
                sname = vw.split("*")[-1].replace(")", "")
                syst = Systematic(sname, title="(%s)/(%s)" %
                                  (vw, nom_w), channel=channel, _type="WEIGHT")
                systematics += [syst]

        # theory systematics: WIP

        return systematics


# prep systematics objects
SYSTEMATICS = {}
SYSTEMATICS["taujet"] = Systematic.factory(channel="taujet")
#SYSTEMATICS["taulep"] = Systematic.factory(channel="taulep")


# MUON_ID_1down
# MUON_ID_1up
# MUON_MS_1down
# MUON_MS_1up
# MUON_SAGITTA_RESBIAS_1down
# MUON_SAGITTA_RESBIAS_1up
# MUON_SAGITTA_RHO_1down
# MUON_SAGITTA_RHO_1up
# MUON_SCALE_1down
# MUON_SCALE_1up


# #### WEIGHTS
# jet_sf_FT_EFF_Eigen_B_0_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_0_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_0_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_0_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_1_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_1_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_1_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_1_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_2_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_2_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_2_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_B_2_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_0_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_0_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_0_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_0_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_1_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_1_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_1_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_1_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_2_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_2_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_2_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_C_2_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_0_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_0_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_0_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_0_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_1_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_1_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_1_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_1_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_2_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_2_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_2_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_2_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_3_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_3_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_3_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_3_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_4_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_4_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_4_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_Eigen_Light_4_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_extrapolation_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_extrapolation_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_extrapolation_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_extrapolation_1up_global_ineffSF_MV2c10
# jet_sf_FT_EFF_extrapolation_from_charm_1down_global_effSF_MV2c10
# jet_sf_FT_EFF_extrapolation_from_charm_1down_global_ineffSF_MV2c10
# jet_sf_FT_EFF_extrapolation_from_charm_1up_global_effSF_MV2c10
# jet_sf_FT_EFF_extrapolation_from_charm_1up_global_ineffSF_MV2c10
# jet_sf_NOMINAL_central_jets_global_effSF_JVT
# jet_sf_NOMINAL_central_jets_global_ineffSF_JVT
# jet_sf_NOMINAL_forward_jets_global_effSF_JVT
# jet_sf_NOMINAL_forward_jets_global_ineffSF_JVT
# jet_sf_NOMINAL_global_effSF_MV2c10
# jet_sf_NOMINAL_global_ineffSF_MV2c10


# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_LooseEleBDTPlusVeto_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_LooseEleBDT_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_MediumEleBDTPlusVeto_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_MediumEleBDT_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_VeryLooseLlhEleOLR_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_LooseEleBDTPlusVeto_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_LooseEleBDT_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_MediumEleBDTPlusVeto_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_MediumEleBDT_electron
# tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_VeryLooseLlhEleOLR_electron
# tau_0_sf_TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1down_TauEffSF_HadTauEleOLR_tauhad
# tau_0_sf_TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1up_TauEffSF_HadTauEleOLR_tauhad
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2025_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR2530_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORR3040_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORRGE40_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORRGE40_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORRGE40_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORRGE40_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORRGE40_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_1PRONGSTATSYSTUNCORRGE40_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORR2030_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_3PRONGSTATSYSTUNCORRGE30_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1down_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1down_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1down_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1up_TauEffSF_JetBDTloose
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1up_TauEffSF_JetBDTmedium
# tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1up_TauEffSF_JetBDTtight
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_reco
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_selection
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_reco
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_selection
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_reco
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_selection
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco
# tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_selection
