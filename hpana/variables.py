import math

class Variable:
    def __init__(self, name, 
                 title=None, label=None, 
                 unit="", scale=None,
                 binning=None, bins=None,
                 tformula=None, blind_cut=None,
                 ):
        
        self.name = name
        self.title = title
        self.unit = unit
        self.scale = scale
        self.binning = binning
        self.bins = bins
        
        if blind_cut:
            self.blind_cut = blind_cut
        
        self.tformula = name
        if tformula:
            self.tformula = tformula

        if scale:
            self.tformula = "({0}) * ({1})".format(scale, self.tformula)

            
    @property 
    def label(self):
        if self._label is None:
            return "%s [%s]"%(self.name, self.unit) 
        else:
            return self._label
    @label.setter
    def label(self, value):
        self._label = value

    @property 
    def binning(self, year, category):
        if isinstance(self._binning, dict):
            if isinstance(self._binning[year], dict):
                return self._binning[year][category]
            elif isinstance(self._binning[year], tuple):
                return self._binning[year]
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
    
#--# tau
tau_0_pt = Variable("tau_0_pt", 
                    title='#font[52]{p}_{T}(#tau_{1}) [GeV]',
                    binning=(20, 0, 400),
                    unit='[GeV]', scale=0.001
                    )

tau_0_eta = Variable("tau_0_eta" , 
                     title='#eta(#tau)',
                     binning=(60, -3., 3.)
                     )

tau_0_n_tracks =  Variable("tau_0_n_tracks",
                           title='#font[152]{#tau}_{1} #font[52]{Tracks}',
                           binning=(5, -.5, 4.5)
                           )

tau_0_q = Variable("tau_0_q",
                   title='#font[152]{#tau}_{1} #font[52]{Charge}',
                   binning=(5, -2.5, 2.5),
                   )
  
upsilon = Variable("upsilon", 
                   title='#font[52]{#Upsilon}',
                   tformula='(tau_0_n_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_pt-1) + -111*(tau_0_n_tracks!=1)',
                   binning=(31, -1.05, 2.05)
                   )

#--# met
#----------------------------------------------------
met_et = Variable("met_et", 
                  title='#font[52]{E}^{miss}_{T} [GeV]',
                  binning=(1000, 0, 1000), #<! rebin in ../utils/MakePlots for final plots
                  scale=0.001, unit='[GeV]'
                  )

met_etx = Variable("met_etx",
                   title='#font[52]{E}^{miss}_{T_{x}}[GeV]',
                   binning=(20, -75, 75),
                   scale=0.001, unit='[GeV]',
                   )   

met_ety = Variable("met_ety",
                   title='#font[52]{E}^{miss}_{T_{y}}[GeV]',
                   binning=(20, -75, 75),
                   scale=0.001, unit='[GeV]',
                   )   
met_phi = Variable("met_phi", 
                   title='#font[52]{E}^{miss}_{T} #phi',
                   binning=(5, -math.pi, math.pi),
                   )

#--# tau + met
#----------------------------------------------------
tau_0_met_dphi = Variable("tau_0_met_dphi",
                            title='#Delta#phi(#tau, E^{miss}_{T})',
                            binning=(10, 0, math.pi),
                            )
tau_0_met_mt = Variable("tau_0_met_mt",
        title='m_{T}(#tau, E^{miss}_{T})[GeV]',
        # many bins needed for fitting, set your own binning in ../utils/MakePlots for plots
        binning=(2000, 0, 2000), 
        scale=0.001, unit='[GeV]',
        )


#--# jets
#----------------------------------------------------
n_jets = Variable("n_jets", 
                  title='#font[52]{Number of Selected Jets}',
                  binning= (10, -.5, 9.5),
                  )
n_bjets = Variable("n_bjets", 
                  title='#font[52]{Number of Selected b-Jets}',
                  binning= (10, -.5, 9.5),
                   )

jet_0_pt =  Variable("jet_0_pt",
                     title='#font[52]{p}_{T}(j_{1}) [GeV]',
                     binning=(20, 0, 500),
                     scale=0.001, unit='[GeV]',
                     )

bjet_0_pt =  Variable("bjet_0_pt",
                      title='#font[52]{p}_{T}lead b-jet [GeV]',
                      binning=(20, 0, 500),
                      scale=0.001, unit='[GeV]',
                      )


