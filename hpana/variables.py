import math

from . import MC_CAMPAIGN
import ROOT

__all__ = [
    "VARIABLES",
    "CLF_FEATURES",
    "rQCD_VARS",
    "tau_0_pt",
    "tau_0_n_charged_tracks",
    "tau_0_jet_bdt_score_trans"]

##------------------------------------------------------------------------------------------
## 
class Variable(object):
    """ base class for analysis variables.

    Attributes
    ----------
    name: str, varibale's name
    unit: str, variable's unit
    title: str, variable's title for x axis on histograms
    label: str, label to be shown on the plot(legend)
    binning: tupel, varibale's binning 
    tformula: ROOT.TFormula, to be used with TTree.Draw() method
    blind_cut: ROOT.TCut, to be used for blinding a variables based on some selection
    
    Examples
    --------
    >>> tau_0_pt = Variable(
    "tau_0_pt",
    title='#font[52]{p}_{T}(#tau_{1}) GeV',
    tformula="tau_0_p4->Pt()",
    binning=(20, 0, 400),
    unit='GeV',
    scale=0.001)

    """
    
    def __init__(
            self, name, 
            unit="",
            title=None,
            label=None, 
            scale=None,
            binning=None,
            bins=None,
            tformula=None,
            blind_cut=None,
            **kwargs):
        
        self.name = name
        self.title = title
        self.unit = unit
        self.scale = scale
        self._binning = binning
        self._bins = bins
        
        # - - - - - - - - see __init__.py
        self.mc_camp = kwargs.pop("mc_camp", MC_CAMPAIGN)
        
        # - - - - variable might have different binning for plotting and WS
        self.workspace_binning = kwargs.pop("workspace_binning", None)
        
        # - - - - blinding a varibale based of some selection
        if blind_cut:
            self.blind_cut = blind_cut

        # - - - - setup flexible TFormula string
        if tformula:
            if isinstance(tformula, dict):
                self.tformula = tformula[self.mc_camp]
            elif isinstance(tformula, str):
                self.tformula = tformula
            else :
                raise TypeError("<str> type is expected but found {}".format(type(tformula)) )
        else:
            self.tformula = self.name 
            
        if self.scale:
            self.tformula = "({0}) * ({1})".format(self.scale, self.tformula)
       
    @property    
    def tformula(self):
        """ build a flexible ROOT.TFormula string
        """
        return self.__tformula
    
    @tformula.setter
    def tformula(self, value):
        if isinstance(value, dict):
            self.__tformula = value[self.mc_camp]
        elif isinstance(value, str):
            self.__tformula = value
        else:
            raise TypeError("%r is not supported"%value)
    
    @property 
    def label(self):
        if self._label is None:
            return "%s %s"%(self.name, self.unit) 
        else:
            return self._label
    @label.setter
    def label(self, value):
        self._label = value

    @property
    def binning(self):
        return self._binning
        
    @binning.setter
    def binning(self, value):
        if isinstance(value, dict):
            self._binning = value.values()[0]
        elif isinstance(value, (tuple, list)):
            self._binning = tuple(value)
        else:
            raise TypeError("%r is not supported"%value)
        
    @property
    def bins(self):
        return self._bins

    @bins.setter
    def bins(self, value):
        if isinstance(value, (list, tuple)):
            self._bins = value
            
    def blind(self,low, high):
        pass

    def __repr__(self):
        if not self.scale:
            self.scale = 1.
        return "VARIABLE:: name=%r, tformula=%r, binning=%r, scale=%r, mc_camp=%r"%(
            self.name, self.tformula, self.binning, self.scale, self.mc_camp)

##------------------------------------------------------------------------------------------
## Building the analysis variables; KEEP THEM AS CLEAN AS POSSIBLE :)

# - - - - - - - - tau
tau_0_pt = Variable(
    "tau_0_pt", 
    title='#font[52]{p}_{T}(#tau_{1}) GeV',
    tformula={
        "mc16": "tau_0_p4->Pt()",
        "mc15": "0.001*tau_0_pt"},
    binning=(20, 0, 400),
    unit='GeV',
    scale=1.)

