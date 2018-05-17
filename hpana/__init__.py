import logging
import os

import ROOT

log = logging.getLogger('hpana')
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)
if hasattr(logging, 'captureWarnings'):
    logging.captureWarnings(True)

# Speed things up a bit
ROOT.SetSignalPolicy(ROOT.kSignalFast)
ROOT.gROOT.SetBatch(True)
log.info("ROOT is in batch mode")

NTUPLES_PATH = {
    "taujet": {"2017":""}
}

NTUPLES_VERSION = "18v01"
CACHE_DIR = ""

YEAR_ENERGY = {
    "2011": 7, "2012": 8 ,
    "2015": 13, "2016": 13, "2017": 13, "2018": 13}

EVENTS_CUTFLOW_HIST = "h_metadata"
EVENTS_CUTFLOW_BIN = 8

NORM_FIELD = "tau_0_pt"

SIGNAL_MASSES = {
    90: "344287",
    100: "344288",
    110: "344289",
    120: "344290",
    
    130: "344291",
    140: "344292",
    150: "344293",

    160: "344250",
    165: "344251",
    170: "344252",
    175: "344253",
    180: "344254",

    200: "341524",
    225: "341525",
    250: "341526",
    275: "341527",
    300: "341528",
    350: "341529",
    400: "341003",

    500: "341530",
    600: "341531",
    700: "341532",
    800: "341533",
    900: "341534",
    1000: "341535",
    1200: "341536",
    1400: "341537",
    1600: "341538",
    1800: "341539",
    2000: "341540",
}
