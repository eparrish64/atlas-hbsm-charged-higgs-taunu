import ROOT

"""
* trigger info; REFERENCE: https://twiki.cern.ch/twiki/bin/view/Atlas/LowestUnprescaled
* up to 302956 this was ICHEP dataset, in the runs 302872 -302956 the
* xe90 trigger became prescaled (~98% or something) so we are using xe90
* until period D4 (302872) and later the xe110; the corresponding
* trigger efficiency in MC is then:
* ((6.11*trigger_EFF_mht90+26.75*trigger_EFF_mht110+3.21*trigger_EFF_lcw70)/36.07)
"""

# ------------------------------------------------------------------
## - -  triggers
# ------------------------------------------------------------------
TRIGGERS = {
    "taujet": {
        "DATA": {
            "2015": "(run_number <= 284484 && HLT_xe70_tc_lcw)",
            "2016": "(run_number > 284484 && HLT_xe90_mht_L1XE50 && run_number <= 302872)||(run_number > 302872 && HLT_xe110_mht_L1XE50)",
            "2017": ("((run_number >= 325713 && run_number <= 328393) && HLT_xe90_pufit_L1XE50)"
                     "|| ((run_number >= 329385 && run_number <= 330470) && HLT_xe100_pufit_L1XE55)"
                     "|| ((run_number >= 330857 && run_number <= 331975) && HLT_xe110_pufit_L1XE55)"
                     "|| ((run_number >= 332303 && run_number <= 340453) && HLT_xe110_pufit_L1XE50)")
        },
        "MC": {  # MAKE SURE THAT TRIGGER AND TRIGGER EFFICIENCY ARE NOT APPLIED ON TOP OF EACH OTHER!
            "2015": "(NOMINAL_pileup_random_run_number <= 284484 && HLT_xe70_tc_lcw)",
            "2016": ("(NOMINAL_pileup_random_run_number > 284484 && HLT_xe90_mht_L1XE50 && NOMINAL_pileup_random_run_number <= 302872)"\
                     "||(NOMINAL_pileup_random_run_number > 302872 && HLT_xe110_mht_L1XE50 && NOMINAL_pileup_random_run_number <= 311481)"),
            "2017": ("((NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 328393) && HLT_xe90_pufit_L1XE50)"\
                     "|| ((NOMINAL_pileup_random_run_number >= 329385 && NOMINAL_pileup_random_run_number <= 330470) && HLT_xe100_pufit_L1XE55)"\
                     "|| ((NOMINAL_pileup_random_run_number >= 330857 && NOMINAL_pileup_random_run_number <= 331975) && HLT_xe110_pufit_L1XE55)"\
                     "|| ((NOMINAL_pileup_random_run_number >= 332303 && NOMINAL_pileup_random_run_number <= 340453) && HLT_xe110_pufit_L1XE50)")
        },
    },
    "taulep": {
        "DATA": {
            "2015": ("((run_number <= 288000)&&"\
                     "(HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose || HLT_mu20_iloose_L1MU15 || HLT_mu50))"),
            "2016": ("((run_number > 288000)"\
                     "&&(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 ||HLT_mu24_ivarloose||HLT_mu24_ivarmedium || HLT_mu26_ivarmedium || HLT_mu50))"),
            "2017": ("(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium || HLT_mu50)"),
            "2018": ""
        },
        "MC": {
            "2015": ("((run_number <= 288000)"\
                     "&&(HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose || HLT_mu20_iloose_L1MU15 || HLT_mu50))"),
            "2016": ("((run_number > 288000)"\
                     "&&(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium || HLT_mu50))"),
            "2017": ("(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium || HLT_mu50)"),
            "2018": ("")
        },
    },
}

# - - - - multijet + MET trigger for FFs multijet CR
MULTIJET_TRIGGER = {
    "2015": "run_number<288000 && HLT_4j85",
    "2016": "run_number > 288000 && HLT_4j100 && run_number <= 302872",
    "2017": "run_number > 325713 && HLT_4j100"
}

