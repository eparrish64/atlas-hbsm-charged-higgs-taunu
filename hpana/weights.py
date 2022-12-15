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
        "weight_pileup": ("NOMINAL_pileup_combined_weight", ) #("weight_total/weight_mc", )
    }

    W_BASE = {
        "weight_total": ("weight_mc", )
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
            ("TAU_EFF_RNNID_HIGHPT_1up" , W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RNNID_HIGHPT_1up_TauEffSF_JetRNNmedium")),
            ("TAU_EFF_RNNID_HIGHPT_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RNNID_HIGHPT_1down_TauEffSF_JetRNNmedium")),

            ("TAU_EFF_RNNID_SYST_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RNNID_SYST_1up_TauEffSF_JetRNNmedium")),
            ("TAU_EFF_RNNID_SYST_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RNNID_SYST_1down_TauEffSF_JetRNNmedium")),
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

            #("TAU_EFF_RECO_HIGHPT_1up", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_reco")),
            #("TAU_EFF_RECO_HIGHPT_1down", W_STR_FMT.format("n_taus", "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_reco")),
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
 #       "jet_sf_NOMINAL_global_effSF_MV2c10":(
 #           "jet_sf_NOMINAL_global_effSF_MV2c10", #<! NOMINAL 
 #           ("jet_effSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_effSF_MV2c10", ),
 #           ("jet_effSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_effSF_MV2c10", ),

 #           ("jet_effSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_effSF_MV2c10", ),
 #           ("jet_effSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_effSF_MV2c10", ),

 #           ("jet_effSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_effSF_MV2c10", ),
 #           ("jet_effSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_effSF_MV2c10", ),

 #           ("jet_effSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_effSF_MV2c10", ),
 #           ("jet_effSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_effSF_MV2c10", ),            
 #           ),
        
        "jet_sf_NOMINAL_global_effSF_DL1r_FixedCutBEff_70":(
            "jet_sf_NOMINAL_global_effSF_DL1r_FixedCutBEff_70", #<! NOMINAL 
            ("jet_effSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_effSF_DL1r_FixedCutBEff_70", ),

            ("jet_effSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_effSF_DL1r_FixedCutBEff_70", ),

            ("jet_effSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_effSF_DL1r_FixedCutBEff_70",),

            ("jet_effSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_effSF_DL1r_FixedCutBEff_70", ),
            ("jet_effSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_effSF_DL1r_FixedCutBEff_70", ),
            ),
            
        

#        "jet_sf_NOMINAL_global_ineffSF_MV2c10":(
#            "jet_sf_NOMINAL_global_ineffSF_MV2c10",

#            ("jet_ineffSF_Eigen_B_0_1down",  "jet_sf_FT_EFF_Eigen_B_0_1down_global_ineffSF_MV2c10",),
#            ("jet_ineffSF_Eigen_B_0_1up",  "jet_sf_FT_EFF_Eigen_B_0_1up_global_ineffSF_MV2c10", ),

#            ("jet_ineffSF_Eigen_C_0_1down",  "jet_sf_FT_EFF_Eigen_C_0_1down_global_ineffSF_MV2c10", ),
#            ("jet_ineffSF_Eigen_C_0_1up",  "jet_sf_FT_EFF_Eigen_C_0_1up_global_ineffSF_MV2c10", ),

#            ("jet_ineffSF_Eigen_Light_0_1down",  "jet_sf_FT_EFF_Eigen_Light_0_1down_global_ineffSF_MV2c10", ),
#            ("jet_ineffSF_Eigen_Light_0_1up",  "jet_sf_FT_EFF_Eigen_Light_0_1up_global_ineffSF_MV2c10", ),

