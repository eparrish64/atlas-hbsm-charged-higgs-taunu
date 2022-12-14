import math

import numpy as np

from hpana import MC_CAMPAIGN
from hpana.weights import WEIGHTS
import ROOT

__all__ = [
    "VARIABLES",
    "CLF_FEATURES",
    "rQCD_VARS",
    "tau_0_pt",
    "tau_0_n_charged_tracks",
    # "tau_0_jet_bdt_score_trans"
    "tau_0_jet_rnn_score_trans"
    ]

## FIXME: tmp workaround for missing bjet p4 in (2015-2017) systematics 
# BJET_P4_STR = "((jet_0_b_tag_score>0.83)*jet_0_p4->{0}+"\
#     "(jet_0_b_tag_score<0.83 && jet_1_b_tag_score>0.83)*jet_1_p4->{0}+"\
#     "(jet_0_b_tag_score<0.83 && jet_1_b_tag_score<0.83 &&jet_2_b_tag_score>0.83)*jet_2_p4->{0})" 


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
    title='#font[52]{p}_{T}(#tau_{1}) [GeV]',
    tformula="tau_0_p4->Pt()",
    binning=(20, 0, 400),
    unit='[GeV]',
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
            latex=None,
            plot_bins=None,
            **kwargs):
        
        self.name = name
        self.title = title
        self.unit = unit
        self.scale = scale
        self.latex = latex
        self._binning = binning
        self._bins = bins
        self.plot_bins = plot_bins

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

## Building the analysis variables; KEEP THEM AS CLEAN AS POSSIBLE :)

##############################################
## average number of pp interactions,
##############################################
n_avg_int = Variable(
    "n_avg_int",
    title = "avg # of int",
    binning=(1000, 0, 100),
    plot_bins=range(10, 60, 2),
    )

## average number of pp interactions, which is corrected by pileup reweighting tool
n_avg_int_cor = Variable(
    "n_avg_int_cor",
    title = "avg # of int (corrected)",
    binning=(1000, 0, 100),
    plot_bins=range(10, 60, 2),
    )
n_actual_int_cor = Variable(
    "n_actual_int_cor",
    title = "actual number of int (corrected)",
    binning=(1000, 0, 100),
    plot_bins=range(10, 60, 2),
    )


##############################################
# - - - - - - - - 
##############################################
tau_0_pt = Variable(
    "tau_0_pt", 
    title='#font[52]{p}_{T}(#tau_{0}) [GeV]',
    latex=r"$\tau_{p_T}$",
    tformula={
        "mc16": "tau_0_p4->Pt()",
        "mc15": "0.001*tau_0_pt"},
    binning=(18, 40, 400),
    plot_bins={
        "COMMON": range(40, 400, 20),
        "TAULEP_PRESEL": range(30, 300, 10),
        "DILEP_BTAG": range(30, 300, 10),
        "DILEP_BVETO": range(30, 300, 10),
        "ZEE": range(30, 300, 10),
        "SS_TAUEL": range(30, 300, 10),
        "SS_TAUMU": range(30, 300, 10),
        "TAUEL_BVETO": range(30, 300, 10),
        "TAUMU_BVETO": range(30, 300, 10),
        "TTBAR_TAULEP": range(30, 300, 10),
        "SR_TAUMU": range(30, 300, 10),
        "SR_TAUEL": range(30, 300, 10),
        "SR_TAULEP": range(30, 300, 10),
        "SR_TAUMU_PARTIAL": range(30, 300, 10),
        "SR_TAUEL_PARTIAL": range(30, 300, 10),
        "SR_TAULEP_PARTIAL": range(30, 300, 10),
    },
    # binning=(18, 30, 300),
    # plot_bins={
    #     "COMMON": range(30, 300, 15),
    #     # "TAULEP_PRESEL": range(30, 300, 10),
    #     # "DILEP_BTAG": range(30, 300, 10),
    #     # "DILEP_BVETO": range(30, 300, 10),
    #     # "ZEE": range(30, 300, 10),
    #     # "SS_TAUEL": range(30, 300, 10),
    #     # "SS_TAUMU": range(30, 300, 10),
    #     # "TAUEL_BVETO": range(30, 300, 10),
    #     # "TAUMU_BVETO": range(30, 300, 10),
    #     # "TTBAR_TAULEP": range(30, 300, 10),
    #     # "SR_TAUMU": range(30, 300, 10),
    #     # "SR_TAUEL": range(30, 300, 10),
    #     # "SR_TAULEP": range(30, 300, 10),
    #     # "SR_TAUMU_PARTIAL": range(30, 300, 10),
    #     # "SR_TAUEL_PARTIAL": range(30, 300, 10),
    #     # "SR_TAULEP_PARTIAL": range(30, 300, 10),
    # },
    # binning=(200, 30, 1000),
    # plot_bins={
    #     # "COMMON": range(30, 300, 30) + range(300, 500, 50) + range(500,1050,50),
    #     "COMMON": range(30,1000,5)
    #     # "FF_CR_MULTIJET": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
    #     # "FF_CR_WJETS": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
    # },

    unit='[GeV]',
    scale=1.)

tau_0_px = Variable(
    "tau_0_px", 
    title='#font[52]{p}_{x}(#tau_{0}) [GeV]',
    latex=r"$\tau_{p_x}$",
    tformula={
        "mc16": "tau_0_p4->Px()",
        "mc15": "0.001*tau_0_px"},
    binning=(40, -1000, 1000),
    plot_bins={
        "COMMON": range(40, 300, 20) + range(300, 500, 50),
        # "FF_CR_MULTIJET": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
        # "FF_CR_WJETS": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
    },
    unit='[GeV]',
    scale=1.)

tau_0_py = Variable(
    "tau_0_py", 
    title='#font[52]{p}_{y}(#tau_{0}) [GeV]',
    latex=r"$\tau_{p_y}$",
    tformula={
        "mc16": "tau_0_p4->Py()",
        "mc15": "0.001*tau_0_py"},
    binning=(40, -1000, 1000),
    plot_bins={
        "COMMON": range(40, 300, 20) + range(300, 500, 50),
        # "FF_CR_MULTIJET": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
        # "FF_CR_WJETS": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
    },
    unit='[GeV]',
    scale=1.)

tau_0_pz = Variable(
    "tau_0_pz", 
    title='#font[52]{p}_{z}(#tau_{0}) [GeV]',
    latex=r"$\tau_{p_z}$",
    tformula={
        "mc16": "tau_0_p4->Pz()",
        "mc15": "0.001*tau_0_pz"},
    binning=(40, -1000, 1000),
    plot_bins={
        "COMMON": range(40, 300, 20) + range(300, 500, 50),
        # "FF_CR_MULTIJET": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
        # "FF_CR_WJETS": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
    },
    unit='[GeV]',
    scale=1.)

tau_0_eta = Variable(
    "tau_0_eta" , 
    title='#eta(#tau_{0})',
    latex=r"$\tau_{\eta}$",
    tformula={
        "mc16": "tau_0_p4->Eta()",
        "mc15": "tau_0_eta"},
    binning=(26, -2.6, 2.6))

tau_0_phi = Variable(
    "tau_0_phi" , 
    title='#phi(#tau_{0})',
    latex=r"$\tau_{\phi}$",
    tformula={
        "mc16": "tau_0_p4->Phi()",
        "mc15": "tau_0_phi"},
    binning=(20, -3.2, 3.2))

tau_0_E = Variable(
    "tau_0_E", 
    title='#font[52]{E}(#tau_{0}) [GeV]',
    latex=r"$\tau_{E}$",
    tformula={
        "mc16": "tau_0_p4->E()",
        "mc15": "0.001*tau_0_E"},
    binning=(200, 0, 1000),
    plot_bins={
        "COMMON": range(40, 300, 20) + range(300, 500, 50),
        # "FF_CR_MULTIJET": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
        # "FF_CR_WJETS": [30, 35, 40, 45, 50, 60, 80, 100, 200, 3500],
    },
    unit='[GeV]',
    scale=1.)

tau_0_n_charged_tracks = Variable(
    "tau_0_n_charged_tracks",
    title='#font[152]{#tau}_{0} #font[52]{Tracks}',
    tformula={
        "mc16": "tau_0_n_charged_tracks",
        "mc15": "tau_0_n_tracks"},
    binning=(5, -.5, 4.5))

tau_0_q = Variable(
    "tau_0_q",
    title='#font[152]{#tau}_{0} #font[52]{Charge}',
    binning=(5, -2.5, 2.5))

## - - only defined for 1 prong taus
tau_0_upsilon = Variable(
    "tau_0_upsilon", 
    title='#font[52]{#Upsilon_{#tau_{0}}}',
    latex=r"$\tau_{\Upsilon}$",
    tformula = {
        "mc15": '(tau_0_n_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_pt-1) + -111*(tau_0_n_tracks!=1)',
        "mc16": "(-999*(tau_0_n_charged_tracks!=1)) + (tau_0_upsilon_pt_based*(tau_0_n_charged_tracks==1))",
    },
    binning=(22, -1.0, 1.2),
    # plot_bins=(-1, 1.2, 0.05))
    )

tau_0_charged_tracks_0_pt = Variable(
    "tau_0_charged_tracks_0_pt",
    title="#font[52]{p_{T}^{#tau-track_{0}}}",
    latex=r"$p_{T}^{\tau\mathrm{-track}_{0}}$",
    tformula={
        "mc16": "tau_0_charged_tracks_p4->Pt()"
    },
    binning=(18, 40, 400),
    plot_bins={
        "COMMON": range(40, 400, 20),
        "TAULEP_PRESEL": range(30, 300, 10),
        "DILEP_BTAG": range(30, 300, 10),
        "DILEP_BVETO": range(30, 300, 10),
        "ZEE": range(30, 300, 10),
        "SS_TAUEL": range(30, 300, 10),
        "SS_TAUMU": range(30, 300, 10),
        "TAUEL_BVETO": range(30, 300, 10),
        "TAUMU_BVETO": range(30, 300, 10),
        "TTBAR_TAULEP": range(30, 300, 10),
        "SR_TAUMU": range(30, 300, 10),
        "SR_TAUEL": range(30, 300, 10),
        "SR_TAULEP": range(30, 300, 10),
        "SR_TAUMU_PARTIAL": range(30, 300, 10),
        "SR_TAUEL_PARTIAL": range(30, 300, 10),
        "SR_TAULEP_PARTIAL": range(30, 300, 10),
    },
    unit='[GeV]',
    scale=1.)

