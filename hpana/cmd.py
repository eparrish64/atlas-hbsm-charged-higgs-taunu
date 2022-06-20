# PYTHON_ARGCOMPLETE_OK

# stdlib
import os, sys
from argparse import ArgumentParser
import multiprocessing
import argcomplete
__all__ = [
    "get_base_parser",
    "get_ana_parser",
    "get_plotting_parser",
    "get_yields_parser",
]

##--------------------------------------------------------------------------------------------------
## base parser
def get_base_parser():

    base_parser = ArgumentParser("hpana cmd parser")

    base_parser.add_argument("--log", "-l",
                        choices=["VERBOSE", "DEBUG", "INFO", "WARNING", "ERROR"], default="INFO")

    base_parser.add_argument("--year", "-y", type=str, choices=("2017", "2018", "2016"), default="2018",
                        help="analysis year, should match the db/samples/<CHANNEL>/YEAR samples you want to use")

    base_parser.add_argument("--channel", "-c", choices=("taujet", "taulep"), default="taujet",
                        help="analysis channel")

    base_parser.add_argument("--mc-campaign", "-mcc", type=str, default="mc16",choices=("mc15", "mc16"),
                        help="mc campaign; analysis samples, ntuples branches, etc. might be different among them")

    base_parser.add_argument("--db-version", "-nv", type=str, default="v06P",
                        help="database version; should match the database version you use when creating database")

    base_parser.add_argument("--data-streams", nargs="+", choices=["2015","2016", "2017", "2018",],
                             help="DATA taking years", default=["2015", "2016", "2017", "2018"])
    
    base_parser.add_argument("--fields", nargs="+",
                        help="list of the variables that you want to analyze")

    base_parser.add_argument("--categories", nargs="+",
                        help="list of the categories that you want to analyze")

    base_parser.add_argument("--systematics", nargs="+",
                        help="list of the systematics that you want to analyze")

    base_parser.add_argument("--systs", "-s", action="store_true",
                        help="process systematics")

    base_parser.add_argument("--hists-file", "-hf", type=str,
                        help="read from/write to the histograms")

    return base_parser

##--------------------------------------------------------------------------------------------------
## analysis parser
def get_ana_parser(base_parser=None):
    """
    """
    if not base_parser:
        ana_parser = get_base_parser()
    else:
        ana_parser = base_parser

    ana_parser.add_argument("--no-hist", "-nh", action="store_true",
                            help="do not wite hists to file")

    ana_parser.add_argument("--no-cxx", "-nc", action="store_true",
                            help="do  not compile cxx macros")

    ana_parser.add_argument("--samples", nargs="+",
                            help="list of samples to process")

    ana_parser.add_argument("--cache-ff", action="store_true",
                            help="cache fake factors")
                            
    ana_parser.add_argument("--parallel", action="store_true",
                            help="if you want to do parallel processing")

    ana_parser.add_argument("--ncpu", type=int, default=multiprocessing.cpu_count(),
                            help="how many cores to use")
    
    ana_parser.add_argument("--merge-hists", action="store_true",
                            help="merge histograms")

    ana_parser.add_argument("--frienddir", type=str, default="/eos/home-b/bburghgr/hptaunu/friendfiles-",
                            help="Where to find friend files")

    ana_parser.add_argument("--partial-unblind", action="store_true", help="Partially unblind signal regions with classifier cuts defined in hpana/categories.py")

    ana_parser.add_argument("--outdir", type=str, default="outdir",
                            help="Where to put the processed histograms")

    ana_parser.add_argument("--submitdir", type=str,
                            help="where to put the job scripts. You will launch condor jobs from here.")

    ana_parser.add_argument("--cluster", action="store_true",
                            help="if you want to submit jobs to the cluster")

    ana_parser.add_argument("--local-scratch", type=str, choices=["tmp", "scratch"], default="tmp",
                            help="name of the local scratch disk on the nodes")

    ana_parser.add_argument("--logsdir", type=str, default="logs",
                            help="where to put the log files")
    
    ana_parser.add_argument("--pickled-analysis", type=str, default="ANALYSIS.pkl",
                            help="main analysis object pickled to be shipped to the worker nodes")

    ana_parser.add_argument("--conf-file", type=str, default="config.yml",
                            help="main analysis configuration flags are written to this file")

    ana_parser.add_argument("--dry-run", action="store_true",
                            help="if you just want to see the scripts that will be submitted to the cluster")
    
    ana_parser.add_argument("--rs-manager", type=str,default="CONDOR", choices=["TORQUE", "SLURM", "CONDOR"],
                            help="the resource manager on your cluster")

    ana_parser.add_argument("--rs-project", type=str,default="ctb-stelzer", choices=["ctb-stelzer", "def-doneil"],
                            help="the resource manager on your cluster")

    ana_parser.add_argument("--retry", help="retry failed jobs", action="store_true")

    ana_parser.add_argument('--plots', action="store_true",
                                 help='p plots', )

    ana_parser.add_argument('--fmt', nargs="+", default=["png", "eps", "pdf"],
                                help="format for the plots")

    ana_parser.add_argument('--logy', action="store_true",
                                 help='Y axis in log scale', )

    # - - - - - - - - - parse analysis args
    #argcomplete.autocomplete(ana_parser)

    return ana_parser

