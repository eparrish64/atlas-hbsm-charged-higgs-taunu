__all__=[
    'EWK',
    'TTbar',
    'Single_Top',
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

from hpana.systematics import Systematic, Variation

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
class Single_Top(MC, Background):
    NO_KYLEFIX = True
    NORM_BY_THEORY = True

    def __init__(self, *args, **kwargs):
        super(Single_Top, self).__init__(*args, **kwargs)
        self.kwargs = kwargs
    
    def weights(self, **kwargs):
        """WIP: specific weights for Top like top pt weights
        """
        weights = super(Single_Top, self).weights(**kwargs)
        if "pt_weighted" in self.kwargs:
            if self.kwargs["pt_weighted"]:
                for wcat in weights:
                    weights[wcat] += ["GetTopPtWeight(truth_top0_pt)"]
        
        return weights

##----------------------------------------------------------------------------------------
##
class TTbar(Single_Top):

    def __init__(self, *args, **kwargs):
        super(TTbar, self).__init__(*args, **kwargs)
        self.kwargs = kwargs

    def workers(self, **kwargs):
        """ Since TTbar jobs are heavy assigning one worker per systematic
        """
        systematics = kwargs.pop("systematics", [])
        if not systematics:
            systematics = self.systematics

        workers = []
        for systematic in systematics:
            _workers = super(TTbar, self).workers(systematics=[systematic], **kwargs)
            for w in _workers:
                w.name = w.name + "." + systematic.name  
            workers += _workers

        return workers

    def systematics_reweight(self,**kwargs):

        print  " IN systematics_reweight"
        #systematics = kwargs.pop("systematics", [])
        #if systematics:
        #syst = self.config.systematics[:]
        wttbar_nom = Systematic(
            #taujet
            "NOMINAL", _type="WEIGHT", variations=[Variation("NOMINAL", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1)", _type="WEIGHT")], )
            #taulep
            #ak "NOMINAL", _type="WEIGHT", variations=[Variation("NOMINAL", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1)", _type="WEIGHT")], )
        # variations fit
        wttbar_fit_syst = Systematic("wttbar_fit", _type="WEIGHT")
        wttbar_fit_syst.variations = [
            #taujet
            Variation("wttbar_1up", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),2)", _type="WEIGHT"),
            Variation("wttbar_1down", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),3)", _type="WEIGHT"),
            Variation("wttbar1_1up", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),4)", _type="WEIGHT"),
            Variation("wttbar1_1down", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),5)", _type="WEIGHT"),
            #taulep
            #ak Variation("wttbar_1up", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),2)", _type="WEIGHT"),
            #ak Variation("wttbar_1down", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),3)", _type="WEIGHT"),
            #ak Variation("wttbar1_1up", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),4)", _type="WEIGHT"),
            #ak Variation("wttbar1_1down", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),5)", _type="WEIGHT"),
            #ak Variation("wttbar2_1up", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),6)", _type="WEIGHT"),
            #ak Variation("wttbar2_1down", title="eff_mass(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),7)", _type="WEIGHT"),
        ]
     

        syst = [wttbar_nom, wttbar_fit_syst]

        return syst



    @property
    def systematics(self, **kwargs):

        systematics = super(TTbar, self).systematics + self.systematics_reweight()      

        return systematics 

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


