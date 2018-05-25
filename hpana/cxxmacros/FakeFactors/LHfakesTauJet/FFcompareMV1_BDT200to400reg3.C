#include <iostream>
using namespace std;
float FFcompareMV1_BDT200to400reg3(float bdt){
	if(bdt<0.100) return 1.023781;
	if(bdt<0.200) return 0.999516;
	if(bdt<0.300) return 0.994346;
	if(bdt<0.400) return 0.983545;
	if(bdt<0.500) return 0.993554;
	if(bdt<0.715) return 0.995780;
	if(bdt<0.813) return 1.000816;
	if(bdt<0.877) return 0.997576;
	if(bdt<0.919) return 0.987388;
	if(bdt<0.947) return 0.986261;
	if(bdt<0.965) return 0.996530;
	if(bdt<0.977) return 1.011101;
	if(bdt<1.000) return 1.014399;
}
