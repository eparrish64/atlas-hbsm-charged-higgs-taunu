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
"""

##------------------------------------------------------------------------------------
##  - - clean events 
##------------------------------------------------------------------------------------

# - - - - - - - - event 
CLEAN_EVT = {
    "mc15": TCut("(event_clean==1) && (n_vx>=1) && (bsm_tj_dirty_jet==0)"),
    "mc16": TCut("(n_vx>=1)")
}

##------------------------------------------------------------------------------------
##  - - mT and MET
##------------------------------------------------------------------------------------
MET50 = {
    "mc15": TCut("met_et>50000"),
    "mc16": TCut("met_p4->Et() > 50000"),
}
MET100 = {
    "mc15": TCut("met_et>100000"),
    "mc16": TCut("met_p4->Et() > 100000"),
}
    
MET150 = {
    "mc15": TCut("met_et > 150000"),
    "mc16": TCut("met_p4->Et() > 150000"),
}

MET_MAX150 = {
    "mc15": TCut("met_et < 150000"),
    "mc16": TCut("met_p4->Et() < 150000"),
}
MET_MAX80 = {
    "mc15": TCut("met_et < 80000"),
    "mc16": TCut("met_p4->Et() < 80000"),
}

MT50 = {
    "mc15": TCut("tau_0_met_mt > 50000"),
    "mc16": TCut("tau_0_met_mt > 50000")
}
MT_MAX100 = {
    "mc15": TCut("tau_0_met_mt < 100000"),
    "mc16": TCut("tau_0_met_mt < 100000")
}

 
##------------------------------------------------------------------------------------
##  - - tau
##------------------------------------------------------------------------------------
TAU_Q = {
    "mc15": TCut("abs(tau_0_q)==1"),
    "mc16": TCut("abs(tau_0_q)==1"),
}
TAU_DECAY_MODE = {
    "mc15": TCut("tau_0_decay_mode==0"),
    "mc16": TCut("tau_0_decay_mode==0"),
}
TAUID_LOOSE = {
    "mc15": TCut("tau_0_jet_bdt_loose==1 && tau_0_jet_bdt_score_sig>0.02"),
    "mc16": TCut("tau_0_jet_bdt_loose==1 && tau_0_jet_bdt_score_trans>0.02"),
}
TAUID_MEDIUM = {
    "mc15":TCut("tau_0_jet_bdt_medium==1"),
    "mc16":TCut("tau_0_jet_bdt_medium==1"),
}
TAUID_TIGHT = {
    "mc15": TCut("tau_0_jet_bdt_tight==1"),
    "mc16": TCut("tau_0_jet_bdt_tight==1"),
}
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
    "mc16": TCut("tau_0_p4->Pt() > 30000") ,
}
TAU_PT40 = {
    "mc15": TCut("tau_0_pt > 40000"),
    "mc16": TCut("tau_0_p4->Pt() > 40000") ,
}
TAU_ETA = {
    "mc15": TCut("abs(tau_0_eta)<2.3 && !(abs(tau_0_eta)< 1.52 && abs(tau_0_eta)> 1.37)"),
    "mc16": TCut("abs(tau_0_p4->Eta())<2.3 && !(abs(tau_0_p4->Eta())< 1.52 && abs(tau_0_p4->Eta())> 1.37)") ,
}


TAU_IS_LEP = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==11 || abs(tau_0_truth_universal_pdgId)==13"),
    "mc16": TCut("true_tau_0_isMuon || true_tau_0_isEle"),
}
TAU_IS_EL = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==11"),
    "mc16": TCut("true_tau_0_isEle"),
}

TAU_IS_TRUE = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==15"),
    "mc16": TCut("true_tau_0_isTau"),
}
TAU_IS_FAKE = {
    "mc15": TCut("!"+(TAU_IS_TRUE["mc15"].GetTitle()+"||"+TAU_IS_LEP["mc15"].GetTitle() ) ),
    "mc16": TCut("!"+(TAU_IS_TRUE["mc16"].GetTitle()+"||"+TAU_IS_LEP["mc16"].GetTitle() ) ),
}
ANTI_TAU = {
    "mc15": TCut("tau_0_jet_bdt_score_sig > 0.02 && tau_0_jet_bdt_loose==0"),
    "mc16": TCut("tau_0_jet_bdt_score_trans > 0.02 && tau_0_jet_bdt_loose==0"),
}

VETO_TAU = {
    "mc15": ROOT.TCut("n_taus==0"),
    "mc16": ROOT.TCut("n_taus==0"),
}

TAU_BASE = {}
for mcc in ["mc15", "mc16"]:
    TAU_BASE[mcc] = TAU_PT30[mcc] + TAU_ETA[mcc] + TAU_TRACKS[mcc]

    
##------------------------------------------------------------------------------------
##  - - lepton
##------------------------------------------------------------------------------------
LEP_VETO = {
    "mc15": TCut("(n_electrons + n_muons)==0"),
    "mc16": TCut("(n_electrons + n_muons)==0"),
}
ONE_LEP = {
    "mc15": TCut("(n_electrons + n_muons)==1"),
    "mc16": TCut("(n_electrons + n_muons)==1"),
}
LEP_PT30 = {
    "mc15": TCut("(mu_0_pt + el_0_pt)> 30000"),
    "mc16": TCut("(mu_0_p4->Pt() + el_0_p4->Pt()) > 30000") ,
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
    "mc16": ROOT.TCut("n_electrons==1 && el_0_p4->Pt() > 30000 && el_0_id_veryloose && el_0_iso_FixedCutTight"\
                      "&& (abs(el_0_p4->Eta()) < 2.47 && !(abs(el_0_p4->Eta()) < 1.52 && abs(el_0_p4->Eta()) > 1.37))"),
}
MU_BASE = {
    "mc15": ROOT.TCut("n_muons==1 && mu_0_pt > 30000 && mu_0_id_tight && mu_0_iso_FixedCutTight && abs(mu_0_eta) < 2.5"),
    "mc16": ROOT.TCut("n_muons==1 && mu_0_p4->Pt() > 30000 && mu_0_id_loose"),# && mu_0_iso_FixedCutTight && abs(mu_0_p4->Eta()) < 2.5"),
}
VETO_EL = {
    "mc15": ROOT.TCut("n_electrons==0"),
    "mc16": ROOT.TCut("n_electrons==0"),
}
VETO_MU = {
    "mc15": ROOT.TCut("n_muons==0"),
    "mc16": ROOT.TCut("n_muons==0"),
}
SS_TAU_MU = {
    "mc15": ROOT.TCut("tau_0_q*mu_0_q==1"),
    "mc16": ROOT.TCut("tau_0_q*mu_0_q==1"),
}
SS_TAU_EL = {
    "mc15": ROOT.TCut("tau_0_q*el_0_q==1"),
    "mc16": ROOT.TCut("tau_0_q*el_0_q==1"),
}
OS_TAU_MU = {
    "mc15": ROOT.TCut("tau_0_q*mu_0_q==-1"),
    "mc16": ROOT.TCut("tau_0_q*mu_0_q==-1"),
}
OS_TAU_EL = {
    "mc15": ROOT.TCut("tau_0_q*el_0_q==-1"),
    "mc16": ROOT.TCut("tau_0_q*el_0_q==-1"),
}

SS_MU_EL = {
    "mc15": ROOT.TCut("mu_0_q*el_0_q==1"),
    "mc16": ROOT.TCut("mu_0_q*el_0_q==1"),
}
OS_MU_EL = {
    "mc15": ROOT.TCut("el_0_q*mu_0_q==-1"),
    "mc16": ROOT.TCut("el_0_q*mu_0_q==-1"),
}

# - - - - W lep 
W_LEP_MT_60 = {
    "mc15": TCut("(sqrt(2. * el_0_pt * met_et"\
                      "* (1 - cos(met_phi - el_0_phi)))"\
                      "+ sqrt(2. * mu_0_pt * met_et"\
                      "* (1 - cos(met_phi - mu_0_phi) ) ) ) > 60000"),
    
    "mc16": TCut("(sqrt(2. * el_0_p4->Pt() * met_p4->Et()"\
                 "* (1-cos(met_p4->Phi() - el_0_p4->Phi())))"\
                 "+ sqrt(2. * mu_0_p4->Pt() * met_p4->Et()"\
                 "* (1 - cos(met_p4->Phi()-mu_0_p4->Phi() ) ) ) ) > 60000")
}
W_LEP_MT_MAX160 = {
    "mc15": TCut("(sqrt(2. * el_0_pt * met_et"\
                      "* (1 - cos(met_phi - el_0_phi)))"\
                      "+ sqrt(2. * mu_0_pt * met_et"\
                      "* (1 - cos(met_phi - mu_0_phi) ) ) ) < 160000"),
    
    "mc16": TCut("(sqrt(2. * el_0_p4->Pt() * met_p4->Et()"\
                 "* (1-cos(met_p4->Phi() - el_0_p4->Phi())))"\
                 "+ sqrt(2. * mu_0_p4->Pt() * met_p4->Et()"\
                 "* (1 - cos(met_p4->Phi()-mu_0_p4->Phi() ) ) ) ) < 160000")
}


##------------------------------------------------------------------------------------
##  - - jets
##------------------------------------------------------------------------------------
NUM_BJETS1 = {
    "mc15": TCut("n_bjets > 0"),
    "mc16": TCut("n_bjets > 0"),
}
NUM_BJETS2 = {
    "mc15": TCut("n_bjets > 1"),
    "mc16": TCut("n_bjets > 1"),
}
NUM_JETS1  = {
    "mc15": TCut("n_jets > 0"),
    "mc16": TCut("n_jets > 0"),
}

NUM_JETS3  = {
    "mc15": TCut("n_jets > 2"),
    "mc16": TCut("n_jets > 2"),
}
NUM_JETS4  = {
    "mc15": TCut("n_jets > 3"),
    "mc16": TCut("n_jets > 3"),
}

BVETO = {
    "mc15": TCut("n_bjets==0"),
    "mc16": TCut("n_bjets==0"),
}
JET_PT25 = {
    "mc15": TCut("jet_0_pt > 25000"),
    "mc16": TCut("jet_0_p4->Pt() > 25000"),
}
BJET_PT25 = {
    "mc15": TCut("bjet_0_pt > 25000"),
    "mc16": TCut("bjet_0_p4->Pt() > 25000"),
}

#WIP! - - - - BDT scores for partial blinding 


##------------------------------------------------------------------------------------
## selection categories: KEEP THEM AS CLEAN AS POSSIBLE :) 
##------------------------------------------------------------------------------------
SELECTIONS = {"taujet":{}, "taulep": {} }
    
##-------------------------------------
# - - TAUJET 
##-------------------------------------
# - - - -  base selections
SELECTIONS["taujet"]["BASE"] = (
    CLEAN_EVT,
    TAU_PT40,
    TAU_ETA,
    LEP_VETO,
    TAU_TRACKS)

# - - - - Preselection
SELECTIONS["taujet"]["PRESELECTION"] = (
    MET100, 
    NUM_JETS3,
    BJET_PT25,
    MT50)

# - - - - TTBar_CR
SELECTIONS["taujet"]["TTBAR"] = (
    NUM_JETS3,
    NUM_BJETS2,
    BJET_PT25,
    MET150,
    MT_MAX100)
    
# - - - - QCD CR
SELECTIONS["taujet"]["QCD"] = (
    NUM_JETS3,
    JET_PT25,
    BVETO,
    MET_MAX150,
    MT50)

# - - - - WJets CR
SELECTIONS["taujet"]["BVETO"] = (
    NUM_JETS3,
    JET_PT25,
    BVETO,
    MET150,
    MT_MAX100)
    
# - - - -  Signal 
SELECTIONS["taujet"]["SR_TAUJET"] = (
    NUM_JETS3,
    JET_PT25,
    MET150,
    MT50,
    NUM_BJETS1,
    BJET_PT25)

##-------------------------------------
# - - TAULEP (BASE will be added to all)
##-------------------------------------
SELECTIONS["taulep"]["BASE"] = (
    CLEAN_EVT,
    #ONE_LEP,
)

SELECTIONS["taulep"]["PRESELECTION"] = (
    TAU_BASE,
    ONE_LEP,
    NUM_JETS1,
    JET_PT25)

# - - - - tau-el signal region
SELECTIONS["taulep"]["SR_TAUEL"] = (
    TAU_BASE,
    EL_BASE,
    OS_TAU_EL,
    VETO_MU,
    NUM_JETS1,
    JET_PT25,
    NUM_BJETS1,
    BJET_PT25,
    MET50,
)

# - - - - tau-mu signal region
SELECTIONS["taulep"]["SR_TAUMU"] = (
    TAU_BASE,
    MU_BASE,
    OS_TAU_MU,
    VETO_EL,
    NUM_JETS1,
    JET_PT25,
    NUM_BJETS1,
    BJET_PT25,
    MET50,
)

# - - - - dilepton b-tag control region
SELECTIONS["taulep"]["TAUEL_BVETO"] = (
    EL_BASE,
    OS_TAU_EL,
    TAU_BASE,
    VETO_MU,
    NUM_JETS1,
    JET_PT25,
    BVETO,
    MET50,
)
SELECTIONS["taulep"]["TAUMU_BVETO"] = (
    MU_BASE,
    OS_TAU_MU,
    TAU_BASE,
    VETO_EL,
    NUM_JETS1,
    JET_PT25,
    BVETO,
    MET50,
)

# - - - - dilepton b-tag (ttbar) control region
SELECTIONS["taulep"]["DILEP_BTAG"] = (
    EL_BASE,
    #OS_MU_EL,
    #TAU_BASE,
    #VETO_TAU,
    NUM_JETS1,
    JET_PT25,
    NUM_BJETS1,
    BJET_PT25,
    MET50,
    MU_BASE,
)

# - - - - same sign tau-el control region
SELECTIONS["taulep"]["SS_TAUEL"] = (
    TAU_BASE,
    EL_BASE,
    SS_TAU_EL,
    VETO_MU,
    NUM_JETS1,
    JET_PT25,
    MET50,
)

# - - - - same-sign tau-mu control region
SELECTIONS["taulep"]["SS_TAUMU"] = (
    TAU_BASE,
    MU_BASE,
    SS_TAU_MU,
    VETO_EL,
    NUM_JETS1,
    JET_PT25,
    MET50,
)


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
    #>>> categories = Category.factory()
    """
    TYPES = {
        "taujet":{
            "PRESELECTION": "presel",
            "TTBAR": "ttbar CR",
            #"QCD": "qcd CR",
            "BVETO": "b-veto CR",
            "SR_TAUJET": "#tau-jet SR",},
        
        "taulep":{
            "PRESELECTION": "presel",
            "SR_TAUEL": "#tau-e SR",
            "SR_TAUMU": "#tau-#mu SR",
            "TAUMU_BVETO": "#tau-#mu b-veto CR",
            "TAUEL_BVETO": "#tau-e b-veto CR",
            "DILEP_BTAG": "#mu-e b-tag CR",
            "SS_TAUEL": "same sign #tau-el CR",
            "SS_TAUMU": "same sign #tau-#mu CR",
            #"ZEE": "Zee CR",
        },
    }
    
    @classmethod
    def factory(cls, mc_camp=MC_CAMPAIGN, channel="taujet"):
        """ factory method for categories
        """
        categories = [] 
        for name, label in cls.TYPES[channel].iteritems(): 
                cat = cls(name, label=label, channel=channel, mc_camp=mc_camp)
                categories.append(cat)
                            
        return categories
    
    def __init__(self, name,
                 label="",
                 channel="taujet",
                 mc_camp="mc16",
                 cuts_list=[]):
        
        self.channel = channel
        self.name = name
        self.label = label;
        self.mc_camp = mc_camp
        self.cuts_list = cuts_list[:]
        
    @property
    def cuts(self):
        """
        """
        if self.cuts_list:
            selections = ROOT.TCut("")
            for citem in self.cuts_list:
                if isinstance(citem, dict):
                    selections += citem[self.mc_camp]
                elif isinstance(citem, ROOT.TCut):
                    selections += citem
                else:
                    raise TypeError("dict or ROOT.TCut is expected but {} found".format(citem))
        else:
            # - - - - - - - -  read selections from SELECTION dictionary
            assert self.name in Category.TYPES[self.channel].keys(),\
                "%s Category is not supported; see categories.Category"%self.name
            base = SELECTIONS[self.channel]["BASE"]
            try:
                cuts_list = base + SELECTIONS[self.channel][self.name.upper()]
            except KeyError:
                raise RuntimeError("couldn't find selections for %s : %s: %s  ! "%(
                    self.name, self.channel, self.mc_camp))

            selections = ROOT.TCut("")
            for citem in cuts_list:
                if isinstance(citem, dict):
                    selections += citem[self.mc_camp]
                elif isinstance(citem, ROOT.TCut):
                    selections += citem
                else:
                    raise TypeError("dict or ROOT.TCut is expected but {} found".format(citem))
                
        return selections 
    
    def __repr__(self):
        return "CATEGORY:: name=%r, cuts=%r\t\n"%(
            self.name, self.cuts.GetTitle())


