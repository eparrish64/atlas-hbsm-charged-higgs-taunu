#include <iostream>
//! 1down 
float GetFF_FF_CR_WJETS_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.155542;
		 if(pt < 40) return 0.144445;
		 if(pt < 45) return 0.127696;
		 if(pt < 50) return 0.114561;
		 if(pt < 60) return 0.113721;
		 if(pt < 80) return 0.094556;
		 if(pt < 100) return 0.084566;
		 if(pt < 200) return 0.071063;
		 if(pt < 3500) return 0.067712;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032526;
		 if(pt < 40) return 0.029805;
		 if(pt < 60) return 0.022077;
		 if(pt < 80) return 0.015418;
		 if(pt < 100) return 0.012108;
		 if(pt < 3500) return 0.011369;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_WJETS_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.155542;
		 if(pt < 40) return 0.144445;
		 if(pt < 45) return 0.127696;
		 if(pt < 50) return 0.114561;
		 if(pt < 60) return 0.113721;
		 if(pt < 80) return 0.094556;
		 if(pt < 100) return 0.084566;
		 if(pt < 200) return 0.071063;
		 if(pt < 3500) return 0.067712;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032526;
		 if(pt < 40) return 0.029805;
		 if(pt < 60) return 0.022077;
		 if(pt < 80) return 0.015418;
		 if(pt < 100) return 0.012108;
		 if(pt < 3500) return 0.011369;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.155542;
		 if(pt < 40) return 0.144445;
		 if(pt < 45) return 0.127696;
		 if(pt < 50) return 0.114561;
		 if(pt < 60) return 0.113721;
		 if(pt < 80) return 0.094556;
		 if(pt < 100) return 0.084566;
		 if(pt < 200) return 0.071063;
		 if(pt < 3500) return 0.067712;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032526;
		 if(pt < 40) return 0.029805;
		 if(pt < 60) return 0.022077;
		 if(pt < 80) return 0.015418;
		 if(pt < 100) return 0.012108;
		 if(pt < 3500) return 0.011369;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1491;
		 if(pt < 40) return 0.1380;
		 if(pt < 45) return 0.1203;
		 if(pt < 50) return 0.1096;
		 if(pt < 60) return 0.1084;
		 if(pt < 80) return 0.0896;
		 if(pt < 100) return 0.0800;
		 if(pt < 200) return 0.0666;
		 if(pt < 3500) return 0.0634;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0317;
		 if(pt < 40) return 0.0290;
		 if(pt < 60) return 0.0214;
		 if(pt < 80) return 0.0148;
		 if(pt < 100) return 0.0116;
		 if(pt < 3500) return 0.0109;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1625;
		 if(pt < 40) return 0.1515;
		 if(pt < 45) return 0.1361;
		 if(pt < 50) return 0.1199;
		 if(pt < 60) return 0.1196;
		 if(pt < 80) return 0.1001;
		 if(pt < 100) return 0.0897;
		 if(pt < 200) return 0.0761;
		 if(pt < 3500) return 0.0726;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0334;
		 if(pt < 40) return 0.0306;
		 if(pt < 60) return 0.0228;
		 if(pt < 80) return 0.0160;
		 if(pt < 100) return 0.0127;
		 if(pt < 3500) return 0.0119;
		 else return 0;
		 }
	 else return 0;
}


//! 1down 
float GetFF_FF_CR_MULTIJET_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129898;
		 if(pt < 40) return 0.116931;
		 if(pt < 45) return 0.093164;
		 if(pt < 50) return 0.082943;
		 if(pt < 60) return 0.084070;
		 if(pt < 80) return 0.077350;
		 if(pt < 100) return 0.069496;
		 if(pt < 200) return 0.061027;
		 if(pt < 3500) return 0.043291;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023618;
		 if(pt < 40) return 0.019910;
		 if(pt < 60) return 0.011817;
		 if(pt < 80) return 0.010987;
		 if(pt < 100) return 0.008778;
		 if(pt < 3500) return 0.007562;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_MULTIJET_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129898;
		 if(pt < 40) return 0.116931;
		 if(pt < 45) return 0.093164;
		 if(pt < 50) return 0.082943;
		 if(pt < 60) return 0.084070;
		 if(pt < 80) return 0.077350;
		 if(pt < 100) return 0.069496;
		 if(pt < 200) return 0.061027;
		 if(pt < 3500) return 0.043291;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023618;
		 if(pt < 40) return 0.019910;
		 if(pt < 60) return 0.011817;
		 if(pt < 80) return 0.010987;
		 if(pt < 100) return 0.008778;
		 if(pt < 3500) return 0.007562;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129898;
		 if(pt < 40) return 0.116931;
		 if(pt < 45) return 0.093164;
		 if(pt < 50) return 0.082943;
		 if(pt < 60) return 0.084070;
		 if(pt < 80) return 0.077350;
		 if(pt < 100) return 0.069496;
		 if(pt < 200) return 0.061027;
		 if(pt < 3500) return 0.043291;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023618;
		 if(pt < 40) return 0.019910;
		 if(pt < 60) return 0.011817;
		 if(pt < 80) return 0.010987;
		 if(pt < 100) return 0.008778;
		 if(pt < 3500) return 0.007562;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1298;
		 if(pt < 40) return 0.1168;
		 if(pt < 45) return 0.0931;
		 if(pt < 50) return 0.0829;
		 if(pt < 60) return 0.0840;
		 if(pt < 80) return 0.0772;
		 if(pt < 100) return 0.0694;
		 if(pt < 200) return 0.0609;
		 if(pt < 3500) return 0.0432;
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


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1300;
		 if(pt < 40) return 0.1170;
		 if(pt < 45) return 0.0932;
		 if(pt < 50) return 0.0830;
		 if(pt < 60) return 0.0842;
		 if(pt < 80) return 0.0775;
		 if(pt < 100) return 0.0696;
		 if(pt < 200) return 0.0612;
		 if(pt < 3500) return 0.0434;
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
