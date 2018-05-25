#include <iostream>
using namespace std;
float FFcompareMV1_BDT500to2000reg7(float bdt){
	if(bdt<0.100) return 1.004080;
	if(bdt<0.200) return 0.975895;
	if(bdt<0.300) return 0.965841;
	if(bdt<0.400) return 0.983184;
	if(bdt<0.500) return 1.007324;
	if(bdt<0.627) return 1.000936;
	if(bdt<0.732) return 0.984592;
	if(bdt<0.807) return 0.974728;
	if(bdt<0.861) return 0.977358;
	if(bdt<0.900) return 0.991513;
	if(bdt<0.928) return 0.982495;
	if(bdt<0.948) return 0.926301;
	if(bdt<0.963) return 0.901402;
	if(bdt<0.973) return 0.949358;
	if(bdt<0.981) return 0.852589;
	if(bdt<0.990) return 0.907880;
	if(bdt<1.000) return 0.863663;
}
