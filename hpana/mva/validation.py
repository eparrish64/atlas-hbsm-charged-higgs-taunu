""" Utilities for evaluating different inputs for a model from samples distributions to weights, features, ...
"""

## stdlib
import os, time

## PyPI
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_curve, auc
from sklearn.feature_selection import RFECV

#ak
from os import environ
# #environ['KERAS_BACKEND'] = 'theano'
# environ['KERAS_BACKEND'] = 'tensorflow'
# # Set architecture of system (AVX instruction set is not supported on SWAN)
# environ['THEANO_FLAGS'] = 'gcc.cxxflags=-march=corei7'
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.regularizers import l2
# from keras import initializers
# from keras.optimizers import SGD
# from keras.wrappers.scikit_learn import KerasClassifier
#ak

## local
from hpana.mva import plt 
from hpana import log


##--------------------------------------------------------------------------
## plot signal samples distribution  
##--------------------------------------------------------------------------
def plot_sig_dist(sdframe, signals=[], outdir=".", outname=None, formats=["png", "pdf", "eps"]):
    """Given signals DataFrame plot # events distribution per mass. 
    """
    dist = []
    masses = []
    for sig in signals:
        sd = sdframe.loc[[sig.name]]
        dist += [sd.shape[0]]
        masses += [sig.mass]

    fig, ax = plt.subplots()
    ax.scatter(np.array(masses), np.array(dist))
    ax.set(xlabel='mass(GeV)', ylabel=' # of events',
        title='Signlas Distribution')
    ax.grid()

    ## save the plot
    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)
    if outname is None:        
        outname = os.path.join(outdir, "Signals_events_distribution")
    for fmt in formats:
        log.info("Saving %s ..."%(outname+"."+fmt))
        plt.savefig(outname+"."+fmt, format=fmt, dpi=600)

    plt.close()

def plot_bkg_dist(bdframe, backgrounds=[], outdir=".", outname=None, formats=["png", "pdf", "eps"]):
    names = []
    sizes = []

    for bkg in backgrounds:
        thisbkg = bdframe.loc[[bkg.name]]
        names.append(bkg.name)
        sizes.append(thisbkg.shape[0])

    sizeDF = pd.DataFrame(data={"Names": names, "Sizes": sizes})

    fig, ax = plt.subplots()
    sizeDF.plot(kind="bar",x="Names",y="Sizes",ax=ax,rot=0,logy=True,stacked=True,sort_columns=True,legend=False)
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.01))

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.5, 0.95, "Total: %s Events" %(sum(sizes)), transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    ax.set(xlabel="Sample Name", ylabel=" # of events", title="Background Distribution")
    # ax.grid()
    # fig.savefig('TESTING.png')

    ## save the plot
    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)
    if outname is None:        
        outname = os.path.join(outdir, "Background_events_distribution")
    for fmt in formats:
        log.info("Saving %s ..."%(outname+"."+fmt))
        plt.savefig(outname+"."+fmt, format=fmt, dpi=600)

    plt.close()




##--------------------------------------------------------------------------
## plot samples weight distribution  
##--------------------------------------------------------------------------
def plot_weights(dframe, bins=None, outdir=".", outname=None, formats=["png", "pdf", "eps"]):
    """Given signals DataFrame plot # events distribution per mass. 
    """

    sig_df = dframe.loc[dframe["class_label"]==1]
    bkg_df = dframe.loc[dframe["class_label"]==0]

    s_weight = sig_df["weight"].values 
    b_weight = bkg_df["weight"].values

    if bins is None:
        bins = np.linspace(-10, 10, 100)

    fig, ax = plt.subplots()
    ax.hist([s_weight, b_weight], bins, log=True, histtype="step", label=[r"$\sum SIG$", r"$\sum BKG$"])
    ax.set(xlabel='total event weight', ylabel=' # of events',
        title='Weights Distribution')

    axes = plt.gca()
    axes.set_xlim([-10,10])
    plt.legend(loc='best')

    ## save the plot
    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)
    if outname is None:        
        outname = os.path.join(outdir, "CLF_weights_distribution") 
    for fmt in formats:
        log.info("Saving %s ..."%(outname+"."+fmt))
        plt.savefig(outname+"."+fmt, format=fmt, dpi=600)
    plt.close()


