# -*- coding: utf-8 -*-

from math import pi
from collections import OrderedDict

import ROOT
from ROOT import TCut

from db.decorators import cached_property
from . import log, MC_CAMPAIGN
from .trigger import get_trigger

"""
This module provides all selections needed for the analysis.
PLEASE NOTE THAT THE UNIT IS CHANGED FROM MeV to GeV as of version 18v04 of the ntuples.
"""

##------------------------------------------------------------------------------------
##  - - clean events 
##------------------------------------------------------------------------------------

# - - - - - - - - event 
CLEAN_EVT = {
    "mc15": TCut("(event_clean==1) && (n_vx>=1) && (bsm_tj_dirty_jet==0)"),
    "mc16": TCut("n_vx > 0"),
}

##------------------------------------------------------------------------------------
##  - - mT and MET
##------------------------------------------------------------------------------------
MET50 = {
    "mc15": TCut("met_et>50000"),
    "mc16": TCut("met_p4->Et() > 50"),
}
MET100 = {
    "mc15": TCut("met_et>100000"),
    "mc16": TCut("met_p4->Et() > 100"),
}
    
MET150 = {
    "mc15": TCut("met_et > 150000"),
    "mc16": TCut("met_p4->Et() > 150"),
}

MET_MAX150 = {
    "mc15": TCut("met_et < 150000"),
    "mc16": TCut("met_p4->Et() < 150"),
}
MET_MAX80 = {
    "mc15": TCut("met_et < 80000"),
    "mc16": TCut("met_p4->Et() < 80"),
}

MT50 = {
    "mc15": TCut("tau_0_met_mt > 50000"),
    "mc16": TCut("tau_0_met_mt > 50")
}
MT_MAX100 = {
    "mc15": TCut("tau_0_met_mt < 100000"),
    "mc16": TCut("tau_0_met_mt < 100")
}

 
##------------------------------------------------------------------------------------
##  - - tau
##------------------------------------------------------------------------------------
TAU_Q = TCut("abs(tau_0_q)==1")
TAU_DECAY_MODE = TCut("tau_0_decay_mode==0")

TAUID_LOOSE = TCut("tau_0_jet_bdt_loose==1")
TAUID_MEDIUM = TCut("tau_0_jet_bdt_medium==1")
TAUID_TIGHT = TCut("tau_0_jet_bdt_tight==1")

TAU_1_TRACK = {
    "mc15": TCut("tau_0_n_tracks==1"),
    "mc16": TCut("tau_0_n_charged_tracks==1"),
}
TAU_3_TRACK = {
    "mc15": TCut("tau_0_n_tracks==3"),
    "mc16": TCut("tau_0_n_charged_tracks==3"),
}
TAU_TRACKS = {
    "mc15": TCut("tau_0_n_tracks==1 || tau_0_n_tracks==3"),
    "mc16": TCut("tau_0_n_charged_tracks==1 || tau_0_n_charged_tracks==3"),
}

TAU_PT30 = {
    "mc15": TCut("tau_0_pt > 30000"),
    "mc16": TCut("tau_0_p4->Pt() > 30") ,
}
TAU_PT40 = {
    "mc15": TCut("tau_0_pt > 40000"),
    "mc16": TCut("tau_0_p4->Pt() > 40") ,
}
TAU_ETA = {
    "mc15": TCut("abs(tau_0_eta)<2.3 && !(abs(tau_0_eta)< 1.52 && abs(tau_0_eta)> 1.37)"),
    "mc16": TCut("abs(tau_0_p4->Eta())<2.3 && !(abs(tau_0_p4->Eta())< 1.52 && abs(tau_0_p4->Eta())> 1.37)") ,
}

## tau truth lable
TAU_IS_TRUE = TCut("true_tau_0_isTau")
TAU_IS_LEP = TCut("true_tau_0_isMuon || true_tau_0_isEle")
TAU_IS_EL = TCut("true_tau_0_isEle")
TAU_IS_EL_OR_HAD = TCut("true_tau_0_isTau || true_tau_0_isEle")
TAU_IS_LEP_OR_HAD = TCut("true_tau_0_isTau || true_tau_0_isEle || true_tau_0_isMuon")

## tau jet parton label 
TAU_IS_LIGHT_QUARK = TCut("true_tau_0_jet_pdgId>0 && true_tau_0_jet_pdgId <4")
TAU_IS_C_QUARK = TCut("true_tau_0_jet_pdgId==4")
TAU_IS_B_QUARK = TCut("true_tau_0_jet_pdgId==5")
TAU_IS_GLUON = TCut("true_tau_0_jet_pdgId==21")
TAU_IS_OTHER = TCut("!(%s || %s || %s ||%s ||%s || %s)"%(
    TAU_IS_EL.GetTitle(), TAU_IS_LIGHT_QUARK, TAU_IS_C_QUARK, TAU_IS_B_QUARK, TAU_IS_GLUON, TAU_IS_TRUE))

