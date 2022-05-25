# -*- coding: utf-8 -*-

from math import pi
from collections import OrderedDict

import ROOT
# from ROOT import TCut

from hpana.db.decorators import cached_property
from hpana import log, MC_CAMPAIGN
from hpana.trigger import get_trigger

"""
This module provides all selections needed for the analysis.
PLEASE NOTE THAT THE UNIT IS CHANGED FROM MeV to GeV as of version 18v04 of the ntuples.
"""

##------------------------------------------------------------------------------------
##  - - clean events 
##------------------------------------------------------------------------------------

# - - - - - - - - event 
CLEAN_EVT = {
    "mc15": ROOT.TCut("(event_clean==1) && (n_vx>=1) && (bsm_tj_dirty_jet==0) && (useEvent==1)"),
    "mc16": ROOT.TCut("n_pvx > 0 && (useEvent==1)"),
}

##------------------------------------------------------------------------------------
##  - - mT and MET
##------------------------------------------------------------------------------------
MET50 = {
    "mc15": ROOT.TCut("met_et>50000"),
    "mc16": ROOT.TCut("met_p4->Et() > 50"),
}
MET100 = {
    "mc15": ROOT.TCut("met_et>100000"),
    "mc16": ROOT.TCut("met_p4->Et() > 100"),
}
    
MET150 = {
    "mc15": ROOT.TCut("met_et > 150000"),
    "mc16": ROOT.TCut("met_p4->Et() > 150"),
}

MET200 = {
    "mc15": ROOT.TCut("met_et > 200000"),
    "mc16": ROOT.TCut("met_p4->Et() > 200"),
}

MET_MAX150 = {
    "mc15": ROOT.TCut("met_et < 150000"),
    "mc16": ROOT.TCut("met_p4->Et() < 150"),
}
MET_MAX80 = {
    "mc15": ROOT.TCut("met_et < 80000"),
    "mc16": ROOT.TCut("met_p4->Et() < 80"),
}

MT50 = {
    "mc15": ROOT.TCut("tau_0_met_mt > 50000"),
    "mc16": ROOT.TCut("tau_0_met_mt > 50")
}
MT_MAX100 = {
    "mc15": ROOT.TCut("tau_0_met_mt < 100000"),
    "mc16": ROOT.TCut("tau_0_met_mt < 100")
}
MT_MAX70 = {
    "mc15": ROOT.TCut("tau_0_met_mt < 70000"),
    "mc16": ROOT.TCut("tau_0_met_mt < 70")
}

MT100 = {
    "mc15": ROOT.TCut("tau_0_met_mt > 100000"),
    "mc16": ROOT.TCut("tau_0_met_mt > 100")
}

MET80 = {
     "mc15": ROOT.TCut("met_et>80000"),
     "mc16": ROOT.TCut("met_p4->Et() > 80"),
}

 
##------------------------------------------------------------------------------------
##  - - tau
##------------------------------------------------------------------------------------
TAU_Q = ROOT.TCut("abs(tau_0_q)==1")
TAU_DECAY_MODE = ROOT.TCut("tau_0_decay_mode==0")

# TAUID_LOOSE = ROOT.TCut("tau_0_jet_bdt_loose==1")
# TAUID_MEDIUM = ROOT.TCut("tau_0_jet_bdt_medium==1")
# TAUID_TIGHT = ROOT.TCut("tau_0_jet_bdt_tight==1")

TAUID_LOOSE = ROOT.TCut("tau_0_jet_rnn_loose==1")
TAUID_MEDIUM = ROOT.TCut("tau_0_jet_rnn_medium==1")
TAUID_TIGHT = ROOT.TCut("tau_0_jet_rnn_tight==1")

TAU_1_TRACK = {
    "mc15": ROOT.TCut("tau_0_n_tracks==1"),
    "mc16": ROOT.TCut("tau_0_n_charged_tracks==1"),
}
TAU_3_TRACK = {
    "mc15": ROOT.TCut("tau_0_n_tracks==3"),
    "mc16": ROOT.TCut("tau_0_n_charged_tracks==3"),
}

TAU_TRACKS = {
    # "mc15": ROOT.TCut("tau_0_n_tracks==1"),
    # "mc16": ROOT.TCut("tau_0_n_charged_tracks==1"),
     #"mc15": ROOT.TCut("tau_0_n_tracks==3"),
     #"mc16": ROOT.TCut("tau_0_n_charged_tracks==3"),
    "mc15": ROOT.TCut("tau_0_n_tracks== 1 || tau_0_n_tracks==3"),
    "mc16": ROOT.TCut("tau_0_n_charged_tracks== 1 || tau_0_n_charged_tracks==3"),
}

