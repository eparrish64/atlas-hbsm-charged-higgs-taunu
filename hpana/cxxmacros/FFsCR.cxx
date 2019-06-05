#include <iostream>
//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.271710;
		 if(pt < 40) return 0.255603;
		 if(pt < 45) return 0.240494;
		 if(pt < 50) return 0.223931;
		 if(pt < 60) return 0.209852;
		 if(pt < 80) return 0.187200;
		 if(pt < 100) return 0.161778;
		 if(pt < 200) return 0.149822;
		 if(pt < 3500) return 0.121962;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.059799;
		 if(pt < 40) return 0.060890;
		 if(pt < 60) return 0.049123;
		 if(pt < 80) return 0.035100;
		 if(pt < 100) return 0.025614;
		 if(pt < 3500) return 0.023420;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2950;
		 if(pt < 40) return 0.2857;
		 if(pt < 45) return 0.2698;
		 if(pt < 50) return 0.2532;
		 if(pt < 60) return 0.2340;
		 if(pt < 80) return 0.2083;
		 if(pt < 100) return 0.1860;
		 if(pt < 200) return 0.1721;
		 if(pt < 3500) return 0.1332;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0635;
		 if(pt < 40) return 0.0640;
		 if(pt < 60) return 0.0538;
		 if(pt < 80) return 0.0424;
		 if(pt < 100) return 0.0348;
		 if(pt < 3500) return 0.0319;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2468;
		 if(pt < 40) return 0.2232;
		 if(pt < 45) return 0.2089;
		 if(pt < 50) return 0.1924;
		 if(pt < 60) return 0.1840;
		 if(pt < 80) return 0.1643;
		 if(pt < 100) return 0.1355;
		 if(pt < 200) return 0.1256;
		 if(pt < 3500) return 0.1098;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0559;
		 if(pt < 40) return 0.0576;
		 if(pt < 60) return 0.0442;
		 if(pt < 80) return 0.0273;
		 if(pt < 100) return 0.0157;
		 if(pt < 3500) return 0.0143;
		 else return 0;
		 }
	 else return 0;
}


//! BDT_1up 
float GetFF_FF_CR_WJETS_BDT_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.200352;
		 if(pt < 40) return 0.188572;
		 if(pt < 45) return 0.175258;
		 if(pt < 50) return 0.161998;
		 if(pt < 60) return 0.150173;
		 if(pt < 80) return 0.130993;
		 if(pt < 100) return 0.110822;
		 if(pt < 200) return 0.101765;
		 if(pt < 3500) return 0.079363;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.041330;
		 if(pt < 40) return 0.041263;
		 if(pt < 60) return 0.032387;
		 if(pt < 80) return 0.022425;
		 if(pt < 100) return 0.015741;
		 if(pt < 3500) return 0.014212;
		 else return 0;
		 }
	 else return 0;
}


//! BDT_1down 
float GetFF_FF_CR_WJETS_BDT_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.346212;
		 if(pt < 40) return 0.325141;
		 if(pt < 45) return 0.307120;
		 if(pt < 50) return 0.288507;
		 if(pt < 60) return 0.269216;
		 if(pt < 80) return 0.243722;
		 if(pt < 100) return 0.213385;
		 if(pt < 200) return 0.198444;
		 if(pt < 3500) return 0.165405;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.077773;
		 if(pt < 40) return 0.079631;
		 if(pt < 60) return 0.065301;
		 if(pt < 80) return 0.047932;
		 if(pt < 100) return 0.036005;
		 if(pt < 3500) return 0.033346;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.199706;
		 if(pt < 40) return 0.180186;
		 if(pt < 45) return 0.148747;
		 if(pt < 50) return 0.137886;
		 if(pt < 60) return 0.142020;
		 if(pt < 80) return 0.139943;
		 if(pt < 100) return 0.130752;
		 if(pt < 200) return 0.121028;
		 if(pt < 3500) return 0.087774;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.049451;
		 if(pt < 40) return 0.047649;
		 if(pt < 60) return 0.030590;
		 if(pt < 80) return 0.027942;
		 if(pt < 100) return 0.023095;
		 if(pt < 3500) return 0.019830;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.2006;
		 if(pt < 40) return 0.1812;
		 if(pt < 45) return 0.1500;
		 if(pt < 50) return 0.1393;
		 if(pt < 60) return 0.1434;
		 if(pt < 80) return 0.1420;
		 if(pt < 100) return 0.1337;
		 if(pt < 200) return 0.1237;
		 if(pt < 3500) return 0.0892;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0498;
		 if(pt < 40) return 0.0482;
		 if(pt < 60) return 0.0314;
		 if(pt < 80) return 0.0291;
		 if(pt < 100) return 0.0247;
		 if(pt < 3500) return 0.0212;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1988;
		 if(pt < 40) return 0.1792;
		 if(pt < 45) return 0.1474;
		 if(pt < 50) return 0.1364;
		 if(pt < 60) return 0.1406;
		 if(pt < 80) return 0.1378;
		 if(pt < 100) return 0.1278;
		 if(pt < 200) return 0.1184;
		 if(pt < 3500) return 0.0863;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0491;
		 if(pt < 40) return 0.0471;
		 if(pt < 60) return 0.0298;
		 if(pt < 80) return 0.0268;
		 if(pt < 100) return 0.0214;
		 if(pt < 3500) return 0.0185;
		 else return 0;
		 }
	 else return 0;
}


//! BDT_1up 
float GetFF_FF_CR_MULTIJET_BDT_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.139907;
		 if(pt < 40) return 0.124334;
		 if(pt < 45) return 0.100640;
		 if(pt < 50) return 0.093103;
		 if(pt < 60) return 0.096371;
		 if(pt < 80) return 0.093643;
		 if(pt < 100) return 0.087138;
		 if(pt < 200) return 0.078988;
		 if(pt < 3500) return 0.055122;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.031706;
		 if(pt < 40) return 0.029711;
		 if(pt < 60) return 0.018112;
		 if(pt < 80) return 0.016749;
		 if(pt < 100) return 0.013512;
		 if(pt < 3500) return 0.011779;
		 else return 0;
		 }
	 else return 0;
}


//! BDT_1down 
float GetFF_FF_CR_MULTIJET_BDT_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.262407;
		 if(pt < 40) return 0.238483;
		 if(pt < 45) return 0.199837;
		 if(pt < 50) return 0.185321;
		 if(pt < 60) return 0.189110;
		 if(pt < 80) return 0.186606;
		 if(pt < 100) return 0.176523;
		 if(pt < 200) return 0.163280;
		 if(pt < 3500) return 0.120493;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.066338;
		 if(pt < 40) return 0.064966;
		 if(pt < 60) return 0.043005;
		 if(pt < 80) return 0.039363;
		 if(pt < 100) return 0.033049;
		 if(pt < 3500) return 0.028451;
		 else return 0;
		 }
	 else return 0;
}