# sublight jet (make sure it's not a bjet)
jet_1_pt = Variable("jet_1_pt",
                    title='#font[52]{p}_{T}(sub-leading jet)[GeV]',
                    tformula= "(jet_2_pt*(jet_0_mvx > 0.8244273 || jet_1_mvx > 0.8244273))"\
                        "+ (jet_1_pt * !(jet_0_mvx > 0.8244273 || jet_1_mvx > 0.8244273))",
                    binning=(20, 0, 500),
                    scale=0.001, unit='[GeV]',
                    )

jet_0_eta = Variable("jet_0_eta",
                     title='#font[152]{#eta}(j_{1})',
                     binning=(60, -4, 4),
                     )

# btag eff check
# n_bjets_wp75 = Variable("n_bjets_wp75",
#                         title='Number of b-Jets (75\% wp)',
#                         tformula="(jet_0_mvx>-0.4)||(jet_1_mvx>-0.4)||(jet_2_mvx>-0.4)",
#                         binning= (2, -0.5, 1.5),
#                         )
# n_bjets_wp85 = Variable("n_bjets_wp85",
#                         title='Number of b-Jets (85\% wp)',
#                         tformula="(jet_0_mvx>0.1758475)||(jet_1_mvx>0.1758475)||(jet_2_mvx>0.1758475)",
#                         binning= (2, -0.5, 1.5),
#                         )

#--# BDT input features 
#----------------------------------------------------

MVA_bjet_0_met_dphi = Variable("MVA_bjet_0_met_dphi", 
                               title='#font[52]{#Delta#phi}(b-jet ,E^{miss}_{T})',
                               tformula='acos(cos(met_phi-bjet_0_phi))',
                               binning=(12, -1., 4),
                               )

MVA_tau_0_bjet_0_dr = Variable("MVA_tau_0_bjet_0_dr", 
                               title='#font[52]{#Delta}R(#tau, b-jet)',
                               tformula='sqrt(acos(cos(tau_0_phi-bjet_0_phi))**2 + (tau_0_eta-bjet_0_eta)**2)',
                               binning=(20, 0, 6.4),
                               )
#--# BDT scores
#---------------------------------------------------- 
#<! with 7/6 input vars,

# treat properly regions where Y is not modeled well
Y = "(tau_0_n_tracks==1)*(2.0*tau_0_allTrk_pt/tau_0_pt-1) + -111*(tau_0_n_tracks!=1)"
Y_CORRECTED = "(tau_0_n_tracks==1)*CorrectUpsilon_1D_WCR((2.0*tau_0_allTrk_pt/tau_0_pt-1), tau_0_n_tracks)"
BDT_SELECTION_1P = "(tau_0_n_tracks + ({0}>0.95)*({0}<1.05)*(tau_0_jet_bdt_loose == 1)"\
                   "+ ({1}>0.95)*({1}<1.05)*(tau_0_jet_bdt_loose != 1))".format(Y, Y_CORRECTED)

FastBDT_sig_90to120_1p3p = Variable("FastBDT_sig_90to120_1p3p",    
                                    title='BDT score, 90 to 120 [GeV]',
                                    tformula="({0}==1)*FastBDT_sig_7V_met150_Opt_90to120_1p"\
                                        "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_90to120_3p".format(BDT_SELECTION_1P),
                                    binning=(1000, 0, 1), 
                                    blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p"\
                                        "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_90to120_3p < 0.50",
                                    )

FastBDT_sig_130to160_1p3p = Variable("FastBDT_sig_130to160_1p3p",
                                     title="BDT score, 130 to 160 [GeV]",
                                     tformula="({0}==1)*FastBDT_sig_7V_met150_Opt_130to160_1p"\
                                         "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_130to160_3p".format(BDT_SELECTION_1P),
                                     binning=(1000, 0, 1),
                                     blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p"\
                                         "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_130to160_3p < 0.50",
                                     )

FastBDT_sig_160to180_1p3p = Variable("FastBDT_sig_160to180_1p3p",
                                     title="BDT score, 160 to 180 [GeV]",
                                     tformula="({0}==1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
                                         "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_160to180_3p".format(BDT_SELECTION_1P),
                                     binning=(1000, 0, 1),
                                     blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
                                         "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p < 0.50",
                                     )

FastBDT_sig_200to400_1p3p = Variable("FastBDT_sig_200to400_1p3p",
                                     title="BDT score, 200 to 400 [GeV]",
                                     tformula="({0}==1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
                                         "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_200to400_3p".format(BDT_SELECTION_1P),
                                     binning=(1000, 0, 1),
                                     blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
                                         "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p < 0.50",
                                     )

