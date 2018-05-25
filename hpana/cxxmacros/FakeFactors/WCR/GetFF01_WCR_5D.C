#include <iostream>
using namespace std;
float GetFF01_WCR_5D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.837431;
		else if(pt<40.000) return 0.878624;
		else if(pt<45.000) return 1.044502;
		else if(pt<50.000) return 1.060600;
		else if(pt<60.000) return 0.990887;
		else if(pt<70.000) return 0.864244;
		else if(pt<80.000) return 0.856013;
		else if(pt<90.000) return 0.798467;
		else if(pt<120.000) return 0.834377;
		else if(pt<160.000) return 0.978955;
		else if(pt<200.000) return 1.042788;
		else return 0.923539;
		}
else if(pantau==1){
		if(pt<35.000) return 0.258402;
		else if(pt<40.000) return 0.267575;
		else if(pt<60.000) return 0.250279;
		else if(pt<90.000) return 0.199736;
		else if(pt<110.000) return 0.144529;
		else if(pt<160.000) return 0.140569;
		else if(pt<300.000) return 0.214073;
		else return 0.240715;
		}
else if(pantau==2){
		if(pt<35.000) return 0.126688;
		else if(pt<40.000) return 0.136917;
		else if(pt<50.000) return 0.131420;
		else if(pt<80.000) return 0.111607;
		else if(pt<130.000) return 0.101835;
		else if(pt<230.000) return 0.136318;
		else return 0.108892;
		}
else if(pantau==3){
		if(pt<35.000) return 0.058735;
		else if(pt<40.000) return 0.061382;
		else if(pt<45.000) return 0.057425;
		else if(pt<50.000) return 0.053195;
		else if(pt<80.000) return 0.044252;
		else if(pt<150.000) return 0.022672;
		else return 0.008134;
		}
else if(pantau==4){
		if(pt<35.000) return 0.031091;
		else if(pt<40.000) return 0.031006;
		else if(pt<45.000) return 0.030601;
		else if(pt<50.000) return 0.027921;
		else if(pt<75.000) return 0.022127;
		else if(pt<100.000) return 0.014743;
		else if(pt<150.000) return 0.009093;
		else return 0.006242;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_WCR_5D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.848911;
		else if(pt<40.000) return 0.894671;
		else if(pt<45.000) return 1.067464;
		else if(pt<50.000) return 1.090122;
		else if(pt<60.000) return 1.016799;
		else if(pt<70.000) return 0.897082;
		else if(pt<80.000) return 0.899778;
		else if(pt<90.000) return 0.850503;
		else if(pt<120.000) return 0.882732;
		else if(pt<160.000) return 1.070851;
		else if(pt<200.000) return 1.210620;
		else return 1.117693;
	}
else if(pantau==1){
		if(pt<35.000) return 0.260935;
		else if(pt<40.000) return 0.270923;
		else if(pt<60.000) return 0.252790;
		else if(pt<90.000) return 0.203301;
		else if(pt<110.000) return 0.150979;
		else if(pt<160.000) return 0.147850;
		else if(pt<300.000) return 0.231257;
		else return 0.307436;
	}
else if(pantau==2){
		if(pt<35.000) return 0.128672;
		else if(pt<40.000) return 0.139430;
		else if(pt<50.000) return 0.133658;
		else if(pt<80.000) return 0.113622;
		else if(pt<130.000) return 0.105252;
		else if(pt<230.000) return 0.144404;
		else return 0.128421;
	}
else if(pantau==3){
		if(pt<35.000) return 0.059588;
		else if(pt<40.000) return 0.062435;
		else if(pt<45.000) return 0.058649;
		else if(pt<50.000) return 0.054573;
		else if(pt<80.000) return 0.045032;
		else if(pt<150.000) return 0.023565;
		else return 0.009384;
	}
else if(pantau==4){
		if(pt<35.000) return 0.031748;
		else if(pt<40.000) return 0.031781;
		else if(pt<45.000) return 0.031503;
		else if(pt<50.000) return 0.028933;
		else if(pt<75.000) return 0.022715;
		else if(pt<100.000) return 0.015613;
		else if(pt<150.000) return 0.010057;
		else return 0.007669;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_WCR_5D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.825951;
		else if(pt<40.000) return 0.862577;
		else if(pt<45.000) return 1.021541;
		else if(pt<50.000) return 1.031077;
		else if(pt<60.000) return 0.964974;
		else if(pt<70.000) return 0.831406;
		else if(pt<80.000) return 0.812249;
		else if(pt<90.000) return 0.746432;
		else if(pt<120.000) return 0.786021;
		else if(pt<160.000) return 0.887060;
		else if(pt<200.000) return 0.874955;
		else return 0.729384;
	}
else if(pantau==1){
		if(pt<35.000) return 0.255870;
		else if(pt<40.000) return 0.264228;
		else if(pt<60.000) return 0.247767;
		else if(pt<90.000) return 0.196171;
		else if(pt<110.000) return 0.138079;
		else if(pt<160.000) return 0.133287;
		else if(pt<300.000) return 0.196890;
		else return 0.173994;
	}
else if(pantau==2){
		if(pt<35.000) return 0.124704;
		else if(pt<40.000) return 0.134404;
		else if(pt<50.000) return 0.129182;
		else if(pt<80.000) return 0.109593;
		else if(pt<130.000) return 0.098417;
		else if(pt<230.000) return 0.128232;
		else return 0.089362;
	}
else if(pantau==3){
		if(pt<35.000) return 0.057881;
		else if(pt<40.000) return 0.060329;
		else if(pt<45.000) return 0.056201;
		else if(pt<50.000) return 0.051817;
		else if(pt<80.000) return 0.043471;
		else if(pt<150.000) return 0.021779;
		else return 0.006883;
	}
else if(pantau==4){
		if(pt<35.000) return 0.030435;
		else if(pt<40.000) return 0.030232;
		else if(pt<45.000) return 0.029699;
		else if(pt<50.000) return 0.026909;
		else if(pt<75.000) return 0.021539;
		else if(pt<100.000) return 0.013872;
		else if(pt<150.000) return 0.008129;
		else return 0.004815;
	}
else {cout << "something wrong" << endl; return 0;}
}

