""" various optimization utilities are put together here. 
"""

## stdlib
import os, time 

## PyPI
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier

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
def optimize_model(model, X_train=None, Y_train=None, X_weight=None, param_grid={},
                outdir="", weight_sample=False, save_model=True, validation_plots=False):
    """ Tune model's hyper parameters and return the best performing alongside the model.
    Parameters
    ----------
    see train_model() 
    """

    if X_train is None:
        X_train = model.X_train
    if X_weight is None:    
        X_weight = model.X_weight
    if Y_train is None:        
        Y_train = model.Y_train 

    gb_clf = GradientBoostingClassifier()

    # parameters to be passed to the estimator's fit method (gb_clf)
    fit_params = {"sample_weight": X_weight if weight_sample else None}

    # run grid search
    grid_search = GridSearchCV(
        gb_clf, param_grid=param_grid, fit_params=dict(fit_params), cv=3, n_jobs=N_OPT_CORES, verbose=3, scoring="roc_auc",  return_train_score=False)
    start = time.time()
    grid_search.fit(X_train, Y_train)

    print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
        % (time.time() - start, len(grid_search.cv_results_['params'])))

    report_name = os.path.join(outdir, model.name.replace(".pkl", "_HyperParams.TXT"))
    with open(report_name, "w") as rfile:
        rfile.write("%s\n"%model.name.replace(".pkl", ""))
        rfile.write(report(grid_search.cv_results_))

    return grid_search.cv_results_

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

            "UP_DOWN":{},
            "SINGLE":{
                "80to80": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "90to90": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "100to100": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "110to110": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "120to120": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "130to130": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "140to140": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "150to150": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "160to160": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "170to170": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "180to180": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "190to190": {'n_estimators': 80, 'learning_rate': 0.1, 'max_depth':8, 'min_samples_leaf':0.005, 'min_samples_split':0.02},
                "200to200": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "225to225": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "250to250": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "275to275": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "300to300": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "350to350": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "400to400": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.002, 'min_samples_split':0.01},
                "500to500": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.001, 'min_samples_split':0.01},
                "600to600": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.001, 'min_samples_split':0.01},
                "700to700": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.001, 'min_samples_split':0.01},
                "800to800": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.001, 'min_samples_split':0.01},
                "900to900": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.001, 'min_samples_split':0.01},
                "1000to1000": {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth':10, 'min_samples_leaf':0.001, 'min_samples_split':0.01},
                "1200to1200": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1400to1400": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1600to1600": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "1800to1800": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "2000to2000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "2500to2500": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
                "3000to3000": {'n_estimators': 200, 'learning_rate': 0.1, 'max_depth':20, 'min_samples_leaf':0.001, 'min_samples_split':0.002},
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

            "UP_DOWN":{},
            "SINGLE":{},

        },
    }

    print  mass_range[0] 
    print mass_range[-1]
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

