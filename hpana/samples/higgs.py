# stdlib imports
import os
import pickle
from math import pi, sqrt

# local imports
from . import log
from .sample import MC, Signal

class Higgs(MC, Signal):
    # - - - - - - - - - signal mass points 
    MASSES_LOW = {
        90: "344287",
        100: "344288",
        110: "344289",
        120: "344290",
        
        130: "344291",
        140: "344292",
        150: "344293",
        }
    MASSES_INT = {
        160: "344250",
        165: "344251",
        170: "344252",
        175: "344253",
        180: "344254",
    }
    
    MASSES_HIGH = {
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

    MASSES = {}
    MASSES.update(MASSES_LOW)
    MASSES.update(MASSES_INT)
    MASSES.update(MASSES_HIGH)

    SAMPLE_PATTERN = {
        "LOW": "MadGraphPythia8EvtGen_A14NNPDF23LO_Hplus_H{0}_taunu",
        "INT": "MadGraphPythia8EvtGen_A14NNPDF23LO_HplusInt_H{0}_taunu",
        "HIGH": "aMcAtNloPythia8EvtGen_A14NNPDF23LO_Hplus4FS_H{0}_taunu",
    }
    
    NORM_BY_THEORY = True
    
    def __init__(self, config,
                 mass=None,
                 name=None,
                 suffix=None,
                 label=None,
                 scale=1,
                 **kwargs):
        
        assert mass in Higgs.MASSES
        if not name:
            name = "Hplus{}".format(mass)
        if label is None:
            if scale!=1:
                label = '{1}#times H^+{0}'.format(mass, scale)
            else:
                label = 'H^{{+}}{0}'.format(mass)

        self.config = config
        self.name = name
        self.label=label
                
        if mass <= max(Higgs.MASSES_LOW.keys()):
            mode = "LOW"
        elif mass <= max(Higgs.MASSES_INT.keys()):
            mode = "INT"
        elif mass <= max(Higgs.MASSES_HIGH.keys()):
            mode = "HIGH"
        else:
            raise ValueError("unknown mass {} for the signal!".format(mass))

        # - - - - the samples for this signal
        self.samples = [(Higgs.SAMPLE_PATTERN[mode].format(mass)) ]
        log.debug("signal: {}".format(self.samples[0]))

        database = kwargs.pop("database", None)
        # - - - - instantiate the base
        super(Higgs, self).__init__(config, label=label, database=database, name=name, **kwargs)

    