##--------------------------------------------------------------------------
## plot feature importance 
##--------------------------------------------------------------------------
def features_ranking(model, features=None, plot=True, outdir="./", formats=["png", "pdf", "eps"]):
    """ get features ranking for a trained model and plot them.
    """

    if features is None:
        features = model.features

    importance = model.feature_importances_
    importance = pd.DataFrame(importance, index=[ft.name for ft in features], 
                            columns=["Importance"])


    importance["Std"] = np.std([tree[0].feature_importances_
                                for tree in model.estimators_[10:]], axis=0)

    ## get the labels                                    
    x = range(model.n_features_) 
    labels = []
    for ft in features:
        if ft.latex:
            title = ft.latex
        else:
            title = ft.name
        labels += [title]


    y = importance.ix[:, 0]
    yerr = importance.ix[:, 1]

    plt.figure(10)
    bars = plt.barh(x, y, yerr=yerr, align="center", tick_label=labels)

    ## automatize bar colors depending on the size 
    for ft_imp, b in zip(model.feature_importances_, bars):
        if ft_imp > 0.2:
            b.set_color("orangered")
        elif ft_imp > 0.15:
            b.set_color("salmon")
        elif ft_imp > 0.1:
            b.set_color("orange")

    plt.gcf().subplots_adjust(left=0.27)
    plt.xlabel("Gini Importance")

    ## set plot title based on the mass region that the model is trained on
    masses = model.name.split("_")[5].split("to")
    if len(masses) > 1:
        mtag =r"$ %s \leq m_{H^+} \leq %s [GeV]$"%(masses[0], masses[1])
    elif masses:
        mtag = masses[0]                
    else:
        mtag = "..."        
    p_title = "Training Region: %s"%mtag
    plt.title(p_title)

    ## save the plot
    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)
    outname = os.path.join(outdir, "feature_importance_%s"%model.name.replace(".pkl", "")) 
    for fmt in formats:
        log.info("Saving %s ..."%(outname+"."+fmt))
        plt.savefig(outname+"."+fmt, format=fmt, dpi=600)

    plt.close()

##--------------------------------------------------------------------------
## plot feature importance 
def features_correlation(model, 
    train_data=None, features=None, outdir="./", outname=None, title="", formats=["png", "pdf", "eps"]):
    """
    Get the correlation matrix for the input features & target.
    
    Parameters
    ----------
    train_data: pandas data frame; training samples
    
    features: list; train features/+target
    outdir: str; path for the plots

    Return
    ------
    None
    """
    if features is None:
        features =  model.features
    if train_data is None:
        train_data = model.train_df

    X_train = train_data[[ft.name for ft in features]]    
    
    corr_matrix = X_train.corr()

    fig, ax1 = plt.subplots(ncols=1, figsize=(10,8))
    opts = {'cmap': plt.get_cmap("RdBu"),
            'vmin': -1, 'vmax': +1}
        
    heatmap1 = ax1.pcolor(corr_matrix, **opts)
    plt.colorbar(heatmap1, ax=ax1)
    if title:
       ax1.set_title(title) 
    
    ## set the lables 
    labels = corr_matrix.columns.values
    titles = []
    for ft in features:
        if ft.latex:
            title = ft.latex
        else:
            title = ft.name
        titles += [title]

    for ax in (ax1,):
        # shift location of ticks to center of the bins
        ax.set_xticks(np.arange(len(labels))+1., minor=False)
        ax.set_yticks(np.arange(len(labels))+0.5, minor=False)
        ax.set_xticklabels(titles, minor=False, ha='right', rotation=70)
        ax.set_yticklabels(titles, minor=False)

    ## add margin for the labels 
    plt.gcf().subplots_adjust(left=0.2, bottom=0.2)

    ## save the plot 
    if outname is None:
        outname = "features_correlation_%s"%model.name.replace(".pkl", "")
    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)
    outname = os.path.join(outdir, outname)
    for fmt in formats:
        log.info("Saving %s ..."%(outname+"."+fmt))
        plt.savefig(outname+"."+fmt, format=fmt, dpi=600)

    plt.close()

