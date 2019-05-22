#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.199313;
		 if(pt < 40) return 0.185474;
		 if(pt < 45) return 0.171631;
		 if(pt < 50) return 0.157682;
		 if(pt < 60) return 0.145338;
		 if(pt < 80) return 0.131338;
		 if(pt < 100) return 0.110178;
		 if(pt < 200) return 0.102788;
		 if(pt < 3500) return 0.079506;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.044861;
		 if(pt < 40) return 0.045312;
		 if(pt < 60) return 0.035384;
		 if(pt < 80) return 0.024715;
		 if(pt < 100) return 0.016881;
		 if(pt < 3500) return 0.016020;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.269478;
		 if(pt < 40) return 0.250489;
		 if(pt < 45) return 0.235042;
		 if(pt < 50) return 0.216913;
		 if(pt < 60) return 0.202707;
		 if(pt < 80) return 0.187160;
		 if(pt < 100) return 0.160455;
		 if(pt < 200) return 0.151028;
		 if(pt < 3500) return 0.120938;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.064218;
		 if(pt < 40) return 0.066253;
		 if(pt < 60) return 0.053046;
		 if(pt < 80) return 0.038257;
		 if(pt < 100) return 0.027157;
		 if(pt < 3500) return 0.026254;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.342998;
		 if(pt < 40) return 0.318116;
		 if(pt < 45) return 0.299934;
		 if(pt < 50) return 0.279394;
		 if(pt < 60) return 0.259824;
		 if(pt < 80) return 0.243690;
		 if(pt < 100) return 0.211851;
		 if(pt < 200) return 0.199588;
		 if(pt < 3500) return 0.164956;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.083007;
		 if(pt < 40) return 0.085986;
		 if(pt < 60) return 0.069947;
		 if(pt < 80) return 0.051860;
		 if(pt < 100) return 0.037889;
		 if(pt < 3500) return 0.037118;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.140204;
		 if(pt < 40) return 0.124310;
		 if(pt < 45) return 0.100400;
		 if(pt < 50) return 0.092061;
		 if(pt < 60) return 0.094831;
		 if(pt < 80) return 0.092852;
		 if(pt < 100) return 0.086841;
		 if(pt < 200) return 0.079908;
		 if(pt < 3500) return 0.056616;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.033926;
		 if(pt < 40) return 0.031850;
		 if(pt < 60) return 0.019572;
		 if(pt < 80) return 0.017766;
		 if(pt < 100) return 0.014315;
		 if(pt < 3500) return 0.012378;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.199339;
		 if(pt < 40) return 0.179471;
		 if(pt < 45) return 0.148033;
		 if(pt < 50) return 0.136205;
		 if(pt < 60) return 0.139719;
		 if(pt < 80) return 0.138662;
		 if(pt < 100) return 0.130242;
		 if(pt < 200) return 0.122178;
		 if(pt < 3500) return 0.089755;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.052420;
		 if(pt < 40) return 0.050621;
		 if(pt < 60) return 0.032650;
		 if(pt < 80) return 0.029325;
		 if(pt < 100) return 0.024221;
		 if(pt < 3500) return 0.020679;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.261442;
		 if(pt < 40) return 0.237455;
		 if(pt < 45) return 0.198577;
		 if(pt < 50) return 0.183143;
		 if(pt < 60) return 0.186300;
		 if(pt < 80) return 0.185067;
		 if(pt < 100) return 0.175960;
		 if(pt < 200) return 0.164854;
		 if(pt < 3500) return 0.123009;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.069861;
		 if(pt < 40) return 0.068587;
		 if(pt < 60) return 0.045504;
		 if(pt < 80) return 0.041035;
		 if(pt < 100) return 0.034472;
		 if(pt < 3500) return 0.029535;
		 else return 0;
		 }
	 else return 0;
}


