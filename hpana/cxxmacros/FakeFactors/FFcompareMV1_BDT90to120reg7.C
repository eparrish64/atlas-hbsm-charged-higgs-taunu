#include <iostream>
using namespace std;
float FFcompareMV1_BDT90to120reg7(float bdt){
	if(bdt<0.100) return 0.993642;
	if(bdt<0.200) return 1.011742;
	if(bdt<0.300) return 1.005664;
	if(bdt<0.400) return 1.015366;
	if(bdt<0.517) return 1.015153;
	if(bdt<0.621) return 0.997503;
	if(bdt<0.702) return 0.969061;
	if(bdt<0.766) return 0.917907;
	if(bdt<0.817) return 0.915699;
	if(bdt<0.856) return 0.909677;
	if(bdt<1.000) return 0.932779;
}
