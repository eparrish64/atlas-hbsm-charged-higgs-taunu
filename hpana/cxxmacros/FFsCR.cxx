#include <iostream>
//! 1down 
float GetFF_FF_CR_WJETS_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.160773;
		 if(pt < 40) return 0.149014;
		 if(pt < 45) return 0.133710;
		 if(pt < 50) return 0.120346;
		 if(pt < 60) return 0.116184;
		 if(pt < 80) return 0.096251;
		 if(pt < 100) return 0.088349;
		 if(pt < 200) return 0.073687;
		 if(pt < 3500) return 0.072027;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032493;
		 if(pt < 40) return 0.029750;
		 if(pt < 60) return 0.022033;
		 if(pt < 80) return 0.015457;
		 if(pt < 100) return 0.012093;
		 if(pt < 3500) return 0.011287;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_WJETS_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.160773;
		 if(pt < 40) return 0.149014;
		 if(pt < 45) return 0.133710;
		 if(pt < 50) return 0.120346;
		 if(pt < 60) return 0.116184;
		 if(pt < 80) return 0.096251;
		 if(pt < 100) return 0.088349;
		 if(pt < 200) return 0.073687;
		 if(pt < 3500) return 0.072027;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032493;
		 if(pt < 40) return 0.029750;
		 if(pt < 60) return 0.022033;
		 if(pt < 80) return 0.015457;
		 if(pt < 100) return 0.012093;
		 if(pt < 3500) return 0.011287;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.160773;
		 if(pt < 40) return 0.149014;
		 if(pt < 45) return 0.133710;
		 if(pt < 50) return 0.120346;
		 if(pt < 60) return 0.116184;
		 if(pt < 80) return 0.096251;
		 if(pt < 100) return 0.088349;
		 if(pt < 200) return 0.073687;
		 if(pt < 3500) return 0.072027;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032493;
		 if(pt < 40) return 0.029750;
		 if(pt < 60) return 0.022033;
		 if(pt < 80) return 0.015457;
		 if(pt < 100) return 0.012093;
		 if(pt < 3500) return 0.011287;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1566;
		 if(pt < 40) return 0.1450;
		 if(pt < 45) return 0.1287;
		 if(pt < 50) return 0.1167;
		 if(pt < 60) return 0.1125;
		 if(pt < 80) return 0.0928;
		 if(pt < 100) return 0.0851;
		 if(pt < 200) return 0.0707;
		 if(pt < 3500) return 0.0691;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0317;
		 if(pt < 40) return 0.0290;
		 if(pt < 60) return 0.0213;
		 if(pt < 80) return 0.0149;
		 if(pt < 100) return 0.0116;
		 if(pt < 3500) return 0.0108;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1652;
		 if(pt < 40) return 0.1533;
		 if(pt < 45) return 0.1392;
		 if(pt < 50) return 0.1242;
		 if(pt < 60) return 0.1201;
		 if(pt < 80) return 0.0999;
		 if(pt < 100) return 0.0918;
		 if(pt < 200) return 0.0769;
		 if(pt < 3500) return 0.0752;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0333;
		 if(pt < 40) return 0.0306;
		 if(pt < 60) return 0.0228;
		 if(pt < 80) return 0.0161;
		 if(pt < 100) return 0.0127;
		 if(pt < 3500) return 0.0118;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1up 
float GetFF_FF_CR_WJETS_tauID_SF_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1627;
		 if(pt < 40) return 0.1512;
		 if(pt < 45) return 0.1365;
		 if(pt < 50) return 0.1232;
		 if(pt < 60) return 0.1189;
		 if(pt < 80) return 0.0992;
		 if(pt < 100) return 0.0915;
		 if(pt < 200) return 0.0773;
		 if(pt < 3500) return 0.0745;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0329;
		 if(pt < 40) return 0.0301;
		 if(pt < 60) return 0.0225;
		 if(pt < 80) return 0.0162;
		 if(pt < 100) return 0.0129;
		 if(pt < 3500) return 0.0122;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1down 
float GetFF_FF_CR_WJETS_tauID_SF_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1588;
		 if(pt < 40) return 0.1468;
		 if(pt < 45) return 0.1309;
		 if(pt < 50) return 0.1175;
		 if(pt < 60) return 0.1134;
		 if(pt < 80) return 0.0933;
		 if(pt < 100) return 0.0852;
		 if(pt < 200) return 0.0701;
		 if(pt < 3500) return 0.0696;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0321;
		 if(pt < 40) return 0.0294;
		 if(pt < 60) return 0.0215;
		 if(pt < 80) return 0.0147;
		 if(pt < 100) return 0.0112;
		 if(pt < 3500) return 0.0104;
		 else return 0;
		 }
	 else return 0;
}


