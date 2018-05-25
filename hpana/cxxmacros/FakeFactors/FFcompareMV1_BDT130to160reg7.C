#include <iostream>
using namespace std;
float FFcompareMV1_BDT130to160reg7(float bdt){
	if(bdt<0.100) return 1.019925;
	if(bdt<0.200) return 1.008407;
	if(bdt<0.300) return 1.008300;
	if(bdt<0.400) return 1.008284;
	if(bdt<0.500) return 0.997928;
	if(bdt<0.627) return 0.990882;
	if(bdt<0.732) return 0.979477;
	if(bdt<0.807) return 0.954908;
	if(bdt<0.861) return 0.935620;
	if(bdt<0.900) return 0.933028;
	if(bdt<0.928) return 0.929853;
	if(bdt<1.000) return 0.924494;
}
