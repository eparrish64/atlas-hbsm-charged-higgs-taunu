"""
* Different scale factor applied as weights to events.
* Class Weight provides methods for getting event weight for different channels
* @NOTE: weights might be different for different selection regions.
* @NOTE: small systematics are commented out, un-comment if you wish to include them.
"""

__all__ = ["Weight"]
from hpana import log

##--------------------------------------------------------------------
##
##--------------------------------------------------------------------
class Weight(object):
    """
    """
    # CAREFUL! must separate booleans via parantheses
    W_STR_FMT = "(({0}!=1)+({0}==1)*{1})"

    W_PILEUP = {
        # TRAILING COMMA IS NECESSARY FOR ONE ELEMENT TUPLES!
        # "weight_pileup": ("weight_total/weight_mc", )
    }

    W_BASE = {
        # "weight_total": ("weight_total", )
        # "weight_total": ("weight_total", )
    }
    W_TAU = {
        # "tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium": ( 
        #     W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium"),  #<! NOMINAL

        #     ## (name, title); title will be used to access the corresponding TTree branch.
        #     ("TAU_EFF_JETID_HIGHPT_1up" , W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTmedium")),
        #     ("TAU_EFF_JETID_HIGHPT_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTmedium")),

        #     ("TAU_EFF_JETID_SYST_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1up_TauEffSF_JetBDTmedium")),
        #     ("TAU_EFF_JETID_SYST_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1down_TauEffSF_JetBDTmedium")),
        # ),

        "tau_0_sf_NOMINAL_TauEffSF_JetRNNmedium": ( 
            W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_JetRNNmedium"),  #<! NOMINAL

            ## (name, title); title will be used to access the corresponding TTree branch.
            ("TAU_EFF_JETID_HIGHPT_1up" , W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetRNNmedium")),
            ("TAU_EFF_JETID_HIGHPT_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetRNNmedium")),

            ("TAU_EFF_JETID_SYST_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1up_TauEffSF_JetRNNmedium")),
            ("TAU_EFF_JETID_SYST_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_SYST_1down_TauEffSF_JetRNNmedium")),
        ),

        # "tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron": (
        #     W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron"),

        #     ("TAU_EFF_ELEOLR_TOTAL_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1up_TauEffSF_HadTauEleOLR_tauhad")),
        #     ("TAU_EFF_ELEOLR_TOTAL_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1down_TauEffSF_HadTauEleOLR_tauhad")),
        # ),

        # "tau_0_sf_NOMINAL_TauEffSF_HadTauEleOLR_tauhad":(
        #     W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_HadTauEleOLR_tauhad"),
        # ),


        "tau_0_sf_NOMINAL_TauEffSF_MediumEleBDT_electron":(
            W_STR_FMT.format(
                "n_taus", "(((true_tau_0_isEle==1)*tau_0_sf_NOMINAL_TauEffSF_MediumEleBDT_electron)+(true_tau_0_isEle!=1))"),

            ("TAU_EFF_ELEBDT_SYST_1down", "(((true_tau_0_isEle==1)*tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEBDT_SYST_1down_TauEffSF_MediumEleBDT_electron)+(true_tau_0_isEle!=1))"),
            ("TAU_EFF_ELEBDT_SYST_1up", "(((true_tau_0_isEle==1)*tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEBDT_SYST_1up_TauEffSF_MediumEleBDT_electron)+(true_tau_0_isEle!=1))"),
        ),

        "tau_0_sf_NOMINAL_TauEffSF_selection":(
            W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_selection"),
        ),

        "tau_0_sf_NOMINAL_TauEffSF_reco": (
            W_STR_FMT.format("n_taus", "tau_0_sf_NOMINAL_TauEffSF_reco"),

            ("TAU_EFF_RECO_TOTAL_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco")),
            ("TAU_EFF_RECO_TOTAL_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_reco")),

            ("TAU_EFF_RECO_HIGHPT_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_reco")),
            ("TAU_EFF_RECO_HIGHPT_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_reco")),
        ),

    }  # W_TAU

    W_JET = {
        "jet_sf_NOMINAL_central_jets_global_effSF_JVT": (
            "jet_sf_NOMINAL_central_jets_global_effSF_JVT",
        ),

        "jet_sf_NOMINAL_central_jets_global_ineffSF_JVT": (
            "jet_sf_NOMINAL_central_jets_global_ineffSF_JVT",
        ),

    }  # W_JET

    W_BJET = {
        # "jet_sf_NOMINAL_global_effSF_MV2c10":(
        #     "jet_sf_NOMINAL_global_effSF_MV2c10", #<! NOMINAL 
        #     ("jet_effSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_effSF_MV2c10", ),
        #     ("jet_effSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_effSF_MV2c10", ),

        #     ("jet_effSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_effSF_MV2c10", ),
        #     ("jet_effSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_effSF_MV2c10", ),

        #     ("jet_effSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_effSF_MV2c10", ),
        #     ("jet_effSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_effSF_MV2c10", ),

        #     ("jet_effSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_effSF_MV2c10", ),
        #     ("jet_effSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_effSF_MV2c10", ),            
        #     ),

        "jet_sf_NOMINAL_global_effSF_DL1r_FixedCutBEff_70":(
            "jet_sf_NOMINAL_global_effSF_DL1r_FixedCutBEff_70", #<! NOMINAL 
            ("jet_effSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_effSF_DL1r_FixedCutBEff_70", ),

            ("jet_effSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_effSF_DL1r_FixedCutBEff_70", ),

            ("jet_effSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_effSF_DL1r_FixedCutBEff_70", ),

            ("jet_effSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_effSF_DL1r_FixedCutBEff_70", ),            
            ),

        # "jet_sf_NOMINAL_global_ineffSF_MV2c10":(
        #     "jet_sf_NOMINAL_global_ineffSF_MV2c10",

        #     ("jet_ineffSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_ineffSF_MV2c10", ),
        #     ("jet_ineffSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_ineffSF_MV2c10", ),

        #     ("jet_ineffSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_ineffSF_MV2c10", ),
        #     ("jet_ineffSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_ineffSF_MV2c10", ),

        #     ("jet_ineffSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_ineffSF_MV2c10", ),
        #     ("jet_ineffSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_ineffSF_MV2c10", ),

        #     ("jet_ineffSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_ineffSF_MV2c10", ),
        #     ("jet_ineffSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_ineffSF_MV2c10", ),            
        #     ),

        "jet_sf_NOMINAL_global_ineffSF_DL1r_FixedCutBEff_70":(
            "jet_sf_NOMINAL_global_ineffSF_DL1r_FixedCutBEff_70",

            ("jet_ineffSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_ineffSF_DL1r_FixedCutBEff_70", ),
            ("jet_ineffSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_ineffSF_DL1r_FixedCutBEff_70", ),

            ("jet_ineffSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_ineffSF_DL1r_FixedCutBEff_70", ),
            ("jet_ineffSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_ineffSF_DL1r_FixedCutBEff_70", ),

            ("jet_ineffSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_ineffSF_DL1r_FixedCutBEff_70", ),
            ("jet_ineffSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_ineffSF_DL1r_FixedCutBEff_70", ),

            ("jet_ineffSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_ineffSF_DL1r_FixedCutBEff_70", ),
            ("jet_ineffSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_ineffSF_DL1r_FixedCutBEff_70", ),            
            ),

    }  # W_BJET

    W_MU = {
        "mu_0_sf_NOMINAL_MuEffSF_TTVA": (
            W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_TTVA"), #<! NOMINAL 
            
            ("MUON_EFF_TTVA_STAT_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_TTVA_STAT_1down_MuEffSF_TTVA")),
            ("MUON_EFF_TTVA_STAT_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_TTVA_STAT_1up_MuEffSF_TTVA")),

            ("MUON_EFF_TTVA_SYS_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_TTVA_SYS_1down_MuEffSF_TTVA")),
            ("MUON_EFF_TTVA_SYS_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_TTVA_SYS_1up_MuEffSF_TTVA")),

        ),

        # "mu_0_sf_NOMINAL_MuEffSF_IsoGradient": (
        #     W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_IsoGradient"),

        #     ("MUON_EFF_ISO_STAT_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_STAT_1down_MuEffSF_IsoGradient")),
        #     ("MUON_EFF_ISO_STAT_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_STAT_1up_MuEffSF_IsoGradient")),

        #     ("MUON_EFF_ISO_SYS_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_SYS_1down_MuEffSF_IsoGradient")),
        #     ("MUON_EFF_ISO_SYS_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_SYS_1up_MuEffSF_IsoGradient")),
        # ),

        "mu_0_sf_NOMINAL_MuEffSF_IsoPflowTight_FixedRad": (
            W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_IsoPflowTight_FixedRad"),

            ("MUON_EFF_ISO_STAT_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_STAT_1down_MuEffSF_IsoPflowTight_FixedRad")),
            ("MUON_EFF_ISO_STAT_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_STAT_1up_MuEffSF_IsoPflowTight_FixedRad")),

            ("MUON_EFF_ISO_SYS_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_SYS_1down_MuEffSF_IsoPflowTight_FixedRad")),
            ("MUON_EFF_ISO_SYS_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_ISO_SYS_1up_MuEffSF_IsoPflowTight_FixedRad")),
        ),


        "mu_0_sf_NOMINAL_MuEffSF_Reco_QualTight": (
            W_STR_FMT.format("n_muons", "mu_0_sf_NOMINAL_MuEffSF_Reco_QualTight"),

            ("MUON_EFF_RECO_STAT_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_RECO_STAT_1down_MuEffSF_Reco_QualTight")), 
            ("MUON_EFF_RECO_STAT_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_RECO_STAT_1up_MuEffSF_Reco_QualTight")), 

            ("MUON_EFF_RECO_SYS_1down", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_RECO_SYS_1down_MuEffSF_Reco_QualTight")), 
            ("MUON_EFF_RECO_SYS_1up", W_STR_FMT.format("n_muons", "mu_0_sf_MUON_EFF_RECO_SYS_1up_MuEffSF_Reco_QualTight")), 
        ),

