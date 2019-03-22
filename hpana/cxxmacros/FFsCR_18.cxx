#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.143717;
		 if(pt < 40) return 0.128895;
		 if(pt < 45) return 0.106480;
		 if(pt < 50) return 0.092588;
		 if(pt < 60) return 0.097129;
		 if(pt < 80) return 0.097440;
		 if(pt < 100) return 0.087941;
		 if(pt < 200) return 0.079211;
		 if(pt < 3500) return 0.060306;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.030505;
		 if(pt < 40) return 0.026445;
		 if(pt < 60) return 0.015914;
		 if(pt < 80) return 0.015143;
		 if(pt < 100) return 0.011874;
		 if(pt < 3500) return 0.010067;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.203779;
		 if(pt < 40) return 0.186332;
		 if(pt < 45) return 0.156497;
		 if(pt < 50) return 0.136849;
		 if(pt < 60) return 0.142703;
		 if(pt < 80) return 0.144876;
		 if(pt < 100) return 0.131994;
		 if(pt < 200) return 0.121293;
		 if(pt < 3500) return 0.095922;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.048542;
		 if(pt < 40) return 0.043749;
		 if(pt < 60) return 0.027705;
		 if(pt < 80) return 0.025785;
		 if(pt < 100) return 0.020823;
		 if(pt < 3500) return 0.017403;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.266616;
		 if(pt < 40) return 0.245736;
		 if(pt < 45) return 0.209476;
		 if(pt < 50) return 0.183943;
		 if(pt < 60) return 0.189707;
		 if(pt < 80) return 0.192771;
		 if(pt < 100) return 0.178107;
		 if(pt < 200) return 0.163226;
		 if(pt < 3500) return 0.131346;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.065731;
		 if(pt < 40) return 0.060361;
		 if(pt < 60) return 0.039533;
		 if(pt < 80) return 0.036899;
		 if(pt < 100) return 0.030297;
		 if(pt < 3500) return 0.025483;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.201276;
		 if(pt < 40) return 0.188312;
		 if(pt < 45) return 0.166875;
		 if(pt < 50) return 0.156051;
		 if(pt < 60) return 0.140108;
		 if(pt < 80) return 0.133355;
		 if(pt < 100) return 0.106242;
		 if(pt < 200) return 0.095659;
		 if(pt < 3500) return 0.084592;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.037712;
		 if(pt < 40) return 0.037308;
		 if(pt < 60) return 0.027998;
		 if(pt < 80) return 0.020041;
		 if(pt < 100) return 0.013557;
		 if(pt < 3500) return 0.010961;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.273862;
		 if(pt < 40) return 0.254967;
		 if(pt < 45) return 0.228253;
		 if(pt < 50) return 0.214019;
		 if(pt < 60) return 0.195545;
		 if(pt < 80) return 0.190175;
		 if(pt < 100) return 0.153302;
		 if(pt < 200) return 0.140698;
		 if(pt < 3500) return 0.127913;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.055558;
		 if(pt < 40) return 0.056336;
		 if(pt < 60) return 0.043789;
		 if(pt < 80) return 0.032242;
		 if(pt < 100) return 0.022778;
		 if(pt < 3500) return 0.018620;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.348594;
		 if(pt < 40) return 0.324929;
		 if(pt < 45) return 0.290594;
		 if(pt < 50) return 0.275653;
		 if(pt < 60) return 0.251387;
		 if(pt < 80) return 0.247837;
		 if(pt < 100) return 0.202260;
		 if(pt < 200) return 0.185736;
		 if(pt < 3500) return 0.170802;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.072907;
		 if(pt < 40) return 0.074645;
		 if(pt < 60) return 0.058974;
		 if(pt < 80) return 0.044712;
		 if(pt < 100) return 0.032895;
		 if(pt < 3500) return 0.027077;
		 else return 0;
		 }
	 else return 0;
}


