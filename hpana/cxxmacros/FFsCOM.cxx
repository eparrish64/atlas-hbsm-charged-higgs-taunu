#include <iostream>
float GetFFCombined_NOMINAL(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 50) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 if(pt < 60) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 80) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
			 if(pt < 100) return (0.33*FF_CR_MULTIJET) + (0.67*FF_CR_WJETS);
			 if(pt < 3500) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 80) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 3500) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 50) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 60) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 100) return (0.27*FF_CR_MULTIJET) + (0.73*FF_CR_WJETS);
			 if(pt < 3500) return (0.78*FF_CR_MULTIJET) + (0.22*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 80) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 3500) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.55*FF_CR_MULTIJET) + (0.45*FF_CR_WJETS);
			 if(pt < 50) return (0.5*FF_CR_MULTIJET) + (0.5*FF_CR_WJETS);
			 if(pt < 60) return (0.64*FF_CR_MULTIJET) + (0.36*FF_CR_WJETS);
			 if(pt < 80) return (1.05*FF_CR_MULTIJET) + (-0.0499999999999*FF_CR_WJETS);
			 if(pt < 100) return (1.32*FF_CR_MULTIJET) + (-0.32*FF_CR_WJETS);
			 if(pt < 3500) return (1.11*FF_CR_MULTIJET) + (-0.11*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 80) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 3500) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 50) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 60) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 80) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 100) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 3500) return (2.04*FF_CR_MULTIJET) + (-1.04*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 45) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 50) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 if(pt < 60) return (0.18*FF_CR_MULTIJET) + (0.82*FF_CR_WJETS);
			 if(pt < 80) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 100) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
			 if(pt < 3500) return (0.95*FF_CR_MULTIJET) + (0.0500000000001*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 3500) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 if(pt < 50) return (0.7*FF_CR_MULTIJET) + (0.3*FF_CR_WJETS);
			 if(pt < 60) return (0.93*FF_CR_MULTIJET) + (0.0700000000001*FF_CR_WJETS);
			 if(pt < 80) return (1.41*FF_CR_MULTIJET) + (-0.41*FF_CR_WJETS);
			 if(pt < 100) return (1.88*FF_CR_MULTIJET) + (-0.88*FF_CR_WJETS);
			 if(pt < 3500) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 80) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 3500) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 50) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 60) return (0.48*FF_CR_MULTIJET) + (0.52*FF_CR_WJETS);
			 if(pt < 80) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 if(pt < 100) return (0.87*FF_CR_MULTIJET) + (0.13*FF_CR_WJETS);
			 if(pt < 3500) return (0.29*FF_CR_MULTIJET) + (0.71*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
			 if(pt < 3500) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 45) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 80) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 100) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 45) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 80) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 100) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 3500) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 45) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 50) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 60) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 80) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 100) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 3500) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 3500) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 45) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 50) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 60) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 100) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 45) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 50) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 60) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 100) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 3500) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (0.98*FF_CR_MULTIJET) + (0.0200000000001*FF_CR_WJETS);
			 if(pt < 45) return (0.91*FF_CR_MULTIJET) + (0.0900000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 if(pt < 60) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 if(pt < 80) return (1.27*FF_CR_MULTIJET) + (-0.27*FF_CR_WJETS);
			 if(pt < 100) return (0.95*FF_CR_MULTIJET) + (0.0500000000001*FF_CR_WJETS);
			 if(pt < 3500) return (-0.73*FF_CR_MULTIJET) + (1.73*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.53*FF_CR_MULTIJET) + (0.47*FF_CR_WJETS);
			 if(pt < 3500) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 if(pt < 45) return (0.89*FF_CR_MULTIJET) + (0.11*FF_CR_WJETS);
			 if(pt < 50) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 if(pt < 60) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 80) return (1.18*FF_CR_MULTIJET) + (-0.18*FF_CR_WJETS);
			 if(pt < 100) return (1.24*FF_CR_MULTIJET) + (-0.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 45) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 50) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 100) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 3500) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 45) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 50) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 60) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 80) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 100) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.72*FF_CR_MULTIJET) + (1.72*FF_CR_WJETS);
			 if(pt < 45) return (-0.6*FF_CR_MULTIJET) + (1.6*FF_CR_WJETS);
			 if(pt < 50) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 60) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 80) return (-0.65*FF_CR_MULTIJET) + (1.65*FF_CR_WJETS);
			 if(pt < 100) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 3500) return (1.8*FF_CR_MULTIJET) + (-0.8*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 60) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 45) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 80) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 100) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.07*FF_CR_MULTIJET) + (2.07*FF_CR_WJETS);
			 if(pt < 45) return (-0.83*FF_CR_MULTIJET) + (1.83*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 80) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 100) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 60) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


