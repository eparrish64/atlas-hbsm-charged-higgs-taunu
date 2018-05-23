import ROOT

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

TRIGGERS = dict()

TRIGGERS["taujet"] = {
    "2015": ROOT.TCut(""), 
    "2016": ROOT.TCut(""),
    "2017": ROOT.TCut(""),
    "2018": ROOT.TCut("")
}

TRIGGERS["taulep"] = {
    "2015": ROOT.TCut(""), 
    "2016": ROOT.TCut(""),
    "2017": ROOT.TCut(""),
    "2018": ROOT.TCut("")
}
