#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.142983;
		 if(pt < 40) return 0.135568;
		 if(pt < 45) return 0.124826;
		 if(pt < 50) return 0.122758;
		 if(pt < 60) return 0.111780;
		 if(pt < 75) return 0.097015;
		 if(pt < 90) return 0.098043;
		 if(pt < 105) return 0.099619;
		 if(pt < 120) return 0.097123;
		 if(pt < 140) return 0.091443;
		 if(pt < 160) return 0.088041;
		 if(pt < 200) return 0.081868;
		 if(pt < 300) return 0.072639;
		 if(pt < 3500) return 0.065648;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.026838;
		 if(pt < 40) return 0.026266;
		 if(pt < 50) return 0.021621;
		 if(pt < 75) return 0.015975;
		 if(pt < 100) return 0.012020;
		 if(pt < 150) return 0.011577;
		 if(pt < 200) return 0.012264;
		 if(pt < 3500) return 0.010754;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.203320;
		 if(pt < 40) return 0.192817;
		 if(pt < 45) return 0.179255;
		 if(pt < 50) return 0.177309;
		 if(pt < 60) return 0.163794;
		 if(pt < 75) return 0.144587;
		 if(pt < 90) return 0.144513;
		 if(pt < 105) return 0.147100;
		 if(pt < 120) return 0.145149;
		 if(pt < 140) return 0.137220;
		 if(pt < 160) return 0.132949;
		 if(pt < 200) return 0.126232;
		 if(pt < 300) return 0.112075;
		 if(pt < 3500) return 0.102337;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.041572;
		 if(pt < 40) return 0.041533;
		 if(pt < 50) return 0.035388;
		 if(pt < 75) return 0.027665;
		 if(pt < 100) return 0.021358;
		 if(pt < 150) return 0.020852;
		 if(pt < 200) return 0.021699;
		 if(pt < 3500) return 0.018116;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.264887;
		 if(pt < 40) return 0.252974;
		 if(pt < 45) return 0.236952;
		 if(pt < 50) return 0.235534;
		 if(pt < 60) return 0.215969;
		 if(pt < 75) return 0.192083;
		 if(pt < 90) return 0.191156;
		 if(pt < 105) return 0.196413;
		 if(pt < 120) return 0.193987;
		 if(pt < 140) return 0.184106;
		 if(pt < 160) return 0.177848;
		 if(pt < 200) return 0.170183;
		 if(pt < 300) return 0.149690;
		 if(pt < 3500) return 0.138671;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.055931;
		 if(pt < 40) return 0.056273;
		 if(pt < 50) return 0.049187;
		 if(pt < 75) return 0.040017;
		 if(pt < 100) return 0.031271;
		 if(pt < 150) return 0.030137;
		 if(pt < 200) return 0.031183;
		 if(pt < 3500) return 0.025894;
		 else return 0;
		 }
	 else return 0;
}


#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.186614;
		 if(pt < 40) return 0.175510;
		 if(pt < 45) return 0.171489;
		 if(pt < 50) return 0.151862;
		 if(pt < 60) return 0.145749;
		 if(pt < 75) return 0.132125;
		 if(pt < 90) return 0.112969;
		 if(pt < 105) return 0.109826;
		 if(pt < 120) return 0.100106;
		 if(pt < 140) return 0.100508;
		 if(pt < 160) return 0.100432;
		 if(pt < 200) return 0.088516;
		 if(pt < 300) return 0.078122;
		 if(pt < 3500) return 0.080606;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032773;
		 if(pt < 40) return 0.034277;
		 if(pt < 50) return 0.026964;
		 if(pt < 75) return 0.020845;
		 if(pt < 100) return 0.013945;
		 if(pt < 150) return 0.012814;
		 if(pt < 200) return 0.013018;
		 if(pt < 3500) return 0.011767;
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
		 if(pt < 90) return 0.162829;
		 if(pt < 105) return 0.160562;
		 if(pt < 120) return 0.145261;
		 if(pt < 140) return 0.148828;
		 if(pt < 160) return 0.148956;
		 if(pt < 200) return 0.132926;
		 if(pt < 300) return 0.119022;
		 if(pt < 3500) return 0.123111;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.048407;
		 if(pt < 40) return 0.051504;
		 if(pt < 50) return 0.041485;
		 if(pt < 75) return 0.033506;
		 if(pt < 100) return 0.023305;
		 if(pt < 150) return 0.022379;
		 if(pt < 200) return 0.021838;
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
		 if(pt < 90) return 0.214208;
		 if(pt < 105) return 0.209549;
		 if(pt < 120) return 0.190411;
		 if(pt < 140) return 0.194428;
		 if(pt < 160) return 0.198113;
		 if(pt < 200) return 0.178659;
		 if(pt < 300) return 0.159907;
		 if(pt < 3500) return 0.172392;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.063528;
		 if(pt < 40) return 0.068138;
		 if(pt < 50) return 0.055670;
		 if(pt < 75) return 0.046128;
		 if(pt < 100) return 0.032968;
		 if(pt < 150) return 0.032304;
		 if(pt < 200) return 0.031668;
		 if(pt < 3500) return 0.027678;
		 else return 0;
		 }
	 else return 0;
}


