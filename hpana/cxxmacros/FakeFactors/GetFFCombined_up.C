#include <iostream>
using namespace std;

float GetFFCombined_up(float,int,float,float,int);

float GetFFCombined_up(float pt,int trk,float FF_QCD,float FF_WCR,int idx){
	if(idx==111) return FF_QCD;
	if(idx==222) return FF_WCR;
	if(idx==1){ //Preselection
		if(trk==1){
			if(pt<35.000) return 1.340899*FF_QCD+-0.340899*FF_WCR;
			else if(pt<40.000) return 1.273714*FF_QCD+-0.273714*FF_WCR;
			else if(pt<45.000) return 1.100915*FF_QCD+-0.100915*FF_WCR;
			else if(pt<50.000) return 1.117618*FF_QCD+-0.117618*FF_WCR;
			else if(pt<60.000) return 0.899087*FF_QCD+0.100913*FF_WCR;
			else if(pt<80.000) return 0.841769*FF_QCD+0.158231*FF_WCR;
			else if(pt<100.000) return 1.564273*FF_QCD+-0.564273*FF_WCR;
			else return 6.062097*FF_QCD+-5.062097*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 1.156869*FF_QCD+-0.156869*FF_WCR;
			else if(pt<40.000) return 1.007873*FF_QCD+-0.007873*FF_WCR;
			else if(pt<45.000) return 0.850583*FF_QCD+0.149417*FF_WCR;
			else if(pt<50.000) return 0.627736*FF_QCD+0.372264*FF_WCR;
			else if(pt<60.000) return 0.474648*FF_QCD+0.525352*FF_WCR;
			else if(pt<80.000) return 0.364384*FF_QCD+0.635616*FF_WCR;
			else if(pt<100.000) return 0.745247*FF_QCD+0.254753*FF_WCR;
			else return 1.444202*FF_QCD+-0.444202*FF_WCR;
		}
	}
	if(idx==2){ //hight MET b-veto
		if(trk==1){
			if(pt<35.000) return 1.891408*FF_QCD+-0.891408*FF_WCR;
			else if(pt<40.000) return 1.798233*FF_QCD+-0.798233*FF_WCR;
			else if(pt<45.000) return 1.403312*FF_QCD+-0.403312*FF_WCR;
			else if(pt<50.000) return 1.397320*FF_QCD+-0.397320*FF_WCR;
			else if(pt<60.000) return 1.182903*FF_QCD+-0.182903*FF_WCR;
			else if(pt<80.000) return 1.078899*FF_QCD+-0.078899*FF_WCR;
			else if(pt<100.000) return 2.031495*FF_QCD+-1.031495*FF_WCR;
			else return 5.955629*FF_QCD+-4.955629*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 1.197519*FF_QCD+-0.197519*FF_WCR;
			else if(pt<40.000) return 1.224127*FF_QCD+-0.224127*FF_WCR;
			else if(pt<45.000) return 1.091611*FF_QCD+-0.091611*FF_WCR;
			else if(pt<50.000) return 0.787996*FF_QCD+0.212004*FF_WCR;
			else if(pt<60.000) return 0.598442*FF_QCD+0.401558*FF_WCR;
			else if(pt<80.000) return 0.477154*FF_QCD+0.522846*FF_WCR;
			else if(pt<100.000) return 0.946543*FF_QCD+0.053457*FF_WCR;
			else return 1.427256*FF_QCD+-0.427256*FF_WCR;
		}
	}
	if(idx==3){ //#tau+jets SR
		if(trk==1){
			if(pt<35.000) return 1.261485*FF_QCD+-0.261485*FF_WCR;
			else if(pt<40.000) return 1.213184*FF_QCD+-0.213184*FF_WCR;
			else if(pt<45.000) return 1.010261*FF_QCD+-0.010261*FF_WCR;
			else if(pt<50.000) return 1.068369*FF_QCD+-0.068369*FF_WCR;
			else if(pt<60.000) return 0.830093*FF_QCD+0.169907*FF_WCR;
			else if(pt<80.000) return 0.766413*FF_QCD+0.233587*FF_WCR;
			else if(pt<100.000) return 1.516918*FF_QCD+-0.516918*FF_WCR;
			else return 2.189798*FF_QCD+-1.189798*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 1.113220*FF_QCD+-0.113220*FF_WCR;
			else if(pt<40.000) return 0.822508*FF_QCD+0.177492*FF_WCR;
			else if(pt<45.000) return 0.734230*FF_QCD+0.265770*FF_WCR;
			else if(pt<50.000) return 0.615094*FF_QCD+0.384906*FF_WCR;
			else if(pt<60.000) return 0.452974*FF_QCD+0.547026*FF_WCR;
			else if(pt<80.000) return 0.331602*FF_QCD+0.668398*FF_WCR;
			else if(pt<100.000) return 0.765187*FF_QCD+0.234813*FF_WCR;
			else return 1.675151*FF_QCD+-0.675151*FF_WCR;
		}
	}
	if(idx==4){ //ttbar(ll) CR
		if(trk==1){
			if(pt<35.000) return 1.614128*FF_QCD+-0.614128*FF_WCR;
			else if(pt<40.000) return 1.400682*FF_QCD+-0.400682*FF_WCR;
			else if(pt<45.000) return 1.581060*FF_QCD+-0.581060*FF_WCR;
			else if(pt<50.000) return 1.743647*FF_QCD+-0.743647*FF_WCR;
			else if(pt<60.000) return 1.750111*FF_QCD+-0.750111*FF_WCR;
			else if(pt<80.000) return 1.139328*FF_QCD+-0.139328*FF_WCR;
			else if(pt<100.000) return 2.455442*FF_QCD+-1.455442*FF_WCR;
			else return 4.336699*FF_QCD+-3.336699*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.642888*FF_QCD+0.357112*FF_WCR;
			else if(pt<40.000) return 0.677611*FF_QCD+0.322389*FF_WCR;
			else if(pt<45.000) return 0.331483*FF_QCD+0.668517*FF_WCR;
			else if(pt<50.000) return 0.288867*FF_QCD+0.711133*FF_WCR;
			else if(pt<60.000) return 0.188929*FF_QCD+0.811071*FF_WCR;
			else if(pt<80.000) return 0.271834*FF_QCD+0.728166*FF_WCR;
			else if(pt<100.000) return 0.343899*FF_QCD+0.656101*FF_WCR;
			else return 0.720546*FF_QCD+0.279454*FF_WCR;
		}
	}
	if(idx==5){ //#tau+lep Same-Sign SR
		if(trk==1){
			if(pt<35.000) return 1.236575*FF_QCD+-0.236575*FF_WCR;
			else if(pt<40.000) return 1.283335*FF_QCD+-0.283335*FF_WCR;
			else if(pt<45.000) return 1.418735*FF_QCD+-0.418735*FF_WCR;
			else if(pt<50.000) return 1.107776*FF_QCD+-0.107776*FF_WCR;
			else if(pt<60.000) return 1.090920*FF_QCD+-0.090920*FF_WCR;
			else if(pt<80.000) return 1.153128*FF_QCD+-0.153128*FF_WCR;
			else if(pt<100.000) return 2.461788*FF_QCD+-1.461788*FF_WCR;
			else return 5.026514*FF_QCD+-4.026514*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.559537*FF_QCD+0.440463*FF_WCR;
			else if(pt<40.000) return 0.561916*FF_QCD+0.438084*FF_WCR;
			else if(pt<45.000) return 0.424165*FF_QCD+0.575835*FF_WCR;
			else if(pt<50.000) return 0.403359*FF_QCD+0.596641*FF_WCR;
			else if(pt<60.000) return 0.246487*FF_QCD+0.753513*FF_WCR;
			else if(pt<80.000) return 0.224633*FF_QCD+0.775367*FF_WCR;
			else if(pt<100.000) return 0.497794*FF_QCD+0.502206*FF_WCR;
			else return 0.825223*FF_QCD+0.174777*FF_WCR;
		}
	}
	if(idx==6){ //#tau+lep WZCR
		if(trk==1){
			if(pt<35.000) return 0.434236*FF_QCD+0.565764*FF_WCR;
			else if(pt<40.000) return 0.487196*FF_QCD+0.512804*FF_WCR;
			else if(pt<45.000) return 0.357017*FF_QCD+0.642983*FF_WCR;
			else if(pt<50.000) return 0.349628*FF_QCD+0.650372*FF_WCR;
			else if(pt<60.000) return 0.309440*FF_QCD+0.690560*FF_WCR;
			else if(pt<80.000) return 0.311307*FF_QCD+0.688693*FF_WCR;
			else if(pt<100.000) return 0.485102*FF_QCD+0.514898*FF_WCR;
			else return 0.670086*FF_QCD+0.329914*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.788860*FF_QCD+0.211140*FF_WCR;
			else if(pt<40.000) return 0.523536*FF_QCD+0.476464*FF_WCR;
			else if(pt<45.000) return 0.440227*FF_QCD+0.559773*FF_WCR;
			else if(pt<50.000) return 0.389758*FF_QCD+0.610242*FF_WCR;
			else if(pt<60.000) return 0.242814*FF_QCD+0.757186*FF_WCR;
			else if(pt<80.000) return 0.192663*FF_QCD+0.807337*FF_WCR;
			else if(pt<100.000) return 0.374369*FF_QCD+0.625631*FF_WCR;
			else return 0.614339*FF_QCD+0.385661*FF_WCR;
		}
	}
	if(idx==7){ //#tau+lep SR
		if(trk==1){
			if(pt<35.000) return 0.022048*FF_QCD+0.977952*FF_WCR;
			else if(pt<40.000) return 0.010647*FF_QCD+0.989353*FF_WCR;
			else if(pt<45.000) return 0.016634*FF_QCD+0.983366*FF_WCR;
			else if(pt<50.000) return 0.025433*FF_QCD+0.974567*FF_WCR;
			else if(pt<60.000) return 0.069429*FF_QCD+0.930571*FF_WCR;
			else if(pt<80.000) return 0.058954*FF_QCD+0.941046*FF_WCR;
			else if(pt<100.000) return 0.204595*FF_QCD+0.795405*FF_WCR;
			else return 0.347183*FF_QCD+0.652817*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 0.149464*FF_QCD+0.850536*FF_WCR;
			else if(pt<40.000) return 0.083078*FF_QCD+0.916922*FF_WCR;
			else if(pt<45.000) return 0.054684*FF_QCD+0.945316*FF_WCR;
			else if(pt<50.000) return 0.029411*FF_QCD+0.970589*FF_WCR;
			else if(pt<60.000) return 0.016183*FF_QCD+0.983817*FF_WCR;
			else if(pt<80.000) return 0.066561*FF_QCD+0.933439*FF_WCR;
			else if(pt<100.000) return 0.161187*FF_QCD+0.838813*FF_WCR;
			else return 0.231469*FF_QCD+0.768531*FF_WCR;
		}
	}
	if(idx==8){ //WCR high MET
		if(trk==1){
			if(pt<35.000) return 0.769323*FF_QCD+0.230677*FF_WCR;
			else if(pt<40.000) return 0.839242*FF_QCD+0.160758*FF_WCR;
			else if(pt<45.000) return 0.782771*FF_QCD+0.217229*FF_WCR;
			else if(pt<50.000) return 0.760629*FF_QCD+0.239371*FF_WCR;
			else if(pt<60.000) return 0.688546*FF_QCD+0.311454*FF_WCR;
			else if(pt<80.000) return 0.648155*FF_QCD+0.351845*FF_WCR;
			else if(pt<100.000) return 1.577435*FF_QCD+-0.577435*FF_WCR;
			else return 1.825309*FF_QCD+-0.825309*FF_WCR;
		}
		else if(trk==3){
			if(pt<35.000) return 1.307945*FF_QCD+-0.307945*FF_WCR;
			else if(pt<40.000) return 1.059964*FF_QCD+-0.059964*FF_WCR;
			else if(pt<45.000) return 1.011671*FF_QCD+-0.011671*FF_WCR;
			else if(pt<50.000) return 0.840922*FF_QCD+0.159078*FF_WCR;
			else if(pt<60.000) return 0.489375*FF_QCD+0.510625*FF_WCR;
			else if(pt<80.000) return 0.394145*FF_QCD+0.605855*FF_WCR;
			else if(pt<100.000) return 0.669057*FF_QCD+0.330943*FF_WCR;
			else return 0.878778*FF_QCD+0.121222*FF_WCR;
		}
	}
}

