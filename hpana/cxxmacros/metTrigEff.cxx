//   CAREFUL!  This is a MonteCarlo Scale Factor data file!
//             Use together with MC trigger decision!
float metTrigEff(float met_et, int variation_index, int run_number){
	 //! variation: MET_TRIG_EFF_CR_NOM
	 if(variation_index==1000){
		 // year: 2015 
		 // trigger: HLT_xe70_mht 
		 if(run_number >= 266904 && run_number <= 284484){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 93.0619538268)/55.6366810686))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 89.5590553282)/56.8194688873))+0.0); 

		 }
		 // year: 2017 
		 // trigger: HLT_xe110_pufit_L1XE50 
		 if(run_number >= 332303 && run_number <= 341649){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.350368777)/56.8400167879))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.249355406)/51.5178628873))+0.0); 

		 }
		 // trigger: HLT_xe110_pufit_L1XE55 
		 if(run_number >= 325713 && run_number <= 331975){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 132.006938735)/47.2507697777))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.749887552)/51.0437616734))+0.0); 

		 }
		 // year: 2016 
		 // trigger: HLT_xe90_mht_L1XE50 
		 if(run_number >= 296939 && run_number <= 302872){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 103.348990165)/56.3107160114))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 94.6923317174)/51.6202343985))+0.0); 

		 }
		 // trigger: HLT_xe110_mht_L1XE50 
		 if(run_number >= 302873 && run_number <= 311481){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 125.234878112)/48.7740968647))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 120.410325866)/49.3915368169))+0.0); 

		 }
		 // year: 2018 
		 // trigger: HLT_xe110_pufit_xe70_L1XE50 
		 if(run_number >= 348885 && run_number <= 364485){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.61670811)/51.6018951346))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 132.435817256)/50.7042552106))+0.0); 

		 }

		 else return 0.;
	}

	 //! variation: MET_TRIG_EFF_CR_TAUID_MED
	 if(variation_index==1001){
		 // year: 2015 
		 // trigger: HLT_xe70_mht 
		 if(run_number >= 266904 && run_number <= 284484){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 91.303757767)/52.8982128111))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 88.688123153)/55.4032606324))+0.0); 

		 }
		 // year: 2017 
		 // trigger: HLT_xe110_pufit_L1XE50 
		 if(run_number >= 332303 && run_number <= 341649){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 134.475124233)/54.9562948133))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.10814207)/51.2469290957))+0.0); 

		 }
		 // trigger: HLT_xe110_pufit_L1XE55 
		 if(run_number >= 325713 && run_number <= 331975){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 131.334583273)/47.5411325382))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.60370124)/50.423668327))+0.0); 

		 }
		 // year: 2016 
		 // trigger: HLT_xe90_mht_L1XE50 
		 if(run_number >= 296939 && run_number <= 302872){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 100.97632858)/57.1622166401))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 94.863372632)/51.4470426807))+0.0); 

		 }
		 // trigger: HLT_xe110_mht_L1XE50 
		 if(run_number >= 302873 && run_number <= 311481){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 125.534627623)/47.0268033264))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 120.34799564)/49.4545641793))+0.0); 

		 }
		 // year: 2018 
		 // trigger: HLT_xe110_pufit_xe70_L1XE50 
		 if(run_number >= 348885 && run_number <= 364485){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 134.342266553)/51.3253186459))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 132.193363806)/50.0839453327))+0.0); 

		 }

		 else return 0.;
	}

	 //! variation: MET_TRIG_EFF_CR_TAUID_TIGHT
	 if(variation_index==1002){
		 // year: 2015 
		 // trigger: HLT_xe70_mht 
		 if(run_number >= 266904 && run_number <= 284484){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 92.0254713627)/53.5500931898))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 89.2749953931)/56.3789836775))+0.0); 

		 }
		 // year: 2017 
		 // trigger: HLT_xe110_pufit_L1XE50 
		 if(run_number >= 332303 && run_number <= 341649){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.359484838)/56.8402750904))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 128.646684151)/50.3209622521))+0.0); 

		 }
		 // trigger: HLT_xe110_pufit_L1XE55 
		 if(run_number >= 325713 && run_number <= 331975){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 133.141197399)/50.342657233))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 130.177786768)/51.3808901105))+0.0); 

		 }
		 // year: 2016 
		 // trigger: HLT_xe90_mht_L1XE50 
		 if(run_number >= 296939 && run_number <= 302872){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 99.7712927607)/56.7239608431))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 94.5135107914)/52.2392003706))+0.0); 

		 }
		 // trigger: HLT_xe110_mht_L1XE50 
		 if(run_number >= 302873 && run_number <= 311481){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 124.787973884)/47.8773406565))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 120.182349616)/49.5474751025))+0.0); 

		 }
		 // year: 2018 
		 // trigger: HLT_xe110_pufit_xe70_L1XE50 
		 if(run_number >= 348885 && run_number <= 364485){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 133.87990418)/49.7375864994))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 131.868152116)/49.3498105469))+0.0); 

		 }

		 else return 0.;
	}

	 //! variation: MET_TRIG_EFF_CR_ELID_MED
	 if(variation_index==1003){
		 // year: 2015 
		 // trigger: HLT_xe70_mht 
		 if(run_number >= 266904 && run_number <= 284484){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 93.0492533384)/55.1235482232))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 89.4456844224)/56.3371720008))+0.0); 

		 }
		 // year: 2017 
		 // trigger: HLT_xe110_pufit_L1XE50 
		 if(run_number >= 332303 && run_number <= 341649){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.472927621)/57.0102685359))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.164453815)/51.2693001092))+0.0); 

		 }
		 // trigger: HLT_xe110_pufit_L1XE55 
		 if(run_number >= 325713 && run_number <= 331975){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 132.223574398)/47.3772863008))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.795690411)/51.2611051474))+0.0); 

		 }
		 // year: 2016 
		 // trigger: HLT_xe90_mht_L1XE50 
		 if(run_number >= 296939 && run_number <= 302872){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 103.574432672)/56.7093693407))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 94.782189818)/51.8406549107))+0.0); 

		 }
		 // trigger: HLT_xe110_mht_L1XE50 
		 if(run_number >= 302873 && run_number <= 311481){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 125.252619831)/48.9084534078))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 120.426046343)/49.4465104523))+0.0); 

		 }
		 // year: 2018 
		 // trigger: HLT_xe110_pufit_xe70_L1XE50 
		 if(run_number >= 348885 && run_number <= 364485){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.775264829)/51.7051074249))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 132.340255343)/50.6615783029))+0.0); 

		 }

		 else return 0.;
	}

	 //! variation: MET_TRIG_EFF_CR_ELID_TIGHT
	 if(variation_index==1004){
		 // year: 2015 
		 // trigger: HLT_xe70_mht 
		 if(run_number >= 266904 && run_number <= 284484){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 92.9341843738)/55.3953988387))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 89.352528096)/56.8102586008))+0.0); 

		 }
		 // year: 2017 
		 // trigger: HLT_xe110_pufit_L1XE50 
		 if(run_number >= 332303 && run_number <= 341649){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.241553094)/56.7577923716))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.10544772)/51.4138084801))+0.0); 

		 }
		 // trigger: HLT_xe110_pufit_L1XE55 
		 if(run_number >= 325713 && run_number <= 331975){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 131.896176154)/47.9741064366))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.586925146)/51.4303040427))+0.0); 

		 }
		 // year: 2016 
		 // trigger: HLT_xe90_mht_L1XE50 
		 if(run_number >= 296939 && run_number <= 302872){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 103.45845276)/56.5134118131))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 94.6381527697)/51.6426332347))+0.0); 

		 }
		 // trigger: HLT_xe110_mht_L1XE50 
		 if(run_number >= 302873 && run_number <= 311481){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 125.210114236)/48.8767476359))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 120.501398088)/49.7750508887))+0.0); 

		 }
		 // year: 2018 
		 // trigger: HLT_xe110_pufit_xe70_L1XE50 
		 if(run_number >= 348885 && run_number <= 364485){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.98217633)/52.1065826055))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 132.226481617)/50.668705068))+0.0); 

		 }

		 else return 0.;
	}

	 //! variation: MET_TRIG_EFF_CR_NJETS3
	 if(variation_index==1005){
		 // year: 2015 
		 // trigger: HLT_xe70_mht 
		 if(run_number >= 266904 && run_number <= 284484){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 95.2936763228)/55.9352759916))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 92.1941773713)/61.4683032925))+0.0); 

		 }
		 // year: 2017 
		 // trigger: HLT_xe110_pufit_L1XE50 
		 if(run_number >= 332303 && run_number <= 341649){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 135.551790406)/57.808100319))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 129.757924966)/53.347471548))+0.0); 

		 }
		 // trigger: HLT_xe110_pufit_L1XE55 
		 if(run_number >= 325713 && run_number <= 331975){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 134.902397115)/52.8939170779))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 131.571948203)/54.3524102631))+0.0); 

		 }
		 // year: 2016 
		 // trigger: HLT_xe90_mht_L1XE50 
		 if(run_number >= 296939 && run_number <= 302872){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 105.815496649)/58.6273116739))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 95.4552887489)/53.8100491309))+0.0); 

		 }
		 // trigger: HLT_xe110_mht_L1XE50 
		 if(run_number >= 302873 && run_number <= 311481){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 127.68809183)/49.7677797061))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 121.229358013)/50.1054578664))+0.0); 

		 }
		 // year: 2018 
		 // trigger: HLT_xe110_pufit_xe70_L1XE50 
		 if(run_number >= 348885 && run_number <= 364485){
			 return 
			 (0.5*(1 + TMath::Erf((met_et - 138.121809959)/54.4110620791))+0.0) 
			 / 
			 (0.5*(1 + TMath::Erf((met_et - 133.91686513)/53.2545134479))+0.0); 

		 }

		 else return 0.;
	}

	 else return 1.; 
}