#            ("jet_ineffSF_extrapolation_1down",  "jet_sf_FT_EFF_extrapolation_1down_global_ineffSF_MV2c10", ),
#            ("jet_ineffSF_extrapolation_1up",  "jet_sf_FT_EFF_extrapolation_1up_global_ineffSF_MV2c10", ),            
#            ),
    }  # W_JET


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
                "n_electrons",                 "el_0_sf_EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_TightLLH_d0z0_v13_isolFCTight_2016")),
        )

    }

    ## met trigger efficiency  (apply overall lumi weighted or apply it per year)
    W_TRIGGER_TAUJET = {
        "metTrigEff": (
            "metTrigEff(met_p4->Et(), 1000, NOMINAL_pileup_random_run_number)", #<! NOMINAL
            ("metTrigEff_SYST_UP", "metTrigEff(met_p4->Et(), 1001, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_SYST_DOWN", "metTrigEff(met_p4->Et(), 1002, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_STAT_UP",  "metTrigEff(met_p4->Et(), 1101, NOMINAL_pileup_random_run_number)"),
            ("metTrigEff_STAT_DOWN",  "metTrigEff(met_p4->Et(), 1102, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_MEDIUM_TAU", "metTrigEff(met_p4->Et(), 1001, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_TIGHT_TAU", "metTrigEff(met_p4->Et(), 1002, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_MEDIUM_EL", "metTrigEff(met_p4->Et(), 1003, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_TIGHT_EL", "metTrigEff(met_p4->Et(), 1004, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_THREE_JETS",  "metTrigEff(met_p4->Et(), 1005, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_TWO_BJETS",  "metTrigEff(met_p4->Et(), 1006, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_STAT_1UP",  "metTrigEff(met_p4->Et(), 1101, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_STAT_1DOWN",  "metTrigEff(met_p4->Et(), 1102, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_STAT_2UP",  "metTrigEff(met_p4->Et(), 1103, NOMINAL_pileup_random_run_number)"),
            #("metTrigEff_STAT_2DOWN",  "metTrigEff(met_p4->Et(), 1104, NOMINAL_pileup_random_run_number)"),
        ),
    }

    W_TTBAR_THEORY = {
        # These theory sytematic involve per-sample weights to e.g. repalce the nominal sample with a variation
        # The values here (1) are a placeholder, to keep all unrelated samples from being affected
        # These values should be replaced on a per-sample basis in get_sample_variation_weight (similar to how we adjust PRW for signal)
        "ttbar_model": ( 
            "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
            ("ttbar_model_POWHEG_HERWIG7", "1"), # per-sample logic goes in samples.py
        ),
        "ttbar_ISR": (
            "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
            ("ttbar_ISR_1up", "1"),
            ("ttbar_ISR_1down", "1"),
        ),
        "ttbar_PDF": (
            "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
            ("ttbar_PDF_1", "1"),
            ("ttbar_PDF_2", "1"),
            ("ttbar_PDF_3", "1"),
            ("ttbar_PDF_4", "1"),
            ("ttbar_PDF_5", "1"),
            ("ttbar_PDF_6", "1"),
            ("ttbar_PDF_7", "1"),
            ("ttbar_PDF_8", "1"),
            ("ttbar_PDF_9", "1"),
            ("ttbar_PDF_10", "1"),
            ("ttbar_PDF_11", "1"),
            ("ttbar_PDF_12", "1"),
            ("ttbar_PDF_13", "1"),
            ("ttbar_PDF_14", "1"),
            ("ttbar_PDF_15", "1"),
            ("ttbar_PDF_16", "1"),
            ("ttbar_PDF_17", "1"),
            ("ttbar_PDF_18", "1"),
            ("ttbar_PDF_19", "1"),
            ("ttbar_PDF_20", "1"),
            ("ttbar_PDF_21", "1"),
            ("ttbar_PDF_22", "1"),
            ("ttbar_PDF_23", "1"),
            ("ttbar_PDF_24", "1"),
            ("ttbar_PDF_25", "1"),
            ("ttbar_PDF_26", "1"),
            ("ttbar_PDF_27", "1"),
            ("ttbar_PDF_28", "1"),
            ("ttbar_PDF_29", "1"),
            ("ttbar_PDF_30", "1"),
        ),
        "ttbar_FSR": ( # TODO check if FSR is needed for our analysis, it's not for most, but "everyone should check"
            "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
            ("ttbar_FSR_1up", "1"),
            ("ttbar_FSR_1down", "1"),
        ),
    }  # W_TTBAR_THEORY

    W_SINGLETOP_THEORY = {
        # These theory sytematic involve per-sample weights to e.g. repalce the nominal sample with a variation
        # The values here (1) are a placeholder, to keep all unrelated samples from being affected
        # These values should be replaced on a per-sample basis in samples.py (similar to how we adjust PRW for signal)
        "singletop_model": ( 
            "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
            ("singletop_model_POWHEG_HERWIG7", "1"), # per-sample logic goes in get_sample_variation_weight
        ),
    }  # W_SINGLETOP_THEORY
    
    W_TTBAR_REWEIGHT = {
      "wttbar_fit": (
        "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
        ("wttbar_1up", "1"),
        ("wttbar_1down", "1"),
      ),
    }
    
    W_WJETS_REWEIGHT = {
      "wwtjets_fit": (
        "1", #<! NOMINAL, per-sample logic is in get_sample_variation_weight
        ("wwtjets_1up", "1"),
        ("wwtjets_1down", "1"),
      ),
    }

    # different scale factor components
    TYPES = {
        "taujet": {
            "BASE": W_BASE,
            "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "TRIGGER": W_TRIGGER_TAUJET,
            "TTBAR": W_TTBAR_THEORY,
            "SINGLETOP": W_SINGLETOP_THEORY,
            "TTBAR_REWEIGHT": W_TTBAR_REWEIGHT,
            "WJETS_REWEIGHT": W_WJETS_REWEIGHT,
        },

        "taulep": {
            "BASE": W_BASE,
            "PILEUP": W_PILEUP,
            "TAU": W_TAU,
            "JET": W_JET,
            "BJET": W_BJET,
            "MU": W_MU,
            "EL": W_EL,
            "TTBAR": W_TTBAR_THEORY,
            "SINGLETOP": W_SINGLETOP_THEORY,
            "TTBAR_REWEIGHT": W_TTBAR_REWEIGHT,
            "WJETS_REWEIGHT": W_WJETS_REWEIGHT,
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

##---------------------------------------------------------------------------------------
##

# This is for samples that need their own custom weights per variation, which may not be available in other samples
# E.g. some ttbar theory weights
# TODO? find somewhere better to put this function, it's thrown in here kind of ad-hoc just to have it somewhere...

def get_sample_variation_weight(systematic, variation, dataset, sample, channel):

  specialSampleDefaults = {
    # These samples have different weights depending on the systematic variation
    # These are the default weights to use, if it's not a variaton where a special case is needed

    # ttbar nominal
    "PhPy8EG_A14_ttbar_hdamp258p75_nonallhad": "1",
    "PhPy8EG_A14_ttbar_hdamp258p75_allhad": "1",

    # ttbar theory variations
    "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75_704_singlelepton": "0",
    "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75_704_dilepton": "0",
    "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75_allhad": "0",
    "PhPy8EG_A14_ttbar_hdamp517p5_SingleLep": "0",
    "PhPy8EG_A14_ttbar_hdamp517p5_allhad": "0",
    "PhPy8EG_A14_ttbar_hdamp517p5_dil": "0",
    
    # singletop nominal
    "PhPy8EG_A14_tchan_BW50_lept_top": "1",
    "PhPy8EG_A14_tchan_BW50_lept_antitop": "1",
    "PowhegPythia8EvtGen_A14_singletop_schan_lept_top": "1",
    "PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop": "1",
    "PowhegPythia8EvtGen_A14_Wt_DR_inclusive_top": "1",
    "PowhegPythia8EvtGen_A14_Wt_DR_inclusive_antitop": "1",
    "PowhegPythia8EvtGen_A14_Wt_DR_dilepton_top": "1",
    "PowhegPythia8EvtGen_A14_Wt_DR_dilepton_antitop": "1",
    
    # singletop theory variations   
    "PowhegHerwig7EvtGen_H7UE_704_tchan_lept_antitop": "0",
    "PowhegHerwig7EvtGen_H7UE_704_tchan_lept_top": "0",
    "PhHerwig7EG_H7UE_singletop_schan_lept_top": "0",
    "PhHerwig7EG_H7UE_singletop_schan_lept_antitop": "0",
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_inclusive_top": "0",
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_inclusive_antitop": "0",
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_dilepton_top": "0",
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_dilepton_antitop": "0",
  }

  specialSampleVariations = {
    # These samples have different weights depending on the systematic variation
    # These are the special weights to use for certain variations
    # For example, nominal ttbar will be disabled for certain systematics, or apply an extra weight from a branch that isn't present in other samples
    # Note: These must match the physics short names from the xsec file exactly, otherwise it will silently give wrong results(!)
    #   This may not be the same as the physics short name from e.g. getMetadata.py (from AthAnalysis)!
    #   # TODO double check all of these!

    # ttbar nominal
    "PhPy8EG_A14_ttbar_hdamp258p75_nonallhad": {
      "ttbar_model": {
        "ttbar_model_POWHEG_HERWIG7": "0",
      },
      "ttbar_ISR": {
        "ttbar_ISR_1up": "0",
        "ttbar_ISR_1down": "pmg_truth_weight_ISRLo",
      },
      "ttbar_FSR": {
        "ttbar_FSR_1up": "pmg_truth_weight_FSRHi",
        "ttbar_FSR_1down": "pmg_truth_weight_FSRLo",
      },
      "ttbar_PDF": {
        "ttbar_PDF_1": "pmg_truth_weight_pdf_signal_weight_1/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_2": "pmg_truth_weight_pdf_signal_weight_2/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_3": "pmg_truth_weight_pdf_signal_weight_3/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_4": "pmg_truth_weight_pdf_signal_weight_4/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_5": "pmg_truth_weight_pdf_signal_weight_5/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_6": "pmg_truth_weight_pdf_signal_weight_6/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_7": "pmg_truth_weight_pdf_signal_weight_7/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_8": "pmg_truth_weight_pdf_signal_weight_8/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_9": "pmg_truth_weight_pdf_signal_weight_9/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_10": "pmg_truth_weight_pdf_signal_weight_10/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_11": "pmg_truth_weight_pdf_signal_weight_11/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_12": "pmg_truth_weight_pdf_signal_weight_12/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_13": "pmg_truth_weight_pdf_signal_weight_13/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_14": "pmg_truth_weight_pdf_signal_weight_14/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_15": "pmg_truth_weight_pdf_signal_weight_15/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_16": "pmg_truth_weight_pdf_signal_weight_16/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_17": "pmg_truth_weight_pdf_signal_weight_17/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_18": "pmg_truth_weight_pdf_signal_weight_18/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_19": "pmg_truth_weight_pdf_signal_weight_19/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_20": "pmg_truth_weight_pdf_signal_weight_20/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_21": "pmg_truth_weight_pdf_signal_weight_21/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_22": "pmg_truth_weight_pdf_signal_weight_22/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_23": "pmg_truth_weight_pdf_signal_weight_23/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_24": "pmg_truth_weight_pdf_signal_weight_24/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_25": "pmg_truth_weight_pdf_signal_weight_25/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_26": "pmg_truth_weight_pdf_signal_weight_26/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_27": "pmg_truth_weight_pdf_signal_weight_27/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_28": "pmg_truth_weight_pdf_signal_weight_28/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_29": "pmg_truth_weight_pdf_signal_weight_29/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_30": "pmg_truth_weight_pdf_signal_weight_30/pmg_truth_weight_pdf_signal_weight_0",
      },
    },
    "PhPy8EG_A14_ttbar_hdamp258p75_allhad": {
      "ttbar_model": {
        "ttbar_model_POWHEG_HERWIG7": "0",
      },
      "ttbar_ISR": {
        "ttbar_ISR_1up": "0",
        "ttbar_ISR_1down": "pmg_truth_weight_ISRLo",
      },
      "ttbar_FSR": {
        "ttbar_FSR_1up": "pmg_truth_weight_FSRHi",
        "ttbar_FSR_1down": "pmg_truth_weight_FSRLo",
      },
      "ttbar_PDF": {
        "ttbar_PDF_1": "pmg_truth_weight_pdf_signal_weight_1/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_2": "pmg_truth_weight_pdf_signal_weight_2/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_3": "pmg_truth_weight_pdf_signal_weight_3/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_4": "pmg_truth_weight_pdf_signal_weight_4/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_5": "pmg_truth_weight_pdf_signal_weight_5/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_6": "pmg_truth_weight_pdf_signal_weight_6/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_7": "pmg_truth_weight_pdf_signal_weight_7/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_8": "pmg_truth_weight_pdf_signal_weight_8/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_9": "pmg_truth_weight_pdf_signal_weight_9/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_10": "pmg_truth_weight_pdf_signal_weight_10/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_11": "pmg_truth_weight_pdf_signal_weight_11/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_12": "pmg_truth_weight_pdf_signal_weight_12/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_13": "pmg_truth_weight_pdf_signal_weight_13/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_14": "pmg_truth_weight_pdf_signal_weight_14/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_15": "pmg_truth_weight_pdf_signal_weight_15/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_16": "pmg_truth_weight_pdf_signal_weight_16/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_17": "pmg_truth_weight_pdf_signal_weight_17/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_18": "pmg_truth_weight_pdf_signal_weight_18/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_19": "pmg_truth_weight_pdf_signal_weight_19/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_20": "pmg_truth_weight_pdf_signal_weight_20/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_21": "pmg_truth_weight_pdf_signal_weight_21/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_22": "pmg_truth_weight_pdf_signal_weight_22/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_23": "pmg_truth_weight_pdf_signal_weight_23/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_24": "pmg_truth_weight_pdf_signal_weight_24/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_25": "pmg_truth_weight_pdf_signal_weight_25/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_26": "pmg_truth_weight_pdf_signal_weight_26/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_27": "pmg_truth_weight_pdf_signal_weight_27/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_28": "pmg_truth_weight_pdf_signal_weight_28/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_29": "pmg_truth_weight_pdf_signal_weight_29/pmg_truth_weight_pdf_signal_weight_0",
        "ttbar_PDF_30": "pmg_truth_weight_pdf_signal_weight_30/pmg_truth_weight_pdf_signal_weight_0",
      },
    },

    # ttbar theory variations
    "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75_704_singlelepton": {
      "ttbar_model": {
        "ttbar_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75_704_dilepton": {
      "ttbar_model": {
        "ttbar_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_tt_hdamp258p75_allhad": {
      "ttbar_model": {
        "ttbar_model_POWHEG_HERWIG7": "1",
      },
    },
    "PhPy8EG_A14_ttbar_hdamp517p5_SingleLep": {
      "ttbar_ISR": {
        "ttbar_ISR_1up": "pmg_truth_weight_ISRHi",
      },
    },
    "PhPy8EG_A14_ttbar_hdamp517p5_allhad": {
      "ttbar_ISR": {
        "ttbar_ISR_1up": "pmg_truth_weight_ISRHi",
      },
    },
    "PhPy8EG_A14_ttbar_hdamp517p5_dil": {
      "ttbar_ISR": {
        "ttbar_ISR_1up": "pmg_truth_weight_ISRHi",
      },
    },

    # singletop nominal
    "PhPy8EG_A14_tchan_BW50_lept_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PhPy8EG_A14_tchan_BW50_lept_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PowhegPythia8EvtGen_A14_singletop_schan_lept_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PowhegPythia8EvtGen_A14_Wt_DR_inclusive_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PowhegPythia8EvtGen_A14_Wt_DR_inclusive_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PowhegPythia8EvtGen_A14_Wt_DR_dilepton_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    "PowhegPythia8EvtGen_A14_Wt_DR_dilepton_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "0",
      },
    },
    
    # singletop theory variations   
    "PowhegHerwig7EvtGen_H7UE_704_tchan_lept_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_704_tchan_lept_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PhHerwig7EG_H7UE_singletop_schan_lept_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PhHerwig7EG_H7UE_singletop_schan_lept_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_inclusive_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_inclusive_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_dilepton_top": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
    "PowhegHerwig7EvtGen_H7UE_Wt_DR_dilepton_antitop": {
      "singletop_model": {
        "singletop_model_POWHEG_HERWIG7": "1",
      },
    },
  }

  sampleChannelDefaults = {
    "TTbar": {
      "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1)",
      "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1)",
    },
    "Wtaunu": {
      "taujet": "njets(n_jets,1)",
      "taulep": "njets(n_jets,1)",
    }
  }

  # Dedicated reweightings, different per channel
  sampleChannelVariations = {
    "TTbar": { # Note that it's TTbar in general, not a specific sample, since the reweighting was found using all samples
      "ttbar_model": {
        "ttbar_model_POWHEG_HERWIG7": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1001)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt() + el_0_p4->Pt(),1001)",
        },
      },
      "ttbar_ISR": {
        "ttbar_ISR_1up": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1002)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt() + el_0_p4->Pt(),1002)",
        },
        "ttbar_ISR_1down": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1003)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt() + el_0_p4->Pt(),1003)",
        }, 
      },
      "ttbar_FSR": {
        "ttbar_FSR_1up": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1004)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt() + el_0_p4->Pt(),1004)",
        },
        "ttbar_FSR_1down": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1005)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt() + el_0_p4->Pt(),1005)",
        }, 
      },
      "wttbar_fit": {
        "wttbar_1up": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),2)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),2)",
        },
        "wttbar_1down": {
          "taujet": "eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),3)",
          "taulep": "eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),3)",
        },
      }
    },
    "Wtaunu": {
      "wwtjets_fit": {
        "wwtjets_1up": {
          "taujet": "njets(n_jets,2)",
          "taulep": "njets(n_jets,2)",
        },
        "wwtjets_1down": {
          "taujet": "njets(n_jets,3)",
          "taulep": "njets(n_jets,3)",
        },
      },
    },
  }

  w = "1"
  if dataset.ds in specialSampleVariations:
    # This dataset requires some weights to be handled in a special way
    w = specialSampleDefaults[dataset.ds] # set nominal value for this sample
    if systematic.name in specialSampleVariations[dataset.ds]:
      # This is a weight which requires special handling fo this sample
      if variation.name in specialSampleVariations[dataset.ds][systematic.name]:
        w = specialSampleVariations[dataset.ds][systematic.name][variation.name]
  w2 = "1"
  if sample in sampleChannelDefaults:
    if channel in sampleChannelDefaults[sample]:
      w2 = sampleChannelDefaults[sample][channel]
  if sample in sampleChannelVariations:
    if systematic.name in sampleChannelVariations[sample]:
      if variation.name in sampleChannelVariations[sample][systematic.name]:
        if channel in sampleChannelVariations[sample][systematic.name][variation.name]:
          w2 = sampleChannelVariations[sample][systematic.name][variation.name][channel]
  w = "(%s)*(%s)" % (w, w2)
  return w

