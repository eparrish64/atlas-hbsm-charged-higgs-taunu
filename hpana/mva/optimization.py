""" various optimization utilities are put together here. 
"""

## stdlib
import os, time 

## PyPI
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np

## local 
from hpana import log
from hpana.mva import GB_HYPERPARAMS, N_OPT_CORES
from hpana.mva import plt

##--------------------------------------------------------------------------
# utility function to report best scores
##--------------------------------------------------------------------------
def report(results, n_top=50):
    r_str = ""
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            r_str += ("--"*50 +"\n")
            r_str += ("Model with rank: {0}\n".format(i))
            r_str += ("Mean validation score: {0:.3f} (std: {1:.3f})\n".format(
                  results['mean_test_score'][candidate], results['std_test_score'][candidate]))
            r_str += ("Mean training time: {0:.2f} [min]\n".format(results['mean_fit_time'][candidate]))                  
            r_str += ("Parameters: {0}\n".format(results['params'][candidate]))
    print r_str
    return r_str

##--------------------------------------------------------------------------
## utility function for optimizing hyprparameters of a model
##--------------------------------------------------------------------------
def optimize_model(model, train_df=None, X_weight=None, param_grid={},
                outdir="", weight_sample=False, save_model=True, validation_plots=False, features=[], balanced=False):
    """ Tune model's hyper parameters and return the best performing alongside the model.
    Parameters
    ----------
    see train_model() 
    """

    # if X_train is None:
    #     X_train = model.X_train
    # if X_weight is None:    
    #     X_weight = model.X_weight
    # if Y_train is None:        
    #     Y_train = model.Y_train 

    if train_df is None:
        tr_df = model.train_df
    if not features:
        features = model.features
 
    b_df = tr_df[tr_df["class_label"]==0]
    s_df = tr_df[tr_df["class_label"]==1]

    if balanced: 
        ## Set training weight of bkg events to 1. Signal events to N_bkg / N_sig.
        weight_sample = False  
        b_df["BDT_Weight"] = 1
        s_df["BDT_Weight"] = float(b_df.shape[0])/float(s_df.shape[0])
        log.info("Balancing training classes via weights in BDT. Setting signal weights to %s" %(float(b_df.shape[0])/float(s_df.shape[0])))

    else:
        log.info("Unbalanced training classes; signal events:{} | bkg events: {}".format(s_df.shape[0], b_df.shape[0]))

    tr_df_ud = pd.concat([b_df, s_df], axis=0)

    ## - - training arrays
    # print features
    # print tr_df_ud
    X_train = tr_df_ud[[ft.name for ft in features]]
    Y_train = tr_df_ud["class_label"]

    gb_clf = GradientBoostingClassifier()

    # parameters to be passed to the estimator's fit method (gb_clf)
    fit_params = {"sample_weight": X_weight if weight_sample else None}

    # run grid search
    grid_search = GridSearchCV(
        gb_clf, param_grid=param_grid, fit_params=dict(fit_params), cv=5, n_jobs=N_OPT_CORES, verbose=3, scoring="roc_auc",  return_train_score=False)
    start = time.time()
    grid_search.fit(X_train, Y_train)

    print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
        % (time.time() - start, len(grid_search.cv_results_['params'])))

    report_name = os.path.join(outdir, model.name.replace(".pkl", "_HyperParams.TXT"))
    with open(report_name, "w") as rfile:
        rfile.write("%s\n"%model.name.replace(".pkl", ""))
        rfile.write(report(grid_search.cv_results_))

    return grid_search.cv_results_

def get_hparam_grid():
    """
    Returns a list of dictionary entries for all possible hparam combinations.
    """
    import itertools
    keys, values = zip(*GB_HYPERPARAMS.items())
    return [dict(zip(keys,v)) for v in itertools.product(*values)]


