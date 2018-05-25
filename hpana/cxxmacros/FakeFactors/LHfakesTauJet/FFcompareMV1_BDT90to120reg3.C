#include <iostream>
using namespace std;
float FFcompareMV1_BDT90to120reg3(float bdt){
		if(bdt<0.100) return 0.977900;
		if(bdt<0.200) return 1.007351;
		if(bdt<0.300) return 1.010028;
		if(bdt<0.400) return 1.012585;
		if(bdt<0.500) return 1.000510;
		if(bdt<0.621) return 0.997852;
		if(bdt<0.702) return 0.981391;
		if(bdt<0.766) return 0.976774;
		if(bdt<0.817) return 0.983636;
		if(bdt<0.856) return 0.998028;
		if(bdt<0.887) return 0.984841;
		if(bdt<1.000) return 1.014926;
}
