#include <iostream>
using namespace std;
float GetFF01_WCR_4D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.837454;
		else if(pt<40.000) return 0.871468;
		else if(pt<45.000) return 1.038778;
		else if(pt<50.000) return 1.058182;
		else if(pt<60.000) return 0.989446;
		else if(pt<70.000) return 0.863793;
		else if(pt<80.000) return 0.857933;
		else if(pt<90.000) return 0.806674;
		else if(pt<120.000) return 0.826456;
		else if(pt<160.000) return 0.936373;
		else if(pt<200.000) return 1.102341;
		else return 0.923539;
		}
else if(pantau==1){
		if(pt<35.000) return 0.257865;
		else if(pt<40.000) return 0.266213;
		else if(pt<60.000) return 0.250153;
		else if(pt<90.000) return 0.198735;
		else if(pt<110.000) return 0.143009;
		else if(pt<160.000) return 0.142071;
		else if(pt<300.000) return 0.210590;
		else return 0.240715;
		}
else if(pantau==2){
		if(pt<35.000) return 0.126942;
		else if(pt<40.000) return 0.136579;
		else if(pt<50.000) return 0.130746;
		else if(pt<80.000) return 0.111679;
		else if(pt<130.000) return 0.102126;
		else if(pt<230.000) return 0.134722;
		else return 0.108892;
		}
else if(pantau>=3){
		if(pt<35.000) return 0.045453;
		else if(pt<40.000) return 0.046521;
		else if(pt<45.000) return 0.044043;
		else if(pt<50.000) return 0.040500;
		else if(pt<75.000) return 0.034051;
		else if(pt<100.000) return 0.021987;
		else if(pt<150.000) return 0.013890;
		else return 0.006868;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_WCR_4D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.848967;
		else if(pt<40.000) return 0.887476;
		else if(pt<45.000) return 1.061776;
		else if(pt<50.000) return 1.087683;
		else if(pt<60.000) return 1.015445;
		else if(pt<70.000) return 0.896829;
		else if(pt<80.000) return 0.901795;
		else if(pt<90.000) return 0.859244;
		else if(pt<120.000) return 0.874514;
		else if(pt<160.000) return 1.025862;
		else if(pt<200.000) return 1.279758;
		else return 1.117693;
	}
else if(pantau==1){
		if(pt<35.000) return 0.260402;
		else if(pt<40.000) return 0.269561;
		else if(pt<60.000) return 0.252670;
		else if(pt<90.000) return 0.202303;
		else if(pt<110.000) return 0.149449;
		else if(pt<160.000) return 0.149421;
		else if(pt<300.000) return 0.227715;
		else return 0.307436;
	}
else if(pantau==2){
		if(pt<35.000) return 0.128935;
		else if(pt<40.000) return 0.139098;
		else if(pt<50.000) return 0.132985;
		else if(pt<80.000) return 0.113700;
		else if(pt<130.000) return 0.105561;
		else if(pt<230.000) return 0.142771;
		else return 0.128421;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.046001;
		else if(pt<40.000) return 0.047183;
		else if(pt<45.000) return 0.044807;
		else if(pt<50.000) return 0.041359;
		else if(pt<75.000) return 0.034564;
		else if(pt<100.000) return 0.022719;
		else if(pt<150.000) return 0.014678;
		else return 0.007782;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_WCR_4D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.825941;
		else if(pt<40.000) return 0.855461;
		else if(pt<45.000) return 1.015780;
		else if(pt<50.000) return 1.028681;
		else if(pt<60.000) return 0.963446;
		else if(pt<70.000) return 0.830756;
		else if(pt<80.000) return 0.814070;
		else if(pt<90.000) return 0.754103;
		else if(pt<120.000) return 0.778397;
		else if(pt<160.000) return 0.846884;
		else if(pt<200.000) return 0.924923;
		else return 0.729384;
	}
else if(pantau==1){
		if(pt<35.000) return 0.255327;
		else if(pt<40.000) return 0.262865;
		else if(pt<60.000) return 0.247636;
		else if(pt<90.000) return 0.195166;
		else if(pt<110.000) return 0.136568;
		else if(pt<160.000) return 0.134722;
		else if(pt<300.000) return 0.193464;
		else return 0.173994;
	}
else if(pantau==2){
		if(pt<35.000) return 0.124949;
		else if(pt<40.000) return 0.134060;
		else if(pt<50.000) return 0.128506;
		else if(pt<80.000) return 0.109658;
		else if(pt<130.000) return 0.098691;
		else if(pt<230.000) return 0.126674;
		else return 0.089362;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.044906;
		else if(pt<40.000) return 0.045859;
		else if(pt<45.000) return 0.043279;
		else if(pt<50.000) return 0.039641;
		else if(pt<75.000) return 0.033538;
		else if(pt<100.000) return 0.021256;
		else if(pt<150.000) return 0.013101;
		else return 0.005954;
	}
else {cout << "something wrong" << endl; return 0;}
}