##--------------------------------------------------------------------------
## simple hyperparameters handler 
##--------------------------------------------------------------------------
def get_hparams(channel, mass_range=(), bin_scheme="NOM", model_type="GB"):
    """Optimized Hyperparameters for differnet classifiers classifier.

    Parameters
    ----------
    channel: str,
        analysis channel, taujet or taulep
    mass_range: tuple,
        signlas's mass range
    bin_scheme: str,
        mass binning scheme for training classifiers
    model_type: str, 
        classifier type
    """

    ## GradientBoosting 
    hparams_GB = {
        "taujet": {
            "NOM": {
                "80to120": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "130to160": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to190": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "200to400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "500to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
            },

            "ALT": {
                "80to160": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to400": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "500to1000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "1200to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
            },

            "UP_DOWN":{
                "80to90": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "80to100": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "2000to3000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "2500to3000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "100to120": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "110to130": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "120to140": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "130to150": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "140to160": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "150to170": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "160to180": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to190": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "180to200": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "190to225": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "200to250": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "225to275": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "250to300": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "275to350": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "300to400": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "350to500": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "400to600": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "500to700": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "600to800": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "700to900": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "800to1000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "900to1200": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1000to1400": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1200to1600": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1400to1800": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1600to2000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1800to2500": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
            },
            "SINGLE":{
                "80to80": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "90to90": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "100to100": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "110to110": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "120to120": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "130to130": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "140to140": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "150to150": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "160to160": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to170": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "180to180": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "190to190": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "200to200": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "225to225": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "250to250": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "275to275": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "300to300": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "350to350": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "400to400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "500to500": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "600to600": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "700to700": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "800to800": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "900to900": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1000to1000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1200to1200": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1400to1400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1600to1600": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1800to1800": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "2000to2000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "2500to2500": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "3000to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},},
            "ALL":{
                "80to3000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
            },

        },
        "taulep": {
            "NOM": {
                "80to120": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "130to160": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to190": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "200to400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "500to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
            },

            "ALT": {
                "80to160": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "500to1000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "1200to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
            },

            "UP_DOWN":{
                "80to90": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "80to100": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "90to110": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "100to120": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "110to130": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "120to140": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "130to150": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "140to160": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "150to170": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "160to180": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to190": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "180to200": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "190to225": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "200to250": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "225to275": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "250to300": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "275to350": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "300to400": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "350to500": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "400to600": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "500to700": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "600to800": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "700to900": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "800to1000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "900to1200": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1000to1400": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1200to1600": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1400to1800": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1600to2000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "1800to2500": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "2000to3000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "2500to3000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
            },
            "SINGLE":{
                "80to80": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "90to90": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "100to100": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "110to110": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "120to120": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "130to130": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "140to140": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "150to150": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "160to160": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "170to170": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "180to180": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "190to190": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':12, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
                "200to200": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "225to225": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "250to250": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "275to275": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "300to300": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "350to350": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "400to400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.002, 'min_samples_split':0.004},
                "500to500": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "600to600": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "700to700": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "800to800": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "900to900": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1000to1000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1200to1200": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1400to1400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1600to1600": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1800to1800": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "2000to2000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "2500to2500": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "3000to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
            },
            "ALL":{
                "80to3000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.005, 'min_samples_split':0.01},
            },
        },
    }

    mtag = "%ito%i"%(mass_range[0], mass_range[-1])
    if model_type=="GB":
        if not bin_scheme in hparams_GB[channel]:
            log.warning("Hyperparameters are not tuned for %s binning scheme, trying the NOM one ..."%bin_scheme)
            bin_scheme = "NOM"
        if mtag in hparams_GB[channel][bin_scheme]:
            return hparams_GB[channel][bin_scheme][mtag]
        else:
            log.warning("Hyperparameters are not tuned for %s mass range, use another range plz"%mtag)

    else:
        raise RuntimeError("Hyperparameters for classifier of type %s are not tuned yet!"%model_type)