##--------------------------------------------------------------------------------------------------
## plot parser
def get_plotting_parser(base_parser=None):
    if not base_parser:
        plotting_parser = get_base_parser()
    else:
        plotting_parser = base_parser
    
    plotting_parser.add_argument('--outdir', '-pd', default="./plots",
                                 help='where to put the plots', )
    
    plotting_parser.add_argument('--no-ratio', action="store_true",
                                 help='dont add ratio plot on the canvas', )
    
    plotting_parser.add_argument('--no-pvalue', action="store_true",
                                 help='if you with to add pvalue info on the plots', )
    
    plotting_parser.add_argument('--backgrounds', action="store_true",
                                 help='plot backgrounds', )
    
    plotting_parser.add_argument('--signals', nargs="+", #action="store_true",
                                 help='signals', )
    
    plotting_parser.add_argument('--fmt', nargs="+", default=["png", "eps", "pdf"],
                                help="format for the plots")

    plotting_parser.add_argument('--logy', action="store_true",
                                 help='Y axis in log scale', )

    plotting_parser.add_argument("--partial-unblind", action="store_true", 
                                 help="Partially unblind signal regions with classifier cuts defined in hpana/categories.py")

    plotting_parser.add_argument("--frienddir", type=str, default="/eos/home-b/bburghgr/hptaunu/friendfiles-",
                            help="Where to find friend files")
    
    plotting_parser.add_argument('--no-data', action="store_true",
                                 help='do NOT plot data', )

    plotting_parser.add_argument('--bdt-only', action="store_true",
                                help='Plot only bdt scores')
    
    plotting_parser.add_argument("--bin-scheme", default="NOM", choices=["NOM", "UP_DOWN", "SINGLE", "ALT", "ALL"], 
                            help="mass binning scheme for training clfs ")
    return plotting_parser

##--------------------------------------------------------------------------------------------------
## yields parser
def get_yields_parser(base_parser=None):

    if not base_parser:
        yields_parser = get_base_parser()
    else:
        yields_parser = base_parser

    yields_parser.add_argument("--cutflow", action="store_true",
                              help="print cutflow table")
    
    yields_parser.add_argument("--yields-table", action="store_true",
                              help="print yields table")
    
    yields_parser.add_argument("--compare", action="store_true",
                              help="compare ntuple versions")

    yields_parser.add_argument("--latex", action="store_true",
                              help="LaTeX formatted table")
    
    yields_parser.add_argument("--samples", nargs="+",
                            help="list of samples to process")

    yields_parser.add_argument("--yfile", default="yields.txt",
                            help="write yields to this file")

    yields_parser.add_argument('--outdir', '-pd', default="./plots",
                                 help='where to put the plots', )

    yields_parser.add_argument('--weighted', action="store_true",
                                 help='Do not weight yields', )
    
    yields_parser.add_argument("--partial-unblind", action="store_true", 
                               help="Partially unblind signal regions with classifier cuts defined in hpana/categories.py")


    yields_parser.add_argument("--frienddir", type=str, default="/eos/home-b/bburghgr/hptaunu/friendfiles-",
                            help="Where to find friend files")

    return yields_parser


##--------------------------------------------------------------------------------------------------
## fake factors parser
def get_ffs_parser(base_parser=None):

    if base_parser:
        ffs_parser = base_parser
    ffs_parser = ArgumentParser("hpana FFs parser")
    
    ffs_parser.add_argument("--log", "-l",
                        choices=["VERBOSE", "DEBUG", "INFO", "WARNING", "ERROR"], default="INFO")
    ffs_parser.add_argument("--db-version",
                        help="database version; should match the database version you use when creating database")

    ffs_parser.add_argument("--data-streams", nargs="+", choices=["2015","2016", "2017", "2018",],
                             help="DATA taking years", default=["2015", "2016"])
    
    ffs_parser.add_argument("--fake-sources", action="store_true",
                              help="what is the source of fake tau")

    ffs_parser.add_argument("--validation-plots", action="store_true",
                              help="get different validation plots")
    
    ffs_parser.add_argument("--eval-rqcd", action="store_true",
                              help="evaluate rQCD")
    
    ffs_parser.add_argument("--samples", nargs="+",
                            help="list of samples to process")
    
    ffs_parser.add_argument("--ffs-cr-cache", default="FFs_CR.yml",
                            help="write CR FFs to this file")
    
    ffs_parser.add_argument("--rqcd-cache", default="FFs_COMBINED.yml",
                            help="write combined FFs to this file")
    
    ffs_parser.add_argument("--ffs-hists-cache", default="FFs_HISTS.pkl",
                              help="cache histograms used for evaluating FFs to this file")

    ffs_parser.add_argument('--pdir', '-pd', default="./ffplots",
                                 help='where to put the plots', )
    ffs_parser.add_argument("--correct-upsilon", "-cu", action="store_true",
                            help="correct upslion distribution for QCD fakes")                                 
    
    ffs_parser.add_argument("--upsilon-correction-cache", "-ucc", default="CorrectUpsilon.cxx", 
                            help= "macro to cache corrected upsilon")
    return ffs_parser