TAU_PT30 = {
    "mc15": ROOT.TCut("tau_0_pt > 30000"),
    "mc16": ROOT.TCut("tau_0_p4->Pt() > 30") ,
}
TAU_PT40 = {
    "mc15": ROOT.TCut("tau_0_pt > 40000"),
    "mc16": ROOT.TCut("tau_0_p4->Pt() > 40") ,
}
TAU_ETA = {
    "mc15": ROOT.TCut("abs(tau_0_eta)<2.3 && !(abs(tau_0_eta)< 1.52 && abs(tau_0_eta)> 1.37)"),
    "mc16": ROOT.TCut("abs(tau_0_p4->Eta())<2.3 && !(abs(tau_0_p4->Eta())< 1.52 && abs(tau_0_p4->Eta())> 1.37)") ,
}

## tau truth label
TAU_IS_TRUE = ROOT.TCut("true_tau_0_isHadTau")
TAU_IS_LEP = ROOT.TCut("true_tau_0_isMuon || true_tau_0_isEle")
TAU_IS_EL = ROOT.TCut("true_tau_0_isEle")
TAU_IS_EL_OR_HAD = ROOT.TCut("true_tau_0_isHadTau || true_tau_0_isEle")
TAU_IS_LEP_OR_HAD = ROOT.TCut("true_tau_0_isHadTau || true_tau_0_isEle || true_tau_0_isMuon")

## tau jet parton label 
TAU_IS_LIGHT_QUARK = ROOT.TCut("true_tau_0_jet_pdgId>0 && true_tau_0_jet_pdgId <4")
TAU_IS_C_QUARK = ROOT.TCut("true_tau_0_jet_pdgId==4")
TAU_IS_B_QUARK = ROOT.TCut("true_tau_0_jet_pdgId==5")
TAU_IS_GLUON = ROOT.TCut("true_tau_0_jet_pdgId==21")
TAU_IS_OTHER = ROOT.TCut("!(%s || %s || %s ||%s ||%s || %s)"%(
    TAU_IS_EL.GetTitle(), TAU_IS_LIGHT_QUARK, TAU_IS_C_QUARK, TAU_IS_B_QUARK, TAU_IS_GLUON, TAU_IS_TRUE))

## QCD fake tau
TAU_IS_FAKE = ROOT.TCut("!(%s || %s)"%(TAU_IS_TRUE, TAU_IS_LEP))
#ANTI_TAU = ROOT.TCut("tau_0_jet_rnn_score_trans > 0.01 && tau_0_jet_rnn_loose==0")
#ANTI_TAU = ROOT.TCut("tau_0_jet_rnn_score_trans > 0.01 && tau_0_jet_rnn_medium==0")
ANTI_TAU = ROOT.TCut("tau_0_jet_rnn_score_trans > 0.01 && tau_0_jet_rnn_loose==0")
# ANTI_TAU = ROOT.TCut("tau_0_jet_rnn_loose==0")


VETO_TAU = ROOT.TCut("n_taus==0")
TAU_EL_OLR_PASS = {
    "mc15": ROOT.TCut("tau_0_ele_olr_pass==1"),
    "mc16": ROOT.TCut("tau_0_ele_bdt_medium_retuned==1"),
    # "mc16": ROOT.TCut("tau_0_ele_olr_pass==1"),

}

TAU_UPSILON = ROOT.TCut("tau_0_upsilon_pt_based<=1.2")

TAU_BASE = {}
for mcc in ["mc15", "mc16"]:
    TAU_BASE[mcc] = TAU_PT30[mcc] + TAU_ETA[mcc] + TAU_TRACKS[mcc] + TAU_EL_OLR_PASS[mcc] + TAU_UPSILON
    
##------------------------------------------------------------------------------------
##  - - lepton
##------------------------------------------------------------------------------------
LEP_VETO = {
    "mc15": ROOT.TCut("(n_electrons + n_muons)==0"),
    "mc16": ROOT.TCut("(n_electrons + n_muons)==0"),
}
ONE_LEP = ROOT.TCut("(n_electrons + n_muons)==1")

LEP_PT30 = {
    "mc15": ROOT.TCut("(mu_0_pt + el_0_pt)> 30000"),
    "mc16": ROOT.TCut("(mu_0_p4->Pt() + el_0_p4->Pt()) > 30") ,
}

# - - - - lep ID
ELID_TIGHT = {
    "mc15":ROOT.TCut("n_electrons && el_0_id_tight"),
    "mc16":ROOT.TCut("n_electrons && el_0_id_tight"),
}
MUID_TIGHT = {
    "mc15":ROOT.TCut("n_muons && mu_0_id_tight"),
    "mc16":ROOT.TCut("n_muons && mu_0_id_tight"),
}

