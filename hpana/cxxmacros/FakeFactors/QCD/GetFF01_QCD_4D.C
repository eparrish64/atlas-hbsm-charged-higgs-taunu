#include <iostream>
using namespace std;
float GetFF01_QCD_4D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.545946;
		else if(pt<40.000) return 0.581447;
		else if(pt<45.000) return 0.629674;
		else if(pt<50.000) return 0.633418;
		else if(pt<60.000) return 0.564316;
		else if(pt<70.000) return 0.486740;
		else if(pt<80.000) return 0.436602;
		else if(pt<90.000) return 0.494896;
		else if(pt<120.000) return 0.596748;
		else if(pt<160.000) return 0.698175;
		else if(pt<200.000) return 0.859849;
		else return 1.000612;
		}
else if(pantau==1){
		if(pt<35.000) return 0.194000;
		else if(pt<40.000) return 0.197048;
		else if(pt<60.000) return 0.174640;
		else if(pt<90.000) return 0.123744;
		else if(pt<110.000) return 0.130157;
		else if(pt<160.000) return 0.139074;
		else if(pt<300.000) return 0.172589;
		else return 0.239852;
		}
else if(pantau==2){
		if(pt<35.000) return 0.098717;
		else if(pt<40.000) return 0.101314;
		else if(pt<50.000) return 0.101844;
		else if(pt<80.000) return 0.083867;
		else if(pt<130.000) return 0.093159;
		else if(pt<230.000) return 0.119061;
		else return 0.150506;
		}
else if(pantau>=3){
		if(pt<35.000) return 0.032251;
		else if(pt<40.000) return 0.031805;
		else if(pt<50.000) return 0.030625;
		else if(pt<75.000) return 0.020356;
		else if(pt<100.000) return 0.013245;
		else if(pt<150.000) return 0.012565;
		else if(pt<200.000) return 0.011997;
		else return 0.011194;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_QCD_4D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.556952;
		else if(pt<40.000) return 0.595729;
		else if(pt<45.000) return 0.647876;
		else if(pt<50.000) return 0.655328;
		else if(pt<60.000) return 0.581987;
		else if(pt<70.000) return 0.504898;
		else if(pt<80.000) return 0.453340;
		else if(pt<90.000) return 0.513069;
		else if(pt<120.000) return 0.610196;
		else if(pt<160.000) return 0.717889;
		else if(pt<200.000) return 0.895389;
		else return 1.034384;
	}
else if(pantau==1){
		if(pt<35.000) return 0.196633;
		else if(pt<40.000) return 0.200297;
		else if(pt<60.000) return 0.176715;
		else if(pt<90.000) return 0.125214;
		else if(pt<110.000) return 0.132206;
		else if(pt<160.000) return 0.141021;
		else if(pt<300.000) return 0.175478;
		else return 0.247388;
	}
else if(pantau==2){
		if(pt<35.000) return 0.100734;
		else if(pt<40.000) return 0.103652;
		else if(pt<50.000) return 0.103839;
		else if(pt<80.000) return 0.085055;
		else if(pt<130.000) return 0.094262;
		else if(pt<230.000) return 0.120856;
		else return 0.154062;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.032871;
		else if(pt<40.000) return 0.032509;
		else if(pt<50.000) return 0.031216;
		else if(pt<75.000) return 0.020748;
		else if(pt<100.000) return 0.013518;
		else if(pt<150.000) return 0.012804;
		else if(pt<200.000) return 0.012362;
		else return 0.011512;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_QCD_4D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.534939;
		else if(pt<40.000) return 0.567164;
		else if(pt<45.000) return 0.611471;
		else if(pt<50.000) return 0.611509;
		else if(pt<60.000) return 0.546644;
		else if(pt<70.000) return 0.468582;
		else if(pt<80.000) return 0.419864;
		else if(pt<90.000) return 0.476723;
		else if(pt<120.000) return 0.583300;
		else if(pt<160.000) return 0.678462;
		else if(pt<200.000) return 0.824310;
		else return 0.966841;
	}
else if(pantau==1){
		if(pt<35.000) return 0.191367;
		else if(pt<40.000) return 0.193798;
		else if(pt<60.000) return 0.172566;
		else if(pt<90.000) return 0.122274;
		else if(pt<110.000) return 0.128108;
		else if(pt<160.000) return 0.137128;
		else if(pt<300.000) return 0.169701;
		else return 0.232317;
	}
else if(pantau==2){
		if(pt<35.000) return 0.096700;
		else if(pt<40.000) return 0.098976;
		else if(pt<50.000) return 0.099849;
		else if(pt<80.000) return 0.082679;
		else if(pt<130.000) return 0.092055;
		else if(pt<230.000) return 0.117265;
		else return 0.146950;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.031631;
		else if(pt<40.000) return 0.031102;
		else if(pt<50.000) return 0.030033;
		else if(pt<75.000) return 0.019965;
		else if(pt<100.000) return 0.012972;
		else if(pt<150.000) return 0.012326;
		else if(pt<200.000) return 0.011632;
		else return 0.010875;
	}
else {cout << "something wrong" << endl; return 0;}
}

