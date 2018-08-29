#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.142598;
		 if(pt < 40) return 0.135518;
		 if(pt < 45) return 0.124711;
		 if(pt < 50) return 0.122396;
		 if(pt < 60) return 0.111415;
		 if(pt < 75) return 0.097673;
		 if(pt < 90) return 0.098309;
		 if(pt < 105) return 0.099986;
		 if(pt < 120) return 0.097033;
		 if(pt < 140) return 0.092176;
		 if(pt < 160) return 0.087563;
		 if(pt < 200) return 0.082947;
		 if(pt < 300) return 0.072914;
		 if(pt < 3500) return 0.066984;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.026549;
		 if(pt < 40) return 0.025690;
		 if(pt < 50) return 0.021541;
		 if(pt < 75) return 0.015924;
		 if(pt < 100) return 0.012062;
		 if(pt < 150) return 0.011447;
		 if(pt < 200) return 0.012128;
		 if(pt < 3500) return 0.010666;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.202822;
		 if(pt < 40) return 0.192755;
		 if(pt < 45) return 0.179240;
		 if(pt < 50) return 0.176608;
		 if(pt < 60) return 0.163133;
		 if(pt < 75) return 0.145492;
		 if(pt < 90) return 0.144859;
		 if(pt < 105) return 0.147564;
		 if(pt < 120) return 0.144854;
		 if(pt < 140) return 0.138142;
		 if(pt < 160) return 0.132030;
		 if(pt < 200) return 0.127750;
		 if(pt < 300) return 0.112522;
		 if(pt < 3500) return 0.103869;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.041107;
		 if(pt < 40) return 0.040568;
		 if(pt < 50) return 0.035255;
		 if(pt < 75) return 0.027583;
		 if(pt < 100) return 0.021458;
		 if(pt < 150) return 0.020634;
		 if(pt < 200) return 0.021541;
		 if(pt < 3500) return 0.017991;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.264276;
		 if(pt < 40) return 0.253127;
		 if(pt < 45) return 0.236771;
		 if(pt < 50) return 0.234690;
		 if(pt < 60) return 0.215254;
		 if(pt < 75) return 0.193094;
		 if(pt < 90) return 0.191562;
		 if(pt < 105) return 0.196921;
		 if(pt < 120) return 0.193540;
		 if(pt < 140) return 0.185456;
		 if(pt < 160) return 0.176470;
		 if(pt < 200) return 0.172077;
		 if(pt < 300) return 0.150157;
		 if(pt < 3500) return 0.140583;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.055255;
		 if(pt < 40) return 0.055010;
		 if(pt < 50) return 0.049021;
		 if(pt < 75) return 0.039895;
		 if(pt < 100) return 0.031438;
		 if(pt < 150) return 0.029801;
		 if(pt < 200) return 0.030932;
		 if(pt < 3500) return 0.025678;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.203764;
		 if(pt < 40) return 0.204067;
		 if(pt < 45) return 0.201733;
		 if(pt < 50) return 0.200172;
		 if(pt < 60) return 0.173081;
		 if(pt < 75) return 0.152899;
		 if(pt < 90) return 0.141474;
		 if(pt < 105) return 0.136526;
		 if(pt < 120) return 0.134976;
		 if(pt < 140) return 0.142733;
		 if(pt < 160) return 0.140626;
		 if(pt < 200) return 0.135284;
		 if(pt < 300) return 0.119311;
		 if(pt < 3500) return 0.112477;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.037234;
		 if(pt < 40) return 0.035881;
		 if(pt < 50) return 0.028394;
		 if(pt < 75) return 0.023711;
		 if(pt < 100) return 0.016301;
		 if(pt < 150) return 0.014113;
		 if(pt < 200) return 0.012871;
		 if(pt < 3500) return 0.013776;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.276691;
		 if(pt < 40) return 0.278082;
		 if(pt < 45) return 0.277905;
		 if(pt < 50) return 0.277201;
		 if(pt < 60) return 0.242059;
		 if(pt < 75) return 0.216324;
		 if(pt < 90) return 0.202533;
		 if(pt < 105) return 0.201743;
		 if(pt < 120) return 0.192791;
		 if(pt < 140) return 0.212742;
		 if(pt < 160) return 0.206322;
		 if(pt < 200) return 0.202199;
		 if(pt < 300) return 0.176744;
		 if(pt < 3500) return 0.183460;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.054971;
		 if(pt < 40) return 0.053358;
		 if(pt < 50) return 0.043544;
		 if(pt < 75) return 0.038078;
		 if(pt < 100) return 0.027158;
		 if(pt < 150) return 0.025251;
		 if(pt < 200) return 0.022457;
		 if(pt < 3500) return 0.022826;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.352364;
		 if(pt < 40) return 0.354369;
		 if(pt < 45) return 0.357011;
		 if(pt < 50) return 0.355436;
		 if(pt < 60) return 0.311045;
		 if(pt < 75) return 0.275644;
		 if(pt < 90) return 0.264752;
		 if(pt < 105) return 0.263601;
		 if(pt < 120) return 0.258451;
		 if(pt < 140) return 0.284150;
		 if(pt < 160) return 0.282550;
		 if(pt < 200) return 0.266528;
		 if(pt < 300) return 0.234552;
		 if(pt < 3500) return 0.255299;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.071982;
		 if(pt < 40) return 0.070237;
		 if(pt < 50) return 0.058586;
		 if(pt < 75) return 0.052539;
		 if(pt < 100) return 0.038544;
		 if(pt < 150) return 0.036188;
		 if(pt < 200) return 0.033016;
		 if(pt < 3500) return 0.032590;
		 else return 0;
		 }
	 else return 0;
}


