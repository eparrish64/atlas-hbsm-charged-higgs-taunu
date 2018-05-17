
# local imports
from . import log

class SYSTEMATICS_CATEGORIES:
    TAUS, \
    JETS, \
    WEIGHTS, \
    NORMALIZATION = range(4)

# WIP:
class Systematic(object):

    def __init__(self, name, variations=None):

        if variations is None:
            self.variations = ('UP', 'DOWN')
        else:
            if not isinstance(variations, (list, tuple)):
                variations = (variations,)
            self.variations = variations
        self.name = name

    def __iter__(self):

        for var in self.variations:
            yield '%s_%s' % (self.name, var)


COMMON_SYSTEMATICS = {
    "taujet":
    {
    "2017":
        {'MET_RESOSOFTTERMS': (('MET_RESOSOFTTERMS_UP',), ('MET_RESOSOFTTERMS_DOWN',)),
         'MET_SCALESOFTTERMS': (('MET_SCALESOFTTERMS_UP',), ('MET_SCALESOFTTERMS_DOWN',)),
         
         'JES_Modelling': (('JES_Modelling_UP',), ('JES_Modelling_DOWN',)),
         'JES_Detector': (('JES_Detector_UP',), ('JES_Detector_DOWN',)),
         'JES_EtaModelling': (('JES_EtaModelling_UP',), ('JES_EtaModelling_DOWN',)),
         'JES_EtaMethod': (('JES_EtaMethod_UP',), ('JES_EtaMethod_DOWN',)),
         'JES_PURho': (('JES_PURho_UP',), ('JES_PURho_DOWN',)),
         'JES_FlavComp': (('JES_FlavComp_UP',), ('JES_FlavComp_DOWN',)),
         'JES_FlavResp': (('JES_FlavResp_UP',), ('JES_FlavResp_DOWN',)),
         
         'JER': (('JER_UP',),),
         
         'MFS': (('MFS_UP',), ('MFS_DOWN',)),
         'ISOL': (('ISOL_UP',), ('ISOL_DOWN',)),
        
         'PU_RESCALE': (('PU_RESCALE_UP',), ('PU_RESCALE_DOWN',)),
         
         'TRIGGER': (('TRIGGER_UP',), ('TRIGGER_DOWN',)),
         'FAKERATE': (('FAKERATE_UP',), ('FAKERATE_DOWN',)),
         'TAU_ID': (('TAU_ID_UP',), ('TAU_ID_DOWN',)),
         
         'QCD_FIT': (('QCDFIT_UP',), ('QCDFIT_DOWN',)),
         'Z_FIT': (('ZFIT_UP',), ('ZFIT_DOWN',)),

         'QCD_SHAPE': (('QCDSHAPE_UP',), ('QCDSHAPE_DOWN',)),
        }
    }
}
WEIGHT_SYSTEMATICS = {
    "taujet":
    {
        "2017":
        {"TRIGGER": ("TRIGGER_UP", "TRIGGER_DOWN"),
         "FAKERATE": ('FAKERATE_UP','FAKERATE_DOWN'),
         "TAU_ID": ('TAU_ID_UP', 'TAU_ID_DOWN'),
         "TAU_ID_STAT": ('TAU_ID_STAT_UP','TAU_ID_STAT_DOWN'),
        }
    }
}

def iter_systematics(include_nominal=False, year=2012, components=None):
    syst = get_systematics(year)
    if include_nominal:
        yield 'NOMINAL'
    terms = components if components is not None else syst.keys()
    for term in terms:
        try:
            variations = syst[term]
        except KeyError:
            raise ValueError("systematic term {0} is not defined".format(term))
        for var in variations:
            yield var


def get_systematics(year=2012):
    if year == 2012:
        return SYSTEMATICS_2012
    elif year == 2011:
        return SYSTEMATICS_2011
    elif year == 2015:
        log.warning('Need to update the list of systematics for 2015')
        return SYSTEMATICS_2012
    else:
        raise ValueError("No systematics defined for year %d" % year)

def systematic_name(systematic):
    if isinstance(systematic, basestring):
        return systematic
    return '_'.join(systematic)


def parse_systematics(string):
    if not string:
        return None
    return [tuple(token.split('+')) for token in string.split(',')]