## QCD fake tau
TAU_IS_FAKE = TCut("!(%s || %s)"%(TAU_IS_TRUE, TAU_IS_LEP))

ANTI_TAU = {
    "mc15": TCut("tau_0_jet_bdt_score_sig > 0.02 && tau_0_jet_bdt_loose==0"),
    "mc16": TCut("tau_0_jet_bdt_score_trans > 0.02 && tau_0_jet_bdt_loose==0"),
}

VETO_TAU = ROOT.TCut("n_taus==0")
TAU_EL_OLR_PASS = {
    "mc15": TCut("tau_0_ele_olr_pass==1"),
    "mc16": TCut("tau_0_ele_olr_pass==1"),
}

TAU_BASE = {}
for mcc in ["mc15", "mc16"]:
    TAU_BASE[mcc] = TAU_PT30[mcc] + TAU_ETA[mcc] + TAU_TRACKS[mcc] + TAU_EL_OLR_PASS[mcc]
    
##------------------------------------------------------------------------------------
##  - - lepton
##------------------------------------------------------------------------------------
LEP_VETO = {
    "mc15": TCut("(n_electrons + n_muons)==0"),
    "mc16": TCut("(n_electrons + n_muons)==0"),
}
ONE_LEP = TCut("(n_electrons + n_muons)==1")

LEP_PT30 = {
    "mc15": TCut("(mu_0_pt + el_0_pt)> 30000"),
    "mc16": TCut("(mu_0_p4->Pt() + el_0_p4->Pt()) > 30") ,
}

# - - - - lep ID
ELID_TIGHT = {
    "mc15":TCut("n_electrons && el_0_id_tight"),
    "mc16":TCut("n_electrons && el_0_id_tight"),
}
MUID_TIGHT = {
    "mc15":TCut("n_muons && mu_0_id_tight"),
    "mc16":TCut("n_muons && mu_0_id_tight"),
}

EL_BASE = {
    "mc15": ROOT.TCut("n_electrons==1 && el_0_et > 30000 && el_0_id_tight && el_0_iso_FixedCutTight"\
                      "&& (abs(el_0_eta) < 2.47 && !(abs(el_0_eta)< 1.52 && abs(el_0_eta)> 1.37 ))"),
    "mc16": ROOT.TCut("n_electrons==1 && el_0_p4->Pt() > 30 && el_0_id_tight && el_0_iso_FixedCutTight"\
                      "&& (abs(el_0_p4->Eta()) < 2.47 && !(abs(el_0_p4->Eta()) < 1.52 && abs(el_0_p4->Eta()) > 1.37))"),
}
MU_BASE = {
    "mc15": ROOT.TCut("n_muons==1 && mu_0_pt > 30000 && mu_0_id_tight && mu_0_iso_FixedCutTight && abs(mu_0_eta) < 2.5"),
    "mc16": ROOT.TCut("n_muons==1 && mu_0_p4->Pt() > 30 && mu_0_id_tight && mu_0_iso_FixedCutTight && abs(mu_0_p4->Eta()) < 2.5"),
}

LEP_BASE = {}
for mc_camp in ["mc15", "mc16"]:
    LEP_BASE[mc_camp] = TCut("%s &&(%s || %s)"%(ONE_LEP, EL_BASE[mc_camp], MU_BASE[mc_camp]))

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
    "mc15": TCut("(sqrt(2. * el_0_pt * met_et"\
                      "* (1 - cos(met_phi - el_0_phi)))"\
                      "+ sqrt(2. * mu_0_pt * met_et"\
                      "* (1 - cos(met_phi - mu_0_phi) ) ) ) > 60000"),
    
    "mc16": TCut("(sqrt(2. * el_0_p4->Pt() * met_p4->Et()"\
                 "* (1-cos(met_p4->Phi() - el_0_p4->Phi())))"\
                 "+ sqrt(2. * mu_0_p4->Pt() * met_p4->Et()"\
                 "* (1 - cos(met_p4->Phi()-mu_0_p4->Phi() ) ) ) ) > 60")
}
W_LEP_MT_MAX160 = {
    "mc15": TCut("(sqrt(2. * el_0_pt * met_et"\
                      "* (1 - cos(met_phi - el_0_phi)))"\
                      "+ sqrt(2. * mu_0_pt * met_et"\
                      "* (1 - cos(met_phi - mu_0_phi) ) ) ) < 160000"),
    
    "mc16": TCut("(sqrt(2. * el_0_p4->Pt() * met_p4->Et()"\
                 "* (1-cos(met_p4->Phi() - el_0_p4->Phi())))"\
                 "+ sqrt(2. * mu_0_p4->Pt() * met_p4->Et()"\
                 "* (1 - cos(met_p4->Phi()-mu_0_p4->Phi() ) ) ) ) < 160")
}


