///CorrectUpsilon_WCR(Y,pantau) - returns corrected Y value obtained from
///Smirnof transform between anti-tau -> tau
const float YCorr_WCR[5][1000] = {{-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.065,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.074,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.080,0.080,0.080,0.080,0.080,0.080,0.080,0.080,0.080,0.080,0.080,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.086,0.086,0.089,0.089,0.089,0.089,0.089,0.089,0.086,0.098,0.098,0.098,0.107,0.107,0.113,0.116,0.122,0.125,0.131,0.134,0.137,0.140,0.143,0.146,0.149,0.152,0.158,0.158,0.164,0.170,0.173,0.179,0.182,0.191,0.197,0.203,0.209,0.215,0.218,0.224,0.230,0.239,0.245,0.251,0.260,0.269,0.278,0.293,0.317,0.362,0.419,0.464,0.515,0.572,0.614,0.641,0.671,0.698,0.719,0.746,0.761,0.773,0.788,0.803,0.812,0.827,0.839,0.851,0.857,0.866,0.872,0.875,0.881,0.887,0.890,0.896,0.899,0.902,0.905,0.908,0.911,0.911,0.914,0.917,0.917,0.920,0.920,0.920,0.923,0.923,0.923,0.923,0.926,0.926,0.926,0.926,0.926,0.926,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.929,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.932,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.935,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.938,0.941,0.941,0.941,0.941,0.941,0.941,0.941,0.941,0.941,0.941,0.941,0.941,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.944,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.947,0.950,0.950,0.950,0.950,0.950,0.950,0.950,0.950,0.950,0.950,0.953,0.953,0.953,0.953,0.953,0.953,0.953,0.953,0.953,0.953,0.953,0.956,0.956,0.956,0.956,0.956,0.956,0.956,0.956,0.956,0.956,0.959,0.959,0.959,0.959,0.959,0.959,0.959,0.959,0.959,0.959,0.962,0.962,0.962,0.962,0.962,0.962,0.962,0.962,0.965,0.965,0.965,0.965,0.965,0.965,0.965,0.965,0.968,0.968,0.968,0.968,0.968,0.968,0.971,0.971,0.971,0.971,0.971,0.971,0.971,0.974,0.974,0.974,0.974,0.974,0.977,0.977,0.977,0.977,0.977,0.980,0.980,0.980,0.980,0.980,0.980,0.983,0.983,0.983,0.986,0.986,0.986,0.989,0.989,0.992,0.992,0.995,0.995,0.995,0.998,1.001,1.001,1.004,1.007,1.010,1.010,1.013,1.019,1.022,1.025,1.031,1.037,1.043,1.049,1.055,1.064,1.073,1.082,1.091,1.103,1.115,1.133,1.145,1.157,1.175,1.193,1.211,1.223,1.238,1.247,1.268,1.310,1.322,1.334,1.358,1.373,1.385,1.397,1.418,1.439,1.454,1.466,1.475,1.478,1.487,1.493,1.502,1.505,1.514,1.520,1.523,1.538,1.550,1.550,1.553,1.556,1.562,1.562,1.568,1.574,1.589,1.592,1.589,1.595,1.610,1.610,1.616,1.619,1.631,1.631,1.649,1.652,1.661,1.664,1.667,1.670,1.679,1.682,1.682,1.685,1.688,1.688,1.688,1.691,1.691,1.691,1.691,1.691,1.694,1.694,1.700,1.700,1.703,1.703,1.706,1.715,1.715,1.715,1.727,1.727,1.730,1.730,1.733,1.733,1.733,1.733,1.736,1.736,1.736,1.736,1.739,1.739,1.742,1.745,1.745,1.748,1.748,1.751,1.751,1.751,1.751,1.751,1.751,1.760,1.760,1.763,1.763,1.763,1.763,1.766,1.766,1.766,1.766,1.763,1.763,1.763,1.763,1.763,1.766,1.766,1.766,1.766,1.766,1.769,1.769,1.769,1.769,1.769,1.775,1.775,1.781,1.781,1.781,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.793,1.793,1.793,1.793,1.793,1.811,1.811,1.811,1.811,1.814,1.814,1.814,1.820,1.820,1.820,1.823,1.823,1.826,1.826,1.826,1.832,1.832,1.832,1.832,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.835,1.841,1.841,1.841,1.841,1.841,1.841,1.841,1.847,1.850,1.850,1.853,1.853,1.853,1.856,1.862,1.862,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.868,1.874,1.880,1.880,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.889,1.889,1.892,1.892,1.892,1.892,1.895,1.895,1.895,1.895,1.895,1.895,1.895,1.895,1.895,1.964,1.967,1.967,1.967,1.967,1.967,1.967,1.970,1.970,1.970,1.967,1.967,1.967,1.967,1.967,1.970,1.970,1.970,1.970,1.970,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.982,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997},{-2,-0.985,-0.985,-0.967,-0.964,-0.964,-0.961,-0.958,-0.952,-0.949,-0.943,-0.937,-0.931,-0.922,-0.913,-0.907,-0.898,-0.886,-0.871,-0.859,-0.838,-0.820,-0.799,-0.781,-0.760,-0.739,-0.721,-0.709,-0.688,-0.679,-0.667,-0.655,-0.649,-0.640,-0.631,-0.625,-0.616,-0.607,-0.598,-0.589,-0.580,-0.568,-0.562,-0.553,-0.544,-0.538,-0.529,-0.526,-0.514,-0.508,-0.502,-0.496,-0.490,-0.481,-0.475,-0.469,-0.463,-0.457,-0.451,-0.445,-0.439,-0.433,-0.430,-0.424,-0.418,-0.412,-0.406,-0.403,-0.397,-0.391,-0.385,-0.382,-0.376,-0.373,-0.370,-0.367,-0.361,-0.352,-0.349,-0.346,-0.340,-0.337,-0.334,-0.331,-0.325,-0.319,-0.319,-0.313,-0.310,-0.304,-0.301,-0.298,-0.295,-0.292,-0.289,-0.286,-0.280,-0.277,-0.274,-0.271,-0.268,-0.265,-0.259,-0.256,-0.253,-0.247,-0.244,-0.241,-0.238,-0.235,-0.229,-0.226,-0.223,-0.220,-0.217,-0.214,-0.211,-0.205,-0.205,-0.202,-0.199,-0.196,-0.193,-0.187,-0.184,-0.181,-0.178,-0.175,-0.172,-0.169,-0.166,-0.160,-0.157,-0.157,-0.154,-0.145,-0.142,-0.139,-0.136,-0.133,-0.130,-0.127,-0.124,-0.118,-0.115,-0.115,-0.112,-0.106,-0.103,-0.103,-0.100,-0.097,-0.094,-0.091,-0.088,-0.085,-0.085,-0.082,-0.079,-0.073,-0.070,-0.067,-0.064,-0.064,-0.058,-0.055,-0.052,-0.049,-0.049,-0.046,-0.040,-0.040,-0.037,-0.034,-0.028,-0.028,-0.025,-0.022,-0.016,-0.013,-0.010,-0.007,-0.004,-0.001,0.002,0.005,0.008,0.011,0.014,0.017,0.017,0.023,0.026,0.026,0.029,0.032,0.035,0.038,0.041,0.044,0.047,0.050,0.050,0.056,0.056,0.059,0.062,0.065,0.068,0.068,0.071,0.074,0.077,0.077,0.080,0.083,0.086,0.089,0.092,0.092,0.095,0.098,0.101,0.104,0.107,0.110,0.113,0.116,0.116,0.119,0.122,0.122,0.128,0.128,0.131,0.134,0.134,0.137,0.140,0.143,0.146,0.149,0.152,0.152,0.155,0.158,0.161,0.164,0.164,0.167,0.170,0.173,0.176,0.179,0.179,0.182,0.185,0.188,0.191,0.194,0.197,0.200,0.203,0.209,0.209,0.212,0.215,0.218,0.221,0.224,0.227,0.230,0.233,0.233,0.236,0.239,0.239,0.242,0.245,0.248,0.251,0.251,0.254,0.257,0.260,0.263,0.263,0.266,0.269,0.272,0.272,0.275,0.278,0.278,0.281,0.284,0.287,0.287,0.290,0.293,0.296,0.299,0.299,0.302,0.305,0.308,0.308,0.311,0.314,0.314,0.317,0.323,0.323,0.326,0.329,0.332,0.335,0.338,0.341,0.341,0.347,0.347,0.350,0.353,0.356,0.359,0.362,0.362,0.365,0.368,0.371,0.374,0.374,0.377,0.380,0.383,0.386,0.389,0.392,0.392,0.395,0.398,0.401,0.404,0.407,0.410,0.410,0.413,0.416,0.419,0.422,0.425,0.428,0.431,0.434,0.437,0.437,0.440,0.443,0.446,0.449,0.452,0.455,0.458,0.461,0.464,0.464,0.473,0.473,0.476,0.479,0.479,0.482,0.485,0.488,0.491,0.494,0.497,0.497,0.500,0.503,0.506,0.509,0.509,0.512,0.515,0.515,0.518,0.521,0.521,0.524,0.527,0.527,0.530,0.533,0.533,0.536,0.539,0.542,0.542,0.545,0.548,0.548,0.551,0.554,0.554,0.557,0.560,0.560,0.563,0.566,0.566,0.569,0.572,0.575,0.578,0.578,0.581,0.584,0.587,0.590,0.590,0.593,0.593,0.596,0.599,0.602,0.602,0.605,0.608,0.608,0.611,0.614,0.614,0.617,0.620,0.620,0.626,0.626,0.629,0.632,0.635,0.635,0.638,0.641,0.644,0.644,0.647,0.650,0.650,0.653,0.656,0.659,0.659,0.662,0.665,0.665,0.668,0.671,0.671,0.674,0.677,0.680,0.680,0.683,0.683,0.686,0.689,0.689,0.692,0.692,0.695,0.698,0.698,0.701,0.704,0.704,0.707,0.710,0.710,0.713,0.713,0.716,0.719,0.719,0.722,0.725,0.725,0.728,0.731,0.731,0.734,0.737,0.737,0.740,0.740,0.743,0.746,0.746,0.749,0.749,0.749,0.752,0.755,0.755,0.758,0.758,0.761,0.761,0.764,0.767,0.767,0.770,0.770,0.773,0.776,0.779,0.779,0.782,0.782,0.785,0.785,0.788,0.791,0.791,0.794,0.797,0.797,0.800,0.803,0.803,0.806,0.809,0.809,0.812,0.815,0.815,0.815,0.818,0.818,0.821,0.821,0.824,0.827,0.827,0.830,0.830,0.833,0.833,0.836,0.836,0.839,0.839,0.842,0.842,0.845,0.848,0.848,0.851,0.851,0.851,0.854,0.857,0.860,0.863,0.866,0.866,0.869,0.872,0.872,0.875,0.878,0.881,0.884,0.884,0.887,0.890,0.890,0.893,0.896,0.896,0.902,0.905,0.908,0.911,0.911,0.914,0.917,0.920,0.923,0.926,0.929,0.932,0.932,0.935,0.938,0.944,0.947,0.950,0.953,0.956,0.959,0.962,0.971,0.977,0.983,0.986,0.989,0.995,0.998,1.001,1.010,1.013,1.019,1.025,1.031,1.034,1.037,1.043,1.049,1.052,1.058,1.061,1.064,1.070,1.073,1.076,1.082,1.085,1.088,1.091,1.100,1.106,1.112,1.115,1.127,1.133,1.142,1.145,1.154,1.154,1.160,1.181,1.187,1.193,1.196,1.208,1.211,1.223,1.238,1.247,1.259,1.268,1.277,1.280,1.289,1.289,1.292,1.307,1.322,1.328,1.334,1.337,1.343,1.349,1.373,1.376,1.388,1.400,1.403,1.409,1.418,1.439,1.442,1.457,1.463,1.466,1.481,1.490,1.493,1.496,1.508,1.514,1.517,1.547,1.562,1.568,1.568,1.568,1.571,1.580,1.580,1.583,1.589,1.595,1.601,1.622,1.625,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.640,1.646,1.646,1.646,1.670,1.676,1.679,1.685,1.688,1.688,1.688,1.688,1.697,1.697,1.697,1.703,1.712,1.712,1.712,1.721,1.721,1.724,1.724,1.727,1.727,1.727,1.727,1.727,1.733,1.733,1.745,1.748,1.748,1.748,1.748,1.751,1.751,1.751,1.757,1.757,1.766,1.769,1.775,1.781,1.781,1.781,1.781,1.784,1.784,1.784,1.784,1.784,1.784,1.784,1.784,1.790,1.790,1.790,1.790,1.790,1.790,1.790,1.793,1.793,1.793,1.793,1.793,1.793,1.793,1.793,1.799,1.799,1.799,1.805,1.805,1.805,1.805,1.808,1.808,1.808,1.808,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.844,1.844,1.844,1.844,1.847,1.847,1.847,1.850,1.850,1.850,1.871,1.871,1.871,1.871,1.880,1.880,1.880,1.880,1.880,1.880,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.889,1.889,1.889,1.889,1.889,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.892,1.901,1.901,1.901,1.901,1.907,1.907,1.907,1.907,1.907,1.907,1.907,1.907,1.907,1.907,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.922,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.940,1.958,1.964,1.964,1.964,1.964,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.967,1.970,1.970,1.970,1.970,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.973,1.976,1.976,1.976,1.976,1.976,1.976,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.979,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.994,1.997,1.997,1.997,1.997,1.997,1.997,1.997,1.997},{-2,-0.991,-0.979,-0.976,-0.970,-0.964,-0.955,-0.952,-0.946,-0.934,-0.928,-0.925,-0.919,-0.916,-0.907,-0.901,-0.895,-0.883,-0.874,-0.865,-0.856,-0.847,-0.835,-0.826,-0.814,-0.805,-0.793,-0.784,-0.775,-0.769,-0.760,-0.751,-0.745,-0.736,-0.730,-0.724,-0.715,-0.709,-0.703,-0.697,-0.691,-0.685,-0.679,-0.673,-0.667,-0.664,-0.658,-0.652,-0.646,-0.643,-0.637,-0.631,-0.625,-0.622,-0.616,-0.613,-0.610,-0.604,-0.601,-0.595,-0.592,-0.586,-0.580,-0.577,-0.571,-0.568,-0.562,-0.559,-0.556,-0.553,-0.550,-0.547,-0.541,-0.538,-0.535,-0.532,-0.526,-0.523,-0.517,-0.514,-0.511,-0.508,-0.505,-0.502,-0.499,-0.493,-0.490,-0.487,-0.484,-0.478,-0.472,-0.469,-0.466,-0.460,-0.457,-0.454,-0.451,-0.448,-0.442,-0.439,-0.436,-0.433,-0.427,-0.424,-0.421,-0.418,-0.415,-0.412,-0.409,-0.406,-0.403,-0.400,-0.397,-0.394,-0.391,-0.388,-0.385,-0.382,-0.379,-0.376,-0.373,-0.367,-0.367,-0.364,-0.361,-0.358,-0.355,-0.352,-0.349,-0.346,-0.343,-0.337,-0.334,-0.331,-0.328,-0.325,-0.322,-0.319,-0.316,-0.313,-0.310,-0.307,-0.304,-0.301,-0.298,-0.295,-0.292,-0.289,-0.286,-0.283,-0.280,-0.277,-0.277,-0.274,-0.271,-0.265,-0.262,-0.259,-0.256,-0.253,-0.250,-0.247,-0.244,-0.241,-0.238,-0.235,-0.232,-0.229,-0.226,-0.223,-0.220,-0.220,-0.217,-0.214,-0.211,-0.208,-0.208,-0.205,-0.202,-0.199,-0.196,-0.193,-0.190,-0.187,-0.184,-0.178,-0.175,-0.175,-0.172,-0.166,-0.163,-0.160,-0.160,-0.157,-0.154,-0.148,-0.148,-0.145,-0.142,-0.139,-0.136,-0.133,-0.130,-0.127,-0.124,-0.121,-0.118,-0.115,-0.112,-0.109,-0.106,-0.103,-0.100,-0.097,-0.094,-0.091,-0.088,-0.085,-0.082,-0.079,-0.076,-0.073,-0.073,-0.070,-0.067,-0.064,-0.061,-0.058,-0.055,-0.052,-0.049,-0.046,-0.043,-0.040,-0.037,-0.031,-0.028,-0.025,-0.022,-0.022,-0.019,-0.016,-0.013,-0.010,-0.007,-0.004,-0.001,0.002,0.005,0.008,0.011,0.014,0.020,0.023,0.026,0.029,0.032,0.035,0.035,0.041,0.044,0.047,0.050,0.053,0.056,0.059,0.062,0.065,0.068,0.071,0.071,0.074,0.083,0.083,0.086,0.089,0.095,0.095,0.098,0.101,0.104,0.107,0.110,0.113,0.116,0.119,0.122,0.125,0.128,0.128,0.131,0.134,0.137,0.140,0.143,0.146,0.149,0.152,0.155,0.158,0.161,0.164,0.167,0.170,0.173,0.176,0.179,0.182,0.185,0.188,0.191,0.191,0.194,0.200,0.203,0.206,0.209,0.212,0.215,0.218,0.221,0.224,0.227,0.233,0.236,0.239,0.242,0.245,0.248,0.257,0.260,0.263,0.266,0.269,0.272,0.275,0.278,0.281,0.287,0.290,0.296,0.299,0.302,0.305,0.305,0.308,0.314,0.314,0.317,0.320,0.323,0.329,0.332,0.335,0.338,0.341,0.344,0.347,0.350,0.350,0.353,0.359,0.362,0.365,0.368,0.371,0.377,0.377,0.386,0.389,0.395,0.401,0.404,0.407,0.413,0.422,0.425,0.428,0.440,0.440,0.446,0.449,0.452,0.458,0.461,0.464,0.470,0.473,0.479,0.482,0.485,0.488,0.497,0.497,0.503,0.506,0.509,0.512,0.515,0.521,0.530,0.530,0.536,0.539,0.548,0.551,0.554,0.557,0.557,0.563,0.569,0.575,0.584,0.587,0.590,0.593,0.599,0.608,0.611,0.614,0.617,0.620,0.623,0.626,0.626,0.632,0.632,0.635,0.641,0.647,0.650,0.650,0.656,0.656,0.656,0.662,0.665,0.665,0.665,0.668,0.671,0.677,0.677,0.677,0.680,0.689,0.692,0.692,0.695,0.698,0.713,0.713,0.716,0.716,0.719,0.719,0.725,0.731,0.731,0.731,0.731,0.734,0.737,0.737,0.743,0.746,0.749,0.752,0.752,0.761,0.764,0.767,0.767,0.767,0.770,0.773,0.773,0.776,0.779,0.785,0.788,0.788,0.788,0.791,0.791,0.794,0.794,0.794,0.794,0.797,0.797,0.797,0.797,0.797,0.797,0.797,0.800,0.803,0.803,0.803,0.803,0.803,0.803,0.803,0.803,0.803,0.806,0.806,0.806,0.806,0.812,0.812,0.812,0.812,0.812,0.815,0.815,0.815,0.818,0.821,0.821,0.821,0.824,0.824,0.824,0.824,0.830,0.830,0.830,0.833,0.833,0.833,0.833,0.833,0.833,0.833,0.833,0.836,0.839,0.842,0.845,0.845,0.848,0.848,0.848,0.848,0.863,0.863,0.863,0.863,0.863,0.863,0.863,0.863,0.863,0.863,0.866,0.866,0.866,0.866,0.866,0.866,0.866,0.866,0.866,0.866,0.866,0.866,0.869,0.869,0.869,0.869,0.869,0.869,0.872,0.872,0.878,0.878,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.881,0.884,0.887,0.887,0.887,0.887,0.887,0.887,0.887,0.887,0.887,0.887,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.890,0.896,0.896,0.896,0.896,0.896,0.896,0.899,0.899,0.899,0.899,0.899,0.899,0.899,0.899,0.899,0.899,0.899,0.899,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.902,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908,0.908},{-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1.000,-1.000,-1.000,-1.000,-1.000,-1.000,-1.000,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.089,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.101,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.104,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.107,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.113,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.116,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.137,0.137,0.137,0.137,0.137,0.137,0.137,0.137,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.140,0.143,0.143,0.152,0.152,0.152,0.155,0.155,0.155,0.158,0.161,0.161,0.170,0.173,0.176,0.176,0.179,0.188,0.191,0.206,0.212,0.224,0.236,0.248,0.254,0.260,0.272,0.281,0.305,0.314,0.332,0.353,0.377,0.386,0.398,0.410,0.422,0.434,0.443,0.455,0.461,0.473,0.479,0.488,0.494,0.500,0.512,0.521,0.527,0.530,0.536,0.545,0.551,0.554,0.557,0.563,0.566,0.572,0.575,0.581,0.587,0.590,0.593,0.599,0.602,0.605,0.611,0.617,0.620,0.626,0.629,0.635,0.638,0.641,0.647,0.650,0.656,0.659,0.665,0.668,0.671,0.677,0.680,0.686,0.689,0.692,0.695,0.698,0.701,0.704,0.707,0.713,0.716,0.719,0.722,0.725,0.728,0.731,0.731,0.734,0.737,0.737,0.740,0.740,0.743,0.746,0.746,0.749,0.749,0.749,0.752,0.752,0.755,0.758,0.758,0.761,0.761,0.764,0.764,0.764,0.767,0.767,0.770,0.770,0.773,0.773,0.776,0.776,0.779,0.779,0.782,0.782,0.782,0.785,0.788,0.788,0.791,0.791,0.794,0.797,0.797,0.797,0.800,0.800,0.803,0.806,0.806,0.809,0.809,0.812,0.812,0.815,0.815,0.818,0.821,0.821,0.827,0.827,0.830,0.830,0.833,0.836,0.839,0.839,0.842,0.842,0.845,0.848,0.848,0.851,0.854,0.854,0.857,0.860,0.863,0.863,0.866,0.869,0.869,0.872,0.875,0.875,0.878,0.881,0.881,0.884,0.887,0.887,0.890,0.890,0.893,0.896,0.896,0.896,0.899,0.899,0.902,0.902,0.905,0.908,0.908,0.911,0.911,0.911,0.914,0.914,0.917,0.917,0.917,0.920,0.920,0.923,0.923,0.923,0.926,0.926,0.926,0.929,0.929,0.929,0.929,0.932,0.932,0.935,0.935,0.935,0.935,0.938,0.938,0.938,0.941,0.941,0.941,0.941,0.944,0.944,0.944,0.944,0.947,0.947,0.947,0.947,0.950,0.950,0.950,0.950,0.950,0.953,0.953,0.953,0.953,0.953,0.956,0.956,0.956,0.956,0.956,0.956,0.959,0.959,0.959,0.959,0.959,0.959,0.959,0.962,0.962,0.962,0.962,0.962,0.965,0.965,0.965,0.965,0.965,0.965,0.965,0.968,0.968,0.968,0.968,0.968,0.968,0.971,0.971,0.971,0.971,0.971,0.971,0.971,0.974,0.974,0.974,0.974,0.974,0.974,0.977,0.977,0.977,0.977,0.977,0.977,0.980,0.980,0.980,0.980,0.980,0.983,0.983,0.983,0.983,0.986,0.986,0.986,0.989,0.989,0.989,0.992,0.992,0.995,0.995,0.998,1.001,1.001,1.004,1.004,1.007,1.010,1.010,1.013,1.013,1.016,1.016,1.019,1.022,1.022,1.022,1.025,1.025,1.025,1.028,1.028,1.028,1.028,1.028,1.031,1.034,1.034,1.082,1.085,1.088,1.094,1.097,1.100,1.103,1.106,1.109,1.124,1.133,1.136,1.139,1.142,1.145,1.151,1.157,1.160,1.163,1.172,1.175,1.175,1.178,1.181,1.181,1.187,1.187,1.196,1.199,1.202,1.205,1.208,1.217,1.220,1.226,1.235,1.235,1.235,1.241,1.247,1.250,1.250,1.259,1.259,1.259,1.259,1.262,1.265,1.268,1.271,1.280,1.289,1.289,1.295,1.301,1.304,1.304,1.304,1.310,1.313,1.319,1.322,1.334,1.334,1.334,1.394,1.400,1.400,1.400,1.418,1.424,1.430,1.433,1.433,1.436,1.439,1.439,1.448,1.454,1.454,1.457,1.460,1.460,1.484,1.484,1.484,1.484,1.487,1.487,1.505,1.505,1.508,1.511,1.511,1.520,1.523,1.523,1.523,1.529,1.529,1.529,1.535,1.535,1.535,1.568,1.568,1.580,1.580,1.586,1.586,1.595,1.595,1.595,1.604,1.604,1.604,1.604,1.607,1.607,1.607,1.622,1.622,1.622,1.625,1.625,1.625,1.637,1.637,1.667,1.670,1.670,1.694,1.694,1.694,1.694,1.694,1.694,1.697,1.697,1.697,1.700,1.700,1.700,1.700,1.700,1.700,1.703,1.703,1.703,1.703,1.709,1.709,1.709,1.709,1.709,1.709,1.709,1.712,1.712,1.712,1.712,1.712,1.721,1.721,1.727,1.727,1.727,1.727,1.730,1.730,1.730,1.736,1.736,1.736,1.736,1.736,1.736,1.736,1.736,1.736,1.739,1.739,1.739,1.739,1.739,1.760,1.760,1.760,1.799,1.799,1.799,1.799,1.799,1.802,1.802,1.802,1.802,1.802,1.802,1.814,1.814,1.814,1.814,1.814,1.814,1.814,1.814,1.814,1.814,1.814,1.814,1.817,1.817,1.817,1.826,1.826,1.826,1.826,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.829,1.844,1.844,1.862,1.862,1.862,1.862,1.865,1.865,1.865,1.865,1.868,1.868,1.868,1.868,1.871,1.871,1.871,1.871,1.871,1.871,1.871,1.871,1.877,1.877,1.877,1.877,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.886,1.901,1.901,1.901,1.907,1.907,1.907,1.910,1.910,1.910,1.910,1.910,1.910,1.910,1.910,1.913,1.913,1.913,1.913,1.913,1.913,1.913,1.925,1.925,1.925,1.925,1.964,1.964,1.964,1.970,1.970,1.970,1.970,1.970,1.973,1.973,1.973,1.973,1.973,1.979,1.979,1.979,1.979,1.979,1.994,1.994,1.997,1.997,1.997,1.997},{-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.532,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.511,-0.490,-0.490,-0.490,-0.490,-0.490,-0.457,-0.457,-0.457,-0.457,-0.445,-0.445,-0.445,-0.445,-0.445,-0.445,-0.427,-0.427,-0.427,-0.427,-0.427,-0.427,-0.406,-0.394,-0.394,-0.388,-0.388,-0.382,-0.382,-0.376,-0.373,-0.370,-0.370,-0.370,-0.364,-0.364,-0.364,-0.358,-0.358,-0.358,-0.349,-0.340,-0.328,-0.319,-0.319,-0.307,-0.304,-0.304,-0.301,-0.298,-0.292,-0.286,-0.286,-0.283,-0.283,-0.277,-0.274,-0.271,-0.268,-0.268,-0.262,-0.259,-0.259,-0.253,-0.250,-0.250,-0.250,-0.247,-0.244,-0.241,-0.238,-0.235,-0.235,-0.232,-0.229,-0.226,-0.223,-0.220,-0.217,-0.214,-0.211,-0.211,-0.208,-0.202,-0.199,-0.193,-0.190,-0.187,-0.184,-0.181,-0.181,-0.181,-0.175,-0.172,-0.172,-0.169,-0.169,-0.166,-0.166,-0.163,-0.160,-0.157,-0.148,-0.145,-0.145,-0.142,-0.139,-0.136,-0.136,-0.133,-0.127,-0.127,-0.124,-0.121,-0.121,-0.118,-0.115,-0.112,-0.106,-0.103,-0.100,-0.100,-0.097,-0.094,-0.091,-0.088,-0.085,-0.079,-0.079,-0.076,-0.073,-0.070,-0.067,-0.067,-0.064,-0.061,-0.058,-0.058,-0.055,-0.049,-0.049,-0.046,-0.046,-0.043,-0.040,-0.037,-0.034,-0.028,-0.025,-0.022,-0.019,-0.016,-0.007,-0.007,-0.001,0.002,0.005,0.011,0.011,0.014,0.020,0.020,0.023,0.035,0.038,0.041,0.047,0.050,0.053,0.056,0.059,0.062,0.065,0.068,0.068,0.074,0.077,0.080,0.083,0.086,0.089,0.095,0.098,0.101,0.104,0.107,0.110,0.113,0.116,0.119,0.122,0.125,0.128,0.131,0.134,0.140,0.143,0.146,0.146,0.149,0.152,0.158,0.161,0.167,0.170,0.176,0.179,0.182,0.185,0.188,0.191,0.197,0.200,0.203,0.206,0.209,0.215,0.215,0.218,0.221,0.224,0.230,0.233,0.236,0.239,0.239,0.242,0.245,0.248,0.251,0.251,0.254,0.257,0.260,0.263,0.269,0.269,0.272,0.275,0.278,0.278,0.281,0.284,0.287,0.290,0.293,0.296,0.299,0.302,0.305,0.311,0.314,0.314,0.317,0.320,0.323,0.326,0.329,0.332,0.335,0.335,0.338,0.341,0.344,0.347,0.350,0.353,0.353,0.356,0.359,0.362,0.365,0.368,0.371,0.374,0.377,0.377,0.380,0.383,0.386,0.389,0.392,0.395,0.398,0.401,0.404,0.407,0.413,0.413,0.416,0.422,0.425,0.425,0.428,0.434,0.437,0.443,0.446,0.452,0.455,0.455,0.458,0.464,0.464,0.467,0.470,0.473,0.476,0.479,0.482,0.485,0.488,0.488,0.491,0.494,0.497,0.500,0.500,0.503,0.506,0.509,0.512,0.515,0.518,0.521,0.524,0.527,0.530,0.533,0.536,0.539,0.542,0.545,0.548,0.551,0.551,0.554,0.557,0.560,0.563,0.566,0.566,0.569,0.572,0.575,0.575,0.578,0.581,0.581,0.584,0.584,0.587,0.593,0.593,0.596,0.599,0.602,0.602,0.605,0.608,0.611,0.611,0.617,0.617,0.620,0.623,0.626,0.629,0.629,0.632,0.635,0.638,0.641,0.641,0.644,0.644,0.647,0.650,0.653,0.653,0.656,0.659,0.659,0.662,0.665,0.665,0.671,0.671,0.674,0.677,0.680,0.680,0.683,0.686,0.689,0.689,0.692,0.692,0.695,0.698,0.701,0.701,0.704,0.704,0.707,0.710,0.713,0.713,0.716,0.716,0.719,0.722,0.722,0.725,0.728,0.731,0.731,0.734,0.737,0.737,0.743,0.743,0.746,0.749,0.749,0.752,0.752,0.755,0.755,0.758,0.758,0.761,0.764,0.767,0.770,0.770,0.773,0.773,0.776,0.779,0.779,0.782,0.782,0.785,0.785,0.788,0.791,0.791,0.794,0.794,0.794,0.797,0.800,0.803,0.806,0.806,0.809,0.809,0.812,0.815,0.818,0.818,0.821,0.824,0.824,0.824,0.827,0.830,0.830,0.833,0.833,0.836,0.836,0.839,0.842,0.842,0.845,0.845,0.848,0.848,0.851,0.854,0.854,0.857,0.857,0.860,0.860,0.863,0.863,0.866,0.869,0.869,0.869,0.872,0.872,0.872,0.875,0.878,0.878,0.881,0.881,0.884,0.884,0.884,0.887,0.890,0.890,0.893,0.893,0.896,0.899,0.899,0.902,0.902,0.902,0.905,0.905,0.908,0.911,0.911,0.914,0.914,0.917,0.917,0.920,0.920,0.923,0.923,0.926,0.926,0.929,0.929,0.932,0.932,0.938,0.941,0.944,0.947,0.947,0.950,0.950,0.956,0.956,0.959,0.959,0.962,0.962,0.965,0.968,0.980,0.983,0.986,0.989,0.992,0.992,0.995,0.998,0.998,1.004,1.007,1.010,1.013,1.016,1.019,1.019,1.028,1.028,1.031,1.034,1.043,1.046,1.070,1.073,1.079,1.082,1.085,1.085,1.088,1.091,1.100,1.109,1.109,1.127,1.127,1.133,1.151,1.151,1.172,1.172,1.172,1.175,1.175,1.208,1.217,1.220,1.226,1.226,1.226,1.232,1.235,1.241,1.250,1.262,1.280,1.286,1.286,1.298,1.298,1.334,1.352,1.352,1.394,1.394,1.397,1.397,1.403,1.403,1.403,1.403,1.463,1.463,1.463,1.463,1.463,1.466,1.466,1.466,1.472,1.472,1.472,1.472,1.472,1.472,1.472,1.625,1.625,1.625,1.625,1.625,1.625,1.637,1.637,1.637,1.637,1.637,1.637,1.637,1.637,1.637,1.637,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.703,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.832,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.904,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.928,1.997,1.997,1.997,1.997,1.997}};

float CorrectUpsilon_WCR(float Y, int pantau){
int bin =  ((Y+1.000)/3.000)*1000;
return (Y<2.000) ? YCorr_WCR[pantau][bin] : -2 ;
}

