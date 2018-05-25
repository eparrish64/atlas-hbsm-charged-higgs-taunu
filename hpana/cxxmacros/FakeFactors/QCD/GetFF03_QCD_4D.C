#include <iostream>
using namespace std;
float GetFF03_QCD_4D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.767122;
		else if(pt<40.000) return 0.790069;
		else if(pt<45.000) return 0.839451;
		else if(pt<50.000) return 0.865513;
		else if(pt<60.000) return 0.776409;
		else if(pt<70.000) return 0.690702;
		else if(pt<80.000) return 0.593459;
		else if(pt<90.000) return 0.663501;
		else if(pt<120.000) return 0.791381;
		else if(pt<160.000) return 0.907750;
		else if(pt<200.000) return 1.116570;
		else return 1.481169;
		}
else if(pantau==1){
		if(pt<35.000) return 0.351934;
		else if(pt<40.000) return 0.350973;
		else if(pt<60.000) return 0.318742;
		else if(pt<90.000) return 0.253348;
		else if(pt<110.000) return 0.253351;
		else if(pt<160.000) return 0.274297;
		else if(pt<300.000) return 0.360874;
		else return 0.529777;
		}
else if(pantau==2){
		if(pt<35.000) return 0.207434;
		else if(pt<40.000) return 0.214608;
		else if(pt<50.000) return 0.218533;
		else if(pt<80.000) return 0.198814;
		else if(pt<130.000) return 0.212609;
		else if(pt<230.000) return 0.262840;
		else return 0.333445;
		}
else if(pantau>=3){
		if(pt<35.000) return 0.061653;
		else if(pt<40.000) return 0.062550;
		else if(pt<50.000) return 0.062434;
		else if(pt<75.000) return 0.046918;
		else if(pt<100.000) return 0.033295;
		else if(pt<150.000) return 0.032118;
		else if(pt<200.000) return 0.031154;
		else return 0.028318;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_QCD_4D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.782588;
		else if(pt<40.000) return 0.809476;
		else if(pt<45.000) return 0.863719;
		else if(pt<50.000) return 0.895450;
		else if(pt<60.000) return 0.800722;
		else if(pt<70.000) return 0.716468;
		else if(pt<80.000) return 0.616210;
		else if(pt<90.000) return 0.687865;
		else if(pt<120.000) return 0.809215;
		else if(pt<160.000) return 0.933381;
		else if(pt<200.000) return 1.162720;
		else return 1.531160;
	}
else if(pantau==1){
		if(pt<35.000) return 0.356710;
		else if(pt<40.000) return 0.356761;
		else if(pt<60.000) return 0.322529;
		else if(pt<90.000) return 0.256357;
		else if(pt<110.000) return 0.257340;
		else if(pt<160.000) return 0.278136;
		else if(pt<300.000) return 0.366913;
		else return 0.546421;
	}
else if(pantau==2){
		if(pt<35.000) return 0.211673;
		else if(pt<40.000) return 0.219560;
		else if(pt<50.000) return 0.222813;
		else if(pt<80.000) return 0.201631;
		else if(pt<130.000) return 0.215128;
		else if(pt<230.000) return 0.266803;
		else return 0.341324;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.062838;
		else if(pt<40.000) return 0.063934;
		else if(pt<50.000) return 0.063640;
		else if(pt<75.000) return 0.047821;
		else if(pt<100.000) return 0.033981;
		else if(pt<150.000) return 0.032729;
		else if(pt<200.000) return 0.032101;
		else return 0.029124;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_QCD_4D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.751656;
		else if(pt<40.000) return 0.770662;
		else if(pt<45.000) return 0.815184;
		else if(pt<50.000) return 0.835576;
		else if(pt<60.000) return 0.752096;
		else if(pt<70.000) return 0.664935;
		else if(pt<80.000) return 0.570707;
		else if(pt<90.000) return 0.639136;
		else if(pt<120.000) return 0.773547;
		else if(pt<160.000) return 0.882119;
		else if(pt<200.000) return 1.070420;
		else return 1.431178;
	}
else if(pantau==1){
		if(pt<35.000) return 0.347158;
		else if(pt<40.000) return 0.345185;
		else if(pt<60.000) return 0.314955;
		else if(pt<90.000) return 0.250339;
		else if(pt<110.000) return 0.249362;
		else if(pt<160.000) return 0.270458;
		else if(pt<300.000) return 0.354835;
		else return 0.513132;
	}
else if(pantau==2){
		if(pt<35.000) return 0.203195;
		else if(pt<40.000) return 0.209656;
		else if(pt<50.000) return 0.214253;
		else if(pt<80.000) return 0.195997;
		else if(pt<130.000) return 0.210089;
		else if(pt<230.000) return 0.258877;
		else return 0.325567;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.060468;
		else if(pt<40.000) return 0.061167;
		else if(pt<50.000) return 0.061227;
		else if(pt<75.000) return 0.046016;
		else if(pt<100.000) return 0.032610;
		else if(pt<150.000) return 0.031507;
		else if(pt<200.000) return 0.030207;
		else return 0.027513;
	}
else {cout << "something wrong" << endl; return 0;}
}

