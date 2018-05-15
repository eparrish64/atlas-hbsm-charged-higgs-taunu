from math import pi
import ROOT
from ROOT import TCut

"""
This module provides all selections needed for the analysis.
"""

# --# trigger
"""
up to 302956 this was ICHEP dataset, in the runs 302872 -302956 the
xe90 trigger became prescaled (~98% or something) so we are using xe90
until period D4 (302872) and later the xe110; the corresponding
trigger efficiency in MC is then:
((6.11*trigger_EFF_mht90+26.75*trigger_EFF_mht110+3.21*trigger_EFF_lcw70)/36.07)
"""
HLT_MET = ROOT.TCut(
    "(run_number<=284484 && HLT_xe70_tc_lcw==1)" #<! 2015 
    "||(run_number>284484 && HLT_xe90_mht_L1XE50==1 && run_number<=302872)"
    "||(run_number>302872 && HLT_xe110_mht_L1XE50==1)"
    )

# --# base
CLEAN_EVT = ROOT.TCut("(event_clean==1) && (n_vx>=1) && (bsm_tj_dirty_jet==0)")

MET_100 = TCut("met_et>100000")
MET_150 = TCut("met_et>150000")
MT100   = TCut("tau_0_met_mt > 100000")
MT50   = TCut("tau_0_met_mt > 50000")

# --# tau
Tau_Q = TCut("abs(tau_0_q)==1")
Tau_Tracks = TCut("tau_0_n_tracks==1 || tau_0_n_tracks==3")
Tau_DECAY_MODE = TCut("tau_0_decay_mode==0")
TauID_LOOSE = TCut("tau_0_jet_bdt_loose==1")
TauID_MED = TCut("tau_0_jet_bdt_medium==1")
TauID_TIGHT = TCut("tau_0_jet_bdt_tight==1")
Tau_PT40 = TCut("tau_0_pt>40000")

LepVeto = TCut("(n_electrons+n_muons)==0")
One_Lep = TCut("(n_electrons+n_muons)==1")
Tau_isLEP = TCut("abs(tau_0_truth_universal_pdgId)==11||abs(tau_0_truth_universal_pdgId)==13")
Tau_isTRUE = TCut("abs(tau_0_truth_universal_pdgId)==15") 
Tau_isFAKE = TCut("!"+(Tau_isTRUE.GetTitle()+"||"+Tau_isLEP.GetTitle()))

## jets
nBJets1 = TCut("n_bjets>0")
nBJets2 = TCut("n_bjets>1")
BVeto = TCut("n_bjets==0")
nJets3 = TCut("n_jets>2")
JET_PT25 = TCut("jet_0_pt > 25000")
bJET_PT25 = TCut("bjet_0_pt > 25000")

# bdt scores, sorry for the ungliness, needed 
# branches are not in the trees
BDT_90to120 = TCut(
    '( (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p + (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_90to120_3p) < 0.5'
    )
BDT_130to160 = TCut(
    '( (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p + (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_130to160_3p) < 0.5'
    )
BDT_160to180 = TCut(
    '( (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p + (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p) < 0.5'
    )

BDT_200to400 = TCut(
    '( (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p + (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p) < 0.5'
    )
BDT_500to2000 = TCut(
    'FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p < 0.5'
    )
LOW_BDT_SCORES = (
    BDT_90to120 + BDT_130to160 + BDT_160to180 + BDT_200to400 + BDT_500to2000
    )

## common cuts for all categories
#  HLT_MET   ###this is only applied to data and QCD
# TauID_MED  ##this is a property of the regionDefition
COMMON_CUTS = (
    CLEAN_EVT
    + Tau_PT40
    + LepVeto
    + Tau_Tracks
    # + TCut("tau_0_n_tracks==1") #<! for upsilon only
    )

class CategoryMeta(type):
    """
    Metaclass for all categories, 
    to avoid duplicate naming for categories and
    regions.
    """
    CATEGORY_REGISTRY = {}
    def __new__(cls, name, bases, dct):
        if name in CategoryMeta.CATEGORY_REGISTRY:
            raise ValueError("Multiple categories with the same name: %s" % name)
        cat = type.__new__(cls, name, bases, dct)
        # register the category
        CategoryMeta.CATEGORY_REGISTRY[name] = cat
        return cat
    
class Category(object):
    __metaclass__ = CategoryMeta
    pass

class Preselection(Category):
    name = "preselection"
    lable= "presel"    
    with_sys = True#False
    tau_id = TauID_MED
    regionFFIDX=1
    cuts = (
        COMMON_CUTS
        + MET_100
        + nJets3
        + bJET_PT25
        + TCut("tau_0_met_mt > 50000"))

## signal
class MVA_SignalRegion_LowBDT(Category):
    name = "MVA_SR_LowBDT"
    label = "MVA signal"
    with_sys = True
    tau_id = TauID_MED
    regionFFIDX=3
    cuts = (
        COMMON_CUTS
        + nBJets1
        + nJets3
        + MET_150
        + TCut("tau_0_met_mt > 50000")
        + LOW_BDT_SCORES
        )
    
class MVA_SignalRegion(Category):
    name = "MVA_SR"
    label = "MVA signal"
    with_sys = True
    tau_id = TauID_MED
    regionFFIDX=3
    cuts = (
        COMMON_CUTS
        + nJets3
        + JET_PT25
        + MET_150 
        + nBJets1
        + bJET_PT25
        + TCut("tau_0_met_mt > 50000")
        )

class QCD_CR(Category):
    name = 'qcdCR'
    lable = 'qcdCR'    
    with_sys = True
    tau_id = TauID_MED
    regionFFIDX=111
    cuts = (
        COMMON_CUTS
        + nJets3
        + JET_PT25
        + BVeto
        + TCut("met_et < 150000")
        + TCut("tau_0_met_mt > 50000"))

class WJets_CR(Category):
    name = 'WjetsCR'
    lable = 'WjetsCR'
    with_sys = True
    tau_id = TauID_MED
    regionFFIDX=2
    cuts = (
        COMMON_CUTS
        + nJets3
        + JET_PT25
        + BVeto
        + MET_150
        + TCut("!(%s)"%MT100)
        )
class WJets_MT100_CR(Category):
    name = 'WjetsmT100CR'
    lable = 'WjetsmT100CR'
    with_sys = True
    tau_id = TauID_MED
    regionFFIDX=2
    cuts = (
        COMMON_CUTS
        + nJets3
        + JET_PT25
        + BVeto
        + MET_150
        + MT100
        )

class TTBar_CR(Category):
    name = 'TTBarCR'
    lable = 'TTBarCR'
    with_sys = True
    tau_id = TauID_MED
    regionFFIDX=3#???? same as SR?
    cuts = (
        CLEAN_EVT
        + Tau_PT40
        + LepVeto 
        + nJets3
        + nBJets2
        + JET_PT25
        + bJET_PT25
        + MET_150
        + TCut("!(%s)"%MT100)
        )
