#include <iostream>
//! 1down 
float GetFF_FF_CR_WJETS_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.259548;
		 if(pt < 40) return 0.220996;
		 if(pt < 45) return 0.210538;
		 if(pt < 50) return 0.192821;
		 if(pt < 60) return 0.209098;
		 if(pt < 80) return 0.184467;
		 if(pt < 100) return 0.170132;
		 if(pt < 200) return 0.144862;
		 if(pt < 3500) return 0.161255;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.063258;
		 if(pt < 40) return 0.064209;
		 if(pt < 60) return 0.051586;
		 if(pt < 80) return 0.038727;
		 if(pt < 100) return 0.027822;
		 if(pt < 3500) return 0.034605;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_WJETS_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.137178;
		 if(pt < 40) return 0.113602;
		 if(pt < 45) return 0.105409;
		 if(pt < 50) return 0.097169;
		 if(pt < 60) return 0.103307;
		 if(pt < 80) return 0.090147;
		 if(pt < 100) return 0.079900;
		 if(pt < 200) return 0.066664;
		 if(pt < 3500) return 0.068428;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032809;
		 if(pt < 40) return 0.032669;
		 if(pt < 60) return 0.025076;
		 if(pt < 80) return 0.017949;
		 if(pt < 100) return 0.012458;
		 if(pt < 3500) return 0.014392;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.197460;
		 if(pt < 40) return 0.165789;
		 if(pt < 45) return 0.156749;
		 if(pt < 50) return 0.144623;
		 if(pt < 60) return 0.153961;
		 if(pt < 80) return 0.136972;
		 if(pt < 100) return 0.122641;
		 if(pt < 200) return 0.103910;
		 if(pt < 3500) return 0.110861;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.048256;
		 if(pt < 40) return 0.048551;
		 if(pt < 60) return 0.038415;
		 if(pt < 80) return 0.028403;
		 if(pt < 100) return 0.020212;
		 if(pt < 3500) return 0.024411;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2533;
		 if(pt < 40) return 0.2394;
		 if(pt < 45) return 0.2320;
		 if(pt < 50) return 0.2163;
		 if(pt < 60) return 0.2092;
		 if(pt < 80) return 0.1865;
		 if(pt < 100) return 0.1746;
		 if(pt < 200) return 0.1585;
		 if(pt < 3500) return 0.1536;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0528;
		 if(pt < 40) return 0.0523;
		 if(pt < 60) return 0.0449;
		 if(pt < 80) return 0.0385;
		 if(pt < 100) return 0.0349;
		 if(pt < 3500) return 0.0388;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1332;
		 if(pt < 40) return 0.0777;
		 if(pt < 45) return 0.0666;
		 if(pt < 50) return 0.0608;
		 if(pt < 60) return 0.0916;
		 if(pt < 80) return 0.0800;
		 if(pt < 100) return 0.0627;
		 if(pt < 200) return 0.0408;
		 if(pt < 3500) return 0.0619;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0434;
		 if(pt < 40) return 0.0446;
		 if(pt < 60) return 0.0315;
		 if(pt < 80) return 0.0176;
		 if(pt < 100) return 0.0044;
		 if(pt < 3500) return 0.0089;
		 else return 0;
		 }
	 else return 0;
}


//! 1down 
float GetFF_FF_CR_MULTIJET_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.248632;
		 if(pt < 40) return 0.229753;
		 if(pt < 45) return 0.195101;
		 if(pt < 50) return 0.176938;
		 if(pt < 60) return 0.179300;
		 if(pt < 80) return 0.166851;
		 if(pt < 100) return 0.151575;
		 if(pt < 200) return 0.133217;
		 if(pt < 3500) return 0.102469;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.051919;
		 if(pt < 40) return 0.045421;
		 if(pt < 60) return 0.033124;
		 if(pt < 80) return 0.029348;
		 if(pt < 100) return 0.023650;
		 if(pt < 3500) return 0.022718;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_MULTIJET_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.123969;
		 if(pt < 40) return 0.110225;
		 if(pt < 45) return 0.091022;
		 if(pt < 50) return 0.081434;
		 if(pt < 60) return 0.082339;
		 if(pt < 80) return 0.075655;
		 if(pt < 100) return 0.067664;
		 if(pt < 200) return 0.059267;
		 if(pt < 3500) return 0.042303;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.024635;
		 if(pt < 40) return 0.020454;
		 if(pt < 60) return 0.013570;
		 if(pt < 80) return 0.012382;
		 if(pt < 100) return 0.009728;
		 if(pt < 3500) return 0.008847;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.184908;
		 if(pt < 40) return 0.168944;
		 if(pt < 45) return 0.142044;
		 if(pt < 50) return 0.128236;
		 if(pt < 60) return 0.128902;
		 if(pt < 80) return 0.119363;
		 if(pt < 100) return 0.108350;
		 if(pt < 200) return 0.094863;
		 if(pt < 3500) return 0.070571;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.038502;
		 if(pt < 40) return 0.033067;
		 if(pt < 60) return 0.023315;
		 if(pt < 80) return 0.020868;
		 if(pt < 100) return 0.016598;
		 if(pt < 3500) return 0.015655;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1869;
		 if(pt < 40) return 0.1710;
		 if(pt < 45) return 0.1450;
		 if(pt < 50) return 0.1317;
		 if(pt < 60) return 0.1321;
		 if(pt < 80) return 0.1244;
		 if(pt < 100) return 0.1156;
		 if(pt < 200) return 0.1017;
		 if(pt < 3500) return 0.0755;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0390;
		 if(pt < 40) return 0.0342;
		 if(pt < 60) return 0.0243;
		 if(pt < 80) return 0.0225;
		 if(pt < 100) return 0.0193;
		 if(pt < 3500) return 0.0183;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1830;
		 if(pt < 40) return 0.1668;
		 if(pt < 45) return 0.1391;
		 if(pt < 50) return 0.1248;
		 if(pt < 60) return 0.1257;
		 if(pt < 80) return 0.1143;
		 if(pt < 100) return 0.1011;
		 if(pt < 200) return 0.0880;
		 if(pt < 3500) return 0.0656;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0380;
		 if(pt < 40) return 0.0319;
		 if(pt < 60) return 0.0223;
		 if(pt < 80) return 0.0192;
		 if(pt < 100) return 0.0139;
		 if(pt < 3500) return 0.0130;
		 else return 0;
		 }
	 else return 0;
}