//! 1down 
float GetFF_FF_CR_MULTIJET_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129901;
		 if(pt < 40) return 0.116972;
		 if(pt < 45) return 0.093165;
		 if(pt < 50) return 0.083054;
		 if(pt < 60) return 0.084043;
		 if(pt < 80) return 0.077358;
		 if(pt < 100) return 0.069476;
		 if(pt < 200) return 0.061077;
		 if(pt < 3500) return 0.043401;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023593;
		 if(pt < 40) return 0.019925;
		 if(pt < 60) return 0.011816;
		 if(pt < 80) return 0.010980;
		 if(pt < 100) return 0.008763;
		 if(pt < 3500) return 0.007556;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_MULTIJET_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129901;
		 if(pt < 40) return 0.116972;
		 if(pt < 45) return 0.093165;
		 if(pt < 50) return 0.083054;
		 if(pt < 60) return 0.084043;
		 if(pt < 80) return 0.077358;
		 if(pt < 100) return 0.069476;
		 if(pt < 200) return 0.061077;
		 if(pt < 3500) return 0.043401;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023593;
		 if(pt < 40) return 0.019925;
		 if(pt < 60) return 0.011816;
		 if(pt < 80) return 0.010980;
		 if(pt < 100) return 0.008763;
		 if(pt < 3500) return 0.007556;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129901;
		 if(pt < 40) return 0.116972;
		 if(pt < 45) return 0.093165;
		 if(pt < 50) return 0.083054;
		 if(pt < 60) return 0.084043;
		 if(pt < 80) return 0.077358;
		 if(pt < 100) return 0.069476;
		 if(pt < 200) return 0.061077;
		 if(pt < 3500) return 0.043401;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023593;
		 if(pt < 40) return 0.019925;
		 if(pt < 60) return 0.011816;
		 if(pt < 80) return 0.010980;
		 if(pt < 100) return 0.008763;
		 if(pt < 3500) return 0.007556;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1298;
		 if(pt < 40) return 0.1169;
		 if(pt < 45) return 0.0931;
		 if(pt < 50) return 0.0830;
		 if(pt < 60) return 0.0840;
		 if(pt < 80) return 0.0773;
		 if(pt < 100) return 0.0694;
		 if(pt < 200) return 0.0610;
		 if(pt < 3500) return 0.0433;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0236;
		 if(pt < 40) return 0.0199;
		 if(pt < 60) return 0.0118;
		 if(pt < 80) return 0.0110;
		 if(pt < 100) return 0.0088;
		 if(pt < 3500) return 0.0075;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1300;
		 if(pt < 40) return 0.1170;
		 if(pt < 45) return 0.0932;
		 if(pt < 50) return 0.0831;
		 if(pt < 60) return 0.0841;
		 if(pt < 80) return 0.0775;
		 if(pt < 100) return 0.0696;
		 if(pt < 200) return 0.0612;
		 if(pt < 3500) return 0.0435;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0236;
		 if(pt < 40) return 0.0199;
		 if(pt < 60) return 0.0118;
		 if(pt < 80) return 0.0110;
		 if(pt < 100) return 0.0088;
		 if(pt < 3500) return 0.0076;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1up 
float GetFF_FF_CR_MULTIJET_tauID_SF_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1300;
		 if(pt < 40) return 0.1171;
		 if(pt < 45) return 0.0934;
		 if(pt < 50) return 0.0833;
		 if(pt < 60) return 0.0843;
		 if(pt < 80) return 0.0777;
		 if(pt < 100) return 0.0699;
		 if(pt < 200) return 0.0615;
		 if(pt < 3500) return 0.0437;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0236;
		 if(pt < 40) return 0.0200;
		 if(pt < 60) return 0.0119;
		 if(pt < 80) return 0.0111;
		 if(pt < 100) return 0.0089;
		 if(pt < 3500) return 0.0077;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1down 
float GetFF_FF_CR_MULTIJET_tauID_SF_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1298;
		 if(pt < 40) return 0.1168;
		 if(pt < 45) return 0.0930;
		 if(pt < 50) return 0.0828;
		 if(pt < 60) return 0.0838;
		 if(pt < 80) return 0.0770;
		 if(pt < 100) return 0.0690;
		 if(pt < 200) return 0.0606;
		 if(pt < 3500) return 0.0431;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0236;
		 if(pt < 40) return 0.0199;
		 if(pt < 60) return 0.0118;
		 if(pt < 80) return 0.0109;
		 if(pt < 100) return 0.0086;
		 if(pt < 3500) return 0.0074;
		 else return 0;
		 }
	 else return 0;
}


