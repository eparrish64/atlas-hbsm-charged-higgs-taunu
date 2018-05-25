#include <iostream>
using namespace std;
float FFcompareMV1_BDT160to180reg3(float bdt){
	if(bdt<0.100) return 1.036812;
	if(bdt<0.200) return 1.015577;
	if(bdt<0.300) return 1.008750;
	if(bdt<0.400) return 0.997751;
	if(bdt<0.500) return 0.996935;
	if(bdt<0.627) return 0.985093;
	if(bdt<0.732) return 0.985069;
	if(bdt<0.807) return 0.998516;
	if(bdt<0.861) return 1.001040;
	if(bdt<0.900) return 0.984980;
	if(bdt<0.928) return 1.001596;
	if(bdt<0.948) return 1.010097;
	if(bdt<0.963) return 0.979083;
	if(bdt<0.973) return 0.999144;
	if(bdt<1.000) return 1.016193;
}