##------------------------------------------------------------------------------------
## - - Fake Factors CR
##------------------------------------------------------------------------------------
FF_CR_MULTIJET = Category(
    "FF_CR_MULTIJET", label="ff multijet CR",
    cuts_list=[
        CLEAN_EVT,
        TAU_PT30,
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
        EL_BASE,
        TAU_BASE,
        BVETO,
        W_LEP_MT_60,
        W_LEP_MT_MAX160,
    ],
)

# - - - - collective Fake Factors CR 
FF_CR_REGIONS = {}
FF_CR_REGIONS["taujet"] = [FF_CR_MULTIJET]
FF_CR_REGIONS["taulep"] = [FF_CR_WJETS]


##------------------------------------------------------------------------------------
## - - cutflow selections 
##------------------------------------------------------------------------------------
CUTFLOW = {
    "taujet": OrderedDict(
        [("cleanEvent",  CLEAN_EVT),
         ("trigger", {"mc16": ROOT.TCut("1>0"), "mc15": ROOT.TCut("1>0")}), #<! trigger is applied globally (just a place holder here)
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
         ("eBase", EL_BASE),
         ("3jets", NUM_JETS3),
         ("jetPt25", JET_PT25),
         ("1bjets", NUM_BJETS1),
         ("MET50", MET150),
         ("mT50", MT50),
        ]),
}
