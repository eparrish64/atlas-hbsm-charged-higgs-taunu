#include <iostream>
//! 1down 
float GetFF_FF_CR_WJETS_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.161142;
		 if(pt < 40) return 0.149530;
		 if(pt < 45) return 0.134366;
		 if(pt < 50) return 0.121102;
		 if(pt < 60) return 0.117098;
		 if(pt < 80) return 0.097441;
		 if(pt < 100) return 0.089742;
		 if(pt < 200) return 0.075279;
		 if(pt < 3500) return 0.073213;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032572;
		 if(pt < 40) return 0.029865;
		 if(pt < 60) return 0.022217;
		 if(pt < 80) return 0.015774;
		 if(pt < 100) return 0.012559;
		 if(pt < 3500) return 0.011762;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_WJETS_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.161142;
		 if(pt < 40) return 0.149530;
		 if(pt < 45) return 0.134366;
		 if(pt < 50) return 0.121102;
		 if(pt < 60) return 0.117098;
		 if(pt < 80) return 0.097441;
		 if(pt < 100) return 0.089742;
		 if(pt < 200) return 0.075279;
		 if(pt < 3500) return 0.073213;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032572;
		 if(pt < 40) return 0.029865;
		 if(pt < 60) return 0.022217;
		 if(pt < 80) return 0.015774;
		 if(pt < 100) return 0.012559;
		 if(pt < 3500) return 0.011762;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_WJETS_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.161142;
		 if(pt < 40) return 0.149530;
		 if(pt < 45) return 0.134366;
		 if(pt < 50) return 0.121102;
		 if(pt < 60) return 0.117098;
		 if(pt < 80) return 0.097441;
		 if(pt < 100) return 0.089742;
		 if(pt < 200) return 0.075279;
		 if(pt < 3500) return 0.073213;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.032572;
		 if(pt < 40) return 0.029865;
		 if(pt < 60) return 0.022217;
		 if(pt < 80) return 0.015774;
		 if(pt < 100) return 0.012559;
		 if(pt < 3500) return 0.011762;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_WJETS_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1569;
		 if(pt < 40) return 0.1455;
		 if(pt < 45) return 0.1293;
		 if(pt < 50) return 0.1175;
		 if(pt < 60) return 0.1134;
		 if(pt < 80) return 0.0940;
		 if(pt < 100) return 0.0865;
		 if(pt < 200) return 0.0723;
		 if(pt < 3500) return 0.0704;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0318;
		 if(pt < 40) return 0.0291;
		 if(pt < 60) return 0.0215;
		 if(pt < 80) return 0.0152;
		 if(pt < 100) return 0.0120;
		 if(pt < 3500) return 0.0113;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_WJETS_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1656;
		 if(pt < 40) return 0.1538;
		 if(pt < 45) return 0.1398;
		 if(pt < 50) return 0.1249;
		 if(pt < 60) return 0.1210;
		 if(pt < 80) return 0.1011;
		 if(pt < 100) return 0.0932;
		 if(pt < 200) return 0.0785;
		 if(pt < 3500) return 0.0763;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0334;
		 if(pt < 40) return 0.0307;
		 if(pt < 60) return 0.0230;
		 if(pt < 80) return 0.0164;
		 if(pt < 100) return 0.0131;
		 if(pt < 3500) return 0.0123;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1up 
float GetFF_FF_CR_WJETS_tauID_SF_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1631;
		 if(pt < 40) return 0.1517;
		 if(pt < 45) return 0.1371;
		 if(pt < 50) return 0.1239;
		 if(pt < 60) return 0.1198;
		 if(pt < 80) return 0.1004;
		 if(pt < 100) return 0.0928;
		 if(pt < 200) return 0.0788;
		 if(pt < 3500) return 0.0756;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0329;
		 if(pt < 40) return 0.0302;
		 if(pt < 60) return 0.0227;
		 if(pt < 80) return 0.0165;
		 if(pt < 100) return 0.0134;
		 if(pt < 3500) return 0.0126;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1down 
float GetFF_FF_CR_WJETS_tauID_SF_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1592;
		 if(pt < 40) return 0.1474;
		 if(pt < 45) return 0.1316;
		 if(pt < 50) return 0.1183;
		 if(pt < 60) return 0.1144;
		 if(pt < 80) return 0.0945;
		 if(pt < 100) return 0.0867;
		 if(pt < 200) return 0.0718;
		 if(pt < 3500) return 0.0709;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0322;
		 if(pt < 40) return 0.0295;
		 if(pt < 60) return 0.0217;
		 if(pt < 80) return 0.0151;
		 if(pt < 100) return 0.0117;
		 if(pt < 3500) return 0.0109;
		 else return 0;
		 }
	 else return 0;
}