tau_0_eta = Variable(
    "tau_0_eta" , 
    title='#eta(#tau)',
    tformula={
        "mc16": "tau_0_p4->Eta()",
        "mc15": "tau_0_eta"},
    binning=(60, -3., 3.))

tau_0_phi = Variable(
    "tau_0_phi" , 
    title='#phi(#tau)',
    tformula={
        "mc16": "tau_0_p4->Phi()",
        "mc15": "tau_0_phi"},
    binning=(10, -3., 3.))

tau_0_n_charged_tracks = Variable(
    "tau_0_n_charged_tracks",
    title='#font[152]{#tau}_{1} #font[52]{Tracks}',
    tformula={
        "mc16": "tau_0_n_charged_tracks",
        "mc15": "tau_0_n_tracks"},
    binning=(5, -.5, 4.5))

tau_0_q = Variable(
    "tau_0_q",
    title='#font[152]{#tau}_{1} #font[52]{Charge}',
    binning=(5, -2.5, 2.5))

## - - only defined for 1 prong taus
tau_0_upsilon = Variable(
    "tau_0_upsilon", 
    title='#font[52]{#Upsilon}',
    tformula = {
        "mc15": '(tau_0_n_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_pt-1) + -111*(tau_0_n_tracks!=1)',
        "mc16": "((tau_0_n_charged_tracks==1)*tau_0_upsilon_pt_based+ -111*(tau_0_n_charged_tracks!=1))"
    },
    binning=(31, -1.05, 2.05))

tau_0_jet_bdt_score = Variable(
    "tau_0_jet_bdt_score",
    title='#font[152]{#tau}_{1} #font[52]{Jet BDT score}',
    binning=(100, -1., 1.))

tau_0_jet_bdt_score_trans = Variable(
    "tau_0_jet_bdt_score_trans",
    title='#font[152]{#tau}_{1} #font[52]{Jet BDT score signal transformed}',
    tformula = {
        "mc15": "tau_0_jet_bdt_score_sig",
        "mc16": "tau_0_jet_bdt_score_trans",
    },
    binning=(20, 0, 1.), )

tau_0_jet_width = Variable(
    "tau_0_jet_width",
    title='#font[152]{#tau}_{1} #font[52]{Jet width}',
    binning=(40, 0., .4))


# - - - - - - - - MET
met_et = Variable(
    "met_et", 
    title='#font[52]{E}^{miss}_{T} GeV',
    tformula={
        "mc16":"met_p4->Et()",
        "mc15": "met_et"},
    binning=(20, 0, 400),
    scale=1.,
    unit='GeV')

met_etx = Variable(
    "met_etx",
    title='#font[52]{E}^{miss}_{T_{x}}GeV',
    tformula={
        "mc16":"met_p4->Px()",
        "mc15": "met_etx"},
    binning=(20, -75, 75),
    scale=1.,
    unit='GeV')   

met_ety = Variable(
    "met_ety",
    title='#font[52]{E}^{miss}_{T_{y}}GeV',
    tformula={
        "mc16":"met_p4->Py()",
        "mc15": "met_ety"},
    binning=(20, -75, 75),
    scale=1.,
    unit='GeV')

met_phi = Variable(
    "met_phi", 
    title='#font[52]{E}^{miss}_{T} #phi',
    tformula={
        "mc16":"met_p4->Phi()",
        "mc15": "met_phi"},
    binning=(10, -math.pi, math.pi))
 
# - - - - - - - - tau + MET
tau_0_met_dphi = Variable(
    "tau_0_met_dphi",
    title='#Delta#phi(#tau, E^{miss}_{T})',
    # tformula={
    #     "mc15": "TMath::Pi() - fabs( fabs( tau_0_p4->Phi() - met_p4->Phi() ) - TMath::Pi() )",
    #     "mc16": "TMath::Pi() - fabs( fabs( tau_0_p4->Phi() - met_p4->Phi() ) - TMath::Pi() )",
    #     },
    binning=(10, -math.pi, math.pi))

