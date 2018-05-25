#include <iostream>
using namespace std;
float GetFF01_WCR(float pt, int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.251830;
		else if(pt<35.000) return 0.250341;
		else if(pt<37.500) return 0.251207;
		else if(pt<40.000) return 0.251185;
		else if(pt<45.000) return 0.250236;
		else if(pt<50.000) return 0.230010;
		else if(pt<55.000) return 0.226351;
		else if(pt<60.000) return 0.211532;
		else if(pt<70.000) return 0.195627;
		else if(pt<80.000) return 0.170253;
		else if(pt<90.000) return 0.159843;
		else if(pt<100.000) return 0.153777;
		else if(pt<120.000) return 0.146061;
		else if(pt<140.000) return 0.149164;
		else if(pt<160.000) return 0.172004;
		else if(pt<200.000) return 0.180818;
		else return 0.199896;
		}
else if(nTracks==3){
		if(pt<35.000) return 0.045453;
		else if(pt<40.000) return 0.046521;
		else if(pt<45.000) return 0.044043;
		else if(pt<50.000) return 0.040500;
		else if(pt<75.000) return 0.034051;
		else if(pt<100.000) return 0.021987;
		else if(pt<150.000) return 0.013890;
		else return 0.006868;
		}
else return 0;
}

float GetFF01_WCR_up(float pt,int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.254223;
		else if(pt<35.000) return 0.253041;
		else if(pt<37.500) return 0.254262;
		else if(pt<40.000) return 0.254584;
		else if(pt<45.000) return 0.253001;
		else if(pt<50.000) return 0.233182;
		else if(pt<55.000) return 0.230085;
		else if(pt<60.000) return 0.215687;
		else if(pt<70.000) return 0.199033;
		else if(pt<80.000) return 0.174303;
		else if(pt<90.000) return 0.164722;
		else if(pt<100.000) return 0.159724;
		else if(pt<120.000) return 0.151477;
		else if(pt<140.000) return 0.156918;
		else if(pt<160.000) return 0.183537;
		else if(pt<200.000) return 0.193482;
		else return 0.215458;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.046001;
		else if(pt<40.000) return 0.047183;
		else if(pt<45.000) return 0.044807;
		else if(pt<50.000) return 0.041359;
		else if(pt<75.000) return 0.034564;
		else if(pt<100.000) return 0.022719;
		else if(pt<150.000) return 0.014678;
		else return 0.007782;
	}
else return 0;
}

float GetFF01_WCR_dn(float pt,int nTracks){
if(nTracks==1){
		if(pt<32.500) return 0.249438;
		else if(pt<35.000) return 0.247641;
		else if(pt<37.500) return 0.248153;
		else if(pt<40.000) return 0.247786;
		else if(pt<45.000) return 0.247471;
		else if(pt<50.000) return 0.226838;
		else if(pt<55.000) return 0.222618;
		else if(pt<60.000) return 0.207377;
		else if(pt<70.000) return 0.192222;
		else if(pt<80.000) return 0.166202;
		else if(pt<90.000) return 0.154964;
		else if(pt<100.000) return 0.147830;
		else if(pt<120.000) return 0.140645;
		else if(pt<140.000) return 0.141410;
		else if(pt<160.000) return 0.160471;
		else if(pt<200.000) return 0.168154;
		else return 0.184334;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.044906;
		else if(pt<40.000) return 0.045859;
		else if(pt<45.000) return 0.043279;
		else if(pt<50.000) return 0.039641;
		else if(pt<75.000) return 0.033538;
		else if(pt<100.000) return 0.021256;
		else if(pt<150.000) return 0.013101;
		else return 0.005954;
	}
else return 0;
}