float GetFFCombined_1up(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 50) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 60) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
			 if(pt < 80) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
			 if(pt < 100) return (0.55*FF_CR_MULTIJET) + (0.45*FF_CR_WJETS);
			 if(pt < 3500) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
			 if(pt < 80) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
			 if(pt < 3500) return (0.43*FF_CR_MULTIJET) + (0.57*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 50) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 if(pt < 100) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 3500) return (1.15*FF_CR_MULTIJET) + (-0.15*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.23*FF_CR_MULTIJET) + (0.77*FF_CR_WJETS);
			 if(pt < 80) return (0.61*FF_CR_MULTIJET) + (0.39*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 if(pt < 50) return (0.61*FF_CR_MULTIJET) + (0.39*FF_CR_WJETS);
			 if(pt < 60) return (0.75*FF_CR_MULTIJET) + (0.25*FF_CR_WJETS);
			 if(pt < 80) return (1.2*FF_CR_MULTIJET) + (-0.2*FF_CR_WJETS);
			 if(pt < 100) return (1.64*FF_CR_MULTIJET) + (-0.64*FF_CR_WJETS);
			 if(pt < 3500) return (1.28*FF_CR_MULTIJET) + (-0.28*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.58*FF_CR_MULTIJET) + (0.42*FF_CR_WJETS);
			 if(pt < 80) return (0.69*FF_CR_MULTIJET) + (0.31*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 50) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 60) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 80) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 100) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 3500) return (2.31*FF_CR_MULTIJET) + (-1.31*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 80) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 3500) return (0.96*FF_CR_MULTIJET) + (0.0400000000001*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 45) return (0.19*FF_CR_MULTIJET) + (0.81*FF_CR_WJETS);
			 if(pt < 50) return (0.27*FF_CR_MULTIJET) + (0.73*FF_CR_WJETS);
			 if(pt < 60) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 80) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 100) return (0.66*FF_CR_MULTIJET) + (0.34*FF_CR_WJETS);
			 if(pt < 3500) return (1.05*FF_CR_MULTIJET) + (-0.0499999999999*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 60) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 80) return (0.45*FF_CR_MULTIJET) + (0.55*FF_CR_WJETS);
			 if(pt < 3500) return (0.78*FF_CR_MULTIJET) + (0.22*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.96*FF_CR_MULTIJET) + (0.0400000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 60) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 80) return (1.59*FF_CR_MULTIJET) + (-0.59*FF_CR_WJETS);
			 if(pt < 100) return (2.28*FF_CR_MULTIJET) + (-1.28*FF_CR_WJETS);
			 if(pt < 3500) return (0.99*FF_CR_MULTIJET) + (0.0100000000001*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 if(pt < 80) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 3500) return (0.86*FF_CR_MULTIJET) + (0.14*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 50) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 60) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
			 if(pt < 80) return (0.77*FF_CR_MULTIJET) + (0.23*FF_CR_WJETS);
			 if(pt < 100) return (1.03*FF_CR_MULTIJET) + (-0.0299999999999*FF_CR_WJETS);
			 if(pt < 3500) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.44*FF_CR_MULTIJET) + (0.56*FF_CR_WJETS);
			 if(pt < 80) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
			 if(pt < 3500) return (0.51*FF_CR_MULTIJET) + (0.49*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 45) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 50) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 60) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 80) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 100) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 3500) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 60) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 80) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 3500) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.67*FF_CR_MULTIJET) + (1.67*FF_CR_WJETS);
			 if(pt < 45) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 50) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 60) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 100) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 3500) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 60) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 80) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 3500) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.67*FF_CR_MULTIJET) + (1.67*FF_CR_WJETS);
			 if(pt < 45) return (-0.58*FF_CR_MULTIJET) + (1.58*FF_CR_WJETS);
			 if(pt < 50) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 60) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 80) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 100) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 3500) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 60) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 80) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 3500) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 45) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 if(pt < 50) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 60) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 80) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 100) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 3500) return (0.21*FF_CR_MULTIJET) + (0.79*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 60) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 80) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 if(pt < 3500) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 45) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 50) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 60) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 80) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 100) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 3500) return (0.24*FF_CR_MULTIJET) + (0.76*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 60) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 80) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 3500) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (1.09*FF_CR_MULTIJET) + (-0.0899999999999*FF_CR_WJETS);
			 if(pt < 45) return (1.01*FF_CR_MULTIJET) + (-0.00999999999989*FF_CR_WJETS);
			 if(pt < 50) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 60) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 80) return (1.41*FF_CR_MULTIJET) + (-0.41*FF_CR_WJETS);
			 if(pt < 100) return (1.2*FF_CR_MULTIJET) + (-0.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 if(pt < 60) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 80) return (0.59*FF_CR_MULTIJET) + (0.41*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (1.07*FF_CR_MULTIJET) + (-0.0699999999999*FF_CR_WJETS);
			 if(pt < 45) return (0.98*FF_CR_MULTIJET) + (0.0200000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.88*FF_CR_MULTIJET) + (0.12*FF_CR_WJETS);
			 if(pt < 60) return (0.91*FF_CR_MULTIJET) + (0.0900000000001*FF_CR_WJETS);
			 if(pt < 80) return (1.31*FF_CR_MULTIJET) + (-0.31*FF_CR_WJETS);
			 if(pt < 100) return (1.48*FF_CR_MULTIJET) + (-0.48*FF_CR_WJETS);
			 if(pt < 3500) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.43*FF_CR_MULTIJET) + (0.57*FF_CR_WJETS);
			 if(pt < 60) return (0.44*FF_CR_MULTIJET) + (0.56*FF_CR_WJETS);
			 if(pt < 80) return (0.6*FF_CR_MULTIJET) + (0.4*FF_CR_WJETS);
			 if(pt < 3500) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 45) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 50) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 60) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 80) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 100) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 if(pt < 3500) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 45) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 50) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 60) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 80) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 100) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 3500) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 45) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 50) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 60) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 80) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 100) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
			 if(pt < 3500) return (2.54*FF_CR_MULTIJET) + (-1.54*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 45) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 50) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 60) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 80) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 100) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 3500) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 60) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 80) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 3500) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	//! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.95*FF_CR_MULTIJET) + (1.95*FF_CR_WJETS);
			 if(pt < 45) return (-0.73*FF_CR_MULTIJET) + (1.73*FF_CR_WJETS);
			 if(pt < 50) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 60) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 80) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 100) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 3500) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 60) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 80) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