# FIXME!!!!
        "mu_0_sf_MuEffSF_Trig": (
          W_STR_FMT.format("n_muons", 
            "mu_0_sf_NOMINAL_MuEffSF_HLT_mu26_ivarmedium_QualTight"),

         ("MUON_EFF_TRIG_SYS_1down",  W_STR_FMT.format("n_muons", 
            "mu_0_sf_MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu26_ivarmedium_QualTight")),
         ("MUON_EFF_TRIG_SYS_1up",  W_STR_FMT.format("n_muons", 
            "mu_0_sf_MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu26_ivarmedium_QualTight")),
        )
    }  # W_MU

    W_EL = {

        "el_0_sf_NOMINAL_EleEffSF_offline_RecoTrk": (
            W_STR_FMT.format("n_electrons", "el_0_sf_NOMINAL_EleEffSF_offline_RecoTrk"),

            ("EL_EFF_RECO_TOTAL_1down", W_STR_FMT.format("n_electrons", "el_0_sf_EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_RecoTrk")),
            ("EL_EFF_RECO_TOTAL_1up", W_STR_FMT.format("n_electrons", "el_0_sf_EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_RecoTrk")),
        ),


        "el_0_sf_NOMINAL_EleEffSF_Isolation_TightLLH_d0z0_v13_FCTight": (
            W_STR_FMT.format(
                "n_electrons", "el_0_sf_NOMINAL_EleEffSF_Isolation_TightLLH_d0z0_v13_FCTight"),

            ("EL_EFF_ISO_TOTAL_1down", W_STR_FMT.format("n_electrons","el_0_sf_EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_TightLLH_d0z0_v13_FCTight")),
            ("EL_EFF_ISO_TOTAL_1up", W_STR_FMT.format("n_electrons","el_0_sf_EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_TightLLH_d0z0_v13_FCTight")),

        ),

        "el_0_sf_NOMINAL_EleEffSF_offline_TightLLH_d0z0_v13": (
            W_STR_FMT.format(
                "n_electrons", "el_0_sf_NOMINAL_EleEffSF_offline_TightLLH_d0z0_v13"),

            ("EL_EFF_ID_TOTAL_1down", W_STR_FMT.format("n_electrons","el_0_sf_EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_TightLLH_d0z0_v13")),
            ("EL_EFF_ID_TOTAL_1up", W_STR_FMT.format("n_electrons","el_0_sf_EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_TightLLH_d0z0_v13")),
        ),

        "el_0_sf_EleEffSF_Trig": (
            W_STR_FMT.format(
                "n_electrons", 
                #"el_0_sf_NOMINAL_EleEffSF_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_MediumLLH_d0z0_v13_isolFCTight_2015*"
                "el_0_sf_NOMINAL_EleEffSF_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_TightLLH_d0z0_v13_isolFCTight_2016"
                    # "*el_0_sf_NOMINAL_EleEffSF_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_TightLLH_d0z0_v13_isolFCTight_2017"
                    ),

            ("EL_EFF_TRIGGER_TOTAL_1down", W_STR_FMT.format(
                "n_electrons",                 "el_0_sf_EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_TightLLH_d0z0_v13_isolFCTight_2016")),

            ("EL_EFF_TRIGGER_TOTAL_1up", W_STR_FMT.format(
                "n_electrons",                 "*el_0_sf_EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_TightLLH_d0z0_v13_isolFCTight_2016")),
        )

    }

    ## met trigger efficiency  (apply overall lumi weighted or apply it per year)
    W_TRIGGER_TAUJET = {
        "metTrigEff": (
            "metTrigEff(met_p4->Et(), 1000, NOMINAL_pileup_random_run_number)", #<! NOMINAL
            ("metTrigEff_MEDIUM_TAU", "metTrigEff(met_p4->Et(), 1001, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_TIGHT_TAU", "metTrigEff(met_p4->Et(), 1002, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_MEDIUM_EL", "metTrigEff(met_p4->Et(), 1003, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_TIGHT_EL", "metTrigEff(met_p4->Et(), 1004, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_THREE_JETS",  "metTrigEff(met_p4->Et(), 1005, NOMINAL_pileup_random_run_number)"),
            # "metTrigEff(met_p4->Et(), 1000)",
        ),
    }

    # different scale factor components
    TYPES = {
        "taujet": {
            "BASE": W_BASE,
            # "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "TRIGGER": W_TRIGGER_TAUJET
        },

        "taulep": {
            "BASE": W_BASE,
            # "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "MU": W_MU,
            "EL": W_EL,
        },
    }

    CHANNELS = ["taujet", "taulep"]
    YEARS = ["2015", "2016", "2017", "2018"]

    @classmethod
    def factory(cls):
        """
        """
        # container for all wights and possible variations
        ws_dict = {}
        for channel in cls.CHANNELS:
            weights = []
            for wtype, wd in cls.TYPES[channel].iteritems():
                for w, variations in wd.iteritems():
                    weight = cls(
                        w, title=variations[0], variations=variations[:],  wtype=wtype, channel=channel)
                    weights.append(weight)
            ws_dict[channel] = weights

        return ws_dict

    def __init__(self, name, title=None, wtype="", variations=[], channel="taujet",):
        self.channel = channel

        assert wtype.upper() in self.TYPES[self.channel].keys(
            ), "%s weight is not supported; see weights.Weight" % wtype.upper()
        self.name = name
        self.wtype = wtype
        self.variations = variations
        if not title:
            title = name
        self.title = title

    def __repr__(self):
        return "WEIGHT:: name=%r, title=%r, type=%r, channel=%r," % (
            self.name, self.title, self.wtype, self.channel)


# prep weight classes
WEIGHTS = Weight.factory()
