#include <iostream>
using namespace std;
float GetFF01_QCD_5D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.545922;
		else if(pt<40.000) return 0.585532;
		else if(pt<45.000) return 0.630236;
		else if(pt<50.000) return 0.636405;
		else if(pt<60.000) return 0.561007;
		else if(pt<70.000) return 0.487809;
		else if(pt<80.000) return 0.444088;
		else if(pt<90.000) return 0.500899;
		else if(pt<120.000) return 0.596159;
		else if(pt<160.000) return 0.692474;
		else if(pt<200.000) return 0.850298;
		else return 1.004013;
		}
else if(pantau==1){
		if(pt<35.000) return 0.194117;
		else if(pt<40.000) return 0.196573;
		else if(pt<60.000) return 0.174663;
		else if(pt<90.000) return 0.123733;
		else if(pt<110.000) return 0.131079;
		else if(pt<160.000) return 0.139144;
		else if(pt<300.000) return 0.172518;
		else return 0.239170;
		}
else if(pantau==2){
		if(pt<35.000) return 0.099158;
		else if(pt<40.000) return 0.101164;
		else if(pt<50.000) return 0.101697;
		else if(pt<80.000) return 0.083819;
		else if(pt<130.000) return 0.093278;
		else if(pt<230.000) return 0.119357;
		else return 0.150435;
		}
else if(pantau==3){
		if(pt<35.000) return 0.042079;
		else if(pt<40.000) return 0.042551;
		else if(pt<45.000) return 0.043370;
		else if(pt<50.000) return 0.037777;
		else if(pt<80.000) return 0.027405;
		else if(pt<150.000) return 0.016733;
		else return 0.013660;
		}
else if(pantau==4){
		if(pt<35.000) return 0.022269;
		else if(pt<40.000) return 0.021646;
		else if(pt<45.000) return 0.022157;
		else if(pt<50.000) return 0.019030;
		else if(pt<75.000) return 0.012564;
		else if(pt<100.000) return 0.008674;
		else if(pt<150.000) return 0.008261;
		else return 0.007597;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_QCD_5D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.556899;
		else if(pt<40.000) return 0.599825;
		else if(pt<45.000) return 0.648394;
		else if(pt<50.000) return 0.658299;
		else if(pt<60.000) return 0.578550;
		else if(pt<70.000) return 0.505956;
		else if(pt<80.000) return 0.461001;
		else if(pt<90.000) return 0.519170;
		else if(pt<120.000) return 0.609586;
		else if(pt<160.000) return 0.712058;
		else if(pt<200.000) return 0.885383;
		else return 1.037765;
	}
else if(pantau==1){
		if(pt<35.000) return 0.196737;
		else if(pt<40.000) return 0.199800;
		else if(pt<60.000) return 0.176731;
		else if(pt<90.000) return 0.125200;
		else if(pt<110.000) return 0.133133;
		else if(pt<160.000) return 0.141089;
		else if(pt<300.000) return 0.175404;
		else return 0.246684;
	}
else if(pantau==2){
		if(pt<35.000) return 0.101171;
		else if(pt<40.000) return 0.103489;
		else if(pt<50.000) return 0.103681;
		else if(pt<80.000) return 0.085005;
		else if(pt<130.000) return 0.094382;
		else if(pt<230.000) return 0.121156;
		else return 0.153990;
	}
else if(pantau==3){
		if(pt<35.000) return 0.043072;
		else if(pt<40.000) return 0.043700;
		else if(pt<45.000) return 0.044718;
		else if(pt<50.000) return 0.039190;
		else if(pt<80.000) return 0.028000;
		else if(pt<150.000) return 0.017025;
		else return 0.013982;
	}
else if(pantau==4){
		if(pt<35.000) return 0.022999;
		else if(pt<40.000) return 0.022463;
		else if(pt<45.000) return 0.023090;
		else if(pt<50.000) return 0.020011;
		else if(pt<75.000) return 0.012987;
		else if(pt<100.000) return 0.008982;
		else if(pt<150.000) return 0.008554;
		else return 0.007929;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF01_QCD_5D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.534945;
		else if(pt<40.000) return 0.571240;
		else if(pt<45.000) return 0.612077;
		else if(pt<50.000) return 0.614510;
		else if(pt<60.000) return 0.543465;
		else if(pt<70.000) return 0.469662;
		else if(pt<80.000) return 0.427174;
		else if(pt<90.000) return 0.482629;
		else if(pt<120.000) return 0.582732;
		else if(pt<160.000) return 0.672890;
		else if(pt<200.000) return 0.815213;
		else return 0.970261;
	}
else if(pantau==1){
		if(pt<35.000) return 0.191498;
		else if(pt<40.000) return 0.193347;
		else if(pt<60.000) return 0.172596;
		else if(pt<90.000) return 0.122265;
		else if(pt<110.000) return 0.129025;
		else if(pt<160.000) return 0.137199;
		else if(pt<300.000) return 0.169632;
		else return 0.231655;
	}
else if(pantau==2){
		if(pt<35.000) return 0.097144;
		else if(pt<40.000) return 0.098839;
		else if(pt<50.000) return 0.099712;
		else if(pt<80.000) return 0.082634;
		else if(pt<130.000) return 0.092175;
		else if(pt<230.000) return 0.117558;
		else return 0.146879;
	}
else if(pantau==3){
		if(pt<35.000) return 0.041087;
		else if(pt<40.000) return 0.041402;
		else if(pt<45.000) return 0.042023;
		else if(pt<50.000) return 0.036365;
		else if(pt<80.000) return 0.026809;
		else if(pt<150.000) return 0.016441;
		else return 0.013339;
	}
else if(pantau==4){
		if(pt<35.000) return 0.021539;
		else if(pt<40.000) return 0.020829;
		else if(pt<45.000) return 0.021224;
		else if(pt<50.000) return 0.018048;
		else if(pt<75.000) return 0.012140;
		else if(pt<100.000) return 0.008366;
		else if(pt<150.000) return 0.007969;
		else return 0.007264;
	}
else {cout << "something wrong" << endl; return 0;}
}

