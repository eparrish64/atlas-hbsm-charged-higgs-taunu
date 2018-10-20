#include <iostream>
float GetFFCombined_NOMINAL(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
		 if(ntracks==1){
			 if(pt < 40) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 45) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 50) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 60) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 75) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 100) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 150) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 300) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 3500) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 50) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 75) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 100) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 200) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
			 if(pt < 3500) return (1.0*FF_CR_MULTIJET) + (1.06581410364e-13*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
		 if(ntracks==1){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 45) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 50) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 75) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 100) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 150) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 300) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 3500) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 50) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 75) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 100) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 200) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 3500) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 45) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 50) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 60) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 75) return (0.19*FF_CR_MULTIJET) + (0.81*FF_CR_WJETS);
			 if(pt < 100) return (0.44*FF_CR_MULTIJET) + (0.56*FF_CR_WJETS);
			 if(pt < 150) return (0.98*FF_CR_MULTIJET) + (0.0200000000001*FF_CR_WJETS);
			 if(pt < 300) return (-0.6*FF_CR_MULTIJET) + (1.6*FF_CR_WJETS);
			 if(pt < 3500) return (1.02*FF_CR_MULTIJET) + (-0.0199999999999*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 75) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 100) return (-1.71*FF_CR_MULTIJET) + (2.71*FF_CR_WJETS);
			 if(pt < 200) return (-2.55*FF_CR_MULTIJET) + (3.55*FF_CR_WJETS);
			 if(pt < 3500) return (1.43*FF_CR_MULTIJET) + (-0.43*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (0.5*FF_CR_MULTIJET) + (0.5*FF_CR_WJETS);
			 if(pt < 50) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 if(pt < 60) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 75) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 100) return (0.31*FF_CR_MULTIJET) + (0.69*FF_CR_WJETS);
			 if(pt < 150) return (1.63*FF_CR_MULTIJET) + (-0.63*FF_CR_WJETS);
			 if(pt < 300) return (3.99*FF_CR_MULTIJET) + (-2.99*FF_CR_WJETS);
			 if(pt < 3500) return (1.99*FF_CR_MULTIJET) + (-0.99*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 75) return (-0.6*FF_CR_MULTIJET) + (1.6*FF_CR_WJETS);
			 if(pt < 100) return (-1.11*FF_CR_MULTIJET) + (2.11*FF_CR_WJETS);
			 if(pt < 200) return (-1.98*FF_CR_MULTIJET) + (2.98*FF_CR_WJETS);
			 if(pt < 3500) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 50) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 75) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 100) return (-0.84*FF_CR_MULTIJET) + (1.84*FF_CR_WJETS);
			 if(pt < 150) return (-2.22*FF_CR_MULTIJET) + (3.22*FF_CR_WJETS);
			 if(pt < 300) return (3.65*FF_CR_MULTIJET) + (-2.65*FF_CR_WJETS);
			 if(pt < 3500) return (2.11*FF_CR_MULTIJET) + (-1.11*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-1.09*FF_CR_MULTIJET) + (2.09*FF_CR_WJETS);
			 if(pt < 75) return (-1.93*FF_CR_MULTIJET) + (2.93*FF_CR_WJETS);
			 if(pt < 100) return (-3.58*FF_CR_MULTIJET) + (4.58*FF_CR_WJETS);
			 if(pt < 200) return (-4.0*FF_CR_MULTIJET) + (5.0*FF_CR_WJETS);
			 if(pt < 3500) return (-3.99*FF_CR_MULTIJET) + (4.99*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.9*FF_CR_MULTIJET) + (1.9*FF_CR_WJETS);
			 if(pt < 50) return (-0.93*FF_CR_MULTIJET) + (1.93*FF_CR_WJETS);
			 if(pt < 60) return (-0.82*FF_CR_MULTIJET) + (1.82*FF_CR_WJETS);
			 if(pt < 75) return (-0.8*FF_CR_MULTIJET) + (1.8*FF_CR_WJETS);
			 if(pt < 100) return (-1.14*FF_CR_MULTIJET) + (2.14*FF_CR_WJETS);
			 if(pt < 150) return (-1.4*FF_CR_MULTIJET) + (2.4*FF_CR_WJETS);
			 if(pt < 300) return (-3.14*FF_CR_MULTIJET) + (4.14*FF_CR_WJETS);
			 if(pt < 3500) return (3.99*FF_CR_MULTIJET) + (-2.99*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-1.01*FF_CR_MULTIJET) + (2.01*FF_CR_WJETS);
			 if(pt < 75) return (-1.86*FF_CR_MULTIJET) + (2.86*FF_CR_WJETS);
			 if(pt < 100) return (-4.0*FF_CR_MULTIJET) + (5.0*FF_CR_WJETS);
			 if(pt < 200) return (-4.0*FF_CR_MULTIJET) + (5.0*FF_CR_WJETS);
			 if(pt < 3500) return (-4.0*FF_CR_MULTIJET) + (5.0*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 40) return (0.28*FF_CR_MULTIJET) + (0.72*FF_CR_WJETS);
			 if(pt < 45) return (0.21*FF_CR_MULTIJET) + (0.79*FF_CR_WJETS);
			 if(pt < 50) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 60) return (0.43*FF_CR_MULTIJET) + (0.57*FF_CR_WJETS);
			 if(pt < 75) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 100) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 150) return (0.98*FF_CR_MULTIJET) + (0.0200000000001*FF_CR_WJETS);
			 if(pt < 300) return (0.45*FF_CR_MULTIJET) + (0.55*FF_CR_WJETS);
			 if(pt < 3500) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 50) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 75) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 100) return (-0.86*FF_CR_MULTIJET) + (1.86*FF_CR_WJETS);
			 if(pt < 200) return (-2.44*FF_CR_MULTIJET) + (3.44*FF_CR_WJETS);
			 if(pt < 3500) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==1007) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.61*FF_CR_MULTIJET) + (1.61*FF_CR_WJETS);
			 if(pt < 45) return (-0.53*FF_CR_MULTIJET) + (1.53*FF_CR_WJETS);
			 if(pt < 50) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 60) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 75) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 100) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 150) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 300) return (-1.85*FF_CR_MULTIJET) + (2.85*FF_CR_WJETS);
			 if(pt < 3500) return (-2.67*FF_CR_MULTIJET) + (3.67*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 50) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 if(pt < 75) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 100) return (-0.95*FF_CR_MULTIJET) + (1.95*FF_CR_WJETS);
			 if(pt < 200) return (-2.57*FF_CR_MULTIJET) + (3.57*FF_CR_WJETS);
			 if(pt < 3500) return (-1.15*FF_CR_MULTIJET) + (2.15*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.53*FF_CR_MULTIJET) + (1.53*FF_CR_WJETS);
			 if(pt < 45) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 75) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 100) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 150) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 300) return (-0.96*FF_CR_MULTIJET) + (1.96*FF_CR_WJETS);
			 if(pt < 3500) return (3.5*FF_CR_MULTIJET) + (-2.5*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 50) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 if(pt < 75) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 100) return (-0.91*FF_CR_MULTIJET) + (1.91*FF_CR_WJETS);
			 if(pt < 200) return (-3.41*FF_CR_MULTIJET) + (4.41*FF_CR_WJETS);
			 if(pt < 3500) return (-0.94*FF_CR_MULTIJET) + (1.94*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (ZEE) target region
	 if (index==1013) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 45) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 50) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 75) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 100) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 150) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 300) return (-0.93*FF_CR_MULTIJET) + (1.93*FF_CR_WJETS);
			 if(pt < 3500) return (3.99*FF_CR_MULTIJET) + (-2.99*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.52*FF_CR_MULTIJET) + (1.52*FF_CR_WJETS);
			 if(pt < 50) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 75) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 100) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 200) return (0.18*FF_CR_MULTIJET) + (0.82*FF_CR_WJETS);
			 if(pt < 3500) return (-3.77*FF_CR_MULTIJET) + (4.77*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==1014) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 45) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 50) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 60) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 75) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 100) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 150) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 300) return (0.28*FF_CR_MULTIJET) + (0.72*FF_CR_WJETS);
			 if(pt < 3500) return (0.53*FF_CR_MULTIJET) + (0.47*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 50) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 75) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 100) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 200) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 3500) return (0.58*FF_CR_MULTIJET) + (0.42*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==1010) {
		 if(ntracks==1){
			 if(pt < 40) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 if(pt < 45) return (0.88*FF_CR_MULTIJET) + (0.12*FF_CR_WJETS);
			 if(pt < 50) return (0.75*FF_CR_MULTIJET) + (0.25*FF_CR_WJETS);
			 if(pt < 60) return (0.63*FF_CR_MULTIJET) + (0.37*FF_CR_WJETS);
			 if(pt < 75) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 100) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 if(pt < 150) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 300) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 3500) return (3.43*FF_CR_MULTIJET) + (-2.43*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (1.05*FF_CR_MULTIJET) + (-0.0499999999999*FF_CR_WJETS);
			 if(pt < 50) return (0.86*FF_CR_MULTIJET) + (0.14*FF_CR_WJETS);
			 if(pt < 75) return (0.91*FF_CR_MULTIJET) + (0.0900000000001*FF_CR_WJETS);
			 if(pt < 100) return (1.2*FF_CR_MULTIJET) + (-0.2*FF_CR_WJETS);
			 if(pt < 200) return (-4.0*FF_CR_MULTIJET) + (5.0*FF_CR_WJETS);
			 if(pt < 3500) return (2.22*FF_CR_MULTIJET) + (-1.22*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 45) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 50) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 60) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 75) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 100) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 150) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
			 if(pt < 300) return (-1.23*FF_CR_MULTIJET) + (2.23*FF_CR_WJETS);
			 if(pt < 3500) return (3.99*FF_CR_MULTIJET) + (-2.99*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 50) return (-0.56*FF_CR_MULTIJET) + (1.56*FF_CR_WJETS);
			 if(pt < 75) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 100) return (-0.8*FF_CR_MULTIJET) + (1.8*FF_CR_WJETS);
			 if(pt < 200) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 3500) return (-2.5*FF_CR_MULTIJET) + (3.5*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==1008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 45) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 if(pt < 50) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 60) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 75) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 100) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 150) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 300) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 3500) return (3.52*FF_CR_MULTIJET) + (-2.52*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
			 if(pt < 50) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 75) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 100) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 200) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==1012) {
		 if(ntracks==1){
		 }
		 if(ntracks==3){
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 45) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 50) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 60) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 75) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 100) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 150) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 300) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (3.35*FF_CR_MULTIJET) + (-2.35*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 50) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 75) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 100) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 200) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==1011) {
		 if(ntracks==1){
			 if(pt < 40) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 if(pt < 45) return (0.76*FF_CR_MULTIJET) + (0.24*FF_CR_WJETS);
			 if(pt < 50) return (0.69*FF_CR_MULTIJET) + (0.31*FF_CR_WJETS);
			 if(pt < 60) return (0.72*FF_CR_MULTIJET) + (0.28*FF_CR_WJETS);
			 if(pt < 75) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
			 if(pt < 100) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 if(pt < 150) return (1.56*FF_CR_MULTIJET) + (-0.56*FF_CR_WJETS);
			 if(pt < 300) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 3500) return (-4.0*FF_CR_MULTIJET) + (5.0*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.77*FF_CR_MULTIJET) + (0.23*FF_CR_WJETS);
			 if(pt < 50) return (0.91*FF_CR_MULTIJET) + (0.0900000000001*FF_CR_WJETS);
			 if(pt < 75) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 if(pt < 100) return (1.9*FF_CR_MULTIJET) + (-0.9*FF_CR_WJETS);
			 if(pt < 200) return (3.99*FF_CR_MULTIJET) + (-2.99*FF_CR_WJETS);
			 if(pt < 3500) return (3.99*FF_CR_MULTIJET) + (-2.99*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 else return 0;
}


float GetFFCombined_UP(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
		 if(ntracks==1){
			 if(pt < 40) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 45) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 50) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 60) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 75) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 100) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 150) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 300) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 3500) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 50) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 75) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 100) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 200) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 3500) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 45) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 50) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 60) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 75) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 100) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 150) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 300) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 3500) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 50) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 75) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 100) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 200) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 3500) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 45) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 if(pt < 50) return (0.17*FF_CR_MULTIJET) + (0.83*FF_CR_WJETS);
			 if(pt < 60) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 75) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 100) return (0.5*FF_CR_MULTIJET) + (0.5*FF_CR_WJETS);
			 if(pt < 150) return (1.04*FF_CR_MULTIJET) + (-0.0399999999999*FF_CR_WJETS);
			 if(pt < 300) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 3500) return (1.08*FF_CR_MULTIJET) + (-0.0799999999999*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 75) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
			 if(pt < 100) return (-1.65*FF_CR_MULTIJET) + (2.65*FF_CR_WJETS);
			 if(pt < 200) return (-2.49*FF_CR_MULTIJET) + (3.49*FF_CR_WJETS);
			 if(pt < 3500) return (1.49*FF_CR_MULTIJET) + (-0.49*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
			 if(pt < 50) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 60) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
			 if(pt < 75) return (0.44*FF_CR_MULTIJET) + (0.56*FF_CR_WJETS);
			 if(pt < 100) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 150) return (1.69*FF_CR_MULTIJET) + (-0.69*FF_CR_WJETS);
			 if(pt < 300) return (4.04*FF_CR_MULTIJET) + (-3.04*FF_CR_WJETS);
			 if(pt < 3500) return (2.05*FF_CR_MULTIJET) + (-1.05*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 75) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 100) return (-1.05*FF_CR_MULTIJET) + (2.05*FF_CR_WJETS);
			 if(pt < 200) return (-1.92*FF_CR_MULTIJET) + (2.92*FF_CR_WJETS);
			 if(pt < 3500) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 50) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 60) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 75) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 100) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 150) return (-2.16*FF_CR_MULTIJET) + (3.16*FF_CR_WJETS);
			 if(pt < 300) return (3.71*FF_CR_MULTIJET) + (-2.71*FF_CR_WJETS);
			 if(pt < 3500) return (2.17*FF_CR_MULTIJET) + (-1.17*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-1.03*FF_CR_MULTIJET) + (2.03*FF_CR_WJETS);
			 if(pt < 75) return (-1.87*FF_CR_MULTIJET) + (2.87*FF_CR_WJETS);
			 if(pt < 100) return (-3.52*FF_CR_MULTIJET) + (4.52*FF_CR_WJETS);
			 if(pt < 200) return (-3.94*FF_CR_MULTIJET) + (4.94*FF_CR_WJETS);
			 if(pt < 3500) return (-3.93*FF_CR_MULTIJET) + (4.93*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.84*FF_CR_MULTIJET) + (1.84*FF_CR_WJETS);
			 if(pt < 50) return (-0.87*FF_CR_MULTIJET) + (1.87*FF_CR_WJETS);
			 if(pt < 60) return (-0.76*FF_CR_MULTIJET) + (1.76*FF_CR_WJETS);
			 if(pt < 75) return (-0.74*FF_CR_MULTIJET) + (1.74*FF_CR_WJETS);
			 if(pt < 100) return (-1.08*FF_CR_MULTIJET) + (2.08*FF_CR_WJETS);
			 if(pt < 150) return (-1.34*FF_CR_MULTIJET) + (2.34*FF_CR_WJETS);
			 if(pt < 300) return (-3.08*FF_CR_MULTIJET) + (4.08*FF_CR_WJETS);
			 if(pt < 3500) return (4.04*FF_CR_MULTIJET) + (-3.04*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.95*FF_CR_MULTIJET) + (1.95*FF_CR_WJETS);
			 if(pt < 75) return (-1.8*FF_CR_MULTIJET) + (2.8*FF_CR_WJETS);
			 if(pt < 100) return (-3.94*FF_CR_MULTIJET) + (4.94*FF_CR_WJETS);
			 if(pt < 200) return (-3.94*FF_CR_MULTIJET) + (4.94*FF_CR_WJETS);
			 if(pt < 3500) return (-3.94*FF_CR_MULTIJET) + (4.94*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 40) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 45) return (0.27*FF_CR_MULTIJET) + (0.73*FF_CR_WJETS);
			 if(pt < 50) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 60) return (0.49*FF_CR_MULTIJET) + (0.51*FF_CR_WJETS);
			 if(pt < 75) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 100) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 150) return (1.04*FF_CR_MULTIJET) + (-0.0399999999999*FF_CR_WJETS);
			 if(pt < 300) return (0.51*FF_CR_MULTIJET) + (0.49*FF_CR_WJETS);
			 if(pt < 3500) return (0.68*FF_CR_MULTIJET) + (0.32*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.43*FF_CR_MULTIJET) + (0.57*FF_CR_WJETS);
			 if(pt < 50) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 75) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 100) return (-0.8*FF_CR_MULTIJET) + (1.8*FF_CR_WJETS);
			 if(pt < 200) return (-2.38*FF_CR_MULTIJET) + (3.38*FF_CR_WJETS);
			 if(pt < 3500) return (0.88*FF_CR_MULTIJET) + (0.12*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==1007) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
			 if(pt < 45) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 50) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 60) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
			 if(pt < 75) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 100) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 150) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 300) return (-1.79*FF_CR_MULTIJET) + (2.79*FF_CR_WJETS);
			 if(pt < 3500) return (-2.61*FF_CR_MULTIJET) + (3.61*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.53*FF_CR_MULTIJET) + (1.53*FF_CR_WJETS);
			 if(pt < 50) return (-0.56*FF_CR_MULTIJET) + (1.56*FF_CR_WJETS);
			 if(pt < 75) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 100) return (-0.89*FF_CR_MULTIJET) + (1.89*FF_CR_WJETS);
			 if(pt < 200) return (-2.51*FF_CR_MULTIJET) + (3.51*FF_CR_WJETS);
			 if(pt < 3500) return (-1.09*FF_CR_MULTIJET) + (2.09*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 45) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 50) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 60) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 75) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 100) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 150) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 300) return (-0.9*FF_CR_MULTIJET) + (1.9*FF_CR_WJETS);
			 if(pt < 3500) return (3.56*FF_CR_MULTIJET) + (-2.56*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.53*FF_CR_MULTIJET) + (1.53*FF_CR_WJETS);
			 if(pt < 50) return (-0.56*FF_CR_MULTIJET) + (1.56*FF_CR_WJETS);
			 if(pt < 75) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 100) return (-0.85*FF_CR_MULTIJET) + (1.85*FF_CR_WJETS);
			 if(pt < 200) return (-3.35*FF_CR_MULTIJET) + (4.35*FF_CR_WJETS);
			 if(pt < 3500) return (-0.88*FF_CR_MULTIJET) + (1.88*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (ZEE) target region
	 if (index==1013) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 45) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 50) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 60) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 75) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 100) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 150) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 300) return (-0.87*FF_CR_MULTIJET) + (1.87*FF_CR_WJETS);
			 if(pt < 3500) return (4.04*FF_CR_MULTIJET) + (-3.04*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
			 if(pt < 50) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 75) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 100) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 200) return (0.24*FF_CR_MULTIJET) + (0.76*FF_CR_WJETS);
			 if(pt < 3500) return (-3.71*FF_CR_MULTIJET) + (4.71*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==1014) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 45) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 50) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 75) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 100) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 150) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 300) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 3500) return (0.59*FF_CR_MULTIJET) + (0.41*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 50) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 75) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 100) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 200) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 3500) return (0.64*FF_CR_MULTIJET) + (0.36*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==1010) {
		 if(ntracks==1){
			 if(pt < 40) return (0.88*FF_CR_MULTIJET) + (0.12*FF_CR_WJETS);
			 if(pt < 45) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.81*FF_CR_MULTIJET) + (0.19*FF_CR_WJETS);
			 if(pt < 60) return (0.69*FF_CR_MULTIJET) + (0.31*FF_CR_WJETS);
			 if(pt < 75) return (0.68*FF_CR_MULTIJET) + (0.32*FF_CR_WJETS);
			 if(pt < 100) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 150) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 300) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 3500) return (3.49*FF_CR_MULTIJET) + (-2.49*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (1.11*FF_CR_MULTIJET) + (-0.11*FF_CR_WJETS);
			 if(pt < 50) return (0.92*FF_CR_MULTIJET) + (0.0800000000001*FF_CR_WJETS);
			 if(pt < 75) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 if(pt < 100) return (1.26*FF_CR_MULTIJET) + (-0.26*FF_CR_WJETS);
			 if(pt < 200) return (-3.94*FF_CR_MULTIJET) + (4.94*FF_CR_WJETS);
			 if(pt < 3500) return (2.28*FF_CR_MULTIJET) + (-1.28*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 45) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 50) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 60) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 75) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 100) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 150) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 300) return (-1.17*FF_CR_MULTIJET) + (2.17*FF_CR_WJETS);
			 if(pt < 3500) return (4.04*FF_CR_MULTIJET) + (-3.04*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 50) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 75) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 100) return (-0.74*FF_CR_MULTIJET) + (1.74*FF_CR_WJETS);
			 if(pt < 200) return (-0.72*FF_CR_MULTIJET) + (1.72*FF_CR_WJETS);
			 if(pt < 3500) return (-2.44*FF_CR_MULTIJET) + (3.44*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==1008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 if(pt < 45) return (0.14*FF_CR_MULTIJET) + (0.86*FF_CR_WJETS);
			 if(pt < 50) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 60) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 75) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 100) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 150) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 300) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 3500) return (3.58*FF_CR_MULTIJET) + (-2.58*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 50) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 75) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 100) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 200) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==1012) {
		 if(ntracks==1){
		 }
		 if(ntracks==3){
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 45) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 50) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 60) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 75) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 100) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 150) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 300) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 3500) return (3.41*FF_CR_MULTIJET) + (-2.41*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 50) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 75) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 100) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 200) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==1011) {
		 if(ntracks==1){
			 if(pt < 40) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 if(pt < 45) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 if(pt < 50) return (0.75*FF_CR_MULTIJET) + (0.25*FF_CR_WJETS);
			 if(pt < 60) return (0.78*FF_CR_MULTIJET) + (0.22*FF_CR_WJETS);
			 if(pt < 75) return (0.58*FF_CR_MULTIJET) + (0.42*FF_CR_WJETS);
			 if(pt < 100) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 150) return (1.62*FF_CR_MULTIJET) + (-0.62*FF_CR_WJETS);
			 if(pt < 300) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 if(pt < 3500) return (-3.94*FF_CR_MULTIJET) + (4.94*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 50) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 if(pt < 75) return (0.85*FF_CR_MULTIJET) + (0.15*FF_CR_WJETS);
			 if(pt < 100) return (1.96*FF_CR_MULTIJET) + (-0.96*FF_CR_WJETS);
			 if(pt < 200) return (4.04*FF_CR_MULTIJET) + (-3.04*FF_CR_WJETS);
			 if(pt < 3500) return (4.04*FF_CR_MULTIJET) + (-3.04*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 else return 0;
}


float GetFFCombined_DOWN(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
		 if(ntracks==1){
			 if(pt < 40) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 45) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 60) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 75) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 100) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 150) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 300) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 3500) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 75) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 100) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 200) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 if(pt < 3500) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 45) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 50) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 60) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 75) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 100) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 150) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 300) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 50) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 75) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 100) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 200) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 50) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 60) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 75) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 100) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 150) return (0.92*FF_CR_MULTIJET) + (0.0800000000001*FF_CR_WJETS);
			 if(pt < 300) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 3500) return (0.96*FF_CR_MULTIJET) + (0.0400000000001*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 75) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 100) return (-1.77*FF_CR_MULTIJET) + (2.77*FF_CR_WJETS);
			 if(pt < 200) return (-2.61*FF_CR_MULTIJET) + (3.61*FF_CR_WJETS);
			 if(pt < 3500) return (1.37*FF_CR_MULTIJET) + (-0.37*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (0.44*FF_CR_MULTIJET) + (0.56*FF_CR_WJETS);
			 if(pt < 50) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
			 if(pt < 60) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 75) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 100) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 150) return (1.57*FF_CR_MULTIJET) + (-0.57*FF_CR_WJETS);
			 if(pt < 300) return (3.93*FF_CR_MULTIJET) + (-2.93*FF_CR_WJETS);
			 if(pt < 3500) return (1.93*FF_CR_MULTIJET) + (-0.93*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 75) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 100) return (-1.17*FF_CR_MULTIJET) + (2.17*FF_CR_WJETS);
			 if(pt < 200) return (-2.04*FF_CR_MULTIJET) + (3.04*FF_CR_WJETS);
			 if(pt < 3500) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.34*FF_CR_MULTIJET) + (1.34*FF_CR_WJETS);
			 if(pt < 50) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 60) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 75) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 100) return (-0.9*FF_CR_MULTIJET) + (1.9*FF_CR_WJETS);
			 if(pt < 150) return (-2.28*FF_CR_MULTIJET) + (3.28*FF_CR_WJETS);
			 if(pt < 300) return (3.59*FF_CR_MULTIJET) + (-2.59*FF_CR_WJETS);
			 if(pt < 3500) return (2.05*FF_CR_MULTIJET) + (-1.05*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-1.15*FF_CR_MULTIJET) + (2.15*FF_CR_WJETS);
			 if(pt < 75) return (-1.99*FF_CR_MULTIJET) + (2.99*FF_CR_WJETS);
			 if(pt < 100) return (-3.64*FF_CR_MULTIJET) + (4.64*FF_CR_WJETS);
			 if(pt < 200) return (-4.05*FF_CR_MULTIJET) + (5.05*FF_CR_WJETS);
			 if(pt < 3500) return (-4.04*FF_CR_MULTIJET) + (5.04*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.96*FF_CR_MULTIJET) + (1.96*FF_CR_WJETS);
			 if(pt < 50) return (-0.99*FF_CR_MULTIJET) + (1.99*FF_CR_WJETS);
			 if(pt < 60) return (-0.88*FF_CR_MULTIJET) + (1.88*FF_CR_WJETS);
			 if(pt < 75) return (-0.86*FF_CR_MULTIJET) + (1.86*FF_CR_WJETS);
			 if(pt < 100) return (-1.2*FF_CR_MULTIJET) + (2.2*FF_CR_WJETS);
			 if(pt < 150) return (-1.46*FF_CR_MULTIJET) + (2.46*FF_CR_WJETS);
			 if(pt < 300) return (-3.2*FF_CR_MULTIJET) + (4.2*FF_CR_WJETS);
			 if(pt < 3500) return (3.93*FF_CR_MULTIJET) + (-2.93*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 50) return (-1.07*FF_CR_MULTIJET) + (2.07*FF_CR_WJETS);
			 if(pt < 75) return (-1.92*FF_CR_MULTIJET) + (2.92*FF_CR_WJETS);
			 if(pt < 100) return (-4.05*FF_CR_MULTIJET) + (5.05*FF_CR_WJETS);
			 if(pt < 200) return (-4.05*FF_CR_MULTIJET) + (5.05*FF_CR_WJETS);
			 if(pt < 3500) return (-4.05*FF_CR_MULTIJET) + (5.05*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 40) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 if(pt < 45) return (0.15*FF_CR_MULTIJET) + (0.85*FF_CR_WJETS);
			 if(pt < 50) return (0.26*FF_CR_MULTIJET) + (0.74*FF_CR_WJETS);
			 if(pt < 60) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 75) return (0.26*FF_CR_MULTIJET) + (0.74*FF_CR_WJETS);
			 if(pt < 100) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 150) return (0.92*FF_CR_MULTIJET) + (0.0800000000001*FF_CR_WJETS);
			 if(pt < 300) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 3500) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.31*FF_CR_MULTIJET) + (0.69*FF_CR_WJETS);
			 if(pt < 50) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 75) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 100) return (-0.92*FF_CR_MULTIJET) + (1.92*FF_CR_WJETS);
			 if(pt < 200) return (-2.5*FF_CR_MULTIJET) + (3.5*FF_CR_WJETS);
			 if(pt < 3500) return (0.76*FF_CR_MULTIJET) + (0.24*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==1007) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.67*FF_CR_MULTIJET) + (1.67*FF_CR_WJETS);
			 if(pt < 45) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 50) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 60) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 75) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 100) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 150) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 300) return (-1.91*FF_CR_MULTIJET) + (2.91*FF_CR_WJETS);
			 if(pt < 3500) return (-2.73*FF_CR_MULTIJET) + (3.73*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.65*FF_CR_MULTIJET) + (1.65*FF_CR_WJETS);
			 if(pt < 50) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 75) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 100) return (-1.01*FF_CR_MULTIJET) + (2.01*FF_CR_WJETS);
			 if(pt < 200) return (-2.63*FF_CR_MULTIJET) + (3.63*FF_CR_WJETS);
			 if(pt < 3500) return (-1.21*FF_CR_MULTIJET) + (2.21*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 45) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 50) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 60) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 75) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 100) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 150) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 300) return (-1.02*FF_CR_MULTIJET) + (2.02*FF_CR_WJETS);
			 if(pt < 3500) return (3.44*FF_CR_MULTIJET) + (-2.44*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.65*FF_CR_MULTIJET) + (1.65*FF_CR_WJETS);
			 if(pt < 50) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 75) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 100) return (-0.97*FF_CR_MULTIJET) + (1.97*FF_CR_WJETS);
			 if(pt < 200) return (-3.47*FF_CR_MULTIJET) + (4.47*FF_CR_WJETS);
			 if(pt < 3500) return (-1.0*FF_CR_MULTIJET) + (2.0*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (ZEE) target region
	 if (index==1013) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 45) return (-0.34*FF_CR_MULTIJET) + (1.34*FF_CR_WJETS);
			 if(pt < 50) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 60) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 75) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 100) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 150) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 300) return (-0.99*FF_CR_MULTIJET) + (1.99*FF_CR_WJETS);
			 if(pt < 3500) return (3.93*FF_CR_MULTIJET) + (-2.93*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.58*FF_CR_MULTIJET) + (1.58*FF_CR_WJETS);
			 if(pt < 50) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 75) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 100) return (-0.34*FF_CR_MULTIJET) + (1.34*FF_CR_WJETS);
			 if(pt < 200) return (0.12*FF_CR_MULTIJET) + (0.88*FF_CR_WJETS);
			 if(pt < 3500) return (-3.83*FF_CR_MULTIJET) + (4.83*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==1014) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 45) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 50) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 60) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 75) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 100) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 150) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 300) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 if(pt < 3500) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 50) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 75) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 100) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 200) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 3500) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==1010) {
		 if(ntracks==1){
			 if(pt < 40) return (0.76*FF_CR_MULTIJET) + (0.24*FF_CR_WJETS);
			 if(pt < 45) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 if(pt < 50) return (0.69*FF_CR_MULTIJET) + (0.31*FF_CR_WJETS);
			 if(pt < 60) return (0.57*FF_CR_MULTIJET) + (0.43*FF_CR_WJETS);
			 if(pt < 75) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
			 if(pt < 100) return (0.68*FF_CR_MULTIJET) + (0.32*FF_CR_WJETS);
			 if(pt < 150) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 300) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 if(pt < 3500) return (3.37*FF_CR_MULTIJET) + (-2.37*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.99*FF_CR_MULTIJET) + (0.0100000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 75) return (0.85*FF_CR_MULTIJET) + (0.15*FF_CR_WJETS);
			 if(pt < 100) return (1.14*FF_CR_MULTIJET) + (-0.14*FF_CR_WJETS);
			 if(pt < 200) return (-4.05*FF_CR_MULTIJET) + (5.05*FF_CR_WJETS);
			 if(pt < 3500) return (2.16*FF_CR_MULTIJET) + (-1.16*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
			 if(pt < 45) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 if(pt < 50) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 60) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 75) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 100) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 150) return (-0.52*FF_CR_MULTIJET) + (1.52*FF_CR_WJETS);
			 if(pt < 300) return (-1.29*FF_CR_MULTIJET) + (2.29*FF_CR_WJETS);
			 if(pt < 3500) return (3.93*FF_CR_MULTIJET) + (-2.93*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.6*FF_CR_MULTIJET) + (1.6*FF_CR_WJETS);
			 if(pt < 50) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 if(pt < 75) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 100) return (-0.86*FF_CR_MULTIJET) + (1.86*FF_CR_WJETS);
			 if(pt < 200) return (-0.84*FF_CR_MULTIJET) + (1.84*FF_CR_WJETS);
			 if(pt < 3500) return (-2.56*FF_CR_MULTIJET) + (3.56*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==1008) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 45) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 50) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 60) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 75) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 100) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 150) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 300) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 3500) return (3.46*FF_CR_MULTIJET) + (-2.46*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 50) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 75) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 100) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 200) return (-0.52*FF_CR_MULTIJET) + (1.52*FF_CR_WJETS);
			 if(pt < 3500) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==1012) {
		 if(ntracks==1){
		 }
		 if(ntracks==3){
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 45) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 50) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 60) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 75) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 100) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 150) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 300) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (3.29*FF_CR_MULTIJET) + (-2.29*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 50) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 75) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 100) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 200) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 3500) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==1011) {
		 if(ntracks==1){
			 if(pt < 40) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 if(pt < 45) return (0.7*FF_CR_MULTIJET) + (0.3*FF_CR_WJETS);
			 if(pt < 50) return (0.63*FF_CR_MULTIJET) + (0.37*FF_CR_WJETS);
			 if(pt < 60) return (0.66*FF_CR_MULTIJET) + (0.34*FF_CR_WJETS);
			 if(pt < 75) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 100) return (0.68*FF_CR_MULTIJET) + (0.32*FF_CR_WJETS);
			 if(pt < 150) return (1.5*FF_CR_MULTIJET) + (-0.5*FF_CR_WJETS);
			 if(pt < 300) return (-0.63*FF_CR_MULTIJET) + (1.63*FF_CR_WJETS);
			 if(pt < 3500) return (-4.05*FF_CR_MULTIJET) + (5.05*FF_CR_WJETS);
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 50) return (0.85*FF_CR_MULTIJET) + (0.15*FF_CR_WJETS);
			 if(pt < 75) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 if(pt < 100) return (1.84*FF_CR_MULTIJET) + (-0.84*FF_CR_WJETS);
			 if(pt < 200) return (3.93*FF_CR_MULTIJET) + (-2.93*FF_CR_WJETS);
			 if(pt < 3500) return (3.93*FF_CR_MULTIJET) + (-2.93*FF_CR_WJETS);
		 }
		 else return 0;
	 }
	 else return 0;
}


