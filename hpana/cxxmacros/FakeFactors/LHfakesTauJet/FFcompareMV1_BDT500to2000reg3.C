#include <iostream>
using namespace std;
float FFcompareMV1_BDT500to2000reg3(float bdt){
	if(bdt<0.100) return 0.993819;
	if(bdt<0.200) return 0.996211;
	if(bdt<0.300) return 1.020333;
	if(bdt<0.400) return 1.023626;
	if(bdt<0.500) return 1.016935;
	if(bdt<0.641) return 1.031489;
	if(bdt<0.785) return 1.041747;
	if(bdt<0.871) return 1.066172;
	if(bdt<0.923) return 1.070208;
	if(bdt<0.954) return 1.056101;
	if(bdt<0.972) return 1.065813;
	if(bdt<0.983) return 1.024621;
	if(bdt<0.990) return 1.003270;
	if(bdt<1.000) return 1.047417;
}