float GetFFCombined_1down(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 50) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 60) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 100) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.21*FF_CR_MULTIJET) + (0.79*FF_CR_WJETS);
			 if(pt < 80) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 3500) return (0.29*FF_CR_MULTIJET) + (0.71*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.72*FF_CR_MULTIJET) + (1.72*FF_CR_WJETS);
			 if(pt < 50) return (-0.63*FF_CR_MULTIJET) + (1.63*FF_CR_WJETS);
			 if(pt < 60) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 80) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 100) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 3500) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 3500) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.43*FF_CR_MULTIJET) + (0.57*FF_CR_WJETS);
			 if(pt < 50) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 60) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
			 if(pt < 80) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 if(pt < 100) return (1.04*FF_CR_MULTIJET) + (-0.0399999999999*FF_CR_WJETS);
			 if(pt < 3500) return (0.94*FF_CR_MULTIJET) + (0.0600000000001*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.49*FF_CR_MULTIJET) + (0.51*FF_CR_WJETS);
			 if(pt < 80) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 3500) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 80) return (-0.64*FF_CR_MULTIJET) + (1.64*FF_CR_WJETS);
			 if(pt < 100) return (-0.85*FF_CR_MULTIJET) + (1.85*FF_CR_WJETS);
			 if(pt < 3500) return (1.8*FF_CR_MULTIJET) + (-0.8*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.15*FF_CR_MULTIJET) + (0.85*FF_CR_WJETS);
			 if(pt < 80) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 3500) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 45) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 50) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 60) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 if(pt < 80) return (0.23*FF_CR_MULTIJET) + (0.77*FF_CR_WJETS);
			 if(pt < 100) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 3500) return (0.85*FF_CR_MULTIJET) + (0.15*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 60) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 if(pt < 80) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 3500) return (0.7*FF_CR_MULTIJET) + (0.3*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 if(pt < 50) return (0.57*FF_CR_MULTIJET) + (0.43*FF_CR_WJETS);
			 if(pt < 60) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 80) return (1.23*FF_CR_MULTIJET) + (-0.23*FF_CR_WJETS);
			 if(pt < 100) return (1.52*FF_CR_MULTIJET) + (-0.52*FF_CR_WJETS);
			 if(pt < 3500) return (0.64*FF_CR_MULTIJET) + (0.36*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.57*FF_CR_MULTIJET) + (0.43*FF_CR_WJETS);
			 if(pt < 80) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 3500) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 50) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.57*FF_CR_MULTIJET) + (0.43*FF_CR_WJETS);
			 if(pt < 100) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 3500) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 80) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 3500) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.87*FF_CR_MULTIJET) + (1.87*FF_CR_WJETS);
			 if(pt < 45) return (-0.75*FF_CR_MULTIJET) + (1.75*FF_CR_WJETS);
			 if(pt < 50) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 60) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 80) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 100) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 3500) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 60) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.89*FF_CR_MULTIJET) + (1.89*FF_CR_WJETS);
			 if(pt < 45) return (-0.76*FF_CR_MULTIJET) + (1.76*FF_CR_WJETS);
			 if(pt < 50) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
			 if(pt < 60) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 80) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 100) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 3500) return (-0.67*FF_CR_MULTIJET) + (1.67*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 60) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.34*FF_CR_MULTIJET) + (1.34*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.9*FF_CR_MULTIJET) + (1.9*FF_CR_WJETS);
			 if(pt < 45) return (-0.79*FF_CR_MULTIJET) + (1.79*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 80) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 100) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 3500) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 60) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 80) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 3500) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 45) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 50) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 60) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 80) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 100) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 3500) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 45) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 50) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 60) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 80) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 100) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 80) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (0.88*FF_CR_MULTIJET) + (0.12*FF_CR_WJETS);
			 if(pt < 45) return (0.81*FF_CR_MULTIJET) + (0.19*FF_CR_WJETS);
			 if(pt < 50) return (0.65*FF_CR_MULTIJET) + (0.35*FF_CR_WJETS);
			 if(pt < 60) return (0.87*FF_CR_MULTIJET) + (0.13*FF_CR_WJETS);
			 if(pt < 80) return (1.13*FF_CR_MULTIJET) + (-0.13*FF_CR_WJETS);
			 if(pt < 100) return (0.7*FF_CR_MULTIJET) + (0.3*FF_CR_WJETS);
			 if(pt < 3500) return (-1.01*FF_CR_MULTIJET) + (2.01*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.28*FF_CR_MULTIJET) + (0.72*FF_CR_WJETS);
			 if(pt < 60) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 if(pt < 80) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 3500) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.88*FF_CR_MULTIJET) + (0.12*FF_CR_WJETS);
			 if(pt < 45) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 50) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 60) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 if(pt < 80) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 if(pt < 100) return (0.99*FF_CR_MULTIJET) + (0.0100000000001*FF_CR_WJETS);
			 if(pt < 3500) return (-0.65*FF_CR_MULTIJET) + (1.65*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 if(pt < 60) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 80) return (0.48*FF_CR_MULTIJET) + (0.52*FF_CR_WJETS);
			 if(pt < 3500) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 45) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 50) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 60) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 80) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 100) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 3500) return (-0.61*FF_CR_MULTIJET) + (1.61*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 60) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 80) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 3500) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 45) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 50) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 60) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 80) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 100) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 60) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 80) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.01*FF_CR_MULTIJET) + (2.01*FF_CR_WJETS);
			 if(pt < 45) return (-0.88*FF_CR_MULTIJET) + (1.88*FF_CR_WJETS);
			 if(pt < 50) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 60) return (-0.82*FF_CR_MULTIJET) + (1.82*FF_CR_WJETS);
			 if(pt < 80) return (-1.09*FF_CR_MULTIJET) + (2.09*FF_CR_WJETS);
			 if(pt < 100) return (-1.68*FF_CR_MULTIJET) + (2.68*FF_CR_WJETS);
			 if(pt < 3500) return (1.06*FF_CR_MULTIJET) + (-0.0599999999999*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 60) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 80) return (-0.53*FF_CR_MULTIJET) + (1.53*FF_CR_WJETS);
			 if(pt < 3500) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.87*FF_CR_MULTIJET) + (1.87*FF_CR_WJETS);
			 if(pt < 45) return (-0.75*FF_CR_MULTIJET) + (1.75*FF_CR_WJETS);
			 if(pt < 50) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 60) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 80) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 100) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 3500) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 60) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.19*FF_CR_MULTIJET) + (2.19*FF_CR_WJETS);
			 if(pt < 45) return (-0.93*FF_CR_MULTIJET) + (1.93*FF_CR_WJETS);
			 if(pt < 50) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 60) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 80) return (-0.58*FF_CR_MULTIJET) + (1.58*FF_CR_WJETS);
			 if(pt < 100) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 3500) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 60) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 80) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 3500) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


