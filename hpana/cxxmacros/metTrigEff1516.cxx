float metTrigEff(float met_et, int variation_index){
	 //! variation: MET_TRIG_EFF_CR_NOMINAL
	 if(variation_index==1000){
		 return 0.0897 * (0.468568141859*(1 + TMath::Erf((met_et - 99.1777030533)/47.6745655326))+0.00264935822853) + 0.1712 * (0.482141973762*(1 + TMath::Erf((met_et - 101.960283026)/48.7143787684))+0.00312914569187) + 0.7390 * (0.487783466476*(1 + TMath::Erf((met_et - 124.948617985)/45.6712595811))+0.00145465832202);	}

	 //! variation: MET_TRIG_EFF_CR_TAU_ID_MED
	 if(variation_index==1001){
		 return 0.0897 * (0.455284139645*(1 + TMath::Erf((met_et - 94.4339044352)/44.1710232413))+0.00477012825842) + 0.1712 * (0.482063448981*(1 + TMath::Erf((met_et - 100.704745354)/47.6633366058))+0.00303765947094) + 0.7390 * (0.496867616574*(1 + TMath::Erf((met_et - 124.952383453)/46.2740566014))+0.000568230011911);	}

	 //! variation: MET_TRIG_EFF_CR_TAU_ID_TIGHT
	 if(variation_index==1002){
		 return 0.0897 * (0.484269677875*(1 + TMath::Erf((met_et - 95.4733684004)/46.8996714405))+-0.00208723836659) + 0.1712 * (0.469456128109*(1 + TMath::Erf((met_et - 98.2550811338)/46.1096572333))+0.00237122141367) + 0.7390 * (0.493749073764*(1 + TMath::Erf((met_et - 123.623630086)/45.2720789223))+0.000388903326961);	}

	 //! variation: MET_TRIG_EFF_CR_EL_ID_MED
	 if(variation_index==1003){
		 return 0.0897 * (0.469815758617*(1 + TMath::Erf((met_et - 99.249586906)/48.0893727428))+0.00154253886497) + 0.1712 * (0.484588778913*(1 + TMath::Erf((met_et - 102.303490334)/49.3032915563))+0.00226955176933) + 0.7390 * (0.4873049221*(1 + TMath::Erf((met_et - 124.873957614)/45.6413726664))+0.00147027566009);	}

	 //! variation: MET_TRIG_EFF_CR_EL_ID_TIGHT
	 if(variation_index==1004){
		 return 0.0897 * (0.467327307121*(1 + TMath::Erf((met_et - 98.627362546)/47.6688444891))+0.00216771987634) + 0.1712 * (0.481803779362*(1 + TMath::Erf((met_et - 101.857442534)/48.9647680568))+0.00250720624127) + 0.7390 * (0.486662301403*(1 + TMath::Erf((met_et - 124.730672641)/45.544377909))+0.00150856662841);	}

	 //! variation: MET_TRIG_EFF_CR_NJETS3
	 if(variation_index==1005){
		 return 0.0897 * (0.474473226103*(1 + TMath::Erf((met_et - 101.29045723)/51.5354004317))+-0.00373649760628) + 0.1712 * (0.473552866867*(1 + TMath::Erf((met_et - 103.863434705)/49.3731005893))+0.00697029144334) + 0.7390 * (0.487895450028*(1 + TMath::Erf((met_et - 127.940475352)/47.105730183))+0.00224445600967);	}

	else 
 return 1.; 
}