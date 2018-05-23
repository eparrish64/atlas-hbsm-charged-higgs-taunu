# stdlib imports
import os
import pickle
from math import pi, sqrt


# local imports
from . import log
from .sample import MC, Signal
from .. import SIGNAL_MASSES

class Higgs(MC, Signal):
    MASSES = SIGNAL_MASSES
    MODES  = {}
    NORM_BY_THEORY = True

    def __init__(self, year,
                 mode='gg', modes=None,
                 mass=None, masses=None,
                 channel=None,
                 sample_pattern=None,
                 ggf_weight=False,
                 vbf_weight=False,
                 suffix=None,
                 label=None,
                 inclusive_decays=False,
                 **kwargs):
        self.channel=channel
        self.inclusive_decays = inclusive_decays
        if masses is None:
            if mass is not None:
                assert mass in Higgs.MASSES
                masses = [mass]
            else:
                # default to 125
                masses = [125]
        else:
            assert len(masses) > 0
            for mass in masses:
                assert mass in Higgs.MASSES
            assert len(set(masses)) == len(masses)

        if modes is None:
            if mode is not None:
                assert mode in Higgs.MODES
                modes = [mode]
            else:
                # default to all modes
                modes = Higgs.MODES
        else:
            assert len(modes) > 0
            for mode in modes:
                assert mode in Higgs.MODES
            assert len(set(modes)) == len(modes)

        name = 'Signal'

        str_mode = ''
        if len(modes) == 1:
            str_mode = modes[0]
            name += '_%s' % str_mode
        elif len(modes) == 2 and set(modes) == set(['W', 'Z']):
            str_mode = 'V'
            name += '_%s' % str_mode

        str_mass = ''
        if len(masses) == 1:
            str_mass = '%d' % masses[0]
            name += '_%s' % str_mass

        if label is None:
            label = '%s#font[52]{H}(%s)#rightarrow#tau#tau' % (
                str_mode, str_mass)


        self.samples = []
        self.masses = []
        self.modes = []

        assert len(modes) == 1
        for mass in masses:
            self.masses.append(mass)
            self.modes.append(modes[0])
            self.samples.append(sample_pattern.format(mass) + '.' + suffix)

        if len(self.modes) == 1:
            self.mode = self.modes[0]
        else:
            self.mode = None
        if len(self.masses) == 1:
            self.mass = self.masses[0]
        else:
            self.mass = None

        super(Higgs, self).__init__(
            year=year, label=label, name=name, **kwargs)

    def weight_systematics(self):
       systematics = super(Higgs, self).weight_systematics()
       if self.ggf_weight:
           systematics.update({
               'QCDscale_ggH1in'})
       return systematics

   def weights(self):
        fields = super(Higgs, self).weight_fields()
        if self.ggf_weight:
            fields.append(self.ggf_weight_field)
        if self.vbf_weight:
            fields.append(self.vbf_weight_field)
        return fields

