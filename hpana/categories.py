# -*- coding: utf-8 -*-

from math import pi
import ROOT
from ROOT import TCut

from db.decorators import cached_property
from . import log, MC_CAMPAIGN

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

MT100 = {
    "mc15": TCut("tau_0_met_mt > 100000"),
    "mc16": TCut("tau_0_met_mt > 100000")
}
MT50 = {
    "mc15": TCut("tau_0_met_mt > 50000"),
    "mc16": TCut("tau_0_met_mt > 50000")
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
TAU_TRACKS = {
    "mc15": TCut("tau_0_n_tracks==1 || tau_0_n_tracks==3"),
    "mc16": TCut("tau_0_n_charged_tracks==1 || tau_0_n_charged_tracks==3"),
}
TAU_PT40 = {
    "mc15": TCut("tau_0_pt > 40000"),
    "mc16": TCut("tau_0_p4->Pt() > 40000") ,
}
TAU_IS_LEP = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==11 || abs(tau_0_truth_universal_pdgId)==13"),
    "mc16": TCut("abs(true_tau_0_pdgId)==11 || abs(true_tau_0_pdgId)==13"),
}
TAU_IS_TRUE = {
    "mc15": TCut("abs(tau_0_truth_universal_pdgId)==15"),
    "mc16": TCut("abs(true_tau_0_pdgId)==15"),
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
    MET100,
    NUM_JETS3,
    BJET_PT25,
    MT50)
    
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
     MT100)
    
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
                 mc_camp="mc16"):
        
        self.channel = channel
        assert name in Category.TYPES[self.channel].keys(),\
            "%s Category is not supported; see categories.Category"%name
        self.name = name
        self.label = label;
        self.mc_camp = mc_camp
        
    @property
    def cuts(self):
        """
        """

        # - - - - - - - -  read selections from SELECTION dictionary
        base = SELECTIONS[self.channel]["BASE"]
        try:
            cuts = base + SELECTIONS[self.channel][self.name.upper()]
        except KeyError:
            raise RuntimeError("couldn't find selections for %s : %s: %s  ! "%(
                self.name, self.channel, self.mc_camp))
        cuts = reduce(lambda c1, c2: c1+c2, [cdict[self.mc_camp] for cdict in cuts])

        return cuts
    
    def __repr__(self):
        return "CATEGORY:: name=%r, channel=%r, mc_camp=%r, cuts=%r\t\n"%(
            self.name, self.channel, self.mc_camp, self.cuts.GetTitle())
    
    
# - - - - - - - - build categories
CATEGORIES = Category.factory()
    
