"""
config.py
contains a simple class for analysis channel specific settings, 
like selections , variables, weights, etc.
"""
# stdlib
import datetime

# local
from . import variables, categories, weights, systematics
from . import (NTUPLES_PATH, NTUPLES_VERSION, CACHE_DIR, YEAR_ENERGY,
               EVENTS_CUTFLOW_HIST, EVENTS_CUTFLOW_BIN, SIGNAL_MASSES, NORM_FIELD)
from .lumi import LUMI, LUMI_UNCERT, get_lumi_uncert
from .systematics import *
from .categories import *
from .trigger import *
from .weights import *
from .variables import *

from db.datasets import Database
from db.decorators import cached_property

##--------------------------------------------------------------------------------------------------
## 
class Configuration():
    """ simple class for wrapping different analysis configurations.
    assuming variables/categories/weights are all the same for all years.
    """
    def __init__(self, channel, year="2017"):
        self.channel = channel
        self.year = year
        self.cache_dir = CACHE_DIR
        self.ntuples_version = NTUPLES_VERSION
        self.norm_field = NORM_FIELD
    @property
    def variables(self):
        # - - - - - - - - set the year for variables from here
        for var in VARIABLES[self.channel]:
            var.year = self.year
            
        return VARIABLES[self.channel]

    @property
    def trigger(self):
        return TRIGGERS[self.channel][self.year]

    @property
    def weights(self):
        """weights dictionary with keys as weight type 
        and items as a list of weight string
        """
        return WEIGHTS[self.channel][self.year]
    
    @property
    def weight_fields(self):
        """weight fields list
        """
        weight_fields = []
        for wt, wl in WEIGHTS[self.channel][self.year].iteritems():
            for w in wl:
                weight_fields.append(w.name)
        return weight_fields
    
    @property
    def event_total_weight(self):
        """overall weight string for the event
        """
        return "*".join(self.weight_fields)
    
    @property
    def categories(self):
        return CATEGORIES[self.channel][self.year]

    @property
    def systematics(self):
        """common systematics components
        """
        return COMMON_SYSTEMATICS[self.channel][self.year]

    @property
    def data_lumi(self):
        return LUMI[self.year]

    @property
    def energy(self):
        return YEAR_ENERGY[self.year]

    @property
    def ntuples_path(self):
        return NTUPLES_PATH[self.channel][self.year]
    
    @property
    def events_cutflow_hist(self):
        return EVENTS_CUTFLOW_HIST[self.year]
    
    @property
    def events_cutflow_bin(self):
        return EVENTS_CUTFLOW_BIN[self.year]
    

    @property
    def weight_systematics(self):
        return WEIGHT_SYSTEMATICS
    
    @property
    def tauid(self):
        return TauID_MED

    @property
    def signal_masses(self):
        return SIGNAL_MASSES

    @cached_property
    def database(self):
        return Database(
            name="datasets_%s%s"%(self.channel, self.ntuples_version),
            verbose=False)
    
    @property
    def hists_file(self):
        return "hists/HISTS_%s_%s.root"%(self.channel, datetime.datetime.today().strftime("%Y_%m_%d"))