float GetFFCombined_Heavy_Flavour_FF_1up(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0816880000001*FF_CR_MULTIJET) + (1.102788*FF_CR_WJETS);
			 if(pt < 50) return (0.225764*FF_CR_MULTIJET) + (0.800436*FF_CR_WJETS);
			 if(pt < 60) return (0.0415199999999*FF_CR_MULTIJET) + (0.99648*FF_CR_WJETS);
			 if(pt < 80) return (0.166192*FF_CR_MULTIJET) + (0.872508*FF_CR_WJETS);
			 if(pt < 100) return (0.33858*FF_CR_MULTIJET) + (0.68742*FF_CR_WJETS);
			 if(pt < 3500) return (0.21549*FF_CR_MULTIJET) + (0.76401*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.3099*FF_CR_MULTIJET) + (0.9297*FF_CR_WJETS);
			 if(pt < 80) return (0.11646*FF_CR_MULTIJET) + (1.17754*FF_CR_WJETS);
			 if(pt < 3500) return (0.39852*FF_CR_MULTIJET) + (0.70848*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.428862*FF_CR_MULTIJET) + (1.449962*FF_CR_WJETS);
			 if(pt < 50) return (-0.400218*FF_CR_MULTIJET) + (1.426418*FF_CR_WJETS);
			 if(pt < 60) return (-0.43596*FF_CR_MULTIJET) + (1.47396*FF_CR_WJETS);
			 if(pt < 80) return (-0.20774*FF_CR_MULTIJET) + (1.24644*FF_CR_WJETS);
			 if(pt < 100) return (0.27702*FF_CR_MULTIJET) + (0.74898*FF_CR_WJETS);
			 if(pt < 3500) return (0.76401*FF_CR_MULTIJET) + (0.21549*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.136356*FF_CR_MULTIJET) + (1.103244*FF_CR_WJETS);
			 if(pt < 80) return (0.47878*FF_CR_MULTIJET) + (0.81522*FF_CR_WJETS);
			 if(pt < 3500) return (0.80811*FF_CR_MULTIJET) + (0.29889*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.561605*FF_CR_MULTIJET) + (0.459495*FF_CR_WJETS);
			 if(pt < 50) return (0.5131*FF_CR_MULTIJET) + (0.5131*FF_CR_WJETS);
			 if(pt < 60) return (0.66432*FF_CR_MULTIJET) + (0.37368*FF_CR_WJETS);
			 if(pt < 80) return (1.090635*FF_CR_MULTIJET) + (-0.0519349999999*FF_CR_WJETS);
			 if(pt < 100) return (1.35432*FF_CR_MULTIJET) + (-0.32832*FF_CR_WJETS);
			 if(pt < 3500) return (1.087245*FF_CR_MULTIJET) + (-0.107745*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.669384*FF_CR_MULTIJET) + (0.570216*FF_CR_WJETS);
			 if(pt < 80) return (0.80228*FF_CR_MULTIJET) + (0.49172*FF_CR_WJETS);
			 if(pt < 3500) return (0.92988*FF_CR_MULTIJET) + (0.17712*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.388018*FF_CR_MULTIJET) + (1.409118*FF_CR_WJETS);
			 if(pt < 50) return (-0.266812*FF_CR_MULTIJET) + (1.293012*FF_CR_WJETS);
			 if(pt < 60) return (-0.39444*FF_CR_MULTIJET) + (1.43244*FF_CR_WJETS);
			 if(pt < 80) return (-0.51935*FF_CR_MULTIJET) + (1.55805*FF_CR_WJETS);
			 if(pt < 100) return (-0.60534*FF_CR_MULTIJET) + (1.63134*FF_CR_WJETS);
			 if(pt < 3500) return (1.99818*FF_CR_MULTIJET) + (-1.01868*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.24792*FF_CR_MULTIJET) + (0.99168*FF_CR_WJETS);
			 if(pt < 80) return (0.0258799999999*FF_CR_MULTIJET) + (1.26812*FF_CR_WJETS);
			 if(pt < 3500) return (0.9963*FF_CR_MULTIJET) + (0.1107*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 45) return (0.112321*FF_CR_MULTIJET) + (0.908779*FF_CR_WJETS);
			 if(pt < 50) return (0.20524*FF_CR_MULTIJET) + (0.82096*FF_CR_WJETS);
			 if(pt < 60) return (0.18684*FF_CR_MULTIJET) + (0.85116*FF_CR_WJETS);
			 if(pt < 80) return (0.332384*FF_CR_MULTIJET) + (0.706316*FF_CR_WJETS);
			 if(pt < 100) return (0.53352*FF_CR_MULTIJET) + (0.49248*FF_CR_WJETS);
			 if(pt < 3500) return (0.930525*FF_CR_MULTIJET) + (0.0489750000001*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 60) return (0.483444*FF_CR_MULTIJET) + (0.756156*FF_CR_WJETS);
			 if(pt < 80) return (0.5176*FF_CR_MULTIJET) + (0.7764*FF_CR_WJETS);
			 if(pt < 3500) return (0.81918*FF_CR_MULTIJET) + (0.28782*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.837302*FF_CR_MULTIJET) + (0.183798*FF_CR_WJETS);
			 if(pt < 50) return (0.71834*FF_CR_MULTIJET) + (0.30786*FF_CR_WJETS);
			 if(pt < 60) return (0.96534*FF_CR_MULTIJET) + (0.0726600000001*FF_CR_WJETS);
			 if(pt < 80) return (1.464567*FF_CR_MULTIJET) + (-0.425867*FF_CR_WJETS);
			 if(pt < 100) return (1.92888*FF_CR_MULTIJET) + (-0.90288*FF_CR_WJETS);
			 if(pt < 3500) return (0.80319*FF_CR_MULTIJET) + (0.17631*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.768552*FF_CR_MULTIJET) + (0.471048*FF_CR_WJETS);
			 if(pt < 80) return (0.91874*FF_CR_MULTIJET) + (0.37526*FF_CR_WJETS);
			 if(pt < 3500) return (0.87453*FF_CR_MULTIJET) + (0.23247*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 50) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 60) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 80) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 100) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 3500) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 80) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 3500) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.751674*FF_CR_MULTIJET) + (1.727874*FF_CR_WJETS);
			 if(pt < 45) return (-0.643434*FF_CR_MULTIJET) + (1.618334*FF_CR_WJETS);
			 if(pt < 50) return (-0.358012*FF_CR_MULTIJET) + (1.325612*FF_CR_WJETS);
			 if(pt < 60) return (-0.39028*FF_CR_MULTIJET) + (1.36598*FF_CR_WJETS);
			 if(pt < 80) return (-0.312387*FF_CR_MULTIJET) + (1.320087*FF_CR_WJETS);
			 if(pt < 100) return (-0.21324*FF_CR_MULTIJET) + (1.27944*FF_CR_WJETS);
			 if(pt < 3500) return (-0.309248*FF_CR_MULTIJET) + (1.275648*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.264366*FF_CR_MULTIJET) + (1.655766*FF_CR_WJETS);
			 if(pt < 60) return (-0.237966*FF_CR_MULTIJET) + (1.637766*FF_CR_WJETS);
			 if(pt < 80) return (-0.22167*FF_CR_MULTIJET) + (1.69947*FF_CR_WJETS);
			 if(pt < 3500) return (-0.290016*FF_CR_MULTIJET) + (1.498416*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.761436*FF_CR_MULTIJET) + (1.737636*FF_CR_WJETS);
			 if(pt < 45) return (-0.643434*FF_CR_MULTIJET) + (1.618334*FF_CR_WJETS);
			 if(pt < 50) return (-0.358012*FF_CR_MULTIJET) + (1.325612*FF_CR_WJETS);
			 if(pt < 60) return (-0.380523*FF_CR_MULTIJET) + (1.356223*FF_CR_WJETS);
			 if(pt < 80) return (-0.352695*FF_CR_MULTIJET) + (1.360395*FF_CR_WJETS);
			 if(pt < 100) return (-0.309198*FF_CR_MULTIJET) + (1.375398*FF_CR_WJETS);
			 if(pt < 3500) return (-0.405888*FF_CR_MULTIJET) + (1.372288*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.306108*FF_CR_MULTIJET) + (1.697508*FF_CR_WJETS);
			 if(pt < 60) return (-0.293958*FF_CR_MULTIJET) + (1.693758*FF_CR_WJETS);
			 if(pt < 80) return (-0.22167*FF_CR_MULTIJET) + (1.69947*FF_CR_WJETS);
			 if(pt < 3500) return (-0.314184*FF_CR_MULTIJET) + (1.522584*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.761436*FF_CR_MULTIJET) + (1.737636*FF_CR_WJETS);
			 if(pt < 45) return (-0.662932*FF_CR_MULTIJET) + (1.637832*FF_CR_WJETS);
			 if(pt < 50) return (-0.38704*FF_CR_MULTIJET) + (1.35464*FF_CR_WJETS);
			 if(pt < 60) return (-0.439065*FF_CR_MULTIJET) + (1.414765*FF_CR_WJETS);
			 if(pt < 80) return (-0.322464*FF_CR_MULTIJET) + (1.330164*FF_CR_WJETS);
			 if(pt < 100) return (-0.234564*FF_CR_MULTIJET) + (1.300764*FF_CR_WJETS);
			 if(pt < 3500) return (-0.135296*FF_CR_MULTIJET) + (1.101696*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.236538*FF_CR_MULTIJET) + (1.627938*FF_CR_WJETS);
			 if(pt < 60) return (-0.237966*FF_CR_MULTIJET) + (1.637766*FF_CR_WJETS);
			 if(pt < 80) return (-0.251226*FF_CR_MULTIJET) + (1.729026*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24168*FF_CR_MULTIJET) + (1.45008*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0585720000001*FF_CR_MULTIJET) + (1.034772*FF_CR_WJETS);
			 if(pt < 45) return (0.0194979999999*FF_CR_MULTIJET) + (0.955402*FF_CR_WJETS);
			 if(pt < 50) return (0.0580559999999*FF_CR_MULTIJET) + (0.909544*FF_CR_WJETS);
			 if(pt < 60) return (0.00975699999992*FF_CR_MULTIJET) + (0.965943*FF_CR_WJETS);
			 if(pt < 80) return (0.0201539999999*FF_CR_MULTIJET) + (0.987546*FF_CR_WJETS);
			 if(pt < 100) return (-0.0319860000001*FF_CR_MULTIJET) + (1.098186*FF_CR_WJETS);
			 if(pt < 3500) return (0.0579839999999*FF_CR_MULTIJET) + (0.908416*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0417419999999*FF_CR_MULTIJET) + (1.349658*FF_CR_WJETS);
			 if(pt < 60) return (0.0279959999999*FF_CR_MULTIJET) + (1.371804*FF_CR_WJETS);
			 if(pt < 80) return (0.0591119999999*FF_CR_MULTIJET) + (1.418688*FF_CR_WJETS);
			 if(pt < 3500) return (0.0362519999999*FF_CR_MULTIJET) + (1.172148*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.263574*FF_CR_MULTIJET) + (1.239774*FF_CR_WJETS);
			 if(pt < 45) return (-0.19498*FF_CR_MULTIJET) + (1.16988*FF_CR_WJETS);
			 if(pt < 50) return (-0.0774080000001*FF_CR_MULTIJET) + (1.045008*FF_CR_WJETS);
			 if(pt < 60) return (-0.126841*FF_CR_MULTIJET) + (1.102541*FF_CR_WJETS);
			 if(pt < 80) return (-0.171309*FF_CR_MULTIJET) + (1.179009*FF_CR_WJETS);
			 if(pt < 100) return (-0.10662*FF_CR_MULTIJET) + (1.17282*FF_CR_WJETS);
			 if(pt < 3500) return (0.0966399999999*FF_CR_MULTIJET) + (0.86976*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0417419999999*FF_CR_MULTIJET) + (1.349658*FF_CR_WJETS);
			 if(pt < 60) return (-0.0139980000001*FF_CR_MULTIJET) + (1.413798*FF_CR_WJETS);
			 if(pt < 80) return (-0.0591120000001*FF_CR_MULTIJET) + (1.536912*FF_CR_WJETS);
			 if(pt < 3500) return (0.0362519999999*FF_CR_MULTIJET) + (1.172148*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (0.956676*FF_CR_MULTIJET) + (0.0195240000001*FF_CR_WJETS);
			 if(pt < 45) return (0.887159*FF_CR_MULTIJET) + (0.0877410000001*FF_CR_WJETS);
			 if(pt < 50) return (0.716024*FF_CR_MULTIJET) + (0.251576*FF_CR_WJETS);
			 if(pt < 60) return (0.946429*FF_CR_MULTIJET) + (0.0292710000001*FF_CR_WJETS);
			 if(pt < 80) return (1.279779*FF_CR_MULTIJET) + (-0.272079*FF_CR_WJETS);
			 if(pt < 100) return (1.01289*FF_CR_MULTIJET) + (0.0533100000001*FF_CR_WJETS);
			 if(pt < 3500) return (-0.705472*FF_CR_MULTIJET) + (1.671872*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.445248*FF_CR_MULTIJET) + (0.946152*FF_CR_WJETS);
			 if(pt < 60) return (0.545922*FF_CR_MULTIJET) + (0.853878*FF_CR_WJETS);
			 if(pt < 80) return (0.783234*FF_CR_MULTIJET) + (0.694566*FF_CR_WJETS);
			 if(pt < 3500) return (-0.12084*FF_CR_MULTIJET) + (1.32924*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.946914*FF_CR_MULTIJET) + (0.0292860000001*FF_CR_WJETS);
			 if(pt < 45) return (0.867661*FF_CR_MULTIJET) + (0.107239*FF_CR_WJETS);
			 if(pt < 50) return (0.764404*FF_CR_MULTIJET) + (0.203196*FF_CR_WJETS);
			 if(pt < 60) return (0.809831*FF_CR_MULTIJET) + (0.165869*FF_CR_WJETS);
			 if(pt < 80) return (1.189086*FF_CR_MULTIJET) + (-0.181386*FF_CR_WJETS);
			 if(pt < 100) return (1.322088*FF_CR_MULTIJET) + (-0.255888*FF_CR_WJETS);
			 if(pt < 3500) return (-0.396224*FF_CR_MULTIJET) + (1.362624*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.55656*FF_CR_MULTIJET) + (0.83484*FF_CR_WJETS);
			 if(pt < 60) return (0.573918*FF_CR_MULTIJET) + (0.825882*FF_CR_WJETS);
			 if(pt < 80) return (0.798012*FF_CR_MULTIJET) + (0.679788*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0845880000001*FF_CR_MULTIJET) + (1.292988*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.107382*FF_CR_MULTIJET) + (1.083582*FF_CR_WJETS);
			 if(pt < 45) return (-0.00974900000008*FF_CR_MULTIJET) + (0.984649*FF_CR_WJETS);
			 if(pt < 50) return (0.0290279999999*FF_CR_MULTIJET) + (0.938572*FF_CR_WJETS);
			 if(pt < 60) return (0.0195139999999*FF_CR_MULTIJET) + (0.956186*FF_CR_WJETS);
			 if(pt < 80) return (-0.0604620000001*FF_CR_MULTIJET) + (1.068162*FF_CR_WJETS);
			 if(pt < 100) return (-0.0959580000001*FF_CR_MULTIJET) + (1.162158*FF_CR_WJETS);
			 if(pt < 3500) return (-0.280256*FF_CR_MULTIJET) + (1.246656*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-1.18637899504e-13*FF_CR_MULTIJET) + (1.3914*FF_CR_WJETS);
			 if(pt < 60) return (-0.0419940000001*FF_CR_MULTIJET) + (1.441794*FF_CR_WJETS);
			 if(pt < 80) return (-0.0147780000001*FF_CR_MULTIJET) + (1.492578*FF_CR_WJETS);
			 if(pt < 3500) return (-0.338352*FF_CR_MULTIJET) + (1.546752*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.29286*FF_CR_MULTIJET) + (1.26906*FF_CR_WJETS);
			 if(pt < 45) return (-0.233976*FF_CR_MULTIJET) + (1.208876*FF_CR_WJETS);
			 if(pt < 50) return (-0.0967600000001*FF_CR_MULTIJET) + (1.06436*FF_CR_WJETS);
			 if(pt < 60) return (-0.136598*FF_CR_MULTIJET) + (1.112298*FF_CR_WJETS);
			 if(pt < 80) return (-0.141078*FF_CR_MULTIJET) + (1.148778*FF_CR_WJETS);
			 if(pt < 100) return (-0.0852960000001*FF_CR_MULTIJET) + (1.151496*FF_CR_WJETS);
			 if(pt < 3500) return (0.0193279999999*FF_CR_MULTIJET) + (0.947072*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0139139999999*FF_CR_MULTIJET) + (1.377486*FF_CR_WJETS);
			 if(pt < 60) return (-0.0419940000001*FF_CR_MULTIJET) + (1.441794*FF_CR_WJETS);
			 if(pt < 80) return (-0.0443340000001*FF_CR_MULTIJET) + (1.522134*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0362520000001*FF_CR_MULTIJET) + (1.244652*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.702864*FF_CR_MULTIJET) + (1.679064*FF_CR_WJETS);
			 if(pt < 45) return (-0.58494*FF_CR_MULTIJET) + (1.55984*FF_CR_WJETS);
			 if(pt < 50) return (-0.33866*FF_CR_MULTIJET) + (1.30626*FF_CR_WJETS);
			 if(pt < 60) return (-0.478093*FF_CR_MULTIJET) + (1.453793*FF_CR_WJETS);
			 if(pt < 80) return (-0.655005*FF_CR_MULTIJET) + (1.662705*FF_CR_WJETS);
			 if(pt < 100) return (-0.575748*FF_CR_MULTIJET) + (1.641948*FF_CR_WJETS);
			 if(pt < 3500) return (1.73952*FF_CR_MULTIJET) + (-0.77312*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.431334*FF_CR_MULTIJET) + (1.822734*FF_CR_WJETS);
			 if(pt < 60) return (-0.363948*FF_CR_MULTIJET) + (1.763748*FF_CR_WJETS);
			 if(pt < 80) return (-0.354672*FF_CR_MULTIJET) + (1.832472*FF_CR_WJETS);
			 if(pt < 3500) return (0.0241679999999*FF_CR_MULTIJET) + (1.184232*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 45) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 50) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 60) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 80) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 100) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 3500) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 60) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 80) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 if(pt < 3500) return (0*FF_CR_MULTIJET) + (1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.044534*FF_CR_MULTIJET) + (2.020734*FF_CR_WJETS);
			 if(pt < 45) return (-0.809167*FF_CR_MULTIJET) + (1.784067*FF_CR_WJETS);
			 if(pt < 50) return (-0.474124*FF_CR_MULTIJET) + (1.441724*FF_CR_WJETS);
			 if(pt < 60) return (-0.556149*FF_CR_MULTIJET) + (1.531849*FF_CR_WJETS);
			 if(pt < 80) return (-0.483696*FF_CR_MULTIJET) + (1.491396*FF_CR_WJETS);
			 if(pt < 100) return (-0.31986*FF_CR_MULTIJET) + (1.38606*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0676480000001*FF_CR_MULTIJET) + (1.034048*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.445248*FF_CR_MULTIJET) + (1.836648*FF_CR_WJETS);
			 if(pt < 60) return (-0.41994*FF_CR_MULTIJET) + (1.81974*FF_CR_WJETS);
			 if(pt < 80) return (-0.354672*FF_CR_MULTIJET) + (1.832472*FF_CR_WJETS);
			 if(pt < 3500) return (-0.18126*FF_CR_MULTIJET) + (1.38966*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


float GetFFCombined_Heavy_Flavour_FF_1down(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 50) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 if(pt < 60) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 80) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
			 if(pt < 100) return (0.33*FF_CR_MULTIJET) + (0.67*FF_CR_WJETS);
			 if(pt < 3500) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 80) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 3500) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 50) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 60) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 100) return (0.27*FF_CR_MULTIJET) + (0.73*FF_CR_WJETS);
			 if(pt < 3500) return (0.78*FF_CR_MULTIJET) + (0.22*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 80) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 3500) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.55*FF_CR_MULTIJET) + (0.45*FF_CR_WJETS);
			 if(pt < 50) return (0.5*FF_CR_MULTIJET) + (0.5*FF_CR_WJETS);
			 if(pt < 60) return (0.64*FF_CR_MULTIJET) + (0.36*FF_CR_WJETS);
			 if(pt < 80) return (1.05*FF_CR_MULTIJET) + (-0.0499999999999*FF_CR_WJETS);
			 if(pt < 100) return (1.32*FF_CR_MULTIJET) + (-0.32*FF_CR_WJETS);
			 if(pt < 3500) return (1.11*FF_CR_MULTIJET) + (-0.11*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 80) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 3500) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 50) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 60) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 80) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 100) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 3500) return (2.04*FF_CR_MULTIJET) + (-1.04*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 45) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 50) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 if(pt < 60) return (0.18*FF_CR_MULTIJET) + (0.82*FF_CR_WJETS);
			 if(pt < 80) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 100) return (0.52*FF_CR_MULTIJET) + (0.48*FF_CR_WJETS);
			 if(pt < 3500) return (0.95*FF_CR_MULTIJET) + (0.0500000000001*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 3500) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 if(pt < 50) return (0.7*FF_CR_MULTIJET) + (0.3*FF_CR_WJETS);
			 if(pt < 60) return (0.93*FF_CR_MULTIJET) + (0.0700000000001*FF_CR_WJETS);
			 if(pt < 80) return (1.41*FF_CR_MULTIJET) + (-0.41*FF_CR_WJETS);
			 if(pt < 100) return (1.88*FF_CR_MULTIJET) + (-0.88*FF_CR_WJETS);
			 if(pt < 3500) return (0.82*FF_CR_MULTIJET) + (0.18*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 80) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 3500) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 if(pt < 50) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 if(pt < 60) return (0.48*FF_CR_MULTIJET) + (0.52*FF_CR_WJETS);
			 if(pt < 80) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 if(pt < 100) return (0.87*FF_CR_MULTIJET) + (0.13*FF_CR_WJETS);
			 if(pt < 3500) return (0.29*FF_CR_MULTIJET) + (0.71*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
			 if(pt < 3500) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 45) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 80) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 100) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 45) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 80) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 100) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 3500) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 45) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 50) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 60) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 80) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 100) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 3500) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 3500) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 45) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 50) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 60) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 100) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 45) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 50) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 60) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 100) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 3500) return (0.0999999999999*FF_CR_MULTIJET) + (0.9*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (0.98*FF_CR_MULTIJET) + (0.0200000000001*FF_CR_WJETS);
			 if(pt < 45) return (0.91*FF_CR_MULTIJET) + (0.0900000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 if(pt < 60) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 if(pt < 80) return (1.27*FF_CR_MULTIJET) + (-0.27*FF_CR_WJETS);
			 if(pt < 100) return (0.95*FF_CR_MULTIJET) + (0.0500000000001*FF_CR_WJETS);
			 if(pt < 3500) return (-0.73*FF_CR_MULTIJET) + (1.73*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.53*FF_CR_MULTIJET) + (0.47*FF_CR_WJETS);
			 if(pt < 3500) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 if(pt < 45) return (0.89*FF_CR_MULTIJET) + (0.11*FF_CR_WJETS);
			 if(pt < 50) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 if(pt < 60) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 80) return (1.18*FF_CR_MULTIJET) + (-0.18*FF_CR_WJETS);
			 if(pt < 100) return (1.24*FF_CR_MULTIJET) + (-0.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 45) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 50) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
			 if(pt < 100) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 3500) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 45) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 50) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 60) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 80) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 100) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.72*FF_CR_MULTIJET) + (1.72*FF_CR_WJETS);
			 if(pt < 45) return (-0.6*FF_CR_MULTIJET) + (1.6*FF_CR_WJETS);
			 if(pt < 50) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 60) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 80) return (-0.65*FF_CR_MULTIJET) + (1.65*FF_CR_WJETS);
			 if(pt < 100) return (-0.54*FF_CR_MULTIJET) + (1.54*FF_CR_WJETS);
			 if(pt < 3500) return (1.8*FF_CR_MULTIJET) + (-0.8*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 60) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 45) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 50) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 80) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 100) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 3500) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.07*FF_CR_MULTIJET) + (2.07*FF_CR_WJETS);
			 if(pt < 45) return (-0.83*FF_CR_MULTIJET) + (1.83*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 80) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 100) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 60) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