##--------------------------------------------------------------------------
## plot feature importance 
def select_features(features, 
    train_data=None, kfolds=5, hyper_params={}, outdir="./", suffix="", title="", formats=["png", "pdf", "eps"]):
    """A recursive feature elimination example with automatic tuning of the number of features selected with cross-validation.
    """

    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)

    X_train = train_data[[ft.name for ft in features]]
    Y_train = train_data["class_label"]    

    model = GradientBoostingClassifier(**hyper_params)

    ## The "accuracy" scoring is proportional to the number of correct
    rfecv = RFECV(estimator=model, step=1, cv=StratifiedKFold(kfolds), scoring='accuracy', n_jobs=-1)
    rfecv.fit(X_train, Y_train)

    print("Optimal number of features : %d" % rfecv.n_features_)

    print rfecv.ranking_
    print rfecv.support_
    print rfecv.grid_scores_

    ## Plot number of features VS. cross-validation scores
    plt.figure()
    plt.xlabel("Number of features selected")
    plt.ylabel("Accuracy ")
    plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
    plt.title(title)

    ## save plot
    outname = "Features_selection"+suffix
    outname = os.path.join(outdir, outname)
    for fmt in formats:
        log.info("Saving %s ..."%(outname+"."+fmt))
        plt.savefig(outname+"."+fmt, format=fmt, dpi=120)
        
    plt.close()

    return 

