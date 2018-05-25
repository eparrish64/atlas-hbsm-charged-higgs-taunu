#include <iostream>
using namespace std;
float FFcompareMV1_BDT130to160reg3(float bdt){
	if(bdt<0.100) return 1.012008;
	if(bdt<0.200) return 1.015866;
	if(bdt<0.300) return 1.005197;
	if(bdt<0.400) return 1.000506;
	if(bdt<0.500) return 0.999555;
	if(bdt<0.627) return 0.996510;
	if(bdt<0.732) return 0.986508;
	if(bdt<0.807) return 0.986441;
	if(bdt<0.861) return 0.985674;
	if(bdt<0.900) return 0.975971;
	if(bdt<0.928) return 0.960008;
	if(bdt<0.948) return 0.968117;
	if(bdt<1.000) return 0.981971;
}
