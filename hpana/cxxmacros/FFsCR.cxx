#include <iostream>
//! RNN_1up 
float GetFF_FF_CR_WJETS_RNN_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.038073;
		 if(pt < 40) return 0.031114;
		 if(pt < 45) return 0.026358;
		 if(pt < 50) return 0.022416;
		 if(pt < 60) return 0.021807;
		 if(pt < 80) return 0.016288;
		 if(pt < 100) return 0.012208;
		 if(pt < 200) return 0.008852;
		 if(pt < 3500) return 0.005831;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.008596;
		 if(pt < 40) return 0.007709;
		 if(pt < 60) return 0.004665;
		 if(pt < 80) return 0.002384;
		 if(pt < 100) return 0.001339;
		 if(pt < 3500) return 0.001235;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.038073;
		 if(pt < 40) return 0.031114;
		 if(pt < 45) return 0.026358;
		 if(pt < 50) return 0.022416;
		 if(pt < 60) return 0.021807;
		 if(pt < 80) return 0.016288;
		 if(pt < 100) return 0.012208;
		 if(pt < 200) return 0.008852;
		 if(pt < 3500) return 0.005831;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.008596;
		 if(pt < 40) return 0.007709;
		 if(pt < 60) return 0.004665;
		 if(pt < 80) return 0.002384;
		 if(pt < 100) return 0.001339;
		 if(pt < 3500) return 0.001235;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.0502;
		 if(pt < 40) return 0.0465;
		 if(pt < 45) return 0.0403;
		 if(pt < 50) return 0.0343;
		 if(pt < 60) return 0.0298;
		 if(pt < 80) return 0.0223;
		 if(pt < 100) return 0.0173;
		 if(pt < 200) return 0.0134;
		 if(pt < 3500) return 0.0079;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0094;
		 if(pt < 40) return 0.0083;
		 if(pt < 60) return 0.0055;
		 if(pt < 80) return 0.0032;
		 if(pt < 100) return 0.0023;
		 if(pt < 3500) return 0.0020;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.0249;
		 if(pt < 40) return 0.0140;
		 if(pt < 45) return 0.0108;
		 if(pt < 50) return 0.0092;
		 if(pt < 60) return 0.0129;
		 if(pt < 80) return 0.0095;
		 if(pt < 100) return 0.0063;
		 if(pt < 200) return 0.0035;
		 if(pt < 3500) return 0.0033;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0077;
		 if(pt < 40) return 0.0071;
		 if(pt < 60) return 0.0038;
		 if(pt < 80) return 0.0015;
		 if(pt < 100) return 0.0003;
		 if(pt < 3500) return 0.0004;
		 else return 0;
		 }
	 else return 0;
}


//! RNN_1down 
float GetFF_FF_CR_WJETS_RNN_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.038073;
		 if(pt < 40) return 0.031114;
		 if(pt < 45) return 0.026358;
		 if(pt < 50) return 0.022416;
		 if(pt < 60) return 0.021807;
		 if(pt < 80) return 0.016288;
		 if(pt < 100) return 0.012208;
		 if(pt < 200) return 0.008852;
		 if(pt < 3500) return 0.005831;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.008596;
		 if(pt < 40) return 0.007709;
		 if(pt < 60) return 0.004665;
		 if(pt < 80) return 0.002384;
		 if(pt < 100) return 0.001339;
		 if(pt < 3500) return 0.001235;
		 else return 0;
		 }
	 else return 0;
}


//! RNN_1up 
float GetFF_FF_CR_MULTIJET_RNN_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.022836;
		 if(pt < 40) return 0.018197;
		 if(pt < 45) return 0.012827;
		 if(pt < 50) return 0.010782;
		 if(pt < 60) return 0.010455;
		 if(pt < 80) return 0.008037;
		 if(pt < 100) return 0.006160;
		 if(pt < 200) return 0.004731;
		 if(pt < 3500) return 0.002388;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.003931;
		 if(pt < 40) return 0.002603;
		 if(pt < 60) return 0.001172;
		 if(pt < 80) return 0.000966;
		 if(pt < 100) return 0.000657;
		 if(pt < 3500) return 0.000511;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.022836;
		 if(pt < 40) return 0.018197;
		 if(pt < 45) return 0.012827;
		 if(pt < 50) return 0.010782;
		 if(pt < 60) return 0.010455;
		 if(pt < 80) return 0.008037;
		 if(pt < 100) return 0.006160;
		 if(pt < 200) return 0.004731;
		 if(pt < 3500) return 0.002388;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.003931;
		 if(pt < 40) return 0.002603;
		 if(pt < 60) return 0.001172;
		 if(pt < 80) return 0.000966;
		 if(pt < 100) return 0.000657;
		 if(pt < 3500) return 0.000511;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.0231;
		 if(pt < 40) return 0.0184;
		 if(pt < 45) return 0.0131;
		 if(pt < 50) return 0.0111;
		 if(pt < 60) return 0.0107;
		 if(pt < 80) return 0.0084;
		 if(pt < 100) return 0.0066;
		 if(pt < 200) return 0.0051;
		 if(pt < 3500) return 0.0026;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0040;
		 if(pt < 40) return 0.0027;
		 if(pt < 60) return 0.0012;
		 if(pt < 80) return 0.0010;
		 if(pt < 100) return 0.0008;
		 if(pt < 3500) return 0.0006;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.0226;
		 if(pt < 40) return 0.0180;
		 if(pt < 45) return 0.0126;
		 if(pt < 50) return 0.0105;
		 if(pt < 60) return 0.0102;
		 if(pt < 80) return 0.0077;
		 if(pt < 100) return 0.0057;
		 if(pt < 200) return 0.0044;
		 if(pt < 3500) return 0.0022;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0039;
		 if(pt < 40) return 0.0025;
		 if(pt < 60) return 0.0011;
		 if(pt < 80) return 0.0009;
		 if(pt < 100) return 0.0006;
		 if(pt < 3500) return 0.0004;
		 else return 0;
		 }
	 else return 0;
}


//! RNN_1down 
float GetFF_FF_CR_MULTIJET_RNN_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.022836;
		 if(pt < 40) return 0.018197;
		 if(pt < 45) return 0.012827;
		 if(pt < 50) return 0.010782;
		 if(pt < 60) return 0.010455;
		 if(pt < 80) return 0.008037;
		 if(pt < 100) return 0.006160;
		 if(pt < 200) return 0.004731;
		 if(pt < 3500) return 0.002388;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.003931;
		 if(pt < 40) return 0.002603;
		 if(pt < 60) return 0.001172;
		 if(pt < 80) return 0.000966;
		 if(pt < 100) return 0.000657;
		 if(pt < 3500) return 0.000511;
		 else return 0;
		 }
	 else return 0;
}