tau_0_met_mt = Variable(
    "tau_0_met_mt",
    title='m_{T}(#tau, E^{miss}_{T})GeV',
    binning=(20, 0, 500), 
    scale=1.,
    unit='GeV')

met_jet_dphi_ratio = Variable(
    "met_jet_dphi_ratio",
    title="#Delta#phi(#tau, E^{miss}_{T})/#Delta#phi(jet, E^{miss}_{T})",
    tformula="(TMath::Pi() - fabs( fabs( tau_0_p4->Phi() - met_p4->Phi() ) - TMath::Pi() ))/ "\
    "(1 + TMath::Pi() - fabs( fabs( jet_0_p4->Phi() - met_p4->Phi() ) - TMath::Pi() )"\
    "+ TMath::Pi() - fabs( fabs( jet_1_p4->Phi() - met_p4->Phi() ) - TMath::Pi() ))",
    binning = (20, 0, 1),   
)

tau_met_jet_dphi_min = Variable(
    "tau_met_jet_dphi_min",
    title="min #Delta#phi(#tau, E^{miss}_{T}, jet)",
    tformula="min(min((TMath::Pi() - fabs(tau_0_p4->Phi() - met_p4->Phi()) )**2 + ( jet_0_p4->Phi() - met_p4->Phi())**2"\
    ", (TMath::Pi() - fabs(tau_0_p4->Phi() - met_p4->Phi()) )**2 + ( jet_0_p4->Phi() - met_p4->Phi())**2)"\
    ", (TMath::Pi() - fabs( tau_0_p4->Phi() - met_p4->Phi()) )**2 + ( jet_1_p4->Phi() - met_p4->Phi())**2) ",
    binning=(20, 0, 10),
)


#WIP - - - - - - - muon

#WIP - - - - - - - electron

#WIP - - - - - - - muon + electron

#WIP - - - - - - - lep + MET


# - - - - - - - - jets
n_jets = Variable(
    "n_jets", 
    title='#font[52]{Number of Selected Jets}',
    binning= (10, -.5, 9.5))

n_bjets = Variable(
    "n_bjets", 
    title='#font[52]{Number of Selected b-Jets}',
    binning= (10, -.5, 9.5))

jet_0_pt =  Variable(
    "jet_0_pt",
    title='#font[52]{p}_{T}(j_{1}) GeV',
    tformula={
        "mc16": "jet_0_p4->Pt()",
        "mc15": "jet_0_pt",},
    binning=(20, 0, 500),
    scale=1.,
    unit='GeV')

bjet_0_pt =  Variable(
    "bjet_0_pt",
    title='#font[52]{p}_{T}lead b-jet GeV',
    tformula={
        "mc16": "bjet_0_p4->Pt()",
        "mc15": "bjet_0_pt",},
    binning=(20, 0, 500),
    scale=1.,
    unit='GeV')

#WIP: FIX ME - - - - subleading light jet (make sure it's not a bjet)
jet_1_pt = Variable(
    "jet_1_pt",
    title='#font[52]{p}_{T}(sub-leading jet) GeV',
    tformula={
        "mc16": "jet_1_p4->Pt()",
        "mc15": "jet_1_pt",},
    binning=(20, 0, 500),
    scale=1.,
    unit='GeV')

jet_0_eta = Variable(
    "jet_0_eta",
    title='#font[152]{#eta}(j_{1})',
    tformula={
        "mc16":"jet_0_p4->Eta()",
        "mc15":"jet_0_eta",},
    binning=(60, -4, 4))

# - - - - - - - -  BDT input features 
bjet_0_met_dphi = Variable(
    "bjet_0_met_dphi", 
    title='#font[52]{#Delta#phi}(b-jet ,E^{miss}_{T})',
    tformula={
        "mc16":"acos(cos(met_p4->Phi() - bjet_0_p4->Phi()))",
        "mc15": "acos(cos(met_phi-bjet_0_phi))",},
    binning=(12, -1., 4))

