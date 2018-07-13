import ROOT

"""
* trigger info.
* up to 302956 this was ICHEP dataset, in the runs 302872 -302956 the
* xe90 trigger became prescaled (~98% or something) so we are using xe90
* until period D4 (302872) and later the xe110; the corresponding
* trigger efficiency in MC is then:
* ((6.11*trigger_EFF_mht90+26.75*trigger_EFF_mht110+3.21*trigger_EFF_lcw70)/36.07)
"""

# - - - - trigger selections 
TRIGGERS = {
    "taujet":{
        "DATA":{
            "2015": "(run_number <= 284484 && HLT_xe70_tc_lcw)", 
            "2016": "(run_number > 284484 && HLT_xe90_mht_L1XE50 && run_number <= 302872)||(run_number > 302872 && HLT_xe110_mht_L1XE50)",
        },
        "MC":{
            "2015": "(run_number <= 284484 && HLT_xe70_tc_lcw)", 
            "2016": "(run_number > 284484 && HLT_xe90_mht_L1XE50 && run_number <= 302872)||(run_number > 302872 && HLT_xe110_mht_L1XE50)",
        },
    },
    "taulep":{
        "DATA":{
            "2015": ("((run_number <= 288000)&&"\
                     "(HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose || HLT_mu20_iloose_L1MU15 || HLT_mu50))"), 
            "2016": ("((run_number > 288000)"\
                     "&&(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium || HLT_mu50))"),
            "2017": "",
            "2018": ""
        },
        "MC":{
            "2015": ("((run_number <= 288000)"\
                     "&&(HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose || HLT_mu20_iloose_L1MU15 || HLT_mu50))"), 
            "2016": ("((run_number > 288000)"\
                     "&&(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium || HLT_mu50))"),
            "2017": (""),
            "2018": ("")
        },
    },
}

# - - - - - - - - trigger efficiencies for MC [not applicabel to Fakes and DATA]
TAUJET_EFF_TEMPLATE = "nominal_trig_eff({})"
TRIGGER_EFFICIENCIES = dict()

# - - - - taujet (MAKE SURE YOU GET THE UNITS RIGHT; GeV or MeV)
TRIGGER_EFFICIENCIES["taujet"] = {
    "mc15": TAUJET_EFF_TEMPLATE.format("met_et/1000."), 
    "mc16": TAUJET_EFF_TEMPLATE.format("met_p4->Et()/1000."),
}


# - - - - multijet trigger for FFs multijet CR
MULTI_JET_TRIGGER = ROOT.TCut("(run_number<288000 && HLT_4j85) || ((run_number>288000 && HLT_4j100))")


##-------------------------------------------------------------------------------------------
## - - helper to reterive the overall trigger selectio
##-------------------------------------------------------------------------------------------
def get_trigger(channel, dtype="MC", data_streams=("2015", "2016")):
    """trigger should be unique per data taking year (stream),
    it could lso different for DATA and MC.
    """
    trigger_string = "||".join((TRIGGERS[channel][dtype][st] for st in data_streams))
    return ROOT.TCut(trigger_string)
                                                    
