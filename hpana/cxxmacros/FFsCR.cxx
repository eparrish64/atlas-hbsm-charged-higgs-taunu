#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.138667;
		 if(pt < 40) return 0.123677;
		 if(pt < 45) return 0.098553;
		 if(pt < 50) return 0.094079;
		 if(pt < 60) return 0.096678;
		 if(pt < 80) return 0.092568;
		 if(pt < 100) return 0.086898;
		 if(pt < 200) return 0.079464;
		 if(pt < 3500) return 0.062700;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.028689;
		 if(pt < 40) return 0.027149;
		 if(pt < 60) return 0.015585;
		 if(pt < 80) return 0.013608;
		 if(pt < 100) return 0.010627;
		 if(pt < 3500) return 0.009556;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.198267;
		 if(pt < 40) return 0.178876;
		 if(pt < 45) return 0.145339;
		 if(pt < 50) return 0.138888;
		 if(pt < 60) return 0.141942;
		 if(pt < 80) return 0.138023;
		 if(pt < 100) return 0.129619;
		 if(pt < 200) return 0.121066;
		 if(pt < 3500) return 0.098416;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.045203;
		 if(pt < 40) return 0.044004;
		 if(pt < 60) return 0.026842;
		 if(pt < 80) return 0.023414;
		 if(pt < 100) return 0.018793;
		 if(pt < 3500) return 0.016514;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.260725;
		 if(pt < 40) return 0.236857;
		 if(pt < 45) return 0.195084;
		 if(pt < 50) return 0.186105;
		 if(pt < 60) return 0.188494;
		 if(pt < 80) return 0.183618;
		 if(pt < 100) return 0.174409;
		 if(pt < 200) return 0.162830;
		 if(pt < 3500) return 0.134081;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.061222;
		 if(pt < 40) return 0.060487;
		 if(pt < 60) return 0.038247;
		 if(pt < 80) return 0.033572;
		 if(pt < 100) return 0.027371;
		 if(pt < 3500) return 0.023998;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.167919;
		 if(pt < 40) return 0.139502;
		 if(pt < 45) return 0.119068;
		 if(pt < 50) return 0.094383;
		 if(pt < 60) return 0.097144;
		 if(pt < 80) return 0.091499;
		 if(pt < 100) return 0.068494;
		 if(pt < 200) return 0.056581;
		 if(pt < 3500) return 0.052272;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032051;
		 if(pt < 40) return 0.031637;
		 if(pt < 60) return 0.022173;
		 if(pt < 80) return 0.010769;
		 if(pt < 100) return 0.005587;
		 if(pt < 3500) return 0.004631;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.228457;
		 if(pt < 40) return 0.190234;
		 if(pt < 45) return 0.164282;
		 if(pt < 50) return 0.130773;
		 if(pt < 60) return 0.136011;
		 if(pt < 80) return 0.131061;
		 if(pt < 100) return 0.100259;
		 if(pt < 200) return 0.083224;
		 if(pt < 3500) return 0.080218;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.047078;
		 if(pt < 40) return 0.047614;
		 if(pt < 60) return 0.034295;
		 if(pt < 80) return 0.017525;
		 if(pt < 100) return 0.009450;
		 if(pt < 3500) return 0.007914;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.292711;
		 if(pt < 40) return 0.242718;
		 if(pt < 45) return 0.210522;
		 if(pt < 50) return 0.169356;
		 if(pt < 60) return 0.174901;
		 if(pt < 80) return 0.170554;
		 if(pt < 100) return 0.132295;
		 if(pt < 200) return 0.110272;
		 if(pt < 3500) return 0.110253;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.061897;
		 if(pt < 40) return 0.062995;
		 if(pt < 60) return 0.046302;
		 if(pt < 80) return 0.024342;
		 if(pt < 100) return 0.013471;
		 if(pt < 3500) return 0.011453;
		 else return 0;
		 }
	 else return 0;
}


