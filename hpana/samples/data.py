# numpy imports
import numpy as np
import glob, os, random, string  

# ROOT
import ROOT

# local imports
from . import log
from .sample import Sample, SystematicsSample, Histset
from ..lumi import LUMI
from ..cluster.parallel import FuncWorker, run_pool, map_pool

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
    STREAMS = ("2015", "2016",)# "2017", "2018")
    def __init__(self, config,
                 name='Data',
                 label='Data',
                 blind=True,
                 blind_regions=[],
                 **kwargs):
        # - - - - intantiate the base class
        super(Data, self).__init__(config, name=name, label=label, **kwargs)

        self.config = config
        
        # - - - - Database 
        self.db = self.config.database

        # - - - - get datasets for the streams
        self.datasets = [self.db["Data1516"]]
        # for stream in Data.STREAMS:
        #     dsprefix = "DATA%s_"%stream
        #     dsprefix = "Data%"%stream
        #     for dk in self.db.keys():
        #         if dk.startswith(dsprefix):
        #             self.datasets.append(self.db[dk])
        self.info = DataInfo(self.config.data_lumi / 1e3, self.config.energy)
        self.blind = blind
        self.blind_regions = blind_regions
        
    def cuts(self, *args, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------

        Returns
        -------
        cut: Cut, updated Cut type.
        """
        cut = super(Data, self).cuts(*args, **kwargs)
        return cut
    
    def workers(self, **kwargs):
        """
        """
        # - - - - no weight on DATA and no hist for blind regions
        systematics = kwargs.pop("systematics", ["NOMINAL"])
        weighted = kwargs.pop("weighted", False)
        
        categories = kwargs.pop("categories", [])
        categories = filter(lambda c: c.name not in self.blind_regions, categories)
            
        _workers = super(Data, self).workers(
            categories=categories,
            systematics=["NOMINAL"],
            weighted=weighted,
            **kwargs)
        
        return _workers
    
    
    def hists(self, **kwargs):
        
        systematics = kwargs.pop("systematics", ["NOMINAL"])
        weighted = kwargs.pop("weighted", False)
        
        if self.blind:
            categories = filter(lambda cat: not cat.name in self.blind_regions,  [c.name for c in categories])
        
        super(Data, self).hists(systematics=systematics, weighted=weighted, **kwargs)
        
