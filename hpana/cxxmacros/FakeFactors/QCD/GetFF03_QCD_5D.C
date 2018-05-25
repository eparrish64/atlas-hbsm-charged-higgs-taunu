#include <iostream>
using namespace std;
float GetFF03_QCD_5D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.767346;
		else if(pt<40.000) return 0.794781;
		else if(pt<45.000) return 0.839177;
		else if(pt<50.000) return 0.865899;
		else if(pt<60.000) return 0.772807;
		else if(pt<70.000) return 0.689262;
		else if(pt<80.000) return 0.605535;
		else if(pt<90.000) return 0.672445;
		else if(pt<120.000) return 0.790055;
		else if(pt<160.000) return 0.897057;
		else if(pt<200.000) return 1.107709;
		else return 1.478017;
		}
else if(pantau==1){
		if(pt<35.000) return 0.351533;
		else if(pt<40.000) return 0.350008;
		else if(pt<60.000) return 0.318214;
		else if(pt<90.000) return 0.253286;
		else if(pt<110.000) return 0.255368;
		else if(pt<160.000) return 0.274480;
		else if(pt<300.000) return 0.360959;
		else return 0.529770;
		}
else if(pantau==2){
		if(pt<35.000) return 0.207834;
		else if(pt<40.000) return 0.214339;
		else if(pt<50.000) return 0.218054;
		else if(pt<80.000) return 0.198369;
		else if(pt<130.000) return 0.212908;
		else if(pt<230.000) return 0.263611;
		else return 0.332640;
		}
else if(pantau==3){
		if(pt<35.000) return 0.081619;
		else if(pt<40.000) return 0.084616;
		else if(pt<45.000) return 0.089084;
		else if(pt<50.000) return 0.078119;
		else if(pt<80.000) return 0.064687;
		else if(pt<150.000) return 0.042693;
		else return 0.034728;
		}
else if(pantau==4){
		if(pt<35.000) return 0.042052;
		else if(pt<40.000) return 0.042122;
		else if(pt<45.000) return 0.043694;
		else if(pt<50.000) return 0.039695;
		else if(pt<75.000) return 0.028709;
		else if(pt<100.000) return 0.021646;
		else if(pt<150.000) return 0.021123;
		else return 0.019777;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_QCD_5D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.782776;
		else if(pt<40.000) return 0.814182;
		else if(pt<45.000) return 0.863356;
		else if(pt<50.000) return 0.895689;
		else if(pt<60.000) return 0.796972;
		else if(pt<70.000) return 0.714903;
		else if(pt<80.000) return 0.628598;
		else if(pt<90.000) return 0.696974;
		else if(pt<120.000) return 0.807849;
		else if(pt<160.000) return 0.922427;
		else if(pt<200.000) return 1.153415;
		else return 1.527704;
	}
else if(pantau==1){
		if(pt<35.000) return 0.356277;
		else if(pt<40.000) return 0.355754;
		else if(pt<60.000) return 0.321980;
		else if(pt<90.000) return 0.256290;
		else if(pt<110.000) return 0.259370;
		else if(pt<160.000) return 0.278317;
		else if(pt<300.000) return 0.366997;
		else return 0.546415;
	}
else if(pantau==2){
		if(pt<35.000) return 0.212054;
		else if(pt<40.000) return 0.219265;
		else if(pt<50.000) return 0.222309;
		else if(pt<80.000) return 0.201175;
		else if(pt<130.000) return 0.215426;
		else if(pt<230.000) return 0.267583;
		else return 0.340501;
	}
else if(pantau==3){
		if(pt<35.000) return 0.083544;
		else if(pt<40.000) return 0.086901;
		else if(pt<45.000) return 0.091852;
		else if(pt<50.000) return 0.081040;
		else if(pt<80.000) return 0.066094;
		else if(pt<150.000) return 0.043438;
		else return 0.035545;
	}
else if(pantau==4){
		if(pt<35.000) return 0.043431;
		else if(pt<40.000) return 0.043712;
		else if(pt<45.000) return 0.045533;
		else if(pt<50.000) return 0.041743;
		else if(pt<75.000) return 0.029677;
		else if(pt<100.000) return 0.022415;
		else if(pt<150.000) return 0.021870;
		else return 0.020643;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_QCD_5D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.751917;
		else if(pt<40.000) return 0.775381;
		else if(pt<45.000) return 0.814999;
		else if(pt<50.000) return 0.836109;
		else if(pt<60.000) return 0.748642;
		else if(pt<70.000) return 0.663621;
		else if(pt<80.000) return 0.582473;
		else if(pt<90.000) return 0.647917;
		else if(pt<120.000) return 0.772260;
		else if(pt<160.000) return 0.871687;
		else if(pt<200.000) return 1.062003;
		else return 1.428330;
	}
else if(pantau==1){
		if(pt<35.000) return 0.346790;
		else if(pt<40.000) return 0.344263;
		else if(pt<60.000) return 0.314448;
		else if(pt<90.000) return 0.250281;
		else if(pt<110.000) return 0.251366;
		else if(pt<160.000) return 0.270643;
		else if(pt<300.000) return 0.354922;
		else return 0.513126;
	}
else if(pantau==2){
		if(pt<35.000) return 0.203614;
		else if(pt<40.000) return 0.209413;
		else if(pt<50.000) return 0.213800;
		else if(pt<80.000) return 0.195563;
		else if(pt<130.000) return 0.210389;
		else if(pt<230.000) return 0.259638;
		else return 0.324778;
	}
else if(pantau==3){
		if(pt<35.000) return 0.079694;
		else if(pt<40.000) return 0.082331;
		else if(pt<45.000) return 0.086316;
		else if(pt<50.000) return 0.075199;
		else if(pt<80.000) return 0.063281;
		else if(pt<150.000) return 0.041949;
		else return 0.033910;
	}
else if(pantau==4){
		if(pt<35.000) return 0.040674;
		else if(pt<40.000) return 0.040532;
		else if(pt<45.000) return 0.041855;
		else if(pt<50.000) return 0.037648;
		else if(pt<75.000) return 0.027741;
		else if(pt<100.000) return 0.020878;
		else if(pt<150.000) return 0.020375;
		else return 0.018910;
	}
else {cout << "something wrong" << endl; return 0;}
}

