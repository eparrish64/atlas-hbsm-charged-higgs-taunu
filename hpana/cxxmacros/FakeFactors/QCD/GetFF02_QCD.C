#include <iostream>
using namespace std;
float GetFF02_QCD(float pt, int nTracks){
  if(nTracks==1){
    if(pt<35.000) return 0.258698;
    else if(pt<40.000) return 0.256418;
    else if(pt<45.000) return 0.245939;
    else if(pt<50.000) return 0.253721;
    else if(pt<60.000) return 0.214414;
    else if(pt<75.000) return 0.180350;
    else if(pt<90.000) return 0.178670;
    else if(pt<105.000) return 0.194458;
    else if(pt<120.000) return 0.203454;
    else if(pt<140.000) return 0.217104;
    else if(pt<160.000) return 0.232745;
    else if(pt<200.000) return 0.255004;
    else if(pt<300.000) return 0.295285;
    else return 0.332055;
  }
  else if(nTracks==3){
    if(pt<35.000) return 0.047521;
    else if(pt<40.000) return 0.047589;
    else if(pt<50.000) return 0.046802;
    else if(pt<75.000) return 0.033638;
    else if(pt<100.000) return 0.023176;
    else if(pt<150.000) return 0.022127;
    else if(pt<200.000) return 0.020836;
    else return 0.018514;
  }
  else
    return 0;
}

float GetFF02_QCD_up(float pt,int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.261249;
		else if(pt<40.000) return 0.259437;
		else if(pt<45.000) return 0.249360;
		else if(pt<50.000) return 0.257727;
		else if(pt<60.000) return 0.217362;
		else if(pt<75.000) return 0.182565;
		else if(pt<90.000) return 0.180687;
		else if(pt<105.000) return 0.196834;
		else if(pt<120.000) return 0.206353;
		else if(pt<140.000) return 0.220277;
		else if(pt<160.000) return 0.236835;
		else if(pt<200.000) return 0.259033;
		else if(pt<300.000) return 0.299948;
		else return 0.339179;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.048435;
		else if(pt<40.000) return 0.048642;
		else if(pt<50.000) return 0.047706;
		else if(pt<75.000) return 0.034285;
		else if(pt<100.000) return 0.023653;
		else if(pt<150.000) return 0.022548;
		else if(pt<200.000) return 0.021470;
		else return 0.019040;
	}
 else
   return 0;
}

float GetFF02_QCD_dn(float pt,int nTracks){
if(nTracks==1){
		if(pt<35.000) return 0.256147;
		else if(pt<40.000) return 0.253398;
		else if(pt<45.000) return 0.242518;
		else if(pt<50.000) return 0.249715;
		else if(pt<60.000) return 0.211466;
		else if(pt<75.000) return 0.178135;
		else if(pt<90.000) return 0.176653;
		else if(pt<105.000) return 0.192082;
		else if(pt<120.000) return 0.200556;
		else if(pt<140.000) return 0.213930;
		else if(pt<160.000) return 0.228656;
		else if(pt<200.000) return 0.250975;
		else if(pt<300.000) return 0.290622;
		else return 0.324930;
	}
else if(nTracks==3){
		if(pt<35.000) return 0.046607;
		else if(pt<40.000) return 0.046536;
		else if(pt<50.000) return 0.045897;
		else if(pt<75.000) return 0.032991;
		else if(pt<100.000) return 0.022699;
		else if(pt<150.000) return 0.021706;
		else if(pt<200.000) return 0.020203;
		else return 0.017987;
	}
 else 
   return 0;
}

