#include <iostream>
//! 1down 
float GetFF_FF_CR_WJETS_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.156335;
		 if(pt < 40) return 0.145459;
		 if(pt < 45) return 0.127577;
		 if(pt < 50) return 0.115180;
		 if(pt < 60) return 0.113858;
		 if(pt < 80) return 0.095223;
		 if(pt < 100) return 0.084059;
		 if(pt < 200) return 0.071384;
		 if(pt < 3500) return 0.071389;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032096;
		 if(pt < 40) return 0.029365;
		 if(pt < 60) return 0.021821;
		 if(pt < 80) return 0.015175;
		 if(pt < 100) return 0.011918;
		 if(pt < 3500) return 0.010979;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_WJETS_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.156335;
		 if(pt < 40) return 0.145459;
		 if(pt < 45) return 0.127577;
		 if(pt < 50) return 0.115180;
		 if(pt < 60) return 0.113858;
		 if(pt < 80) return 0.095223;
		 if(pt < 100) return 0.084059;
		 if(pt < 200) return 0.071384;
		 if(pt < 3500) return 0.071389;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032096;
		 if(pt < 40) return 0.029365;
		 if(pt < 60) return 0.021821;
		 if(pt < 80) return 0.015175;
		 if(pt < 100) return 0.011918;
		 if(pt < 3500) return 0.010979;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.156335;
		 if(pt < 40) return 0.145459;
		 if(pt < 45) return 0.127577;
		 if(pt < 50) return 0.115180;
		 if(pt < 60) return 0.113858;
		 if(pt < 80) return 0.095223;
		 if(pt < 100) return 0.084059;
		 if(pt < 200) return 0.071384;
		 if(pt < 3500) return 0.071389;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032096;
		 if(pt < 40) return 0.029365;
		 if(pt < 60) return 0.021821;
		 if(pt < 80) return 0.015175;
		 if(pt < 100) return 0.011918;
		 if(pt < 3500) return 0.010979;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1742;
		 if(pt < 40) return 0.1655;
		 if(pt < 45) return 0.1533;
		 if(pt < 50) return 0.1425;
		 if(pt < 60) return 0.1389;
		 if(pt < 80) return 0.1225;
		 if(pt < 100) return 0.1139;
		 if(pt < 200) return 0.1058;
		 if(pt < 3500) return 0.0954;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0349;
		 if(pt < 40) return 0.0320;
		 if(pt < 60) return 0.0260;
		 if(pt < 80) return 0.0215;
		 if(pt < 100) return 0.0197;
		 if(pt < 3500) return 0.0190;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1369;
		 if(pt < 40) return 0.1235;
		 if(pt < 45) return 0.0985;
		 if(pt < 50) return 0.0853;
		 if(pt < 60) return 0.0862;
		 if(pt < 80) return 0.0647;
		 if(pt < 100) return 0.0505;
		 if(pt < 200) return 0.0321;
		 if(pt < 3500) return 0.0439;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0291;
		 if(pt < 40) return 0.0266;
		 if(pt < 60) return 0.0173;
		 if(pt < 80) return 0.0083;
		 if(pt < 100) return 0.0035;
		 if(pt < 3500) return 0.0022;
		 else return 0;
		 }
	 else return 0;
}


//! 1down 
float GetFF_FF_CR_MULTIJET_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129904;
		 if(pt < 40) return 0.116940;
		 if(pt < 45) return 0.093174;
		 if(pt < 50) return 0.082957;
		 if(pt < 60) return 0.084082;
		 if(pt < 80) return 0.077370;
		 if(pt < 100) return 0.069528;
		 if(pt < 200) return 0.061065;
		 if(pt < 3500) return 0.043322;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023619;
		 if(pt < 40) return 0.019911;
		 if(pt < 60) return 0.011820;
		 if(pt < 80) return 0.010993;
		 if(pt < 100) return 0.008789;
		 if(pt < 3500) return 0.007574;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_MULTIJET_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129904;
		 if(pt < 40) return 0.116940;
		 if(pt < 45) return 0.093174;
		 if(pt < 50) return 0.082957;
		 if(pt < 60) return 0.084082;
		 if(pt < 80) return 0.077370;
		 if(pt < 100) return 0.069528;
		 if(pt < 200) return 0.061065;
		 if(pt < 3500) return 0.043322;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023619;
		 if(pt < 40) return 0.019911;
		 if(pt < 60) return 0.011820;
		 if(pt < 80) return 0.010993;
		 if(pt < 100) return 0.008789;
		 if(pt < 3500) return 0.007574;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129904;
		 if(pt < 40) return 0.116940;
		 if(pt < 45) return 0.093174;
		 if(pt < 50) return 0.082957;
		 if(pt < 60) return 0.084082;
		 if(pt < 80) return 0.077370;
		 if(pt < 100) return 0.069528;
		 if(pt < 200) return 0.061065;
		 if(pt < 3500) return 0.043322;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023619;
		 if(pt < 40) return 0.019911;
		 if(pt < 60) return 0.011820;
		 if(pt < 80) return 0.010993;
		 if(pt < 100) return 0.008789;
		 if(pt < 3500) return 0.007574;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1313;
		 if(pt < 40) return 0.1184;
		 if(pt < 45) return 0.0952;
		 if(pt < 50) return 0.0850;
		 if(pt < 60) return 0.0864;
		 if(pt < 80) return 0.0806;
		 if(pt < 100) return 0.0740;
		 if(pt < 200) return 0.0654;
		 if(pt < 3500) return 0.0462;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0239;
		 if(pt < 40) return 0.0205;
		 if(pt < 60) return 0.0124;
		 if(pt < 80) return 0.0118;
		 if(pt < 100) return 0.0101;
		 if(pt < 3500) return 0.0088;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1285;
		 if(pt < 40) return 0.1155;
		 if(pt < 45) return 0.0911;
		 if(pt < 50) return 0.0809;
		 if(pt < 60) return 0.0818;
		 if(pt < 80) return 0.0742;
		 if(pt < 100) return 0.0650;
		 if(pt < 200) return 0.0567;
		 if(pt < 3500) return 0.0404;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0233;
		 if(pt < 40) return 0.0193;
		 if(pt < 60) return 0.0112;
		 if(pt < 80) return 0.0101;
		 if(pt < 100) return 0.0074;
		 if(pt < 3500) return 0.0063;
		 else return 0;
		 }
	 else return 0;
}