EL_BASE = {
    "mc15": ROOT.TCut("n_electrons==1 && el_0_et > 30000 && el_0_id_tight && el_0_iso_FCTight"\
                      "&& (abs(el_0_eta) < 2.47 && !(abs(el_0_eta)< 1.52 && abs(el_0_eta)> 1.37 ))"),
    "mc16": ROOT.TCut("n_electrons==1 && el_0_p4->Pt() > 30 && el_0_id_tight && el_0_iso_FCTight"\
                      "&& (abs(el_0_p4->Eta()) < 2.47 && !(abs(el_0_p4->Eta()) < 1.52 && abs(el_0_p4->Eta()) > 1.37))"),
}
MU_BASE = {
#     "mc15": ROOT.TCut("n_muons==1 && mu_0_pt > 30000 && mu_0_id_tight && mu_0_iso_Gradient && abs(mu_0_eta) < 2.5"),
#     "mc16": ROOT.TCut("n_muons==1 && mu_0_p4->Pt() > 30 && mu_0_id_tight && mu_0_iso_Gradient && abs(mu_0_p4->Eta()) < 2.5"),
# Switching to mu_0_iso_FCTight_FixedRad
    "mc15": ROOT.TCut("n_muons==1 && mu_0_pt > 30000 && mu_0_id_tight && mu_0_iso_PflowTight_FixedRad && abs(mu_0_eta) < 2.5"),
    "mc16": ROOT.TCut("n_muons==1 && mu_0_p4->Pt() > 30 && mu_0_id_tight && mu_0_iso_PflowTight_FixedRad && abs(mu_0_p4->Eta()) < 2.5"),
}

LEP_BASE = {}
for mc_camp in ["mc15", "mc16"]:
    LEP_BASE[mc_camp] = ROOT.TCut("%s &&(%s || %s)"%(ONE_LEP.GetTitle(), EL_BASE[mc_camp].GetTitle(), MU_BASE[mc_camp].GetTitle()))

VETO_EL = ROOT.TCut("n_electrons==0")
VETO_MU = ROOT.TCut("n_muons==0")

## charges
SS_TAU_MU = ROOT.TCut("tau_0_q*mu_0_q==1")
SS_TAU_EL = ROOT.TCut("tau_0_q*el_0_q==1")
SS_TAU_LEP = ROOT.TCut("(tau_0_q * el_0_q)==1 ||(tau_0_q * mu_0_q)==1")

OS_TAU_MU = ROOT.TCut("tau_0_q*mu_0_q==-1")
OS_TAU_EL = ROOT.TCut("tau_0_q*el_0_q==-1")
OS_TAU_LEP = ROOT.TCut("(tau_0_q * el_0_q)==-1 ||(tau_0_q * mu_0_q)==-1")

SS_MU_EL = ROOT.TCut("mu_0_q*el_0_q==1")
OS_MU_EL = ROOT.TCut("el_0_q*mu_0_q==-1")

## masses
MASS_STR = "sqrt((tau_0_p4->E() + el_0_p4->E())**2"\
           " - (tau_0_p4->Px() + el_0_p4->Px())**2"\
           " - (tau_0_p4->Py() + el_0_p4->Py())**2"\
           " - (tau_0_p4->Pz() + el_0_p4->Pz())**2)"
TAU_EL_MASS = ROOT.TCut("(40 < {0}) && ({0} < 140)".format(MASS_STR))

# - - - - W lep
W_LEP_MT_60 = {
    "mc15": ROOT.TCut("(sqrt(2. * el_0_pt * met_et"\
                      "* (1 - cos(met_phi - el_0_phi)))"\
                      "+ sqrt(2. * mu_0_pt * met_et"\
                      "* (1 - cos(met_phi - mu_0_phi) ) ) ) > 60000"),
    
    "mc16": ROOT.TCut("(sqrt(2. * el_0_p4->Pt() * met_p4->Et()"\
                 "* (1-cos(met_p4->Phi() - el_0_p4->Phi())))"\
                 "+ sqrt(2. * mu_0_p4->Pt() * met_p4->Et()"\
                 "* (1 - cos(met_p4->Phi()-mu_0_p4->Phi() ) ) ) ) > 60")
}
W_LEP_MT_MAX160 = {
    "mc15": ROOT.TCut("(sqrt(2. * el_0_pt * met_et"\
                      "* (1 - cos(met_phi - el_0_phi)))"\
                      "+ sqrt(2. * mu_0_pt * met_et"\
                      "* (1 - cos(met_phi - mu_0_phi) ) ) ) < 160000"),
    
    "mc16": ROOT.TCut("(sqrt(2. * el_0_p4->Pt() * met_p4->Et()"\
                 "* (1-cos(met_p4->Phi() - el_0_p4->Phi())))"\
                 "+ sqrt(2. * mu_0_p4->Pt() * met_p4->Et()"\
                 "* (1 - cos(met_p4->Phi()-mu_0_p4->Phi() ) ) ) ) < 160")
}


