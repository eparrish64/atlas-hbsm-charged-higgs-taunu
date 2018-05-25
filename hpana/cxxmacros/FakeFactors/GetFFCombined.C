#include <iostream>
using namespace std;

float GetFFCombined(float,int,float,float,int);

float GetFFCombined(float pt,int trk,float FF_QCD,float FF_WCR,int idx){
	if(idx==111) return FF_QCD;
	if(idx==222) return FF_WCR;
	if(idx==1){ //Preselection
		if(trk==1){
			if(pt<35.000) return 1.017805*FF_QCD+-0.017805*FF_WCR;
			else if(pt<40.000) return 0.868830*FF_QCD+0.131170*FF_WCR;
			else if(pt<45.000) return 0.754965*FF_QCD+0.245035*FF_WCR;
			else if(pt<50.000) return 0.648390*FF_QCD+0.351610*FF_WCR;
			else if(pt<60.000) return 0.532227*FF_QCD+0.467773*FF_WCR;
			else if(pt<80.000) return 0.533141*FF_QCD+0.466859*FF_WCR;
			else if(pt<100.000) return 0.897294*FF_QCD+0.102706*FF_WCR;
			else return 3.222198*FF_QCD+-2.222198*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.885184*FF_QCD+0.114816*FF_WCR;
			else if(pt<40.000) return 0.663311*FF_QCD+0.336689*FF_WCR;
			else if(pt<45.000) return 0.556412*FF_QCD+0.443588*FF_WCR;
			else if(pt<50.000) return 0.407178*FF_QCD+0.592822*FF_WCR;
			else if(pt<60.000) return 0.318201*FF_QCD+0.681799*FF_WCR;
			else if(pt<80.000) return 0.251416*FF_QCD+0.748584*FF_WCR;
			else if(pt<100.000) return 0.473761*FF_QCD+0.526239*FF_WCR;
			else return 0.915827*FF_QCD+0.084173*FF_WCR;
		}
	}
	if(idx==2){ //hight MET b-veto
		if(trk==1){
			if(pt<35.000) return 1.276196*FF_QCD+-0.276196*FF_WCR;
			else if(pt<40.000) return 1.080305*FF_QCD+-0.080305*FF_WCR;
			else if(pt<45.000) return 0.853577*FF_QCD+0.146423*FF_WCR;
			else if(pt<50.000) return 0.816956*FF_QCD+0.183044*FF_WCR;
			else if(pt<60.000) return 0.623601*FF_QCD+0.376399*FF_WCR;
			else if(pt<80.000) return 0.612393*FF_QCD+0.387607*FF_WCR;
			else if(pt<100.000) return 1.033562*FF_QCD+-0.033562*FF_WCR;
			else return 3.524443*FF_QCD+-2.524443*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.985544*FF_QCD+0.014456*FF_WCR;
			else if(pt<40.000) return 0.782967*FF_QCD+0.217033*FF_WCR;
			else if(pt<45.000) return 0.697926*FF_QCD+0.302074*FF_WCR;
			else if(pt<50.000) return 0.492304*FF_QCD+0.507696*FF_WCR;
			else if(pt<60.000) return 0.372455*FF_QCD+0.627545*FF_WCR;
			else if(pt<80.000) return 0.320832*FF_QCD+0.679168*FF_WCR;
			else if(pt<100.000) return 0.603674*FF_QCD+0.396326*FF_WCR;
			else return 1.002443*FF_QCD+-0.002443*FF_WCR;
		}
	}
	if(idx==3){ //#tau+jets SR
		if(trk==1){
			if(pt<35.000) return 0.689748*FF_QCD+0.310252*FF_WCR;
			else if(pt<40.000) return 0.547089*FF_QCD+0.452911*FF_WCR;
			else if(pt<45.000) return 0.621524*FF_QCD+0.378476*FF_WCR;
			else if(pt<50.000) return 0.470435*FF_QCD+0.529565*FF_WCR;
			else if(pt<60.000) return 0.399393*FF_QCD+0.600607*FF_WCR;
			else if(pt<80.000) return 0.422773*FF_QCD+0.577227*FF_WCR;
			else if(pt<100.000) return 0.687324*FF_QCD+0.312676*FF_WCR;
			else return 1.156497*FF_QCD+-0.156497*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.731221*FF_QCD+0.268779*FF_WCR;
			else if(pt<40.000) return 0.527894*FF_QCD+0.472106*FF_WCR;
			else if(pt<45.000) return 0.407217*FF_QCD+0.592783*FF_WCR;
			else if(pt<50.000) return 0.307881*FF_QCD+0.692119*FF_WCR;
			else if(pt<60.000) return 0.267588*FF_QCD+0.732412*FF_WCR;
			else if(pt<80.000) return 0.180521*FF_QCD+0.819479*FF_WCR;
			else if(pt<100.000) return 0.368156*FF_QCD+0.631844*FF_WCR;
			else return 0.831884*FF_QCD+0.168116*FF_WCR;
		}
	}
	if(idx==4){ //ttbar(ll) CR
		if(trk==1){
			if(pt<35.000) return 0.611468*FF_QCD+0.388532*FF_WCR;
			else if(pt<40.000) return 0.289872*FF_QCD+0.710128*FF_WCR;
			else if(pt<45.000) return 0.299417*FF_QCD+0.700583*FF_WCR;
			else if(pt<50.000) return 0.595615*FF_QCD+0.404385*FF_WCR;
			else if(pt<60.000) return 0.519627*FF_QCD+0.480373*FF_WCR;
			else if(pt<80.000) return 0.279111*FF_QCD+0.720889*FF_WCR;
			else if(pt<100.000) return 0.401251*FF_QCD+0.598749*FF_WCR;
			else return 1.029887*FF_QCD+-0.029887*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.126689*FF_QCD+0.873311*FF_WCR;
			else if(pt<40.000) return 0.121525*FF_QCD+0.878475*FF_WCR;
			else if(pt<45.000) return -0.068803*FF_QCD+1.068803*FF_WCR;
			else if(pt<50.000) return -0.045335*FF_QCD+1.045335*FF_WCR;
			else if(pt<60.000) return -0.046983*FF_QCD+1.046983*FF_WCR;
			else if(pt<80.000) return -0.031920*FF_QCD+1.031920*FF_WCR;
			else if(pt<100.000) return -0.152881*FF_QCD+1.152881*FF_WCR;
			else return 0.004919*FF_QCD+0.995081*FF_WCR;
		}
	}
	if(idx==5){ //#tau+lep Same-Sign SR
		if(trk==1){
			if(pt<35.000) return 0.357987*FF_QCD+0.642013*FF_WCR;
			else if(pt<40.000) return 0.534673*FF_QCD+0.465327*FF_WCR;
			else if(pt<45.000) return 0.436206*FF_QCD+0.563794*FF_WCR;
			else if(pt<50.000) return 0.388122*FF_QCD+0.611878*FF_WCR;
			else if(pt<60.000) return 0.376537*FF_QCD+0.623463*FF_WCR;
			else if(pt<80.000) return 0.482889*FF_QCD+0.517111*FF_WCR;
			else if(pt<100.000) return 0.941808*FF_QCD+0.058192*FF_WCR;
			else return 1.452882*FF_QCD+-0.452882*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.203002*FF_QCD+0.796998*FF_WCR;
			else if(pt<40.000) return 0.195423*FF_QCD+0.804577*FF_WCR;
			else if(pt<45.000) return 0.099918*FF_QCD+0.900082*FF_WCR;
			else if(pt<50.000) return 0.087555*FF_QCD+0.912445*FF_WCR;
			else if(pt<60.000) return 0.036984*FF_QCD+0.963016*FF_WCR;
			else if(pt<80.000) return 0.027728*FF_QCD+0.972272*FF_WCR;
			else if(pt<100.000) return 0.068418*FF_QCD+0.931582*FF_WCR;
			else return 0.200111*FF_QCD+0.799889*FF_WCR;
		}
	}
	if(idx==6){ //#tau+lep WZCR
		if(trk==1){
			if(pt<35.000) return 0.183815*FF_QCD+0.816185*FF_WCR;
			else if(pt<40.000) return 0.203969*FF_QCD+0.796031*FF_WCR;
			else if(pt<45.000) return 0.171718*FF_QCD+0.828282*FF_WCR;
			else if(pt<50.000) return 0.144410*FF_QCD+0.855590*FF_WCR;
			else if(pt<60.000) return 0.147944*FF_QCD+0.852056*FF_WCR;
			else if(pt<80.000) return 0.170043*FF_QCD+0.829957*FF_WCR;
			else if(pt<100.000) return 0.202939*FF_QCD+0.797061*FF_WCR;
			else return 0.244129*FF_QCD+0.755871*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.441074*FF_QCD+0.558926*FF_WCR;
			else if(pt<40.000) return 0.338539*FF_QCD+0.661461*FF_WCR;
			else if(pt<45.000) return 0.276561*FF_QCD+0.723439*FF_WCR;
			else if(pt<50.000) return 0.227930*FF_QCD+0.772070*FF_WCR;
			else if(pt<60.000) return 0.158939*FF_QCD+0.841061*FF_WCR;
			else if(pt<80.000) return 0.124773*FF_QCD+0.875227*FF_WCR;
			else if(pt<100.000) return 0.192995*FF_QCD+0.807005*FF_WCR;
			else return 0.321006*FF_QCD+0.678994*FF_WCR;
		}
	}
	if(idx==7){ //#tau+lep SR
		if(trk==1){
			if(pt<35.000) return -0.284434*FF_QCD+1.284434*FF_WCR;
			else if(pt<40.000) return -0.250225*FF_QCD+1.250225*FF_WCR;
			else if(pt<45.000) return -0.207083*FF_QCD+1.207083*FF_WCR;
			else if(pt<50.000) return -0.201670*FF_QCD+1.201670*FF_WCR;
			else if(pt<60.000) return -0.139029*FF_QCD+1.139029*FF_WCR;
			else if(pt<80.000) return -0.088531*FF_QCD+1.088531*FF_WCR;
			else if(pt<100.000) return -0.148078*FF_QCD+1.148078*FF_WCR;
			else return -0.418305*FF_QCD+1.418305*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return -0.128436*FF_QCD+1.128436*FF_WCR;
			else if(pt<40.000) return -0.135464*FF_QCD+1.135464*FF_WCR;
			else if(pt<45.000) return -0.141807*FF_QCD+1.141807*FF_WCR;
			else if(pt<50.000) return -0.134221*FF_QCD+1.134221*FF_WCR;
			else if(pt<60.000) return -0.093176*FF_QCD+1.093176*FF_WCR;
			else if(pt<80.000) return -0.064492*FF_QCD+1.064492*FF_WCR;
			else if(pt<100.000) return -0.119652*FF_QCD+1.119652*FF_WCR;
			else return 0.004919*FF_QCD+0.995081*FF_WCR;
		}
	}
	if(idx==8){ //WCR high MET
		if(trk==1){
			if(pt<35.000) return 0.369386*FF_QCD+0.630614*FF_WCR;
			else if(pt<40.000) return 0.368234*FF_QCD+0.631766*FF_WCR;
			else if(pt<45.000) return 0.245158*FF_QCD+0.754842*FF_WCR;
			else if(pt<50.000) return 0.245676*FF_QCD+0.754324*FF_WCR;
			else if(pt<60.000) return 0.342951*FF_QCD+0.657049*FF_WCR;
			else if(pt<80.000) return 0.248310*FF_QCD+0.751690*FF_WCR;
			else if(pt<100.000) return 0.660815*FF_QCD+0.339185*FF_WCR;
			else return 0.597886*FF_QCD+0.402114*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.687974*FF_QCD+0.312026*FF_WCR;
			else if(pt<40.000) return 0.607380*FF_QCD+0.392620*FF_WCR;
			else if(pt<45.000) return 0.517163*FF_QCD+0.482837*FF_WCR;
			else if(pt<50.000) return 0.430747*FF_QCD+0.569253*FF_WCR;
			else if(pt<60.000) return 0.287420*FF_QCD+0.712580*FF_WCR;
			else if(pt<80.000) return 0.223853*FF_QCD+0.776147*FF_WCR;
			else if(pt<100.000) return 0.313567*FF_QCD+0.686433*FF_WCR;
			else return 0.401214*FF_QCD+0.598786*FF_WCR;
		}
	}
}

