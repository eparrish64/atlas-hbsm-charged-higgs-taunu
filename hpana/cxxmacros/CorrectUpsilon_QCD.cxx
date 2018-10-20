///CorrectUpsilon_QCD(Y,pantau) - returns corrected Y value obtained from
///Smirnof transform between anti-tau -> tau
const float YCorr_QCD[5][1000] = {{-2,-2,-0.583,-0.583,-0.583,-0.580,-0.580,-0.580,-0.580,-0.580,-0.580,-0.580,-0.547,-0.547,-0.547,-0.433,-0.433,-0.364,-0.364,-0.364,-0.364,-0.364,-0.136,-0.136,-0.136,-0.136,-0.085,-0.028,-0.001,-0.001,-0.001,-0.001,0.011,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.038,0.038,0.038,0.041,0.041,0.041,0.041,0.047,0.047,0.047,0.047,0.047,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.053,0.056,0.056,0.056,0.056,0.056,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.062,0.062,0.062,0.062,0.062,0.065,0.065,0.065,0.065,0.068,0.068,0.068,0.068,0.071,0.071,0.071,0.071,0.071,0.071,0.071,0.071,0.071,0.074,0.074,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.080,0.080,0.080,0.080,0.080,0.083,0.083,0.086,0.086,0.086,0.086,0.086,0.086,0.089,0.089,0.089,0.089,0.089,0.092,0.092,0.092,0.092,0.092,0.092,0.092,0.092,0.092,0.092,0.092,0.092,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.104,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.110,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.119,0.119,0.119,0.119,0.119,0.119,0.119,0.119,0.119,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.122,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.128,0.128,0.128,0.128,0.128,0.128,0.128,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.131,0.134,0.134,0.134,0.134,0.134,0.134,0.134,0.137,0.137,0.137,0.137,0.140,0.143,0.143,0.146,0.149,0.152,0.152,0.158,0.158,0.164,0.167,0.173,0.173,0.179,0.185,0.191,0.197,0.200,0.206,0.212,0.218,0.227,0.236,0.245,0.257,0.269,0.287,0.311,0.335,0.371,0.407,0.440,0.482,0.506,0.536,0.563,0.584,0.605,0.623,0.641,0.662,0.677,0.692,0.704,0.716,0.728,0.737,0.746,0.755,0.764,0.770,0.782,0.788,0.794,0.800,0.806,0.812,0.818,0.824,0.827,0.833,0.836,0.839,0.845,0.848,0.851,0.854,0.857,0.860,0.863,0.866,0.866,0.869,0.872,0.875,0.875,0.878,0.881,0.881,0.884,0.887,0.887,0.887,0.890,0.890,0.890,0.893,0.893,0.893,0.893,0.893,0.896,0.896,0.896,0.899,0.899,0.899,0.899,0.899,0.899,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.905,0.905,0.905,0.905,0.905,0.905,0.905,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.911,0.911,0.911,0.911,0.911,0.911,0.911,0.911,0.914,0.914,0.914,0.914,0.914,0.914,0.914,0.914,0.917,0.917,0.917,0.917,0.917,0.917,0.920,0.920,0.920,0.920,0.920,0.920,0.920,0.920,0.920,0.920,0.920,0.923,0.923,0.923,0.923,0.923,0.923,0.923,0.926,0.926,0.926,0.926,0.926,0.926,0.926,0.926,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.935,0.935,0.935,0.935,0.935,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.941,0.941,0.941,0.941,0.941,0.941,0.944,0.944,0.944,0.944,0.944,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.950,0.950,0.950,0.950,0.950,0.950,0.953,0.953,0.953,0.953,0.953,0.956,0.956,0.956,0.956,0.956,0.956,0.956,0.956,0.959,0.959,0.959,0.959,0.959,0.959,0.959,0.962,0.962,0.962,0.962,0.962,0.962,0.965,0.965,0.965,0.965,0.965,0.965,0.965,0.968,0.968,0.968,0.968,0.968,0.968,0.971,0.971,0.971,0.971,0.971,0.971,0.974,0.974,0.974,0.974,0.977,0.977,0.977,0.977,0.977,0.980,0.980,0.980,0.983,0.983,0.983,0.986,0.986,0.986,0.986,0.989,0.989,0.989,0.992,0.992,0.992,0.995,0.995,0.998,0.998,1.001,1.004,1.004,1.007,1.010,1.013,1.016,1.019,1.025,1.028,1.034,1.037,1.046,1.052,1.058,1.064,1.073,1.082,1.091,1.097,1.109,1.118,1.127,1.136,1.142,1.151,1.160,1.175,1.181,1.193,1.202,1.214,1.226,1.241,1.250,1.259,1.271,1.277,1.286,1.295,1.301,1.310,1.322,1.328,1.337,1.346,1.358,1.373,1.379,1.382,1.388,1.397,1.403,1.415,1.427,1.427,1.433,1.436,1.439,1.442,1.448,1.454,1.463,1.463,1.466,1.475,1.478,1.481,1.487,1.490,1.490,1.493,1.505,1.511,1.514,1.514,1.517,1.520,1.526,1.526,1.529,1.535,1.538,1.538,1.541,1.547,1.550,1.550,1.556,1.556,1.559,1.568,1.571,1.580,1.580,1.583,1.583,1.586,1.595,1.604,1.610,1.619,1.619,1.622,1.628,1.631,1.634,1.634,1.649,1.652,1.652,1.658,1.667,1.667,1.667,1.670,1.670,1.676,1.676,1.679,1.682,1.685,1.685,1.688,1.688,1.688,1.688,1.691,1.697,1.697,1.700,1.703,1.703,1.706,1.706,1.706,1.709,1.709,1.709,1.709,1.709,1.712,1.712,1.712,1.712,1.712,1.712,1.712,1.712,1.724,1.724,1.727,1.736,1.739,1.739,1.745,1.763,1.763,1.766,1.766,1.766,1.766,1.769,1.769,1.778,1.778,1.784,1.787,1.787,1.787,1.787,1.787,1.787,1.787,1.787,1.787,1.787,1.787,1.787,1.790,1.790,1.796,1.796,1.796,1.796,1.796,1.796,1.805,1.805,1.808,1.808,1.823,1.823,1.823,1.823,1.826,1.826,1.826,1.826,1.838,1.838,1.838,1.838,1.838,1.841,1.841,1.841,1.856,1.856,1.862,1.862,1.862,1.862,1.862,1.862,1.862,1.862,1.862,1.868,1.868,1.868,1.868,1.868,1.871,1.871,1.871,1.877,1.883,1.883,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.889,1.889,1.889,1.889,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.898,1.898,1.898,1.898,1.898,1.898,1.898,1.898,1.898,1.907,1.907,1.907,1.907,1.907,1.913,1.913,1.913,1.916,1.916,1.916,1.916,1.916,1.916,1.916,1.916,1.916,1.937,1.937,1.937,1.937,1.937,1.937,1.949,1.949,1.949,1.949,1.949,1.955,1.955,1.955,1.955,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.961,1.964,1.964,1.964,1.964,1.964,1.967,1.967,1.985,1.985,1.985,1.988,1.991,1.991,1.991,1.991,1.994,1.994,1.994,1.994,1.994,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997},{-0.994,-0.985,-0.976,-0.967,-0.958,-0.943,-0.934,-0.922,-0.907,-0.892,-0.880,-0.862,-0.847,-0.832,-0.817,-0.802,-0.790,-0.778,-0.766,-0.754,-0.745,-0.733,-0.721,-0.709,-0.697,-0.688,-0.679,-0.670,-0.661,-0.652,-0.646,-0.637,-0.628,-0.622,-0.613,-0.607,-0.601,-0.592,-0.586,-0.580,-0.574,-0.568,-0.562,-0.556,-0.550,-0.544,-0.538,-0.532,-0.526,-0.520,-0.517,-0.511,-0.505,-0.502,-0.499,-0.493,-0.487,-0.481,-0.478,-0.475,-0.469,-0.463,-0.460,-0.454,-0.451,-0.448,-0.442,-0.436,-0.433,-0.430,-0.427,-0.421,-0.418,-0.412,-0.409,-0.406,-0.400,-0.397,-0.394,-0.391,-0.388,-0.382,-0.379,-0.376,-0.370,-0.367,-0.361,-0.358,-0.355,-0.352,-0.349,-0.346,-0.343,-0.340,-0.337,-0.334,-0.331,-0.328,-0.322,-0.319,-0.316,-0.313,-0.310,-0.307,-0.304,-0.301,-0.298,-0.295,-0.292,-0.289,-0.286,-0.283,-0.280,-0.277,-0.274,-0.271,-0.268,-0.265,-0.262,-0.259,-0.256,-0.253,-0.250,-0.247,-0.244,-0.241,-0.238,-0.235,-0.232,-0.229,-0.226,-0.223,-0.220,-0.217,-0.214,-0.211,-0.208,-0.205,-0.202,-0.199,-0.196,-0.193,-0.190,-0.187,-0.184,-0.184,-0.181,-0.178,-0.175,-0.172,-0.169,-0.166,-0.163,-0.160,-0.157,-0.154,-0.151,-0.148,-0.145,-0.142,-0.139,-0.136,-0.133,-0.133,-0.130,-0.127,-0.124,-0.121,-0.118,-0.115,-0.115,-0.112,-0.109,-0.106,-0.103,-0.100,-0.097,-0.094,-0.091,-0.091,-0.088,-0.085,-0.082,-0.079,-0.079,-0.076,-0.073,-0.070,-0.067,-0.064,-0.061,-0.061,-0.058,-0.055,-0.052,-0.049,-0.049,-0.046,-0.043,-0.040,-0.037,-0.034,-0.031,-0.028,-0.028,-0.025,-0.022,-0.019,-0.016,-0.016,-0.013,-0.010,-0.007,-0.007,-0.004,-0.001,-0.001,0.002,0.005,0.008,0.011,0.014,0.017,0.020,0.023,0.026,0.026,0.029,0.032,0.035,0.038,0.041,0.041,0.044,0.047,0.050,0.050,0.053,0.056,0.059,0.062,0.062,0.065,0.068,0.071,0.074,0.077,0.080,0.080,0.083,0.086,0.086,0.089,0.092,0.095,0.098,0.101,0.104,0.104,0.107,0.110,0.113,0.116,0.119,0.119,0.122,0.125,0.128,0.131,0.134,0.137,0.137,0.140,0.143,0.146,0.146,0.149,0.155,0.158,0.158,0.161,0.164,0.167,0.170,0.173,0.176,0.179,0.179,0.182,0.188,0.191,0.194,0.197,0.200,0.203,0.206,0.206,0.209,0.212,0.215,0.218,0.221,0.224,0.227,0.230,0.230,0.233,0.236,0.239,0.242,0.245,0.248,0.251,0.254,0.257,0.260,0.263,0.266,0.269,0.272,0.275,0.275,0.278,0.281,0.284,0.287,0.290,0.293,0.296,0.299,0.302,0.305,0.308,0.311,0.314,0.317,0.320,0.323,0.323,0.326,0.329,0.332,0.335,0.338,0.341,0.341,0.344,0.347,0.350,0.353,0.356,0.359,0.362,0.365,0.368,0.371,0.374,0.377,0.380,0.383,0.386,0.389,0.392,0.392,0.395,0.398,0.401,0.404,0.407,0.410,0.413,0.416,0.419,0.422,0.425,0.428,0.431,0.434,0.434,0.437,0.440,0.443,0.446,0.449,0.452,0.455,0.458,0.461,0.461,0.464,0.467,0.470,0.473,0.476,0.479,0.482,0.482,0.485,0.488,0.491,0.494,0.497,0.500,0.503,0.503,0.506,0.509,0.515,0.515,0.521,0.521,0.527,0.530,0.530,0.533,0.536,0.542,0.545,0.545,0.548,0.551,0.554,0.557,0.557,0.560,0.563,0.566,0.569,0.572,0.575,0.578,0.581,0.584,0.587,0.590,0.593,0.596,0.596,0.599,0.602,0.605,0.605,0.608,0.611,0.614,0.617,0.617,0.620,0.623,0.626,0.626,0.629,0.632,0.635,0.638,0.641,0.644,0.644,0.647,0.650,0.653,0.656,0.659,0.659,0.662,0.665,0.668,0.671,0.671,0.674,0.677,0.680,0.683,0.686,0.686,0.689,0.692,0.695,0.698,0.701,0.701,0.704,0.707,0.710,0.710,0.713,0.716,0.719,0.722,0.722,0.725,0.728,0.731,0.731,0.734,0.737,0.737,0.740,0.743,0.746,0.746,0.749,0.752,0.755,0.758,0.758,0.761,0.764,0.767,0.767,0.770,0.773,0.776,0.776,0.779,0.782,0.785,0.788,0.791,0.794,0.794,0.797,0.800,0.800,0.803,0.806,0.806,0.809,0.809,0.812,0.815,0.815,0.818,0.821,0.824,0.827,0.830,0.830,0.833,0.833,0.836,0.839,0.839,0.842,0.845,0.848,0.848,0.851,0.854,0.857,0.857,0.860,0.863,0.866,0.866,0.869,0.872,0.875,0.878,0.881,0.884,0.887,0.890,0.890,0.893,0.896,0.899,0.902,0.905,0.911,0.914,0.917,0.920,0.923,0.926,0.929,0.935,0.938,0.941,0.947,0.953,0.956,0.959,0.965,0.971,0.977,0.980,0.983,0.989,0.995,1.001,1.004,1.010,1.016,1.022,1.031,1.037,1.043,1.049,1.055,1.061,1.067,1.070,1.076,1.085,1.091,1.097,1.103,1.112,1.121,1.127,1.136,1.142,1.151,1.160,1.166,1.178,1.190,1.199,1.208,1.211,1.220,1.229,1.238,1.253,1.262,1.271,1.286,1.292,1.307,1.310,1.325,1.340,1.349,1.361,1.364,1.370,1.382,1.394,1.403,1.418,1.421,1.430,1.439,1.442,1.448,1.451,1.454,1.463,1.469,1.487,1.502,1.511,1.514,1.523,1.532,1.535,1.544,1.547,1.553,1.562,1.571,1.574,1.586,1.589,1.595,1.604,1.607,1.616,1.616,1.622,1.625,1.631,1.634,1.640,1.643,1.649,1.649,1.652,1.655,1.664,1.670,1.673,1.679,1.679,1.682,1.688,1.691,1.694,1.700,1.703,1.709,1.718,1.718,1.727,1.727,1.730,1.733,1.739,1.742,1.745,1.748,1.748,1.751,1.757,1.757,1.760,1.760,1.760,1.769,1.775,1.778,1.778,1.778,1.787,1.787,1.787,1.787,1.787,1.787,1.793,1.793,1.796,1.796,1.796,1.796,1.796,1.799,1.799,1.799,1.808,1.808,1.808,1.811,1.814,1.814,1.814,1.814,1.814,1.823,1.823,1.823,1.826,1.826,1.826,1.829,1.829,1.829,1.829,1.829,1.832,1.832,1.832,1.835,1.835,1.835,1.838,1.841,1.841,1.841,1.841,1.841,1.841,1.841,1.841,1.841,1.841,1.847,1.847,1.847,1.847,1.850,1.850,1.850,1.853,1.853,1.856,1.856,1.856,1.856,1.856,1.856,1.856,1.856,1.856,1.859,1.859,1.859,1.859,1.868,1.868,1.868,1.868,1.868,1.877,1.877,1.877,1.877,1.877,1.877,1.877,1.877,1.883,1.883,1.883,1.883,1.883,1.883,1.883,1.886,1.886,1.886,1.886,1.889,1.889,1.889,1.889,1.889,1.889,1.889,1.889,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.898,1.898,1.898,1.898,1.898,1.898,1.898,1.898,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.913,1.913,1.913,1.913,1.913,1.913,1.913,1.913,1.919,1.919,1.919,1.919,1.919,1.919,1.919,1.919,1.919,1.919,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.931,1.931,1.931,1.931,1.931,1.934,1.934,1.934,1.934,1.934,1.937,1.937,1.937,1.937,1.937,1.937,1.937,1.937,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.946,1.955,1.955,1.955,1.955,1.955,1.955,1.955,1.961,1.961,1.961,1.964,1.964,1.964,1.964,1.964,1.964,1.964,1.964,1.964,1.964,1.964,1.964,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.976,1.976,1.976,1.976,1.976,1.976,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.991,1.991,1.991,1.991,1.991,1.991,1.991,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997},{-0.997,-0.985,-0.976,-0.967,-0.958,-0.952,-0.943,-0.934,-0.925,-0.919,-0.910,-0.904,-0.898,-0.889,-0.883,-0.874,-0.868,-0.862,-0.856,-0.850,-0.841,-0.835,-0.829,-0.820,-0.814,-0.805,-0.799,-0.793,-0.787,-0.781,-0.775,-0.769,-0.763,-0.757,-0.751,-0.745,-0.742,-0.736,-0.730,-0.727,-0.721,-0.718,-0.712,-0.706,-0.703,-0.697,-0.694,-0.688,-0.685,-0.679,-0.676,-0.670,-0.664,-0.658,-0.655,-0.652,-0.646,-0.640,-0.637,-0.631,-0.628,-0.625,-0.619,-0.616,-0.613,-0.607,-0.601,-0.598,-0.595,-0.592,-0.586,-0.583,-0.577,-0.574,-0.571,-0.565,-0.562,-0.559,-0.556,-0.550,-0.547,-0.544,-0.541,-0.535,-0.532,-0.529,-0.526,-0.523,-0.517,-0.514,-0.511,-0.508,-0.505,-0.502,-0.499,-0.493,-0.490,-0.487,-0.481,-0.478,-0.475,-0.472,-0.469,-0.466,-0.460,-0.457,-0.454,-0.451,-0.448,-0.445,-0.439,-0.436,-0.433,-0.430,-0.427,-0.421,-0.418,-0.415,-0.412,-0.409,-0.406,-0.403,-0.400,-0.397,-0.394,-0.388,-0.388,-0.382,-0.379,-0.376,-0.373,-0.370,-0.367,-0.364,-0.358,-0.358,-0.352,-0.349,-0.346,-0.343,-0.340,-0.337,-0.334,-0.331,-0.328,-0.325,-0.322,-0.319,-0.313,-0.310,-0.307,-0.304,-0.301,-0.298,-0.295,-0.292,-0.286,-0.283,-0.280,-0.277,-0.274,-0.271,-0.268,-0.265,-0.262,-0.259,-0.253,-0.250,-0.247,-0.244,-0.241,-0.238,-0.235,-0.232,-0.229,-0.226,-0.223,-0.220,-0.217,-0.214,-0.211,-0.208,-0.205,-0.199,-0.196,-0.193,-0.190,-0.187,-0.184,-0.181,-0.175,-0.172,-0.169,-0.166,-0.163,-0.157,-0.154,-0.151,-0.148,-0.145,-0.142,-0.139,-0.136,-0.133,-0.130,-0.127,-0.124,-0.121,-0.118,-0.115,-0.112,-0.106,-0.103,-0.100,-0.097,-0.094,-0.091,-0.088,-0.082,-0.079,-0.076,-0.073,-0.070,-0.067,-0.064,-0.061,-0.058,-0.055,-0.052,-0.049,-0.046,-0.043,-0.040,-0.037,-0.034,-0.028,-0.025,-0.022,-0.019,-0.016,-0.013,-0.010,-0.004,-0.001,0.002,0.005,0.011,0.011,0.017,0.020,0.023,0.026,0.029,0.035,0.038,0.041,0.044,0.047,0.053,0.056,0.059,0.062,0.068,0.071,0.074,0.077,0.080,0.083,0.086,0.092,0.095,0.098,0.101,0.104,0.107,0.110,0.113,0.116,0.119,0.122,0.125,0.128,0.134,0.137,0.140,0.143,0.146,0.149,0.152,0.155,0.158,0.161,0.161,0.167,0.170,0.173,0.179,0.182,0.185,0.188,0.191,0.194,0.200,0.203,0.206,0.209,0.212,0.215,0.218,0.221,0.227,0.230,0.233,0.239,0.242,0.245,0.248,0.251,0.254,0.257,0.260,0.263,0.269,0.272,0.275,0.278,0.281,0.287,0.293,0.299,0.302,0.305,0.311,0.317,0.320,0.323,0.326,0.332,0.332,0.338,0.341,0.344,0.347,0.356,0.359,0.362,0.368,0.371,0.371,0.374,0.380,0.383,0.383,0.389,0.392,0.395,0.398,0.401,0.404,0.407,0.413,0.419,0.422,0.428,0.431,0.434,0.440,0.443,0.446,0.449,0.452,0.455,0.461,0.464,0.470,0.473,0.476,0.482,0.485,0.491,0.494,0.497,0.500,0.503,0.506,0.509,0.512,0.518,0.521,0.524,0.527,0.530,0.536,0.539,0.542,0.542,0.548,0.551,0.551,0.560,0.560,0.563,0.569,0.572,0.572,0.575,0.581,0.581,0.584,0.584,0.587,0.590,0.596,0.602,0.602,0.608,0.614,0.614,0.617,0.620,0.623,0.626,0.629,0.632,0.635,0.638,0.641,0.641,0.644,0.647,0.653,0.653,0.653,0.656,0.659,0.662,0.662,0.668,0.671,0.674,0.677,0.683,0.686,0.689,0.692,0.692,0.695,0.695,0.698,0.701,0.704,0.704,0.707,0.710,0.710,0.716,0.719,0.722,0.722,0.725,0.728,0.728,0.731,0.731,0.734,0.734,0.737,0.740,0.740,0.740,0.746,0.749,0.755,0.755,0.758,0.764,0.767,0.770,0.770,0.770,0.773,0.776,0.779,0.779,0.782,0.782,0.782,0.785,0.788,0.788,0.791,0.791,0.797,0.797,0.800,0.800,0.803,0.806,0.806,0.806,0.809,0.809,0.812,0.815,0.815,0.815,0.818,0.821,0.824,0.827,0.830,0.833,0.833,0.836,0.839,0.842,0.842,0.842,0.842,0.845,0.848,0.848,0.851,0.851,0.851,0.854,0.854,0.854,0.857,0.857,0.860,0.860,0.863,0.866,0.869,0.869,0.872,0.872,0.875,0.875,0.878,0.881,0.881,0.884,0.887,0.890,0.893,0.896,0.896,0.899,0.899,0.899,0.899,0.905,0.908,0.908,0.911,0.911,0.917,0.923,0.923,0.926,0.935,0.935,0.935,0.947,0.956,0.956,0.956,0.962,0.971,1.001,1.025,1.040,1.040,1.043,1.073,1.100,1.100,1.106,1.106,1.115,1.115,1.124,1.145,1.163,1.229,1.229,1.229,1.238,1.259,1.283,1.283,1.283,1.283,1.283,1.298,1.298,1.352,1.352,1.352,1.397,1.421,1.421,1.421,1.442,1.442,1.442,1.442,1.451,1.601,1.601,1.601,1.631,1.631,1.631,1.631,1.631,1.652,1.652,1.679,1.679,1.679,1.700,1.700,1.700,1.700,1.700,1.718,1.718,1.718,1.718,1.718,1.718,1.718,1.718,1.718,1.718,1.718,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.838,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952,1.952},{-2,-2,-2,-2,-2,-2,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.109,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,-0.031,0.014,0.014,0.014,0.014,0.014,0.014,0.014,0.014,0.014,0.014,0.014,0.014,0.020,0.020,0.020,0.020,0.020,0.020,0.020,0.020,0.020,0.020,0.020,0.041,0.041,0.041,0.041,0.041,0.041,0.041,0.041,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.050,0.050,0.050,0.050,0.050,0.050,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.059,0.059,0.059,0.059,0.059,0.059,0.059,0.062,0.062,0.065,0.065,0.065,0.065,0.068,0.068,0.068,0.068,0.074,0.074,0.077,0.077,0.077,0.080,0.080,0.080,0.083,0.083,0.083,0.083,0.083,0.083,0.086,0.086,0.089,0.089,0.089,0.095,0.095,0.098,0.098,0.098,0.098,0.098,0.104,0.104,0.104,0.107,0.107,0.107,0.116,0.116,0.122,0.122,0.125,0.125,0.128,0.131,0.131,0.131,0.131,0.134,0.134,0.140,0.140,0.146,0.146,0.149,0.149,0.149,0.149,0.149,0.149,0.149,0.149,0.149,0.149,0.158,0.158,0.158,0.158,0.158,0.158,0.158,0.161,0.161,0.161,0.161,0.164,0.170,0.170,0.170,0.170,0.170,0.173,0.173,0.176,0.176,0.176,0.176,0.179,0.179,0.179,0.182,0.185,0.185,0.185,0.185,0.188,0.188,0.188,0.191,0.191,0.191,0.191,0.194,0.194,0.194,0.197,0.197,0.197,0.197,0.197,0.197,0.197,0.200,0.200,0.203,0.203,0.206,0.206,0.206,0.206,0.206,0.209,0.209,0.209,0.212,0.212,0.212,0.212,0.215,0.215,0.218,0.218,0.218,0.224,0.224,0.227,0.227,0.227,0.227,0.227,0.230,0.233,0.233,0.233,0.233,0.236,0.236,0.239,0.242,0.242,0.245,0.245,0.245,0.245,0.251,0.251,0.254,0.260,0.263,0.266,0.269,0.269,0.269,0.269,0.272,0.272,0.275,0.281,0.281,0.284,0.290,0.290,0.293,0.293,0.296,0.296,0.296,0.296,0.299,0.299,0.302,0.305,0.305,0.308,0.308,0.311,0.314,0.314,0.314,0.314,0.317,0.317,0.320,0.320,0.323,0.326,0.326,0.329,0.332,0.332,0.335,0.335,0.338,0.338,0.338,0.338,0.341,0.341,0.341,0.344,0.344,0.347,0.347,0.350,0.350,0.353,0.356,0.356,0.359,0.362,0.365,0.368,0.374,0.374,0.380,0.383,0.386,0.392,0.395,0.401,0.407,0.413,0.416,0.419,0.422,0.428,0.434,0.437,0.446,0.449,0.458,0.461,0.464,0.470,0.473,0.479,0.485,0.488,0.494,0.497,0.503,0.509,0.512,0.515,0.518,0.521,0.527,0.530,0.533,0.536,0.539,0.545,0.548,0.554,0.557,0.560,0.566,0.566,0.569,0.572,0.575,0.581,0.581,0.587,0.587,0.590,0.593,0.596,0.599,0.599,0.602,0.605,0.608,0.611,0.614,0.617,0.620,0.623,0.623,0.626,0.629,0.629,0.632,0.632,0.635,0.635,0.638,0.641,0.644,0.644,0.647,0.650,0.650,0.650,0.653,0.656,0.659,0.659,0.662,0.662,0.665,0.665,0.668,0.668,0.671,0.671,0.674,0.674,0.677,0.677,0.680,0.680,0.683,0.686,0.686,0.689,0.692,0.692,0.692,0.695,0.698,0.701,0.704,0.704,0.707,0.710,0.710,0.713,0.716,0.716,0.719,0.722,0.725,0.728,0.728,0.731,0.734,0.737,0.737,0.740,0.743,0.746,0.746,0.749,0.752,0.755,0.758,0.761,0.761,0.764,0.767,0.770,0.770,0.773,0.776,0.779,0.782,0.785,0.788,0.791,0.794,0.797,0.800,0.803,0.803,0.806,0.809,0.812,0.815,0.818,0.821,0.824,0.824,0.827,0.830,0.833,0.836,0.839,0.839,0.842,0.845,0.848,0.848,0.851,0.854,0.857,0.857,0.860,0.860,0.863,0.866,0.869,0.869,0.872,0.875,0.875,0.878,0.881,0.881,0.884,0.884,0.887,0.890,0.890,0.893,0.896,0.896,0.899,0.899,0.902,0.905,0.908,0.908,0.911,0.911,0.911,0.914,0.914,0.917,0.917,0.920,0.920,0.923,0.923,0.926,0.926,0.929,0.929,0.929,0.932,0.932,0.932,0.935,0.935,0.935,0.938,0.938,0.941,0.941,0.941,0.944,0.944,0.944,0.944,0.947,0.947,0.947,0.947,0.950,0.950,0.950,0.953,0.953,0.953,0.953,0.956,0.956,0.956,0.956,0.956,0.959,0.959,0.959,0.959,0.959,0.959,0.962,0.962,0.962,0.962,0.965,0.965,0.965,0.965,0.965,0.965,0.968,0.968,0.968,0.968,0.968,0.968,0.971,0.971,0.971,0.971,0.971,0.971,0.974,0.974,0.974,0.974,0.974,0.977,0.977,0.977,0.977,0.977,0.977,0.980,0.980,0.980,0.980,0.983,0.983,0.983,0.983,0.983,0.983,0.986,0.986,0.986,0.986,0.989,0.989,0.989,0.989,0.992,0.992,0.992,0.995,0.995,0.995,0.998,0.998,1.001,1.001,1.004,1.004,1.007,1.010,1.010,1.013,1.016,1.016,1.019,1.022,1.025,1.028,1.028,1.031,1.034,1.034,1.037,1.040,1.043,1.049,1.052,1.055,1.058,1.061,1.064,1.067,1.070,1.073,1.076,1.079,1.082,1.085,1.088,1.091,1.091,1.094,1.097,1.097,1.100,1.103,1.106,1.106,1.109,1.112,1.112,1.112,1.115,1.118,1.121,1.121,1.124,1.127,1.130,1.133,1.136,1.136,1.139,1.142,1.145,1.148,1.151,1.154,1.157,1.160,1.163,1.166,1.166,1.169,1.169,1.172,1.175,1.178,1.178,1.181,1.184,1.184,1.187,1.190,1.190,1.193,1.199,1.202,1.205,1.208,1.211,1.214,1.214,1.217,1.217,1.217,1.223,1.226,1.232,1.232,1.235,1.241,1.244,1.247,1.250,1.253,1.256,1.256,1.256,1.259,1.265,1.268,1.271,1.277,1.280,1.283,1.289,1.292,1.292,1.292,1.301,1.304,1.310,1.310,1.313,1.313,1.313,1.316,1.316,1.316,1.316,1.319,1.319,1.322,1.325,1.325,1.328,1.328,1.331,1.334,1.337,1.337,1.340,1.343,1.346,1.349,1.373,1.382,1.382,1.382,1.382,1.385,1.385,1.388,1.388,1.394,1.397,1.400,1.400,1.403,1.406,1.412,1.412,1.412,1.412,1.415,1.415,1.421,1.421,1.421,1.424,1.424,1.424,1.424,1.424,1.424,1.433,1.433,1.442,1.442,1.442,1.442,1.445,1.448,1.448,1.451,1.451,1.457,1.463,1.469,1.469,1.469,1.484,1.484,1.490,1.493,1.493,1.493,1.493,1.496,1.496,1.496,1.496,1.496,1.505,1.505,1.517,1.517,1.520,1.520,1.523,1.523,1.523,1.523,1.529,1.529,1.529,1.544,1.571,1.571,1.577,1.577,1.577,1.580,1.580,1.580,1.580,1.580,1.589,1.589,1.610,1.610,1.619,1.619,1.619,1.619,1.619,1.619,1.622,1.622,1.622,1.622,1.646,1.646,1.646,1.676,1.679,1.679,1.688,1.688,1.688,1.688,1.688,1.694,1.694,1.697,1.697,1.697,1.709,1.709,1.709,1.715,1.715,1.715,1.715,1.724,1.724,1.724,1.736,1.736,1.736,1.736,1.745,1.745,1.748,1.748,1.748,1.760,1.760,1.760,1.763,1.763,1.763,1.763,1.766,1.766,1.766,1.766,1.772,1.772,1.781,1.781,1.781,1.781,1.781,1.814,1.814,1.826,1.826,1.826,1.826,1.826,1.826,1.826,1.847,1.847,1.847,1.895,1.895,1.895,1.895,1.895,1.898,1.898,1.898,1.901,1.901,1.901,1.901,1.904,1.904,1.904,1.925,1.925,1.925,1.925,1.925,1.925,1.925,1.925,1.925,1.925,1.955,1.955,1.955,1.955,1.958,1.958,1.958,1.958,1.958,1.976,1.976,1.976},{-2,-2,-2,-2,-2,-0.442,-0.442,-0.442,-0.442,-0.442,-0.442,-0.442,-0.424,-0.424,-0.418,-0.418,-0.418,-0.418,-0.403,-0.394,-0.394,-0.394,-0.394,-0.319,-0.319,-0.298,-0.298,-0.292,-0.286,-0.286,-0.286,-0.283,-0.283,-0.283,-0.280,-0.280,-0.280,-0.280,-0.274,-0.274,-0.268,-0.265,-0.265,-0.262,-0.262,-0.259,-0.259,-0.256,-0.247,-0.241,-0.241,-0.238,-0.238,-0.235,-0.220,-0.208,-0.202,-0.202,-0.199,-0.196,-0.196,-0.193,-0.190,-0.190,-0.187,-0.181,-0.181,-0.178,-0.178,-0.175,-0.166,-0.166,-0.166,-0.166,-0.163,-0.163,-0.163,-0.160,-0.160,-0.160,-0.160,-0.157,-0.154,-0.151,-0.151,-0.148,-0.142,-0.139,-0.139,-0.136,-0.133,-0.133,-0.130,-0.130,-0.127,-0.127,-0.124,-0.121,-0.115,-0.112,-0.112,-0.112,-0.109,-0.106,-0.106,-0.106,-0.100,-0.094,-0.085,-0.085,-0.085,-0.082,-0.076,-0.073,-0.073,-0.070,-0.070,-0.067,-0.067,-0.061,-0.058,-0.058,-0.055,-0.052,-0.052,-0.049,-0.046,-0.046,-0.046,-0.046,-0.040,-0.040,-0.037,-0.034,-0.034,-0.031,-0.028,-0.028,-0.022,-0.022,-0.019,-0.016,-0.016,-0.013,-0.013,-0.010,-0.004,-0.004,0.005,0.011,0.014,0.017,0.020,0.020,0.023,0.026,0.026,0.032,0.035,0.038,0.041,0.041,0.041,0.044,0.047,0.047,0.050,0.053,0.056,0.059,0.059,0.062,0.065,0.068,0.071,0.071,0.074,0.080,0.083,0.083,0.086,0.089,0.095,0.098,0.101,0.104,0.107,0.110,0.110,0.113,0.116,0.119,0.122,0.125,0.128,0.131,0.131,0.134,0.134,0.137,0.140,0.143,0.146,0.146,0.149,0.152,0.152,0.155,0.158,0.158,0.161,0.161,0.167,0.170,0.173,0.179,0.179,0.182,0.185,0.188,0.188,0.191,0.194,0.200,0.203,0.209,0.212,0.215,0.218,0.221,0.224,0.230,0.233,0.236,0.239,0.242,0.245,0.245,0.248,0.251,0.251,0.257,0.260,0.263,0.266,0.269,0.269,0.272,0.275,0.278,0.278,0.281,0.284,0.287,0.290,0.290,0.293,0.296,0.299,0.302,0.305,0.308,0.308,0.311,0.314,0.317,0.317,0.320,0.323,0.326,0.326,0.329,0.332,0.335,0.338,0.341,0.341,0.344,0.347,0.350,0.350,0.353,0.356,0.359,0.359,0.362,0.365,0.365,0.368,0.371,0.371,0.377,0.380,0.383,0.383,0.386,0.389,0.392,0.392,0.398,0.401,0.404,0.404,0.407,0.410,0.410,0.413,0.416,0.419,0.422,0.425,0.428,0.428,0.431,0.434,0.437,0.440,0.443,0.446,0.449,0.452,0.455,0.455,0.458,0.461,0.464,0.467,0.470,0.470,0.473,0.476,0.476,0.479,0.482,0.485,0.488,0.491,0.494,0.494,0.497,0.500,0.503,0.503,0.506,0.509,0.512,0.512,0.515,0.518,0.521,0.524,0.527,0.527,0.530,0.533,0.533,0.536,0.539,0.539,0.542,0.542,0.545,0.548,0.548,0.551,0.551,0.554,0.554,0.557,0.560,0.563,0.566,0.566,0.569,0.572,0.572,0.575,0.578,0.578,0.581,0.584,0.587,0.590,0.593,0.593,0.596,0.596,0.599,0.602,0.605,0.608,0.608,0.611,0.614,0.617,0.620,0.620,0.623,0.623,0.626,0.626,0.629,0.629,0.632,0.635,0.635,0.638,0.641,0.644,0.647,0.647,0.650,0.653,0.656,0.656,0.659,0.662,0.662,0.665,0.668,0.671,0.674,0.677,0.680,0.683,0.683,0.686,0.689,0.692,0.692,0.695,0.695,0.698,0.698,0.701,0.701,0.704,0.704,0.707,0.707,0.710,0.713,0.713,0.716,0.719,0.719,0.722,0.725,0.725,0.725,0.728,0.728,0.731,0.731,0.734,0.737,0.737,0.740,0.743,0.746,0.746,0.749,0.752,0.752,0.755,0.755,0.758,0.761,0.764,0.764,0.767,0.770,0.770,0.773,0.773,0.776,0.779,0.782,0.782,0.782,0.785,0.785,0.788,0.788,0.791,0.791,0.794,0.794,0.797,0.800,0.800,0.800,0.803,0.803,0.806,0.809,0.809,0.812,0.812,0.815,0.815,0.818,0.818,0.821,0.821,0.824,0.827,0.827,0.830,0.830,0.830,0.833,0.836,0.836,0.839,0.839,0.842,0.842,0.845,0.848,0.848,0.848,0.851,0.854,0.854,0.857,0.857,0.860,0.860,0.863,0.863,0.866,0.869,0.872,0.872,0.872,0.875,0.875,0.875,0.878,0.878,0.878,0.881,0.881,0.884,0.887,0.887,0.890,0.890,0.893,0.893,0.896,0.899,0.899,0.902,0.905,0.905,0.908,0.908,0.908,0.911,0.911,0.914,0.917,0.917,0.917,0.920,0.923,0.923,0.923,0.926,0.929,0.932,0.932,0.932,0.932,0.935,0.935,0.938,0.941,0.941,0.944,0.947,0.947,0.947,0.950,0.950,0.953,0.956,0.956,0.959,0.962,0.962,0.968,0.968,0.974,0.977,0.980,0.980,0.986,0.989,0.992,0.992,1.001,1.001,1.007,1.010,1.010,1.016,1.019,1.025,1.025,1.025,1.028,1.031,1.034,1.043,1.043,1.049,1.052,1.061,1.061,1.061,1.061,1.064,1.064,1.070,1.076,1.076,1.082,1.085,1.085,1.088,1.088,1.088,1.091,1.094,1.094,1.094,1.097,1.112,1.112,1.115,1.133,1.133,1.136,1.136,1.136,1.139,1.145,1.145,1.145,1.145,1.151,1.151,1.157,1.157,1.157,1.172,1.172,1.178,1.178,1.190,1.190,1.217,1.217,1.238,1.241,1.241,1.241,1.262,1.262,1.262,1.283,1.283,1.283,1.289,1.289,1.289,1.289,1.289,1.289,1.292,1.292,1.292,1.292,1.292,1.310,1.310,1.310,1.310,1.331,1.331,1.331,1.331,1.331,1.331,1.331,1.388,1.388,1.388,1.388,1.388,1.388,1.388,1.388,1.388,1.388,1.388,1.388,1.451,1.451,1.451,1.451,1.451,1.451,1.451,1.451,1.451,1.451,1.451,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.460,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.499,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.589,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.628,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.742,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.754,1.793,1.793,1.793,1.793,1.793,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823,1.823}};

float CorrectUpsilon_QCD(float Y, int pantau){
int bin =  ((Y+1.000)/3.000)*1000;
return (Y<2.000) ? YCorr_QCD[pantau][bin] : -2 ;
}