##------------------------------------------------------------------------------------
##  - - jets
##------------------------------------------------------------------------------------
NUM_JETS1  = ROOT.TCut("n_jets > 0")
NUM_JETS2  = ROOT.TCut("n_jets > 1")
NUM_JETS3  = ROOT.TCut("n_jets > 2")
NUM_JETS4  = ROOT.TCut("n_jets > 3")

NUM_BJETS1 = ROOT.TCut("n_bjets_DL1r_FixedCutBEff_70 > 0")
NUM_BJETS2 = ROOT.TCut("n_bjets_DL1r_FixedCutBEff_70 > 1")
BVETO = ROOT.TCut("n_bjets_DL1r_FixedCutBEff_70==0")

JET_PT25 = {
    "mc15": ROOT.TCut("jet_0_pt > 25000"),
    "mc16": ROOT.TCut("jet_0_p4->Pt() > 25"),
}
BJET_PT25 = {
    "mc15": ROOT.TCut("bjet_0_pt > 25000"),
    "mc16": ROOT.TCut("bjet_0_p4->Pt() > 25"),
}

## negative MC weights 
NEGATIVE_MC_WEIGHT = ROOT.TCut("weight_mc<0")
POSITIVE_MC_WEIGHT = ROOT.TCut("weight_mc>=0")

#WIP! - - - - BDT scores for partial blinding 

# Make that PNN scores, this is a simple <128 cut on a uint8 score for all mass points
PARTIAL_UNBLIND_TAULEP = ROOT.TCut("1")
taulep_partial_unblind_cut_dict = {
  80: 52, #57, #45,
  90: 54, #60,
  100: 56, #60,
  110: 71, #73,
  120: 81, #85,
  130: 77, #80,
  140: 105, #106,
}
PARTIAL_UNBLIND_TAUJET = ROOT.TCut("1")
taujet_partial_unblind_cut_dict = {
  80: 66, #69, #45,
  90: 73, #69,
  100: 67, #65,
  110: 86, #78,
  120: 95, #88,
  130: 84, #74,
  140: 103, #98,
  150: 120, #115,
}
for mass in [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 225, 250, 275, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000]:
    cut = 128
    if mass in taulep_partial_unblind_cut_dict:
        cut = taulep_partial_unblind_cut_dict[mass]
    PARTIAL_UNBLIND_TAULEP += ROOT.TCut("80to3000_{0} < {1}".format(mass, cut))
    cut = 128
    if mass in taujet_partial_unblind_cut_dict:
        cut = taujet_partial_unblind_cut_dict[mass]
    PARTIAL_UNBLIND_TAUJET += ROOT.TCut("80to3000_{0} < {1}".format(mass, cut))

##------------------------------------------------------------------------------------
## - - base class for selection categories
##------------------------------------------------------------------------------------
class Category:
    """    
    Attributes
    ----------
    
    Examples
    --------
    #>>> presel = Category("Preselection", label="presel", channel="taujet", year="2017")
    """
    
    def __init__(self, name,
                 label="",
                 channel="taujet",
                 mc_camp="mc16",
                 tauid=TAUID_MEDIUM,
                 truth_tau=TAU_IS_TRUE,
                 ff_index=1,
                 cuts_list=[]):
        self.channel = channel
        self.name = name
        self.label = label;
        self.mc_camp = mc_camp
        self.cuts_list = cuts_list[:]
        self.tauid = tauid
        self.truth_tau = truth_tau
        self.ff_index = ff_index
        
    @property
    def cuts(self):
        """
        """
        selections = ROOT.TCut("")
        if self.cuts_list:
            for citem in self.cuts_list:
                if isinstance(citem, dict):
                    selections += citem[self.mc_camp]
                elif isinstance(citem, ROOT.TCut):
                    selections += citem
                else:
                    raise TypeError("dict or ROOT.TCut is expected but {} found".format(citem))
        if self.tauid:
            selections += self.tauid
        if self.truth_tau:
            selections += self.truth_tau
            
        return selections 
    
    def __repr__(self):
        return "CATEGORY:: name=%r, cuts=%r\t\n"%(
            self.name, self.cuts.GetTitle())


##-------------------------------------
# - - taujet channel 
##-------------------------------------
Category_TAUJET_BASE = Category(
    name="TAUJET_BASE",
    label="#tau-jet base",
    ff_index=1009,
    cuts_list = [
        CLEAN_EVT,
    ],
)

