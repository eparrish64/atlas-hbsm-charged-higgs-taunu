//   CAREFUL!  This function returns efficiency of the D1 (tau+jets) generator filter after all SR selections
//             There is a strong signal mass dependence
//             Units are MeV!
float FilterEffi(float met_et=150000., float Hmass=90000.){

  //
  float effi=1.0;
  float loss=0.0;

  if( met_et <170000 ) loss=0.05;
  if( met_et <160000 ) loss=0.15;

  loss *= 1.0-0.00002*(Hmass-90000.);
  if( loss<0.0 ) loss=0.0;

  effi -= loss;

  return effi;

}
