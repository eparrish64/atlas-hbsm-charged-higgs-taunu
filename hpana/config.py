"""
config.py
contains a simple class for analysis channel specific settings, 
like selections , variables, weights, etc.
"""
# stdlib
import datetime, re

# local
from . import (MC_CAMPAIGN, CACHE_DIR, YEAR_ENERGY,
               EVENTS_CUTFLOW_HIST, EVENTS_CUTFLOW_BIN, NORM_FIELD)
from .systematics import *
from .categories import *
from .lumi import *
from .trigger import *
from .weights import *
from .variables import *

##--------------------------------------------------------------------------------------------------
## 
class Configuration:
    """ simple class for wrapping different analysis configurations.
    assuming variables/categories/weights are all the same for all years.
    """
    def __init__(self, channel,
                 year="2018",
                 mc_campaign=MC_CAMPAIGN,
                 cache_dir=CACHE_DIR,
                 norm_field=NORM_FIELD,
                 db_version="18v01",
                 data_streams=("2015", "2016", )):
        self.channel = channel
        self.cache_dir = cache_dir
        self.db_version = db_version
        self.norm_field = norm_field
        self.mc_camp = mc_campaign
        self.data_streams = data_streams
        self.year = year
    
    @property
    def variables(self):
        variables = VARIABLES[self.channel]
        for var in variables:
            var.mc_camp = self.mc_camp
        return variables
    
    def trigger(self, dtype="MC", category=None):
        """trigger should be unique per data taking year (stream),
        it's also different for DATA and MC.
        """
        # - - check if it is a MULTIJET (aka QCD) control region
        if category:
            if ("MULTIJET" in category.name or "QCD" in category.name):
                log.debug("applying multijet trigger for %s category"%category.name)
                return ROOT.TCut(MULTIJET_TRIGGER)
            
        return get_trigger(self.channel, data_streams=self.data_streams, dtype=dtype)
    
    @property
    def weight_fields(self):
        """weight fields list
        """
        return Weight.factory(channel=self.channel, mc_camp=self.mc_camp)
    
    @property
    def event_total_weight(self):
        """overall weight string for the event
        """
        return "*".join(self.weight_fields)
    
    @property
    def categories(self):
        return Category.factory(channel=self.channel, mc_camp=self.mc_camp) + self.ff_cr_regions

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
        for stream in self.data_streams:
            try:
                lumi += LUMI[stream]
            except KeyError:
                raise ("failed to get lumi for %s! "%stream)
        return lumi
    
    @property
    def energy(self):
        """ should be the same among different streams.
        """
        stream = self.data_streams[0]
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
        return TAUID_MEDIUM[self.mc_camp]

    @property
    def antitau(self):
        return ANTI_TAU[self.mc_camp]

    
    @property
    def true_tau(self):
        return TAU_IS_TRUE[self.mc_camp]
    
    @property
    def signal_masses(self):
        return SIGNAL_MASSES

    @property
    def hists_file(self):
        return "HISTS_%s_%s.root"%(self.channel, datetime.datetime.today().strftime("%Y_%m_%d"))

    @property
    def hist_name_template(self):
        return "{0}_category_{1}_var_{2}" #<! sample name, category name, variable name

    @property
    def hist_name_regex(self):
        return re.compile("^(?P<sample>\w+)_category_(?P<category>\w+)_var_(?P<variable>\w+)$")
    
    @property
    def ff_cr_regions(self):
        for _, cr in FF_CR_REGIONS.iteritems():
            for c in cr:
                c.mc_camp = self.mc_camp
        return FF_CR_REGIONS[self.channel]

