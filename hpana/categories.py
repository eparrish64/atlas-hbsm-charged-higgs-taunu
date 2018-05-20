# -*- coding: utf-8 -*-

from math import pi
import ROOT
from ROOT import TCut

from db.decorators import cached_property

"""
This module provides all selections needed for the analysis.
"""

##------------------------------------------------------------------------------------
## TAUJET BASIC CUTS

# - - - - - - - - event 
CLEAN_EVT = ROOT.TCut("(event_clean==1) && (n_vx>=1) && (bsm_tj_dirty_jet==0)")

# - - - - - - - - MET 
MET100 = TCut("met_et>100000")
MET150 = TCut("met_et>150000")
MT100   = TCut("tau_0_met_mt > 100000")
MT50   = TCut("tau_0_met_mt > 50000")

# - - - - - - - - tau
Tau_Q = TCut("abs(tau_0_q)==1")
TAU_TRACKS = TCut("tau_0_n_tracks==1 || tau_0_n_tracks==3")
Tau_DECAY_MODE = TCut("tau_0_decay_mode==0")
TauID_LOOSE = TCut("tau_0_jet_bdt_loose==1")
TauID_MED = TCut("tau_0_jet_bdt_medium==1")
TauID_TIGHT = TCut("tau_0_jet_bdt_tight==1")
Tau_PT40 = TCut("tau_0_pt>40000")

# - - - - - - - - lep
LEP_VETO = TCut("(n_electrons+n_muons)==0")
ONE_LEP = TCut("(n_electrons+n_muons)==1")

# - - - - - - - - tau ID
TAU_IS_LEP = TCut("abs(tau_0_truth_universal_pdgId)==11||abs(tau_0_truth_universal_pdgId)==13")
TAU_IS_TRUE = TCut("abs(tau_0_truth_universal_pdgId)==15") 
TAU_IS_FAKE = TCut("!"+(TAU_IS_TRUE.GetTitle()+"||"+TAU_IS_LEP.GetTitle()))
TRUTH_MATCH = TCut("abs(tau_0_truth_universal_pdgId)==15")

# - - - - - - - - jets
NUM_BJETS1 = TCut("n_bjets>0")
NUM_BJETS2 = TCut("n_bjets>1")
BVETO = TCut("n_bjets==0")
NUM_JETS3 = TCut("n_jets>2")
JET_PT25 = TCut("jet_0_pt > 25000")
BJET_PT25 = TCut("bjet_0_pt > 25000")

#WIP! - - - - BDT scores for partial blinding 


##------------------------------------------------------------------------------------
## selection categories: KEEP THEM AS CLEAN AS POSSIBLE :) 

SELECTIONS = dict()

# - - - -  base selections
SELECTIONS["BASE"] = {
    "taujet":{
        "2015":
        (CLEAN_EVT
         + Tau_PT40
         + LEP_VETO
         + TAU_TRACKS
         + TCut("tau_0_n_tracks==1")),
        
        "2016":
        (CLEAN_EVT
         + Tau_PT40
         + LEP_VETO
         + TAU_TRACKS
         + TCut("tau_0_n_tracks==1")),
        
        "2017":
        (CLEAN_EVT
         + Tau_PT40
         + LEP_VETO
         + TAU_TRACKS
         + TCut("tau_0_n_tracks==1")),
    },
    "taulep":{
        "2015": TCut(""),
        "2016": TCut(""),
        "2017": TCut(""),
    }
} #<! BASE

# - - - - Preselection
SELECTIONS["PRESELECTION"] = {
    "taujet": {
        "2015":(MET100
                + NUM_JETS3
                + BJET_PT25
                + TCut("tau_0_met_mt > 50000")),
        "2016":(MET100
                + NUM_JETS3
                + BJET_PT25
                + TCut("tau_0_met_mt > 50000")),
        "2017": TCut(""),
    },
    "taulep": {
        "2015": TCut(""),
        "2016": TCut(""),
        "2017": TCut(""),
    },
    
}

