#include <iostream>
using namespace std;
float FFcompareMV1_BDT200to400reg7(float bdt){
	if(bdt<0.100) return 1.021054;
	if(bdt<0.200) return 1.003584;
	if(bdt<0.300) return 0.983537;
	if(bdt<0.400) return 0.975913;
	if(bdt<0.500) return 0.964653;
	if(bdt<0.627) return 0.975939;
	if(bdt<0.732) return 0.979924;
	if(bdt<0.807) return 0.974591;
	if(bdt<0.861) return 0.970917;
	if(bdt<0.900) return 0.977338;
	if(bdt<0.928) return 0.998462;
	if(bdt<0.948) return 0.978170;
	if(bdt<0.963) return 0.941420;
	if(bdt<0.973) return 0.901055;
	if(bdt<0.981) return 0.829138;
	if(bdt<1.000) return 0.922346;
}
