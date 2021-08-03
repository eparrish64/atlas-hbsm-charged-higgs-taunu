float eff_mass_taujet(float eff_m,int var)
{

//effective mass for taujet: with taupt
// from fit

  //if (var != 0) std::cout<<"in eff_mass "<<var<<" "<<eff_m<<std::endl;

  double par0 = 0.;
  double par1 = 0.;
  double par2 = 0.;   
  double par3 = 0.;

  if (var == 0 || var==1)
  {
    par0 =    0.455040; 
    par1 =    0.001959; 
    par2 =    0.001714; 
    par3 =  -53.037334; 
  }
  else if (var==2) //mod 0 up
  {
    par0 =    0.351124; 
    par1 =    0.001214; 
    par2 =    0.001241; 
    par3 =  -259.786708;
  } 
  else if (var==3) //mod 0 down
  {
    par0 =    0.558956;
    par1 =    0.002704; 
    par2 =    0.002187; 
    par3 =  153.712040;  
  }
  else if (var==4) //mod 1 up
  {
    par0 =    0.540129;
    par1 =    0.001759;
    par2 =    0.001850;
    par3 =  -53.037377;
  }
  else if (var==5) //mod 1 down
  {
    par0 =    0.369952;
    par1 =    0.002160;
    par2 =    0.001578;
    par3 =  -53.037291;
  }
  else 
   par0 = 1.;


  double myfunc = par0 + par1*(eff_m - par3)*exp(-par2*eff_m);
  //std::cout<<"myfunc "<<myfunc <<std::endl;
  return myfunc;

}

