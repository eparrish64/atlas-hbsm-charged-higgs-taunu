#include <iostream>
using namespace std;

float GetFFCombined_dn(float,int,float,float,int);

float GetFFCombined_dn(float pt,int trk,float FF_QCD,float FF_WCR,int idx){
	if(idx==111) return FF_QCD;
	if(idx==222) return FF_WCR;
	if(idx==1){ //Preselection
		if(trk==1){
			if(pt<35.000) return 0.869393*FF_QCD+0.130607*FF_WCR;
			else if(pt<40.000) return 0.675422*FF_QCD+0.324578*FF_WCR;
			else if(pt<45.000) return 0.595824*FF_QCD+0.404176*FF_WCR;
			else if(pt<50.000) return 0.422890*FF_QCD+0.577110*FF_WCR;
			else if(pt<60.000) return 0.354055*FF_QCD+0.645945*FF_WCR;
			else if(pt<80.000) return 0.388060*FF_QCD+0.611940*FF_WCR;
			else if(pt<100.000) return 0.595971*FF_QCD+0.404029*FF_WCR;
			else return 1.346695*FF_QCD+-0.346695*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.731221*FF_QCD+0.268779*FF_WCR;
			else if(pt<40.000) return 0.502501*FF_QCD+0.497499*FF_WCR;
			else if(pt<45.000) return 0.418891*FF_QCD+0.581109*FF_WCR;
			else if(pt<50.000) return 0.297484*FF_QCD+0.702516*FF_WCR;
			else if(pt<60.000) return 0.238818*FF_QCD+0.761182*FF_WCR;
			else if(pt<80.000) return 0.197480*FF_QCD+0.802520*FF_WCR;
			else if(pt<100.000) return 0.345990*FF_QCD+0.654010*FF_WCR;
			else return 0.671539*FF_QCD+0.328461*FF_WCR;
		}
	}
	if(idx==2){ //hight MET b-veto
		if(trk==1){
			if(pt<35.000) return 0.987364*FF_QCD+0.012636*FF_WCR;
			else if(pt<40.000) return 0.756250*FF_QCD+0.243750*FF_WCR;
			else if(pt<45.000) return 0.595824*FF_QCD+0.404176*FF_WCR;
			else if(pt<50.000) return 0.557074*FF_QCD+0.442926*FF_WCR;
			else if(pt<60.000) return 0.376537*FF_QCD+0.623463*FF_WCR;
			else if(pt<80.000) return 0.399522*FF_QCD+0.600478*FF_WCR;
			else if(pt<100.000) return 0.595971*FF_QCD+0.404029*FF_WCR;
			else return 1.755409*FF_QCD+-0.755409*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.790932*FF_QCD+0.209068*FF_WCR;
			else if(pt<40.000) return 0.580316*FF_QCD+0.419684*FF_WCR;
			else if(pt<45.000) return 0.517163*FF_QCD+0.482837*FF_WCR;
			else if(pt<50.000) return 0.361729*FF_QCD+0.638271*FF_WCR;
			else if(pt<60.000) return 0.267588*FF_QCD+0.732412*FF_WCR;
			else if(pt<80.000) return 0.242092*FF_QCD+0.757908*FF_WCR;
			else if(pt<100.000) return 0.437449*FF_QCD+0.562551*FF_WCR;
			else return 0.790877*FF_QCD+0.209123*FF_WCR;
		}
	}
	if(idx==3){ //#tau+jets SR
		if(trk==1){
			if(pt<35.000) return 0.415626*FF_QCD+0.584374*FF_WCR;
			else if(pt<40.000) return 0.246448*FF_QCD+0.753552*FF_WCR;
			else if(pt<45.000) return 0.436206*FF_QCD+0.563794*FF_WCR;
			else if(pt<50.000) return 0.204353*FF_QCD+0.795647*FF_WCR;
			else if(pt<60.000) return 0.206426*FF_QCD+0.793574*FF_WCR;
			else if(pt<80.000) return 0.268752*FF_QCD+0.731248*FF_WCR;
			else if(pt<100.000) return 0.299545*FF_QCD+0.700455*FF_WCR;
			else return 0.672890*FF_QCD+0.327110*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.552566*FF_QCD+0.447434*FF_WCR;
			else if(pt<40.000) return 0.383069*FF_QCD+0.616931*FF_WCR;
			else if(pt<45.000) return 0.256347*FF_QCD+0.743653*FF_WCR;
			else if(pt<50.000) return 0.172467*FF_QCD+0.827533*FF_WCR;
			else if(pt<60.000) return 0.175908*FF_QCD+0.824092*FF_WCR;
			else if(pt<80.000) return 0.109801*FF_QCD+0.890199*FF_WCR;
			else if(pt<100.000) return 0.192995*FF_QCD+0.807005*FF_WCR;
			else return 0.436408*FF_QCD+0.563592*FF_WCR;
		}
	}
	if(idx==4){ //ttbar(ll) CR
		if(trk==1){
			if(pt<35.000) return 0.173419*FF_QCD+0.826581*FF_WCR;
			else if(pt<40.000) return -0.183509*FF_QCD+1.183509*FF_WCR;
			else if(pt<45.000) return -0.248059*FF_QCD+1.248059*FF_WCR;
			else if(pt<50.000) return 0.115319*FF_QCD+0.884681*FF_WCR;
			else if(pt<60.000) return 0.029911*FF_QCD+0.970089*FF_WCR;
			else if(pt<80.000) return -0.073691*FF_QCD+1.073691*FF_WCR;
			else if(pt<100.000) return -0.380471*FF_QCD+1.380471*FF_WCR;
			else return -0.305432*FF_QCD+1.305432*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return -0.098690*FF_QCD+1.098690*FF_WCR;
			else if(pt<40.000) return -0.114815*FF_QCD+1.114815*FF_WCR;
			else if(pt<45.000) return -0.248104*FF_QCD+1.248104*FF_WCR;
			else if(pt<50.000) return -0.196769*FF_QCD+1.196769*FF_WCR;
			else if(pt<60.000) return -0.125444*FF_QCD+1.125444*FF_WCR;
			else if(pt<80.000) return -0.171342*FF_QCD+1.171342*FF_WCR;
			else if(pt<100.000) return -0.245244*FF_QCD+1.245244*FF_WCR;
			else return -0.004908*FF_QCD+1.004908*FF_WCR;
		}
	}
	if(idx==5){ //#tau+lep Same-Sign SR
		if(trk==1){
			if(pt<35.000) return -0.023529*FF_QCD+1.023529*FF_WCR;
			else if(pt<40.000) return 0.193493*FF_QCD+0.806507*FF_WCR;
			else if(pt<45.000) return 0.004686*FF_QCD+0.995314*FF_WCR;
			else if(pt<50.000) return 0.068081*FF_QCD+0.931919*FF_WCR;
			else if(pt<60.000) return 0.065033*FF_QCD+0.934967*FF_WCR;
			else if(pt<80.000) return 0.179532*FF_QCD+0.820468*FF_WCR;
			else if(pt<100.000) return 0.299545*FF_QCD+0.700455*FF_WCR;
			else return 0.047480*FF_QCD+0.952520*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.037823*FF_QCD+0.962177*FF_WCR;
			else if(pt<40.000) return 0.027985*FF_QCD+0.972015*FF_WCR;
			else if(pt<45.000) return -0.047686*FF_QCD+1.047686*FF_WCR;
			else if(pt<50.000) return -0.058737*FF_QCD+1.058737*FF_WCR;
			else if(pt<60.000) return -0.058892*FF_QCD+1.058892*FF_WCR;
			else if(pt<80.000) return -0.064492*FF_QCD+1.064492*FF_WCR;
			else if(pt<100.000) return -0.126403*FF_QCD+1.126403*FF_WCR;
			else return -0.004908*FF_QCD+1.004908*FF_WCR;
		}
	}
	if(idx==6){ //#tau+lep WZCR
		if(trk==1){
			if(pt<35.000) return 0.062591*FF_QCD+0.937409*FF_WCR;
			else if(pt<40.000) return 0.062301*FF_QCD+0.937699*FF_WCR;
			else if(pt<45.000) return 0.081378*FF_QCD+0.918622*FF_WCR;
			else if(pt<50.000) return 0.040459*FF_QCD+0.959541*FF_WCR;
			else if(pt<60.000) return 0.065033*FF_QCD+0.934967*FF_WCR;
			else if(pt<80.000) return 0.096961*FF_QCD+0.903039*FF_WCR;
			else if(pt<100.000) return 0.061931*FF_QCD+0.938069*FF_WCR;
			else return 0.026297*FF_QCD+0.973703*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.284463*FF_QCD+0.715537*FF_WCR;
			else if(pt<40.000) return 0.244399*FF_QCD+0.755601*FF_WCR;
			else if(pt<45.000) return 0.198118*FF_QCD+0.801882*FF_WCR;
			else if(pt<50.000) return 0.146053*FF_QCD+0.853947*FF_WCR;
			else if(pt<60.000) return 0.118303*FF_QCD+0.881697*FF_WCR;
			else if(pt<80.000) return 0.088076*FF_QCD+0.911924*FF_WCR;
			else if(pt<100.000) return 0.111109*FF_QCD+0.888891*FF_WCR;
			else return 0.178776*FF_QCD+0.821224*FF_WCR;
		}
	}
	if(idx==7){ //#tau+lep SR
		if(trk==1){
			if(pt<35.000) return -0.438955*FF_QCD+1.438955*FF_WCR;
			else if(pt<40.000) return -0.383825*FF_QCD+1.383825*FF_WCR;
			else if(pt<45.000) return -0.319334*FF_QCD+1.319334*FF_WCR;
			else if(pt<50.000) return -0.325490*FF_QCD+1.325490*FF_WCR;
			else if(pt<60.000) return -0.245838*FF_QCD+1.245838*FF_WCR;
			else if(pt<80.000) return -0.159486*FF_QCD+1.159486*FF_WCR;
			else if(pt<100.000) return -0.319591*FF_QCD+1.319591*FF_WCR;
			else return -0.873786*FF_QCD+1.873786*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return -0.265435*FF_QCD+1.265435*FF_WCR;
			else if(pt<40.000) return -0.238042*FF_QCD+1.238042*FF_WCR;
			else if(pt<45.000) return -0.237017*FF_QCD+1.237017*FF_WCR;
			else if(pt<50.000) return -0.202172*FF_QCD+1.202172*FF_WCR;
			else if(pt<60.000) return -0.125444*FF_QCD+1.125444*FF_WCR;
			else if(pt<80.000) return -0.128047*FF_QCD+1.128047*FF_WCR;
			else if(pt<100.000) return -0.245244*FF_QCD+1.245244*FF_WCR;
			else return -0.004908*FF_QCD+1.004908*FF_WCR;
		}
	}
	if(idx==8){ //WCR high MET
		if(trk==1){
			if(pt<35.000) return 0.173419*FF_QCD+0.826581*FF_WCR;
			else if(pt<40.000) return 0.152151*FF_QCD+0.847849*FF_WCR;
			else if(pt<45.000) return -0.004673*FF_QCD+1.004673*FF_WCR;
			else if(pt<50.000) return 0.004439*FF_QCD+0.995561*FF_WCR;
			else if(pt<60.000) return 0.186633*FF_QCD+0.813367*FF_WCR;
			else if(pt<80.000) return 0.070787*FF_QCD+0.929213*FF_WCR;
			else if(pt<100.000) return 0.245270*FF_QCD+0.754730*FF_WCR;
			else return 0.015754*FF_QCD+0.984246*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.382936*FF_QCD+0.617064*FF_WCR;
			else if(pt<40.000) return 0.394478*FF_QCD+0.605522*FF_WCR;
			else if(pt<45.000) return 0.297198*FF_QCD+0.702802*FF_WCR;
			else if(pt<50.000) return 0.247246*FF_QCD+0.752754*FF_WCR;
			else if(pt<60.000) return 0.193310*FF_QCD+0.806690*FF_WCR;
			else if(pt<80.000) return 0.140156*FF_QCD+0.859844*FF_WCR;
			else if(pt<100.000) return 0.155764*FF_QCD+0.844236*FF_WCR;
			else return 0.168180*FF_QCD+0.831820*FF_WCR;
		}
	}
}

