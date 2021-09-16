float njets(int n_jets,int var)
{

//njets reweighting for wjets - from fit
// Functional form:   p0 + p1x + p2xx + p3xxx

 double par0 = 0.;
 double par1 = 0.;
 double par2 = 0.;
 double par3 = 0.;

 if (var == 0 || var==1)
 {
   par0 =    0.846034;
   par1 =    0.204287; 
   par2 =   -0.067187;
   par3 =    0.004877;
 }
 else if (var==2) //mod 0 up
 {
   par0 =    1.057846;
   par1 =    0.064605;
   par2 =   -0.038565;
   par3 =    0.003049;
 }
 else if (var==3) //mod 0 down
 {
   par0 =    0.634222;
   par1 =    0.343970;
   par2 =   -0.095808;
   par3 =    0.006706;
 } 
 else if (var==4) //mod 1 up
 {
   par0 =    0.852330;
   par1 =    0.212911;
   par2 =   -0.071661; 
   par3 =    0.005330; 
 }  
 else if (var==5) //mod 1 down
 {
   par0 =    0.839739;
   par1 =    0.195664;
   par2 =   -0.062712;
   par3 =    0.004424;
 }  
 else 
   par0 = 1.;

 double x = (double) n_jets;
 double myfunc = par0 + par1*x + par2*x*x + par3*x*x*x;
 //std::cout<<"myfunc "<<myfunc <<std::endl;
 return myfunc;	

}
