#include <iostream>
using namespace std;
float GetFF02_WCR(float pt, int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.340278;
		else if(pt<35.000) return 0.338344;
		else if(pt<37.500) return 0.336653;
		else if(pt<40.000) return 0.339351;
		else if(pt<45.000) return 0.337990;
		else if(pt<50.000) return 0.311340;
		else if(pt<55.000) return 0.308967;
		else if(pt<60.000) return 0.289013;
		else if(pt<70.000) return 0.271954;
		else if(pt<80.000) return 0.240905;
		else if(pt<90.000) return 0.229554;
		else if(pt<100.000) return 0.221421;
		else if(pt<120.000) return 0.215978;
		else if(pt<140.000) return 0.222802;
		else if(pt<160.000) return 0.258775;
		else if(pt<200.000) return 0.278636;
		else return 0.316070;
		}
else if(nTracks==3){
		if(pt<35.000) return 0.064341;
		else if(pt<40.000) return 0.066540;
		else if(pt<45.000) return 0.063789;
		else if(pt<50.000) return 0.059118;
		else if(pt<75.000) return 0.051374;
		else if(pt<100.000) return 0.036012;
		else if(pt<150.000) return 0.023536;
		else return 0.011292;
		}
 else 
   return 0;
}

float GetFF02_WCR_up(float pt,int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.343510;
		else if(pt<35.000) return 0.341993;
		else if(pt<37.500) return 0.340746;
		else if(pt<40.000) return 0.343942;
		else if(pt<45.000) return 0.341725;
		else if(pt<50.000) return 0.315633;
		else if(pt<55.000) return 0.314063;
		else if(pt<60.000) return 0.294690;
		else if(pt<70.000) return 0.276688;
		else if(pt<80.000) return 0.246637;
		else if(pt<90.000) return 0.236561;
		else if(pt<100.000) return 0.229985;
		else if(pt<120.000) return 0.223987;
		else if(pt<140.000) return 0.234383;
		else if(pt<160.000) return 0.276126;
		else if(pt<200.000) return 0.298152;
		else return 0.340676;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.065116;
		else if(pt<40.000) return 0.067486;
		else if(pt<45.000) return 0.064896;
		else if(pt<50.000) return 0.060372;
		else if(pt<75.000) return 0.052147;
		else if(pt<100.000) return 0.037210;
		else if(pt<150.000) return 0.024872;
		else return 0.012794;
	}
 else return 0;
}

float GetFF02_WCR_dn(float pt,int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.337045;
		else if(pt<35.000) return 0.334695;
		else if(pt<37.500) return 0.332560;
		else if(pt<40.000) return 0.334759;
		else if(pt<45.000) return 0.334255;
		else if(pt<50.000) return 0.307046;
		else if(pt<55.000) return 0.303871;
		else if(pt<60.000) return 0.283336;
		else if(pt<70.000) return 0.267219;
		else if(pt<80.000) return 0.235174;
		else if(pt<90.000) return 0.222546;
		else if(pt<100.000) return 0.212858;
		else if(pt<120.000) return 0.207970;
		else if(pt<140.000) return 0.211220;
		else if(pt<160.000) return 0.241424;
		else if(pt<200.000) return 0.259121;
		else return 0.291463;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.063566;
		else if(pt<40.000) return 0.065593;
		else if(pt<45.000) return 0.062682;
		else if(pt<50.000) return 0.057864;
		else if(pt<75.000) return 0.050600;
		else if(pt<100.000) return 0.034814;
		else if(pt<150.000) return 0.022199;
		else return 0.009789;
 }
 else 
   return 0;
}