# - - - - TTBar_CR
SELECTIONS["TTBAR_CR"] = {
    "taujet": {
        "2015":(Tau_PT40
                + LEP_VETO
                + NUM_JETS3
                + NUM_BJETS2
                + JET_PT25
                + BJET_PT25
                + MET150
                + TCut("!(%s)"%MT100)),
        "2016":(Tau_PT40
                + LEP_VETO
                + NUM_JETS3
                + NUM_BJETS2
                + JET_PT25
                + BJET_PT25
                + MET150
                + TCut("!(%s)"%MT100)),
        "2017": TCut(""),
    },
    "taulep": {
        "2015": TCut(""),
        "2016": TCut(""),
        "2017": TCut(""),
    },
    
}

# - - - - QCD CR 
SELECTIONS["QCD_CR"] = {
    "taujet": {
        "2015":(NUM_JETS3
                + JET_PT25
                + BVETO
                + TCut("met_et < 150000")
                + TCut("tau_0_met_mt > 50000")),
        "2016":(NUM_JETS3
                + JET_PT25
                + BVETO
                + TCut("met_et < 150000")
                + TCut("tau_0_met_mt > 50000")),
        "2017": TCut(""),
    },
    "taulep": {
        "2015": TCut(""),
        "2016": TCut(""),
        "2017": TCut(""),
    },
    
}

# - - - - WJets CR
SELECTIONS["WJETS_CR"] = {
    "taujet": {
        "2015":(NUM_JETS3
                + JET_PT25
                + BVETO
                + MET150
                + MT100),
        "2016":(NUM_JETS3
                + JET_PT25
                + BVETO
                + MET150
                + MT100),
        "2017": TCut(""),
    },
    "taulep": {
        "2015": TCut(""),
        "2016": TCut(""),
        "2017": TCut(""),
    },
    
}

# - - - -  Signal 
SELECTIONS["SR"] = {
    "taujet": {
        "2015":(NUM_JETS3
                + JET_PT25
                + MET150 
                + NUM_BJETS1
                + BJET_PT25
                + TCut("tau_0_met_mt > 50000")),
        "2016":(NUM_JETS3
                + JET_PT25
                + MET150 
                + NUM_BJETS1
                + BJET_PT25
                + TCut("tau_0_met_mt > 50000")),
        "2017": TCut(""),
    },
    "taulep": {
        "2015": TCut(""),
        "2016": TCut(""),
        "2017": TCut(""),
    },
}

##------------------------------------------------------------------------------------
## 
class Category(object):
    """base class for selection categories.

    Attributes
    ----------
    
    Examples
    --------
    >>> presel = Category("Preselection", label="presel", channel="taujet", year="2017")
    >>> categories = Category.factory()
    """
    NAMES = {
        "Preselection": "Presel",
        "TTBar_CR": "ttbar CR",
        "QCD_CR": "qcd CR",
        "WJets_CR": "wjets CR",
        "SR": "signal region",
    }
    CHANNELS = ["taujet", "taulep"]
    YEARS = ["2015", "2016", "2017"]
    
    @classmethod
    def factory(cls):
        """ factory method for categories
        """
        categories = {}
        for channel in cls.CHANNELS:
            if channel not in categories:
                categories[channel] = {}
            for year in cls.YEARS:
                if year not in categories[channel]:
                    categories[channel][year] = []
                for name, label in cls.NAMES.iteritems():
                    cat = cls(name, label=label, channel=channel, year=year)
                    categories[channel][year].append(cat)
                    
        return categories
    
    def __init__(self, name, label="", channel="taujet", year="2017"):
        assert name in self.NAMES.keys(), "%s Category is not supported; see categories.Category"%name
        self.name = name
        self.label = label
        self.channel = channel
        self.year = year

    @cached_property
    def cuts(self):
        """
        """

        # - - - - - - - -  read selections from SELECTION dictionary
        base = SELECTIONS["BASE"][self.channel][self.year]
        try:
            selection = base + SELECTIONS[self.name.upper()][self.channel][self.year]
            return selection
        except KeyError:
            log.warning(
                "couldn't find selections for %s : %s: %s  !; continuing with the base selections ... "%(self.name, self.channel, self.year))
            return base
    
    
    def __repr__(self):
        return "CATEGORY:: name=%r, channel=%r, year=%r, cuts=%r\t\n"%(
            self.name, self.channel, self.year, self.cuts.GetTitle())
    
    
# - - - - - - - - build categories
CATEGORIES = Category.factory()

