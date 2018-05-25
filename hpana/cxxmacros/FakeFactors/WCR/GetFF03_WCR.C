#include <iostream>
using namespace std;
float GetFF03_WCR(float pt, int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.434286;
		else if(pt<35.000) return 0.431382;
		else if(pt<37.500) return 0.428547;
		else if(pt<40.000) return 0.427014;
		else if(pt<45.000) return 0.430183;
		else if(pt<50.000) return 0.399608;
		else if(pt<55.000) return 0.395826;
		else if(pt<60.000) return 0.373124;
		else if(pt<70.000) return 0.357909;
		else if(pt<80.000) return 0.318351;
		else if(pt<90.000) return 0.306572;
		else if(pt<100.000) return 0.297152;
		else if(pt<120.000) return 0.279160;
		else if(pt<140.000) return 0.292872;
		else if(pt<160.000) return 0.346861;
		else if(pt<200.000) return 0.370163;
		else return 0.412946;
		}
else if(nTracks==3){
		if(pt<35.000) return 0.081806;
		else if(pt<40.000) return 0.085604;
		else if(pt<45.000) return 0.082902;
		else if(pt<50.000) return 0.077695;
		else if(pt<75.000) return 0.069053;
		else if(pt<100.000) return 0.049456;
		else if(pt<150.000) return 0.033439;
		else return 0.016888;
		}
else return 0;
}

float GetFF03_WCR_up(float pt,int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.438412;
		else if(pt<35.000) return 0.436034;
		else if(pt<37.500) return 0.433757;
		else if(pt<40.000) return 0.432792;
		else if(pt<45.000) return 0.434937;
		else if(pt<50.000) return 0.405119;
		else if(pt<55.000) return 0.402355;
		else if(pt<60.000) return 0.380453;
		else if(pt<70.000) return 0.364140;
		else if(pt<80.000) return 0.325925;
		else if(pt<90.000) return 0.315930;
		else if(pt<100.000) return 0.308645;
		else if(pt<120.000) return 0.289511;
		else if(pt<140.000) return 0.308096;
		else if(pt<160.000) return 0.370118;
		else if(pt<200.000) return 0.396089;
		else return 0.445095;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.082792;
		else if(pt<40.000) return 0.086822;
		else if(pt<45.000) return 0.084341;
		else if(pt<50.000) return 0.079342;
		else if(pt<75.000) return 0.070092;
		else if(pt<100.000) return 0.051101;
		else if(pt<150.000) return 0.035337;
		else return 0.019136;
	}
else return 0;
}

float GetFF03_WCR_dn(float pt,int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.430161;
		else if(pt<35.000) return 0.426729;
		else if(pt<37.500) return 0.423336;
		else if(pt<40.000) return 0.421236;
		else if(pt<45.000) return 0.425429;
		else if(pt<50.000) return 0.394097;
		else if(pt<55.000) return 0.389298;
		else if(pt<60.000) return 0.365795;
		else if(pt<70.000) return 0.351678;
		else if(pt<80.000) return 0.310777;
		else if(pt<90.000) return 0.297213;
		else if(pt<100.000) return 0.285660;
		else if(pt<120.000) return 0.268809;
		else if(pt<140.000) return 0.277649;
		else if(pt<160.000) return 0.323604;
		else if(pt<200.000) return 0.344237;
		else return 0.380798;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.080821;
		else if(pt<40.000) return 0.084386;
		else if(pt<45.000) return 0.081463;
		else if(pt<50.000) return 0.076047;
		else if(pt<75.000) return 0.068013;
		else if(pt<100.000) return 0.047811;
		else if(pt<150.000) return 0.031540;
		else return 0.014640;
	}
else return 0;
}

