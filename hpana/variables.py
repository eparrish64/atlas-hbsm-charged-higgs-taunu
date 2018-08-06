import math

from . import MC_CAMPAIGN
import ROOT

__all__ = [
    "VARIABLES",
    "BDT_FEATURES",
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
        self.tform = tformula
        self.binning = binning
        self.bins = bins
        
        # - - - - - - - - see __init__.py
        self.mc_camp = kwargs.pop("mc_camp", MC_CAMPAIGN)

        # - - - - variable might have different binning for plotting and WS
        self.workspace_binning = kwargs.pop("workspace_binning", None)
        
        # - - - - blinding a varibale based of some selection
        if blind_cut:
            self.blind_cut = blind_cut
            
    @property    
    def tformula(self):
        """ build a flexible ROOT.TFormula string
        """
        if self.tform:
            if isinstance(self.tform, dict):
                tformula = self.tform[self.mc_camp]
            elif isinstance(self.tform, str):
                tformula = self.tform
            else :
                raise TypeError("<str> type is expected but found {}".format(type(self.tform)) )
        else:
            tformula = self.name 
            
        if self.scale:
            tformula = "({0}) * ({1})".format(self.scale, tformula)
            
        return tformula
    
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
        return self.__binning
        
    @binning.setter
    def binning(self, value):
        if isinstance(value, dict):
            self.__binning = value.values()[0]
        elif isinstance(value, (tuple, list)):
            self.__binning = tuple(value)
        else:
            raise TypeError("%r is not supported"%value)
        
    @property
    def bins(self):
        return self.__bins

    @bins.setter
    def bins(self, value):
        if isinstance(value, (list, tuple)):
            self.__bins = value
            
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
        "mc15": "tau_0_pt"},
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
  
tau_0_upsilon = Variable(
    "tau_0_upsilon", 
    title='#font[52]{#Upsilon}',
    tformula = {
        "mc15": '(tau_0_n_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_pt-1) + -111*(tau_0_n_tracks!=1)',
        "mc16": '(tau_0_n_charged_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_p4->Pt()-1) + -111*(tau_0_n_charged_tracks!=1)',
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
    binning=(5, -math.pi, math.pi))

# - - - - - - - - tau + MET
tau_0_met_dphi = Variable(
    "tau_0_met_dphi",
    title='#Delta#phi(#tau, E^{miss}_{T})',
    binning=(10, 0, math.pi))

tau_0_met_mt = Variable(
    "tau_0_met_mt",
    title='m_{T}(#tau, E^{miss}_{T})GeV',
    binning=(50, 0, 500), 
    workspace_binning=(1000, 0, 1000),
    scale=1.,
    unit='GeV')

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
    tau_0_n_charged_tracks,
    tau_0_q, 
    tau_0_upsilon,
    
    met_et, 
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
]


# - - - - - - - - prep all varibales dictionary 
VARIABLES = {}
VARIABLES["taujet"] = VARIABLES_TAUJET

VARIABLES["taulep"] = VARIABLES_TAUJET



# - - - - - - - - BDT input features
BDT_FEATURES = {
    "taujet": [
        tau_0_met_dphi,
        tau_0_pt,
        met_et,
        bjet_0_pt,
        bjet_0_met_dphi,
        bjet_0_tau_0_dr,
        tau_0_upsilon,
    ],
    "taulep": [],
}




# - - - - - - - -  BDT scores

# - - - - treat properly regions where Y is not modeled well
Y = "(tau_0_n_charged_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_p4->Pt()-1) + -111*(tau_0_n_charged_tracks!=1)"
Y_CORRECTED = "(tau_0_n_charged_tracks==1)*CorrectUpsilon_1D_WCR((2.0*tau_0_allTrk_pt/tau_0_p4->Pt()-1), tau_0_n_charged_tracks)"
BDT_SELECTION_1P = "(tau_0_n_charged_tracks + ({0}>0.95)*({0}<1.05)*(tau_0_jet_bdt_loose == 1)"\
                   "+ ({1}>0.95)*({1}<1.05)*(tau_0_jet_bdt_loose != 1))".format(Y, Y_CORRECTED)

FastBDT_sig_90to120_1p3p = Variable(
    "FastBDT_sig_90to120_1p3p",    
    title='BDT score, 90 to 120 [GeV]',
    tformula= {
        "mc16": "({0}==1)*FastBDT_sig_7V_met150_Opt_90to120_1p"\
        "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_90to120_3p".format(BDT_SELECTION_1P),
        },
    binning=(10, 0, 1), 
    blind_cut="(tau_0_n_charged_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p"\
    "+ (tau_0_n_charged_tracks == 3)*FastBDT_sig_6V_met150_Opt_90to120_3p < 0.50",
)

FastBDT_sig_130to160_1p3p = Variable(
    "FastBDT_sig_130to160_1p3p",
    title="BDT score, 130 to 160 [GeV]",
    tformula={
        "mc16": "({0}==1)*FastBDT_sig_7V_met150_Opt_130to160_1p"\
        "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_130to160_3p".format(BDT_SELECTION_1P)
    },
    binning=(10, 0, 1),
    blind_cut="(tau_0_n_charged_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p"\
    "+ (tau_0_n_charged_tracks == 3)*FastBDT_sig_6V_met150_Opt_130to160_3p < 0.50",
)

FastBDT_sig_160to180_1p3p = Variable(
    "FastBDT_sig_160to180_1p3p",
    title="BDT score, 160 to 180 [GeV]",
    tformula={
        "mc16":"({0}==1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
        "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_160to180_3p".format(BDT_SELECTION_1P)
    },
    binning=(10, 0, 1),
    blind_cut="(tau_0_n_charged_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
    "+ (tau_0_n_charged_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p < 0.50",
)

FastBDT_sig_200to400_1p3p = Variable(
    "FastBDT_sig_200to400_1p3p",
    title="BDT score, 200 to 400 [GeV]",
    tformula={
        "mc16": "({0}==1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
        "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_200to400_3p".format(BDT_SELECTION_1P)
    },
    binning=(10, 0, 1),
    blind_cut="(tau_0_n_charged_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
    "+ (tau_0_n_charged_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p < 0.50",
)
FastBDT_sig_500to2000_1p3p = Variable(
    "FastBDT_sig_500to2000_1p3p", 
    title='BDT score, 500 to 2000 [GeV]',
    tformula={
        "mc16": "FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p",
    },
    binning=(10, 0, 1),
    blind_cut='FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p < 0.50',
)


BDT_SCORES = {
    "taujet":[
        FastBDT_sig_90to120_1p3p,
        FastBDT_sig_130to160_1p3p,
        FastBDT_sig_160to180_1p3p,
        FastBDT_sig_200to400_1p3p,
        FastBDT_sig_500to2000_1p3p
    ],
    "taulep":[],
}

# - - - - - - - - add BDT scores to the list of analysis variables 
#VARIABLES["taujet"] += BDT_SCORES["taujet"]


# - - - - - - - - variables for rQCD calcualtion (different for 1p and 3p taus)
rQCD_VARS = {"1": tau_0_jet_width, "3": tau_0_jet_bdt_score_trans}

# - - - - - - - - variables for extracting FFs shapes 
FFS_TEMPLATE_VARS = (tau_0_pt, tau_0_n_charged_tracks, tau_0_jet_bdt_score_trans)
