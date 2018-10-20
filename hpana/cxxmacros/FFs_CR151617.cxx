#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.188703;
		 if(pt < 40) return 0.187861;
		 if(pt < 45) return 0.174969;
		 if(pt < 50) return 0.175526;
		 if(pt < 60) return 0.163691;
		 if(pt < 75) return 0.147329;
		 if(pt < 100) return 0.149262;
		 if(pt < 150) return 0.150184;
		 if(pt < 300) return 0.134547;
		 if(pt < 3500) return 0.104502;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.031755;
		 if(pt < 40) return 0.030612;
		 if(pt < 50) return 0.024986;
		 if(pt < 75) return 0.020071;
		 if(pt < 100) return 0.019189;
		 if(pt < 200) return 0.021030;
		 if(pt < 3500) return 0.018426;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.188703;
		 if(pt < 40) return 0.187861;
		 if(pt < 45) return 0.174969;
		 if(pt < 50) return 0.175526;
		 if(pt < 60) return 0.163691;
		 if(pt < 75) return 0.147329;
		 if(pt < 100) return 0.149262;
		 if(pt < 150) return 0.150184;
		 if(pt < 300) return 0.134547;
		 if(pt < 3500) return 0.104502;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.031755;
		 if(pt < 40) return 0.030612;
		 if(pt < 50) return 0.024986;
		 if(pt < 75) return 0.020071;
		 if(pt < 100) return 0.019189;
		 if(pt < 200) return 0.021030;
		 if(pt < 3500) return 0.018426;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.245622;
		 if(pt < 40) return 0.245228;
		 if(pt < 45) return 0.229885;
		 if(pt < 50) return 0.231819;
		 if(pt < 60) return 0.214870;
		 if(pt < 75) return 0.194960;
		 if(pt < 100) return 0.197547;
		 if(pt < 150) return 0.200176;
		 if(pt < 300) return 0.179211;
		 if(pt < 3500) return 0.141787;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.042773;
		 if(pt < 40) return 0.041486;
		 if(pt < 50) return 0.034584;
		 if(pt < 75) return 0.028859;
		 if(pt < 100) return 0.028057;
		 if(pt < 200) return 0.030316;
		 if(pt < 3500) return 0.026374;
		 else return 0;
		 }
	 else return 0;
}


#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.254024;
		 if(pt < 40) return 0.238936;
		 if(pt < 45) return 0.235515;
		 if(pt < 50) return 0.209784;
		 if(pt < 60) return 0.203951;
		 if(pt < 75) return 0.188598;
		 if(pt < 100) return 0.164062;
		 if(pt < 150) return 0.147253;
		 if(pt < 300) return 0.128914;
		 if(pt < 3500) return 0.123111;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.048407;
		 if(pt < 40) return 0.051504;
		 if(pt < 50) return 0.041485;
		 if(pt < 75) return 0.033506;
		 if(pt < 100) return 0.023305;
		 if(pt < 200) return 0.022275;
		 if(pt < 3500) return 0.019480;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.254024;
		 if(pt < 40) return 0.238936;
		 if(pt < 45) return 0.235515;
		 if(pt < 50) return 0.209784;
		 if(pt < 60) return 0.203951;
		 if(pt < 75) return 0.188598;
		 if(pt < 100) return 0.164062;
		 if(pt < 150) return 0.147253;
		 if(pt < 300) return 0.128914;
		 if(pt < 3500) return 0.123111;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.048407;
		 if(pt < 40) return 0.051504;
		 if(pt < 50) return 0.041485;
		 if(pt < 75) return 0.033506;
		 if(pt < 100) return 0.023305;
		 if(pt < 200) return 0.022275;
		 if(pt < 3500) return 0.019480;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.323859;
		 if(pt < 40) return 0.303336;
		 if(pt < 45) return 0.302029;
		 if(pt < 50) return 0.270330;
		 if(pt < 60) return 0.261753;
		 if(pt < 75) return 0.243999;
		 if(pt < 100) return 0.215521;
		 if(pt < 150) return 0.192743;
		 if(pt < 300) return 0.172695;
		 if(pt < 3500) return 0.172392;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.063528;
		 if(pt < 40) return 0.068138;
		 if(pt < 50) return 0.055670;
		 if(pt < 75) return 0.046128;
		 if(pt < 100) return 0.032968;
		 if(pt < 200) return 0.032182;
		 if(pt < 3500) return 0.027678;
		 else return 0;
		 }
	 else return 0;
}


