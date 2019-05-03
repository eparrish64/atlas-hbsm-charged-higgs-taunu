""" Utilities for evaluating different inputs for a model from samples distributions to weights, features, ...
"""

## stdlib
import os, time

## PyPI
import numpy as np 
import pandas as pd

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
##--------------------------------------------------------------------------
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