float GetFFCombined_binning_1up(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 50) return (0.27*FF_CR_MULTIJET) + (0.73*FF_CR_WJETS);
			 if(pt < 60) return (0.12*FF_CR_MULTIJET) + (0.88*FF_CR_WJETS);
			 if(pt < 80) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
			 if(pt < 100) return (0.49*FF_CR_MULTIJET) + (0.51*FF_CR_WJETS);
			 if(pt < 3500) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 80) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 3500) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 50) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 60) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 80) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 100) return (0.29*FF_CR_MULTIJET) + (0.71*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 80) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 3500) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 if(pt < 50) return (0.68*FF_CR_MULTIJET) + (0.32*FF_CR_WJETS);
			 if(pt < 60) return (0.81*FF_CR_MULTIJET) + (0.19*FF_CR_WJETS);
			 if(pt < 80) return (1.33*FF_CR_MULTIJET) + (-0.33*FF_CR_WJETS);
			 if(pt < 100) return (2.07*FF_CR_MULTIJET) + (-1.07*FF_CR_WJETS);
			 if(pt < 3500) return (1.5*FF_CR_MULTIJET) + (-0.5*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 80) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 3500) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 50) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
			 if(pt < 60) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 80) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 100) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 3500) return (2.75*FF_CR_MULTIJET) + (-1.75*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 45) return (0.19*FF_CR_MULTIJET) + (0.81*FF_CR_WJETS);
			 if(pt < 50) return (0.26*FF_CR_MULTIJET) + (0.74*FF_CR_WJETS);
			 if(pt < 60) return (0.23*FF_CR_MULTIJET) + (0.77*FF_CR_WJETS);
			 if(pt < 80) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
			 if(pt < 100) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 3500) return (1.23*FF_CR_MULTIJET) + (-0.23*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 3500) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (1.02*FF_CR_MULTIJET) + (-0.0199999999999*FF_CR_WJETS);
			 if(pt < 50) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 if(pt < 60) return (1.15*FF_CR_MULTIJET) + (-0.15*FF_CR_WJETS);
			 if(pt < 80) return (1.71*FF_CR_MULTIJET) + (-0.71*FF_CR_WJETS);
			 if(pt < 100) return (2.69*FF_CR_MULTIJET) + (-1.69*FF_CR_WJETS);
			 if(pt < 3500) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 80) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 3500) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 50) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 60) return (0.58*FF_CR_MULTIJET) + (0.42*FF_CR_WJETS);
			 if(pt < 80) return (0.68*FF_CR_MULTIJET) + (0.32*FF_CR_WJETS);
			 if(pt < 100) return (1.13*FF_CR_MULTIJET) + (-0.13*FF_CR_WJETS);
			 if(pt < 3500) return (0.34*FF_CR_MULTIJET) + (0.66*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
			 if(pt < 3500) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.58*FF_CR_MULTIJET) + (1.58*FF_CR_WJETS);
			 if(pt < 45) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
			 if(pt < 50) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 60) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 100) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 3500) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.63*FF_CR_MULTIJET) + (1.63*FF_CR_WJETS);
			 if(pt < 45) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
			 if(pt < 50) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 60) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 100) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 3500) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 45) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 if(pt < 50) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 80) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 100) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 3500) return (0.75*FF_CR_MULTIJET) + (0.25*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 3500) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 45) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 50) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (0.15*FF_CR_MULTIJET) + (0.85*FF_CR_WJETS);
			 if(pt < 100) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 3500) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 45) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 50) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 60) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 80) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 100) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (1.19*FF_CR_MULTIJET) + (-0.19*FF_CR_WJETS);
			 if(pt < 45) return (1.03*FF_CR_MULTIJET) + (-0.0299999999999*FF_CR_WJETS);
			 if(pt < 50) return (0.77*FF_CR_MULTIJET) + (0.23*FF_CR_WJETS);
			 if(pt < 60) return (0.99*FF_CR_MULTIJET) + (0.0100000000001*FF_CR_WJETS);
			 if(pt < 80) return (1.62*FF_CR_MULTIJET) + (-0.62*FF_CR_WJETS);
			 if(pt < 100) return (1.26*FF_CR_MULTIJET) + (-0.26*FF_CR_WJETS);
			 if(pt < 3500) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.53*FF_CR_MULTIJET) + (0.47*FF_CR_WJETS);
			 if(pt < 3500) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (1.02*FF_CR_MULTIJET) + (-0.0199999999999*FF_CR_WJETS);
			 if(pt < 45) return (0.95*FF_CR_MULTIJET) + (0.0500000000001*FF_CR_WJETS);
			 if(pt < 50) return (0.93*FF_CR_MULTIJET) + (0.0700000000001*FF_CR_WJETS);
			 if(pt < 60) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 if(pt < 80) return (1.25*FF_CR_MULTIJET) + (-0.25*FF_CR_WJETS);
			 if(pt < 100) return (2.07*FF_CR_MULTIJET) + (-1.07*FF_CR_WJETS);
			 if(pt < 3500) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 45) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 50) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 60) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 80) return (0.18*FF_CR_MULTIJET) + (0.82*FF_CR_WJETS);
			 if(pt < 100) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 if(pt < 3500) return (0.66*FF_CR_MULTIJET) + (0.34*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 3500) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 45) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 50) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 60) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 80) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 100) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 3500) return (0.31*FF_CR_MULTIJET) + (0.69*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 45) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 50) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 60) return (-0.41*FF_CR_MULTIJET) + (1.41*FF_CR_WJETS);
			 if(pt < 80) return (0.12*FF_CR_MULTIJET) + (0.88*FF_CR_WJETS);
			 if(pt < 100) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 3500) return (3.81*FF_CR_MULTIJET) + (-2.81*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 60) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.58*FF_CR_MULTIJET) + (1.58*FF_CR_WJETS);
			 if(pt < 45) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
			 if(pt < 50) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 60) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 80) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 100) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 3500) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.01*FF_CR_MULTIJET) + (2.01*FF_CR_WJETS);
			 if(pt < 45) return (-0.73*FF_CR_MULTIJET) + (1.73*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 80) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 100) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 60) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


