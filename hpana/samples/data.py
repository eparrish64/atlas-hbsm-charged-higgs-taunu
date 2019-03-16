# numpy imports
import numpy as np
import glob
import os
import random
import string
import copy

# ROOT
import ROOT

# local imports
from hpana import log
from hpana.samples.sample import Sample, SystematicsSample, Histset
from hpana.lumi import LUMI
from hpana.categories import Category
from hpana.systematics import Systematic

# ----------------------------------------------------------------------------------
##
# ----------------------------------------------------------------------------------
class DataInfo():
    """
    Class to hold lumi and collision energy info for plot labels
    """

    def __init__(self, lumi, energies):
        self.lumi = lumi
        if not isinstance(energies, (tuple, list)):
            self.energies = [energies]
        else:
            # defensive copy
            self.energies = energies[:]
        self.mode = 'root'

    def __add__(self, other):
        return DataInfo(self.lumi + other.lumi,
                        self.energies + other.energies)

    def __iadd__(self, other):
        self.lumi += other.lumi
        self.energies.extend(other.energies)

    def __str__(self):
        if self.mode == 'root':
            label = '#scale[0.7]{#int} L dt = %.1f fb^{-1}  ' % self.lumi
            label += '#sqrt{#font[52]{s}} = '
            label += '+'.join(map(lambda e: '%d TeV' % e,
                                  sorted(set(self.energies))))
        else:
            label = '$\int L dt = %.1f$ fb$^{-1}$ ' % self.lumi
            label += '$\sqrt{s} =$ '
            label += '$+$'.join(map(lambda e: '%d TeV' % e,
                                    sorted(set(self.energies))))
        return label


# ----------------------------------------------------------------------------------
##
class Data(Sample):
    """
    """
    STREAMS = ("2015", "2016", "2017", "2018")
    __HERE = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, config,
                 name='Data',
                 label='Data',
                 streams=[],
                 blind=True,
                 blind_streams=["2017", "2018"],
                 blind_regions=["SR_TAUJET", "SR_TAULEP", "SR_TAUEL", "SR_TAUMU"],
                 grls=["data_2015_lumi.csv", "data_2016_lumi.csv", "data_2017_lumi.csv", "data_2018_lumi.csv"],
                 **kwargs):

        database = kwargs.pop("database", None)

        # - - - - intantiate the base class
        super(Data, self).__init__(config, name=name, label=label, **kwargs)

        self.config = config
        self.grls = grls

        if not streams:
            streams = self.config.data_streams
        for st in streams:
            assert st in Data.STREAMS, "{0} stream not found in {1}".format(
                st, Data.STREAMS)
        self.streams = streams
        self.data_runs = []
        self.good_runs = []
        log.info("DATA STREAMS: {}".format(self.streams))

        # - - - - blind streams and regions
        self.blind = blind
        self.blind_streams = blind_streams
        for st in self.blind_streams:
            if st in self.streams:
                self.blind = True
        self.blind_regions = blind_regions


        # - - - - get datasets for the streams(TP FIX: KEEP 207 for r20.7)
        if "207" in name:
            # - - r20.7 ntuples are merged!
            self.datasets = [self.config.database["DATA207"]]
        else:
            self.datasets = []
            for stream in self.streams:
                dsprefix = "DATA%s_" % stream
                for dk in self.config.database.keys():
                    if dk.startswith(dsprefix):
                        self.datasets.append(self.config.database[dk])
                        self.data_runs += [(int(self.config.database[dk].id))]

        if len(self.datasets) > 1:
            # - - - - update the data lumi based on the existing data runs
            data_lumi = {}
            # - - - - in CSV:
            # - - - - Run, Good, Bad, LDelivered, LRecorded, LAr Corrected, Prescale Corrected, Live Fraction, LAr Fraction, Prescale Fraction
            good_run_lines = []
            for grl in self.grls:
                stream = grl.split("_")[1]  # <! keep the name pattern
                data_lumi[stream] = 0
                grlf = os.path.join(Data.__HERE, grl)
                with open(grlf, "r") as grl_file:
                    good_run_lines = grl_file.readlines()

                good_run_lines = filter(
                    lambda gl: gl[0].isdigit(), good_run_lines)
                for grun_line in good_run_lines:
                    # - - add 00 prefix
                    grun = int(grun_line.split(",")[0])  # <! ,Run
                    if (grun in self.data_runs):
                        # <! ,Prescale Corrected
                        glumi = float(grun_line.split(",")[6])
                        self.good_runs += [(grun, glumi)]
                        data_lumi[stream] += glumi
                if (data_lumi[stream] != self.config.data_lumi[stream]):
                    log.warning(
                        "default LUMI for %s is %0.4f and calculated one is %0.4f; updating the default" % (
                            stream, self.config.data_lumi[stream] / 1e3, data_lumi[stream] / 1e3))
                    self.config.data_lumi.update(data_lumi)

        int_lumi = sum([self.config.data_lumi[st] for st in self.streams])
        self.info = DataInfo(int_lumi / 1e3, self.config.energy)

    def get_lumi_block(self, start_run, end_run):
        """calcualte lumi for the given stram for the runs in a specific range (including both ends).
        """
        lumi = 0
        for grun in self.good_runs:
            if (start_run <= grun[0] <= end_run):
                lumi += grun[1]
        return lumi

    def triggers(self, categories=[], dtype="DATA"):
        """ trigger could be different for different selection categories.
        Parameters
        -----------
        categories:
         list(Category type): selection categories. 
        """

        trigger_dict = {}
        for cat in categories:
            trigger_dict[cat.name] = self.config.trigger(
                dtype=dtype, category=cat)

        return trigger_dict

    def cuts(self, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------

        Returns
        -------
        cut: Cut, updated Cut type.
        """

        # - - - - data trigger
        trigger = kwargs.pop("trigger", self.config.trigger(dtype="DATA"))
        cut = super(Data, self).cuts(trigger=trigger, **kwargs)
        return cut

    def cutflow(self, cuts, **kwargs):
        """
        """
        categories = []
        cuts_list = []
        for name, cut in cuts.iteritems():
            if name.upper() == "TRIGGER":
                cut = self.config.trigger(dtype="DATA")
            cuts_list += [cut]
            categories.append(
                Category(name, cuts_list=cuts_list, mc_camp=self.config.mc_camp))

        field = kwargs.pop("field", self.config.variables[0])
        hists = self.hists(categories=categories, fields=[field], **kwargs)

        return hists

    def workers(self, **kwargs):
        """
        """
        # - - - - not applicable to DATA
        kwargs.pop("systematics", None)
        systematics = filter(lambda s: s.name=="NOMINAL", self.config.systematics)

        # - - - - no weight on DATA and no hist for blind regions
        weighted = kwargs.pop("weighted", False)

        categories = kwargs.pop("categories", [])
        if self.blind:
            categories = filter(
                lambda c: c.name not in self.blind_regions, categories)

        data_categories = copy.deepcopy(categories)
        for ct in data_categories:
            ct.truth_tau = None

        _workers = super(Data, self).workers(
            categories=data_categories,
            systematics=systematics,
            weighted=False,
            **kwargs)
        return _workers
