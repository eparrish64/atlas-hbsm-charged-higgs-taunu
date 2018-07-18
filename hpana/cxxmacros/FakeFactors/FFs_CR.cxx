#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2047;
		 if(pt < 40) return 0.1894;
		 if(pt < 45) return 0.1740;
		 if(pt < 50) return 0.1615;
		 if(pt < 60) return 0.1367;
		 if(pt < 75) return 0.1098;
		 if(pt < 90) return 0.1267;
		 if(pt < 105) return 0.1350;
		 if(pt < 120) return 0.1348;
		 if(pt < 140) return 0.1278;
		 if(pt < 160) return 0.1223;
		 if(pt < 200) return 0.1189;
		 if(pt < 300) return 0.1061;
		 if(pt < 3500) return 0.0981;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0432;
		 if(pt < 40) return 0.0445;
		 if(pt < 50) return 0.0345;
		 if(pt < 75) return 0.0234;
		 if(pt < 100) return 0.0175;
		 if(pt < 150) return 0.0185;
		 if(pt < 200) return 0.0201;
		 if(pt < 3500) return 0.0166;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2047;
		 if(pt < 40) return 0.1894;
		 if(pt < 45) return 0.1740;
		 if(pt < 50) return 0.1615;
		 if(pt < 60) return 0.1367;
		 if(pt < 75) return 0.1098;
		 if(pt < 90) return 0.1267;
		 if(pt < 105) return 0.1350;
		 if(pt < 120) return 0.1348;
		 if(pt < 140) return 0.1278;
		 if(pt < 160) return 0.1223;
		 if(pt < 200) return 0.1189;
		 if(pt < 300) return 0.1061;
		 if(pt < 3500) return 0.0981;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0432;
		 if(pt < 40) return 0.0445;
		 if(pt < 50) return 0.0345;
		 if(pt < 75) return 0.0234;
		 if(pt < 100) return 0.0175;
		 if(pt < 150) return 0.0185;
		 if(pt < 200) return 0.0201;
		 if(pt < 3500) return 0.0166;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_MULTIJET(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2666;
		 if(pt < 40) return 0.2482;
		 if(pt < 45) return 0.2290;
		 if(pt < 50) return 0.2133;
		 if(pt < 60) return 0.1822;
		 if(pt < 75) return 0.1481;
		 if(pt < 90) return 0.1681;
		 if(pt < 105) return 0.1809;
		 if(pt < 120) return 0.1809;
		 if(pt < 140) return 0.1723;
		 if(pt < 160) return 0.1636;
		 if(pt < 200) return 0.1615;
		 if(pt < 300) return 0.1417;
		 if(pt < 3500) return 0.1330;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0579;
		 if(pt < 40) return 0.0600;
		 if(pt < 50) return 0.0477;
		 if(pt < 75) return 0.0344;
		 if(pt < 100) return 0.0257;
		 if(pt < 150) return 0.0266;
		 if(pt < 200) return 0.0288;
		 if(pt < 3500) return 0.0236;
		 else return 0;
		 }
	 else return 0;
}


#include <iostream>
//! tau_0_jet_bdt_score_trans lower cut (0.01)
float GetFF01_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2847;
		 if(pt < 40) return 0.2871;
		 if(pt < 45) return 0.2822;
		 if(pt < 50) return 0.2771;
		 if(pt < 60) return 0.2555;
		 if(pt < 75) return 0.2368;
		 if(pt < 90) return 0.2231;
		 if(pt < 105) return 0.2246;
		 if(pt < 120) return 0.2276;
		 if(pt < 140) return 0.2390;
		 if(pt < 160) return 0.2415;
		 if(pt < 200) return 0.2130;
		 if(pt < 300) return 0.1779;
		 if(pt < 3500) return 0.1974;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0581;
		 if(pt < 40) return 0.0572;
		 if(pt < 50) return 0.0475;
		 if(pt < 75) return 0.0443;
		 if(pt < 100) return 0.0391;
		 if(pt < 150) return 0.0358;
		 if(pt < 200) return 0.0316;
		 if(pt < 3500) return 0.0246;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.02)
float GetFF02_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2847;
		 if(pt < 40) return 0.2871;
		 if(pt < 45) return 0.2822;
		 if(pt < 50) return 0.2771;
		 if(pt < 60) return 0.2555;
		 if(pt < 75) return 0.2368;
		 if(pt < 90) return 0.2231;
		 if(pt < 105) return 0.2246;
		 if(pt < 120) return 0.2276;
		 if(pt < 140) return 0.2390;
		 if(pt < 160) return 0.2415;
		 if(pt < 200) return 0.2130;
		 if(pt < 300) return 0.1779;
		 if(pt < 3500) return 0.1974;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0581;
		 if(pt < 40) return 0.0572;
		 if(pt < 50) return 0.0475;
		 if(pt < 75) return 0.0443;
		 if(pt < 100) return 0.0391;
		 if(pt < 150) return 0.0358;
		 if(pt < 200) return 0.0316;
		 if(pt < 3500) return 0.0246;
		 else return 0;
		 }
	 else return 0;
}


//! tau_0_jet_bdt_score_trans lower cut (0.03)
float GetFF03_FF_CR_WJETS(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.3630;
		 if(pt < 40) return 0.3663;
		 if(pt < 45) return 0.3639;
		 if(pt < 50) return 0.3564;
		 if(pt < 60) return 0.3282;
		 if(pt < 75) return 0.3021;
		 if(pt < 90) return 0.2916;
		 if(pt < 105) return 0.2969;
		 if(pt < 120) return 0.3069;
		 if(pt < 140) return 0.3197;
		 if(pt < 160) return 0.3267;
		 if(pt < 200) return 0.2771;
		 if(pt < 300) return 0.2358;
		 if(pt < 3500) return 0.2674;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0764;
		 if(pt < 40) return 0.0758;
		 if(pt < 50) return 0.0642;
		 if(pt < 75) return 0.0610;
		 if(pt < 100) return 0.0553;
		 if(pt < 150) return 0.0514;
		 if(pt < 200) return 0.0462;
		 if(pt < 3500) return 0.0352;
		 else return 0;
		 }
	 else return 0;
}


