#include <iostream>
using namespace std;
float GetFF03_WCR_5D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 1.061079;
		else if(pt<40.000) return 1.088086;
		else if(pt<45.000) return 1.288712;
		else if(pt<50.000) return 1.316783;
		else if(pt<60.000) return 1.210827;
		else if(pt<70.000) return 1.086109;
		else if(pt<80.000) return 1.046310;
		else if(pt<90.000) return 0.990473;
		else if(pt<120.000) return 1.063794;
		else if(pt<160.000) return 1.180190;
		else if(pt<200.000) return 1.329454;
		else return 1.288220;
		}
else if(pantau==1){
		if(pt<35.000) return 0.429805;
		else if(pt<40.000) return 0.434749;
		else if(pt<60.000) return 0.406311;
		else if(pt<90.000) return 0.348855;
		else if(pt<110.000) return 0.259947;
		else if(pt<160.000) return 0.257851;
		else if(pt<300.000) return 0.421565;
		else return 0.460812;
		}
else if(pantau==2){
		if(pt<35.000) return 0.247356;
		else if(pt<40.000) return 0.263394;
		else if(pt<50.000) return 0.255222;
		else if(pt<80.000) return 0.226369;
		else if(pt<130.000) return 0.218449;
		else if(pt<230.000) return 0.301695;
		else return 0.214677;
		}
else if(pantau==3){
		if(pt<35.000) return 0.107847;
		else if(pt<40.000) return 0.115721;
		else if(pt<45.000) return 0.110608;
		else if(pt<50.000) return 0.103758;
		else if(pt<80.000) return 0.091526;
		else if(pt<150.000) return 0.053027;
		else return 0.019815;
		}
else if(pantau==4){
		if(pt<35.000) return 0.054725;
		else if(pt<40.000) return 0.055566;
		else if(pt<45.000) return 0.056164;
		else if(pt<50.000) return 0.052635;
		else if(pt<75.000) return 0.044242;
		else if(pt<100.000) return 0.032979;
		else if(pt<150.000) return 0.021665;
		else return 0.015723;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_WCR_5D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 1.075625;
		else if(pt<40.000) return 1.107959;
		else if(pt<45.000) return 1.317043;
		else if(pt<50.000) return 1.353437;
		else if(pt<60.000) return 1.242491;
		else if(pt<70.000) return 1.127378;
		else if(pt<80.000) return 1.099803;
		else if(pt<90.000) return 1.055021;
		else if(pt<120.000) return 1.125446;
		else if(pt<160.000) return 1.290976;
		else if(pt<200.000) return 1.543425;
		else return 1.559042;
	}
else if(pantau==1){
		if(pt<35.000) return 0.434017;
		else if(pt<40.000) return 0.440188;
		else if(pt<60.000) return 0.410388;
		else if(pt<90.000) return 0.355082;
		else if(pt<110.000) return 0.271548;
		else if(pt<160.000) return 0.271208;
		else if(pt<300.000) return 0.455403;
		else return 0.588540;
	}
else if(pantau==2){
		if(pt<35.000) return 0.251230;
		else if(pt<40.000) return 0.268228;
		else if(pt<50.000) return 0.259569;
		else if(pt<80.000) return 0.230455;
		else if(pt<130.000) return 0.225780;
		else if(pt<230.000) return 0.319591;
		else return 0.253179;
	}
else if(pantau==3){
		if(pt<35.000) return 0.109413;
		else if(pt<40.000) return 0.117706;
		else if(pt<45.000) return 0.112965;
		else if(pt<50.000) return 0.106446;
		else if(pt<80.000) return 0.093139;
		else if(pt<150.000) return 0.055116;
		else return 0.022861;
	}
else if(pantau==4){
		if(pt<35.000) return 0.055881;
		else if(pt<40.000) return 0.056954;
		else if(pt<45.000) return 0.057819;
		else if(pt<50.000) return 0.054543;
		else if(pt<75.000) return 0.045418;
		else if(pt<100.000) return 0.034926;
		else if(pt<150.000) return 0.023961;
		else return 0.019317;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF03_WCR_5D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 1.046532;
		else if(pt<40.000) return 1.068213;
		else if(pt<45.000) return 1.260382;
		else if(pt<50.000) return 1.280130;
		else if(pt<60.000) return 1.179163;
		else if(pt<70.000) return 1.044841;
		else if(pt<80.000) return 0.992816;
		else if(pt<90.000) return 0.925924;
		else if(pt<120.000) return 1.002142;
		else if(pt<160.000) return 1.069405;
		else if(pt<200.000) return 1.115484;
		else return 1.017399;
	}
else if(pantau==1){
		if(pt<35.000) return 0.425592;
		else if(pt<40.000) return 0.429310;
		else if(pt<60.000) return 0.402235;
		else if(pt<90.000) return 0.342628;
		else if(pt<110.000) return 0.248345;
		else if(pt<160.000) return 0.244494;
		else if(pt<300.000) return 0.387727;
		else return 0.333085;
	}
else if(pantau==2){
		if(pt<35.000) return 0.243482;
		else if(pt<40.000) return 0.258560;
		else if(pt<50.000) return 0.250876;
		else if(pt<80.000) return 0.222283;
		else if(pt<130.000) return 0.211118;
		else if(pt<230.000) return 0.283799;
		else return 0.176175;
	}
else if(pantau==3){
		if(pt<35.000) return 0.106280;
		else if(pt<40.000) return 0.113736;
		else if(pt<45.000) return 0.108250;
		else if(pt<50.000) return 0.101070;
		else if(pt<80.000) return 0.089912;
		else if(pt<150.000) return 0.050938;
		else return 0.016768;
	}
else if(pantau==4){
		if(pt<35.000) return 0.053568;
		else if(pt<40.000) return 0.054178;
		else if(pt<45.000) return 0.054508;
		else if(pt<50.000) return 0.050727;
		else if(pt<75.000) return 0.043066;
		else if(pt<100.000) return 0.031032;
		else if(pt<150.000) return 0.019368;
		else return 0.012129;
	}
else {cout << "something wrong" << endl; return 0;}
}

