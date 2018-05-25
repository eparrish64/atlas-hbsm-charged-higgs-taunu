#include <iostream>
using namespace std;
float GetFF03_WCR_4D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 1.059745;
		else if(pt<40.000) return 1.078093;
		else if(pt<45.000) return 1.282633;
		else if(pt<50.000) return 1.308696;
		else if(pt<60.000) return 1.210258;
		else if(pt<70.000) return 1.085615;
		else if(pt<80.000) return 1.049179;
		else if(pt<90.000) return 1.007424;
		else if(pt<120.000) return 1.052886;
		else if(pt<160.000) return 1.126873;
		else if(pt<200.000) return 1.427794;
		else return 1.288220;
		}
else if(pantau==1){
		if(pt<35.000) return 0.428613;
		else if(pt<40.000) return 0.432178;
		else if(pt<60.000) return 0.405946;
		else if(pt<90.000) return 0.347528;
		else if(pt<110.000) return 0.258228;
		else if(pt<160.000) return 0.262171;
		else if(pt<300.000) return 0.415212;
		else return 0.460812;
		}
else if(pantau==2){
		if(pt<35.000) return 0.248161;
		else if(pt<40.000) return 0.262526;
		else if(pt<50.000) return 0.254331;
		else if(pt<80.000) return 0.226717;
		else if(pt<130.000) return 0.218649;
		else if(pt<230.000) return 0.298082;
		else return 0.214677;
		}
else if(pantau>=3){
		if(pt<35.000) return 0.081806;
		else if(pt<40.000) return 0.085604;
		else if(pt<45.000) return 0.082902;
		else if(pt<50.000) return 0.077695;
		else if(pt<75.000) return 0.069053;
		else if(pt<100.000) return 0.049456;
		else if(pt<150.000) return 0.033439;
		else return 0.016888;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_WCR_4D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 1.074315;
		else if(pt<40.000) return 1.097896;
		else if(pt<45.000) return 1.311030;
		else if(pt<50.000) return 1.345181;
		else if(pt<60.000) return 1.242060;
		else if(pt<70.000) return 1.127135;
		else if(pt<80.000) return 1.102819;
		else if(pt<90.000) return 1.073077;
		else if(pt<120.000) return 1.114112;
		else if(pt<160.000) return 1.234569;
		else if(pt<200.000) return 1.657593;
		else return 1.559042;
	}
else if(pantau==1){
		if(pt<35.000) return 0.432831;
		else if(pt<40.000) return 0.437613;
		else if(pt<60.000) return 0.410030;
		else if(pt<90.000) return 0.353769;
		else if(pt<110.000) return 0.269857;
		else if(pt<160.000) return 0.275733;
		else if(pt<300.000) return 0.448978;
		else return 0.588540;
	}
else if(pantau==2){
		if(pt<35.000) return 0.252056;
		else if(pt<40.000) return 0.267369;
		else if(pt<50.000) return 0.258687;
		else if(pt<80.000) return 0.230819;
		else if(pt<130.000) return 0.226003;
		else if(pt<230.000) return 0.315889;
		else return 0.253179;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.082792;
		else if(pt<40.000) return 0.086822;
		else if(pt<45.000) return 0.084341;
		else if(pt<50.000) return 0.079342;
		else if(pt<75.000) return 0.070092;
		else if(pt<100.000) return 0.051101;
		else if(pt<150.000) return 0.035337;
		else return 0.019136;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_WCR_4D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 1.045176;
		else if(pt<40.000) return 1.058291;
		else if(pt<45.000) return 1.254237;
		else if(pt<50.000) return 1.272211;
		else if(pt<60.000) return 1.178456;
		else if(pt<70.000) return 1.044095;
		else if(pt<80.000) return 0.995539;
		else if(pt<90.000) return 0.941771;
		else if(pt<120.000) return 0.991660;
		else if(pt<160.000) return 1.019178;
		else if(pt<200.000) return 1.197996;
		else return 1.017399;
	}
else if(pantau==1){
		if(pt<35.000) return 0.424396;
		else if(pt<40.000) return 0.426744;
		else if(pt<60.000) return 0.401861;
		else if(pt<90.000) return 0.341288;
		else if(pt<110.000) return 0.246599;
		else if(pt<160.000) return 0.248608;
		else if(pt<300.000) return 0.381446;
		else return 0.333085;
	}
else if(pantau==2){
		if(pt<35.000) return 0.244265;
		else if(pt<40.000) return 0.257683;
		else if(pt<50.000) return 0.249975;
		else if(pt<80.000) return 0.222615;
		else if(pt<130.000) return 0.211294;
		else if(pt<230.000) return 0.280274;
		else return 0.176175;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.080821;
		else if(pt<40.000) return 0.084386;
		else if(pt<45.000) return 0.081463;
		else if(pt<50.000) return 0.076047;
		else if(pt<75.000) return 0.068013;
		else if(pt<100.000) return 0.047811;
		else if(pt<150.000) return 0.031540;
		else return 0.014640;
	}
else {cout << "something wrong" << endl; return 0;}
}

