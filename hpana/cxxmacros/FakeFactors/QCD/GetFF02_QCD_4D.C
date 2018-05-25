#include <iostream>
using namespace std;
float GetFF02_QCD_4D(float pt, int pantau){
if(pantau==0){
		if(pt<35.000) return 0.646632;
		else if(pt<40.000) return 0.680181;
		else if(pt<45.000) return 0.729003;
		else if(pt<50.000) return 0.738614;
		else if(pt<60.000) return 0.669525;
		else if(pt<70.000) return 0.586437;
		else if(pt<80.000) return 0.513344;
		else if(pt<90.000) return 0.572844;
		else if(pt<120.000) return 0.685172;
		else if(pt<160.000) return 0.788047;
		else if(pt<200.000) return 0.991873;
		else return 1.213365;
		}
else if(pantau==1){
		if(pt<35.000) return 0.270217;
		else if(pt<40.000) return 0.271552;
		else if(pt<60.000) return 0.243361;
		else if(pt<90.000) return 0.184683;
		else if(pt<110.000) return 0.191423;
		else if(pt<160.000) return 0.210614;
		else if(pt<300.000) return 0.275397;
		else return 0.359359;
		}
else if(pantau==2){
		if(pt<35.000) return 0.151015;
		else if(pt<40.000) return 0.154570;
		else if(pt<50.000) return 0.157496;
		else if(pt<80.000) return 0.138293;
		else if(pt<130.000) return 0.151777;
		else if(pt<230.000) return 0.194198;
		else return 0.239902;
		}
else if(pantau>=3){
		if(pt<35.000) return 0.047521;
		else if(pt<40.000) return 0.047589;
		else if(pt<50.000) return 0.046802;
		else if(pt<75.000) return 0.033638;
		else if(pt<100.000) return 0.023176;
		else if(pt<150.000) return 0.022127;
		else if(pt<200.000) return 0.020836;
		else return 0.018514;
		}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_QCD_4D_up(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.659669;
		else if(pt<40.000) return 0.696888;
		else if(pt<45.000) return 0.750077;
		else if(pt<50.000) return 0.764162;
		else if(pt<60.000) return 0.690491;
		else if(pt<70.000) return 0.608314;
		else if(pt<80.000) return 0.533024;
		else if(pt<90.000) return 0.593879;
		else if(pt<120.000) return 0.700613;
		else if(pt<160.000) return 0.810298;
		else if(pt<200.000) return 1.032869;
		else return 1.254317;
	}
else if(pantau==1){
		if(pt<35.000) return 0.273885;
		else if(pt<40.000) return 0.276030;
		else if(pt<60.000) return 0.246252;
		else if(pt<90.000) return 0.186876;
		else if(pt<110.000) return 0.194437;
		else if(pt<160.000) return 0.213561;
		else if(pt<300.000) return 0.280005;
		else return 0.370649;
	}
else if(pantau==2){
		if(pt<35.000) return 0.154101;
		else if(pt<40.000) return 0.158137;
		else if(pt<50.000) return 0.160581;
		else if(pt<80.000) return 0.140253;
		else if(pt<130.000) return 0.153576;
		else if(pt<230.000) return 0.197127;
		else return 0.245570;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.048435;
		else if(pt<40.000) return 0.048642;
		else if(pt<50.000) return 0.047706;
		else if(pt<75.000) return 0.034285;
		else if(pt<100.000) return 0.023653;
		else if(pt<150.000) return 0.022548;
		else if(pt<200.000) return 0.021470;
		else return 0.019040;
	}
else {cout << "something wrong" << endl; return 0;}
}

float GetFF02_QCD_4D_dn(float pt,int pantau){
if(pantau==0){
		if(pt<35.000) return 0.633595;
		else if(pt<40.000) return 0.663473;
		else if(pt<45.000) return 0.707929;
		else if(pt<50.000) return 0.713067;
		else if(pt<60.000) return 0.648559;
		else if(pt<70.000) return 0.564560;
		else if(pt<80.000) return 0.493664;
		else if(pt<90.000) return 0.551808;
		else if(pt<120.000) return 0.669732;
		else if(pt<160.000) return 0.765796;
		else if(pt<200.000) return 0.950877;
		else return 1.172413;
	}
else if(pantau==1){
		if(pt<35.000) return 0.266550;
		else if(pt<40.000) return 0.267074;
		else if(pt<60.000) return 0.240470;
		else if(pt<90.000) return 0.182489;
		else if(pt<110.000) return 0.188410;
		else if(pt<160.000) return 0.207666;
		else if(pt<300.000) return 0.270788;
		else return 0.348068;
	}
else if(pantau==2){
		if(pt<35.000) return 0.147928;
		else if(pt<40.000) return 0.151003;
		else if(pt<50.000) return 0.154412;
		else if(pt<80.000) return 0.136334;
		else if(pt<130.000) return 0.149979;
		else if(pt<230.000) return 0.191270;
		else return 0.234234;
	}
else if(pantau>=3){
		if(pt<35.000) return 0.046607;
		else if(pt<40.000) return 0.046536;
		else if(pt<50.000) return 0.045897;
		else if(pt<75.000) return 0.032991;
		else if(pt<100.000) return 0.022699;
		else if(pt<150.000) return 0.021706;
		else if(pt<200.000) return 0.020203;
		else return 0.017987;
	}
else {cout << "something wrong" << endl; return 0;}
}