bjet_0_tau_0_dr = Variable(
    "bjet_0_tau_0_dr", 
    title='#font[52]{#Delta}R(#tau, b-jet)',
    tformula={
        "mc16": "sqrt(acos(cos(tau_0_p4->Phi() - bjet_0_p4->Phi()))**2 + (tau_0_p4->Phi() - bjet_0_p4->Eta())**2)",
        "mc15": "sqrt(acos(cos(tau_0_phi-bjet_0_phi))**2 + (tau_0_eta-bjet_0_eta)**2)",},
    binning=(20, 0, 6.4))


#WIP: - - - - - - - - BDT scores

# - - - - - - - - taujet channel variables list
VARIABLES_TAUJET = [
    tau_0_pt,
    tau_0_eta,
    tau_0_phi, 
    tau_0_n_charged_tracks,
    tau_0_q, 
    tau_0_upsilon,
    
    met_et,
    met_etx,
    met_ety,
    met_phi,
    
    tau_0_met_mt,
    tau_0_met_dphi,
    
    n_jets,
    n_bjets,
    jet_0_pt,
    jet_0_eta,
    bjet_0_pt,
    jet_1_pt,
    
    bjet_0_met_dphi,
    bjet_0_tau_0_dr,
    met_jet_dphi_ratio,
    tau_met_jet_dphi_min,
]


# - - - - - - - - prep all varibales dictionary 
VARIABLES = {}
VARIABLES["taujet"] = VARIABLES_TAUJET

VARIABLES["taulep"] = VARIABLES_TAUJET


# - - - - - - - - BDT input features
CLF_FEATURES = {
    "taujet": [
        tau_0_met_dphi,
        tau_0_pt,
        met_et,
        bjet_0_pt,
        bjet_0_met_dphi,
        bjet_0_tau_0_dr,
        tau_0_upsilon,
        met_jet_dphi_ratio,
        tau_met_jet_dphi_min,
    ],
    "taulep": [],
}




# - - - - - - - -  BDT scores

# - - - - treat properly regions where Y is not modeled well
Y = "(tau_0_n_charged_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_p4->Pt()-1) + -111*(tau_0_n_charged_tracks!=1)"
Y_CORRECTED = "(tau_0_n_charged_tracks==1)*CorrectUpsilon_1D_WCR((2.0*tau_0_allTrk_pt/tau_0_p4->Pt()-1), tau_0_n_charged_tracks)"
BDT_SELECTION_1P = "(tau_0_n_charged_tracks + ({0}>0.95)*({0}<1.05)*(tau_0_jet_bdt_loose == 1)"\
                   "+ ({1}>0.95)*({1}<1.05)*(tau_0_jet_bdt_loose != 1))".format(Y, Y_CORRECTED)

clf_score_GB100_mass_90to120 = Variable(
    "clf_score_GB100_mass_90to120",    
    title='BDT score, 90 to 120 [GeV]',
    tformula= {
        "mc16": "({0}==1)*GB100_mass_90to120_ntracks_1"\
        "+ ({0}!=1)*GB100_mass_90to120_ntracks_3".format("tau_0_n_charged_tracks"),
        },
    binning=(20, 0, 1), 
)
clf_score_GB100_mass_400to400 = Variable(
    "clf_score_GB100_mass_400to400",    
    title='BDT score, 400 [GeV]',
    tformula= {
        "mc16": "({0}==1)*GB100_mass_400to400_ntracks_1"\
        "+ ({0}!=1)*GB100_mass_400to400_ntracks_3".format("tau_0_n_charged_tracks"),
        },
    binning=(20, 0, 1), 
)

BDT_SCORES = {
    "taujet":[
        clf_score_GB100_mass_90to120,
        clf_score_GB100_mass_400to400,
    ],
    "taulep":[],
}

# - - - - - - - - add BDT scores to the list of analysis variables 
#VARIABLES["taujet"] += BDT_SCORES["taujet"]


# - - - - - - - - variables for rQCD calcualtion (different for 1p and 3p taus)
rQCD_VARS = {"1": tau_0_jet_width, "3": tau_0_jet_bdt_score_trans}

# - - - - - - - - variables for extracting FFs shapes 
FFS_TEMPLATE_VARS = (tau_0_pt, tau_0_n_charged_tracks, tau_0_jet_bdt_score_trans)
