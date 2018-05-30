import math

from . import MC_CAMPAIGN

__all__ = [ "VARIABLES"]

##------------------------------------------------------------------------------------------
## 
class Variable:
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
        self.binning = binning
        self.bins = bins
        self.tform = tformula
        
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
                if self.mc_camp in self.tform:
                    tformula = self.tform[self.mc_camp]
                else:
                    tformula = self.tform["default"]
            else:
                tformula = self.tform
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
    def binning(self, mc_camp, category):
        if isinstance(self._binning, dict):
            if isinstance(self._binning[mc_camp], dict):
                return self._binning[mc_camp][category]
            elif isinstance(self._binning[mc_camp], tuple):
                return self._binning[mc_camp]
        else:    
            return self._binning
    @binning.setter
    def binning(self, value):
        assert isinstance(value, tuple) or isinstance(value, dict)
        if isinstance(value, tuple):
            assert len(value)==3
            
        self._binning = value

    @property
    def bins(self):
        return self._bins
    @bins.setter
    def bins(self, value):
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
        "mc15": "tau_0_pt"},
    binning=(20, 0, 400),
    unit='GeV',
    scale=0.001)

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
  
upsilon = Variable(
    "upsilon", 
    title='#font[52]{#Upsilon}',
    tformula = {
        "mc15": '(tau_0_n_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_pt-1) + -111*(tau_0_n_tracks!=1)',
        "mc16": '(tau_0_n_charged_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_p4->Pt()-1) + -111*(tau_0_n_charged_tracks!=1)',
    },
    binning=(31, -1.05, 2.05))

# - - - - - - - - MET
met_et = Variable(
    "met_et", 
    title='#font[52]{E}^{miss}_{T} GeV',
    tformula={
        "mc16":"met_p4->Et()",
        "mc15": "met_et"},
    binning=(20, 0, 400),
    scale=0.001,
    unit='GeV')

met_etx = Variable(
    "met_etx",
    title='#font[52]{E}^{miss}_{T_{x}}GeV',
    tformula={
        "mc16":"met_p4->Px()",
        "mc15": "met_etx"},
    binning=(20, -75, 75),
    scale=0.001,
    unit='GeV')   

met_ety = Variable(
    "met_ety",
    title='#font[52]{E}^{miss}_{T_{y}}GeV',
    tformula={
        "mc16":"met_p4->Py()",
        "mc15": "met_ety"},
    binning=(20, -75, 75),
    scale=0.001,
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
    binning=(50, 0, 50), 
    workspace_binning=(1000, 0, 1000),
    scale=0.001,
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
    scale=0.001,
    unit='GeV')

bjet_0_pt =  Variable(
    "bjet_0_pt",
    title='#font[52]{p}_{T}lead b-jet GeV',
    tformula={
        "mc16": "bjet_0_p4->Pt()",
        "mc15": "bjet_0_pt",},
    binning=(20, 0, 500),
    scale=0.001,
    unit='GeV')

#WIP: FIX ME - - - - subleading light jet (make sure it's not a bjet)
jet_1_pt = Variable(
    "jet_1_pt",
    title='#font[52]{p}_{T}(sub-leading jet) GeV',
    tformula={
        "mc16": "jet_1_p4->Pt()",
        "mc15": "jet_1_pt",},
    binning=(20, 0, 500),
    scale=0.001,
    unit='GeV')

jet_0_eta = Variable(
    "jet_0_eta",
    title='#font[152]{#eta}(j_{1})',
    tformula={
        "mc16":"jet_0_p4->Eta()",
        "mc15":"jet_0_eta",},
    binning=(60, -4, 4))

# - - - - - - - -  BDT input features 
MVA_bjet_0_met_dphi = Variable(
    "MVA_bjet_0_met_dphi", 
    title='#font[52]{#Delta#phi}(b-jet ,E^{miss}_{T})',
    tformula={
        "mc16":"acos(cos(met_p4->Phi() - bjet_0_p4->Phi()))",
        "mc15": "acos(cos(met_phi-bjet_0_phi))",},
    binning=(12, -1., 4))

MVA_bjet_0_tau_0_dr = Variable(
    "MVA_bjet_0_tau_0_dr", 
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
    upsilon,
    
    met_et, 
    tau_0_met_mt,
    tau_0_met_dphi,
    
    n_jets,
    n_bjets,
    jet_0_pt,
    jet_0_eta,
    bjet_0_pt,
    jet_1_pt,
    
    MVA_bjet_0_met_dphi,
    MVA_bjet_0_tau_0_dr,
]


# - - - - - - - - prep all varibales dictionary 
VARIABLES = {}
VARIABLES["taujet"] = VARIABLES_TAUJET

VARIABLES["taulep"] = VARIABLES_TAUJET