tau_pol_cms = Variable(
    "tau_pol_cms", 
    title='#font[52]{polcms}',
    latex=r"$polcms$",
    tformula = {
        "mc16": "tau_0_allTrk_pt/tau_0_p4->Pt()",
    },
    binning=(3000, -1.0, 2.0),
    # plot_bins=np.arange(-1, 1.2, 0.05)
    )

tau_0_jet_rnn_score = Variable(
    "tau_0_jet_rnn_score",
    title='#font[152]{#tau}_{0} #font[52]{Jet RNN score}',
    binning=(100, -1., 1.))

tau_0_jet_rnn_score_trans = Variable(
    "tau_0_jet_rnn_score_trans",
    title='#font[152]{#tau}_{0} #font[52]{Jet RNN score signal transformed}',
    tformula = {
        "mc15": "tau_0_jet_rnn_score_sig",
        "mc16": "tau_0_jet_rnn_score_trans",
    },
    binning=(20, 0, 1.), )

tau_0_jet_width = Variable(
    "tau_0_jet_width",
    title='#font[152]{#tau}_{0} #font[52]{Jet width}',
    binning=(40, 0., .4))


effm_tau = Variable(
    "effm_tau",
    title='#font[52]{Eff mass tau} [GeV]',
    tformula="jet_pt_sum + met_p4->Et() + tau_0_p4->Pt()",
    binning=(30, 0, 3000),
    unit='[GeV]',
    scale=1.
    )  

effm_taulep = Variable(
    "effm_taulep",
    title='#font[52]{Eff mass tau lep} [GeV]',
    tformula="jet_pt_sum + met_p4->Et() + tau_0_p4->Pt() + mu_0_p4->Pt()+el_0_p4->Pt()",
    binning=(30, 0, 3000),
    unit='[GeV]',
    scale=1.
    )  

##############################################
##############################################
tau_0_allTrk_eta = Variable(
    "tau_0_allTrk_eta",
    title="tau_0_allTrk_eta",
    binning=(26, -2.6, 2.6),    
    )

tau_0_allTrk_n = Variable(
    "tau_0_allTrk_n",
    title="tau_0_allTrk_n",
    binning=(10, 0, 10),    
    )

tau_0_allTrk_phi = Variable(
    "tau_0_allTrk_phi",
    title="tau_0_allTrk_phi",
    binning=(60, -3, 3),    
    )

tau_0_allTrk_pt = Variable(
    "tau_0_allTrk_pt",
    title="tau_0_allTrk_pt",
    binning=(20, 0, 400),
    )

tau_0_ele_BDTEleScoreTrans_run2 = Variable(
    "tau_0_ele_BDTEleScoreTrans_run2",
    title="tau_0_ele_BDTEleScoreTrans_run2",
    binning=(20, -1, 1),
    )

tau_0_ele_bdt_score_retuned = Variable(
    "tau_0_ele_bdt_score_retuned", 
    title="tau_0_ele_bdt_score_retuned",
    binning=(20, -1, 1),
    )

tau_0_ele_bdt_score_trans_retuned = Variable(
    "tau_0_ele_bdt_score_trans_retuned", 
    title="tau_0_ele_bdt_score_trans_retuned",
    binning=(20, -1, 1),
    )

tau_0_jet_width_trks_dr04 = Variable(
    "tau_0_jet_width_trks_dr04",
    title="tau_0_jet_width_trks_dr04",
    binning=(20, 0, 1),
)

tau_0_leadTrk_eta  = Variable(
    "tau_0_leadTrk_eta",
    title="tau_0_leadTrk_eta",
    binning=(26, -2.6, 2.6),    
)

tau_0_leadTrk_phi = Variable(
    "tau_0_leadTrk_phi",
    title="tau_0_leadTrk_phi",
    binning=(60, -3, 3),   
)

tau_0_leadTrk_pt = Variable(
    "tau_0_leadTrk_pt",
    title="tau_0_leadTrk_pt",
    binning=(20, 0, 400)
    )

