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
		 //! total variation UP
		 if(var==2){
			 float SF_temp[12] = { 
1.071, 1.088, 1.060, 0.993, 0.948, 0.895, 0.849, 0.823, 0.834, 0.921, 1.228, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! total variation DOWN
		 if(var==3){
			 float SF_temp[12] = { 
0.620, 0.888, 0.989, 0.974, 0.843, 0.685, 0.545, 0.467, 0.494, 0.652, 0.864, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		  if (var!=-1){std::cout << "njet SF ERROR:   Unrecognized variation index! " << var << std::endl;}
		 return 1.0; 
 }; 
 