##--------------------------------------------------------------------------
## check if model is overfitted 
def check_overfitting(features, 
    train_data=None, 
    base_params={}, 
    hyper_params={}, 
    test_size=0.2, 
    check_tree_depth=False,
    check_min_samples_leaf=False,
    check_min_samples_split=False,
    check_num_trees=False,
    max_depths=np.linspace(1, 32, 32),
    min_samples_splits=np.linspace(0.01, 1.0, 20),
    min_samples_leafs=np.linspace(0.01, 0.1, 10),
    num_trees=range(20, 210, 10),
    outdir="./", 
    suffix="",
    title="", 
    formats=["png"]):

    """ With AUC (Area Under Curve) as the evaluation metric, over/under fitting is checked
    1) max_depth
        The first parameter to tune is max_depth. This indicates how deep the tree can be. 
        The deeper the tree, the more splits it has and it captures more information about the data.
    2) min_samples_split
        min_samples_split represents the minimum number of samples required to split an internal node. 
        This can vary between considering at least one sample at each node to considering all of the samples at each node. 
        When we increase this parameter, the tree becomes more constrained as it has to consider more samples at each node. 

    3) min_samples_leaf
        min_samples_leaf is The minimum number of samples required to be at a leaf node. 
        This parameter is similar to min_samples_splits, however, 
        this describe the minimum number of samples of samples at the leafs, the base of the tree.

    4) number_of_trees

    """

    if not os.path.isdir(outdir):
        os.system("mkdir -p %s"%outdir)

    X_train = train_data[[ft.name for ft in features]]
    Y_train = train_data["class_label"]    

    ## split train and test sets 
    x_train, x_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=test_size)


    ## 1) max_depth
    if check_tree_depth:
        log.info("Checking Tree depth...")
        train_results = []
        test_results = []
        for max_depth in max_depths:
            base_params["max_depth"] = max_depth
            dt = DecisionTreeClassifier(**base_params)
            dt.fit(x_train, y_train)
            train_pred = dt.predict(x_train)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
    
            ## Add auc score to previous train results
            train_results.append(roc_auc)
    
            y_pred = dt.predict(x_test)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)

            ## Add auc score to previous test results
            test_results.append(roc_auc)

        line1, = plt.plot(max_depths, train_results, "b", label="Train AUC")
        line2, = plt.plot(max_depths, test_results, "r", label="Test AUC")
        plt.legend(loc="best") 
        plt.ylabel("AUC score")
        plt.xlabel("Tree depth")
        plt.title(title) 

        ## save the plot 
        outname = os.path.join(outdir, "Tree_depth"+suffix)
        for fmt in formats:
            log.info("Saving %s ..."%(outname+"."+fmt))
            plt.savefig(outname+"."+fmt, format=fmt, dpi=120)
            
        plt.close()

    ## 2) min_samples_split 
    if check_min_samples_split:
        log.info("Checking min samples fraction per split...")

        train_results = []
        test_results = []
        for min_samples_split in min_samples_splits:
            base_params["min_samples_split"] = min_samples_split
            dt = DecisionTreeClassifier(**base_params)
            dt.fit(x_train, y_train)
            train_pred = dt.predict(x_train)
            
            false_positive_rate, true_positive_rate, thresholds =  roc_curve(y_train, train_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            train_results.append(roc_auc)
            
            y_pred = dt.predict(x_test)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            test_results.append(roc_auc)

        line1, = plt.plot(min_samples_splits, train_results, "b", label="Train AUC")
        line2, = plt.plot(min_samples_splits, test_results, "r", label="Test AUC")
        plt.legend(loc="best")
        plt.ylabel("AUC score")
        plt.xlabel("Min samples split")
        plt.title(title) 

        ## save the plot 
        outname = os.path.join(outdir, "Min_samples_split"+suffix)
        for fmt in formats:
            log.info("Saving %s ..."%(outname+"."+fmt))
            plt.savefig(outname+"."+fmt, format=fmt, dpi=120)
            
        plt.close()

    ## 3) min_samples_leaf
    if check_min_samples_leaf:
        log.info("Checking min samples fraction per leaf...")
        train_results = []
        test_results = []
        for min_samples_leaf in min_samples_leafs:
            base_params["min_samples_leaf"] = min_samples_leaf
            dt = DecisionTreeClassifier(**base_params)
            dt.fit(x_train, y_train)
            
            train_pred = dt.predict(x_train)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            train_results.append(roc_auc)
            
            y_pred = dt.predict(x_test)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            test_results.append(roc_auc)

        line1, = plt.plot(min_samples_leafs, train_results, "b", label="Train AUC")
        line2, = plt.plot(min_samples_leafs, test_results, "r", label="Test AUC")

        plt.legend(loc="best")
        plt.ylabel("AUC score")
        plt.xlabel("Min samples leaf")
        plt.title(title) 

        outname = os.path.join(outdir, "Min_samples_leaf"+suffix)
        for fmt in formats:
            log.info("Saving %s ..."%(outname+"."+fmt))
            plt.savefig(outname+"."+fmt, format=fmt, dpi=120)            
        plt.close()

    ## 4) check numbr of estimators for ensemble classifier (GradientBoosting here)
    if check_num_trees:
        log.info("Checking number of estimators for the ensemble classifier...")
        train_results = []
        test_results = []
        for ntree in num_trees:
            hyper_params.update(base_params)
            hyper_params["n_estimators"] = ntree
            gb = GradientBoostingClassifier(**hyper_params)
            gb.fit(x_train, y_train)
            
            train_pred = gb.predict(x_train)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            train_results.append(roc_auc)
            
            y_pred = gb.predict(x_test)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            test_results.append(roc_auc)

        line1, = plt.plot(num_trees, train_results, "b", label="Train AUC")
        line2, = plt.plot(num_trees, test_results, "r", label="Test AUC")

        plt.legend(loc="best")
        plt.ylabel("AUC score")
        plt.xlabel("Number of Trees")
        plt.title(title) 

        outname = os.path.join(outdir, "Number_of_trees"+suffix)
        for fmt in formats:
            log.info("Saving %s ..."%(outname+"."+fmt))
            plt.savefig(outname+"."+fmt, format=fmt, dpi=120)            
        plt.close()


    return 
