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
## REFERENCE: https://atlas-tagservices.cern.ch/tagservices/RunBrowser/runBrowserReport/rBR_Period_Report.php
## https://twiki.cern.ch/twiki/bin/viewauth/Atlas/LowestUnprescaled
TRIGGERS = {
    "taujet": {
        "DATA": {
            "2015": "(run_number <= 284484 && (HLT_xe70_tc_lcw || HLT_xe70_mht))",

            "2016": "(run_number >= 296939 && (HLT_xe90_mht_L1XE50 || HLT_xe80_tc_lcw_L1XE50) && run_number <= 302872)" #<! period A-C
                       "||(run_number > 302872 && HLT_xe110_mht_L1XE50 && run_number < 311481)", #<! period D-

            # "2017": ("((run_number >= 325713 && run_number <= 328393) && HLT_xe90_pufit_L1XE50)" #<! period B (prescaled!)
            #          "|| ((run_number >= 329385 && run_number <= 330470) && HLT_xe100_pufit_L1XE55)" #<! period C (prescaled!)
            #          "|| ((run_number >= 330857 && run_number <= 331975) && HLT_xe110_pufit_L1XE50)" #<! period D1-5 (prescaled!)
            #          "|| ((run_number >= 332303 && run_number <= 340453) && HLT_xe110_pufit_L1XE55)"), #<! D6-K

            ##@NOTE MET trigger option that gives you full luminosity at the cost of a higher threshold (recommended if you prefer not to combine triggers over different data-taking periods) 
# -> PB            "2017": ("((run_number >= 332303 && run_number <= 340453) && HLT_xe110_pufit_L1XE50) ||((run_number >= 325713 && run_number <= 331975) && HLT_xe110_pufit_L1XE55)"),
            "2017": ("((run_number >= 332303 && run_number <= 341649) && HLT_xe110_pufit_L1XE50) ||((run_number >= 325713 && run_number <= 331975) && HLT_xe110_pufit_L1XE55)"),

            "2018": ("( run_number >= 348885 && run_number <= 364485  && HLT_xe110_pufit_xe70_L1XE50)"), #<! period B-
                    #"|| ( run_number >= 355529  && run_number <=364485  && (HLT_xe110_pufit_xe65_L1XE50 || HLT_xe110_pufit_xe70_L1XE50))") #<! period K- 
        },

        "MC": {  # MAKE SURE THAT TRIGGER AND TRIGGER EFFICIENCY ARE NOT APPLIED ON TOP OF EACH OTHER!
# -> PB            "2015": "(NOMINAL_pileup_random_run_number <= 284484 && HLT_xe70_tc_lcw )",
            "2015": "(NOMINAL_pileup_random_run_number <= 284484 && (HLT_xe70_tc_lcw || HLT_xe70_mht))",
            
# -> PB            "2016": ("(NOMINAL_pileup_random_run_number >= 296939 && HLT_xe90_mht_L1XE50 && NOMINAL_pileup_random_run_number <= 302872)"\
            "2016": ("(NOMINAL_pileup_random_run_number >= 296939 && (HLT_xe90_mht_L1XE50 || HLT_xe80_tc_lcw_L1XE50) && NOMINAL_pileup_random_run_number <= 302872)"\
                    "||(NOMINAL_pileup_random_run_number > 302872 && HLT_xe110_mht_L1XE50 && NOMINAL_pileup_random_run_number <= 311481)"),
            
            # "2017": ("((NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 328393) && HLT_xe90_pufit_L1XE50)"\
            #          "|| ((NOMINAL_pileup_random_run_number >= 329385 && NOMINAL_pileup_random_run_number <= 330470) && HLT_xe100_pufit_L1XE55)"\
            #          "|| ((NOMINAL_pileup_random_run_number >= 330857 && NOMINAL_pileup_random_run_number <= 331975) && HLT_xe110_pufit_L1XE55)"\
            #          "|| ((NOMINAL_pileup_random_run_number >= 332303 && NOMINAL_pileup_random_run_number <= 340453) && HLT_xe110_pufit_L1XE50)"),

            ##@NOTE MET trigger option that gives you full luminosity at the cost of a higher threshold (recommended if you prefer not to combine triggers over different data-taking periods) 
# -> PB            "2017": ("((NOMINAL_pileup_random_run_number >= 332303 && NOMINAL_pileup_random_run_number <= 340453) && HLT_xe110_pufit_L1XE50)"\
            "2017": ("((NOMINAL_pileup_random_run_number >= 332303 && NOMINAL_pileup_random_run_number <= 341649) && HLT_xe110_pufit_L1XE50)"\
                    "||((NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 331975) && HLT_xe110_pufit_L1XE55)"),

            "2018": ("( NOMINAL_pileup_random_run_number >= 348885 && NOMINAL_pileup_random_run_number <= 364485  && HLT_xe110_pufit_xe70_L1XE50)"), #<! period B-
                    # "|| ( NOMINAL_pileup_random_run_number >= 355529  && NOMINAL_pileup_random_run_number <=364485  && (HLT_xe110_pufit_xe65_L1XE50 || HLT_xe110_pufit_xe70_L1XE50))") #<! period K- 
        },
    },

    "taulep": {
        "DATA": {
            "2015": ("((run_number <= 288000)&&"\
                     "(HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose || HLT_mu20_iloose_L1MU15))"),
        
            "2016": ("((run_number >= 296939 && run_number <= 311481)"\
                     "&&(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium))"),
        
            "2017": (" run_number >= 325713 && run_number <= 340453 && (HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0 ||HLT_mu26_ivarmedium)"),
        
            "2018": (" run_number >= 348885 && run_number <=364485 && (HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0 ||HLT_mu26_ivarmedium)")
        },

        "MC": {
            "2015": ("((NOMINAL_pileup_random_run_number <= 288000)"\
                     "&&(HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose || HLT_mu20_iloose_L1MU15))"),

            "2016": ("((NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 311481)"\
                     "&&(HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0 || HLT_mu26_ivarmedium))"),

            "2017": (" NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 340453 && (HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0 ||HLT_mu26_ivarmedium)"),
        
            "2018": (" NOMINAL_pileup_random_run_number >= 348885 && NOMINAL_pileup_random_run_number <=364485 && (HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0 ||HLT_mu26_ivarmedium)")
        },
    },
}

