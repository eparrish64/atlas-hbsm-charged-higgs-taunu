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
0.805, 0.958, 1.005, 0.977, 0.900, 0.802, 0.713, 0.660, 0.671, 0.775, 1.000, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation UP
		 if(var==2){
			 float SF_temp[12] = { 
1.037, 1.059, 1.039, 0.991, 0.951, 0.903, 0.861, 0.839, 0.859, 0.964, 1.257, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation DOWN
		 if(var==3){
			 float SF_temp[12] = { 
0.572, 0.856, 0.972, 0.963, 0.848, 0.702, 0.567, 0.487, 0.503, 0.647, 0.856, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR05_MUF05 
		 if(var==1001){
			 float SF_temp[12] = { 
1.107, 0.996, 0.877, 0.758, 0.649, 0.558, 0.492, 0.461, 0.473, 0.536, 0.658, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR05_MUF1 
		 if(var==1002){
			 float SF_temp[12] = { 
1.122, 1.006, 0.883, 0.762, 0.651, 0.558, 0.492, 0.461, 0.474, 0.539, 0.664, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR1_MUF05 
		 if(var==1003){
			 float SF_temp[12] = { 
0.780, 0.940, 0.993, 0.968, 0.894, 0.797, 0.707, 0.652, 0.659, 0.757, 0.975, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR1_MUF2 
		 if(var==1004){
			 float SF_temp[12] = { 
0.829, 0.974, 1.016, 0.984, 0.905, 0.807, 0.717, 0.662, 0.671, 0.771, 0.990, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR2_MUF1 
		 if(var==1005){
			 float SF_temp[12] = { 
0.264, 0.804, 1.105, 1.220, 1.206, 1.117, 1.010, 0.938, 0.958, 1.123, 1.491, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  MUR2_MUF2 
		 if(var==1006){
			 float SF_temp[12] = { 
0.301, 0.830, 1.122, 1.233, 1.217, 1.128, 1.021, 0.950, 0.971, 1.138, 1.505, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  qsf_1down 
		 if(var==1007){
			 float SF_temp[12] = { 
1.089, 0.972, 0.844, 0.722, 0.625, 0.570, 0.576, 0.660, 0.840, 1.135, 1.562, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  qsf_1up 
		 if(var==1008){
			 float SF_temp[12] = { 
1.078, 0.992, 0.882, 0.768, 0.672, 0.616, 0.622, 0.710, 0.903, 1.223, 1.690, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  ckkw_1down 
		 if(var==1009){
			 float SF_temp[12] = { 
1.036, 0.948, 0.842, 0.737, 0.648, 0.594, 0.592, 0.660, 0.814, 1.072, 1.452, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for  ckkw_1up 
		 if(var==1010){
			 float SF_temp[12] = { 
1.141, 1.104, 1.019, 0.916, 0.822, 0.768, 0.781, 0.890, 1.125, 1.513, 2.085, 1.000 
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
		 std::cout << "njet SF ERROR:   Unrecognized variation index! " << var << std::endl; 
		 return 1.0; 
 }; 
 
