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

# - - - - - - - - - trigger selection
TRIGGERS = dict()

# - - - - taujet 
TRIGGERS["taujet"] = {
    "2015": ROOT.TCut("(run_number<=284484 && HLT_xe70_tc_lcw==1)"), 
    "2016": ROOT.TCut(
        "(run_number>284484 && HLT_xe90_mht_L1XE50==1 && run_number<=302872)"\
        "||(run_number>302872 && HLT_xe110_mht_L1XE50==1)"),
}

#WIP: - - - - taulep 
TRIGGERS["taulep"] = {
    "2015": ROOT.TCut(""), 
    "2016": ROOT.TCut(""),
    "2017": ROOT.TCut(""),
    "2018": ROOT.TCut("")
}

# - - - - - - - - trigger efficiencies for MC [not applicabel to Fakes and DATA]
TAUJET_EFF_TEMPLATE = "nominal_trig_eff({})"
TRIGGER_EFFICIENCIES = dict()

# - - - - taujet (MAKE SURE YOU GET THE UNITS RIGHT; GeV or MeV)
TRIGGER_EFFICIENCIES["taujet"] = {
    "mc15": TAUJET_EFF_TEMPLATE.format("met_et/1000."), 
    "mc16": TAUJET_EFF_TEMPLATE.format("met_p4->Et()/1000."),
}

##---------------------------------------------------------------------------------
## WIP: 
def get_trig_eff(years):
    """
    """
    return
