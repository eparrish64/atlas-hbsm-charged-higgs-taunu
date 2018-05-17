import ROOT
__all__ = ["WEIGHTS"]

## scale factors 
WEIGHTS = {
    'general':
        {
        'weight_mc':{},
        'weight_total/weight_mc':{}, #< pile up weight
        },
    
    #--# Tau
    'tau':
        {
        'tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium':
            {
            "UP": "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1up_TauEffSF_JetBDTmedium/tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium",
            "DOWN": "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1down_TauEffSF_JetBDTmedium/tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium",
            },
        'tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron':
            {
            "UP": "tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_VeryLooseLlhEleOLR_electron/tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron",
            "DOWN": "tau_0_sf_TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_VeryLooseLlhEleOLR_electron/tau_0_sf_NOMINAL_TauEffSF_VeryLooseLlhEleOLR_electron",
            },
        'tau_0_sf_NOMINAL_TauEffSF_reco':
            {
            "UP": "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco/tau_0_sf_NOMINAL_TauEffSF_reco",
            "DOWN": "tau_0_sf_TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_reco/tau_0_sf_NOMINAL_TauEffSF_reco",
            }
        },
    
    # "UP": "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTmedium/tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium",
    # "DOWN": "tau_0_sf_TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTmedium/tau_0_sf_NOMINAL_TauEffSF_JetBDTmedium",

    #--# Jet
    'jet': {
        'jet_sf_NOMINAL_central_jets_global_ineffSF_JVT':
            {
            "UP": "jet_sf_JET_JvtEfficiency_1up_central_jets_global_ineffSF_JVT/jet_sf_NOMINAL_central_jets_global_ineffSF_JVT",
            "DOWN": "jet_sf_JET_JvtEfficiency_1down_central_jets_global_ineffSF_JVT/jet_sf_NOMINAL_central_jets_global_ineffSF_JVT",
            },
        'jet_sf_NOMINAL_central_jets_global_effSF_JVT':
            {
            "UP": "jet_sf_JET_JvtEfficiency_1up_central_jets_global_effSF_JVT/jet_sf_NOMINAL_central_jets_global_effSF_JVT",
            "DOWN": "jet_sf_JET_JvtEfficiency_1down_central_jets_global_effSF_JVT/jet_sf_NOMINAL_central_jets_global_effSF_JVT",
            },

        'jet_sf_NOMINAL_global_effSF_MVX': #<! check bjet sf components systs below
            {
            "UP": "jet_sf_FT_EFF_extrapolation_1up_global_effSF_MVX/jet_sf_NOMINAL_global_effSF_MVX",
            "DOWN": "jet_sf_FT_EFF_extrapolation_1down_global_effSF_MVX/jet_sf_NOMINAL_global_effSF_MVX",
            },
        'jet_sf_NOMINAL_global_ineffSF_MVX':
            {
            "UP": "jet_sf_FT_EFF_extrapolation_1up_global_ineffSF_MVX/jet_sf_NOMINAL_global_ineffSF_MVX",
            "DOWN": "jet_sf_FT_EFF_extrapolation_1down_global_ineffSF_MVX/jet_sf_NOMINAL_global_ineffSF_MVX",
            },
        },
    } #<! WEIGHTS