# - - - - multijet trigger for FFs multijet CR (@NOTE the MET trig threshold)
MULTIJET_TRIGGER = {
    "DATA":{
        "2015": "(run_number <= 284484 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15))",

        "2016": "(run_number >= 296939 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15) && run_number <=311481)",

        "2017": "(run_number >= 324320 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15) && run_number <=341649)",
        "2018": "(run_number >= 348197 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15) && run_number <= 364485)",
        },

    "MC":{
        "2015": "(NOMINAL_pileup_random_run_number <= 284484 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15))",

        "2016": "(NOMINAL_pileup_random_run_number >= 296939 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15) && NOMINAL_pileup_random_run_number <=311481)",

        "2017": "(NOMINAL_pileup_random_run_number >= 324320 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15) && NOMINAL_pileup_random_run_number <=341649)",
        "2018": "(NOMINAL_pileup_random_run_number >= 348197 && (HLT_4j120  ||HLT_3j175 || HLT_3j200||HLT_3j225||HLT_4j100 || HLT_4j110||HLT_4j85  || HLT_5j60 || HLT_5j70_L14J15 || HLT_5j85 || HLT_5j85_L14J15) && NOMINAL_pileup_random_run_number <= 364485)",
        },
}

# - - - - dilep trigger for taujet DILEP_BTAG  CR
DILEP_TRIGGER = {
    "DATA": {
            "2015": ("((run_number <= 288000)&&"\
                     "((HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose) && HLT_mu20_iloose_L1MU15))"),

            "2016": ("((run_number >= 296939 && run_number <= 311481)"\
                     "&&((HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0) && HLT_mu26_ivarmedium))"),

            "2017": (" run_number >= 325713 && run_number <= 340453 && ((HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0) && HLT_mu26_ivarmedium)"),

            "2018": (" run_number >= 348885 && run_number <=364485 && ((HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0) && HLT_mu26_ivarmedium)")
        },

        "MC": {
            "2015": ("((NOMINAL_pileup_random_run_number <= 288000)"\
                     "&&((HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium || HLT_e120_lhloose) && HLT_mu20_iloose_L1MU15))"),

            "2016": ("((NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 311481)"\
                     "&&((HLT_e26_lhtight_nod0_ivarloose || HLT_e60_lhmedium_nod0 || HLT_e140_lhloose_nod0) && HLT_mu26_ivarmedium))"),

            "2017": (" NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 340453 && ((HLT_e26_lhtight_nod0_ivarloose|| HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0) && HLT_mu26_ivarmedium)"),

            "2018": (" NOMINAL_pileup_random_run_number >= 348885 && NOMINAL_pileup_random_run_number <=364485 && ((HLT_e26_lhtight_nod0_ivarloose || HLT_e140_lhloose_nod0 || HLT_e60_lhmedium_nod0) && HLT_mu26_ivarmedium)")
        },
}