##--------------------------------------------------------------------------------------------------
## met trigger efficiency parser
def get_trig_eff_parser(base_parser=None):
    trig_eff_parser = ArgumentParser("hpana:: MET trig eff parser")
    
    trig_eff_parser.add_argument("--log", "-l",
                        choices=["VERBOSE", "DEBUG", "INFO", "WARNING", "ERROR"], default="INFO")
    
    trig_eff_parser.add_argument("--db-version",
                        help="database version; should match the database version you use when creating database")

    trig_eff_parser.add_argument("--data-streams", nargs="+", choices=["2015","2016", "2017", "2018",],
                             help="DATA taking yeats", default=["2015", "2016"])
    
    trig_eff_parser.add_argument("--pdir", default="trigeff_plots",
                                 help="where to put the plots")

    trig_eff_parser.add_argument("--hists-cache",default="metTrigEff_HISTS.pkl",
                                 help="read all the histograms from the cache")
    
    trig_eff_parser.add_argument("--fit-cache", default="metTrigEff.cxx",
                                 help="cache fit parameters to this")

    trig_eff_parser.add_argument("--parallel", action="store_true",
                            help="if you want to do parallel processing")

    trig_eff_parser.add_argument("--ncpu", type=int, default=multiprocessing.cpu_count(),
                            help="how many cores to use")
    
    trig_eff_parser.add_argument("--dry-run", action="store_true",
                            help="if you just want to see the scripts that will be submitted to the cluster")
    
    return trig_eff_parser


##--------------------------------------------------------------------------------------------------
## base parser
def get_clf_parser(base_parser=None):

    clf_parser = ArgumentParser("hpana clf parser")

    clf_parser.add_argument("--log", "-l",
                        choices=["VERBOSE", "DEBUG", "INFO", "WARNING", "ERROR"], default="INFO")

    clf_parser.add_argument("--channel", "-c", choices=("taujet", "taulep"), default="taujet",
                        help="analysis channel")

    clf_parser.add_argument("--mc-campaign", "-mcc", type=str, default="mc16",choices=("mc15", "mc16"),
                        help="mc campaign; analysis samples, ntuples branches, etc. might be different among them")

    clf_parser.add_argument("--db-version", "-nv", type=str, 
                        help="database version; should match the database version you use when creating database")

    clf_parser.add_argument("--data-streams", nargs="+", choices=["2015","2016", "2017", "2018",],
                             help="DATA taking years", default=["2015", "2016"])
    
    clf_parser.add_argument("--backend", choices=["tmva","sklearn",],
                             help="ML backend", default="sklearn")

    clf_parser.add_argument("--train-bdt", action="store_true",
                            help="train a Boosted Decision Tree")

    clf_parser.add_argument("--optimize-bdt", action="store_true",
                            help="optimize Boosted Decision Tree")
    
    clf_parser.add_argument("--train-data", default=None,
                            help="training data ")
    
    clf_parser.add_argument("--train-nn", action="store_true",
                            help="train a Neural Network")
    
    clf_parser.add_argument("--per-mass", action="store_true",
                            help="train per mass point")
    
    clf_parser.add_argument("--parallel", action="store_true",
                            help="if you want to do parallel processing")

    clf_parser.add_argument("--ncpu", type=int, default=multiprocessing.cpu_count(),
                            help="how many cores to use")

    clf_parser.add_argument("--validation-plots", action="store_true",
                            help="plot some ROC curves to see the training performance")
    
    clf_parser.add_argument("--rank-feats", action="store_true",
                            help="features importance ")
    
    clf_parser.add_argument("--plot-correlations", action="store_true",
                            help="plot features correlation")

    clf_parser.add_argument("--kfolds", type=int, default=5,
                            help="number for folds for k-fold training")
    
    clf_parser.add_argument("--outdir", type=str, default="clfout",
                            help="directory to put the training outputs in")

    clf_parser.add_argument("--submitdir", type=str,
                            help="where to put the job scripts. You will launch condor jobs from here.")

    clf_parser.add_argument("--sig", nargs="+", default=None,
                            help="list of signals")

    clf_parser.add_argument("--bkg", nargs="+", default=None,
                            help="list of bkgs")

    clf_parser.add_argument("--mass-range", nargs=2, default=[80, 3000], 
                            help="signals' mass range")

    clf_parser.add_argument("--bin-scheme", default="NOM", choices=["NOM", "UP_DOWN", "SINGLE", "ALT", "ALL"], 
                            help="mass binning scheme for training clfs ")

    clf_parser.add_argument("--dry-run", action="store_true",
                            help="if you just want to see the scripts that will be submitted to the cluster")
                                
    clf_parser.add_argument("--cluster", action="store_true",
                            help="if you want to submit jobs to the cluster")

    clf_parser.add_argument("--local-scratch", type=str, choices=["tmp", "scratch"], default="scratch",
                            help="name of the local scratch disk on the nodes")

    clf_parser.add_argument("--logsdir", type=str, default="logs",
                            help="where to put the log files")
    
    clf_parser.add_argument("--rs-manager", type=str, default="CONDOR", choices=["TORQUE", "SLURM", "CONDOR"],
                            help="the resource manager on your cluster")

    clf_parser.add_argument("--rs-project", type=str, default="ctb-stelzer", choices=["ctb-stelzer", "def-doneil"],
                            help="the resource manager on your cluster")

    clf_parser.add_argument("--retry", action="store_true",
                            help="retry failed jobs", )
    
    clf_parser.add_argument("--inc-trks", action="store_true",
                            help="train on both 1p and 3p taus ?")

    clf_parser.add_argument("--balanced", action="store_true",
                            help="Balance training classes")

    clf_parser.add_argument("--weight-sample", action="store_true",
                            help="Apply weights (FF, x-sec, lumi, etc) for background samples")

    clf_parser.add_argument("--parse-auc", action="store_true",
                            help="Only parse optimization output txt files")

    clf_parser.add_argument("--plot-sample-size", action="store_true",
                            help="Plot the size (number of events) of background and signal samples")

    return clf_parser

