import logging, warnings
import os


# - - - - - - - - setup logging
logging.basicConfig()

logging.addLevelName(
    logging.INFO, "\033[1;94m%s\033[1;0m" % logging.getLevelName(logging.INFO))
logging.addLevelName(
    logging.DEBUG, "\033[1;51m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
logging.addLevelName(
    logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
logging.addLevelName(
    logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

log = logging.getLogger(__name__)
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)
if hasattr(logging, 'captureWarnings'):
    logging.captureWarnings(True)
    

# - - - - - - - - Speed things up a bit
# import ROOT
# ROOT.SetSignalPolicy(ROOT.kSignalFast)
# ROOT.gROOT.SetBatch(True)
# log.info("ROOT is in batch mode")
    
warnings.filterwarnings(action='ignore', category=RuntimeWarning,
                        message='creating converter.*' )
warnings.filterwarnings(action="ignore", category=RuntimeWarning,
                        message="no dictionary for.* ")

# - - - - - - - - consts 
NTUPLES_VERSION = "18v01"

# - - - - cache directory 
CACHE_DIR = ".CACHE"

# - - - - MC campagin 
MC_CAMPAIGN = "mc16"

# - - - - energy
YEAR_ENERGY = {
    "2011": 7, "2012": 8 ,
    "2015": 13, "2016": 13, "2017": 13, "2018": 13}

# - - - - cutflow hist (holding metadata )
EVENTS_CUTFLOW_HIST = {"mc15": "h_metadata", "mc16": "h_metadata",}
EVENTS_CUTFLOW_BIN = { "mc15": 8, "mc16": 8}

# - - - - - - - - -
NORM_FIELD = "tau_0_pt"

