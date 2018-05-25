#include <iostream>
using namespace std;
float GetFF02_QCD_5D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.647156;
		else if(pt<40.000) return 0.684032;
		else if(pt<45.000) return 0.728111;
		else if(pt<50.000) return 0.743311;
		else if(pt<60.000) return 0.665811;
		else if(pt<70.000) return 0.585890;
		else if(pt<80.000) return 0.523691;
		else if(pt<90.000) return 0.580566;
		else if(pt<120.000) return 0.683807;
		else if(pt<160.000) return 0.780623;
		else if(pt<200.000) return 0.980313;
		else return 1.214645;
		}
else if(pantau==1){
		if(pt<35.000) return 0.269917;
		else if(pt<40.000) return 0.271100;
		else if(pt<60.000) return 0.243066;
		else if(pt<90.000) return 0.184645;
		else if(pt<110.000) return 0.192693;
		else if(pt<160.000) return 0.210759;
		else if(pt<300.000) return 0.275289;
		else return 0.359227;
		}
else if(pantau==2){
		if(pt<35.000) return 0.151433;
		else if(pt<40.000) return 0.154219;
		else if(pt<50.000) return 0.157177;
		else if(pt<80.000) return 0.137885;
		else if(pt<130.000) return 0.152016;
		else if(pt<230.000) return 0.194556;
		else return 0.239127;
		}
else if(pantau==3){
		if(pt<35.000) return 0.063003;
		else if(pt<40.000) return 0.064399;
		else if(pt<45.000) return 0.067019;
		else if(pt<50.000) return 0.058598;
		else if(pt<80.000) return 0.046292;
		else if(pt<150.000) return 0.029565;
		else return 0.022959;
		}
else if(pantau==4){
		if(pt<35.000) return 0.032327;
		else if(pt<40.000) return 0.032021;
		else if(pt<45.000) return 0.033060;
		else if(pt<50.000) return 0.029299;
		else if(pt<75.000) return 0.020529;
		else if(pt<100.000) return 0.014997;
		else if(pt<150.000) return 0.014538;
		else return 0.013027;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_QCD_5D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.660169;
		else if(pt<40.000) return 0.700729;
		else if(pt<45.000) return 0.749089;
		else if(pt<50.000) return 0.768884;
		else if(pt<60.000) return 0.686630;
		else if(pt<70.000) return 0.607685;
		else if(pt<80.000) return 0.543637;
		else if(pt<90.000) return 0.601743;
		else if(pt<120.000) return 0.699208;
		else if(pt<160.000) return 0.802700;
		else if(pt<200.000) return 1.020762;
		else return 1.255479;
	}
else if(pantau==1){
		if(pt<35.000) return 0.273559;
		else if(pt<40.000) return 0.275550;
		else if(pt<60.000) return 0.245942;
		else if(pt<90.000) return 0.186835;
		else if(pt<110.000) return 0.195713;
		else if(pt<160.000) return 0.213705;
		else if(pt<300.000) return 0.279894;
		else return 0.370513;
	}
else if(pantau==2){
		if(pt<35.000) return 0.154508;
		else if(pt<40.000) return 0.157763;
		else if(pt<50.000) return 0.160244;
		else if(pt<80.000) return 0.139836;
		else if(pt<130.000) return 0.153814;
		else if(pt<230.000) return 0.197488;
		else return 0.244779;
	}
else if(pantau==3){
		if(pt<35.000) return 0.064489;
		else if(pt<40.000) return 0.066138;
		else if(pt<45.000) return 0.069101;
		else if(pt<50.000) return 0.060788;
		else if(pt<80.000) return 0.047299;
		else if(pt<150.000) return 0.030080;
		else return 0.023499;
	}
else if(pantau==4){
		if(pt<35.000) return 0.033387;
		else if(pt<40.000) return 0.033229;
		else if(pt<45.000) return 0.034451;
		else if(pt<50.000) return 0.030810;
		else if(pt<75.000) return 0.021221;
		else if(pt<100.000) return 0.015529;
		else if(pt<150.000) return 0.015053;
		else return 0.013598;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_QCD_5D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.634143;
		else if(pt<40.000) return 0.667335;
		else if(pt<45.000) return 0.707132;
		else if(pt<50.000) return 0.717739;
		else if(pt<60.000) return 0.644991;
		else if(pt<70.000) return 0.564094;
		else if(pt<80.000) return 0.503746;
		else if(pt<90.000) return 0.559389;
		else if(pt<120.000) return 0.668406;
		else if(pt<160.000) return 0.758547;
		else if(pt<200.000) return 0.939864;
		else return 1.173812;
	}
else if(pantau==1){
		if(pt<35.000) return 0.266275;
		else if(pt<40.000) return 0.266650;
		else if(pt<60.000) return 0.240189;
		else if(pt<90.000) return 0.182455;
		else if(pt<110.000) return 0.189673;
		else if(pt<160.000) return 0.207813;
		else if(pt<300.000) return 0.270685;
		else return 0.347941;
	}
else if(pantau==2){
		if(pt<35.000) return 0.148358;
		else if(pt<40.000) return 0.150674;
		else if(pt<50.000) return 0.154110;
		else if(pt<80.000) return 0.135935;
		else if(pt<130.000) return 0.150218;
		else if(pt<230.000) return 0.191624;
		else return 0.233476;
	}
else if(pantau==3){
		if(pt<35.000) return 0.061517;
		else if(pt<40.000) return 0.062660;
		else if(pt<45.000) return 0.064937;
		else if(pt<50.000) return 0.056407;
		else if(pt<80.000) return 0.045285;
		else if(pt<150.000) return 0.029049;
		else return 0.022419;
	}
else if(pantau==4){
		if(pt<35.000) return 0.031267;
		else if(pt<40.000) return 0.030812;
		else if(pt<45.000) return 0.031668;
		else if(pt<50.000) return 0.027788;
		else if(pt<75.000) return 0.019837;
		else if(pt<100.000) return 0.014464;
		else if(pt<150.000) return 0.014024;
		else return 0.012457;
	}
else {cout << "something wrong" << endl; return 0;}
}

