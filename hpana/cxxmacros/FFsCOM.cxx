#include <iostream>
float GetFFCombined_NOMINAL(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 50) return (0.22*FF_CR_MULTIJET) + (0.78*FF_CR_WJETS);
			 if(pt < 60) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 80) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
			 if(pt < 3500) return (0.31*FF_CR_MULTIJET) + (0.69*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.86*FF_CR_MULTIJET) + (0.14*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.1*FF_CR_MULTIJET) + (-0.0999999999999*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.77*FF_CR_MULTIJET) + (-0.77*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.97*FF_CR_MULTIJET) + (0.0300000000001*FF_CR_WJETS);
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
	 //! Combined FFs for (TAUJET_BASE) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (1.35*FF_CR_MULTIJET) + (-0.35*FF_CR_WJETS);
			 if(pt < 45) return (1.14*FF_CR_MULTIJET) + (-0.14*FF_CR_WJETS);
			 if(pt < 50) return (1.07*FF_CR_MULTIJET) + (-0.0699999999999*FF_CR_WJETS);
			 if(pt < 60) return (1.31*FF_CR_MULTIJET) + (-0.31*FF_CR_WJETS);
			 if(pt < 80) return (1.9*FF_CR_MULTIJET) + (-0.9*FF_CR_WJETS);
			 if(pt < 3500) return (-0.34*FF_CR_MULTIJET) + (1.34*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.87*FF_CR_MULTIJET) + (0.13*FF_CR_WJETS);
			 if(pt < 60) return (0.78*FF_CR_MULTIJET) + (0.22*FF_CR_WJETS);
			 if(pt < 80) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 if(pt < 3500) return (0.59*FF_CR_MULTIJET) + (0.41*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.89*FF_CR_MULTIJET) + (0.11*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.39*FF_CR_MULTIJET) + (0.61*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
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
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==2006) {
	 return 0;
	}
	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 45) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 50) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 60) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 80) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 60) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 80) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 3500) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.56*FF_CR_MULTIJET) + (1.56*FF_CR_WJETS);
			 if(pt < 45) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 50) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 if(pt < 60) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 80) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 60) return (-0.14*FF_CR_MULTIJET) + (1.14*FF_CR_WJETS);
			 if(pt < 80) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 if(pt < 3500) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_BASE) target region
	 if (index==2020) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 if(pt < 45) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 if(pt < 50) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 60) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
			 if(pt < 80) return (-0.0200000000001*FF_CR_MULTIJET) + (1.02*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0699999999999*FF_CR_MULTIJET) + (0.93*FF_CR_WJETS);
			 if(pt < 60) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 80) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0400000000001*FF_CR_MULTIJET) + (1.04*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.06*FF_CR_MULTIJET) + (2.06*FF_CR_WJETS);
			 if(pt < 45) return (-0.79*FF_CR_MULTIJET) + (1.79*FF_CR_WJETS);
			 if(pt < 50) return (-0.53*FF_CR_MULTIJET) + (1.53*FF_CR_WJETS);
			 if(pt < 60) return (-0.55*FF_CR_MULTIJET) + (1.55*FF_CR_WJETS);
			 if(pt < 80) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 3500) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 if(pt < 60) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 80) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 3500) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.25*FF_CR_MULTIJET) + (1.25*FF_CR_WJETS);
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
			 if(pt < 40) return (-1.05*FF_CR_MULTIJET) + (2.05*FF_CR_WJETS);
			 if(pt < 45) return (-0.83*FF_CR_MULTIJET) + (1.83*FF_CR_WJETS);
			 if(pt < 50) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 60) return (-0.57*FF_CR_MULTIJET) + (1.57*FF_CR_WJETS);
			 if(pt < 80) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 60) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.44*FF_CR_MULTIJET) + (0.56*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.13*FF_CR_MULTIJET) + (-0.13*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.22*FF_CR_MULTIJET) + (-0.22*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.97*FF_CR_MULTIJET) + (-0.97*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.04*FF_CR_MULTIJET) + (-0.0399999999999*FF_CR_WJETS);
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
	 //! Combined FFs for (TAUJET_BASE) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (1.42*FF_CR_MULTIJET) + (-0.42*FF_CR_WJETS);
			 if(pt < 45) return (1.2*FF_CR_MULTIJET) + (-0.2*FF_CR_WJETS);
			 if(pt < 50) return (1.11*FF_CR_MULTIJET) + (-0.11*FF_CR_WJETS);
			 if(pt < 60) return (1.36*FF_CR_MULTIJET) + (-0.36*FF_CR_WJETS);
			 if(pt < 80) return (1.98*FF_CR_MULTIJET) + (-0.98*FF_CR_WJETS);
			 if(pt < 3500) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
			 if(pt < 60) return (0.8*FF_CR_MULTIJET) + (0.2*FF_CR_WJETS);
			 if(pt < 80) return (0.86*FF_CR_MULTIJET) + (0.14*FF_CR_WJETS);
			 if(pt < 3500) return (0.61*FF_CR_MULTIJET) + (0.39*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.02*FF_CR_MULTIJET) + (-0.0199999999999*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.47*FF_CR_MULTIJET) + (0.53*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.19*FF_CR_MULTIJET) + (0.81*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.16*FF_CR_MULTIJET) + (0.84*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.31*FF_CR_MULTIJET) + (1.31*FF_CR_WJETS);
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
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==2006) {
	 return 0;
	}
	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 45) return (-0.2*FF_CR_MULTIJET) + (1.2*FF_CR_WJETS);
			 if(pt < 50) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 60) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 80) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 3500) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 60) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 80) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (-0.26*FF_CR_MULTIJET) + (1.26*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.49*FF_CR_MULTIJET) + (1.49*FF_CR_WJETS);
			 if(pt < 45) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 50) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 60) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 if(pt < 80) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 3500) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.11*FF_CR_MULTIJET) + (1.11*FF_CR_WJETS);
			 if(pt < 60) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
			 if(pt < 80) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_BASE) target region
	 if (index==2020) {
		 if(ntracks==1){
			 if(pt < 40) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 45) return (-0.0100000000001*FF_CR_MULTIJET) + (1.01*FF_CR_WJETS);
			 if(pt < 50) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 60) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0899999999999*FF_CR_MULTIJET) + (0.91*FF_CR_WJETS);
			 if(pt < 60) return (0.0599999999999*FF_CR_MULTIJET) + (0.94*FF_CR_WJETS);
			 if(pt < 80) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 if(pt < 3500) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.94*FF_CR_MULTIJET) + (1.94*FF_CR_WJETS);
			 if(pt < 45) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 50) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 60) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 80) return (-0.45*FF_CR_MULTIJET) + (1.45*FF_CR_WJETS);
			 if(pt < 3500) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 60) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 80) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 3500) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.13*FF_CR_MULTIJET) + (1.13*FF_CR_WJETS);
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
			 if(pt < 40) return (-0.92*FF_CR_MULTIJET) + (1.92*FF_CR_WJETS);
			 if(pt < 45) return (-0.72*FF_CR_MULTIJET) + (1.72*FF_CR_WJETS);
			 if(pt < 50) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 60) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 80) return (-0.36*FF_CR_MULTIJET) + (1.36*FF_CR_WJETS);
			 if(pt < 3500) return (0.12*FF_CR_MULTIJET) + (0.88*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 60) return (-0.28*FF_CR_MULTIJET) + (1.28*FF_CR_WJETS);
			 if(pt < 80) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0600000000001*FF_CR_MULTIJET) + (1.06*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.18*FF_CR_MULTIJET) + (0.82*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.58*FF_CR_MULTIJET) + (0.42*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.98*FF_CR_MULTIJET) + (0.0200000000001*FF_CR_WJETS);
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
			 if(pt < 3500) return (1.57*FF_CR_MULTIJET) + (-0.57*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.9*FF_CR_MULTIJET) + (0.1*FF_CR_WJETS);
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
	 //! Combined FFs for (TAUJET_BASE) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (1.28*FF_CR_MULTIJET) + (-0.28*FF_CR_WJETS);
			 if(pt < 45) return (1.09*FF_CR_MULTIJET) + (-0.0899999999999*FF_CR_WJETS);
			 if(pt < 50) return (1.03*FF_CR_MULTIJET) + (-0.0299999999999*FF_CR_WJETS);
			 if(pt < 60) return (1.27*FF_CR_MULTIJET) + (-0.27*FF_CR_WJETS);
			 if(pt < 80) return (1.83*FF_CR_MULTIJET) + (-0.83*FF_CR_WJETS);
			 if(pt < 3500) return (-0.48*FF_CR_MULTIJET) + (1.48*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.84*FF_CR_MULTIJET) + (0.16*FF_CR_WJETS);
			 if(pt < 60) return (0.76*FF_CR_MULTIJET) + (0.24*FF_CR_WJETS);
			 if(pt < 80) return (0.81*FF_CR_MULTIJET) + (0.19*FF_CR_WJETS);
			 if(pt < 3500) return (0.56*FF_CR_MULTIJET) + (0.44*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.77*FF_CR_MULTIJET) + (0.23*FF_CR_WJETS);
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
			 if(pt < 3500) return (0.3*FF_CR_MULTIJET) + (0.7*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.0300000000001*FF_CR_MULTIJET) + (1.03*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.0500000000001*FF_CR_MULTIJET) + (1.05*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.72*FF_CR_MULTIJET) + (1.72*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.62*FF_CR_MULTIJET) + (1.62*FF_CR_WJETS);
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
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==2006) {
	 return 0;
	}
	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.47*FF_CR_MULTIJET) + (1.47*FF_CR_WJETS);
			 if(pt < 45) return (-0.33*FF_CR_MULTIJET) + (1.33*FF_CR_WJETS);
			 if(pt < 50) return (-0.18*FF_CR_MULTIJET) + (1.18*FF_CR_WJETS);
			 if(pt < 60) return (-0.22*FF_CR_MULTIJET) + (1.22*FF_CR_WJETS);
			 if(pt < 80) return (-0.27*FF_CR_MULTIJET) + (1.27*FF_CR_WJETS);
			 if(pt < 3500) return (-0.38*FF_CR_MULTIJET) + (1.38*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 60) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 80) return (-0.17*FF_CR_MULTIJET) + (1.17*FF_CR_WJETS);
			 if(pt < 3500) return (-0.4*FF_CR_MULTIJET) + (1.4*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.64*FF_CR_MULTIJET) + (1.64*FF_CR_WJETS);
			 if(pt < 45) return (-0.5*FF_CR_MULTIJET) + (1.5*FF_CR_WJETS);
			 if(pt < 50) return (-0.29*FF_CR_MULTIJET) + (1.29*FF_CR_WJETS);
			 if(pt < 60) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 80) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 3500) return (-0.15*FF_CR_MULTIJET) + (1.15*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 60) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 if(pt < 80) return (-0.19*FF_CR_MULTIJET) + (1.19*FF_CR_WJETS);
			 if(pt < 3500) return (-0.16*FF_CR_MULTIJET) + (1.16*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_BASE) target region
	 if (index==2020) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 45) return (-0.1*FF_CR_MULTIJET) + (1.1*FF_CR_WJETS);
			 if(pt < 50) return (-8.52651282912e-14*FF_CR_MULTIJET) + (1.0*FF_CR_WJETS);
			 if(pt < 60) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 if(pt < 80) return (-0.0900000000001*FF_CR_MULTIJET) + (1.09*FF_CR_WJETS);
			 if(pt < 3500) return (-0.12*FF_CR_MULTIJET) + (1.12*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 60) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (-0.0800000000001*FF_CR_MULTIJET) + (1.08*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.19*FF_CR_MULTIJET) + (2.19*FF_CR_WJETS);
			 if(pt < 45) return (-0.91*FF_CR_MULTIJET) + (1.91*FF_CR_WJETS);
			 if(pt < 50) return (-0.63*FF_CR_MULTIJET) + (1.63*FF_CR_WJETS);
			 if(pt < 60) return (-0.66*FF_CR_MULTIJET) + (1.66*FF_CR_WJETS);
			 if(pt < 80) return (-0.73*FF_CR_MULTIJET) + (1.73*FF_CR_WJETS);
			 if(pt < 3500) return (-0.42*FF_CR_MULTIJET) + (1.42*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.44*FF_CR_MULTIJET) + (1.44*FF_CR_WJETS);
			 if(pt < 60) return (-0.39*FF_CR_MULTIJET) + (1.39*FF_CR_WJETS);
			 if(pt < 80) return (-0.43*FF_CR_MULTIJET) + (1.43*FF_CR_WJETS);
			 if(pt < 3500) return (-0.46*FF_CR_MULTIJET) + (1.46*FF_CR_WJETS);
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
			 if(pt < 3500) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
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
			 if(pt < 45) return (-0.94*FF_CR_MULTIJET) + (1.94*FF_CR_WJETS);
			 if(pt < 50) return (-0.59*FF_CR_MULTIJET) + (1.59*FF_CR_WJETS);
			 if(pt < 60) return (-0.68*FF_CR_MULTIJET) + (1.68*FF_CR_WJETS);
			 if(pt < 80) return (-0.61*FF_CR_MULTIJET) + (1.61*FF_CR_WJETS);
			 if(pt < 3500) return (-0.23*FF_CR_MULTIJET) + (1.23*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.37*FF_CR_MULTIJET) + (1.37*FF_CR_WJETS);
			 if(pt < 60) return (-0.35*FF_CR_MULTIJET) + (1.35*FF_CR_WJETS);
			 if(pt < 80) return (-0.3*FF_CR_MULTIJET) + (1.3*FF_CR_WJETS);
			 if(pt < 3500) return (-0.24*FF_CR_MULTIJET) + (1.24*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 else return 0;
}

