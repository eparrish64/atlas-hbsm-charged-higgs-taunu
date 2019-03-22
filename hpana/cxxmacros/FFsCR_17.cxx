#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.141699;
		 if(pt < 40) return 0.125668;
		 if(pt < 45) return 0.096866;
		 if(pt < 50) return 0.090556;
		 if(pt < 60) return 0.098437;
		 if(pt < 80) return 0.095746;
		 if(pt < 100) return 0.084946;
		 if(pt < 200) return 0.079665;
		 if(pt < 3500) return 0.060062;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.029500;
		 if(pt < 40) return 0.027629;
		 if(pt < 60) return 0.015918;
		 if(pt < 80) return 0.014972;
		 if(pt < 100) return 0.011111;
		 if(pt < 3500) return 0.010286;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.202452;
		 if(pt < 40) return 0.181926;
		 if(pt < 45) return 0.143953;
		 if(pt < 50) return 0.134877;
		 if(pt < 60) return 0.144918;
		 if(pt < 80) return 0.143415;
		 if(pt < 100) return 0.127861;
		 if(pt < 200) return 0.122209;
		 if(pt < 3500) return 0.095658;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.046830;
		 if(pt < 40) return 0.045315;
		 if(pt < 60) return 0.027534;
		 if(pt < 80) return 0.025665;
		 if(pt < 100) return 0.019819;
		 if(pt < 3500) return 0.017531;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.267533;
		 if(pt < 40) return 0.241566;
		 if(pt < 45) return 0.193749;
		 if(pt < 50) return 0.181319;
		 if(pt < 60) return 0.192625;
		 if(pt < 80) return 0.191539;
		 if(pt < 100) return 0.173766;
		 if(pt < 200) return 0.164420;
		 if(pt < 3500) return 0.132554;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.063736;
		 if(pt < 40) return 0.062447;
		 if(pt < 60) return 0.039299;
		 if(pt < 80) return 0.036441;
		 if(pt < 100) return 0.029023;
		 if(pt < 3500) return 0.025818;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.198521;
		 if(pt < 40) return 0.182550;
		 if(pt < 45) return 0.171654;
		 if(pt < 50) return 0.150667;
		 if(pt < 60) return 0.153173;
		 if(pt < 80) return 0.137251;
		 if(pt < 100) return 0.117190;
		 if(pt < 200) return 0.097545;
		 if(pt < 3500) return 0.093153;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.037181;
		 if(pt < 40) return 0.037265;
		 if(pt < 60) return 0.029262;
		 if(pt < 80) return 0.019134;
		 if(pt < 100) return 0.015005;
		 if(pt < 3500) return 0.014078;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.269081;
		 if(pt < 40) return 0.247254;
		 if(pt < 45) return 0.236268;
		 if(pt < 50) return 0.209371;
		 if(pt < 60) return 0.213872;
		 if(pt < 80) return 0.197400;
		 if(pt < 100) return 0.171965;
		 if(pt < 200) return 0.144440;
		 if(pt < 3500) return 0.141797;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.054435;
		 if(pt < 40) return 0.056156;
		 if(pt < 60) return 0.045153;
		 if(pt < 80) return 0.031154;
		 if(pt < 100) return 0.025569;
		 if(pt < 3500) return 0.023403;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.345674;
		 if(pt < 40) return 0.313495;
		 if(pt < 45) return 0.301681;
		 if(pt < 50) return 0.269022;
		 if(pt < 60) return 0.274778;
		 if(pt < 80) return 0.259227;
		 if(pt < 100) return 0.226484;
		 if(pt < 200) return 0.189482;
		 if(pt < 3500) return 0.193310;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.071594;
		 if(pt < 40) return 0.074442;
		 if(pt < 60) return 0.060723;
		 if(pt < 80) return 0.043178;
		 if(pt < 100) return 0.036569;
		 if(pt < 3500) return 0.034128;
		 else return 0;
		 }
	 else return 0;
}


