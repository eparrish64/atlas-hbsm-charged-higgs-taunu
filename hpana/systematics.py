"""
* Base class for systematics types. 
* Systematic class mainly encapsulated systematics info for different types.
* Systematic Objects, can then be passed to the anlaysis workers in order to 
* do histograms depending on the type and source of systematics
* @author : sina.bahrasemani@cern.ch
"""

# local imports
from hpana import log
from hpana.weights import WEIGHTS


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
class Systematic(object):
    TYPES = ["TREE", "WEIGHT", "THEORY"]

    # systematics with dedicated TTree
    SOURCES = {"taujet": {}, "taulep": {}}

    # taujet specific
    SOURCES["taujet"] = {
        "TAU": (
            "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1up",
            "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1down",
            "TAUS_TRUEHADTAU_SME_TES_INSITU_1up",
            "TAUS_TRUEHADTAU_SME_TES_INSITU_1down",
            "TAUS_TRUEHADTAU_SME_TES_MODEL_1up",
            "TAUS_TRUEHADTAU_SME_TES_MODEL_1down",
        ),
        "JET": (),
        "MET": (),
    }

    # taulep specific
    SOURCES["taulep"]["TAU"] = SOURCES["taujet"]["TAU"]
    SOURCES["taulep"]["JET"] = SOURCES["taujet"]["JET"]
    SOURCES["taulep"]["MET"] = SOURCES["taujet"]["MET"]
    SOURCES["taulep"]["MUON"] = (
        "MUON_ID_1down",
        "MUON_ID_1up",
        "MUON_MS_1down",
        "MUON_MS_1up",
        "MUON_SAGITTA_RESBIAS_1down",
        "MUON_SAGITTA_RESBIAS_1up",
        "MUON_SAGITTA_RHO_1down",
        "MUON_SAGITTA_RHO_1up",
        "MUON_SCALE_1down",
        "MUON_SCALE_1up",
    )
    SOURCES["taulep"]["ELECTRON"] = ()

    def __init__(self, name, title=None, _type="TREE", channel="taujet"):
        assert _type in Systematic.TYPES, "systematics of type %s is not supported" % _type
        self._type = _type
        self.channel = channel
        self.name = name
        if not title:
            title = name
        self.title = title

    def __repr__(self):
        return "name=%r, title=%r, type=%r" % (self.name, self.title, self._type)

    @classmethod
    def factory(cls, channels=["taujet", "taulep"]):
        """ factroy method for providing analysis wide systematics. 
        """
        systs_dict = {}
        for channel in channels:
            # kinematics systematics (TTrees including NOMINAL)
            systematics = [cls("NOMINAL", _type="TREE", channel=channel)]
            for source, ws in cls.SOURCES[channel].iteritems():
                assert isinstance(ws, (tuple, list)), "must be a tuple or list"
                for w in ws:
                    syst = cls(w, _type="TREE", channel=channel)
                    systematics += [syst]

            # weight systematics
            nom_weights = [nw.name for nw in WEIGHTS[channel]]
            nom_weight = "*".join(nom_weights)
            for weight in WEIGHTS[channel]:
                nom_w = weight.variations[0]
                var_weights = weight.variations[1:]
                for vw in var_weights:
                    # FIX ME: better solution ?
                    sname = vw.split("*")[-1].replace(")", "")
                    syst = cls(sname, title="(%s)/(%s)" %
                               (vw, nom_w), channel=channel, _type="WEIGHT")
                    systematics += [syst]

            # theory systematics: WIP
            systs_dict[channel] = systematics

        return systs_dict


# prepapre systematic objects
SYSTEMATICS = Systematic.factory()
