import ROOT
import numpy as np
import math

xmin = 0.
xmax = 3000.
npoints = 100
halfbin = 0.5*(xmax-xmin)/npoints
outfilename = "eff_mass_taulep_merged.cxx"

def plot_meff(fileName):

  systs = [1, 2, 3, 4, 5, 6, 7]

  COLORS = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kMagenta, ROOT.kOrange, ROOT.kYellow, ROOT.kCyan, ROOT.kCyan+1]

  fs = []
    
  ROOT.gROOT.LoadMacro("eff_mass_taulep.cxx")
  from ROOT import eff_mass_taulep


  x = np.linspace(xmin, xmax, npoints+1)
  ymin_stat = []
  ymax_stat = []
  ymin_syst = []
  ymax_syst = []


  for ii, xx in enumerate(x):
    #ymax.append(max(fs[i].Eval(xx) for i in range(0, len(fs))))
    statplus = 0.0
    statminus = 0.0
    ynom = eff_mass_taulep(int(xx+halfbin),0)
    #print(" xx = ",xx)
    #print(" int(xx+halfbin) = ",xx)
    
    for i, syst in enumerate(systs):
      #print(" i = ",i,"  syst = ",syst)
      y = eff_mass_taulep(int(xx+halfbin),syst) - ynom
      if y>0:
          statplus += y*y
      else:
          statminus += y*y
        
    
    ymax_stat.append(ynom+math.sqrt(statplus))
    ymin_stat.append(ynom-math.sqrt(statminus))

  ### Try writing out the mergged systematics )in form of lookup table:

  with open(outfilename, "a") as cfile:
                index = 0

                cfile.write("\t\t //! NOMINAL \n")
                cfile.write("\t\t if(var==%i || var==%i){\n"%(index,index+1))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(eff_mass_taulep(int(xx+halfbin),index)))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )


                cfile.write("\t\t //! statistical variation UP\n")
                cfile.write("\t\t if(var==%i){\n"%(index+2))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(ymax_stat[ii]))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )

                cfile.write("\t\t //! statistical variation DOWN\n")
                cfile.write("\t\t if(var==%i){\n"%(index+3))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(ymin_stat[ii]))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )

                cfile.write("\t\t std::cout << \"njet SF ERROR:   Unrecognized variation index! \" << var << std::endl; \n")
                cfile.write("\t\t return 1.0; \n")
                cfile.write(" }; \n")
                cfile.write(" \n" )

      
  
##------------------------------------------------------------------------------------
## - - main driver
##------------------------------------------------------------------------------------
if __name__=="__main__":

    
    with open(outfilename, "w") as cfile:
            cfile.write("//             This is an effective mass reweighting for ttbar - from fit\n")
            cfile.write("//             To be used for the tau+lep channel!\n")
            cfile.write("//             in a the lookup table form (after compactification)\n")
            istring = "float eff_mass_taulep(float eff_m,int var){\n"
            cfile.write(istring)
            cfile.write("\t //! xmin: %4.1f \n"%( xmin ) )
            cfile.write("\t //! xmax: %4.1f \n"%( xmax ) )
            cfile.write("\t //! npoints: %i \n"%( npoints ) )
            cfile.write("\t int i = static_cast<int>(%i*(eff_m - %4.1f)/(%4.1f - %4.1f)); \n"%(npoints, xmin, xmax, xmin))
            cfile.write("\t if ( i < 0 || i > %i ) i=%i; \n"%(npoints,npoints))
            cfile.write("\n")
    
    plot_meff(outfilename)
    