float GetFFCombined_Heavy_Flavour_FF(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){
	 //! Combined FFs for (SR_TAUJET) target region
	 if (index==1001) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.091897551*FF_CR_MULTIJET) + (1.112981449*FF_CR_WJETS);
			 if(pt < 50) return (0.194982142*FF_CR_MULTIJET) + (0.831239657*FF_CR_WJETS);
			 if(pt < 60) return (-0.031140463*FF_CR_MULTIJET) + (1.069155881*FF_CR_WJETS);
			 if(pt < 80) return (0.114257083*FF_CR_MULTIJET) + (0.924443671*FF_CR_WJETS);
			 if(pt < 3500) return (0.30364217*FF_CR_MULTIJET) + (0.675848701*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.297492061*FF_CR_MULTIJET) + (0.942058193*FF_CR_WJETS);
			 if(pt < 80) return (0.219972098*FF_CR_MULTIJET) + (1.073981418*FF_CR_WJETS);
			 if(pt < 3500) return (0.553509703*FF_CR_MULTIJET) + (0.553509703*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR) target region
	 if (index==1002) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.377801042*FF_CR_MULTIJET) + (1.39888494*FF_CR_WJETS);
			 if(pt < 50) return (-0.492586464*FF_CR_MULTIJET) + (1.518808263*FF_CR_WJETS);
			 if(pt < 60) return (-0.290644317*FF_CR_MULTIJET) + (1.328659736*FF_CR_WJETS);
			 if(pt < 80) return (-0.218127158*FF_CR_MULTIJET) + (1.256827912*FF_CR_WJETS);
			 if(pt < 3500) return (0.950106145*FF_CR_MULTIJET) + (0.029384726*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.185932538*FF_CR_MULTIJET) + (1.053617716*FF_CR_WJETS);
			 if(pt < 80) return (0.530520941*FF_CR_MULTIJET) + (0.763432574*FF_CR_WJETS);
			 if(pt < 3500) return (0.752773196*FF_CR_MULTIJET) + (0.35424621*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO) target region
	 if (index==1004) {
		 if(ntracks==1){
			 if(pt < 45) return (0.541174466*FF_CR_MULTIJET) + (0.479909432*FF_CR_WJETS);
			 if(pt < 50) return (0.472062028*FF_CR_MULTIJET) + (0.554159772*FF_CR_WJETS);
			 if(pt < 60) return (0.622809251*FF_CR_MULTIJET) + (0.415206168*FF_CR_WJETS);
			 if(pt < 80) return (1.080248784*FF_CR_MULTIJET) + (-0.04154803*FF_CR_WJETS);
			 if(pt < 3500) return (0.98928578*FF_CR_MULTIJET) + (-0.009794909*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.656961635*FF_CR_MULTIJET) + (0.582588619*FF_CR_WJETS);
			 if(pt < 80) return (0.698734899*FF_CR_MULTIJET) + (0.595218617*FF_CR_WJETS);
			 if(pt < 3500) return (0.929896301*FF_CR_MULTIJET) + (0.177123105*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (WJETS) target region
	 if (index==1003) {
		 if(ntracks==1){
			 if(pt < 45) return (-0.408433559*FF_CR_MULTIJET) + (1.429517457*FF_CR_WJETS);
			 if(pt < 50) return (-0.287342104*FF_CR_MULTIJET) + (1.313563903*FF_CR_WJETS);
			 if(pt < 60) return (-0.363305397*FF_CR_MULTIJET) + (1.401320815*FF_CR_WJETS);
			 if(pt < 80) return (-0.498576362*FF_CR_MULTIJET) + (1.537277115*FF_CR_WJETS);
			 if(pt < 3500) return (1.733698842*FF_CR_MULTIJET) + (-0.754207971*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.247910051*FF_CR_MULTIJET) + (0.991640203*FF_CR_WJETS);
			 if(pt < 80) return (0.155274422*FF_CR_MULTIJET) + (1.138679094*FF_CR_WJETS);
			 if(pt < 3500) return (1.084879018*FF_CR_MULTIJET) + (0.022140388*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_PRESEL) target region
	 if (index==1000) {
		 if(ntracks==1){
			 if(pt < 40) return (0.020421678*FF_CR_MULTIJET) + (1.00066222*FF_CR_WJETS);
			 if(pt < 45) return (0.020421678*FF_CR_MULTIJET) + (1.00066222*FF_CR_WJETS);
			 if(pt < 50) return (0.123146616*FF_CR_MULTIJET) + (0.903075183*FF_CR_WJETS);
			 if(pt < 60) return (0.186842775*FF_CR_MULTIJET) + (0.851172643*FF_CR_WJETS);
			 if(pt < 80) return (0.176579128*FF_CR_MULTIJET) + (0.862121625*FF_CR_WJETS);
			 if(pt < 3500) return (0.91092651*FF_CR_MULTIJET) + (0.068564361*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.471029097*FF_CR_MULTIJET) + (0.73133465*FF_CR_WJETS);
			 if(pt < 60) return (0.471029097*FF_CR_MULTIJET) + (0.768521158*FF_CR_WJETS);
			 if(pt < 80) return (0.491702336*FF_CR_MULTIJET) + (0.80225118*FF_CR_WJETS);
			 if(pt < 3500) return (0.852404943*FF_CR_MULTIJET) + (0.254614463*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUJET_BASE) target region
	 if (index==1009) {
		 if(ntracks==1){
			 if(pt < 40) return (1.368252423*FF_CR_MULTIJET) + (-0.347168525*FF_CR_WJETS);
			 if(pt < 45) return (1.368252423*FF_CR_MULTIJET) + (-0.153162585*FF_CR_WJETS);
			 if(pt < 50) return (1.180155069*FF_CR_MULTIJET) + (-0.061573308*FF_CR_WJETS);
			 if(pt < 60) return (1.100296344*FF_CR_MULTIJET) + (-0.32178478*FF_CR_WJETS);
			 if(pt < 80) return (1.360697987*FF_CR_MULTIJET) + (-0.955604693*FF_CR_WJETS);
			 if(pt < 3500) return (-0.205693083*FF_CR_MULTIJET) + (1.185183954*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.991640203*FF_CR_MULTIJET) + (0.161141533*FF_CR_WJETS);
			 if(pt < 60) return (0.991640203*FF_CR_MULTIJET) + (0.247910051*FF_CR_WJETS);
			 if(pt < 80) return (1.125739559*FF_CR_MULTIJET) + (0.168213957*FF_CR_WJETS);
			 if(pt < 3500) return (0.675281838*FF_CR_MULTIJET) + (0.431737568*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (BVETO_MT100) target region
	 if (index==1006) {
		 if(ntracks==1){
			 if(pt < 45) return (0.827077957*FF_CR_MULTIJET) + (0.194005941*FF_CR_WJETS);
			 if(pt < 50) return (0.831239657*FF_CR_MULTIJET) + (0.348915412*FF_CR_WJETS);
			 if(pt < 60) return (0.685090176*FF_CR_MULTIJET) + (0.114181696*FF_CR_WJETS);
			 if(pt < 80) return (0.924443671*FF_CR_MULTIJET) + (-0.415480301*FF_CR_WJETS);
			 if(pt < 3500) return (0.773797788*FF_CR_MULTIJET) + (0.205693083*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.756125655*FF_CR_MULTIJET) + (0.483424599*FF_CR_WJETS);
			 if(pt < 80) return (0.815190715*FF_CR_MULTIJET) + (0.478762801*FF_CR_WJETS);
			 if(pt < 3500) return (0.885615525*FF_CR_MULTIJET) + (0.221403881*FF_CR_WJETS);
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
			 if(pt < 45) return (0.336957686*FF_CR_MULTIJET) + (0.684126212*FF_CR_WJETS);
			 if(pt < 50) return (0.46179981*FF_CR_MULTIJET) + (0.56442199*FF_CR_WJETS);
			 if(pt < 60) return (0.467106938*FF_CR_MULTIJET) + (0.57090848*FF_CR_WJETS);
			 if(pt < 80) return (0.685542497*FF_CR_MULTIJET) + (0.353158256*FF_CR_WJETS);
			 if(pt < 3500) return (0.362411622*FF_CR_MULTIJET) + (0.617079249*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 60) return (0.495820102*FF_CR_MULTIJET) + (0.743730152*FF_CR_WJETS);
			 if(pt < 80) return (0.595218617*FF_CR_MULTIJET) + (0.698734899*FF_CR_WJETS);
			 if(pt < 3500) return (0.575650091*FF_CR_MULTIJET) + (0.531369315*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAULEP) target region
	 if (index==2001) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.771213541*FF_CR_MULTIJET) + (1.747433213*FF_CR_WJETS);
			 if(pt < 45) return (-0.643421782*FF_CR_MULTIJET) + (1.61830327*FF_CR_WJETS);
			 if(pt < 50) return (-0.34832269*FF_CR_MULTIJET) + (1.315885719*FF_CR_WJETS);
			 if(pt < 60) return (-0.390281009*FF_CR_MULTIJET) + (1.36598353*FF_CR_WJETS);
			 if(pt < 80) return (-0.332540701*FF_CR_MULTIJET) + (1.340239793*FF_CR_WJETS);
			 if(pt < 3500) return (-0.193288063*FF_CR_MULTIJET) + (1.159728377*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.278278938*FF_CR_MULTIJET) + (1.669673628*FF_CR_WJETS);
			 if(pt < 60) return (-0.251965718*FF_CR_MULTIJET) + (1.651775259*FF_CR_WJETS);
			 if(pt < 80) return (-0.221670558*FF_CR_MULTIJET) + (1.699474278*FF_CR_WJETS);
			 if(pt < 3500) return (-0.145005269*FF_CR_MULTIJET) + (1.353382511*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUEL) target region
	 if (index==2002) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.790737934*FF_CR_MULTIJET) + (1.766957606*FF_CR_WJETS);
			 if(pt < 45) return (-0.662919412*FF_CR_MULTIJET) + (1.6378009*FF_CR_WJETS);
			 if(pt < 50) return (-0.357998321*FF_CR_MULTIJET) + (1.325561349*FF_CR_WJETS);
			 if(pt < 60) return (-0.390281009*FF_CR_MULTIJET) + (1.36598353*FF_CR_WJETS);
			 if(pt < 80) return (-0.342617691*FF_CR_MULTIJET) + (1.350316784*FF_CR_WJETS);
			 if(pt < 3500) return (-0.260938885*FF_CR_MULTIJET) + (1.227379199*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.333934726*FF_CR_MULTIJET) + (1.725329415*FF_CR_WJETS);
			 if(pt < 60) return (-0.293960004*FF_CR_MULTIJET) + (1.693769546*FF_CR_WJETS);
			 if(pt < 80) return (-0.147780372*FF_CR_MULTIJET) + (1.625584092*FF_CR_WJETS);
			 if(pt < 3500) return (-0.181256586*FF_CR_MULTIJET) + (1.389633828*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SR_TAUMU) target region
	 if (index==2003) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.790737934*FF_CR_MULTIJET) + (1.766957606*FF_CR_WJETS);
			 if(pt < 45) return (-0.662919412*FF_CR_MULTIJET) + (1.6378009*FF_CR_WJETS);
			 if(pt < 50) return (-0.387025211*FF_CR_MULTIJET) + (1.35458824*FF_CR_WJETS);
			 if(pt < 60) return (-0.44882316*FF_CR_MULTIJET) + (1.424525682*FF_CR_WJETS);
			 if(pt < 80) return (-0.342617691*FF_CR_MULTIJET) + (1.350316784*FF_CR_WJETS);
			 if(pt < 3500) return (-0.15463045*FF_CR_MULTIJET) + (1.121070764*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.264364991*FF_CR_MULTIJET) + (1.655759681*FF_CR_WJETS);
			 if(pt < 60) return (-0.237967622*FF_CR_MULTIJET) + (1.637777164*FF_CR_WJETS);
			 if(pt < 80) return (-0.251226632*FF_CR_MULTIJET) + (1.729030352*FF_CR_WJETS);
			 if(pt < 3500) return (-0.096670179*FF_CR_MULTIJET) + (1.305047421*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUEL_BVETO) target region
	 if (index==2004) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.0700000000001*FF_CR_MULTIJET) + (1.07*FF_CR_WJETS);
			 if(pt < 45) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 50) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 if(pt < 60) return (0.00999999999991*FF_CR_MULTIJET) + (0.99*FF_CR_WJETS);
			 if(pt < 80) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 3500) return (0.0799999999999*FF_CR_MULTIJET) + (0.92*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.0299999999999*FF_CR_MULTIJET) + (0.97*FF_CR_WJETS);
			 if(pt < 60) return (0.0199999999999*FF_CR_MULTIJET) + (0.98*FF_CR_WJETS);
			 if(pt < 80) return (0.0399999999999*FF_CR_MULTIJET) + (0.96*FF_CR_WJETS);
			 if(pt < 3500) return (0.0499999999999*FF_CR_MULTIJET) + (0.95*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAUMU_BVETO) target region
	 if (index==2005) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.263579311*FF_CR_MULTIJET) + (1.239798983*FF_CR_WJETS);
			 if(pt < 45) return (-0.194976298*FF_CR_MULTIJET) + (1.169857786*FF_CR_WJETS);
			 if(pt < 50) return (-0.087080673*FF_CR_MULTIJET) + (1.054643701*FF_CR_WJETS);
			 if(pt < 60) return (-0.117084303*FF_CR_MULTIJET) + (1.092786824*FF_CR_WJETS);
			 if(pt < 80) return (-0.181385837*FF_CR_MULTIJET) + (1.189084929*FF_CR_WJETS);
			 if(pt < 3500) return (0.096644031*FF_CR_MULTIJET) + (0.869796283*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.041741841*FF_CR_MULTIJET) + (1.349652849*FF_CR_WJETS);
			 if(pt < 60) return (-0.013998095*FF_CR_MULTIJET) + (1.413807637*FF_CR_WJETS);
			 if(pt < 80) return (-0.073890186*FF_CR_MULTIJET) + (1.551693906*FF_CR_WJETS);
			 if(pt < 3500) return (0.084586407*FF_CR_MULTIJET) + (1.123790835*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUEL) target region
	 if (index==2007) {
		 if(ntracks==1){
			 if(pt < 40) return (0.956695278*FF_CR_MULTIJET) + (0.019524393*FF_CR_WJETS);
			 if(pt < 45) return (0.887142154*FF_CR_MULTIJET) + (0.087739334*FF_CR_WJETS);
			 if(pt < 50) return (0.68696975*FF_CR_MULTIJET) + (0.280593278*FF_CR_WJETS);
			 if(pt < 60) return (0.91716037*FF_CR_MULTIJET) + (0.058542151*FF_CR_WJETS);
			 if(pt < 80) return (1.279777847*FF_CR_MULTIJET) + (-0.272078755*FF_CR_WJETS);
			 if(pt < 3500) return (-0.444562544*FF_CR_MULTIJET) + (1.411002859*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.445246301*FF_CR_MULTIJET) + (0.946148389*FF_CR_WJETS);
			 if(pt < 60) return (0.545925721*FF_CR_MULTIJET) + (0.85388382*FF_CR_WJETS);
			 if(pt < 80) return (0.768457934*FF_CR_MULTIJET) + (0.709345785*FF_CR_WJETS);
			 if(pt < 3500) return (0.036251317*FF_CR_MULTIJET) + (1.172125924*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (SS_TAUMU) target region
	 if (index==2008) {
		 if(ntracks==1){
			 if(pt < 40) return (0.937170885*FF_CR_MULTIJET) + (0.039048787*FF_CR_WJETS);
			 if(pt < 45) return (0.867644525*FF_CR_MULTIJET) + (0.107236964*FF_CR_WJETS);
			 if(pt < 50) return (0.754699162*FF_CR_MULTIJET) + (0.212863866*FF_CR_WJETS);
			 if(pt < 60) return (0.790319043*FF_CR_MULTIJET) + (0.185383479*FF_CR_WJETS);
			 if(pt < 80) return (1.189084929*FF_CR_MULTIJET) + (-0.181385837*FF_CR_WJETS);
			 if(pt < 3500) return (-0.444562544*FF_CR_MULTIJET) + (1.411002859*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.528729982*FF_CR_MULTIJET) + (0.862664708*FF_CR_WJETS);
			 if(pt < 60) return (0.573921912*FF_CR_MULTIJET) + (0.82588763*FF_CR_WJETS);
			 if(pt < 80) return (0.798014009*FF_CR_MULTIJET) + (0.679789711*FF_CR_WJETS);
			 if(pt < 3500) return (0.04833509*FF_CR_MULTIJET) + (1.160042152*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (DILEP_BTAG) target region
	 if (index==2006) {
	 return 0;
	}
	 //! Combined FFs for (ZEE) target region
	 if (index==2009) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.390487869*FF_CR_MULTIJET) + (1.366707541*FF_CR_WJETS);
			 if(pt < 45) return (-0.263218002*FF_CR_MULTIJET) + (1.23809949*FF_CR_WJETS);
			 if(pt < 50) return (-0.116107563*FF_CR_MULTIJET) + (1.083670592*FF_CR_WJETS);
			 if(pt < 60) return (-0.146355378*FF_CR_MULTIJET) + (1.1220579*FF_CR_WJETS);
			 if(pt < 80) return (-0.181385837*FF_CR_MULTIJET) + (1.189084929*FF_CR_WJETS);
			 if(pt < 3500) return (-0.18362366*FF_CR_MULTIJET) + (1.150063974*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.18088131*FF_CR_MULTIJET) + (1.572275999*FF_CR_WJETS);
			 if(pt < 60) return (-0.195973336*FF_CR_MULTIJET) + (1.595782878*FF_CR_WJETS);
			 if(pt < 80) return (-0.192114484*FF_CR_MULTIJET) + (1.669918203*FF_CR_WJETS);
			 if(pt < 3500) return (-0.338345628*FF_CR_MULTIJET) + (1.546722869*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_PRESEL) target region
	 if (index==2000) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.556445213*FF_CR_MULTIJET) + (1.532664885*FF_CR_WJETS);
			 if(pt < 45) return (-0.41919904*FF_CR_MULTIJET) + (1.394080528*FF_CR_WJETS);
			 if(pt < 50) return (-0.222539497*FF_CR_MULTIJET) + (1.190102525*FF_CR_WJETS);
			 if(pt < 60) return (-0.282953731*FF_CR_MULTIJET) + (1.258656253*FF_CR_WJETS);
			 if(pt < 80) return (-0.292232737*FF_CR_MULTIJET) + (1.299931829*FF_CR_WJETS);
			 if(pt < 3500) return (-0.028993209*FF_CR_MULTIJET) + (0.995433523*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.18088131*FF_CR_MULTIJET) + (1.572275999*FF_CR_WJETS);
			 if(pt < 60) return (-0.209971431*FF_CR_MULTIJET) + (1.609780973*FF_CR_WJETS);
			 if(pt < 80) return (-0.221670558*FF_CR_MULTIJET) + (1.699474278*FF_CR_WJETS);
			 if(pt < 3500) return (-0.084586407*FF_CR_MULTIJET) + (1.292963649*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TAULEP_BASE) target region
	 if (index==2020) {
		 if(ntracks==1){
			 if(pt < 40) return (-0.039048787*FF_CR_MULTIJET) + (1.015268459*FF_CR_WJETS);
			 if(pt < 45) return (-0.058492889*FF_CR_MULTIJET) + (1.033374378*FF_CR_WJETS);
			 if(pt < 50) return (0.038702521*FF_CR_MULTIJET) + (0.928860507*FF_CR_WJETS);
			 if(pt < 60) return (-0.048785126*FF_CR_MULTIJET) + (1.024487648*FF_CR_WJETS);
			 if(pt < 80) return (-0.090692918*FF_CR_MULTIJET) + (1.098392011*FF_CR_WJETS);
			 if(pt < 3500) return (0.028993209*FF_CR_MULTIJET) + (0.937447105*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (0.111311575*FF_CR_MULTIJET) + (1.280083115*FF_CR_WJETS);
			 if(pt < 60) return (0.055992382*FF_CR_MULTIJET) + (1.34381716*FF_CR_WJETS);
			 if(pt < 80) return (0.073890186*FF_CR_MULTIJET) + (1.403913534*FF_CR_WJETS);
			 if(pt < 3500) return (-1.03032e-13*FF_CR_MULTIJET) + (1.208377242*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (TTBAR_TAULEP) target region
	 if (index==2021) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.064079442*FF_CR_MULTIJET) + (2.040299114*FF_CR_WJETS);
			 if(pt < 45) return (-0.81890045*FF_CR_MULTIJET) + (1.793781938*FF_CR_WJETS);
			 if(pt < 50) return (-0.512808405*FF_CR_MULTIJET) + (1.480371434*FF_CR_WJETS);
			 if(pt < 60) return (-0.536636387*FF_CR_MULTIJET) + (1.512338909*FF_CR_WJETS);
			 if(pt < 80) return (-0.634850428*FF_CR_MULTIJET) + (1.642549521*FF_CR_WJETS);
			 if(pt < 3500) return (-0.086979628*FF_CR_MULTIJET) + (1.053419942*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.58438577*FF_CR_MULTIJET) + (1.975780459*FF_CR_WJETS);
			 if(pt < 60) return (-0.51792953*FF_CR_MULTIJET) + (1.917739072*FF_CR_WJETS);
			 if(pt < 80) return (-0.502453265*FF_CR_MULTIJET) + (1.980256984*FF_CR_WJETS);
			 if(pt < 3500) return (-0.326261855*FF_CR_MULTIJET) + (1.534639097*FF_CR_WJETS);
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
			 if(pt < 40) return (-0.771213541*FF_CR_MULTIJET) + (1.747433213*FF_CR_WJETS);
			 if(pt < 45) return (-0.643421782*FF_CR_MULTIJET) + (1.61830327*FF_CR_WJETS);
			 if(pt < 50) return (-0.34832269*FF_CR_MULTIJET) + (1.315885719*FF_CR_WJETS);
			 if(pt < 60) return (-0.390281009*FF_CR_MULTIJET) + (1.36598353*FF_CR_WJETS);
			 if(pt < 80) return (-0.332540701*FF_CR_MULTIJET) + (1.340239793*FF_CR_WJETS);
			 if(pt < 3500) return (-0.193288063*FF_CR_MULTIJET) + (1.159728377*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.278278938*FF_CR_MULTIJET) + (1.669673628*FF_CR_WJETS);
			 if(pt < 60) return (-0.251965718*FF_CR_MULTIJET) + (1.651775259*FF_CR_WJETS);
			 if(pt < 80) return (-0.221670558*FF_CR_MULTIJET) + (1.699474278*FF_CR_WJETS);
			 if(pt < 3500) return (-0.145005269*FF_CR_MULTIJET) + (1.353382511*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 //! Combined FFs for (MET_TRIG_EFF_CR_NOM) target region
	 if (index==2011) {
		 if(ntracks==1){
			 if(pt < 40) return (-1.044555049*FF_CR_MULTIJET) + (2.020774721*FF_CR_WJETS);
			 if(pt < 45) return (-0.81890045*FF_CR_MULTIJET) + (1.793781938*FF_CR_WJETS);
			 if(pt < 50) return (-0.493457145*FF_CR_MULTIJET) + (1.461020173*FF_CR_WJETS);
			 if(pt < 60) return (-0.565907463*FF_CR_MULTIJET) + (1.541609984*FF_CR_WJETS);
			 if(pt < 80) return (-0.453464592*FF_CR_MULTIJET) + (1.461163684*FF_CR_WJETS);
			 if(pt < 3500) return (-0.019328806*FF_CR_MULTIJET) + (0.98576912*FF_CR_WJETS);
			 else return 0;
		 }
		 if(ntracks==3){
			 if(pt < 40) return (-0.473074195*FF_CR_MULTIJET) + (1.864468884*FF_CR_WJETS);
			 if(pt < 60) return (-0.447939053*FF_CR_MULTIJET) + (1.847748595*FF_CR_WJETS);
			 if(pt < 80) return (-0.354672893*FF_CR_MULTIJET) + (1.832476612*FF_CR_WJETS);
			 if(pt < 3500) return (-0.120837724*FF_CR_MULTIJET) + (1.329214966*FF_CR_WJETS);
			 else return 0;
		 }
		 else return 0;
	 }
	 else return 0;
}