# ------------------------------------------------------------------
# - -  MET triggers for trigger efficiency
# ------------------------------------------------------------------
MET_TRIGGERS = {
    "DATA": {
        "2015": {
            "HLT_xe70_mht": {  # 2015 (3.2 fb-1)
                ###                "TRIGGER": ROOT.TCut("(run_number <= 284484 && HLT_xe70_mht==1)"),
                "TRIGGER": ROOT.TCut("run_number <= 284484 && (HLT_xe70_tc_lcw || HLT_xe70_mht)"),
                "NO_TRIGGER": ROOT.TCut("(run_number <= 284484)"),
                "LUMI": 3.2,
                "RUNS": (266904, 284484),
            },
            # "HLT_xe70_mht": {  # 2015 (3.2 fb-1)
            #     "TRIGGER": ROOT.TCut("(run_number <= 284484 && HLT_xe70_mht==1)"),
            #     "NO_TRIGGER": ROOT.TCut("(run_number <= 284484)"),
            #     "LUMI": 3.2,
            #     "RUNS": (266904, 284484),
            # },
            # "HLT_xe70_tc_lcw": {  # 2015 (3.2 fb-1)
            #     "TRIGGER": ROOT.TCut("(run_number <= 284484 && HLT_xe70_tc_lcw==1)"),
            #     "NO_TRIGGER": ROOT.TCut("(run_number <= 284484)"),
            #     "LUMI": 3.2,
            #     "RUNS": (266904, 284484),
            # },
        },
        "2016": {
            "HLT_xe90_mht_L1XE50": {  # 2016(6.11) up to D3 period
                ###                "TRIGGER": ROOT.TCut("(run_number >= 296939 && (HLT_xe90_mht_L1XE50==1) && run_number <= 302872)"),
                "TRIGGER": ROOT.TCut("(run_number >= 296939 && run_number <= 302872) && (HLT_xe90_mht_L1XE50 || HLT_xe80_tc_lcw_L1XE50)"),
                "NO_TRIGGER": ROOT.TCut("(run_number >= 296939 && run_number <= 302872)"),
                "LUMI": 6.11,
                "RUNS": (296939, 302872)
            },
            # "HLT_xe90_mht_L1XE50": {  # 2016(6.11) up to D3 period
            #     "TRIGGER": ROOT.TCut("(run_number >= 296939 && (HLT_xe90_mht_L1XE50==1) && run_number <= 302872)"),
            #     "NO_TRIGGER": ROOT.TCut("(run_number >= 296939 && run_number <= 302872)"),
            #     "LUMI": 6.11,
            #     "RUNS": (296939, 302872)
            # },
            # "HLT_xe80_tc_lcw_L1XE50": {  # 2016(6.11) up to D3 period
            #     "TRIGGER": ROOT.TCut("(run_number >= 296939 && run_number <= 302872) && (HLT_xe80_tc_lcw_L1XE50==1)"),
            #     "NO_TRIGGER": ROOT.TCut("(run_number >= 296939 && run_number <= 302872)"),
            #     "LUMI": 6.11,
            #     "RUNS": (296939, 302872)
            # },
            "HLT_xe110_mht_L1XE50": {  # 2016 (26.75) D4-L periods
                "TRIGGER": ROOT.TCut("(run_number >= 302872 && run_number < 311481) && HLT_xe110_mht_L1XE50==1"),
                "NO_TRIGGER": ROOT.TCut("(run_number >= 302872 && run_number < 311481)"),
                "LUMI": 26.75,
                "RUNS": (302873, 311481),
            },
        },
        "2017": {
            # "HLT_xe90_pufit_L1XE50": {  # period B
            #     "TRIGGER": ROOT.TCut("(run_number >= 325713 && run_number <= 328393) && HLT_xe90_pufit_L1XE50"),
            #     "NO_TRIGGER": ROOT.TCut("(run_number >= 325713 && run_number <= 328393)"),
            #     "LUMI": 5.3687,
            #     "RUNS": (325713, 328393),
            # },
            # "HLT_xe100_pufit_L1XE55": {  # priod C
            #     "TRIGGER": ROOT.TCut("(run_number >= 329385 && run_number <= 330470) && HLT_xe100_pufit_L1XE55"),
            #     "NO_TRIGGER": ROOT.TCut("(run_number >= 329385 && run_number <= 330470)"),
            #     "LUMI": 2.3613,
            #     "RUNS": (329385, 330470),
            # },
            "HLT_xe110_pufit_L1XE55": {  # period B-D5 (unprescaled)
                "TRIGGER": ROOT.TCut("(run_number >= 325713 && run_number <= 331975) && HLT_xe110_pufit_L1XE55"),
                "NO_TRIGGER": ROOT.TCut("(run_number >= 325713 && run_number <= 331975)"),
                "LUMI": 5.0998,
                # "RUNS": (330857, 331975),
                "RUNS": (325713, 331975),
            },
            "HLT_xe110_pufit_L1XE50": {  # D6-
                "TRIGGER": ROOT.TCut("(run_number >= 332303 && run_number <= 341649) && HLT_xe110_pufit_L1XE50"),
                "NO_TRIGGER": ROOT.TCut("(run_number >= 332303 && run_number <= 341649)"),
                "LUMI": 31.4773,
                "RUNS": (332303, 341649),
            },
        },

        "2018":{
            "HLT_xe110_pufit_xe70_L1XE50":{
                "TRIGGER": ROOT.TCut("(run_number >= 348885 && run_number <= 364485)  && HLT_xe110_pufit_xe70_L1XE50"),
                "NO_TRIGGER": ROOT.TCut("run_number >= 348885 && run_number <= 364485"),
                "LUMI": 58.4502,
                "RUNS":(348885, 364485),
            },
        },
      },


    "MC": {
        "2015": {
            "HLT_xe70_mht": {  # 2015 (3.2 fb-1)
                ###                "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number <= 284484 && HLT_xe70_mht==1)"),
                "TRIGGER": ROOT.TCut("NOMINAL_pileup_random_run_number <= 284484 && (HLT_xe70_tc_lcw || HLT_xe70_mht)"),
                "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number <= 284484)"),
                "LUMI": 3.2,
                "RUNS": (266904, 284484),
            },
            # "HLT_xe70_mht": {  # 2015 (3.2 fb-1)
            #     "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number <= 284484 && HLT_xe70_mht==1)"),
            #     "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number <= 284484)"),
            #     "LUMI": 3.2,
            #     "RUNS": (266904, 284484),
            # },
            # "HLT_xe70_tc_lcw": {  # 2015 (3.2 fb-1)
            #     "TRIGGER": ROOT.TCut("NOMINAL_pileup_random_run_number <= 284484 && (HLT_xe70_tc_lcw==1)"),
            #     "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number <= 284484)"),
            #     "LUMI": 3.2,
            #     "RUNS": (266904, 284484),
            # },
        },
        "2016": {
            "HLT_xe90_mht_L1XE50": {  # 2016(6.11) up to D3 period
               ###                "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && (HLT_xe90_mht_L1XE50==1) && NOMINAL_pileup_random_run_number <= 302872)"),
               "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 302872) && (HLT_xe90_mht_L1XE50 || HLT_xe80_tc_lcw_L1XE50)"),
               "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 302872)"),
               "LUMI": 6.11,
               "RUNS": (296939, 302872)
            },
            # "HLT_xe90_mht_L1XE50": {  # 2016(6.11) up to D3 period
            #     "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && (HLT_xe90_mht_L1XE50==1) && NOMINAL_pileup_random_run_number <= 302872)"),
            #     "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 302872)"),
            #     "LUMI": 6.11,
            #     "RUNS": (296939, 302872)
            # },
            # "HLT_xe80_tc_lcw_L1XE50": {  # 2016(6.11) up to D3 period
            #     "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 302872) && (HLT_xe80_tc_lcw_L1XE50)"),
            #     "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 296939 && NOMINAL_pileup_random_run_number <= 302872)"),
            #     "LUMI": 6.11,
            #     "RUNS": (296939, 302872)
            # },
            "HLT_xe110_mht_L1XE50": {  # 2016 (26.75) D4-L periods
                "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 302872 && NOMINAL_pileup_random_run_number < 311481) && HLT_xe110_mht_L1XE50==1"),
                "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 302872 && NOMINAL_pileup_random_run_number < 311481)"),
                "LUMI": 26.75,
                "RUNS": (302873, 311481),
            },
        },
        "2017": {
            "HLT_xe110_pufit_L1XE55": {  # period B-D5 (unprescaled)
                "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 331975) && HLT_xe110_pufit_L1XE55"),
                "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 325713 && NOMINAL_pileup_random_run_number <= 331975)"),
                "LUMI": 5.0998,
                # "RUNS": (330857, 331975),
                "RUNS": (325713, 331975),
            },
            "HLT_xe110_pufit_L1XE50": {  # D6-
                "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 332303 && NOMINAL_pileup_random_run_number <= 341649) && HLT_xe110_pufit_L1XE50"),
                "NO_TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 332303 && NOMINAL_pileup_random_run_number <= 341649)"),
                "LUMI": 31.4773,
                "RUNS": (332303, 341649),
            },
        },
        "2018": {
            "HLT_xe110_pufit_xe70_L1XE50":{
                "TRIGGER": ROOT.TCut("(NOMINAL_pileup_random_run_number >= 348885 && NOMINAL_pileup_random_run_number <= 364485)  && HLT_xe110_pufit_xe70_L1XE50"),
                "NO_TRIGGER": ROOT.TCut("NOMINAL_pileup_random_run_number >= 348885 && NOMINAL_pileup_random_run_number <= 364485"),
                "LUMI": 58.4502,
                "RUNS":(348885, 364485),
            },
        },

    },

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
    #if channel == "taujet" and dtype == "MC":
    #     trigger_string = ""
    #else:
    trigger_string = "||".join((TRIGGERS[channel][dtype][st] for st in data_streams))

    return ROOT.TCut(trigger_string)

# -------------------------------------------------------
# - -
# -------------------------------------------------------
def get_mj_trigger(streams, dtype="DATA"):
    """
    combined MJ + MET trigger used in taujet CR for FFs extraction to avoid bias from MET trigger low efficiency.
    """

    trig_string = []
    for st in streams:
        trig_string.append("( {0} )".format(MULTIJET_TRIGGER[dtype][st]))

    trig_string = "||".join(trig_string)
    return ROOT.TCut(trig_string)

# -------------------------------------------------------
# - -
# -------------------------------------------------------
def get_dilep_trigger(channel, dtype="MC", data_streams=("2015", "2016")):
    """trigger should be unique per data taking year (stream),
    it could lso different for DATA and MC.
    """
    assert dtype in ("MC", "DATA"), "choose from (DATA, MC)"

    # do not apply trigger for taujet
    if channel == "taujet":
        assert ValueError("Dilep CR is for taulep channel only")
        trigger_string = ""
    else:
        trigger_string = "||".join(
            (DILEP_TRIGGER[dtype][st] for st in data_streams))

    return ROOT.TCut(trigger_string)