//! STAT_1up 
float GetFF_FF_CR_WJETS_STAT_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.163279;
		 if(pt < 40) return 0.152216;
		 if(pt < 45) return 0.137949;
		 if(pt < 50) return 0.125065;
		 if(pt < 60) return 0.120249;
		 if(pt < 80) return 0.100282;
		 if(pt < 100) return 0.097161;
		 if(pt < 200) return 0.079473;
		 if(pt < 3500) return 0.085032;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.033295;
		 if(pt < 40) return 0.030693;
		 if(pt < 60) return 0.022894;
		 if(pt < 80) return 0.016690;
		 if(pt < 100) return 0.013954;
		 if(pt < 3500) return 0.013144;
		 else return 0;
		 }
	 else return 0;
}


//! STAT_1down 
float GetFF_FF_CR_WJETS_STAT_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.159005;
		 if(pt < 40) return 0.146845;
		 if(pt < 45) return 0.130783;
		 if(pt < 50) return 0.117140;
		 if(pt < 60) return 0.113948;
		 if(pt < 80) return 0.094600;
		 if(pt < 100) return 0.082324;
		 if(pt < 200) return 0.071085;
		 if(pt < 3500) return 0.061395;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.031850;
		 if(pt < 40) return 0.029037;
		 if(pt < 60) return 0.021540;
		 if(pt < 80) return 0.014858;
		 if(pt < 100) return 0.011163;
		 if(pt < 3500) return 0.010381;
		 else return 0;
		 }
	 else return 0;
}


//! 1down 
float GetFF_FF_CR_MULTIJET_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.130342;
		 if(pt < 40) return 0.117221;
		 if(pt < 45) return 0.093677;
		 if(pt < 50) return 0.083563;
		 if(pt < 60) return 0.084582;
		 if(pt < 80) return 0.078049;
		 if(pt < 100) return 0.070303;
		 if(pt < 200) return 0.061811;
		 if(pt < 3500) return 0.043814;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023683;
		 if(pt < 40) return 0.020147;
		 if(pt < 60) return 0.011982;
		 if(pt < 80) return 0.011188;
		 if(pt < 100) return 0.009033;
		 if(pt < 3500) return 0.007792;
		 else return 0;
		 }
	 else return 0;
}


//! 1up 
float GetFF_FF_CR_MULTIJET_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.130342;
		 if(pt < 40) return 0.117221;
		 if(pt < 45) return 0.093677;
		 if(pt < 50) return 0.083563;
		 if(pt < 60) return 0.084582;
		 if(pt < 80) return 0.078049;
		 if(pt < 100) return 0.070303;
		 if(pt < 200) return 0.061811;
		 if(pt < 3500) return 0.043814;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023683;
		 if(pt < 40) return 0.020147;
		 if(pt < 60) return 0.011982;
		 if(pt < 80) return 0.011188;
		 if(pt < 100) return 0.009033;
		 if(pt < 3500) return 0.007792;
		 else return 0;
		 }
	 else return 0;
}


//! NOMINAL 
float GetFF_FF_CR_MULTIJET_NOMINAL(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.130342;
		 if(pt < 40) return 0.117221;
		 if(pt < 45) return 0.093677;
		 if(pt < 50) return 0.083563;
		 if(pt < 60) return 0.084582;
		 if(pt < 80) return 0.078049;
		 if(pt < 100) return 0.070303;
		 if(pt < 200) return 0.061811;
		 if(pt < 3500) return 0.043814;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023683;
		 if(pt < 40) return 0.020147;
		 if(pt < 60) return 0.011982;
		 if(pt < 80) return 0.011188;
		 if(pt < 100) return 0.009033;
		 if(pt < 3500) return 0.007792;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1up 
float GetFF_FF_CR_MULTIJET_MCSubt_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1303;
		 if(pt < 40) return 0.1172;
		 if(pt < 45) return 0.0936;
		 if(pt < 50) return 0.0835;
		 if(pt < 60) return 0.0845;
		 if(pt < 80) return 0.0780;
		 if(pt < 100) return 0.0702;
		 if(pt < 200) return 0.0617;
		 if(pt < 3500) return 0.0438;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0237;
		 if(pt < 40) return 0.0201;
		 if(pt < 60) return 0.0120;
		 if(pt < 80) return 0.0112;
		 if(pt < 100) return 0.0090;
		 if(pt < 3500) return 0.0078;
		 else return 0;
		 }
	 else return 0;
}