##------------------------------------------------------------------------------------
##  - - jets
##------------------------------------------------------------------------------------
NUM_JETS1  = TCut("n_jets > 0")
NUM_JETS3  = TCut("n_jets > 2")
NUM_JETS4  = TCut("n_jets > 3")

NUM_BJETS1 = TCut("n_bjets > 0")
NUM_BJETS2 = TCut("n_bjets > 1")
BVETO = TCut("n_bjets==0")

JET_PT25 = {
    "mc15": TCut("jet_0_pt > 25000"),
    "mc16": TCut("jet_0_p4->Pt() > 25"),
}
BJET_PT25 = {
    "mc15": TCut("bjet_0_pt > 25000"),
    "mc16": TCut("bjet_0_p4->Pt() > 25"),
}

#WIP! - - - - BDT scores for partial blinding 


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
                 cuts_list=[]):
        
        self.channel = channel
        self.name = name
        self.label = label;
        self.mc_camp = mc_camp
        self.cuts_list = cuts_list[:]
        self.tauid = tauid
        self.truth_tau = truth_tau
        
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
Category_TAUJET_PRESEL = Category(
    name="TAUJET_PRESEL",
    label="#tau-jet presel",
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        MET100, 
        NUM_JETS3,    
        MT50],
)

Category_SR_TAUJET = Category(
    name="SR_TAUJET",
    label="#tau-jet SR",
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

Category_TTBAR = Category(
    name="TTBAR",
    label="t#bar{t} CR",
    cuts_list=[
        CLEAN_EVT,
        TAU_BASE,
        LEP_VETO,
        TAU_PT40,
        NUM_JETS3,
        NUM_BJETS2,     
        MET150,
        MT_MAX100],
)

Category_WJETS = Category(
    name="WJETS",
    label="W/Z jets CR",
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


##------------------------------------------
# - - taulep channel
##------------------------------------------
Category_TAULEP_PRESEL = Category(
    name="TAULEP_PRESEL",
    label="#tau-lep presel",
    cuts_list = [
        CLEAN_EVT,
        TAU_BASE,
        LEP_BASE,
        NUM_JETS1,
        JET_PT25
    ],
)

Category_SR_TAULEP = Category(
    name="SR_TAULEP",
    label="#tau-lep SR",
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

Category_TAUEL_BVETO = Category(
    name="TAUEL_BVETO",
    label="#tau-lep b-veto CR",
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

Category_DILEP_BTAG = Category(
    name="DILEP_BTAG",
    label="dilep-btag CR",
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
    label="same sign #tau-e",
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
    label="same sign #tau-#mu",
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
    label="Z#rightarrow e e",
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
    ],
)

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
    Category_ZEE,
    Category_TAULEP_PRESEL,
]

    
##------------------------------------------------------------------------------------
## - - Fake Factors CR
##------------------------------------------------------------------------------------
FF_CR_MULTIJET = Category(
    "FF_CR_MULTIJET",
    label="ff multijet CR",
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
    cuts_list=[
        CLEAN_EVT,
        TAU_EL_OLR_PASS,
        
        ROOT.TCut("n_electrons==1"),
        ROOT.TCut("el_0_p4->Pt() > 26"),
        # - - trigger matched electron
        ROOT.TCut( 
            "(el_0_trig_HLT_e24_lhmedium_L1EM20VH==1 && run_number <= 288000)" #<! 2015
            "|| (el_0_trig_HLT_e26_lhtight_nod0_ivarloose==1 && run_number > 288000)" #<! 2016
            #"||(el_0_trig_trigger_matched==1 && HLT_e26_lhtight_nod0_ivarloose==1 && run_number > 288000)"
        ),
        #EL_BASE,
        #TAU_BASE,
        ROOT.TCut("n_taus==1"), 
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
                  cuts_list=[
                      CLEAN_EVT,
                      TAU_BASE,
                      LEP_VETO,
                      NUM_JETS3,
                      NUM_BJETS1,
                      MET100,
                  ])

CLF_TL = Category("CLF_TAULEP",
                  label="clf #tau-lep",
                  cuts_list=[
                      CLEAN_EVT,
                      TAU_BASE,
                      LEP_BASE,
                      NUM_JETS1,
                      NUM_BJETS1,
                      MET50,
                  ])

CLASSIFIER_CATEGORIES = {
    "taujet": CLF_TJ,
    "taulep":CLF_TL,
}



##------------------------------------------------------------------------------------
## - - MET trigger efficency control regions 
##------------------------------------------------------------------------------------
MET_TRIGG_EFF_CUTS_BASE = [
    ROOT.TCut("n_taus==1"),
    ROOT.TCut("n_electrons==1"),
    ROOT.TCut("el_0_p4->Pt() > 26"),
    # - - trigger matched electron
    ROOT.TCut( 
        "(el_0_trig_HLT_e24_lhmedium_L1EM20VH==1 && run_number <= 288000)" #<! 2015
        "|| (el_0_trig_HLT_e26_lhtight_nod0_ivarloose==1 && run_number > 288000)" #<! 2016
        #"||(el_0_trig_trigger_matched==1 && HLT_e26_lhtight_nod0_ivarloose==1 && run_number > 288000)"
    ),
    
    ROOT.TCut("n_jets>1 && n_bjets>0"),
    ROOT.TCut("jet_0_p4->Pt() > 25 && jet_1_p4->Pt() > 25"),
    
    # - - only for the bkg modelling in this region (not applied for calcualting trigger efficency).
    #ROOT.TCut("met_p4->Et() > 100"),
]

## - - - - systematic variations from tau/el ID and number of jets.

MET_TRIG_EFF_CR_NOM = Category(
    "MET_TRIG_EFF_CR_NOM",
    label="E^{T}_{miss} trig eff CR (nom)",
    tauid=TAUID_LOOSE,
    truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("el_0_id_loose==1")],
)

MET_TRIG_EFF_CR_TAUID_MED = Category(
    "MET_TRIG_EFF_CR_TAUID_MED",
    label="E^{T}_{miss} trig eff CR (MED #tau)",
    tauid=TAUID_MEDIUM,
    truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("el_0_id_loose==1")],
)

MET_TRIG_EFF_CR_TAUID_TIGHT = Category(
    "MET_TRIG_EFF_CR_TAUID_TIGHT",
    label="E^{T}_{miss} trig eff CR (TIGHT #tau)",
    tauid=TAUID_TIGHT,
    truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("el_0_id_loose==1")],
)

