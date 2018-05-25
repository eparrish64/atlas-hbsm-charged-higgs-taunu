#include <iostream>
using namespace std;
float GetFF02_WCR_4D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.939114;
		else if(pt<40.000) return 0.971117;
		else if(pt<45.000) return 1.139434;
		else if(pt<50.000) return 1.179436;
		else if(pt<60.000) return 1.080764;
		else if(pt<70.000) return 0.957891;
		else if(pt<80.000) return 0.950233;
		else if(pt<90.000) return 0.909204;
		else if(pt<120.000) return 0.954481;
		else if(pt<160.000) return 1.012094;
		else if(pt<200.000) return 1.205619;
		else return 1.156528;
		}
else if(pantau==1){
		if(pt<35.000) return 0.340920;
		else if(pt<40.000) return 0.347649;
		else if(pt<60.000) return 0.325441;
		else if(pt<90.000) return 0.268475;
		else if(pt<110.000) return 0.195743;
		else if(pt<160.000) return 0.206370;
		else if(pt<300.000) return 0.334375;
		else return 0.301272;
		}
else if(pantau==2){
		if(pt<35.000) return 0.184111;
		else if(pt<40.000) return 0.196620;
		else if(pt<50.000) return 0.189698;
		else if(pt<80.000) return 0.165369;
		else if(pt<130.000) return 0.159244;
		else if(pt<230.000) return 0.214325;
		else return 0.160536;
		}
else if(pantau>=3){
		if(pt<35.000) return 0.064341;
		else if(pt<40.000) return 0.066540;
		else if(pt<45.000) return 0.063789;
		else if(pt<50.000) return 0.059118;
		else if(pt<75.000) return 0.051374;
		else if(pt<100.000) return 0.036012;
		else if(pt<150.000) return 0.023536;
		else return 0.011292;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_WCR_4D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.952025;
		else if(pt<40.000) return 0.988955;
		else if(pt<45.000) return 1.164660;
		else if(pt<50.000) return 1.212317;
		else if(pt<60.000) return 1.109163;
		else if(pt<70.000) return 0.994526;
		else if(pt<80.000) return 0.998814;
		else if(pt<90.000) return 0.968456;
		else if(pt<120.000) return 1.009985;
		else if(pt<160.000) return 1.108820;
		else if(pt<200.000) return 1.399658;
		else return 1.399663;
	}
else if(pantau==1){
		if(pt<35.000) return 0.344274;
		else if(pt<40.000) return 0.352020;
		else if(pt<60.000) return 0.328715;
		else if(pt<90.000) return 0.273296;
		else if(pt<110.000) return 0.204558;
		else if(pt<160.000) return 0.217045;
		else if(pt<300.000) return 0.361567;
		else return 0.384778;
	}
else if(pantau==2){
		if(pt<35.000) return 0.187001;
		else if(pt<40.000) return 0.200247;
		else if(pt<50.000) return 0.192948;
		else if(pt<80.000) return 0.168361;
		else if(pt<130.000) return 0.164600;
		else if(pt<230.000) return 0.227129;
		else return 0.189328;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.065116;
		else if(pt<40.000) return 0.067486;
		else if(pt<45.000) return 0.064896;
		else if(pt<50.000) return 0.060372;
		else if(pt<75.000) return 0.052147;
		else if(pt<100.000) return 0.037210;
		else if(pt<150.000) return 0.024872;
		else return 0.012794;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_WCR_4D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.926203;
		else if(pt<40.000) return 0.953279;
		else if(pt<45.000) return 1.114208;
		else if(pt<50.000) return 1.146555;
		else if(pt<60.000) return 1.052364;
		else if(pt<70.000) return 0.921256;
		else if(pt<80.000) return 0.901651;
		else if(pt<90.000) return 0.849952;
		else if(pt<120.000) return 0.898978;
		else if(pt<160.000) return 0.915368;
		else if(pt<200.000) return 1.011579;
		else return 0.913392;
	}
else if(pantau==1){
		if(pt<35.000) return 0.337565;
		else if(pt<40.000) return 0.343277;
		else if(pt<60.000) return 0.322166;
		else if(pt<90.000) return 0.263654;
		else if(pt<110.000) return 0.186928;
		else if(pt<160.000) return 0.195694;
		else if(pt<300.000) return 0.307183;
		else return 0.217765;
	}
else if(pantau==2){
		if(pt<35.000) return 0.181221;
		else if(pt<40.000) return 0.192993;
		else if(pt<50.000) return 0.186449;
		else if(pt<80.000) return 0.162376;
		else if(pt<130.000) return 0.153888;
		else if(pt<230.000) return 0.201522;
		else return 0.131744;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.063566;
		else if(pt<40.000) return 0.065593;
		else if(pt<45.000) return 0.062682;
		else if(pt<50.000) return 0.057864;
		else if(pt<75.000) return 0.050600;
		else if(pt<100.000) return 0.034814;
		else if(pt<150.000) return 0.022199;
		else return 0.009789;
	}
else {cout << "something wrong" << endl; return 0;}
}