# ------------------------------------------------------------------
# - -  MET triggers for trigger efficiency
# ------------------------------------------------------------------
MET_TRIGGERS = {
    "2015": {
        "HLT_xe70_mht": {  # 2015 (3.2 fb-1)
            "TRIGGER": ROOT.TCut("(run_number <= 284484 && HLT_xe70_mht==1)"),
            "NO_TRIGGER": ROOT.TCut("(run_number <= 284484)"),
            "LUMI": 3.2,
            "RUNS": (266904, 284484),
        },
    },
    "2016": {
        "HLT_xe90_mht_L1XE50": {  # 2016(6.11) up to D3 period
            "TRIGGER": ROOT.TCut("(run_number >= 296939 && (HLT_xe90_mht_L1XE50==1) && run_number <= 302872)"),
            "NO_TRIGGER": ROOT.TCut("(run_number >= 296939 && run_number <= 302872)"),
            "LUMI": 6.11,
            "RUNS": (296939, 302872)
        },
        "HLT_xe110_mht_L1XE50": {  # 2016 (26.75) D4-L periods
            "TRIGGER": ROOT.TCut("(run_number >= 302872 && HLT_xe110_mht_L1XE50==1 && run_number < 311481)"),
            "NO_TRIGGER": ROOT.TCut("(run_number >= 302872 && run_number < 311481)"),
            "LUMI": 26.75,
            "RUNS": (302873, 311480),
        },
    },
    "2017": {
        "HLT_xe90_pufit_L1XE50": {  # period B
            "TRIGGER": ROOT.TCut("(run_number >= 325713 && run_number <= 328393) && HLT_xe90_pufit_L1XE50"),
            "NO_TRIGGER": ROOT.TCut("(run_number >= 325713 && run_number <= 328393)"),
            "LUMI": 5.3687,
            "RUNS": (325713, 328393),
        },
        "HLT_xe100_pufit_L1XE55": {  # priod C
            "TRIGGER": ROOT.TCut("(run_number >= 329385 && run_number <= 330470) && HLT_xe100_pufit_L1XE55"),
            "NO_TRIGGER": ROOT.TCut("(run_number >= 329385 && run_number <= 330470)"),
            "LUMI": 2.3613,
            "RUNS": (329385, 330470),
        },
        "HLT_xe110_pufit_L1XE55": {  # period D1-D5
            "TRIGGER": ROOT.TCut("(run_number >= 330857 && run_number <= 331975) && HLT_xe110_pufit_L1XE55"),
            "NO_TRIGGER": ROOT.TCut("(run_number >= 330857 && run_number <= 331975)"),
            "LUMI": 5.0998,
            "RUNS": (330857, 331975),
        },
        "HLT_xe110_pufit_L1XE50": {  # D6-
            "TRIGGER": ROOT.TCut("(run_number >= 332303 && run_number <= 340453) && HLT_xe110_pufit_L1XE50"),
            "NO_TRIGGER": ROOT.TCut("(run_number >= 332303 && run_number <= 340453)"),
            "LUMI": 31.4773,
            "RUNS": (332303, 340453),
        },
    },
}


# - - - - trigger efficiencies for MC [not applicabel to Fakes and DATA]
TAUJET_EFF_TEMPLATE = "nominal_trig_eff({})"
TRIGGER_EFFICIENCIES = dict()

# - - - - taujet (MAKE SURE YOU GET THE UNITS RIGHT; GeV or MeV)
TRIGGER_EFFICIENCIES["taujet"] = {
    "mc15": TAUJET_EFF_TEMPLATE.format("met_et/1000."),
    "mc16": TAUJET_EFF_TEMPLATE.format("met_p4->Et()"),
}


# -------------------------------------------------------
# - - helper to reterive the overall trigger selection
# -------------------------------------------------------
def get_trigger(channel, dtype="MC", data_streams=("2015", "2016")):
    """trigger should be unique per data taking year (stream),
    it could lso different for DATA and MC.
    """
    assert dtype in ("MC", "DATA"), "choose from (DATA, MC)"

    # do not apply trigger on MC for taujet as the trig efficiency is applied!
    if channel == "taujet" and dtype == "MC":
        trigger_string = ""
    else:
        trigger_string = "||".join(
            (TRIGGERS[channel][dtype][st] for st in data_streams))

    return ROOT.TCut(trigger_string)

# -------------------------------------------------------
# - -
# -------------------------------------------------------
def get_mj_met_trigger(streams, dtype="DATA"):
    """
    combined MJ + MET trigger used in taujet CR for FFs extraction to avoid bias from MET trigger low efficiency.
    """
    if dtype == "MC":
        return ROOT.TCut("")

    trig_string = []
    for st in streams:
        trig_string.append("( ({0}) || ({1}) )".format(
            MULTIJET_TRIGGER[st], TRIGGERS["taujet"]["DATA"][st]))

    trig_string = "||".join(trig_string)
    return ROOT.TCut(trig_string)