MET_TRIG_EFF_CR_ELID_MED = Category(
    "MET_TRIG_EFF_CR_ELID_MED",
    label="E^{T}_{miss} trig eff CR (MED e)",
    tauid=TAUID_LOOSE,
    truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("el_0_id_medium==1")],
)

MET_TRIG_EFF_CR_ELID_TIGHT = Category(
    "MET_TRIG_EFF_CR_ELID_TIGHT",
    label="E^{T}_{miss} trig eff CR (TIGHT e)",
    tauid=TAUID_LOOSE,
    truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("el_0_id_tight==1")],
)

MET_TRIG_EFF_CR_NJETS3 = Category(
    "MET_TRIG_EFF_CR_NJETS3",
    label="E^{T}_{miss} trig eff CR (3 jets)",
    tauid=TAUID_LOOSE,
    truth_tau=None,
    cuts_list=MET_TRIGG_EFF_CUTS_BASE + [ROOT.TCut("el_0_id_loose==1"), ROOT.TCut("n_jets > 2")],
)

## - - - -  PLEASE KEEP THE ORDER (it will be used to assign an index for each region in cxx macros)
MET_TRIG_EFF_CRs = [
    MET_TRIG_EFF_CR_NOM,
    MET_TRIG_EFF_CR_TAUID_MED,
    MET_TRIG_EFF_CR_TAUID_TIGHT,
    MET_TRIG_EFF_CR_ELID_MED,
    MET_TRIG_EFF_CR_ELID_TIGHT,
    MET_TRIG_EFF_CR_NJETS3
]


##------------------------------------------------------------------------------------
## - - cutflow selections 
##------------------------------------------------------------------------------------
CUTFLOW = {
    "taujet": OrderedDict(
        [
            ("cleanEvent",  CLEAN_EVT),
            ("trigger", {"mc16": ROOT.TCut("1>0"), "mc15": ROOT.TCut("1>0")}), #<! trigger is applied globally (just a place holder here)
            ("ElOLR", TAU_EL_OLR_PASS),
            ("tauPt40", TAU_PT40),
            ("tauID", TAUID_MEDIUM),
            ("lepVeto", LEP_VETO),
            ("3jets", NUM_JETS3),
            ("jetPt25", JET_PT25),
            ("1bjets", NUM_BJETS1),
            ("MET150", MET150),
            ("mT50", MT50),
        ]),
    "taulep":
    OrderedDict(
        [("cleanEvent",  CLEAN_EVT),
         ("trigger", {"mc16": ROOT.TCut("1>0"), "mc15": ROOT.TCut("1>0")}), #<! trigger is applied globally (just a place holder here)
         ("tauPt40", TAU_PT40),
         ("tauID", TAUID_MEDIUM),
         ("eBase", LEP_BASE),
         ("3jets", NUM_JETS3),
         ("jetPt25", JET_PT25),
         ("1bjets", NUM_BJETS1),
         ("MET50", MET150),
         ("mT50", MT50),
        ]),
}
