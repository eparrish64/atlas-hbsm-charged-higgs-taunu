//             This is an effective mass reweighting for ttbar - from fit
//             To be used for the tau+jets channel!
//             in a the lookup table form (after compactification)
float eff_mass_taujet(float eff_m,int var){
	 //! xmin:  0.0 
	 //! xmax: 3000.0 
	 //! npoints: 100 
	 int i = static_cast<int>(100*(eff_m -  0.0)/(3000.0 -  0.0)); 
	 if ( i < 0 || i > 100 ) i=100; 

		 //! NOMINAL 
		 if(var==0 || var==1){
			 float SF_temp[102] = { 
0.585, 0.633, 0.676, 0.714, 0.747, 0.777, 0.803, 0.825, 0.845, 0.861, 0.875, 0.887, 0.896, 0.903, 0.909, 0.912, 0.915, 0.915, 0.915, 0.914, 0.911, 0.908, 0.904, 0.899, 0.893, 0.887, 0.880, 0.873, 0.866, 0.858, 0.850, 0.842, 0.834, 0.825, 0.817, 0.808, 0.799, 0.791, 0.782, 0.773, 0.765, 0.756, 0.748, 0.739, 0.731, 0.723, 0.715, 0.707, 0.699, 0.691, 0.684, 0.677, 0.669, 0.662, 0.656, 0.649, 0.642, 0.636, 0.630, 0.624, 0.618, 0.612, 0.607, 0.602, 0.596, 0.591, 0.586, 0.582, 0.577, 0.573, 0.568, 0.564, 0.560, 0.556, 0.552, 0.549, 0.545, 0.542, 0.538, 0.535, 0.532, 0.529, 0.526, 0.523, 0.521, 0.518, 0.516, 0.513, 0.511, 0.509, 0.507, 0.505, 0.503, 0.501, 0.499, 0.497, 0.495, 0.494, 0.492, 0.491, 0.489, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! statistical variation UP
		 if(var==2){
			 float SF_temp[102] = { 
0.703, 0.728, 0.752, 0.775, 0.799, 0.823, 0.844, 0.863, 0.878, 0.891, 0.902, 0.910, 0.916, 0.921, 0.924, 0.926, 0.926, 0.925, 0.923, 0.921, 0.919, 0.916, 0.913, 0.909, 0.904, 0.899, 0.893, 0.886, 0.879, 0.872, 0.864, 0.856, 0.847, 0.839, 0.830, 0.821, 0.813, 0.804, 0.795, 0.787, 0.778, 0.770, 0.762, 0.755, 0.747, 0.740, 0.733, 0.727, 0.721, 0.715, 0.709, 0.704, 0.698, 0.693, 0.688, 0.684, 0.679, 0.675, 0.670, 0.666, 0.663, 0.659, 0.656, 0.652, 0.649, 0.646, 0.643, 0.640, 0.638, 0.635, 0.633, 0.630, 0.628, 0.626, 0.624, 0.622, 0.620, 0.619, 0.617, 0.615, 0.614, 0.613, 0.611, 0.610, 0.609, 0.608, 0.607, 0.606, 0.605, 0.604, 0.603, 0.602, 0.601, 0.601, 0.600, 0.599, 0.599, 0.598, 0.598, 0.597, 0.597, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! statistical variation DOWN
		 if(var==3){
			 float SF_temp[102] = { 
0.189, 0.286, 0.372, 0.449, 0.516, 0.575, 0.626, 0.670, 0.707, 0.738, 0.763, 0.783, 0.799, 0.812, 0.822, 0.829, 0.834, 0.838, 0.840, 0.841, 0.841, 0.840, 0.838, 0.836, 0.833, 0.830, 0.826, 0.822, 0.817, 0.812, 0.807, 0.802, 0.796, 0.791, 0.785, 0.779, 0.772, 0.766, 0.760, 0.753, 0.747, 0.740, 0.734, 0.727, 0.720, 0.714, 0.707, 0.700, 0.693, 0.686, 0.678, 0.670, 0.662, 0.654, 0.646, 0.638, 0.630, 0.622, 0.615, 0.607, 0.600, 0.593, 0.586, 0.579, 0.572, 0.566, 0.559, 0.553, 0.547, 0.541, 0.535, 0.530, 0.524, 0.519, 0.513, 0.508, 0.503, 0.498, 0.493, 0.489, 0.484, 0.480, 0.475, 0.471, 0.467, 0.463, 0.459, 0.455, 0.451, 0.448, 0.444, 0.441, 0.437, 0.434, 0.431, 0.427, 0.424, 0.421, 0.419, 0.416, 0.413, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 std::cout << "njet SF ERROR:   Unrecognized variation index! " << var << std::endl; 
		 return 1.0; 
 }; 
 
