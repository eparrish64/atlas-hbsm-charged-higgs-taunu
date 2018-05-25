#include <iostream>
using namespace std;
float GetFF02_WCR_5D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.940433;
		else if(pt<40.000) return 0.979369;
		else if(pt<45.000) return 1.145395;
		else if(pt<50.000) return 1.185276;
		else if(pt<60.000) return 1.080727;
		else if(pt<70.000) return 0.958415;
		else if(pt<80.000) return 0.947878;
		else if(pt<90.000) return 0.898792;
		else if(pt<120.000) return 0.964048;
		else if(pt<160.000) return 1.058858;
		else if(pt<200.000) return 1.134743;
		else return 1.156528;
		}
else if(pantau==1){
		if(pt<35.000) return 0.341619;
		else if(pt<40.000) return 0.349264;
		else if(pt<60.000) return 0.325632;
		else if(pt<90.000) return 0.269757;
		else if(pt<110.000) return 0.197824;
		else if(pt<160.000) return 0.203014;
		else if(pt<300.000) return 0.337988;
		else return 0.294456;
		}
else if(pantau==2){
		if(pt<35.000) return 0.183690;
		else if(pt<40.000) return 0.197084;
		else if(pt<50.000) return 0.190280;
		else if(pt<80.000) return 0.165108;
		else if(pt<130.000) return 0.158877;
		else if(pt<230.000) return 0.217053;
		else return 0.160536;
		}
else if(pantau==3){
		if(pt<35.000) return 0.084625;
		else if(pt<40.000) return 0.089638;
		else if(pt<45.000) return 0.084736;
		else if(pt<50.000) return 0.078703;
		else if(pt<80.000) return 0.067991;
		else if(pt<150.000) return 0.038023;
		else return 0.013404;
		}
else if(pantau==4){
		if(pt<35.000) return 0.043160;
		else if(pt<40.000) return 0.043382;
		else if(pt<45.000) return 0.043447;
		else if(pt<50.000) return 0.040179;
		else if(pt<75.000) return 0.032951;
		else if(pt<100.000) return 0.023877;
		else if(pt<150.000) return 0.015404;
		else return 0.010270;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_WCR_5D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.953325;
		else if(pt<40.000) return 0.997257;
		else if(pt<45.000) return 1.170575;
		else if(pt<50.000) return 1.218269;
		else if(pt<60.000) return 1.108989;
		else if(pt<70.000) return 0.994832;
		else if(pt<80.000) return 0.996339;
		else if(pt<90.000) return 0.957366;
		else if(pt<120.000) return 1.019919;
		else if(pt<160.000) return 1.158254;
		else if(pt<200.000) return 1.317375;
		else return 1.399663;
	}
else if(pantau==1){
		if(pt<35.000) return 0.344968;
		else if(pt<40.000) return 0.353633;
		else if(pt<60.000) return 0.328899;
		else if(pt<90.000) return 0.274571;
		else if(pt<110.000) return 0.206653;
		else if(pt<160.000) return 0.213531;
		else if(pt<300.000) return 0.365117;
		else return 0.376073;
	}
else if(pantau==2){
		if(pt<35.000) return 0.186566;
		else if(pt<40.000) return 0.200702;
		else if(pt<50.000) return 0.193521;
		else if(pt<80.000) return 0.168088;
		else if(pt<130.000) return 0.164209;
		else if(pt<230.000) return 0.229928;
		else return 0.189328;
	}
else if(pantau==3){
		if(pt<35.000) return 0.085855;
		else if(pt<40.000) return 0.091176;
		else if(pt<45.000) return 0.086541;
		else if(pt<50.000) return 0.080742;
		else if(pt<80.000) return 0.069190;
		else if(pt<150.000) return 0.039520;
		else return 0.015464;
	}
else if(pantau==4){
		if(pt<35.000) return 0.044072;
		else if(pt<40.000) return 0.044466;
		else if(pt<45.000) return 0.044727;
		else if(pt<50.000) return 0.041635;
		else if(pt<75.000) return 0.033827;
		else if(pt<100.000) return 0.025287;
		else if(pt<150.000) return 0.017037;
		else return 0.012617;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_WCR_5D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.927540;
		else if(pt<40.000) return 0.961482;
		else if(pt<45.000) return 1.120215;
		else if(pt<50.000) return 1.152283;
		else if(pt<60.000) return 1.052465;
		else if(pt<70.000) return 0.921999;
		else if(pt<80.000) return 0.899417;
		else if(pt<90.000) return 0.840218;
		else if(pt<120.000) return 0.908177;
		else if(pt<160.000) return 0.959462;
		else if(pt<200.000) return 0.952110;
		else return 0.913392;
	}
else if(pantau==1){
		if(pt<35.000) return 0.338271;
		else if(pt<40.000) return 0.344894;
		else if(pt<60.000) return 0.322365;
		else if(pt<90.000) return 0.264942;
		else if(pt<110.000) return 0.188995;
		else if(pt<160.000) return 0.192498;
		else if(pt<300.000) return 0.310859;
		else return 0.212839;
	}
else if(pantau==2){
		if(pt<35.000) return 0.180813;
		else if(pt<40.000) return 0.193467;
		else if(pt<50.000) return 0.187040;
		else if(pt<80.000) return 0.162128;
		else if(pt<130.000) return 0.153545;
		else if(pt<230.000) return 0.204178;
		else return 0.131744;
	}
else if(pantau==3){
		if(pt<35.000) return 0.083396;
		else if(pt<40.000) return 0.088101;
		else if(pt<45.000) return 0.082930;
		else if(pt<50.000) return 0.076664;
		else if(pt<80.000) return 0.066792;
		else if(pt<150.000) return 0.036525;
		else return 0.011343;
	}
else if(pantau==4){
		if(pt<35.000) return 0.042248;
		else if(pt<40.000) return 0.042298;
		else if(pt<45.000) return 0.042166;
		else if(pt<50.000) return 0.038723;
		else if(pt<75.000) return 0.032075;
		else if(pt<100.000) return 0.022467;
		else if(pt<150.000) return 0.013771;
		else return 0.007922;
	}
else {cout << "something wrong" << endl; return 0;}
}

