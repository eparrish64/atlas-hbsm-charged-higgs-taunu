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
0.846, 0.988, 1.025, 0.986, 0.900, 0.797, 0.706, 0.657, 0.677, 0.798, 1.047, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! statistical variation UP
		 if(var==2){
			 float SF_temp[12] = { 
1.058, 1.088, 1.058, 0.990, 0.907, 0.803, 0.717, 0.667, 0.701, 0.877, 1.228, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! statistical variation DOWN
		 if(var==3){
			 float SF_temp[12] = { 
0.634, 0.888, 0.991, 0.982, 0.894, 0.792, 0.696, 0.647, 0.654, 0.719, 0.867, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 std::cout << "njet SF ERROR:   Unrecognized variation index! " << var << std::endl; 
		 return 1.0; 
 }; 
 