//! MCSubt_1down 
float GetFF_FF_CR_MULTIJET_MCSubt_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1304;
		 if(pt < 40) return 0.1173;
		 if(pt < 45) return 0.0937;
		 if(pt < 50) return 0.0836;
		 if(pt < 60) return 0.0847;
		 if(pt < 80) return 0.0781;
		 if(pt < 100) return 0.0704;
		 if(pt < 200) return 0.0619;
		 if(pt < 3500) return 0.0439;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0237;
		 if(pt < 40) return 0.0202;
		 if(pt < 60) return 0.0120;
		 if(pt < 80) return 0.0112;
		 if(pt < 100) return 0.0090;
		 if(pt < 3500) return 0.0078;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1up 
float GetFF_FF_CR_MULTIJET_tauID_SF_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1305;
		 if(pt < 40) return 0.1174;
		 if(pt < 45) return 0.0939;
		 if(pt < 50) return 0.0837;
		 if(pt < 60) return 0.0848;
		 if(pt < 80) return 0.0783;
		 if(pt < 100) return 0.0707;
		 if(pt < 200) return 0.0622;
		 if(pt < 3500) return 0.0441;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0237;
		 if(pt < 40) return 0.0202;
		 if(pt < 60) return 0.0120;
		 if(pt < 80) return 0.0113;
		 if(pt < 100) return 0.0092;
		 if(pt < 3500) return 0.0079;
		 else return 0;
		 }
	 else return 0;
}


//! tauID_SF_1down 
float GetFF_FF_CR_MULTIJET_tauID_SF_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.1302;
		 if(pt < 40) return 0.1171;
		 if(pt < 45) return 0.0935;
		 if(pt < 50) return 0.0834;
		 if(pt < 60) return 0.0844;
		 if(pt < 80) return 0.0778;
		 if(pt < 100) return 0.0699;
		 if(pt < 200) return 0.0614;
		 if(pt < 3500) return 0.0435;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.0237;
		 if(pt < 40) return 0.0201;
		 if(pt < 60) return 0.0119;
		 if(pt < 80) return 0.0111;
		 if(pt < 100) return 0.0089;
		 if(pt < 3500) return 0.0077;
		 else return 0;
		 }
	 else return 0;
}


//! STAT_1up 
float GetFF_FF_CR_MULTIJET_STAT_1up(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.131555;
		 if(pt < 40) return 0.118623;
		 if(pt < 45) return 0.094931;
		 if(pt < 50) return 0.084704;
		 if(pt < 60) return 0.085339;
		 if(pt < 80) return 0.078605;
		 if(pt < 100) return 0.070950;
		 if(pt < 200) return 0.062242;
		 if(pt < 3500) return 0.044401;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.024140;
		 if(pt < 40) return 0.020679;
		 if(pt < 60) return 0.012195;
		 if(pt < 80) return 0.011379;
		 if(pt < 100) return 0.009253;
		 if(pt < 3500) return 0.007912;
		 else return 0;
		 }
	 else return 0;
}


//! STAT_1down 
float GetFF_FF_CR_MULTIJET_STAT_1down(float pt, int nTracks){
	 if(nTracks==1){
		 if(pt < 35) return 0.129130;
		 if(pt < 40) return 0.115820;
		 if(pt < 45) return 0.092424;
		 if(pt < 50) return 0.082421;
		 if(pt < 60) return 0.083825;
		 if(pt < 80) return 0.077493;
		 if(pt < 100) return 0.069656;
		 if(pt < 200) return 0.061380;
		 if(pt < 3500) return 0.043227;
		 else return 0;
		 }
	 if(nTracks==3){
		 if(pt < 35) return 0.023227;
		 if(pt < 40) return 0.019614;
		 if(pt < 60) return 0.011769;
		 if(pt < 80) return 0.010997;
		 if(pt < 100) return 0.008812;
		 if(pt < 3500) return 0.007672;
		 else return 0;
		 }
	 else return 0;
}