float GetFFCombined_binning_1down(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 50) return (0.17*FF_CR_MULTIJET) + (0.83*FF_CR_WJETS);
			 if(pt < 60) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 100) return (0.17*FF_CR_MULTIJET) + (0.83*FF_CR_WJETS);
			 if(pt < 3500) return (0.12*FF_CR_MULTIJET) + (0.88*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 80) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 3500) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 100) return (0.25*FF_CR_MULTIJET) + (0.75*FF_CR_WJETS);
			 if(pt < 3500) return (0.66*FF_CR_MULTIJET) + (0.34*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.11*FF_CR_MULTIJET) + (0.89*FF_CR_WJETS);
			 if(pt < 80) return (0.37*FF_CR_MULTIJET) + (0.63*FF_CR_WJETS);
			 if(pt < 3500) return (0.73*FF_CR_MULTIJET) + (0.27*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.36*FF_CR_MULTIJET) + (0.64*FF_CR_WJETS);
			 if(pt < 50) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 60) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
			 if(pt < 80) return (0.77*FF_CR_MULTIJET) + (0.23*FF_CR_WJETS);
			 if(pt < 100) return (0.57*FF_CR_MULTIJET) + (0.43*FF_CR_WJETS);
			 if(pt < 3500) return (0.72*FF_CR_MULTIJET) + (0.28*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 80) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 3500) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.52*FF_CR_MULTIJET) + (1.52*FF_CR_WJETS);
			 if(pt < 50) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 60) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 80) return (-0.82*FF_CR_MULTIJET) + (1.82*FF_CR_WJETS);
			 if(pt < 100) return (-1.23*FF_CR_MULTIJET) + (2.23*FF_CR_WJETS);
			 if(pt < 3500) return (1.33*FF_CR_MULTIJET) + (-0.33*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.2*FF_CR_MULTIJET) + (0.8*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 45) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 50) return (0.14*FF_CR_MULTIJET) + (0.86*FF_CR_WJETS);
			 if(pt < 60) return (0.13*FF_CR_MULTIJET) + (0.87*FF_CR_WJETS);
			 if(pt < 80) return (0.17*FF_CR_MULTIJET) + (0.83*FF_CR_WJETS);
			 if(pt < 100) return (0.21*FF_CR_MULTIJET) + (0.79*FF_CR_WJETS);
			 if(pt < 3500) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.42*FF_CR_MULTIJET) + (0.58*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 3500) return (0.74*FF_CR_MULTIJET) + (0.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 50) return (0.5*FF_CR_MULTIJET) + (0.5*FF_CR_WJETS);
			 if(pt < 60) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 80) return (1.11*FF_CR_MULTIJET) + (-0.11*FF_CR_WJETS);
			 if(pt < 100) return (1.07*FF_CR_MULTIJET) + (-0.0699999999999*FF_CR_WJETS);
			 if(pt < 3500) return (0.67*FF_CR_MULTIJET) + (0.33*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.62*FF_CR_MULTIJET) + (0.38*FF_CR_WJETS);
			 if(pt < 80) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 3500) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_MULTIJET) target region
	 if (index==9001) {
	 return FF_CR_MULTIJET;
	}
	 //! Combined FFs for (CLF_TAUJET) target region
	 if (index==1005) {
		 if(ntracks==1){
			 if(pt < 45) return (0.29*FF_CR_MULTIJET) + (0.71*FF_CR_WJETS);
			 if(pt < 50) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 60) return (0.38*FF_CR_MULTIJET) + (0.62*FF_CR_WJETS);
			 if(pt < 80) return (0.66*FF_CR_MULTIJET) + (0.34*FF_CR_WJETS);
			 if(pt < 100) return (0.61*FF_CR_MULTIJET) + (0.39*FF_CR_WJETS);
			 if(pt < 3500) return (0.24*FF_CR_MULTIJET) + (0.76*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
			 if(pt < 3500) return (0.46*FF_CR_MULTIJET) + (0.54*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.96*FF_CR_MULTIJET) + (1.96*FF_CR_WJETS);
			 if(pt < 45) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 50) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 60) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 if(pt < 80) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 100) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 3500) return (-0.94*FF_CR_MULTIJET) + (1.94*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.93*FF_CR_MULTIJET) + (1.93*FF_CR_WJETS);
			 if(pt < 45) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 50) return (-0.51*FF_CR_MULTIJET) + (1.51*FF_CR_WJETS);
			 if(pt < 60) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 80) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 100) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 3500) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.99*FF_CR_MULTIJET) + (1.99*FF_CR_WJETS);
			 if(pt < 45) return (-0.74*FF_CR_MULTIJET) + (1.74*FF_CR_WJETS);
			 if(pt < 50) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 60) return (-0.69*FF_CR_MULTIJET) + (1.69*FF_CR_WJETS);
			 if(pt < 80) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 if(pt < 100) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 3500) return (-1.03*FF_CR_MULTIJET) + (2.03*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 3500) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 45) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 50) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 60) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 80) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 100) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
			 if(pt < 45) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 50) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 60) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 if(pt < 80) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 100) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 3500) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 80) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 3500) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (0.77*FF_CR_MULTIJET) + (0.23*FF_CR_WJETS);
			 if(pt < 45) return (0.79*FF_CR_MULTIJET) + (0.21*FF_CR_WJETS);
			 if(pt < 50) return (0.71*FF_CR_MULTIJET) + (0.29*FF_CR_WJETS);
			 if(pt < 60) return (0.95*FF_CR_MULTIJET) + (0.0500000000001*FF_CR_WJETS);
			 if(pt < 80) return (0.92*FF_CR_MULTIJET) + (0.0800000000001*FF_CR_WJETS);
			 if(pt < 100) return (0.64*FF_CR_MULTIJET) + (0.36*FF_CR_WJETS);
			 if(pt < 3500) return (-1.19*FF_CR_MULTIJET) + (2.19*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.32*FF_CR_MULTIJET) + (0.68*FF_CR_WJETS);
			 if(pt < 60) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
			 if(pt < 80) return (0.53*FF_CR_MULTIJET) + (0.47*FF_CR_WJETS);
			 if(pt < 3500) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.92*FF_CR_MULTIJET) + (0.0800000000001*FF_CR_WJETS);
			 if(pt < 45) return (0.83*FF_CR_MULTIJET) + (0.17*FF_CR_WJETS);
			 if(pt < 50) return (0.65*FF_CR_MULTIJET) + (0.35*FF_CR_WJETS);
			 if(pt < 60) return (0.76*FF_CR_MULTIJET) + (0.24*FF_CR_WJETS);
			 if(pt < 80) return (1.11*FF_CR_MULTIJET) + (-0.11*FF_CR_WJETS);
			 if(pt < 100) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 3500) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.4*FF_CR_MULTIJET) + (0.6*FF_CR_WJETS);
			 if(pt < 60) return (0.41*FF_CR_MULTIJET) + (0.59*FF_CR_WJETS);
			 if(pt < 80) return (0.54*FF_CR_MULTIJET) + (0.46*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 45) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 50) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 80) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 100) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 3500) return (-1.24*FF_CR_MULTIJET) + (2.24*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 3500) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 45) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 50) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 60) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 100) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 3500) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.78*FF_CR_MULTIJET) + (1.78*FF_CR_WJETS);
			 if(pt < 45) return (-0.73*FF_CR_MULTIJET) + (1.73*FF_CR_WJETS);
			 if(pt < 50) return (-0.67*FF_CR_MULTIJET) + (1.67*FF_CR_WJETS);
			 if(pt < 60) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 80) return (-1.42*FF_CR_MULTIJET) + (2.42*FF_CR_WJETS);
			 if(pt < 100) return (-1.49*FF_CR_MULTIJET) + (2.49*FF_CR_WJETS);
			 if(pt < 3500) return (-0.21*FF_CR_MULTIJET) + (1.21*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
			 if(pt < 60) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (FF_CR_WJETS) target region
	 if (index==9002) {
	 return FF_CR_WJETS;
	}
	 //! Combined FFs for (CLF_TAULEP) target region
	 if (index==2010) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.96*FF_CR_MULTIJET) + (1.96*FF_CR_WJETS);
			 if(pt < 45) return (-0.77*FF_CR_MULTIJET) + (1.77*FF_CR_WJETS);
			 if(pt < 50) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 60) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
			 if(pt < 80) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 if(pt < 100) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 3500) return (-0.94*FF_CR_MULTIJET) + (1.94*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.13*FF_CR_MULTIJET) + (2.13*FF_CR_WJETS);
			 if(pt < 45) return (-0.93*FF_CR_MULTIJET) + (1.93*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.65*FF_CR_MULTIJET) + (1.65*FF_CR_WJETS);
			 if(pt < 80) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 100) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 3500) return (-0.98*FF_CR_MULTIJET) + (1.98*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.32*FF_CR_MULTIJET) + (1.32*FF_CR_WJETS);
			 if(pt < 60) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 80) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 3500) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }

	 else return 0;
}


