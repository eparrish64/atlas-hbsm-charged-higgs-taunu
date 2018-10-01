float metTrigEff(float met_et, int variation_index){
	 //! variation: MET_TRIG_EFF_CR_NOMINAL
	 if(variation_index==1000){
       return 0.6221 * (0.489660682215*(1 + TMath::Erf((met_et - 132.947994324)/47.1720112071))+0.00192670407796) + 0.0723 * (0.48838858126*(1 + TMath::Erf((met_et - 126.020652696)/46.3381518502))+0.00439447012308) + 0.1411 * (0.49103485396*(1 + TMath::Erf((met_et - 132.343960195)/43.4659400839))+0.00153354965639) + 0.1645 * (0.468634509449*(1 + TMath::Erf((met_et - 115.268467297)/49.6408688836))+0.000477362508121);	}

     else return 1;
}
