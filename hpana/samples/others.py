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
]

import ROOT

# local imports
from .sample import MC, Background, cached_property
from . import log
from ..categories import TAU_IS_TRUE

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
        cut += TAU_IS_TRUE
        return cut


##----------------------------------------------------------------------------------------
##
class Top(MC, Background):
    NO_KYLEFIX = True
    NORM_BY_THEORY = True

    def __init__(self, *args, **kwargs):
        super(Top, self).__init__(*args, **kwargs)

    @cached_property
    def weights(self, **kwargs):
        """WIP: specific weights for Top like top pt weights
        """
        weights = super(Top, self).weights
        weights += ["GetTopPtWeight(truth_top0_pt)"]
        
        return weights
    
        
##----------------------------------------------------------------------------------------
## sample dedicated classes 

class Diboson(MC, Background):
    # mixin
    pass

class Others(MC, Background):
    # mixin
    pass

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