Category_TAUJET_PRESEL = Category(
    name="TAUJET_PRESEL",
    label="#tau-jet presel",
    ff_index=1000,
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        MET150, 
        NUM_JETS3,
        # MT50,
        # NUM_BJETS1,    
        ],
)

Category_SR_TAUJET = Category(
    name="SR_TAUJET",
    label="#tau-jet SR",
    ff_index=1001,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        JET_PT25,
        MET150,
        MT50,
        NUM_BJETS1,
    ],
)

Category_SR_TAUJET_PARTIAL = Category(
    name="SR_TAUJET_PARTIAL",
    label="#tau-jet partially unblinded SR",
    ff_index=1001,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        JET_PT25,
        MET150,
        MT50,
        NUM_BJETS1,
        PARTIAL_UNBLIND_TAUJET,
    ],
)

Category_TTBAR = Category(
    name="TTBAR",
    label="t#bar{t} CR",
    ff_index=1002,
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        NUM_BJETS2,     
        MET150,
        MT_MAX100,
        ],
)

Category_WJETS = Category(
    name="WJETS",
    label="W/Z jets CR",
    ff_index=1003,
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        JET_PT25,
        BVETO,
        MET150,
        MT_MAX100],
)

Category_BVETO = Category(
    name="BVETO",
    label="b-veto CR",
    ff_index=1004,
    cuts_list= [
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        JET_PT25,
        BVETO,
        MET150,
        MT50,],
)

Category_BVETO_MT100 = Category(
    name="BVETO_MT100",
    label="b-veto CR MT100",
    ff_index=1006,
    cuts_list= [
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        JET_PT25,
        BVETO,
        MET150,
        MT100,
    ],
)


##------------------------------------------
# - - taulep channel
##------------------------------------------

Category_TAULEP_BASE = Category(
    name="TAULEP_BASE",
    label="#tau-lep base",
    ff_index=2020,
    cuts_list = [
        CLEAN_EVT,
    ],
)

Category_TAULEP_PRESEL = Category(
    name="TAULEP_PRESEL",
    label="#tau-lep presel",
    ff_index=2000,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_BASE,
        OS_TAU_LEP,
        NUM_JETS1,
        JET_PT25,
        MET50,
    ],
)

Category_SR_TAULEP = Category(
    name="SR_TAULEP",
    label="#tau-lep SR",
    ff_index=2001,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_BASE,
        OS_TAU_LEP,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,  
        MET50,
    ],
)

Category_SR_TAUEL = Category(
    name="SR_TAUEL",
    label="#tau-e SR",
    ff_index=2002,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        EL_BASE,
        OS_TAU_EL,
        VETO_MU,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,     
        MET50,
    ],
)

Category_SR_TAUMU = Category(
    name="SR_TAUMU",
    label="#tau-#mu SR",
    ff_index=2003,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        MU_BASE,
        OS_TAU_MU,
        VETO_EL,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,
        MET50,
    ],
)

Category_SR_TAULEP_PARTIAL = Category(
    name="SR_TAULEP_PARTIAL",
    label="#tau-lep partially unblinded SR",
    ff_index=2001,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_BASE,
        OS_TAU_LEP,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,  
        MET50,
        PARTIAL_UNBLIND_TAULEP,
    ],
)

Category_SR_TAUEL_PARTIAL = Category(
    name="SR_TAUEL_PARTIAL",
    label="#tau-e partially unblinded SR",
    ff_index=2002,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        EL_BASE,
        OS_TAU_EL,
        VETO_MU,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,
        MET50,
        PARTIAL_UNBLIND_TAULEP,
    ],
)

Category_SR_TAUMU_PARTIAL = Category(
    name="SR_TAUMU_PARTIAL",
    label="#tau-#mu partially unblinded SR",
    ff_index=2003,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        MU_BASE,
        OS_TAU_MU,
        VETO_EL,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,
        MET50,
        PARTIAL_UNBLIND_TAULEP,
    ],
)

Category_TAUEL_BVETO = Category(
    name="TAUEL_BVETO",
    label="#tau-e b-veto CR",
    ff_index=2004,
    cuts_list = [
        CLEAN_EVT,
        EL_BASE,
        OS_TAU_EL,
        TAU_BASE,
        VETO_MU,
        NUM_JETS1,
        JET_PT25,
        BVETO,
        MET50,
    ],
)

Category_TAUMU_BVETO = Category(
    name="TAUMU_BVETO",
    label="#tau-#mu b-veto CR",
    ff_index=2005,
    cuts_list = [
        CLEAN_EVT,
        MU_BASE,
        OS_TAU_MU,
        TAU_BASE,
        VETO_EL,
        NUM_JETS1,
        JET_PT25,
        BVETO,
        MET50,
    ],
)

