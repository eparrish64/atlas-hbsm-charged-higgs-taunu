//   MetEfficiency xe70("xe70", "../TriggerEfficiency/met_efficiencies_lcw70.root", tnew);
//   MetEfficiency xe90("xe90", "../TriggerEfficiency/met_efficiencies_mht90.root", tnew);
//   MetEfficiency xe110("xe110", "../TriggerEfficiency/met_efficiencies_mht110.root", tnew);


// TriggerEfficiency/met_efficiencies_lcw70.root:/ 17 Keys
// fit_met_3jets       fit_met_binning     fit_met_e_medium    fit_met_e_tight     fit_met_nominal     fit_met_stat        fit_met_tau_medium  fit_met_tau_tight   
// TriggerEfficiency/met_efficiencies_mht110.root:/ 15 Keys
// fit_met_3jets       fit_met_e_medium    fit_met_e_tight     fit_met_nominal     fit_met_stat        fit_met_tau_medium  fit_met_tau_tight   
// TriggerEfficiency/met_efficiencies_mht90.root:/ 15 Keys
// fit_met_3jets       fit_met_e_medium    fit_met_e_tight     fit_met_nominal     fit_met_stat        fit_met_tau_medium  fit_met_tau_tight   

#include <TF1.h>
#include <TFile.h>

TF1* fit_met_3jets_70(0);       
TF1* fit_met_binning_70(0);     
TF1* fit_met_e_medium_70(0);    
TF1* fit_met_e_tight_70(0);     
TF1* fit_met_nominal_70(0);     
TF1* fit_met_stat_70(0);        
TF1* fit_met_tau_medium_70(0);
TF1* fit_met_tau_tight_70(0);

TF1* fit_met_3jets_110(0);
TF1* fit_met_e_medium_110(0);
TF1* fit_met_e_tight_110(0);     
TF1* fit_met_nominal_110(0);     
TF1* fit_met_stat_110(0);        
TF1* fit_met_tau_medium_110(0);   
TF1* fit_met_tau_tight_110(0);

TF1* fit_met_3jets_90(0);
TF1* fit_met_e_medium_90(0);
TF1* fit_met_e_tight_90(0);     
TF1* fit_met_nominal_90(0);     
TF1* fit_met_stat_90(0);        
TF1* fit_met_tau_medium_90(0);   
TF1* fit_met_tau_tight_90(0);

double r70=3212.96/36074.6;
double r90=6116.5131/36074.6;
double r110=1-r70-r90;
void load_data();
void reset_data();
void ApplyEff(){reset_data();}

float nominal_trig_eff(float met){
  load_data();
  return r70*fit_met_nominal_70->Eval(met)+r90*fit_met_nominal_90->Eval(met)+r110*fit_met_nominal_110->Eval(met);
}

float e_medium_trig_eff(float met){
  load_data();
  return r70*fit_met_e_medium_70->Eval(met)+r90*fit_met_e_medium_90->Eval(met)+r110*fit_met_e_medium_110->Eval(met);
}

float e_tight_trig_eff(float met){
  load_data();
  return r70*fit_met_e_tight_70->Eval(met)+r90*fit_met_e_tight_90->Eval(met)+r110*fit_met_e_tight_110->Eval(met);
}


float tau_medium_trig_eff(float met){
  load_data();
  return r70*fit_met_tau_medium_70->Eval(met)+r90*fit_met_tau_medium_90->Eval(met)+r110*fit_met_tau_medium_110->Eval(met);
}

float tau_tight_trig_eff(float met){
  load_data();
  return r70*fit_met_tau_tight_70->Eval(met)+r90*fit_met_tau_tight_90->Eval(met)+r110*fit_met_tau_tight_110->Eval(met);
}

float Threejets_trig_eff(float met){
  load_data();
  return r70*fit_met_3jets_70->Eval(met)+r90*fit_met_3jets_90->Eval(met)+r110*fit_met_3jets_110->Eval(met);
}


// uncertainties 
float stat_trig_eff(float met){
  load_data();
  return r70*fit_met_stat_70->Eval(met)+r90*fit_met_stat_90->Eval(met)+r110*fit_met_stat_110->Eval(met);
}
// float binning_trig_eff(float met){
//   load_data();
//   return r70*fit_met_binning_70->Eval(met)+r90*fit_met_binning_90->Eval(met)+r110*fit_met_binning_110->Eval(met);
// }

void load_data(){

  if(fit_met_nominal_110) return;

  TFile* f_70 = TFile::Open("met_efficiencies_lcw70.root");
  TFile* f_90 = TFile::Open("met_efficiencies_mht90.root");
  TFile* f_110 = TFile::Open("met_efficiencies_mht110.root");

  fit_met_3jets_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_3jets"));       
  fit_met_binning_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_binning"));     
  fit_met_e_medium_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_e_medium"));    
  fit_met_e_tight_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_e_tight"));     
  fit_met_nominal_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_nominal"));     
  fit_met_stat_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_stat"));        
  fit_met_tau_medium_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_tau_medium"));
  fit_met_tau_tight_70 = dynamic_cast<TF1*> (f_70->Get("fit_met_tau_tight"));

  fit_met_3jets_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_3jets"));
  fit_met_e_medium_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_e_medium"));
  fit_met_e_tight_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_e_tight"));     
  fit_met_nominal_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_nominal"));     
  fit_met_stat_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_stat"));        
  fit_met_tau_medium_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_tau_medium"));   
  fit_met_tau_tight_110 = dynamic_cast<TF1*> (f_110->Get("fit_met_tau_tight"));

  fit_met_3jets_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_3jets"));
  fit_met_e_medium_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_e_medium"));
  fit_met_e_tight_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_e_tight"));     
  fit_met_nominal_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_nominal"));     
  fit_met_stat_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_stat"));        
  fit_met_tau_medium_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_tau_medium"));   
  fit_met_tau_tight_90 = dynamic_cast<TF1*> (f_90->Get("fit_met_tau_tight"));

  f_70->Close();
  f_90->Close();
  f_110->Close();  
}

void reset_data(){
  fit_met_3jets_70 = 0;       
  fit_met_binning_70 = 0;     
  fit_met_e_medium_70 = 0;    
  fit_met_e_tight_70 = 0;     
  fit_met_nominal_70 = 0;     
  fit_met_stat_70 = 0;        
  fit_met_tau_medium_70 = 0;
  fit_met_tau_tight_70 = 0;

  fit_met_3jets_110 = 0;
  fit_met_e_medium_110 = 0;
  fit_met_e_tight_110 = 0;     
  fit_met_nominal_110 = 0;     
  fit_met_stat_110 = 0;        
  fit_met_tau_medium_110 = 0;   
  fit_met_tau_tight_110 = 0;

  fit_met_3jets_90 = 0;
  fit_met_e_medium_90 = 0;
  fit_met_e_tight_90 = 0;     
  fit_met_nominal_90 = 0;     
  fit_met_stat_90 = 0;        
  fit_met_tau_medium_90 = 0;   
  fit_met_tau_tight_90 = 0;
}
