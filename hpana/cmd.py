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

    base_parser.add_argument("--db-version", "-nv", type=str, 
                        help="database version; should match the database version you use when creating database")

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

    ana_parser.add_argument("--local-scratch", type=str, choices=["tmp", "scratch"], default="tmp",
                            help="name of the local scratch disk on the nodes")

    ana_parser.add_argument("--outdir", type=str, default="submitdir",
                            help="where to put the job scripts and the proccessed histograms")

    ana_parser.add_argument("--logsdir", type=str, default="logs",
                            help="where to put the log files")

    ana_parser.add_argument("--pickle-analysis", type=str,
                            help="give a name to pickle the analysis object and save it to that")
    
    ana_parser.add_argument("--pickled-analysis", type=str, default="ANALYSIS.pkl",
                            help="main analysis object pickled to be shipped to the worker nodes")

    ana_parser.add_argument("--cache-ff", action="store_true",
                            help="cache fake factors")
    
    ana_parser.add_argument("--parallel", action="store_true",
                            help="if you want to do parallel processing")

    ana_parser.add_argument("--ncpu", type=int, default=multiprocessing.cpu_count(),
                            help="how many cores to use")
    
    ana_parser.add_argument("--merge-hists", action="store_true",
                            help="merge histograms")

    ana_parser.add_argument("--cluster", action="store_true",
                            help="if you wnat to submit jobs to the cluster")

    ana_parser.add_argument("--dry-run", action="store_true",
                            help="if you just want to see the scripts that will be submitted to the cluster")
    
    ana_parser.add_argument("--rs-manager", type=str,default="TORQUE", choices=["TORQUE", "SLURUM"],
                            help="the resource manager on your cluster")

    
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
    
    plotting_parser.add_argument('--pdir', '-pd', default="./plots",
                                 help='where to put the plots', )
    
    plotting_parser.add_argument('--no-ratio', action="store_true",
                                 help='dont add ratio plot on the canvas', )
    
    plotting_parser.add_argument('--no-pvalue', action="store_true",
                                 help='if you with to add pvalue info on the plots', )
    
    plotting_parser.add_argument('--backgrounds', action="store_true",
                                 help='plot backgrounds', )
    
    plotting_parser.add_argument('--signals', action="store_true",
                                 help='plot signals', )
    
    plotting_parser.add_argument('--logy', action="store_true",
                                 help='Y axis in log scale', )
    
    plotting_parser.add_argument('--no-data', action="store_true",
                                 help='dont plot data', )
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
    
    yields_parser.add_argument("--latex", action="store_true",
                              help="LaTeX formatted table")
    
    yields_parser.add_argument("--samples", nargs="+",
                            help="list of samples to process")
    yields_parser.add_argument("--yfile", default="yields.txt",
                            help="write yields to this file")
    
    return yields_parser


##--------------------------------------------------------------------------------------------------
## fake factors parser
def get_ffs_parser(base_parser=None):

    if not base_parser:
        ffs_parser = get_base_parser()
    else:
        ffs_parser = base_parser

    ffs_parser.add_argument("--cache-cr-ffs", action="store_true",
                              help="cache CR fake factors for the FF CRs")
    
    ffs_parser.add_argument("--cache-rqcd", action="store_true",
                              help="cache combined FFs")
    
    ffs_parser.add_argument("--cache-ffs-hists", action="store_true",
                              help="cache histograms used for evaluating FFs")
    
    ffs_parser.add_argument("--validation-plots", action="store_true",
                              help="get different validation plots")
    
    ffs_parser.add_argument("--eval-rqcd", action="store_true",
                              help="evaluate rQCD")
    
    ffs_parser.add_argument("--samples", nargs="+",
                            help="list of samples to process")
    
    ffs_parser.add_argument("--ffs-cr-cache", default="FF_CR.pkl",
                            help="write CR FFs to this file")
    
    ffs_parser.add_argument("--rqcd-cache", default="FF_rQCD.pkl",
                            help="write combined FFs to this file")
    
    ffs_parser.add_argument("--ffs-hists-cache", default="FF_HISTS.pkl",
                              help="cache histograms used for evaluating FFs to this file")

    ffs_parser.add_argument('--pdir', '-pd', default="./ffplots",
                                 help='where to put the plots', )
    
    return ffs_parser
