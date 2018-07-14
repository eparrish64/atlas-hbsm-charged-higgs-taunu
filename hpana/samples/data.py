# numpy imports
import numpy as np
import glob, os, random, string  

# ROOT
import ROOT

# local imports
from . import log
from .sample import Sample, SystematicsSample, Histset
from ..lumi import LUMI
from ..cluster.parallel import map_pool
from ..categories import Category

##----------------------------------------------------------------------------------
##
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


##----------------------------------------------------------------------------------
##
class Data(Sample):
    """
    """
    STREAMS = ("2015", "2016", "2017", "2018")
    def __init__(self, config,
                 name='Data',
                 label='Data',
                 streams=[],
                 blind=True,
                 blind_regions=[],
                 **kwargs):

        database = kwargs.pop("database", None)
        
        # - - - - intantiate the base class
        super(Data, self).__init__(config, name=name, label=label, database=database, **kwargs)

        self.config = config

        if not streams:
            streams = self.config.data_streams
        for st in streams:
            assert st in Data.STREAMS, "{0} stream not found in {1}".format(st, Data.STREAMS) 
        self.streams = streams

        log.info("DATA STREAMS: {}".format(self.streams))
        # - - - - Database 
        self.database = database

        # - - - - get datasets for the streams(TP FIX: KEEP 207 for r20.7)
        if "207" in name:
            self.datasets = [self.database["DATA207"]]
        else:
            self.datasets = []
            for stream in self.streams:
                dsprefix = "DATA%s_"%stream
                for dk in self.database.keys():
                    if dk.startswith(dsprefix):
                        self.datasets.append(self.database[dk])
        self.info = DataInfo(self.config.data_lumi / 1e3, self.config.energy)
        self.blind = blind
        self.blind_regions = blind_regions

    def triggers(self, categories=[]):
        """ trigger could be different for different selection categories.
        Parameters
        -----------
        categories:
         list(Category type): selection categories. 
        """
        
        trigger_dict = {} 
        for cat in categories:
            trigger_dict[cat.name] = self.config.trigger(dtype="DATA", category=cat)
            
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
            if name.upper()=="TRIGGER":
                cut = self.config.trigger(dtype="DATA")
            cuts_list += [cut]
            categories.append(Category(name, cuts_list=cuts_list, mc_camp=self.config.mc_camp))
            
        field = kwargs.pop("field", self.config.variables[0])
        hists = self.hists(categories=categories,
                           fields=[field],
                           systematics=["NOMINAL"],
                           **kwargs)
        
        return hists
    
    
    def workers(self, **kwargs):
        """
        """
        # - - - - not applicable to DATA
        kwargs.pop("systematics", None)
        
        # - - - - no weight on DATA and no hist for blind regions
        weighted = kwargs.pop("weighted", False)
        
        categories = kwargs.pop("categories", [])
        categories = filter(lambda c: c.name not in self.blind_regions, categories)
        
        _workers = super(Data, self).workers(
            categories=categories,
            systematics=["NOMINAL"],
            weighted=False,
            **kwargs)
        return _workers
    