def get_evalclf_parser(base_parser=None):
    if base_parser is None:
        evalclf_parser = get_clf_parser()
    else:
        evalclf_parser = base_parser

    evalclf_parser.add_argument("--year", "-y", type=str, choices=("2017", "2018", "2016"), default="2018",
                        help="analysis year, should match the db/samples/<CHANNEL>/YEAR samples you want to use")

    evalclf_parser.add_argument("--conf-file", type=str, default="config.yml",
                            help="main analysis configuration flags are writen to this file")
    
    evalclf_parser.add_argument('--files', nargs='+', 
                        help='ntuples to create friend files for')

    evalclf_parser.add_argument('--models', '-w', nargs="+",
                            help='path to xml or pickled trained models')

    evalclf_parser.add_argument("--models-path", "-mp", nargs="+",
                                help="directory that holds trained models")

    evalclf_parser.add_argument("--mtype", choices=["keras", "bdt"], default="bdt",
                            help="TMVA Method type")

    evalclf_parser.add_argument("--fields", nargs="+",
                        help="list of the variables that you want to analyze")

    evalclf_parser.add_argument("--categories", nargs="+",
                        help="list of the categories that you want to analyze")

    evalclf_parser.add_argument("--systematics", nargs="+",
                        help="list of the systematics that you want to analyze")

    evalclf_parser.add_argument("--systs", "-s", action="store_true",
                        help="process all systematics")

    evalclf_parser.add_argument("--samples", nargs="+",
                                help="list of samples to process")

    evalclf_parser.add_argument("--merge-hists", action="store_true",
                                help="merge histograms")

    evalclf_parser.add_argument("--friend", action="store_true",
                                help="save clf scores to TTrees in a friend file")

    evalclf_parser.add_argument("--partial-unblind", action="store_true", help="Partially unblind signal regions with classifier cuts defined in hpana/categories.py")

    evalclf_parser.add_argument("--frienddir", type=str, default="/eos/home-b/bburghgr/hptaunu/friendfiles-",
                            help="Where to find friend files when evaluating on the fly")

    evalclf_parser.add_argument("--direct", action="store_true",
                                help="calculate clf scores on the fly")

    evalclf_parser.add_argument("--indirect", action="store_true",
                                help="calculate clf scores via dataframes saved to model pkl files")

    evalclf_parser.add_argument("--plot-scores", action="store_true",
                                help="calculate and plot clf scores directly from np arrays")

    evalclf_parser.add_argument("--pickled-analysis", type=str, default="ANALYSIS.pkl",
                            help="main analysis object pickled to be shipped to the worker nodes")

    evalclf_parser.add_argument("--eval-nn", action="store_true",
                                help="Evaluate the neural net")

    return evalclf_parser
