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

        self.args = args

    
    def weights(self, **kwargs):
        """WIP: specific weights for Top like top pt weights
        """
        weights = super(Single_Top, self).weights(**kwargs)

        if "effm_weighted" in self.kwargs:
            if self.kwargs["effm_weighted"]:
                for wcat in weights:
                    if self.args[0].channel == 'taujet':
                        weights[wcat] += ["eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1)"]
                    elif self.args[0].channel == 'taulep':
                        weights[wcat] += ["eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt() + el_0_p4->Pt(),1)"]
                    else:
                        weights[wcat] += 1


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

        if self.args[0].channel == 'taujet':
            #taujet "-1" as reweighting already applied to nominal
            wttbar_nom = Systematic(
            	"NOMINAL", _type="WEIGHT", variations=[Variation("NOMINAL", title="eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),-1)", _type="WEIGHT")], )
            # variations fit
            wttbar_fit_syst = Systematic("wttbar_fit", _type="WEIGHT")
            wttbar_fit_syst.variations = [
            	Variation("wttbar_1up", title="(1./eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1))*eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),2)", _type="WEIGHT"),
	    	Variation("wttbar_1down", title="(1./eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1))*eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),3)", _type="WEIGHT"),
            	#ak Variation("wttbar1_1up", title="(1./eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1))*eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),4)", _type="WEIGHT"),
            	#ak Variation("wttbar1_1down", title="(1./eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),1))*eff_mass_taujet(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt(),5)", _type="WEIGHT"),
            ]
        elif self.args[0].channel == 'taulep':
            #taulep "-1" as reweighting already applied to nominal
            wttbar_nom = Systematic(
            	"NOMINAL", _type="WEIGHT", variations=[Variation("NOMINAL", title="eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),-1)", _type="WEIGHT")], )
            # variations fit
            wttbar_fit_syst = Systematic("wttbar_fit", _type="WEIGHT")
            wttbar_fit_syst.variations = [
            	Variation("wttbar_1up", title="(1./eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1))*eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),2)", _type="WEIGHT"),
            	Variation("wttbar_1down", title="(1./eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1))*eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),3)", _type="WEIGHT"),
            	#ak Variation("wttbar1_1up", title="(1./eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1))*eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),4)", _type="WEIGHT"),
            	#ak Variation("wttbar1_1down", title="(1./eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1))*eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),5)", _type="WEIGHT"),
            	#ak Variation("wttbar2_1up", title="(1./eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1))*eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),6)", _type="WEIGHT"),
            	#ak Variation("wttbar2_1down", title="(1./eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),1))*eff_mass_taulep(jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()+ mu_0_p4->Pt() + el_0_p4->Pt(),7)", _type="WEIGHT"),
            ]
     

        syst = [wttbar_nom, wttbar_fit_syst]

        return syst



    @property
    def systematics(self, **kwargs):

        systematics = super(TTbar, self).systematics[1:] + self.systematics_reweight()     

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
    def __init__(self, *args, **kwargs):
        super(Sh_Wtaunu, self).__init__(*args, **kwargs)
        self.kwargs = kwargs

    def weights(self, **kwargs):
        """WIP: specific weights for Top like top pt weights
        """
        weights = super(Sh_Wtaunu, self).weights(**kwargs)

        if "njets" in self.kwargs:
            if self.kwargs["njets"]:
                for wcat in weights:
                    weights[wcat] += ["njets(n_jets,1)"]
        return weights

    def systematics_Wtjets_reweight(self,**kwargs):

        #print  " IN systematics_WJETS_reweight"
        wwtjets_nom = Systematic(
            "NOMINAL", _type="WEIGHT", variations=[Variation("NOMINAL", title="njets(n_jets,-1)", _type="WEIGHT")], )
        # variations fit
        wwtjets_fit_syst = Systematic("wwtjets_fit", _type="WEIGHT")
        wwtjets_fit_syst.variations = [
            Variation("wwtjets_1up", title="(1./(njets(n_jets,1)))*njets(n_jets,2)", _type="WEIGHT"),
            Variation("wwtjets_1down", title="(1./(njets(n_jets,1)))*njets(n_jets,3)", _type="WEIGHT"),
            #ak Variation("wwtjets1_1up", title="(1./(njets(n_jets,1)))*njets(n_jets,4)", _type="WEIGHT"),
            #ak Variation("wwtjets1_1down", title="(1./(njets(n_jets,1)))*njets(n_jets,5)", _type="WEIGHT"),
        ]

        syst = [wwtjets_nom, wwtjets_fit_syst]

        return syst
 
    def workers(self, **kwargs):
        systematics = kwargs.pop("systematics", [])
        if not systematics:
            systematics = self.systematics

        workers = []
        for systematic in systematics:
            _workers = super(Sh_Wtaunu, self).workers(systematics=[systematic], **kwargs)
            #print "worker in sample wtjets",systematic
            for w in _workers:
                w.name = w.name + "." + systematic.name

            workers += _workers

        return workers

    @property
    def systematics(self, **kwargs):

        systematics = super(Sh_Wtaunu, self).systematics[1:] + self.systematics_Wtjets_reweight()          

        return systematics


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


