#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.136913;
		 if(pt < 40) return 0.122744;
		 if(pt < 45) return 0.101822;
		 if(pt < 50) return 0.099661;
		 if(pt < 60) return 0.096597;
		 if(pt < 80) return 0.091902;
		 if(pt < 100) return 0.092623;
		 if(pt < 200) return 0.083397;
		 if(pt < 3500) return 0.068336;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.028303;
		 if(pt < 40) return 0.027457;
		 if(pt < 60) return 0.016224;
		 if(pt < 80) return 0.013337;
		 if(pt < 100) return 0.011729;
		 if(pt < 3500) return 0.010385;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.195882;
		 if(pt < 40) return 0.177334;
		 if(pt < 45) return 0.149010;
		 if(pt < 50) return 0.145651;
		 if(pt < 60) return 0.141323;
		 if(pt < 80) return 0.136331;
		 if(pt < 100) return 0.137036;
		 if(pt < 200) return 0.126199;
		 if(pt < 3500) return 0.105500;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.044227;
		 if(pt < 40) return 0.043920;
		 if(pt < 60) return 0.027797;
		 if(pt < 80) return 0.023037;
		 if(pt < 100) return 0.020569;
		 if(pt < 3500) return 0.018174;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.256232;
		 if(pt < 40) return 0.234121;
		 if(pt < 45) return 0.199510;
		 if(pt < 50) return 0.194435;
		 if(pt < 60) return 0.187444;
		 if(pt < 80) return 0.180578;
		 if(pt < 100) return 0.182769;
		 if(pt < 200) return 0.169619;
		 if(pt < 3500) return 0.141082;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.059579;
		 if(pt < 40) return 0.060204;
		 if(pt < 60) return 0.039518;
		 if(pt < 80) return 0.033410;
		 if(pt < 100) return 0.029802;
		 if(pt < 3500) return 0.026072;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.187240;
		 if(pt < 40) return 0.174834;
		 if(pt < 45) return 0.159391;
		 if(pt < 50) return 0.148672;
		 if(pt < 60) return 0.143098;
		 if(pt < 80) return 0.127263;
		 if(pt < 100) return 0.109164;
		 if(pt < 200) return 0.113806;
		 if(pt < 3500) return 0.075403;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.035964;
		 if(pt < 40) return 0.034305;
		 if(pt < 60) return 0.026528;
		 if(pt < 80) return 0.017862;
		 if(pt < 100) return 0.012756;
		 if(pt < 3500) return 0.011590;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.253712;
		 if(pt < 40) return 0.239110;
		 if(pt < 45) return 0.219745;
		 if(pt < 50) return 0.205660;
		 if(pt < 60) return 0.200227;
		 if(pt < 80) return 0.180451;
		 if(pt < 100) return 0.158863;
		 if(pt < 200) return 0.165238;
		 if(pt < 3500) return 0.115426;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.053181;
		 if(pt < 40) return 0.051233;
		 if(pt < 60) return 0.041286;
		 if(pt < 80) return 0.029181;
		 if(pt < 100) return 0.021252;
		 if(pt < 3500) return 0.020436;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.321482;
		 if(pt < 40) return 0.304051;
		 if(pt < 45) return 0.281445;
		 if(pt < 50) return 0.266143;
		 if(pt < 60) return 0.256182;
		 if(pt < 80) return 0.230407;
		 if(pt < 100) return 0.208861;
		 if(pt < 200) return 0.220088;
		 if(pt < 3500) return 0.157699;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.069938;
		 if(pt < 40) return 0.067623;
		 if(pt < 60) return 0.056010;
		 if(pt < 80) return 0.040662;
		 if(pt < 100) return 0.030197;
		 if(pt < 3500) return 0.029225;
		 else return 0;
		 }
	 else return 0;
}