# average BDTs 160-180 and 200-400 (for evaluating mass point 200)
FastBDT_sig_200to400_160to180_avg_1p3p = Variable("FastBDT_sig_200to400_160to180_avg_1p3p",
                                                  title='BDT score, average 160 to 180 and, 200 to 400  [GeV]',
                                                  tformula="1/2. *(({0}==1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
                                                      "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_200to400_3p"\
                                                      "+ ({0}==1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
                                                      "+ ({0}!=1)*FastBDT_sig_6V_met150_Opt_160to180_3p)".format(BDT_SELECTION_1P),
                                                  binning=(1000, 0, 1),
                                                  blind_cut="(1/2. *((tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
                                                      "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p"\
                                                      "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
                                                      "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p)) < 0.50",
                                                  )
FastBDT_sig_500to2000_1p3p = Variable("FastBDT_sig_500to2000_1p3p", 
                                      title='BDT score, 500 to 2000 [GeV]',
                                      tformula="FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p",
                                      binning=(1000, 0, 1),
                                      blind_cut='FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p < 0.50',
                                      )




# FastBDT_sig_90to120_1p3p = Variable("FastBDT_sig_90to120_1p3p",    
#                                     title='BDT score, 90 to 120 [GeV]',
#                                     tformula="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p"\
#                                         "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_90to120_3p",
#                                     binning=(1000, 0, 1), 
#                                     blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_90to120_1p"\
#                                         "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_90to120_3p < 0.50",
#                                     )

# FastBDT_sig_130to160_1p3p = Variable("FastBDT_sig_130to160_1p3p",
#                                      title="BDT score, 130 to 160 [GeV]",
#                                      tformula="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p"\
#                                          "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_130to160_3p",
#                                      binning=(1000, 0, 1),
#                                      blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_130to160_1p"\
#                                          "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_130to160_3p < 0.50",
#                                      )

# FastBDT_sig_160to180_1p3p = Variable("FastBDT_sig_160to180_1p3p",
#                                      title="BDT score, 160 to 180 [GeV]",
#                                      tformula="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
#                                          "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p",
#                                      binning=(1000, 0, 1),
#                                      blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
#                                          "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p < 0.50",
#                                      )

# FastBDT_sig_200to400_1p3p = Variable("FastBDT_sig_200to400_1p3p",
#                                      title="BDT score, 200 to 400 [GeV]",
#                                      tformula="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
#                                          "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p",
#                                      binning=(1000, 0, 1),
#                                      blind_cut="(tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
#                                          "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p < 0.50",
#                                      )

# # average BDTs 160-180 and 200-400 (for evaluating mass point 200)
# FastBDT_sig_200to400_160to180_avg_1p3p = Variable("FastBDT_sig_200to400_160to180_avg_1p3p",
#                                                   title='BDT score, average 160 to 180 and, 200 to 400  [GeV]',
#                                                   tformula="1/2. *((tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
#                                                       "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p"\
#                                                       "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
#                                                       "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p)",
#                                                   binning=(1000, 0, 1),
#                                                   blind_cut="(1/2. *((tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_200to400_1p"\
#                                                       "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_200to400_3p"\
#                                                       "+ (tau_0_n_tracks == 1)*FastBDT_sig_7V_met150_Opt_160to180_1p"\
#                                                       "+ (tau_0_n_tracks == 3)*FastBDT_sig_6V_met150_Opt_160to180_3p)) < 0.50",
#                                                   )
# FastBDT_sig_500to2000_1p3p = Variable("FastBDT_sig_500to2000_1p3p", 
#                                       title='BDT score, 500 to 2000 [GeV]',
#                                       tformula="FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p",
#                                       binning=(1000, 0, 1),
#                                       blind_cut='FastBDT_sig_6V_2dFF_met150_Opt_500to2000_1p3p < 0.50',
#                                       )



TAUJET_VARIABLES = [
    tau_0_pt,
    tau_0_eta, 
    tau_0_n_tracks,
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
    #jet_1_pt,
    
    MVA_bjet_0_met_dphi,
    MVA_tau_0_bjet_0_dr,

    FastBDT_sig_90to120_1p3p,
    FastBDT_sig_130to160_1p3p,
    FastBDT_sig_160to180_1p3p,
    FastBDT_sig_200to400_1p3p,
    FastBDT_sig_200to400_160to180_avg_1p3p,
    FastBDT_sig_500to2000_1p3p
    ]


TAUJET_VARIABLES_BDTS = [
    FastBDT_sig_90to120_1p3p,
    FastBDT_sig_130to160_1p3p,
    FastBDT_sig_160to180_1p3p,
    FastBDT_sig_200to400_1p3p,
    FastBDT_sig_200to400_160to180_avg_1p3p,
    FastBDT_sig_500to2000_1p3p
    ]