#--# QCD fakes scale factors
sf_weight_string="((({0})/(({1})+({1}==0)))+({0}==0)*({1}==0))"
FAKES_SF_SYSTS = [
    {"name": "tau_ff_stat_up",
     "ffQCD": "GetFF02_QCD_up(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR": "GetFF02_WCR_up(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True
     },
    
    {"name": "tau_ff_stat_down",
     "ffQCD": "GetFF02_QCD_dn(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR": "GetFF02_WCR_dn(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True
     },
    
    {"name": "tau_ff_bdt_up",
     "ffQCD": "GetFF01_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR": "GetFF01_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True,
     "tauID":"(!tau_0_jet_bdt_loose&&tau_0_jet_bdt_score_sig>0.01)"
     },
    
    {"name": "tau_ff_bdt_do",
     "ffQCD":"GetFF03_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR":"GetFF03_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True,
     "tauID":"(!tau_0_jet_bdt_loose&&tau_0_jet_bdt_score_sig>0.03)"
     },
    
    {"name":"tau_ff_alpha_up",
     "ffQCD":"GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR":"GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
      "weight":"GetFFCombined_up(tau_0_pt/1000, tau_0_n_tracks, ffQCD, ffWCR, regionFFIDX)",
     "isFFSys":True},
    {"name":"tau_ff_alpha_down",
     "ffQCD":"GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR":"GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "weight":"GetFFCombined_dn(tau_0_pt/1000, tau_0_n_tracks, ffQCD, ffWCR, regionFFIDX)",
     "isFFSys":True},

   # FF MC subtraction
    {"name":"tau_ff_mcsub_up",
     "weight":"1+0.5*(!tau_0_jet_bdt_loose)*((abs(tau_0_truth_universal_pdgId)==11)"
     "+(abs(tau_0_truth_universal_pdgId)==13)+(abs(tau_0_truth_universal_pdgId)==15))",
 #    "isFFSys":True,
     },
    {"name":"tau_ff_mcsub_down",
     "weight":"1/(1+0.5*(!tau_0_jet_bdt_loose)*((abs(tau_0_truth_universal_pdgId)==11)"
     "+(abs(tau_0_truth_universal_pdgId)==13)+(abs(tau_0_truth_universal_pdgId)==15)))",
#     "isFFSys":True,
     },

    {"name": "tau_eleolr_el_up",
     "weight":sf_weight_string.format(
            "(abs(tau_0_truth_universal_pdgId)!=11) + (abs(tau_0_truth_universal_pdgId)==11)*GetElFakeSFup(tau_0_n_tracks, tau_0_eta)",
            "(abs(tau_0_truth_universal_pdgId)!=11) + (abs(tau_0_truth_universal_pdgId)==11)*GetElFakeSF(tau_0_n_tracks, tau_0_eta)")
     },
    {"name":"tau_eleolr_el_down",
     "weight":sf_weight_string.format(
            "(abs(tau_0_truth_universal_pdgId)!=11) + (abs(tau_0_truth_universal_pdgId)==11)*GetElFakeSFdn(tau_0_n_tracks, tau_0_eta)",
            "(abs(tau_0_truth_universal_pdgId)!=11) + (abs(tau_0_truth_universal_pdgId)==11)*GetElFakeSF(tau_0_n_tracks, tau_0_eta)")
     },
    
    ] #<! FAKES_SF_SYSTS

