#include <iostream>
#include <TMath.h>
float GetElFakeSF(int nTrack, float eta){
   float abseta=TMath::Abs(eta);
   if(nTrack==3) return 1;
   if(abseta<0.1) return 0.844681;
   if(abseta<0.8) return 1.06235;
   if(abseta<1.32) return 1.02361;
   if(abseta<2.0) return 0.885368;
   if(abseta<2.3) return 0.996587;
	return 1;
}

float GetElFakeSFup(int nTrack, float eta){
   float abseta=TMath::Abs(eta);
   if(nTrack==3) return 1;
   if(abseta<0.1) return 0.844681;
   if(abseta<0.8) return 1.10418;
   if(abseta<1.32) return 1.0407;
   if(abseta<2.0) return 0.931866;
   if(abseta<2.3) return 1.02997;
	return 1;
}

float GetElFakeSFdn(int nTrack, float eta){
   float abseta=TMath::Abs(eta);
   if(nTrack==3) return 1;
   if(abseta<0.1) return 0.844681;
   if(abseta<0.8) return 1.02051;
   if(abseta<1.32) return 1.00653;
   if(abseta<2.0) return 0.83887;
   if(abseta<2.3) return 0.963207;
	return 1;
}

