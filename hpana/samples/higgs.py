# stdlib imports
import os
import pickle
from math import pi, sqrt

# local imports
from . import log
from .sample import MC, Signal

class Higgs(MC, Signal):
    # - - - - - - - - - signal mass points 
    TAUJET_SIGS ={
        "LOW":{ 
            80 : "346239",
            90 : "346241",
            100 : "346243",
            110 : "346245",
            120 : "346247",
            130 : "346249",
        },
        "INT":{
            140 : "346251",
            150 : "346253",
            160 : "346255",
            170 : "346257",
            180 : "346259",
            190 : "346261",
        },
        "HIGH":{        
            200 : "346263",
            225 : "346265",
            250 : "346267",
            275 : "346269",
            300 : "346271",
            350 : "346273",
            400 : "346275",
            500 : "346277",
            600 : "346279",
            700 : "346281",
            800 : "346283",
            900 : "346285",
            1000 : "346287",
            1200 : "346289",
            1400 : "346291",
            1600 : "346293",
            1800 : "346295",
            2000 : "346297",
            2500 : "346299",
            3000 : "346301",
        }   
    }

    TAULEP_SIGS = {
        "LOW":{ 
            80 : "346238",
            90 : "346240",
            100 : "346242",
            110 : "346244",
            120 : "346246",
            130 : "346248",
        },
        "INT":{
            140 : "346250",
            150 : "346252",
            160 : "346254",
            170 : "346256",
            180 : "346258",
            190 : "346260",
        },
        "HIGH":{
            200 : "346262",
            225 : "346264",
            250 : "346266",
            275 : "346268",
            300 : "346270",
            350 : "346272",
            400 : "346274",
            500 : "346276",
            600 : "346278",
            700 : "346280",
            800 : "346282",
            900 : "346284",
            1000 : "346286",
            1200 : "346288",
            1400 : "346290",
            1600 : "346292",
            1800 : "346294",
            2000 : "346296",
            2500 : "346298",
            3000 : "346300",
        }
    }

    MASS_REGIONS_DICT = {
        "taulep":TAULEP_SIGS,
        "taujet": TAUJET_SIGS,
    } 

    ## flat masses dict
    MASSES_DICT = {"taulep":{}, "taujet": {}}
    for key in ["LOW", "INT", "HIGH"]:
        for channel in ["taulep", "taujet"]:
            for m, did in MASS_REGIONS_DICT[channel][key].iteritems():
                MASSES_DICT[channel][m] = did

    ## all masses 
    MASSES = sorted(MASSES_DICT["taujet"])

    SAMPLE_PATTERN = {
        "LOW": "MadGraphPy8EvtGen_A14NNPDF30LO_HpL_H{}",
        "INT": "MadGraphPy8EvtGen_A14NNPDF30LO_HpI_H{}",
        "HIGH": "aMcAtNloPy8EvtGen_A14NNPDF30NLO_HpH_H{}",
    }
    
    NORM_BY_THEORY = True
    
    def __init__(self, config,
                 mass=None,
                 name=None,
                 suffix=None,
                 label=None,
                 scale=1,
                 **kwargs):
        
        ## check if this mass point is supported
        assert mass in Higgs.MASSES, "unsupported %r mass"%mass

        self.config = config

        if not name:
            name = "Hplus{}".format(mass)
            # name = Higgs.MASSES_DICT[self.config.channel][mass]     
        if label is None:
            if scale!=1:
                label = '{1}#times H^+{0}'.format(mass, scale)
            else:
                label = 'H^{{+}}{0}'.format(mass)

        self.name = name
        self.label=label
        
        if mass <= 130:
            mode = "LOW"
        elif mass <= 190:
            mode = "INT"
        elif 200 <= mass <= 3000:
            mode = "HIGH"
        else:
            raise ValueError("unknown mass {} for the signal!".format(mass))
        self.mass = mass
        self.mode = mode
        
        # - - - - the samples for this signal
        self.samples = [(Higgs.SAMPLE_PATTERN[mode].format(mass)) ]
        log.debug("signal: {}".format(self.samples[0]))
        
        database = kwargs.pop("database", None)
        # - - - - instantiate the base
        super(Higgs, self).__init__(config, label=label, database=database, name=name, **kwargs)

    
