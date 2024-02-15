//             This is an effective mass reweighting for ttbar - from fit
//             To be used for the tau+lepton channel!
//             in a the lookup table form (after compactification)
float eff_mass_taulep(float eff_m,int var){
	 //! xmin:  0.0 
	 //! xmax: 3000.0 
	 //! npoints: 100 
	 int i = static_cast<int>(100*(eff_m -  0.0)/(3000.0 -  0.0)); 
	 if ( i < 0 || i > 100 ) i=100; 

		 //! NOMINAL 
		 if(var==0 || var==1){
			 float SF_temp[102] = { 
0.734, 0.771, 0.804, 0.833, 0.857, 0.879, 0.898, 0.913, 0.927, 0.938, 0.946, 0.953, 0.959, 0.963, 0.965, 0.966, 0.966, 0.966, 0.964, 0.961, 0.958, 0.955, 0.950, 0.946, 0.941, 0.935, 0.930, 0.924, 0.918, 0.912, 0.905, 0.899, 0.893, 0.886, 0.880, 0.874, 0.867, 0.861, 0.855, 0.849, 0.843, 0.837, 0.831, 0.826, 0.820, 0.815, 0.809, 0.804, 0.799, 0.794, 0.789, 0.785, 0.780, 0.776, 0.772, 0.768, 0.764, 0.760, 0.756, 0.753, 0.749, 0.746, 0.743, 0.740, 0.737, 0.734, 0.731, 0.729, 0.726, 0.724, 0.721, 0.719, 0.717, 0.715, 0.713, 0.711, 0.709, 0.707, 0.706, 0.704, 0.702, 0.701, 0.699, 0.698, 0.697, 0.696, 0.694, 0.693, 0.692, 0.691, 0.690, 0.689, 0.688, 0.687, 0.686, 0.686, 0.685, 0.684, 0.683, 0.683, 0.682, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! full variation UP
		 if(var==2){
			 float SF_temp[102] = { 
0.856, 0.888, 0.916, 0.940, 0.961, 0.980, 0.995, 1.008, 1.018, 1.026, 1.033, 1.037, 1.040, 1.042, 1.042, 1.042, 1.040, 1.038, 1.035, 1.031, 1.026, 1.021, 1.016, 1.010, 1.004, 0.997, 0.990, 0.984, 0.977, 0.970, 0.964, 0.957, 0.951, 0.945, 0.938, 0.932, 0.927, 0.921, 0.915, 0.910, 0.905, 0.900, 0.895, 0.890, 0.886, 0.882, 0.878, 0.874, 0.870, 0.866, 0.863, 0.859, 0.856, 0.853, 0.850, 0.848, 0.845, 0.842, 0.840, 0.838, 0.836, 0.834, 0.832, 0.830, 0.828, 0.826, 0.825, 0.823, 0.822, 0.820, 0.819, 0.818, 0.817, 0.816, 0.815, 0.814, 0.813, 0.812, 0.811, 0.811, 0.810, 0.809, 0.809, 0.808, 0.807, 0.807, 0.806, 0.806, 0.805, 0.805, 0.805, 0.804, 0.804, 0.804, 0.803, 0.803, 0.803, 0.803, 0.802, 0.802, 0.802, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! full variation DOWN
		 if(var==3){
			 float SF_temp[102] = { 
0.599, 0.643, 0.681, 0.713, 0.742, 0.766, 0.787, 0.804, 0.818, 0.830, 0.840, 0.847, 0.853, 0.858, 0.860, 0.862, 0.862, 0.862, 0.860, 0.858, 0.855, 0.851, 0.846, 0.842, 0.836, 0.831, 0.825, 0.819, 0.813, 0.807, 0.800, 0.794, 0.787, 0.781, 0.774, 0.768, 0.762, 0.755, 0.749, 0.743, 0.737, 0.731, 0.725, 0.719, 0.713, 0.707, 0.702, 0.696, 0.691, 0.686, 0.681, 0.676, 0.671, 0.666, 0.661, 0.657, 0.652, 0.648, 0.644, 0.640, 0.636, 0.632, 0.628, 0.624, 0.620, 0.617, 0.614, 0.610, 0.607, 0.604, 0.601, 0.598, 0.595, 0.592, 0.590, 0.587, 0.585, 0.582, 0.580, 0.578, 0.576, 0.574, 0.572, 0.570, 0.568, 0.566, 0.564, 0.563, 0.561, 0.559, 0.558, 0.556, 0.555, 0.554, 0.552, 0.551, 0.550, 0.549, 0.548, 0.547, 0.546, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for HERWIG PS 
		 if(var==1001){
			 float SF_temp[102] = { 
1.137, 1.133, 1.130, 1.126, 1.123, 1.119, 1.116, 1.112, 1.109, 1.105, 1.102, 1.098, 1.094, 1.091, 1.087, 1.083, 1.080, 1.076, 1.072, 1.069, 1.065, 1.061, 1.057, 1.053, 1.050, 1.046, 1.042, 1.038, 1.034, 1.030, 1.026, 1.023, 1.019, 1.015, 1.011, 1.007, 1.003, 0.999, 0.994, 0.990, 0.986, 0.982, 0.978, 0.974, 0.970, 0.966, 0.961, 0.957, 0.953, 0.949, 0.944, 0.940, 0.936, 0.932, 0.927, 0.923, 0.918, 0.914, 0.910, 0.905, 0.901, 0.896, 0.892, 0.887, 0.883, 0.878, 0.874, 0.869, 0.864, 0.860, 0.855, 0.850, 0.846, 0.841, 0.836, 0.832, 0.827, 0.822, 0.817, 0.812, 0.808, 0.803, 0.798, 0.793, 0.788, 0.783, 0.778, 0.773, 0.768, 0.763, 0.758, 0.753, 0.748, 0.743, 0.738, 0.732, 0.727, 0.722, 0.717, 0.712, 0.706, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for ISR 1up 
		 if(var==1002){
			 float SF_temp[102] = { 
0.612, 0.685, 0.748, 0.801, 0.845, 0.880, 0.909, 0.932, 0.949, 0.961, 0.970, 0.974, 0.976, 0.974, 0.971, 0.965, 0.958, 0.949, 0.939, 0.928, 0.916, 0.903, 0.891, 0.877, 0.864, 0.850, 0.837, 0.823, 0.810, 0.796, 0.783, 0.770, 0.758, 0.746, 0.734, 0.722, 0.711, 0.700, 0.689, 0.679, 0.669, 0.660, 0.651, 0.642, 0.634, 0.626, 0.618, 0.611, 0.604, 0.597, 0.590, 0.584, 0.579, 0.573, 0.568, 0.563, 0.558, 0.554, 0.549, 0.545, 0.541, 0.538, 0.534, 0.531, 0.528, 0.525, 0.522, 0.520, 0.517, 0.515, 0.512, 0.510, 0.508, 0.507, 0.505, 0.503, 0.502, 0.500, 0.499, 0.497, 0.496, 0.495, 0.494, 0.493, 0.492, 0.491, 0.490, 0.489, 0.488, 0.488, 0.487, 0.486, 0.486, 0.485, 0.485, 0.484, 0.484, 0.483, 0.483, 0.482, 0.482, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for ISR 1down 
		 if(var==1003){
			 float SF_temp[102] = { 
0.978, 0.991, 1.003, 1.014, 1.024, 1.033, 1.041, 1.048, 1.055, 1.060, 1.066, 1.070, 1.074, 1.077, 1.080, 1.082, 1.084, 1.086, 1.087, 1.088, 1.088, 1.089, 1.089, 1.088, 1.088, 1.087, 1.086, 1.085, 1.084, 1.083, 1.081, 1.080, 1.078, 1.076, 1.074, 1.072, 1.071, 1.069, 1.067, 1.064, 1.062, 1.060, 1.058, 1.056, 1.054, 1.052, 1.050, 1.047, 1.045, 1.043, 1.041, 1.039, 1.037, 1.035, 1.033, 1.031, 1.029, 1.027, 1.025, 1.023, 1.021, 1.020, 1.018, 1.016, 1.014, 1.013, 1.011, 1.010, 1.008, 1.006, 1.005, 1.003, 1.002, 1.001, 0.999, 0.998, 0.997, 0.995, 0.994, 0.993, 0.992, 0.991, 0.990, 0.989, 0.987, 0.986, 0.985, 0.984, 0.984, 0.983, 0.982, 0.981, 0.980, 0.979, 0.978, 0.978, 0.977, 0.976, 0.976, 0.975, 0.974, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for FSR 1up 
		 if(var==1004){
			 float SF_temp[102] = { 
0.736, 0.772, 0.803, 0.830, 0.853, 0.872, 0.889, 0.902, 0.913, 0.922, 0.929, 0.934, 0.937, 0.939, 0.940, 0.939, 0.938, 0.935, 0.932, 0.929, 0.925, 0.920, 0.915, 0.909, 0.904, 0.898, 0.892, 0.886, 0.879, 0.873, 0.867, 0.860, 0.854, 0.848, 0.842, 0.836, 0.830, 0.824, 0.818, 0.813, 0.807, 0.802, 0.797, 0.792, 0.787, 0.782, 0.777, 0.773, 0.769, 0.764, 0.760, 0.757, 0.753, 0.749, 0.746, 0.742, 0.739, 0.736, 0.733, 0.730, 0.728, 0.725, 0.723, 0.720, 0.718, 0.716, 0.714, 0.712, 0.710, 0.708, 0.706, 0.705, 0.703, 0.702, 0.700, 0.699, 0.697, 0.696, 0.695, 0.694, 0.693, 0.692, 0.691, 0.690, 0.689, 0.688, 0.687, 0.687, 0.686, 0.685, 0.685, 0.684, 0.683, 0.683, 0.682, 0.682, 0.681, 0.681, 0.680, 0.680, 0.680, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 //! nominal for FSR 1down 
		 if(var==1005){
			 float SF_temp[102] = { 
0.775, 0.813, 0.846, 0.876, 0.901, 0.923, 0.942, 0.958, 0.972, 0.983, 0.992, 0.999, 1.004, 1.008, 1.010, 1.011, 1.011, 1.010, 1.008, 1.005, 1.002, 0.998, 0.993, 0.988, 0.983, 0.977, 0.971, 0.965, 0.959, 0.952, 0.946, 0.939, 0.933, 0.926, 0.920, 0.913, 0.907, 0.900, 0.894, 0.888, 0.881, 0.875, 0.869, 0.864, 0.858, 0.852, 0.847, 0.842, 0.837, 0.832, 0.827, 0.822, 0.818, 0.813, 0.809, 0.805, 0.801, 0.797, 0.794, 0.790, 0.787, 0.783, 0.780, 0.777, 0.774, 0.771, 0.768, 0.766, 0.763, 0.761, 0.758, 0.756, 0.754, 0.752, 0.750, 0.748, 0.746, 0.744, 0.743, 0.741, 0.740, 0.738, 0.737, 0.735, 0.734, 0.733, 0.732, 0.731, 0.730, 0.729, 0.728, 0.727, 0.726, 0.725, 0.724, 0.723, 0.723, 0.722, 0.721, 0.720, 0.720, 1.000 
			  }; 
			 return SF_temp[i]; 
		  }; 
		 if (var!=-1) std::cout << "eff_mass SF ERROR:   Unrecognized variation index! " << var << std::endl; 
		 return 1.0; 
 }; 
 
