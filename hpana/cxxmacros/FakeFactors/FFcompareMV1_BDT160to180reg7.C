#include <iostream>
using namespace std;
float FFcompareMV1_BDT160to180reg7(float bdt){
	if(bdt<0.100) return 1.018094;
	if(bdt<0.200) return 1.014647;
	if(bdt<0.300) return 1.005994;
	if(bdt<0.400) return 0.993726;
	if(bdt<0.500) return 0.989422;
	if(bdt<0.627) return 0.970266;
	if(bdt<0.732) return 0.981318;
	if(bdt<0.807) return 0.963278;
	if(bdt<0.861) return 0.973399;
	if(bdt<0.900) return 0.974061;
	if(bdt<0.928) return 0.911833;
	if(bdt<0.948) return 0.912175;
	if(bdt<1.000) return 0.927935;
}
