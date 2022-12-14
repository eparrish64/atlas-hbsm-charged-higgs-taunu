"""
config.py
contains a simple class for analysis channel specific settings, 
like selections , variables, weights, etc.
"""
# stdlib
import datetime
import re

# local
from . import (MC_CAMPAIGN, CACHE_DIR, YEAR_ENERGY,
               EVENTS_CUTFLOW_HIST, EVENTS_CUTFLOW_BIN, NORM_FIELD)
from hpana.systematics import *
from hpana.categories import *
from hpana.lumi import *
from hpana.trigger import *
from hpana.weights import *
from hpana.variables import *
from hpana.systematics import SYSTEMATICS
from hpana.db import cached_property
from hpana.db.datasets import Database

# ------------------------------------------------------------
##
# ------------------------------------------------------------
class Configuration(object):
    """ simple class for wrapping different analysis configurations.
    assuming variables/categories/weights are all the same for all years.
    """

    def __init__(self, channel,
                year="2018",
                mc_campaign=MC_CAMPAIGN,
                cache_dir=CACHE_DIR,
                norm_field=NORM_FIELD,
                db_version="18v01",
                data_streams=("2015", "2016"),
                FFs_macros=["FFsCOM.cxx", "FFsCR.cxx"], 
                metTrigEff_macros=["metTrigEff.cxx"], 
                upsilon_macros=["CorrectUpsilon.cxx"],                
                effm_taujet_macros=["eff_mass_taujet.cxx"],
                effm_taulep_macros=["eff_mass_taulep.cxx"],
                njets_macros=["njets.cxx"],
                root_conf_files = [],
                ):
        self.channel = channel
        self.cache_dir = cache_dir
        self.db_version = db_version
        self.norm_field = norm_field
        self.mc_camp = mc_campaign
        self.data_streams = data_streams
        self.year = year
        self.FFs_macros = FFs_macros
        self.metTrigEff_macros = metTrigEff_macros
        self.upsilon_macros = upsilon_macros
        self.effm_taujet_macros = effm_taujet_macros
        self.effm_taulep_macros	= effm_taulep_macros
        self.njets_macros=njets_macros
        self.root_conf_files = root_conf_files

        # - - - - DATA luminosity dictionary (keys are data streams)
        self.data_lumi = LUMI

    @cached_property
    def database(self):
        return Database(name="DB_%s"%self.channel, version=self.db_version, verbose=False)

    @property
    def variables(self):
        variables = VARIABLES[self.channel]
        for var in variables:
            var.mc_camp = self.mc_camp
        return variables

    def trigger(self, data_streams=None, dtype="MC", category=None):
        """trigger should be unique per data taking year (stream),
        it's also different for DATA and MC.
        """
        if data_streams is None:
            data_streams = self.data_streams
        # - - check if it is a MULTIJET (aka QCD) control region
        if category:
            if ("MULTIJET" in category.name or "QCD" in category.name):
                log.debug("Applying multijet trigger for %s category" %category.name)
                return get_mj_trigger(data_streams, dtype=dtype)
            if ("DILEP" in category.name):
                log.debug("Applying dilep trigger for %s category" %(category.name))
                return get_dilep_trigger(self.channel, data_streams=data_streams, dtype=dtype)
                
        return get_trigger(self.channel, data_streams=data_streams, dtype=dtype)

    @property
    def weight_fields(self):
        """weight fields list
        """
        return Weight.factory()[self.channel]

    @property
    def event_total_weight(self):
        """overall weight string for the event
        """
        return "*".join(self.weight_fields)

    @property
    def categories(self):
        cats = CATEGORIES[self.channel] #+ self.ff_cr_regions
        # if self.channel=="taulep":
        #     cats += self.met_trigeff_regions
        for c in cats:
            c.mc_camp = self.mc_camp
        return cats

    def categories_func(self, partial_unblind=False):
        cats = CATEGORIES[self.channel] #+ self.ff_cr_regions
        if partial_unblind==True:
            if self.channel == "taulep":
                cats += [Category_SR_TAULEP_PARTIAL, Category_SR_TAUEL_PARTIAL, Category_SR_TAUMU_PARTIAL]
            elif self.channel == "taujet":
                cats += [Category_SR_TAUJET_PARTIAL]
            else:
                pass
        # if self.channel=="taulep":
        #     cats += self.met_trigeff_regions
        for c in cats:
            c.mc_camp = self.mc_camp
        return cats

    @property
    def systematics(self):
        """common systematics components
        """
        return SYSTEMATICS[self.channel]

    @property
    def systematics_variations(self):
        varss = []
        for st in self.systematics:
            varss += st.variations
    
    @property
    def data_lumi(self):
        """ lumi is per data taking year (stream)
        """
        return self.__data_lumi

    @data_lumi.setter
    def data_lumi(self, value):
        self.__data_lumi = value

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
        if isinstance(TAUID_MEDIUM, dict):
            return TAUID_MEDIUM[self.mc_camp]
        return TAUID_MEDIUM

    @property
    def antitau(self):
        if isinstance(ANTI_TAU, dict):
            return ANTI_TAU[self.mc_camp]
        return ANTI_TAU

    @property
    def true_tau(self):
        if isinstance(TAU_IS_TRUE, dict):
            return TAU_IS_TRUE[self.mc_camp]
        return TAU_IS_TRUE

    @property
    def signal_masses(self):
        return SIGNAL_MASSES

    @cached_property
    def hists_file(self):
        return "HISTS_%s_%s.root" % (self.channel, datetime.datetime.today().strftime("%Y_%m_%d"))

    @property
    def hist_name_template(self):
        # <! sample name, category name, variable name
        return "{0}_category_{1}_var_{2}"

    @property
    def hist_name_regex(self):
        return re.compile("^(?P<sample>\w+)_category_(?P<category>\w+)_var_(?P<variable>\w+)$")

    @property
    def ff_cr_regions(self):
        for _, cr in FF_CR_REGIONS.iteritems():
            for c in cr:
                c.mc_camp = self.mc_camp
        return FF_CR_REGIONS[self.channel]

    @property
    def clf_regions(self):
        if isinstance(CLASSIFIER_CATEGORIES[self.channel], (list, tuple)):
            return CLASSIFIER_CATEGORIES[self.channel]
        else:
            return [CLASSIFIER_CATEGORIES[self.channel]]

    @property
    def met_trigeff_regions(self):
        if self.channel=="taulep":
            return [MET_TRIG_EFF_CR_NOM]
        return []
