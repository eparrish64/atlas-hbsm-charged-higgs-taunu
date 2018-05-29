"""
config.py
contains a simple class for analysis channel specific settings, 
like selections , variables, weights, etc.
"""
# stdlib
import datetime

# local
from . import (MC_CAMPAIGN, NTUPLES_VERSION, CACHE_DIR, YEAR_ENERGY,
               EVENTS_CUTFLOW_HIST, EVENTS_CUTFLOW_BIN, SIGNAL_MASSES, NORM_FIELD)
from .systematics import *
from .categories import *
from .lumi import *
from .trigger import *
from .weights import *
from .variables import *

from samples.data import Data
from db.datasets import Database
from db.decorators import cached_property

##--------------------------------------------------------------------------------------------------
## 
class Configuration:
    """ simple class for wrapping different analysis configurations.
    assuming variables/categories/weights are all the same for all years.
    """
    def __init__(self, channel,
                 mc_campaign=MC_CAMPAIGN,
                 cache_dir=CACHE_DIR,
                 norm_field=NORM_FIELD,
                 ntuples_version=NTUPLES_VERSION,):
        self.channel = channel
        self.cache_dir = cache_dir
        self.ntuples_version = ntuples_version
        self.norm_field = norm_field
        self.mc_camp = mc_campaign

        #FIX ME: tmp fix 
        self.year = "2017"
        if self.mc_camp =="mc15":
            self.year = "2017"
                
                    
    @property
    def variables(self):
        return VARIABLES[self.channel]

    @property
    def trigger(self):
        """trigger should be unique per data taking year (stream)
        """
        trigger_string = "(%s)"%TRIGGERS[self.channel][Data.STREAMS[0]] 
        for stream in Data.STREAMS[1:]:
            trigger_string += " || (%s)"% TRIGGERS[self.channel][stream]

        return ROOT.TCut(trigger_string)
            
    @property
    def weights(self):
        """weights dictionary with keys as weight type 
        and items as a list of weight string
        """
        return WEIGHTS[self.channel]
    
    @property
    def weight_fields(self):
        """weight fields list
        """
        return [w.name for w in WEIGHTS[self.channel]]
    
    @property
    def event_total_weight(self):
        """overall weight string for the event
        """
        return "*".join(self.weight_fields)
    
    @property
    def categories(self):
        return CATEGORIES[self.channel]

    @property
    def systematics(self):
        """common systematics components
        """
        return COMMON_SYSTEMATICS[self.channel][self.mc_camp]

    @property
    def data_lumi(self):
        """ lumi is per data taking year (stream)
        """
        lumi = 0
        for stream in Data.STREAMS:
            try:
                lumi += LUMI[stream]
            except KeyError:
                raise ("failed to get lumi for %s! "%stream)
        return lumi
    
    @property
    def energy(self):
        """ should be the same among different streams.
        """
        stream = Data.STREAMS[0]
        return YEAR_ENERGY[stream]

    @property
    def events_cutflow_hist(self):
        return EVENTS_CUTFLOW_HIST[self.mc_camp]
    
    @property
    def events_cutflow_bin(self):
        return EVENTS_CUTFLOW_BIN[self.mc_camp]
    

    @property
    def weight_systematics(self):
        return WEIGHT_SYSTEMATICS
    
    @property
    def tauid(self):
        return TauID_MED[self.mc_camp]

    @property
    def true_tau(self):
        return TAU_IS_TRUE[self.mc_camp]
    
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

    @property
    def hist_name_template(self):
        return "{0}_category_{1}_{2}" #<! sample name, category name, variable name
