#include <iostream>
using namespace std;
float GetFF03_QCD(float pt, int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.340784;
		else if(pt<40.000) return 0.338206;
		else if(pt<45.000) return 0.324608;
		else if(pt<50.000) return 0.336615;
		else if(pt<60.000) return 0.290745;
		else if(pt<75.000) return 0.253151;
		else if(pt<90.000) return 0.246716;
		else if(pt<105.000) return 0.262943;
		else if(pt<120.000) return 0.270392;
		else if(pt<140.000) return 0.288476;
		else if(pt<160.000) return 0.307572;
		else if(pt<200.000) return 0.334738;
		else if(pt<300.000) return 0.395484;
		else return 0.476236;
		}
else if(nTracks==3){
		if(pt<35.000) return 0.061653;
		else if(pt<40.000) return 0.062550;
		else if(pt<50.000) return 0.062434;
		else if(pt<75.000) return 0.046918;
		else if(pt<100.000) return 0.033295;
		else if(pt<150.000) return 0.032118;
		else if(pt<200.000) return 0.031154;
		else return 0.028318;
		}
else return 0;
}

float GetFF03_QCD_up(float pt,int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.344145;
		else if(pt<40.000) return 0.342188;
		else if(pt<45.000) return 0.329124;
		else if(pt<50.000) return 0.341929;
		else if(pt<60.000) return 0.294742;
		else if(pt<75.000) return 0.256261;
		else if(pt<90.000) return 0.249501;
		else if(pt<105.000) return 0.266156;
		else if(pt<120.000) return 0.274244;
		else if(pt<140.000) return 0.292693;
		else if(pt<160.000) return 0.312976;
		else if(pt<200.000) return 0.340027;
		else if(pt<300.000) return 0.401729;
		else return 0.486453;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.062838;
		else if(pt<40.000) return 0.063934;
		else if(pt<50.000) return 0.063640;
		else if(pt<75.000) return 0.047821;
		else if(pt<100.000) return 0.033981;
		else if(pt<150.000) return 0.032729;
		else if(pt<200.000) return 0.032101;
		else return 0.029124;
	}
else return 0;
}

float GetFF03_QCD_dn(float pt,int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.337424;
		else if(pt<40.000) return 0.334224;
		else if(pt<45.000) return 0.320093;
		else if(pt<50.000) return 0.331300;
		else if(pt<60.000) return 0.286747;
		else if(pt<75.000) return 0.250042;
		else if(pt<90.000) return 0.243931;
		else if(pt<105.000) return 0.259730;
		else if(pt<120.000) return 0.266540;
		else if(pt<140.000) return 0.284259;
		else if(pt<160.000) return 0.302168;
		else if(pt<200.000) return 0.329450;
		else if(pt<300.000) return 0.389238;
		else return 0.466018;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.060468;
		else if(pt<40.000) return 0.061167;
		else if(pt<50.000) return 0.061227;
		else if(pt<75.000) return 0.046016;
		else if(pt<100.000) return 0.032610;
		else if(pt<150.000) return 0.031507;
		else if(pt<200.000) return 0.030207;
		else return 0.027513;
	}
else return 0;
}

