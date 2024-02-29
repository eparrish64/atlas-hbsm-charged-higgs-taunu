//             This is a number of jets reweighting for wjets - from fit
//             To be used for both tau+jets and tau+lep channels!
//             in a the lookup table form (after compactification)
float njets(int n_jets,int var){
	 //! xmin:  0.0 
	 //! xmax: 10.0 
	 //! npoints: 10 
	 int i = static_cast<int>(10*(n_jets -  0.0)/(10.0 -  0.0)); 
	 if ( i < 0 || i > 10 ) i=10; 

		 //! NOMINAL 
		 if(var==0 || var==1){
			 float SF_temp[12] = { 
0.806, 0.954, 0.997, 0.964, 0.883, 0.783, 0.693, 0.642, 0.659, 0.772, 1.010, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation UP
		 if(var==2){
			 float SF_temp[12] = { 
1.036, 1.055, 1.030, 0.982, 0.942, 0.891, 0.847, 0.821, 0.829, 0.898, 1.157, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation DOWN
		 if(var==3){
			 float SF_temp[12] = { 
0.575, 0.853, 0.963, 0.943, 0.821, 0.671, 0.533, 0.451, 0.461, 0.572, 0.737, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR05_MUF05 
		 if(var==1001){
			 float SF_temp[12] = { 
1.104, 0.990, 0.868, 0.746, 0.632, 0.534, 0.462, 0.424, 0.428, 0.481, 0.594, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR05_MUF1 
		 if(var==1002){
			 float SF_temp[12] = { 
1.119, 1.000, 0.874, 0.749, 0.633, 0.534, 0.462, 0.424, 0.428, 0.484, 0.600, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR1_MUF05 
		 if(var==1003){
			 float SF_temp[12] = { 
0.781, 0.936, 0.985, 0.955, 0.875, 0.775, 0.684, 0.629, 0.640, 0.746, 0.975, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR1_MUF2 
		 if(var==1004){
			 float SF_temp[12] = { 
0.830, 0.970, 1.008, 0.970, 0.887, 0.785, 0.694, 0.641, 0.654, 0.761, 0.992, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR2_MUF1 
		 if(var==1005){
			 float SF_temp[12] = { 
0.270, 0.803, 1.095, 1.202, 1.179, 1.082, 0.967, 0.890, 0.907, 1.073, 1.444, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR2_MUF2 
		 if(var==1006){
			 float SF_temp[12] = { 
0.306, 0.828, 1.113, 1.214, 1.189, 1.091, 0.976, 0.899, 0.916, 1.081, 1.450, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  qsf_1down 
		 if(var==1007){
			 float SF_temp[12] = { 
1.085, 0.966, 0.835, 0.711, 0.610, 0.550, 0.548, 0.621, 0.788, 1.065, 1.470, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  qsf_1up 
		 if(var==1008){
			 float SF_temp[12] = { 
1.074, 0.986, 0.872, 0.755, 0.655, 0.594, 0.591, 0.669, 0.848, 1.149, 1.593, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  ckkw_1down 
		 if(var==1009){
			 float SF_temp[12] = { 
1.031, 0.941, 0.834, 0.724, 0.631, 0.569, 0.556, 0.610, 0.745, 0.981, 1.332, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  ckkw_1up 
		 if(var==1010){
			 float SF_temp[12] = { 
1.136, 1.096, 1.009, 0.902, 0.805, 0.744, 0.748, 0.846, 1.066, 1.435, 1.982, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdf_1down 
		 if(var==1015){
			 float SF_temp[12] = { 
0.868, 1.035, 1.082, 1.043, 0.951, 0.838, 0.737, 0.683, 0.707, 0.842, 1.122, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdf_1up 
		 if(var==1016){
			 float SF_temp[12] = { 
0.758, 0.888, 0.925, 0.895, 0.823, 0.735, 0.654, 0.608, 0.620, 0.716, 0.921, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdfset_1down 
		 if(var==1017){
			 float SF_temp[12] = { 
0.813, 0.953, 0.991, 0.954, 0.870, 0.766, 0.670, 0.610, 0.613, 0.707, 0.919, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdfset_1up 
		 if(var==1018){
			 float SF_temp[12] = { 
0.805, 0.943, 0.981, 0.946, 0.865, 0.766, 0.676, 0.624, 0.637, 0.742, 0.967, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  alphaS_1down 
		 if(var==1019){
			 float SF_temp[12] = { 
0.840, 0.958, 0.983, 0.941, 0.857, 0.759, 0.673, 0.625, 0.641, 0.749, 0.974, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  alphaS_1up 
		 if(var==1020){
			 float SF_temp[12] = { 
0.822, 0.975, 1.021, 0.989, 0.909, 0.809, 0.719, 0.669, 0.688, 0.806, 1.051, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 std::cout << "njet SF ERROR:   Unrecognized variation index! " << var << std::endl; 
		 return 1.0; 
 }; 
 