# <<-----------------------------------------------------
# << Fake heavy flavor
FAKES_LH_SF_SYSTS = [
    {"name":"tau_ff_FFcompareMV1_BDT90to120reg3_1up",
     "ffQCD":"FFcompareMV1_BDT90to120reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_90to120_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p)*GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     
     "ffWCR":"FFcompareMV1_BDT90to120reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_90to120_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p)*GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True},
    
    {"name":"tau_ff_FFcompareMV1_BDT130to160reg3_1up",
     "ffQCD":"FFcompareMV1_BDT130to160reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_130to160_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p)*GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     
     "ffWCR":"FFcompareMV1_BDT130to160reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_130to160_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p)*GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True},
    
    {"name":"tau_ff_FFcompareMV1_BDT160to180reg3_1up",
     "ffQCD":"FFcompareMV1_BDT160to180reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_160to180_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p)*GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     
     "ffWCR":"FFcompareMV1_BDT160to180reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_160to180_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p)*GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True},
    
    {"name":"tau_ff_FFcompareMV1_BDT200to400reg3_1up",
     "ffQCD":"FFcompareMV1_BDT200to400reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_200to400_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p)*GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     
     "ffWCR":"FFcompareMV1_BDT200to400reg3((tau_0_n_tracks != 1)*FastBDT_sig_6V_met150_Opt_200to400_3p"
     "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p)*GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True},
    
    {"name":"tau_ff_FFcompareMV1_BDT500to2000reg3_1up",
     "ffQCD":"FFcompareMV1_BDT500to2000reg3(FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p)*GetFF02_QCD(tau_0_pt/1000,tau_0_n_tracks)",
     "ffWCR":"FFcompareMV1_BDT500to2000reg3(FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p)*GetFF02_WCR(tau_0_pt/1000,tau_0_n_tracks)",
     "isFFSys":True},
    ] #<! LH fakes

    
#--# met trigger efficiency 
NOM_TRIG_EFF = "nominal_trig_eff(met_et/1000)" 
MET_EFF_SF_SYST = [ #<! symmetric up and down
    {"name":"e_medium_trig_eff_up",
     "weight": "e_medium_trig_eff(met_et/1000) / %s"%NOM_TRIG_EFF},

    {"name":"e_tight_trig_eff_up",
     "weight":"e_tight_trig_eff(met_et/1000) / %s"%NOM_TRIG_EFF},
    
    {"name":"tau_medium_trig_eff_up",
     "weight":"tau_medium_trig_eff(met_et/1000) / %s"%NOM_TRIG_EFF},

    {"name":"tau_tight_trig_eff_up",
     "weight":"tau_tight_trig_eff(met_et/1000) / %s"%NOM_TRIG_EFF},
    
    {"name": "met_trig_eff_stat_up",
     "weight": "stat_trig_eff(met_et/1000)/%s"%NOM_TRIG_EFF},

    {"name":"three_jets_trig_eff_up", 
     "weight": "Threejets_trig_eff(met_et/1000)/%s"%NOM_TRIG_EFF},
    # {"name": "met_trig_eff_stat_down",
    #  "weight": "1/stat_trig_eff(met_et/1000)/%s"%NOM_TRIG_EFF},
    ]

#--# ttbar theory uncerts
TTBar_Theory_SYSTS = [
    {"name":"ttbar_scale_up",
     "weight":"GetShapeWeight(tau_0_met_mt/1000., 0)"},
    {"name":"ttbar_scale_down",
     "weight":"GetShapeWeight(tau_0_met_mt/1000., 1)"},
    
    {"name":"ttbar_model_up",
     "weight":"GetShapeWeight(tau_0_met_mt/1000., 2)"},
    # {"name":"ttbar_model_down",
    #  "weight":"1./GetShapeWeight(tau_0_met_mt/1000., 2)"},
    
    {"name":"ttbar_psue_up",
     "weight":"GetShapeWeight(tau_0_met_mt/1000., 3)"},
    # {"name":"ttbar_psue_down",
    #  "weight":"1./GetShapeWeight(tau_0_met_mt/1000., 3)"},
    ]

#--# bjet scale factors systematics
BJET_SF_NOM = "(jet_sf_NOMINAL_global_ineffSF_MVX*jet_sf_NOMINAL_global_effSF_MVX)"
BJET_SF_SYSTS = [
    {"name":"FT_EFF_Eigen_B_0_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_B_0_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_0_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_B_0_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_B_0_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_0_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_B_1_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_B_1_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_1_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_B_1_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_B_1_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_1_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_B_2_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_B_2_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_2_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_B_2_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_B_2_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_2_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_B_3_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_B_3_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_3_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_B_3_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_B_3_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_3_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_B_4_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_B_4_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_4_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_B_4_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_B_4_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_4_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_B_5_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_B_2_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_5_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_B_5_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_B_2_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_B_5_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},


    {"name":"FT_EFF_Eigen_C_0_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_C_0_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_0_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_C_0_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_C_0_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_0_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    # # # # # very very small 
    {"name":"FT_EFF_Eigen_C_1_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_C_1_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_1_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_C_1_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_C_1_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_1_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_C_2_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_C_2_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_2_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_C_2_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_C_2_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_2_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    # {"name":"FT_EFF_Eigen_C_3_1down",
    #  "weight":"(jet_sf_FT_EFF_Eigen_C_3_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_3_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    # {"name":"FT_EFF_Eigen_C_3_1up",
    #  "weight":"(jet_sf_FT_EFF_Eigen_C_3_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_C_3_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_0_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_0_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_0_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_0_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_0_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_0_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_1_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_1_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_1_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_1_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_1_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_1_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_2_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_2_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_2_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_2_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_2_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_2_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_3_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_3_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_3_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_3_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_3_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_3_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_4_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_4_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_4_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_4_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_4_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_4_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},

    {"name":"FT_EFF_Eigen_Light_5_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_5_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_5_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_5_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_5_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_5_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_6_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_6_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_6_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_6_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_6_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_6_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_7_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_7_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_7_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_7_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_7_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_7_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_8_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_8_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_8_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_8_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_8_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_8_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},

    {"name":"FT_EFF_Eigen_Light_9_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_9_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_9_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_9_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_9_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_9_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_10_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_10_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_10_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_10_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_10_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_10_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_11_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_11_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_11_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_11_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_11_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_11_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_12_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_12_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_12_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_12_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_12_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_12_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},

    {"name":"FT_EFF_Eigen_Light_13_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_13_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_13_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_13_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_13_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_13_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_14_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_14_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_14_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_14_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_14_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_14_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_Eigen_Light_15_1down",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_15_1down_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_15_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_Eigen_Light_15_1up",
     "weight":"(jet_sf_FT_EFF_Eigen_Light_15_1up_global_ineffSF_MVX*jet_sf_FT_EFF_Eigen_Light_15_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_extrapolation_1down",
     "weight":"(jet_sf_FT_EFF_extrapolation_1down_global_ineffSF_MVX*jet_sf_FT_EFF_extrapolation_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_extrapolation_1up",
     "weight":"(jet_sf_FT_EFF_extrapolation_1up_global_ineffSF_MVX*jet_sf_FT_EFF_extrapolation_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    {"name":"FT_EFF_extrapolation_from_charm_1down",
     "weight":"(jet_sf_FT_EFF_extrapolation_from_charm_1down_global_ineffSF_MVX"
     "*jet_sf_FT_EFF_extrapolation_from_charm_1down_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    {"name":"FT_EFF_extrapolation_from_charm_1up",
     "weight":"(jet_sf_FT_EFF_extrapolation_from_charm_1up_global_ineffSF_MVX"
     "*jet_sf_FT_EFF_extrapolation_from_charm_1up_global_effSF_MVX)/{0}".format(BJET_SF_NOM)},
    
    ] #<! BJET_SF_SYSTS



#--# prepare event weight 
#--#--------------------------------------------------------------------------
top_pt_weight  = "GetTopPtWeight(truth_top0_pt)"
met_eff_weight = "nominal_trig_eff(met_et/1000)"
electron_elor_weight = "(abs(tau_0_truth_universal_pdgId)!=11) + (abs(tau_0_truth_universal_pdgId)==11)*GetElFakeSF(tau_0_n_tracks, tau_0_eta)"

eventWeight = "1"
for w_cat, components in WEIGHTS.iteritems():
    for w in components:
        eventWeight += "*%s"%w

#--# met eff, top pt weight and ELOR
eventWeight += "*%s"%met_eff_weight
eventWeight += "*%s"%top_pt_weight
electron_elor_weight += "*%s"%electron_elor_weight
TAUJET_EVTWEIGHT  = ROOT.TCut(eventWeight)

#--# weight systematics 
COMMON_SF_SYSTS = []
for w_type in WEIGHTS.keys():
    for name, weight in WEIGHTS[w_type].iteritems():
        if len(weight) > 1:
            COMMON_SF_SYSTS.append({"name": name+"_UP", "weight": weight["UP"]})
            COMMON_SF_SYSTS.append({"name": name+"_DOWN", "weight": weight["DOWN"]})
            
# <<-----------------------------------------------------------------------------
# << add fakes SF syst and Bjet SF syst
weight_sys_list  = []
weight_sys_list += COMMON_SF_SYSTS
weight_sys_list += MET_EFF_SF_SYST
weight_sys_list += FAKES_SF_SYSTS 
weight_sys_list += BJET_SF_SYSTS
weight_sys_list += FAKES_LH_SF_SYSTS

#weight_sys_list += TTBar_Theory_SYSTS #<! NOT NEEDED ANYMORE !