##############################################
# - - - - - - - muon
##############################################
mu_0_pt = Variable(
    "mu_0_pt", 
    title='#font[52]{p}_{T}(#mu_{0}) [GeV]',
    tformula="mu_0_p4->Pt()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.)

mu_0_px = Variable(
    "mu_0_px", 
    title='#font[52]{p}_{x}(#mu_{0}) [GeV]',
    tformula="mu_0_p4->Px()",
    binning=(40, -1000, 1000),
    unit='[GeV]',
    scale=1.)

mu_0_py = Variable(
    "mu_0_py", 
    title='#font[52]{p}_{y}(#mu_{0}) [GeV]',
    tformula="mu_0_p4->Py()",
    binning=(40, -1000, 1000),
    unit='[GeV]',
    scale=1.)

mu_0_pz = Variable(
    "mu_0_pz", 
    title='#font[52]{p}_{z}(#mu_{0}) [GeV]',
    tformula="mu_0_p4->Pz()",
    binning=(40, -1000, 1000),
    unit='[GeV]',
    scale=1.)

mu_0_eta = Variable(
    "mu_0_eta",
    title='#font[152]{#eta}(#mu_{0})',
    tformula={
        "mc16":"mu_0_p4->Eta()",
        "mc15":"mu_0_p4->Eta()",},
    binning=(26, -2.6, 2.6))
    
mu_0_phi = Variable(
    "mu_0_phi",
    title='#font[152]{#phi}(#mu_{0})',
    tformula={
        "mc16":"mu_0_p4->Phi()",
        "mc15":"mu_0_p4->Phi()",},
    binning=(64, -3.2, 3.2)
    )

mu_0_E = Variable(
    "mu_0_E", 
    title='#font[52]{E}(#mu_{0}) [GeV]',
    tformula="mu_0_p4->E()",
    binning=(20, 0, 400),
    unit='[GeV]',
    scale=1.)


##############################################
# - - - - - - - electron
##############################################
el_0_pt = Variable(
    "el_0_pt", 
    title='#font[52]{p}_{T}(e_{0}) [GeV]',
    tformula="el_0_p4->Pt()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.
    )

el_0_px = Variable(
    "el_0_px", 
    title='#font[52]{p}_{x}(e_{0}) [GeV]',
    tformula="el_0_p4->Px()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.
    )

el_0_py = Variable(
    "el_0_py", 
    title='#font[52]{p}_{y}(e_{0}) [GeV]',
    tformula="el_0_p4->Py()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.
    )

el_0_pz = Variable(
    "el_0_pz", 
    title='#font[52]{p}_{z}(e_{0}) [GeV]',
    tformula="el_0_p4->Pz()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.
    )

el_0_eta = Variable(
    "el_0_eta",
    title='#font[152]{#eta}(e_{0})',
    tformula={
        "mc16":"el_0_p4->Eta()",
        "mc15":"el_0_p4->Eta()",},
    binning=(26, -2.6, 2.6))
    
el_0_phi = Variable(
    "el_0_phi",
    title='#font[152]{#phi}(e_{0})',
    tformula={
        "mc16":"el_0_p4->Phi()",
        "mc15":"el_0_p4->Phi()",},
    binning=(64, -3.2, 3.2)
    )

el_0_E = Variable(
    "el_0_E", 
    title='#font[52]{E}(e_{0}) [GeV]',
    tformula="el_0_p4->E()",
    binning=(20, 0, 400),
    unit='[GeV]',
    scale=1.
    )

##############################################
# - - - - - - - - jets
##############################################
n_jets = Variable(
    "n_jets", 
    title='#font[52]{Number of Selected Jets}',
    binning= (10, 0, 10))

n_bjets = Variable(
    "n_bjets", 
    title='#font[52]{Number of Selected b-Jets}',
    binning= (10, 0, 10))

n_bjets_DL1r_FixedCutBEff_70 = Variable(
    "n_bjets_DL1r_FixedCutBEff_70", 
    title='#font[52]{Number of Selected b-Jets (FixedCutBEff 70)}',
    binning= (10, 0, 10))

bjet_0_pt =  Variable(
    "bjet_0_pt",
    title='#font[52]{p}_{T}lead b-jet [GeV]',
    latex=r"$b-jet_{p_T}$",
    tformula="bjet_0_p4->Pt()",
    binning=(15, 25, 400),
    plot_bins={
        "COMMON": range(25, 400, 25), # range(40, 100, 10) + range(100, 300, 20) + range(300, 500, 50),
        "TTBAR": range(25, 400, 25),
        "WJETS": range(25, 400, 25),
        "BVETO": range(25, 400, 25),
        "TAUJET_PRESEL": range(25, 400, 25),
        "BVETO_MT100": range(25, 400, 25),
        "TAUJET_PRESEL": range(25, 400, 25),
        "SR_TAUJET": range(25, 400, 25),
        "SR_TAUJET_PARTIAL": range(25, 400, 25),
    },
    scale=1.,
    unit='[GeV]')

bjet_0_px =  Variable(
    "bjet_0_px",
    title='#font[52]{p}_{x}lead b-jet [GeV]',
    latex=r"$b-jet_{p_x}$",
    tformula="bjet_0_p4->Px()",
    binning=(40, -1000, 1000),
    plot_bins=range(-1000, 1000, 40),
    scale=1.,
    unit='[GeV]')

bjet_0_py =  Variable(
    "bjet_0_py",
    title='#font[52]{p}_{y}lead b-jet [GeV]',
    latex=r"$b-jet_{p_y}$",
    tformula="bjet_0_p4->Py()",
    binning=(40, -1000, 1000),
    plot_bins=range(-1000, 1000, 40),
    scale=1.,
    unit='[GeV]')

bjet_0_pz =  Variable(
    "bjet_0_pz",
    title='#font[52]{p}_{z}lead b-jet [GeV]',
    latex=r"$b-jet_{p_z}$",
    tformula="bjet_0_p4->Pz()",
    binning=(40, -1000, 1000),
    plot_bins=range(-1000, 1000, 40),
    scale=1.,
    unit='[GeV]')

bjet_0_eta = Variable(
    "bjet_0_eta",
    title='#font[152]{#eta}(bj_{0})',
    latex=r"$b-jet_{\eta}$",
    tformula={
        "mc16":"bjet_0_p4->Eta()",
        "mc15":"bjet_0_eta",},
    binning=(26, -2.6, 2.6))

bjet_0_phi = Variable(
    "bjet_0_phi",
    title='#font[152]{#phi}(bj_{0})',
    latex=r"$b-jet_{\phi}$",
    tformula={
        "mc16":"bjet_0_p4->Phi()",
        "mc15":"bjet_0_phi",},
    binning=(20, -3.2, 3.2))

bjet_0_E =  Variable(
    "bjet_0_E",
    title='#font[52]{E} lead b-jet [GeV]',
    latex=r"$b-jet_{E}$",
    tformula="bjet_0_p4->E()",
    binning=(200, 25, 1000),
    # plot_bins=range(25, 500, 25),
    scale=1.,
    unit='[GeV]')

bjet_1_pt =  Variable(
    "bjet_1_pt",
    title='#font[52]{p}_{T} sub-leading b-jet [GeV]',
    latex=r"$b-jet_{p_T}^{1}$",
    tformula="bjet_1_p4->Pt()",
    binning=(200, 25, 1000),
    plot_bins=range(25, 1000, 25),
    scale=1.,
    unit='[GeV]')

bjet_1_px =  Variable(
    "bjet_1_px",
    title='#font[52]{p}_{x} sub=leading b-jet [GeV]',
    latex=r"$b-jet_{p_x}^{1}$",
    tformula="bjet_1_p4->Px()",
    binning=(40, -1000, 1000),
    plot_bins=range(-1000, 1000, 40),
    scale=1.,
    unit='[GeV]')

bjet_1_py =  Variable(
    "bjet_1_py",
    title='#font[52]{p}_{y} sub-leading b-jet [GeV]',
    latex=r"$b-jet_{p_y}^{1}$",
    tformula="bjet_1_p4->Py()",
    binning=(40, -1000, 1000),
    plot_bins=range(-1000, 1000, 40),
    scale=1.,
    unit='[GeV]')

bjet_1_pz =  Variable(
    "bjet_1_pz",
    title='#font[52]{p}_{z} sub-leading b-jet [GeV]',
    latex=r"$b-jet_{p_z}^{1}$",
    tformula="bjet_1_p4->Pz()",
    binning=(40, -1000, 1000),
    plot_bins=range(-1000, 1000, 40),
    scale=1.,
    unit='[GeV]')

bjet_1_eta = Variable(
    "bjet_1_eta",
    title='#font[152]{#eta}(bj_{1})',
    latex=r"$b-jet_{\eta}^{1}$",
    tformula={
        "mc16":"bjet_1_p4->Eta()",
        "mc15":"bjet_1_eta",},
    binning=(26, -2.6, 2.6))

bjet_1_phi = Variable(
    "bjet_1_phi",
    title='#font[152]{#phi}(bj_{1})',
    latex=r"$b-jet_{\phi}^{1}$",
    tformula={
        "mc16":"bjet_1_p4->Phi()",
        "mc15":"bjet_1_phi",},
    binning=(20, -3.2, 3.2))

bjet_1_E =  Variable(
    "bjet_1_E",
    title='#font[52]{E} sub-leading b-jet [GeV]',
    latex=r"$b-jet_{E}^{1}$",
    tformula="bjet_1_p4->E()",
    binning=(200, 25, 1000),
    # plot_bins=range(25, 500, 25),
    scale=1.,
    unit='[GeV]')

jet_0_pt =  Variable(
    "jet_0_pt",
    title='#font[52]{p}_{T}(j_{0}) [GeV]',
    latex=r"$j^{0}_{p_T}$",
    tformula={
        "mc16": "jet_0_p4->Pt()",
        "mc15": "jet_0_pt",},
    binning=(20, 25, 525),
    scale=1.,
    unit='[GeV]')

jet_0_px =  Variable(
    "jet_0_px",
    title='#font[52]{p}_{x}(j_{0}) [GeV]',
    latex=r"$j^{0}_{p_x}$",
    tformula={
        "mc16": "jet_0_p4->Px()",
        "mc15": "jet_0_px",},
    binning=(40, -1000, 1000),
    scale=1.,
    unit='[GeV]')

jet_0_py =  Variable(
    "jet_0_py",
    title='#font[52]{p}_{y}(j_{0}) [GeV]',
    latex=r"$j^{0}_{p_y}$",
    tformula={
        "mc16": "jet_0_p4->Py()",
        "mc15": "jet_0_py",},
    binning=(40, -1000, 1000),
    scale=1.,
    unit='[GeV]')

jet_0_pz =  Variable(
    "jet_0_pz",
    title='#font[52]{p}_{z}(j_{0}) [GeV]',
    latex=r"$j^{0}_{p_z}$",
    tformula={
        "mc16": "jet_0_p4->Pz()",
        "mc15": "jet_0_pz",},
    binning=(40, -1000, 1000),
    scale=1.,
    unit='[GeV]')

jet_0_eta = Variable(
    "jet_0_eta",
    title='#font[152]{#eta}(j_{0})',
    latex=r'$j^{0}_{\eta}$',
    tformula={
        "mc16":"jet_0_p4->Eta()",
        "mc15":"jet_0_eta",},
    binning=(26, -2.6, 2.6))

jet_0_phi = Variable(
    "jet_0_phi",
    title='#font[152]{#phi}(j_{0})',
    latex=r'$j^{0}_{\phi}$',
    tformula={
        "mc16":"jet_0_p4->Phi()",
        "mc15":"jet_0_phi",},
    binning=(20, -3.2, 3.2))

jet_0_E =  Variable(
    "jet_0_E",
    title='#font[52]{E}(j_{0}) [GeV]',
    latex=r"$j^{0}_{E}$",
    tformula={
        "mc16": "jet_0_p4->E()",
        "mc15": "jet_0_pt",},
    binning=(20, 25, 525),
    scale=1.,
    unit='[GeV]')

#WIP: FIX ME - - - - subleading light jet (make sure it's not a bjet)
jet_1_pt = Variable(
    "jet_1_pt",
    title='#font[52]{p}_{T}(sub-leading jet) [GeV]',
    tformula={
        "mc16": "jet_1_p4->Pt()",
        "mc15": "jet_1_pt",},
    binning=(20, 25, 525),
    scale=1.,
    unit='[GeV]')

jet_1_eta = Variable(
    "jet_1_eta",
    title='#font[152]{#eta}(j_{1})',
    latex=r'$j^{1}_{\eta}$',
    tformula={
        "mc16":"jet_1_p4->Eta()",
        "mc15":"jet_1_eta",},
    binning=(26, -2.6, 2.6))

jet_1_phi = Variable(
    "jet_1_phi",
    title='#font[152]{#phi}(j_{1})',
    latex=r'$j^{1}_{\phi}$',
    tformula={
        "mc16":"jet_1_p4->Phi()",
        "mc15":"jet_1_phi",},
    binning=(20, -3.2, 3.2))

jet_2_pt = Variable(
    "jet_2_pt",
    title='#font[52]{p}_{T}(sub-sub-leading jet) [GeV]',
    tformula={
        "mc16": "jet_2_p4->Pt()",
        "mc15": "jet_2_pt",},
    binning=(20, 25, 525),
    scale=1.,
    unit='[GeV]')

jet_2_eta = Variable(
    "jet_2_eta",
    title='#font[152]{#eta}(j_{2})',
    latex=r'$j^{2}_{\eta}$',
    tformula={
        "mc16":"jet_2_p4->Eta()",
        "mc15":"jet_2_eta",},
    binning=(26, -2.6, 2.6))

jet_2_phi = Variable(
    "jet_2_phi",
    title='#font[152]{#phi}(j_{2})',
    latex=r'$j^{2}_{\phi}$',
    tformula={
        "mc16":"jet_2_p4->Phi()",
        "mc15":"jet_2_phi",},
    binning=(20, -3.2, 3.2))


##############################################
# - - - - - - - - MET
##############################################
met_et = Variable(
    "met_et", 
    title='#font[52]{E}^{miss}_{T} [GeV]',
    latex=r"$E^{miss}_{T}$",
    tformula={
        "mc16":"met_p4->Et()",
        "mc15": "met_et"},
    binning=(18, 50, 500),
    plot_bins={
        "COMMON": range(50, 500, 25),
        "TAUJET_PRESEL": range(150, 500, 25),
        "BVETO_MT100": range(150, 500, 25),
        "BVETO": range(150, 500, 25),
        "TTBAR": range(150, 500, 25),
        "WJETS": range(150, 500, 25),
        "SR_TAUJET": range(150, 500, 25),
        "SR_TAUJET_PARTIAL": range(150, 500, 25),

        "TAULEP_PRESEL": range(50, 300, 25),
        "DILEP_BTAG": range(50, 300, 25),
        "DILEP_BVETO": range(50, 300, 25),
        "ZEE": range(50, 300, 25),
        "SS_TAUEL": range(50, 300, 25),
        "SS_TAUMU": range(50, 300, 25),
        "TAUEL_BVETO": range(50, 300, 25),
        "TAUMU_BVETO": range(50, 300, 25),
        "TTBAR_TAULEP": range(50, 300, 25),
        "SR_TAUMU": range(50, 300, 25),
        "SR_TAUEL": range(50, 300, 25),
        "SR_TAULEP": range(50, 300, 25),
        "SR_TAUMU_PARTIAL": range(50, 300, 25),
        "SR_TAUEL_PARTIAL": range(50, 300, 25),
        "SR_TAULEP_PARTIAL": range(50, 300, 25),
    },
    scale=1.,
    unit='[GeV]')

met_ex = Variable(
    "met_ex",
    title='#font[52]{E}^{miss}_{x}[GeV]',
    tformula={
        "mc16":"met_p4->Px()",
        # "mc15": "met_ex"
        },
    binning=(40, -1000, 1000),
    scale=1.,
    unit='[GeV]')   

met_ey = Variable(
    "met_ey",
    title='#font[52]{E}^{miss}_{y}[GeV]',
    tformula={
        "mc16":"met_p4->Py()",
        # "mc15": "met_ety"
        },
    binning=(40, -1000, 1000),
    scale=1.,
    unit='[GeV]')

met_phi = Variable(
    "met_phi", 
    title='#font[52]{E}^{miss}_{T} {#phi}',
    latex=r"$E^{miss}_{T} \phi$",
    tformula={
        "mc16":"met_p4->Phi()",
        "mc15": "met_phi"},
    binning=(10, -math.pi, math.pi))
 
##############################################
# - - - - - - - - tau + MET
##############################################
tau_0_met_dphi = Variable(
    "tau_0_met_dphi",
    title='#Delta#phi(#tau, E^{miss}_{T})',
    latex=r"$\Delta\phi(\tau, E^{miss}_{T})$",
    tformula={
        "mc16":"abs(acos(cos(met_p4->Phi() - {})))".format("tau_0_p4->Phi()"),
        "mc15": "abs(acos(cos(met_phi-tau_0_eta)))",},
    binning=(16, 0.0, math.pi),
    # plot_bins=np.arange(-2, 2.4, .4)
    )

tau_0_met_mt = Variable(
    "tau_0_met_mt",
    title='m_{T}(#tau, E^{miss}_{T})[GeV]',
    latex=r"$m_{T}(\tau, E^{miss}_{T})$",
    binning=(16, 0, 400),
    plot_bins={
        "COMMON": range(0,400, 25), # range(40, 100, 10) + range(100, 300, 20) + range(300, 500, 50),
        "TTBAR": range(0, 125, 25),
        "WJETS": range(0, 125, 25),
        "BVETO": range(50, 400, 25),
        "BVETO_MT100": range(100, 400, 25),
        "SR_TAUJET": range(50, 400, 25),
        "SR_TAUJET_PARTIAL": range(50, 400, 25),
        # "FF_CR_MULTIJET": range(50, 200, 15) + range(200, 500, 50),
        # "FF_CR_WJETS": range(50, 200, 15) + range(200, 500, 50),
    },        
    scale=1.,
    unit='[GeV]')


##############################################
# - - - - - - - - tau + JET
##############################################
met_jet_dphi_ratio = Variable(
    "met_jet_dphi_ratio",
    title="#Delta#phi(#tau, E^{miss}_{T})/#Delta#phi(jet, E^{miss}_{T})",
    latex=r"$\Delta\phi(\tau, E^{miss}_{T})/\Delta\phi(j, E^{miss}_{T})$",
    tformula="(TMath::Pi() - fabs( fabs( tau_0_p4->Phi() - met_p4->Phi() ) - TMath::Pi() ))/ "\
    "(1 + TMath::Pi() - fabs( fabs( jet_0_p4->Phi() - met_p4->Phi() ) - TMath::Pi() )"\
    "+ TMath::Pi() - fabs( fabs( jet_1_p4->Phi() - met_p4->Phi() ) - TMath::Pi() ))",
    binning = (10, 0, 2),
    # plot_bins=np.arange(0, 1, 0.05),   
)

tau_met_jet_dphi_min = Variable(
    "tau_met_jet_dphi_min",
    title="min #Delta#phi(#tau, E^{miss}_{T}, jet)",
    latex=r"min $\Delta\phi(\tau, E^{miss}_{T}, j)$",
    tformula="min(min((TMath::Pi() - fabs(tau_0_p4->Phi() - met_p4->Phi()) )**2 + ( jet_0_p4->Phi() - met_p4->Phi())**2"\
    ", (TMath::Pi() - fabs(tau_0_p4->Phi() - met_p4->Phi()) )**2 + ( jet_0_p4->Phi() - met_p4->Phi())**2)"\
    ", (TMath::Pi() - fabs( tau_0_p4->Phi() - met_p4->Phi()) )**2 + ( jet_1_p4->Phi() - met_p4->Phi())**2) ",
    binning=(20, 0, 10),
)

###########################AK
## FIX me! Only NOT b-tagged jets to be used
tau0_met_dp = Variable(
    "tau0_met_dp",
    title='#Delta#phi(#tau, E^{miss}_{T})',
    latex=r"$\Delta\phi(\tau, E^{miss}_{T})$",
    tformula="((fabs(tau_0_p4->Phi() - met_p4->Phi())) > TMath::Pi())*(2* TMath::Pi() - fabs(tau_0_p4->Phi() - met_p4->Phi())) + ((fabs(tau_0_p4->Phi() - met_p4->Phi())) <= TMath::Pi())*(fabs(tau_0_p4->Phi() - met_p4->Phi()))", 
    ##
    #tformula="(fabs(tau_0_p4->Phi() - met_p4->Phi() )) > TMath::Pi() ? 2* TMath::Pi() - fabs(tau_0_p4->Phi() - met_p4->Phi() )  : fabs(tau_0_p4->Phi() - met_p4->Phi() )",
    #tformula="2* 3.14 - fabs(tau_0_p4->Phi() - met_p4->Phi() )",
    binning=(20, -1, 4),
)

jet0_met_dp = Variable(
    "jet0_met_dp",
    title='#Delta#phi(#jet0, E^{miss}_{T})',
    latex=r"$\Delta\phi(jet0, E^{miss}_{T})$",
    tformula="((fabs(jet_0_p4->Phi() - met_p4->Phi())) > TMath::Pi())*(2* TMath::Pi() - fabs(jet_0_p4->Phi() - met_p4->Phi())) + ((fabs(jet_0_p4->Phi() - met_p4->Phi())) <= TMath::Pi())*(fabs(jet_0_p4->Phi() - met_p4->Phi()))",
    #tformula="(fabs(jet_0_p4->Phi() - met_p4->Phi())) > 3.14 ? 2* 3.14 - fabs(jet_0_p4->Phi() - met_p4->Phi())  : fabs(jet_0_p4->Phi() - met_p4->Phi())",
    #tformula="(fabs(jet_0_p4->Phi() - met_p4->Phi())) > TMath::Pi() ? 2* TMath::Pi() - fabs(jet_0_p4->Phi() - met_p4->Phi())  : fabs(jet_0_p4->Phi() - met_p4->Phi())",
    binning=(20, -1, 4),
)

jet1_met_dp = Variable(
    "jet1_met_dp",
    title='#Delta#phi(#jet1, E^{miss}_{T})',
    latex=r"$\Delta\phi(jet1, E^{miss}_{T})$",
    tformula="((fabs(jet_1_p4->Phi() - met_p4->Phi())) > TMath::Pi())*(2* TMath::Pi() - fabs(jet_1_p4->Phi() - met_p4->Phi())) + ((fabs(jet_1_p4->Phi() - met_p4->Phi())) <= TMath::Pi())*(fabs(jet_1_p4->Phi() - met_p4->Phi()))",
    #tformula="(fabs(jet_1_p4->Phi() - met_p4->Phi())) > TMath::Pi() ? 2* TMath::Pi() - fabs(jet_1_p4->Phi() - met_p4->Phi())  : fabs(jet_1_p4->Phi() - met_p4->Phi())",
    binning=(20, -1, 4),
    #plot_bins=np.arange(-2, 2.4, .4)
)

jet2_met_dp = Variable(
    "jet2_met_dp",
    title='#Delta#phi(#jet2, E^{miss}_{T})',
    latex=r"$\Delta\phi(jet2, E^{miss}_{T})$",
    tformula="((fabs(jet_2_p4->Phi() - met_p4->Phi())) > TMath::Pi())*(2* TMath::Pi() - fabs(jet_2_p4->Phi() - met_p4->Phi())) + ((fabs(jet_2_p4->Phi() - met_p4->Phi())) <= TMath::Pi())*(fabs(jet_2_p4->Phi() - met_p4->Phi()))",
    #tformula="(fabs(jet_2_p4->Phi() - met_p4->Phi())) > TMath::Pi() ? 2* TMath::Pi() - fabs(jet_2_p4->Phi() - met_p4->Phi())  : fabs(jet_2_p4->Phi() - met_p4->Phi())",
    binning=(20, -1, 4),
)

taujet0_dp  = Variable(
    "taujet0_dp",
    title='taujet0_dp)',
    latex="taujet0_dp",
    tformula="sqrt((TMath::Pi()-"+tau0_met_dp.tformula+")**2+ "+jet0_met_dp.tformula+"**2)",
    binning=(20, -1, 4),
)

taujet1_dp  = Variable(
    "taujet1_dp",
    title='taujet1_dp)',
    latex="taujet1_dp",
    tformula="sqrt((TMath::Pi()-"+tau0_met_dp.tformula+")**2+ "+jet1_met_dp.tformula+"**2)",
    binning=(20, -1, 4),
)

taujet2_dp  = Variable(
    "taujet2_dp",
    title='taujet2_dp)',
    latex="taujet2_dp",
    tformula="sqrt((TMath::Pi()-"+tau0_met_dp.tformula+")**2+ "+jet2_met_dp.tformula+"**2)",
    binning=(20, -1, 4),
)

r_min = Variable(
    "r_min",
    title="r_min_bb",
    latex="r_min_bb",
    tformula="min(min("+taujet0_dp.tformula+","+taujet1_dp.tformula+"),"+taujet2_dp.tformula+")",
    binning=(20, 0, 10),
)


r_min_cut = Variable(
    "r_min_cut",
    title="r_min_bb",
    latex="r_min_bb",
    tformula="((tau_0_allTrk_pt/tau_0_p4->Pt() > 0.75)*(min(min("+taujet0_dp.tformula+","+taujet1_dp.tformula+"),"+taujet2_dp.tformula+")))",
    binning=(20, 0, 10),
)

##########################AK

bjet_0_met_dphi = Variable(
    "bjet_0_met_dphi", 
    title='#font[52]{#Delta#phi}(b-jet ,E^{miss}_{T})',
    latex=r"$\Delta\phi(b-jet ,E^{miss}_{T})$",
    tformula={
        "mc16":"abs(acos(cos(met_p4->Phi() - {})))".format("bjet_0_p4->Phi()"),
        "mc15": "abs(acos(cos(met_phi-bjet_0_eta)))",},
    binning=(16, .0, math.pi),
    # plot_bins=np.arange(0, 4, 0.5),
    )

bjet_0_tau_0_dr = Variable(
    "bjet_0_tau_0_dr", 
    title='#font[52]{#Delta}R(#tau, b-jet)',
    latex=r"$\Delta R(\tau, b-jet)$",
    tformula={
        "mc16": "sqrt(acos(cos(tau_0_p4->Phi() - {0}))**2 + (tau_0_p4->Eta() - {1})**2)".format(
            "bjet_0_p4->Phi()", "bjet_0_p4->Eta()"),
        "mc15": "sqrt(acos(cos(tau_0_phi-bjet_0_eta))**2 + (tau_0_eta-bjet_0_eta)**2)",},
    binning=(25, 0, 5))


##############################################
# - - - - - - - mu + el
##############################################
lep_0_pt = Variable(
    "lep_0_pt", 
    title='#font[52]{p}_{T}(l_{0}) [GeV]',
    latex=r"$\ell_{p_T}$",
    tformula="mu_0_p4->Pt()+el_0_p4->Pt()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.)

lep_0_px = Variable(
    "lep_0_px", 
    title='#font[52]{p}_{x}(l_{0}) [GeV]',
    latex=r"$\ell_{p_x}$",
    tformula="mu_0_p4->Px()+el_0_p4->Px()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.)

lep_0_py = Variable(
    "lep_0_py", 
    title='#font[52]{p}_{y}(l_{0}) [GeV]',
    latex=r"$\ell_{p_y}$",
    tformula="mu_0_p4->Py()+el_0_p4->Py()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.)

lep_0_pz = Variable(
    "lep_0_pz", 
    title='#font[52]{p}_{z}(l_{0}) [GeV]',
    latex=r"$\ell_{p_z}$",
    tformula="mu_0_p4->Pz()+el_0_p4->Pz()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.)

lep_0_eta = Variable(
    "lep_0_eta" , 
    title='#font[52]{#eta}(l_{0})',
    latex=r"$l_{\eta}$",
    tformula={
        "mc16": "mu_0_p4->Eta()+el_0_p4->Eta()",
        "mc15": "mu_0_p4->Eta()+el_0_p4->Eta()"},
    binning=(26, -2.6, 2.6),
    # plot_bins=np.arange(-2.6, 2.6, 0.2)
    )

lep_0_phi = Variable(
    "lep_0_phi" , 
    title='#font[52]{#phi}(l_{0})',
    latex=r"$l_{\phi}$",
    tformula={
        "mc16": "mu_0_p4->Phi()+el_0_p4->Phi()",
        "mc15": "mu_0_p4->Phi()+el_0_p4->Phi()"},
    binning=(64, -3.2, 3.2),
    # plot_bins=np.arange(-2.5, 2.5, 0.1)
    )

lep_0_E = Variable(
    "lep_0_E", 
    title='#font[52]{E}(l_{0}) [GeV]',
    latex=r"$\ell_{E}$",
    tformula="mu_0_p4->E()+el_0_p4-E()",
    binning=(18, 30, 300),
    unit='[GeV]',
    scale=1.)

tau_0_lep_0_mass = Variable(
    "tau_0_lep_0_mass", 
    title='#font[52]{m}_{#tau l} [GeV]',
    latex=r"$m_{ll}$",
    tformula="sqrt((tau_0_p4->E()+el_0_p4->E())**2 - ((tau_0_p4->Px()+el_0_p4->Px())**2 + (tau_0_p4->Py()+el_0_p4->Py())**2 + (tau_0_p4->Pz()+el_0_p4->Pz())**2))",
    binning=(50, 40, 140),
    plot_bins=range(40, 140, 2),
    unit='[GeV]',
    scale=1.)

##############################################
# - - - - - - - lep + tau
##############################################
tau_0_lep_0_dr = Variable(
    "tau_0_lep_0_dr",
    title='#Delta#phi(l, #tau)',
    latex=r"$\Delta\phi(\ell, \tau)$",
    tformula="sqrt(acos(cos(tau_0_p4->Phi() - el_0_p4->Phi() - mu_0_p4->Phi()))**2 + (tau_0_p4->Eta() - el_0_p4->Eta() - mu_0_p4->Eta())**2)",
    binning=(20, 0, 6.4))

##############################################
# - - - - - - - lep + MET
##############################################
mu_0_met_dphi = Variable(
    "mu_0_met_dphi",
    title='#Delta#phi(#mu, E^{miss}_{T})',
    latex=r"$\Delta\phi(\mu, E^{miss}_{T})$",
    tformula="abs(acos(cos(met_p4->Phi() - mu_0_p4->Phi())))",
    binning=(16, 0.0, math.pi),
    # plot_bins=np.arange(0, 3.2, 0.2)
    )

el_0_met_dphi = Variable(
    "el_0_met_dphi",
    title='#Delta#phi(e, E^{miss}_{T})',
    latex=r"$\Delta\phi(e, E^{miss}_{T})$",
    tformula="abs(acos(cos(met_p4->Phi() - el_0_p4->Phi())))",
    binning=(16, 0.0, math.pi),
    # plot_bins=np.arange(0, 3.2, 0.2)
    )

lep_0_met_dphi = Variable(
    "lep_0_met_dphi",
    title='#Delta#phi(l, E^{miss}_{T})',
    latex=r"$\Delta\phi(\ell, E^{miss}_{T})$",
    tformula="abs(acos(cos(met_p4->Phi() - el_0_p4->Phi() - mu_0_p4->Phi())))",
    binning=(16, 0.0, math.pi),
    # plot_bins=np.arange(0, 3.2, 0.2)
    )

lep_0_met_mt = Variable(
    "lep_0_met_mt",
    title='m_{T}(l, E^{miss}_{T})[GeV]',
    latex=r"$m_{T}(\ell, E^{miss}_{T}$)",
    binning=(16, 0.0, 400),
    plot_bins=range(0, 400, 25),
    tformula="sqrt(2 * (el_0_p4->Pt() + mu_0_p4->Pt()) * met_p4->Et() * (1 - cos(met_p4->Phi() - el_0_p4->Phi() - mu_0_p4->Phi() ) ) )", 
    unit='[GeV]')

##############################################
# - - - - - - - lep + jet
##############################################
bjet_0_lep_0_dr = Variable(
    "bjet_0_lep_0_dr",
    title='#Delta#phi(l, b-jet)',
    latex=r"$\Delta\phi(\ell, b-jet)$",
    tformula="sqrt(acos(cos({0} - el_0_p4->Phi() - mu_0_p4->Phi()))**2 + ({1} - el_0_p4->Eta() - mu_0_p4->Eta())**2)".format(
        "bjet_0_p4->Phi()", "bjet_0_p4->Eta()"),
    binning=(25, 0, 5)
    )

bjet_0_el_0_dr = Variable(
    "bjet_0_el_0_dr",
    title='#Delta#phi(e, b-jet)',
    latex=r"$\Delta\phi(e, b-jet)$",
    tformula="sqrt(acos(cos({0} - el_0_p4->Phi() ))**2 + ({1} - el_0_p4->Eta() )**2)".format(
        "bjet_0_p4->Phi()", "bjet_0_p4->Eta()"),
    binning=(25, 0, 5)
    )

bjet_0_mu_0_dr = Variable(
    "bjet_0_mu_0_dr",
    title='#Delta#phi(#mu, b-jet)',
    latex=r"$\Delta\phi(\mu, b-jet)$",
    tformula="sqrt(acos(cos({0} - mu_0_p4->Phi() ))**2 + ({1} - mu_0_p4->Eta() )**2)".format(
        "bjet_0_p4->Phi()", "bjet_0_p4->Eta()"),
    binning=(25, 0, 5)
    )

##############################################
# - - - - - - - TruthMass
##############################################
TruthMass = Variable(
    "TruthMass",
    title="TruthMass",
    binning=(300, 0., 3000.)
    )

##############################################
# - - - - - - - Pileup Weight
##############################################
Pileup_Weight = Variable(
    "Pileup_Weight",
    title='pileup weight',
    tformula="NOMINAL_pileup_combined_weight",
    binning=(1000, -5, 5),
    # plot_bins=np.arange(-5,5,0.1)
    )

##############################################
# - - - - - - - Pileup Weight
##############################################
mc_Weight = Variable(
    "mc_weight",
    title='mc weight',
    tformula="weight_mc",
    binning=(1000, -2000, 2000),
    # plot_bins=np.arange(-5,5,0.1)
    )

##-----------------------------------------------------------------
# - - - - - - - - taujet channel variables list
##-----------------------------------------------------------------
VARIABLES_TAUJET = [
    n_avg_int_cor,
    n_actual_int_cor,
    
    tau_0_pt,
    # tau_0_px,
    # tau_0_py,
    # tau_0_pz,
    tau_0_eta,
    tau_0_phi,
    # tau_0_E,
    tau_0_n_charged_tracks,
    tau_0_q, 
    tau_0_upsilon,
    tau_0_charged_tracks_0_pt,
    tau_0_met_mt,
    tau_0_met_dphi,

    met_et,
    met_phi,
    met_jet_dphi_ratio,
    
    n_jets,
    n_bjets_DL1r_FixedCutBEff_70,
    
    jet_0_pt,
    jet_0_eta,
    jet_0_phi,

    jet_1_pt,
    jet_1_eta,
    jet_1_phi,

    jet_2_pt,
    jet_2_eta,
    jet_2_phi,

    bjet_0_pt,
    bjet_0_eta,
    bjet_0_phi,
    bjet_0_met_dphi,
    bjet_0_tau_0_dr,

    # bjet_1_pt,   
    # bjet_1_eta,
    # bjet_1_phi,

    effm_tau,
    # Pileup_Weight,
    # mc_Weight,
]

##-----------------------------------------------------------------
# - - - - - - - - taulep channel variables list
##----------------------------------------------------------b-------
VARIABLES_TAULEP = [
    n_avg_int_cor,
    n_actual_int_cor,

    tau_0_pt,
    # tau_0_px,
    # tau_0_py,
    # tau_0_pz,
    tau_0_eta,
    tau_0_phi,
    # tau_0_E,
    tau_0_n_charged_tracks,
    tau_0_q, 
    tau_0_upsilon,
    tau_0_charged_tracks_0_pt,
    tau_0_met_mt,
    tau_0_met_dphi,
    tau_0_lep_0_mass,
    tau_0_lep_0_dr,

    lep_0_pt,
    # lep_0_px,
    # lep_0_py,
    # lep_0_pz,
    lep_0_eta,
    lep_0_phi,
    # lep_0_E,
    lep_0_met_mt,
    lep_0_met_dphi,

    el_0_pt,
    # el_0_px,
    # el_0_py,
    # el_0_pz,
    el_0_eta,
    el_0_phi,
    # el_0_E,
    el_0_met_dphi,

    mu_0_pt,
    # mu_0_px,
    # mu_0_py,
    # mu_0_pz,
    mu_0_eta,
    mu_0_phi,
    # mu_0_E,
    mu_0_met_dphi,

    met_et,
    # met_ex,
    # met_ey,
    met_phi,
    met_jet_dphi_ratio,

    n_jets,
    n_bjets_DL1r_FixedCutBEff_70,

    jet_0_pt,
    # jet_0_px,
    # jet_0_py,
    # jet_0_pz,
    jet_0_eta,
    jet_0_phi,
    # jet_0_E,

    jet_1_pt,
    # jet_1_px,
    # jet_1_py,
    # jet_1_pz,
    jet_1_eta,
    jet_1_phi,
    # jet_1_E,

    bjet_0_pt,
    # bjet_0_px,
    # bjet_0_py,
    # bjet_0_pz,
    bjet_0_eta,
    bjet_0_phi,
    # bjet_0_E,
    
    bjet_0_met_dphi,
    bjet_0_tau_0_dr,
    bjet_0_lep_0_dr,
    bjet_0_el_0_dr,
    bjet_0_mu_0_dr,

    effm_taulep,

    # Pileup_Weight,
    # mc_Weight,
]


# - - - - - - - - prep all variables dictionary 
VARIABLES = {}
VARIABLES["taujet"] = VARIABLES_TAUJET
VARIABLES["taulep"] = VARIABLES_TAULEP


##-----------------------------------------------------------------
# - - - - - - - - BDT input features
##-----------------------------------------------------------------
CLF_FEATURES = {
    "taujet": {
        "LOW": [
            # tau_0_met_dphi,
            # tau_0_pt,
            # met_et,
            # bjet_0_pt,
            # bjet_0_met_dphi,
            # bjet_0_tau_0_dr,
            # met_jet_dphi_ratio,
            # tau_0_upsilon,
            # TruthMass,
            tau_0_pt,
            tau_0_eta,
            tau_0_phi,
            tau_0_E,
            tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,
            bjet_0_pt,
            bjet_0_eta,
            bjet_0_phi,
            bjet_0_E,
            met_et,
            met_phi,
            jet_0_pt,
            jet_0_eta,
            jet_0_phi,
            jet_0_E,
            jet_1_pt,
            jet_1_eta,
            jet_1_phi,
            # jet_1_E,
            jet_2_pt,
            jet_2_eta,
            jet_2_phi,
            # jet_2_E,
        ],
        
        "HIGH": [ #<! above 400 [GeV]
            # tau_0_met_dphi,
            # tau_0_pt,
            # met_et,
            # bjet_0_pt,
            # bjet_0_met_dphi,
            # bjet_0_tau_0_dr,
            # met_jet_dphi_ratio,
            # TruthMass,

            tau_0_pt,
            tau_0_eta,
            tau_0_phi,
            tau_0_E,
            # tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,
            bjet_0_pt,
            bjet_0_eta,
            bjet_0_phi,
            bjet_0_E,
            met_et,
            met_phi,
            jet_0_pt,
            jet_0_eta,
            jet_0_phi,
            jet_0_E,
            jet_1_pt,
            jet_1_eta,
            jet_1_phi,
            # jet_1_E,
            jet_2_pt,
            jet_2_eta,
            jet_2_phi,
            # jet_2_E,
        ],
    },

    "taulep": {
        "LOW": [
            # n_avg_int_cor,
            # n_actual_int_cor,

            # tau_0_pt,
            # # tau_0_px,
            # # tau_0_py,
            # # tau_0_pz,
            # tau_0_eta,
            # tau_0_phi,
            # tau_0_E,
            # tau_0_n_charged_tracks,
            # tau_0_q, 
            # tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,

            # lep_0_pt,
            # # lep_0_px,
            # # lep_0_py,
            # # lep_0_pz,
            # lep_0_eta,
            # lep_0_phi,
            # lep_0_E,

            # el_0_pt,
            # # el_0_px,
            # # el_0_py,
            # # el_0_pz,
            # el_0_eta,
            # el_0_phi,
            # el_0_E,

            # mu_0_pt,
            # # mu_0_px,
            # # mu_0_py,
            # # mu_0_pz,
            # mu_0_eta,
            # mu_0_phi,
            # mu_0_E,

            # met_et,
            # # met_ex,
            # # met_ey,
            # met_phi,
            # # tau_0_met_mt,
            # # tau_0_met_dphi,
            # # lep_0_met_mt,
            # # lep_0_met_dphi,
            # # tau_0_lep_0_mass,

            # # # n_jets,
            # # # n_bjets,    
            # jet_0_pt,
            # # jet_0_px,
            # # jet_0_py,
            # # jet_0_pz,
            # jet_0_eta,
            # jet_0_phi,
            # jet_0_E,
            # jet_1_pt,

            # bjet_0_pt,
            # # bjet_0_px,
            # # bjet_0_py,
            # # bjet_0_pz,
            # bjet_0_eta,
            # bjet_0_phi,
            # bjet_0_E,

            # bjet_0_met_dphi,
            # bjet_0_tau_0_dr,
            # bjet_0_lep_0_dr,
            # tau_0_lep_0_dr,
            # met_jet_dphi_ratio,



            tau_0_pt,
            tau_0_eta,
            tau_0_phi,
            tau_0_E,
            tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,
            lep_0_pt,
            lep_0_eta,
            lep_0_phi,
            lep_0_E,
            bjet_0_pt,
            bjet_0_eta,
            bjet_0_phi,
            bjet_0_E,
            met_et,
            met_phi,
            jet_0_pt,
            jet_0_eta,
            jet_0_phi,
            jet_0_E,
            jet_1_pt,

            # tau_0_pt,
            # lep_0_pt,
            # bjet_0_pt,
            # met_et,
            # tau_0_met_dphi,
            # lep_0_met_dphi,
            # bjet_0_met_dphi,
            # tau_0_lep_0_dr,
            # bjet_0_lep_0_dr,
            # met_jet_dphi_ratio,
            # tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,
            # TruthMass,
        ],
        "HIGH": [ #<! above 400 [GeV]
            # tau_0_pt,
            # tau_0_eta,
            # tau_0_phi,
            # tau_0_E,
            # lep_0_pt,
            # lep_0_eta,
            # lep_0_phi,
            # lep_0_E,
            # bjet_0_pt,
            # bjet_0_eta,
            # bjet_0_phi,
            # bjet_0_E,
            # met_et,
            # met_phi,
            # jet_0_pt,
            # jet_0_eta,
            # jet_0_phi,
            # jet_0_E,

            # tau_0_pt,
            # lep_0_pt,
            # bjet_0_pt,
            # met_et,
            # tau_0_met_dphi,
            # lep_0_met_dphi,
            # bjet_0_met_dphi,
            # tau_0_lep_0_dr,
            # bjet_0_lep_0_dr,
            # met_jet_dphi_ratio,
            # tau_0_charged_tracks_0_pt,
            # tau_0_upsilon,
            # TruthMass,
                        # n_avg_int_cor,
            # n_actual_int_cor,

            # tau_0_pt,
            # # tau_0_px,
            # # tau_0_py,
            # # tau_0_pz,
            # tau_0_eta,
            # tau_0_phi,
            # tau_0_E,
            # tau_0_n_charged_tracks,
            # tau_0_q, 
            # tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,

            # lep_0_pt,
            # # lep_0_px,
            # # lep_0_py,
            # # lep_0_pz,
            # lep_0_eta,
            # lep_0_phi,
            # lep_0_E,

            # el_0_pt,
            # # el_0_px,
            # # el_0_py,
            # # el_0_pz,
            # el_0_eta,
            # el_0_phi,
            # el_0_E,

            # mu_0_pt,
            # # mu_0_px,
            # # mu_0_py,
            # # mu_0_pz,
            # mu_0_eta,
            # mu_0_phi,
            # mu_0_E,

            # met_et,
            # # met_ex,
            # # met_ey,
            # met_phi,
            # # tau_0_met_mt,
            # # tau_0_met_dphi,
            # # lep_0_met_mt,
            # # lep_0_met_dphi,
            # # tau_0_lep_0_mass,

            # # # n_jets,
            # # # n_bjets,    
            # jet_0_pt,
            # # jet_0_px,
            # # jet_0_py,
            # # jet_0_pz,
            # jet_0_eta,
            # jet_0_phi,
            # jet_0_E,
            # jet_1_pt,

            # bjet_0_pt,
            # # bjet_0_px,
            # # bjet_0_py,
            # # bjet_0_pz,
            # bjet_0_eta,
            # bjet_0_phi,
            # bjet_0_E,
            tau_0_pt,
            tau_0_eta,
            tau_0_phi,
            tau_0_E,
            # tau_0_upsilon,
            # tau_0_charged_tracks_0_pt,
            lep_0_pt,
            lep_0_eta,
            lep_0_phi,
            lep_0_E,
            bjet_0_pt,
            bjet_0_eta,
            bjet_0_phi,
            bjet_0_E,
            met_et,
            met_phi,
            jet_0_pt,
            jet_0_eta,
            jet_0_phi,
            jet_0_E,
            jet_1_pt,
        ],
    }        
}

##-----------------------------------------------------------------
# - - - - - - - -  BDT scores (fine binning for WS; rebin for plots)
##-----------------------------------------------------------------

#### NOMINAL
clf_score_GB200_mass_80to120 = Variable(
    "clf_score_GB200_mass_80to120",    
    title='BDT score (80 to 120 [GeV])', 
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.1, 0.1),
)
clf_score_GB200_mass_130to160 = Variable(
    "clf_score_GB200_mass_130to160",    
    title='BDT score (130 to 160 [GeV])', 
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.1, 0.1),
)
clf_score_GB200_mass_170to190 = Variable(
    "clf_score_GB200_mass_170to190",    
    title='BDT score (170 to 190 [GeV])',
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.1, 0.1),
)

clf_score_GB200_mass_200to400 = Variable(
    "clf_score_GB200_mass_200to400",    
    title='BDT score (200 to 400 [GeV])',
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.1, 0.1),
)

clf_score_GB200_mass_500to3000 = Variable(
    "clf_score_GB200_mass_500to3000",    
    title='BDT score (500 to 3000 [GeV])',
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.1, 0.1),
)

