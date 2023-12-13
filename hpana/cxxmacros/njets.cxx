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
0.810, 0.961, 1.004, 0.970, 0.886, 0.782, 0.686, 0.626, 0.633, 0.734, 0.959, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation UP
		 if(var==2){
			 float SF_temp[12] = { 
1.041, 1.061, 1.038, 0.987, 0.944, 0.893, 0.847, 0.822, 0.837, 0.936, 1.216, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation DOWN
		 if(var==3){
			 float SF_temp[12] = { 
0.578, 0.860, 0.971, 0.953, 0.828, 0.671, 0.526, 0.436, 0.446, 0.588, 0.814, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR05_MUF05 
		 if(var==1001){
			 float SF_temp[12] = { 
1.111, 0.997, 0.875, 0.751, 0.636, 0.537, 0.462, 0.420, 0.420, 0.469, 0.577, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR05_MUF1 
		 if(var==1002){
			 float SF_temp[12] = { 
1.126, 1.008, 0.881, 0.755, 0.637, 0.537, 0.461, 0.420, 0.421, 0.472, 0.583, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR1_MUF05 
		 if(var==1003){
			 float SF_temp[12] = { 
0.785, 0.943, 0.992, 0.962, 0.880, 0.777, 0.680, 0.618, 0.621, 0.716, 0.934, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR1_MUF2 
		 if(var==1004){
			 float SF_temp[12] = { 
0.834, 0.976, 1.015, 0.978, 0.892, 0.786, 0.689, 0.629, 0.633, 0.731, 0.950, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR2_MUF1 
		 if(var==1005){
			 float SF_temp[12] = { 
0.269, 0.808, 1.104, 1.212, 1.189, 1.092, 0.976, 0.898, 0.915, 1.084, 1.459, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR2_MUF2 
		 if(var==1006){
			 float SF_temp[12] = { 
0.306, 0.834, 1.121, 1.224, 1.199, 1.100, 0.984, 0.907, 0.924, 1.091, 1.464, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  qsf_1down 
		 if(var==1007){
			 float SF_temp[12] = { 
1.095, 0.974, 0.842, 0.717, 0.615, 0.554, 0.552, 0.626, 0.794, 1.072, 1.478, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  qsf_1up 
		 if(var==1008){
			 float SF_temp[12] = { 
1.085, 0.995, 0.880, 0.762, 0.661, 0.600, 0.597, 0.676, 0.855, 1.158, 1.604, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  ckkw_1down 
		 if(var==1009){
			 float SF_temp[12] = { 
1.041, 0.950, 0.841, 0.731, 0.636, 0.574, 0.561, 0.614, 0.750, 0.985, 1.337, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  ckkw_1up 
		 if(var==1010){
			 float SF_temp[12] = { 
1.148, 1.106, 1.018, 0.909, 0.810, 0.748, 0.752, 0.849, 1.068, 1.437, 1.984, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  fac_1down 
		 if(var==1011){
			 float SF_temp[12] = { 
1.055, 0.947, 0.828, 0.714, 0.619, 0.560, 0.553, 0.612, 0.753, 0.993, 1.346, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  fac_1up 
		 if(var==1012){
			 float SF_temp[12] = { 
1.112, 1.042, 0.941, 0.831, 0.735, 0.678, 0.682, 0.772, 0.970, 1.299, 1.784, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  renorm_1down 
		 if(var==1013){
			 float SF_temp[12] = { 
0.739, 0.675, 0.599, 0.521, 0.456, 0.416, 0.414, 0.461, 0.571, 0.756, 1.029, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  renorm_1up 
		 if(var==1014){
			 float SF_temp[12] = { 
1.546, 1.383, 1.207, 1.039, 0.901, 0.814, 0.799, 0.876, 1.066, 1.391, 1.872, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdf_1down 
		 if(var==1015){
			 float SF_temp[12] = { 
0.869, 1.040, 1.090, 1.052, 0.959, 0.846, 0.745, 0.691, 0.717, 0.856, 1.143, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdf_1up 
		 if(var==1016){
			 float SF_temp[12] = { 
0.760, 0.893, 0.932, 0.901, 0.826, 0.733, 0.646, 0.591, 0.592, 0.675, 0.866, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdfset_1down 
		 if(var==1017){
			 float SF_temp[12] = { 
0.817, 0.960, 0.999, 0.964, 0.881, 0.780, 0.688, 0.633, 0.644, 0.750, 0.977, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  pdfset_1up 
		 if(var==1018){
			 float SF_temp[12] = { 
0.809, 0.950, 0.989, 0.953, 0.869, 0.767, 0.672, 0.613, 0.617, 0.711, 0.925, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  alphaS_1down 
		 if(var==1019){
			 float SF_temp[12] = { 
0.844, 0.965, 0.991, 0.947, 0.862, 0.759, 0.668, 0.612, 0.620, 0.717, 0.930, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  alphaS_1up 
		 if(var==1020){
			 float SF_temp[12] = { 
0.826, 0.982, 1.029, 0.996, 0.913, 0.809, 0.713, 0.655, 0.664, 0.770, 1.002, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 std::cout << "njet SF ERROR:   Unrecognized variation index! " << var << std::endl; 
		 return 1.0; 
 }; 
 
