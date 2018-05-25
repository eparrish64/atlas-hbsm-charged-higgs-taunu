#include <iostream>
using namespace std;
float GetFF01_QCD(float pt, int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.181221;
		else if(pt<40.000) return 0.180095;
		else if(pt<45.000) return 0.171858;
		else if(pt<50.000) return 0.174737;
		else if(pt<60.000) return 0.144458;
		else if(pt<75.000) return 0.115262;
		else if(pt<90.000) return 0.115130;
		else if(pt<105.000) return 0.127680;
		else if(pt<120.000) return 0.132077;
		else if(pt<140.000) return 0.140327;
		else if(pt<160.000) return 0.148054;
		else if(pt<200.000) return 0.161153;
		else if(pt<300.000) return 0.185393;
		else return 0.213226;
		}
else if(nTracks==3){
		if(pt<35.000) return 0.032251;
		else if(pt<40.000) return 0.031805;
		else if(pt<50.000) return 0.030625;
		else if(pt<75.000) return 0.020356;
		else if(pt<100.000) return 0.013245;
		else if(pt<150.000) return 0.012565;
		else if(pt<200.000) return 0.011997;
		else return 0.011194;
		}
else return 0;
}

float GetFF01_QCD_up(float pt,int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.183008;
		else if(pt<40.000) return 0.182215;
		else if(pt<45.000) return 0.174249;
		else if(pt<50.000) return 0.177496;
		else if(pt<60.000) return 0.146444;
		else if(pt<75.000) return 0.116678;
		else if(pt<90.000) return 0.116430;
		else if(pt<105.000) return 0.129240;
		else if(pt<120.000) return 0.133958;
		else if(pt<140.000) return 0.142378;
		else if(pt<160.000) return 0.150655;
		else if(pt<200.000) return 0.163699;
		else if(pt<300.000) return 0.188321;
		else return 0.217800;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.032871;
		else if(pt<40.000) return 0.032509;
		else if(pt<50.000) return 0.031216;
		else if(pt<75.000) return 0.020748;
		else if(pt<100.000) return 0.013518;
		else if(pt<150.000) return 0.012804;
		else if(pt<200.000) return 0.012362;
		else return 0.011512;
	}
else return 0;
}

float GetFF01_QCD_dn(float pt,int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.179434;
		else if(pt<40.000) return 0.177974;
		else if(pt<45.000) return 0.169467;
		else if(pt<50.000) return 0.171979;
		else if(pt<60.000) return 0.142472;
		else if(pt<75.000) return 0.113846;
		else if(pt<90.000) return 0.113831;
		else if(pt<105.000) return 0.126120;
		else if(pt<120.000) return 0.130195;
		else if(pt<140.000) return 0.138275;
		else if(pt<160.000) return 0.145452;
		else if(pt<200.000) return 0.158607;
		else if(pt<300.000) return 0.182466;
		else return 0.208651;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.031631;
		else if(pt<40.000) return 0.031102;
		else if(pt<50.000) return 0.030033;
		else if(pt<75.000) return 0.019965;
		else if(pt<100.000) return 0.012972;
		else if(pt<150.000) return 0.012326;
		else if(pt<200.000) return 0.011632;
		else return 0.010875;
	}
 else return 0;
}