Category_DILEP_BVETO = Category(
    name="DILEP_BVETO",
    label="dilep-bveto CR",
    ff_index=2006,
    tauid=None,
    truth_tau=None,
    cuts_list = [
        CLEAN_EVT,
        EL_BASE,
        MU_BASE,
        OS_MU_EL,
        VETO_TAU,
        NUM_JETS1,
        JET_PT25,
        BVETO,
        MET50,
    ],
)

Category_DILEP_BTAG = Category(
    name="DILEP_BTAG",
    label="dilep-btag CR",
    ff_index=2006,
    tauid=None,
    truth_tau=None,
    cuts_list = [
        CLEAN_EVT,
        EL_BASE,
        MU_BASE,
        OS_MU_EL,
        VETO_TAU,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,        
        MET50,
    ],
)

Category_SS_TAUEL = Category(
    name="SS_TAUEL",
    label="same sign #tau-e CR",
    ff_index=2007,
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        EL_BASE,
        SS_TAU_EL,
        VETO_MU,
        NUM_JETS1,
        JET_PT25,
        MET50,
    ],
)

Category_SS_TAUMU = Category(
    name="SS_TAUMU",
    label="same sign #tau-#mu CR",
    ff_index=2008,
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        MU_BASE,
        SS_TAU_MU,
        VETO_EL,
        NUM_JETS1,
        JET_PT25,
        MET50,
    ],
)

Category_ZEE = Category(
    name="ZEE",
    label="Zee CR",
    ff_index=2009,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        EL_BASE,
        VETO_MU,
        OS_TAU_EL,
        NUM_JETS1,
        JET_PT25,
        BVETO,
        TAU_EL_MASS,
        MET50,
    ],
)

Category_TTBAR_TAULEP = Category(
    name="TTBAR_TAULEP",
    label="#tau-lep ttbar CR",
    ff_index=2021,
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_BASE,
        OS_TAU_LEP,
        NUM_JETS2,
        JET_PT25,
        NUM_BJETS2,
        MT_MAX70,
        MET80,
    ],
)

##------------------------------------------------------------------------------------
## - - Fake Factors CR
##------------------------------------------------------------------------------------
FF_CR_MULTIJET = Category(
    "FF_CR_MULTIJET",
    label="ff multijet CR",
    ff_index=9001,
    cuts_list=[
        CLEAN_EVT,
        TAU_PT30,
        TAU_EL_OLR_PASS,
        TAU_TRACKS,
        NUM_JETS3,
        LEP_VETO,
        BVETO,
        MET_MAX80,
        MT50,],
)

FF_CR_WJETS = Category(
    "FF_CR_WJETS", label="ff Wjets CR",
    ff_index=9002,
    cuts_list=[
        CLEAN_EVT,
        TAU_EL_OLR_PASS,
        
        ROOT.TCut("n_electrons==1"),
        ROOT.TCut("el_0_p4->Pt() > 26"),
        # - - trigger matched electron
        ROOT.TCut("el_0_trig_trigger_matched==1"
            # "(el_0_trig_HLT_e24_lhmedium_L1EM20VH==1 && run_number <= 288000)" #<! 2015
            # "|| (el_0_trig_HLT_e26_lhtight_nod0_ivarloose==1 && run_number > 288000)" #<! 2016
            #"||(el_0_trig_trigger_matched==1 && HLT_e26_lhtight_nod0_ivarloose==1 && run_number > 288000)"
        ),
        EL_BASE,
        TAU_BASE,
        # ROOT.TCut("n_taus==1"), 
        BVETO,
        W_LEP_MT_60,
        W_LEP_MT_MAX160,
    ],
)

# - - - - collective Fake Factors CR 
FF_CR_REGIONS = {}
FF_CR_REGIONS["taujet"] = [FF_CR_MULTIJET]
FF_CR_REGIONS["taulep"] = [FF_CR_WJETS]


## - - - - fake tau origin
FAKE_TAU_SOURCE = {
    "electron": TAU_IS_EL,
    "lquark": TAU_IS_LIGHT_QUARK,
    "cquark": TAU_IS_B_QUARK,
    "bquark": TAU_IS_C_QUARK,
    "gluon": TAU_IS_GLUON,
    "other": TAU_IS_OTHER,
    "tau": TAU_IS_TRUE,
}