#### SINGLE
clf_score_GB200_mass_80to80 = Variable(
    "clf_score_GB200_mass_80to80",    
    title='NN score (80 GeV)', 
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_90to90 = Variable(
    "clf_score_GB200_mass_90to90",
    title='NN score (90 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_100to100 = Variable(
    "clf_score_GB200_mass_100to100",
    title='NN score (100 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_110to110 = Variable(
    "clf_score_GB200_mass_110to110",
    title='NN score (110 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_120to120 = Variable(
    "clf_score_GB200_mass_120to120",
    title='NN score (120 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_130to130 = Variable(
    "clf_score_GB200_mass_130to130",    
    title='NN score (130 GeV)', 
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_140to140 = Variable(
    "clf_score_GB200_mass_140to140",
    title='NN score (140 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_150to150 = Variable(
    "clf_score_GB200_mass_150to150",
    title='NN score (150 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_160to160 = Variable(
    "clf_score_GB200_mass_160to160",
    title='NN score (160 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_170to170 = Variable(
    "clf_score_GB200_mass_170to170",    
    title='NN score (170 GeV)',
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_180to180 = Variable(
    "clf_score_GB200_mass_180to180",
    title='NN score (180 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_190to190 = Variable(
    "clf_score_GB200_mass_190to190",
    title='NN score (190 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_200to200 = Variable(
    "clf_score_GB200_mass_200to200",    
    title='NN score (200 GeV)',
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_225to225 = Variable(
    "clf_score_GB200_mass_225to225",
    title='NN score (225 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_250to250 = Variable(
    "clf_score_GB200_mass_250to250",
    title='NN score (250 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_275to275 = Variable(
    "clf_score_GB200_mass_275to275",
    title='NN score (275 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_300to300 = Variable(
    "clf_score_GB200_mass_300to300",
    title='NN score (300 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_350to350 = Variable(
    "clf_score_GB200_mass_350to350",
    title='NN score (350 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_400to400 = Variable(
    "clf_score_GB200_mass_400to400",
    title='NN score (400 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_500to500 = Variable(
    "clf_score_GB200_mass_500to500",
    title='NN score (500 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)


clf_score_GB200_mass_600to600 = Variable(
    "clf_score_GB200_mass_600to600",
    title='NN score (600 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)


clf_score_GB200_mass_700to700 = Variable(
    "clf_score_GB200_mass_700to700",
    title='NN score (700 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)


clf_score_GB200_mass_800to800 = Variable(
    "clf_score_GB200_mass_800to800",
    title='NN score (800 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)


clf_score_GB200_mass_900to900 = Variable(
    "clf_score_GB200_mass_900to900",
    title='NN score (900 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_1000to1000 = Variable(
    "clf_score_GB200_mass_1000to1000",    
    title='NN score (1000 GeV)',
    binning=(1000, 0, 1), 
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_1200to1200 = Variable(
    "clf_score_GB200_mass_1200to1200",
    title='NN score (1200 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_1400to1400 = Variable(
    "clf_score_GB200_mass_1400to1400",
    title='NN score (1400 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_1600to1600 = Variable(
    "clf_score_GB200_mass_1600to1600",
    title='NN score (1600 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_1800to1800 = Variable(
    "clf_score_GB200_mass_1800to1800",
    title='NN score (1800 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_2000to2000 = Variable(
    "clf_score_GB200_mass_2000to2000",
    title='NN score (2000 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_2500to2500 = Variable(
    "clf_score_GB200_mass_2500to2500",
    title='NN score (2500 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

clf_score_GB200_mass_3000to3000 = Variable(
    "clf_score_GB200_mass_3000to3000",
    title='NN score (3000 GeV)',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.05, 0.05),
)

#### UP_DOWN (Sliding Window)
clf_score_GB200_mass_80to90 = Variable(
    'clf_score_GB200_mass_80to90',
    title='BDT score (80 to 90 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_80to100 = Variable(
    'clf_score_GB200_mass_80to100',
    title='BDT score (80 to 100 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_90to110 = Variable(
    'clf_score_GB200_mass_90to110',
    title='BDT score (90 to 110 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_100to120 = Variable(
    'clf_score_GB200_mass_100to120',
    title='BDT score (100 to 120 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_110to130 = Variable(
    'clf_score_GB200_mass_110to130',
    title='BDT score (110 to 130 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_120to140 = Variable(
    'clf_score_GB200_mass_120to140',
    title='BDT score (120 to 140 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_130to150 = Variable(
    'clf_score_GB200_mass_130to150',
    title='BDT score (130 to 150 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_140to160 = Variable(
    'clf_score_GB200_mass_140to160',
    title='BDT score (140 to 160 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_150to170 = Variable(
    'clf_score_GB200_mass_150to170',
    title='BDT score (150 to 170 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_160to180 = Variable(
    'clf_score_GB200_mass_160to180',
    title='BDT score (160 to 180 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
# clf_score_GB200_mass_170to190 = Variable(
#     'clf_score_GB200_mass_170to190',
#     title='BDT score (170 to 190 [GeV])',
#     binning=(1000,0,1),
#     plot_bins=np.arange(0,1.1,0.1),
# )
clf_score_GB200_mass_180to200 = Variable(
    'clf_score_GB200_mass_180to200',
    title='BDT score (180 to 200 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_190to225 = Variable(
    'clf_score_GB200_mass_190to225',
    title='BDT score (190 to 225 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_200to250 = Variable(
    'clf_score_GB200_mass_200to250',
    title='BDT score (200 to 250 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_225to275 = Variable(
    'clf_score_GB200_mass_225to275',
    title='BDT score (225 to 275 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_250to300 = Variable(
    'clf_score_GB200_mass_250to300',
    title='BDT score (250 to 300 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_275to350 = Variable(
    'clf_score_GB200_mass_275to350',
    title='BDT score (275 to 350 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_300to400 = Variable(
    'clf_score_GB200_mass_300to400',
    title='BDT score (300 to 400 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_350to500 = Variable(
    'clf_score_GB200_mass_350to500',
    title='BDT score (350 to 500 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_400to600 = Variable(
    'clf_score_GB200_mass_400to600',
    title='BDT score (400 to 600 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_500to700 = Variable(
    'clf_score_GB200_mass_500to700',
    title='BDT score (500 to 700 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_600to800 = Variable(
    'clf_score_GB200_mass_600to800',
    title='BDT score (600 to 800 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_700to900 = Variable(
    'clf_score_GB200_mass_700to900',
    title='BDT score (700 to 900 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_800to1000 = Variable(
    'clf_score_GB200_mass_800to1000',
    title='BDT score (800 to 1000 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_900to1200 = Variable(
    'clf_score_GB200_mass_900to1200',
    title='BDT score (900 to 1200 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_1000to1400 = Variable(
    'clf_score_GB200_mass_1000to1400',
    title='BDT score (1000 to 1400 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_1200to1600 = Variable(
    'clf_score_GB200_mass_1200to1600',
    title='BDT score (1200 to 1600 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_1400to1800 = Variable(
    'clf_score_GB200_mass_1400to1800',
    title='BDT score (1400 to 1800 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_1600to2000 = Variable(
    'clf_score_GB200_mass_1600to2000',
    title='BDT score (1600 to 2000 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_1800to2500 = Variable(
    'clf_score_GB200_mass_1800to2500',
    title='BDT score (1800 to 2500 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_2000to3000 = Variable(
    'clf_score_GB200_mass_2000to3000',
    title='BDT score (2000 to 3000 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)
clf_score_GB200_mass_2500to3000 = Variable(
    'clf_score_GB200_mass_2500to3000',
    title='BDT score (2500 to 3000 [GeV])',
    binning=(1000,0,1),
    plot_bins=np.arange(0,1.1,0.1),
)

#### SINGLE
clf_score_GB200_mass_80to3000 = Variable(
    "clf_score_GB200_mass_80to3000",
    title='BDT score (80 to 3000 [GeV])',
    binning=(1000, 0, 1),
    plot_bins=np.arange(0, 1.1, 0.1),
)

BDT_SCORES = {
    "taujet":{
        "NOM":[
            clf_score_GB200_mass_80to120,
            clf_score_GB200_mass_130to160,
            clf_score_GB200_mass_170to190,
            clf_score_GB200_mass_200to400,
            clf_score_GB200_mass_500to3000,
                ],
        "SINGLE":[
            clf_score_GB200_mass_80to80,
            clf_score_GB200_mass_90to90,
            clf_score_GB200_mass_100to100,
            clf_score_GB200_mass_110to110,
            clf_score_GB200_mass_120to120,
            clf_score_GB200_mass_130to130,
            clf_score_GB200_mass_140to140,
            clf_score_GB200_mass_150to150,
            clf_score_GB200_mass_160to160,
            clf_score_GB200_mass_170to170,
            clf_score_GB200_mass_180to180,         
            clf_score_GB200_mass_190to190,
            clf_score_GB200_mass_200to200,
            clf_score_GB200_mass_225to225,
            clf_score_GB200_mass_250to250,
            clf_score_GB200_mass_275to275,
            clf_score_GB200_mass_300to300,
            clf_score_GB200_mass_350to350,
            clf_score_GB200_mass_400to400,
            clf_score_GB200_mass_500to500,
            clf_score_GB200_mass_600to600,
            clf_score_GB200_mass_700to700,
            clf_score_GB200_mass_800to800,
            clf_score_GB200_mass_900to900,
            clf_score_GB200_mass_1000to1000,
            clf_score_GB200_mass_1200to1200,
            clf_score_GB200_mass_1400to1400,
            clf_score_GB200_mass_1600to1600,
            clf_score_GB200_mass_1800to1800,
            clf_score_GB200_mass_2000to2000,
            clf_score_GB200_mass_2500to2500,
            clf_score_GB200_mass_3000to3000,
            ],
        "UP_DOWN":[
            clf_score_GB200_mass_80to90,
            clf_score_GB200_mass_80to100,
            clf_score_GB200_mass_90to110,
            clf_score_GB200_mass_100to120,
            clf_score_GB200_mass_110to130,
            clf_score_GB200_mass_120to140,
            clf_score_GB200_mass_130to150,
            clf_score_GB200_mass_140to160,
            clf_score_GB200_mass_150to170,
            clf_score_GB200_mass_160to180,
            clf_score_GB200_mass_170to190,
            clf_score_GB200_mass_180to200,
            clf_score_GB200_mass_190to225,
            clf_score_GB200_mass_200to250,
            clf_score_GB200_mass_225to275,
            clf_score_GB200_mass_250to300,
            clf_score_GB200_mass_275to350,
            clf_score_GB200_mass_300to400,
            clf_score_GB200_mass_350to500,
            clf_score_GB200_mass_400to600,
            clf_score_GB200_mass_500to700,
            clf_score_GB200_mass_600to800,
            clf_score_GB200_mass_700to900,
            clf_score_GB200_mass_800to1000,
            clf_score_GB200_mass_900to1200,
            clf_score_GB200_mass_1000to1400,
            clf_score_GB200_mass_1200to1600,
            clf_score_GB200_mass_1400to1800,
            clf_score_GB200_mass_1600to2000,
            clf_score_GB200_mass_1800to2500,
            clf_score_GB200_mass_2000to3000,
            clf_score_GB200_mass_2500to3000,
            ],        
        "ALL":[
            clf_score_GB200_mass_80to3000,
            ],
        },

    "taulep":{
        "NOM":[
            clf_score_GB200_mass_80to120,
            clf_score_GB200_mass_130to160,
            clf_score_GB200_mass_170to190,
            clf_score_GB200_mass_200to400,
            clf_score_GB200_mass_500to3000,
                ],
        "SINGLE":[
            clf_score_GB200_mass_80to80,
            clf_score_GB200_mass_90to90,
            clf_score_GB200_mass_100to100,
            clf_score_GB200_mass_110to110,
            clf_score_GB200_mass_120to120,
            clf_score_GB200_mass_130to130,
            clf_score_GB200_mass_140to140,
            clf_score_GB200_mass_150to150,
            clf_score_GB200_mass_160to160,
            clf_score_GB200_mass_170to170,
            clf_score_GB200_mass_180to180,         
            clf_score_GB200_mass_190to190,
            clf_score_GB200_mass_200to200,
            clf_score_GB200_mass_225to225,
            clf_score_GB200_mass_250to250,
            clf_score_GB200_mass_275to275,
            clf_score_GB200_mass_300to300,
            clf_score_GB200_mass_350to350,
            clf_score_GB200_mass_400to400,
            clf_score_GB200_mass_500to500,
            clf_score_GB200_mass_600to600,
            clf_score_GB200_mass_700to700,
            clf_score_GB200_mass_800to800,
            clf_score_GB200_mass_900to900,
            clf_score_GB200_mass_1000to1000,
            clf_score_GB200_mass_1200to1200,
            clf_score_GB200_mass_1400to1400,
            clf_score_GB200_mass_1600to1600,
            clf_score_GB200_mass_1800to1800,
            clf_score_GB200_mass_2000to2000,
            clf_score_GB200_mass_2500to2500,
            clf_score_GB200_mass_3000to3000,
            ],
        "UP_DOWN":[
            clf_score_GB200_mass_80to90,
            clf_score_GB200_mass_80to100,
            clf_score_GB200_mass_90to110,
            clf_score_GB200_mass_100to120,
            clf_score_GB200_mass_110to130,
            clf_score_GB200_mass_120to140,
            clf_score_GB200_mass_130to150,
            clf_score_GB200_mass_140to160,
            clf_score_GB200_mass_150to170,
            clf_score_GB200_mass_160to180,
            clf_score_GB200_mass_170to190,
            clf_score_GB200_mass_180to200,
            clf_score_GB200_mass_190to225,
            clf_score_GB200_mass_200to250,
            clf_score_GB200_mass_225to275,
            clf_score_GB200_mass_250to300,
            clf_score_GB200_mass_275to350,
            clf_score_GB200_mass_300to400,
            clf_score_GB200_mass_350to500,
            clf_score_GB200_mass_400to600,
            clf_score_GB200_mass_500to700,
            clf_score_GB200_mass_600to800,
            clf_score_GB200_mass_700to900,
            clf_score_GB200_mass_800to1000,
            clf_score_GB200_mass_900to1200,
            clf_score_GB200_mass_1000to1400,
            clf_score_GB200_mass_1200to1600,
            clf_score_GB200_mass_1400to1800,
            clf_score_GB200_mass_1600to2000,
            clf_score_GB200_mass_1800to2500,
            clf_score_GB200_mass_2000to3000,
            clf_score_GB200_mass_2500to3000,
            ],        
        "ALL":[
            clf_score_GB200_mass_80to3000,
            ],
    }
}



##-----------------------------------------------------------------
# - - - - - - - - variables for rQCD calculation
##-----------------------------------------------------------------
#rQCD_VARS = {"1": tau_0_jet_width, "3": tau_0_jet_rnn_score_trans}
rQCD_VARS = {"1": tau_0_jet_width, "3": tau_0_jet_width}

# - - - - - - - - variables for extracting FFs shapes 
FFS_TEMPLATE_VARS = (tau_0_pt, tau_0_n_charged_tracks, tau_0_jet_rnn_score_trans)


##-----------------------------------------------------------------
# - - - - - - - - Scale Factors 
##-----------------------------------------------------------------
WEIGHT_VARS = {"taujet": [], "taulep":[]}
for channel in ["taujet", "taulep"]:
    for weight in WEIGHTS[channel]:
        name = weight.name
        title = weight.variations[0]
        wv = Variable(
            name, 
            title=name, 
            tformula=title,
            binning=(4000, -2, 2),
            plot_bins=np.arange(0.5, 1.5, 0.01),
        )
        WEIGHT_VARS[channel] += [wv]

##-----------------------------------------##
# MVA scores for partial unblinding studies #
##-----------------------------------------##

VARIABLES_PARTIAL_UNBLIND_SCORES = []

for mass in [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 225, 250, 275, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000]:
    VARIABLES_PARTIAL_UNBLIND_SCORES.append(
        Variable(
            '80to3000_{0}'.format(mass),
            title='{0} GeV NN Score (uint8)'.format(mass),
            binning=(256,0,256),
        )
    )

# Uncomment these if making uint8 pnn score plots (when e.g. finding cut values for partial unblinding)
#VARIABLES_TAULEP += VARIABLES_PARTIAL_UNBLIND_SCORES
#VARIABLES_TAUJET += VARIABLES_PARTIAL_UNBLIND_SCORES
