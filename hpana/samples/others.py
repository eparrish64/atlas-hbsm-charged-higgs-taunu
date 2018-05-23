__all__=[
    'EWK',
    'Top',
    'Diboson',
    'Sh_Zll',
    'Sh_Wtaunu',
    'Sh_Wlnu',
    'Others',
    "Mg_Ztautau",
    "Sh_Ztautau",
    "Pythia_Ztautau"
]
import ROOT

# local imports
from .sample import MC, Background
from . import log
from ..categories import TRUTH_MATCH

##----------------------------------------------------------------------------------------
##
class EWK(MC, Background):
    NO_KYLEFIX = True
    NORM_BY_THEORY = True

    def __init__(self, *args, **kwargs):
        self.truth_matched = kwargs.pop('truth_matched', False)
        super(EWK, self).__init__(*args, **kwargs)
        
    def cuts(self, *args, **kwargs):
        cut = super(EWK, self).cuts(*args, **kwargs)
        cut += TRUTH_MATCH
        return cut


##----------------------------------------------------------------------------------------
##
class Top(MC, Background):
    NO_KYLEFIX = True
    NORM_BY_THEORY = True

    def __init__(self, *args, **kwargs):
        self.matched = kwargs.pop('truth_matched', False)
        super(Top, self).__init__(*args, **kwargs)

    def cuts(self, *args, **kwargs):
        cut = super(Top, self).cuts(*args, **kwargs)
        cut += TRUTH_MATCH
        return cut

##----------------------------------------------------------------------------------------
##
class Diboson(MC, Background):
    NO_KYLEFIX = True
    NORM_BY_THEORY = True

    def __init__(self, *args, **kwargs):
        self.truth_matched = kwargs.pop('truth_matched', True)
        super(Diboson, self).__init__(*args, **kwargs)

    def cuts(self, *args, **kwargs):
        cut = super(Diboson, self).cuts(*args, **kwargs)
        cut += TRUTH_MATCH
        return cut

##----------------------------------------------------------------------------------------
##
class Others(MC, Background):
    NO_KYLEFIX = True
    NORM_BY_THEORY = True

    def __init__(self, *args, **kwargs):
        self.truth_matched = kwargs.pop('truth_matched', True)
        super(Others, self).__init__(*args, **kwargs)

    def cuts(self, *args, **kwargs):
        cut = super(Others, self).cuts(*args, **kwargs)
        cut += TRUTH_MATCH
        return cut


##----------------------------------------------------------------------------------------
##
# INDIVIDUAL SAMPLES
class Sh_Wtaunu(MC, Background):
    pass

class Sh_Wlnu(MC, Background):
    pass

class Sh_Zll(MC, Background):
    pass


# Sherpa2.2
class Sh_Ztautau(MC, Background):
    pass

# MadGraph
class Mg_Ztautau(MC, Background):
    pass


class MC_Ztautau_DY(MC_Ztautau):
    pass

class Pythia_Ztautau(MC_Ztautau):
    pass