##------------------------------------------------------------------------------------
## - - Classifier training selections
##------------------------------------------------------------------------------------
CLF_TJ = Category("CLF_TAUJET",
        label="clf #tau-jet",
        ff_index=1005,
        #   truth_tau=None,
        cuts_list = [
            CLEAN_EVT,
            TAU_BASE,
            LEP_VETO,
            TAU_PT40,
            NUM_JETS3,
            JET_PT25,
            MET100,
            MT50,
            NUM_BJETS1,

    ])

CLF_TL = Category("CLF_TAULEP",
        label="clf #tau-lep",
        ff_index=2010,  
    #   truth_tau=None,
        cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        LEP_BASE,
        OS_TAU_LEP,
        NUM_JETS1,
        JET_PT25,
        NUM_BJETS1,  
        MET50,
        ])

CLASSIFIER_CATEGORIES = {
    "taujet": CLF_TJ,
    "taulep": CLF_TL,
}



##------------------------------------------------------------------------------------
## - - MET trigger efficency control regions 
##------------------------------------------------------------------------------------

MET_TRIGG_EFF_CUTS_BASE = [
    ROOT.TCut("n_taus==1"),
    TAUID_LOOSE,
    TAU_EL_OLR_PASS,
    # default (electrons)
    ROOT.TCut("n_electrons==1&&n_muons==0"),
    ROOT.TCut("tau_0_q*el_0_q==-1"),
    ROOT.TCut("el_0_p4->Pt() > 26"),
    ROOT.TCut( "el_0_trig_trigger_matched==1"),
    ROOT.TCut("el_0_id_loose==1"),
    # optional (electrons OR muons)
    #    ROOT.TCut("n_electrons+n_muons==1"),
    #    ROOT.TCut("(n_electrons==1 && el_0_p4->Pt() > 26 && el_0_id_loose && el_0_trig_trigger_matched==1 && tau_0_q*el_0_q==-1)"\
    #              "|| (n_muons==1 && mu_0_p4->Pt() > 30 && mu_0_id_loose && mu_0_trig_trigger_matched==1 && tau_0_q*mu_0_q==-1)"),
    
    ROOT.TCut("n_jets>1"),
    NUM_BJETS1,
    ROOT.TCut("jet_0_p4->Pt() > 25 && jet_1_p4->Pt() > 25"),
    
    # - - only for the bkg modelling in this region (not applied for calculating trigger efficiency).
    #ROOT.TCut("met_p4->Et() > 100"),
]


## - - - - systematic variations from tau/el ID and number of jets.

MET_TRIG_EFF_CR_NOM = Category(
    "MET_TRIG_EFF_CR_NOM",
    label="E^{T}_{miss} trig eff CR (nom)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE,
)

MET_TRIG_EFF_CR_TAUID_MED = Category(
    "MET_TRIG_EFF_CR_TAUID_MED",
    label="E^{T}_{miss} trig eff CR (MED #tau)",
    ff_index=2011,
    tauid=TAUID_MEDIUM,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [TAUID_MEDIUM],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [TAUID_MEDIUM],
)

MET_TRIG_EFF_CR_TAUID_TIGHT = Category(
    "MET_TRIG_EFF_CR_TAUID_TIGHT",
    label="E^{T}_{miss} trig eff CR (TIGHT #tau)",
    ff_index=2011,
    tauid=TAUID_TIGHT,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [TAUID_TIGHT],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [TAUID_TIGHT],
)

MET_TRIG_EFF_CR_ELID_MED = Category(
    "MET_TRIG_EFF_CR_ELID_MED",
    label="E^{T}_{miss} trig eff CR (MED e)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [ROOT.TCut("n_electrons==0 || el_0_id_medium==1")],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("n_electrons==0 || el_0_id_medium==1")],
)

MET_TRIG_EFF_CR_ELID_TIGHT = Category(
    "MET_TRIG_EFF_CR_ELID_TIGHT",
    label="E^{T}_{miss} trig eff CR (TIGHT e)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [ROOT.TCut("n_electrons==0 || el_0_id_tight==1")],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("n_electrons==0 || el_0_id_tight==1")],
)

MET_TRIG_EFF_CR_NJETS3 = Category(
    "MET_TRIG_EFF_CR_NJETS3",
    label="E^{T}_{miss} trig eff CR (3 jets)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    #cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [ROOT.TCut("n_jets > 2")],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("n_jets > 2")],
)

MET_TRIG_EFF_CR_NBJET1 = Category(
    "MET_TRIG_EFF_CR_NBJET1",
    label="E^{T}_{miss} trig eff CR (1 b-jet)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,                                                                                                                      
    cuts_list=MET_TRIGG_EFF_CUTS_BASE,
)

MET_TRIG_EFF_CR_NBJET2 = Category(
    "MET_TRIG_EFF_CR_NBJET1",
    label="E^{T}_{miss} trig eff CR (2 b-jets)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2],
)

