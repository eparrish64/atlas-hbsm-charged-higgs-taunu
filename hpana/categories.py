# -*- coding: utf-8 -*-


from math import pi
from collections import OrderedDict

import ROOT
from ROOT import TCut

from db.decorators import cached_property
from . import log, MC_CAMPAIGN
from .trigger import HLT_MET

"""
This module provides all selections needed for the analysis.
"""

##------------------------------------------------------------------------------------
## TAUJET BASIC CUTS

# - - - - - - - - event 
CLEAN_EVT = {
    "mc15": TCut("(event_clean==1) && (n_vx>=1) && (bsm_tj_dirty_jet==0)"),
    "mc16": TCut("(n_vx>=1)")
}

# - - - - - - - - MET & MT
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

 
# - - - - - - - - tau
TAU_Q = {
    "mc15": TCut("abs(tau_0_q)==1"),
    "mc16": TCut("abs(tau_0_q)==1"),
}
TAU_DECAY_MODE = {
    "mc15": TCut("tau_0_decay_mode==0"),
    "mc16": TCut("tau_0_decay_mode==0"),
}
TAUID_LOOSE = {
    "mc15": TCut("tau_0_jet_bdt_loose==1"),
    "mc16": TCut("tau_0_jet_bdt_loose==1"),
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

TAU_IS_LEP = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==11 || abs(tau_0_truth_universal_pdgId)==13"),
    "mc16": TCut("true_tau_0_isMuon || true_tau_0_isEle")#("abs(true_tau_0_pdgId)==11 || abs(true_tau_0_pdgId)==13"),
}
TAU_IS_TRUE = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==15"),
    "mc16": TCut("true_tau_0_isTau")#("abs(true_tau_0_pdgId)==15"),
}
TAU_IS_FAKE = {
    "mc15": TCut("!"+(TAU_IS_TRUE["mc15"].GetTitle()+"||"+TAU_IS_LEP["mc15"].GetTitle() ) ),
    "mc16": TCut("!"+(TAU_IS_TRUE["mc16"].GetTitle()+"||"+TAU_IS_LEP["mc16"].GetTitle() ) ),
}
ANTI_TAU = {
    "mc15": TCut("tau_0_jet_bdt_score_sig > 0.02 && tau_0_jet_bdt_loose==0"),
    "mc16": TCut("tau_0_jet_bdt_score_trans > 0.02 && tau_0_jet_bdt_loose==0"),
}
# - - - - - - - - lep
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

# - - - - lep ID
ELID_TIGHT = {
    "mc15":TCut("n_electrons && el_0_id_tight"),
    "mc16":TCut("n_electrons && el_0_id_tight"),
}
MUID_TIGHT = {
    "mc15":TCut("n_muons && mu_0_id_tight"),
    "mc16":TCut("n_muons && mu_0_id_tight"),
}

# - - - - - - - - jets
NUM_BJETS1 = {
    "mc15": TCut("n_bjets > 0"),
    "mc16": TCut("n_bjets > 0"),
}
NUM_BJETS2 = {
    "mc15": TCut("n_bjets > 1"),
    "mc16": TCut("n_bjets > 1"),
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

SELECTIONS = {"taujet":{}, "taulep": {} }
    
# - - - - - - - - - TAUJET channel
# - - - -  base selections
SELECTIONS["taujet"]["BASE"] = (
    CLEAN_EVT,
    TAU_PT40,
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

# - - - - - - - - TAULEP
SELECTIONS["taulep"]["BASE"] = ()
SELECTIONS["taujet"]["PRESELECTION"]
SELECTIONS["taujet"]["TTBAR"]

##------------------------------------------------------------------------------------
## 
class Category:
    """base class for selection categories.
    
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
            "QCD": "qcd CR",
            "BVETO": "b-veto CR",
            "SR_TAUJET": "signal region",},
        
        "taulep":{},
    }
    
    @classmethod
    def factory(cls, mc_camp=MC_CAMPAIGN, channel="taujet"):
        """ factory method for categories
        """
        categories = [] #{"taujet":[], "taulep": []}
        for channel, types in cls.TYPES.iteritems():
            for name, label in types.iteritems(): 
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
            print self.mc_camp, reduce(lambda c1, c2: c1+c2, [cdict[self.mc_camp] for cdict in self.cuts_list])
            return reduce(lambda c1, c2: c1+c2, [cdict[self.mc_camp] for cdict in self.cuts_list])
        
        else:
            # - - - - - - - -  read selections from SELECTION dictionary
            assert self.name in Category.TYPES[self.channel].keys(),\
                "%s Category is not supported; see categories.Category"%self.name
            base = SELECTIONS[self.channel]["BASE"]
            try:
                cuts = base + SELECTIONS[self.channel][self.name.upper()]
            except KeyError:
                raise RuntimeError("couldn't find selections for %s : %s: %s  ! "%(
                    self.name, self.channel, self.mc_camp))
            cuts = reduce(lambda c1, c2: c1+c2, [cdict[self.mc_camp] for cdict in cuts])

            return cuts
    
    def __repr__(self):
        return "CATEGORY:: name=%r, cuts=%r\t\n"%(
            self.name, self.cuts.GetTitle())
    
    
# - - - - - - - - build categories
CATEGORIES = Category.factory()
    


# - - - - - - - - Fake Factors CR
FF_CR_MULTIJET = Category(
    "FF_CR_MULTIJET", label="ff multijet CR",
    cuts_list=[
        CLEAN_EVT,
        TAU_PT30,
        NUM_JETS4,
        LEP_VETO,
        BVETO,
        MET_MAX80,
        MT50,],
)

FF_CR_WJETS = Category(
    "FF_CR_WJETS", label="ff Wjets CR",
    cuts_list=[
        CLEAN_EVT,
        ONE_LEP,
        LEP_PT30,
        BVETO,
        ELID_TIGHT,
        MUID_TIGHT,
        W_LEP_MT_60,
        W_LEP_MT_MAX160,
    ],
)

# - - - - - - - - collective Fake Factors CR 
FF_CR_REGIONS = {}
FF_CR_REGIONS["taujet"] = [FF_CR_MULTIJET]
FF_CR_REGIONS["taulep"] = [FF_CR_WJETS]



# - - - - - - - - cutflow selections 
CUTFLOW = {
    "taujet": OrderedDict(
        [("clean event",  CLEAN_EVT),
         ("trigger", {"mc16": HLT_MET, "mc15":HLT_MET }),
         ("tau pt > 40 GeV", TAU_PT40),
         ("tauid", TAUID_MEDIUM),
         ("lep veto", LEP_VETO),
         #(">= 3 jets", NUM_JETS3),
         (">= 1 b-jets", NUM_BJETS1),
         #("jet pT > 25 GeV", JET_PT25),
         ("MET > 150 GeV", MET150),
         ("mT > 50 GeV", MT50),
        ]),
    "taulep": OrderedDict(),
}
