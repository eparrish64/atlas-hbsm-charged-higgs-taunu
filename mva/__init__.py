## stdlib
import re

## PyPI
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

## local
from hpana.samples.higgs import Higgs
from hpana.variables import CLF_FEATURES

##----------------------------------------------------------------------------------
## consts
##----------------------------------------------------------------------------------
N_TRACKS = [1]
FOLD_CUT_STR = "event_number%{0}!={1}"

## - - complete list of training features irrespective of the mass region (to get a complete Dataframe for training)
ALL_FEATS = {"taujet": [], "taulep": []}
for channel in ["taujet", "taulep"]:
    for region, rg_feats in CLF_FEATURES[channel].iteritems():
        for ft in rg_feats:
            if not ft.name in [f.name for f in ALL_FEATS[channel]]:
                ALL_FEATS[channel] += [ft] 

## - - list of branches to be cached for training 
BRANCHES = {"taujet": ["event_number", "tau_0_n_charged_tracks"], "taulep": ["event_number", "tau_0_n_charged_tracks"] }
for channel in ["taujet", "taulep"]:
     BRANCHES[channel] += [ft.tformula for ft in ALL_FEATS[channel]]

## different training mass bins 
TRAINING_MASS_BINS = {
    # as of 2015+2016 legacy analysis --> optimized binning given the limited stat
    "NOM": [     
        (80, 90, 100, 110, 120), #< low mass 
        (130, 140, 150, 160), #< int mass I
        (170, 180, 190), #< int mass II
        (200, 225, 250, 275, 300, 350, 400), #< high mass I
        tuple(range(500, 1100, 100) + range(1200, 2200, 200) + [2500, 3000]), #< high mass II
        ],   
    # one mass point above and one blow --> no discontinuity in training bins 
    #ak"UP_DOWN": [(80, 90, 100), (2000, 2500, 3000)] + [tuple(Higgs.MASSES[cnt-1:cnt+2]) for cnt in range(len(Higgs.MASSES))[3:-2]],
    "UP_DOWN": [(80, 90), (2500, 3000)] + [tuple(Higgs.MASSES[cnt-1:cnt+2]) for cnt in range(len(Higgs.MASSES))[0:-1]],

    # train per mass point 
    "SINGLE": [(m,) for m in Higgs.MASSES],

    "ALT": [     
        (80, 90, 100, 110, 120, 130, 140, 150, 160), #< low mass 
        (170, 180, 190, 200, 225, 250, 275, 300, 350, 400), #< int mass + high mass I
        tuple(range(500, 1100, 100)), 
        tuple(range(1200, 2200, 200) + [2500, 3000]), #< high mass II
    ], 

} 

## - - Hyperparameters for GradientBoosting 
GB_HYPERPARAMS = {
    # "loss": ["deviance", "exponential"],
    "learning_rate": [0.1, 0.2],
    "n_estimators":[100, 200,], 
    "min_samples_leaf": [0.01, 0.02],
    "max_depth": [10, 15],
}

## cores for GridSearch hyperparams optimization 
N_OPT_CORES = 48

BDT_FILE_PATTERN = re.compile(
    '^(?P<name>\w+)'
    '_(?P<mass>\w+)'
    '_rem_(?P<rem>\d+)'
    '_mod_(?P<mod>\d+)'
    '(?P<prong>\w+)'
    '\.(?P<suffix>\w+)$')
    
XML_FILE_PATTERN = re.compile(
    "^(?P<name>\w+)"
    "_(?P<mass>(\d+to\d+))"
    "_ntracks_(?P<ntracks>\d+)"
    "_nfolds_(?P<nfolds>\d)"
    "_fold_(?P<fold>\d)"
    "(\.weights\.xml)$"
)
PKL_FILE_PATTERN = re.compile(
    "^(model_)"
    "(?P<name>\w+)"
    "_channel_(?P<channel>\w+)"
    "_mass_(?P<mass>\w+)"
    "_ntracks_(?P<ntracks>\d+)"
    "_nfolds_(?P<nfolds>\d)"
    "_fold_(?P<fold>\d)"
    "_nvars_(?P<nvars>\d+)"
    "(\.pkl)$"
)