MET_TRIG_EFF_CR_MUID_MED = Category(
    "MET_TRIG_EFF_CR_MUID_MED",
    label="E^{T}_{miss} trig eff CR (MED mu)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [ROOT.TCut("n_muons==0 || mu_0_id_medium==1")],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("n_muons==0 || mu_0_id_medium==1")],
)

MET_TRIG_EFF_CR_MUID_TIGHT = Category(
    "MET_TRIG_EFF_CR_MUID_TIGHT",
    label="E^{T}_{miss} trig eff CR (TIGHT mu)",
    ff_index=2011,
    tauid=TAUID_LOOSE,
    # truth_tau=None,
    # cuts_list=MET_TRIGG_EFF_CUTS_BASE + [NUM_BJETS2] + [ROOT.TCut("n_muons==0 || mu_0_id_tight==1")],
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("n_muons==0 || mu_0_id_tight==1")],
)

## - - - -  PLEASE KEEP THE ORDER (it will be used to assign an index for each region in cxx macros)
MET_TRIG_EFF_CRs = [
    MET_TRIG_EFF_CR_NOM,
    MET_TRIG_EFF_CR_TAUID_MED,
    MET_TRIG_EFF_CR_TAUID_TIGHT,
    MET_TRIG_EFF_CR_ELID_MED,
    MET_TRIG_EFF_CR_ELID_TIGHT,
    MET_TRIG_EFF_CR_NJETS3,
#    MET_TRIG_EFF_CR_NBJET1,
    MET_TRIG_EFF_CR_NBJET2,
    #    MET_TRIG_EFF_CR_MUID_MED,
    #    MET_TRIG_EFF_CR_MUID_TIGHT
]


##------------------------------------------------------------------------------------
## - - cutflow selections 
##------------------------------------------------------------------------------------

CUTFLOW = {
    "taujet": OrderedDict(
        [
            # ("cleanEvent",  CLEAN_EVT),
            ("trigger", ROOT.TCut("1.>0")), #<! trigger is applied globally (just a place holder here)

            ("tauBase", TAU_BASE["mc16"] + TAU_PT40["mc16"]),
            ("tauID", TAUID_MEDIUM),

            ("lepVeto", LEP_VETO),

            # ("3jets", NUM_JETS3),
            # ("jetPt25", JET_PT25),

            ("1bjets", NUM_BJETS1),

            ("MET150", MET150),    

            ("mT50", MT50),
        ]),

    "taulep":
    OrderedDict(
        [
            ("trigger", {"mc16": ROOT.TCut("1.>0"), "mc15": ROOT.TCut("1.>0")}), #<! trigger is applied globally (just a place holder here)
            # ("cleanEvent",  CLEAN_EVT),

            ("tauBase", TAU_BASE["mc16"]),
            ("tauID", TAUID_MEDIUM),
            # ("tauPt30", TAU_PT30["mc16"]+TAU_BASE["mc16"]),

            # ("lepBase", LEP_BASE["mc16"]),
            # ("OS", OS_TAU_LEP),


            # ("elBase", EL_BASE["mc16"]),
            # ("OS", OS_TAU_EL),


            ("muBase", MU_BASE["mc16"]),
            ("OS", OS_TAU_MU),


            # ("1jets", NUM_JETS1),
            # ("jetPt25", JET_PT25),
            
            ("MET50", MET50),

            ("1bjets", NUM_BJETS1),
            # ("bjetPt25", BJET_PT25),

        ]),
}


##--------------------------------------------------------------
# - - analysis selection regions (PLEASE KEEP THE ORDER)
##--------------------------------------------------------------
CATEGORIES = OrderedDict()
CATEGORIES["taujet"] = [
    Category_SR_TAUJET,
    Category_TTBAR,
    Category_BVETO,
    Category_WJETS,
    Category_TAUJET_PRESEL,
    Category_BVETO_MT100,
    # Category_SR_TAUJET_PARTIAL,
]

CATEGORIES["taulep"] = [
    Category_SR_TAULEP,
    Category_SR_TAUEL,
    Category_SR_TAUMU,
    Category_TAUEL_BVETO,
    Category_TAUMU_BVETO,
    Category_SS_TAUEL,
    Category_SS_TAUMU,
    Category_DILEP_BTAG,
    Category_DILEP_BVETO,
    Category_ZEE,
    Category_TAULEP_PRESEL,
    Category_TTBAR_TAULEP,
    MET_TRIG_EFF_CR_NOM,
    # Category_SR_TAUEL_PARTIAL,
    # Category_SR_TAUMU_PARTIAL,
    # Category_SR_TAULEP_PARTIAL,
]
