float eff_mass_taulep(float eff_m,int var)
{

//effective mass for taulep: with taupt and leppt
// from fit

  //if (var != 0) std::cout<<"in eff_mass "<<var<<" "<<eff_m<<std::endl;

  double par0 = 0.;
  double par1 = 0.;
  double par2 = 0.;   
  double par3 = 0.;

  if (var == 0 || var==1)
  {
    par0 =    0.954958; 
    par1 =    7.61847e-05; 
    par2 =    -1.64189e-07; 
    par3 =   2.67967e-11; 
  }
  else if (var==2) //mod 0 up
  {
    par0 =    0.846007; 
    par1 =    0.000493343; 
    par2 =    -5.97663e-07; 
    par3 =    1.42008e-10;
  } 
  else if (var==3) //mod 0 down
  {
    par0 =    1.06391;
    par1 =    -0.000340974; 
    par2 =    2.69285e-07; 
    par3 =  -8.84145e-11;  
  }
  else if (var==4) //mod 1 up
  {
    par0 =    0.954958;
    par1 =    7.61847e-05;
    par2 =    -1.64189e-07;
    par3 =    3.38885e-11;
  }
  else if (var==5) //mod 1 down
  {
    par0 =    0.954958;
    par1 =    7.61847e-05;
    par2 =    -1.64189e-07;
    par3 =    1.97049e-11;
  }
  else if (var==6) //mod 2 up
  {
    par0 =    0.954958;
    par1 =    -3.58711e-06;
    par2 =    -1.64208e-08;
    par3 =    -2.15138e-11;
  }
  else if (var==7) //mod 2 down
  {
    par0 =    0.954959;
    par1 =    0.000155956;
    par2 =    -3.11957e-07;
    par3 =    7.51073e-11;
  } 
  else 
   par0 = 1.;


  double myfunc = par0 + par1*eff_m + par2*eff_m*eff_m + par3*eff_m*eff_m*eff_m;
  //std::cout<<"myfunc "<<myfunc <<std::endl;
  return myfunc;

}