// total efficiency (lumi weighted) 
float metTrigEff(float met_et, int variation_index){
	 //! variation: MET_TRIG_EFF_CR_NOM
	 if(variation_index==1000){
		 return 
		 ( 0.0232 * ((0.5*(1 + TMath::Erf((met_et - 93.0619538268)/55.6366810686))+0.0))+0.2265 * ((0.5*(1 + TMath::Erf((met_et - 135.350368777)/56.8400167879))+0.0))+0.0923 * ((0.5*(1 + TMath::Erf((met_et - 132.006938735)/47.2507697777))+0.0))+0.0442 * ((0.5*(1 + TMath::Erf((met_et - 103.348990165)/56.3107160114))+0.0))+0.1932 * ((0.5*(1 + TMath::Erf((met_et - 125.234878112)/48.7740968647))+0.0))+0.4206 * ((0.5*(1 + TMath::Erf((met_et - 135.61670811)/51.6018951346))+0.0)) )
			 / 
		 ( 0.0244 * ((0.5*(1 + TMath::Erf((met_et - 89.5590553282)/56.8194688873))+0.0))+0.2401 * ((0.5*(1 + TMath::Erf((met_et - 129.249355406)/51.5178628873))+0.0))+0.0389 * ((0.5*(1 + TMath::Erf((met_et - 129.749887552)/51.0437616734))+0.0))+0.0466 * ((0.5*(1 + TMath::Erf((met_et - 94.6923317174)/51.6202343985))+0.0))+0.2041 * ((0.5*(1 + TMath::Erf((met_et - 120.410325866)/49.3915368169))+0.0))+0.4459 * ((0.5*(1 + TMath::Erf((met_et - 132.435817256)/50.7042552106))+0.0)) );
	 }

	 //! variation: MET_TRIG_EFF_CR_TAUID_MED
	 if(variation_index==1001){
		 return 
		 ( 0.0232 * ((0.5*(1 + TMath::Erf((met_et - 91.303757767)/52.8982128111))+0.0))+0.2265 * ((0.5*(1 + TMath::Erf((met_et - 134.475124233)/54.9562948133))+0.0))+0.0923 * ((0.5*(1 + TMath::Erf((met_et - 131.334583273)/47.5411325382))+0.0))+0.0442 * ((0.5*(1 + TMath::Erf((met_et - 100.97632858)/57.1622166401))+0.0))+0.1932 * ((0.5*(1 + TMath::Erf((met_et - 125.534627623)/47.0268033264))+0.0))+0.4206 * ((0.5*(1 + TMath::Erf((met_et - 134.342266553)/51.3253186459))+0.0)) )
			 / 
		 ( 0.0244 * ((0.5*(1 + TMath::Erf((met_et - 88.688123153)/55.4032606324))+0.0))+0.2401 * ((0.5*(1 + TMath::Erf((met_et - 129.10814207)/51.2469290957))+0.0))+0.0389 * ((0.5*(1 + TMath::Erf((met_et - 129.60370124)/50.423668327))+0.0))+0.0466 * ((0.5*(1 + TMath::Erf((met_et - 94.863372632)/51.4470426807))+0.0))+0.2041 * ((0.5*(1 + TMath::Erf((met_et - 120.34799564)/49.4545641793))+0.0))+0.4459 * ((0.5*(1 + TMath::Erf((met_et - 132.193363806)/50.0839453327))+0.0)) );
	 }

	 //! variation: MET_TRIG_EFF_CR_TAUID_TIGHT
	 if(variation_index==1002){
		 return 
		 ( 0.0232 * ((0.5*(1 + TMath::Erf((met_et - 92.0254713627)/53.5500931898))+0.0))+0.2265 * ((0.5*(1 + TMath::Erf((met_et - 135.359484838)/56.8402750904))+0.0))+0.0923 * ((0.5*(1 + TMath::Erf((met_et - 133.141197399)/50.342657233))+0.0))+0.0442 * ((0.5*(1 + TMath::Erf((met_et - 99.7712927607)/56.7239608431))+0.0))+0.1932 * ((0.5*(1 + TMath::Erf((met_et - 124.787973884)/47.8773406565))+0.0))+0.4206 * ((0.5*(1 + TMath::Erf((met_et - 133.87990418)/49.7375864994))+0.0)) )
			 / 
		 ( 0.0244 * ((0.5*(1 + TMath::Erf((met_et - 89.2749953931)/56.3789836775))+0.0))+0.2401 * ((0.5*(1 + TMath::Erf((met_et - 128.646684151)/50.3209622521))+0.0))+0.0389 * ((0.5*(1 + TMath::Erf((met_et - 130.177786768)/51.3808901105))+0.0))+0.0466 * ((0.5*(1 + TMath::Erf((met_et - 94.5135107914)/52.2392003706))+0.0))+0.2041 * ((0.5*(1 + TMath::Erf((met_et - 120.182349616)/49.5474751025))+0.0))+0.4459 * ((0.5*(1 + TMath::Erf((met_et - 131.868152116)/49.3498105469))+0.0)) );
	 }

	 //! variation: MET_TRIG_EFF_CR_ELID_MED
	 if(variation_index==1003){
		 return 
		 ( 0.0232 * ((0.5*(1 + TMath::Erf((met_et - 93.0492533384)/55.1235482232))+0.0))+0.2265 * ((0.5*(1 + TMath::Erf((met_et - 135.472927621)/57.0102685359))+0.0))+0.0923 * ((0.5*(1 + TMath::Erf((met_et - 132.223574398)/47.3772863008))+0.0))+0.0442 * ((0.5*(1 + TMath::Erf((met_et - 103.574432672)/56.7093693407))+0.0))+0.1932 * ((0.5*(1 + TMath::Erf((met_et - 125.252619831)/48.9084534078))+0.0))+0.4206 * ((0.5*(1 + TMath::Erf((met_et - 135.775264829)/51.7051074249))+0.0)) )
			 / 
		 ( 0.0244 * ((0.5*(1 + TMath::Erf((met_et - 89.4456844224)/56.3371720008))+0.0))+0.2401 * ((0.5*(1 + TMath::Erf((met_et - 129.164453815)/51.2693001092))+0.0))+0.0389 * ((0.5*(1 + TMath::Erf((met_et - 129.795690411)/51.2611051474))+0.0))+0.0466 * ((0.5*(1 + TMath::Erf((met_et - 94.782189818)/51.8406549107))+0.0))+0.2041 * ((0.5*(1 + TMath::Erf((met_et - 120.426046343)/49.4465104523))+0.0))+0.4459 * ((0.5*(1 + TMath::Erf((met_et - 132.340255343)/50.6615783029))+0.0)) );
	 }

	 //! variation: MET_TRIG_EFF_CR_ELID_TIGHT
	 if(variation_index==1004){
		 return 
		 ( 0.0232 * ((0.5*(1 + TMath::Erf((met_et - 92.9341843738)/55.3953988387))+0.0))+0.2265 * ((0.5*(1 + TMath::Erf((met_et - 135.241553094)/56.7577923716))+0.0))+0.0923 * ((0.5*(1 + TMath::Erf((met_et - 131.896176154)/47.9741064366))+0.0))+0.0442 * ((0.5*(1 + TMath::Erf((met_et - 103.45845276)/56.5134118131))+0.0))+0.1932 * ((0.5*(1 + TMath::Erf((met_et - 125.210114236)/48.8767476359))+0.0))+0.4206 * ((0.5*(1 + TMath::Erf((met_et - 135.98217633)/52.1065826055))+0.0)) )
			 / 
		 ( 0.0244 * ((0.5*(1 + TMath::Erf((met_et - 89.352528096)/56.8102586008))+0.0))+0.2401 * ((0.5*(1 + TMath::Erf((met_et - 129.10544772)/51.4138084801))+0.0))+0.0389 * ((0.5*(1 + TMath::Erf((met_et - 129.586925146)/51.4303040427))+0.0))+0.0466 * ((0.5*(1 + TMath::Erf((met_et - 94.6381527697)/51.6426332347))+0.0))+0.2041 * ((0.5*(1 + TMath::Erf((met_et - 120.501398088)/49.7750508887))+0.0))+0.4459 * ((0.5*(1 + TMath::Erf((met_et - 132.226481617)/50.668705068))+0.0)) );
	 }

	 //! variation: MET_TRIG_EFF_CR_NJETS3
	 if(variation_index==1005){
		 return 
		 ( 0.0232 * ((0.5*(1 + TMath::Erf((met_et - 95.2936763228)/55.9352759916))+0.0))+0.2265 * ((0.5*(1 + TMath::Erf((met_et - 135.551790406)/57.808100319))+0.0))+0.0923 * ((0.5*(1 + TMath::Erf((met_et - 134.902397115)/52.8939170779))+0.0))+0.0442 * ((0.5*(1 + TMath::Erf((met_et - 105.815496649)/58.6273116739))+0.0))+0.1932 * ((0.5*(1 + TMath::Erf((met_et - 127.68809183)/49.7677797061))+0.0))+0.4206 * ((0.5*(1 + TMath::Erf((met_et - 138.121809959)/54.4110620791))+0.0)) )
			 / 
		 ( 0.0244 * ((0.5*(1 + TMath::Erf((met_et - 92.1941773713)/61.4683032925))+0.0))+0.2401 * ((0.5*(1 + TMath::Erf((met_et - 129.757924966)/53.347471548))+0.0))+0.0389 * ((0.5*(1 + TMath::Erf((met_et - 131.571948203)/54.3524102631))+0.0))+0.0466 * ((0.5*(1 + TMath::Erf((met_et - 95.4552887489)/53.8100491309))+0.0))+0.2041 * ((0.5*(1 + TMath::Erf((met_et - 121.229358013)/50.1054578664))+0.0))+0.4459 * ((0.5*(1 + TMath::Erf((met_et - 133.91686513)/53.2545134479))+0.0)) );
	 }


	 else return 0;
}
