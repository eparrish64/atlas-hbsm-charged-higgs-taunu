import ROOT
import numpy as np
import math

xmin = 0
xmax = 10
npoints = 10
halfbin = 0.5*(xmax-xmin)/npoints
outfilename = "njets_merged.cxx"

def plot_njets(fileName):

  systs = [1, 2, 3, 4, 5]

  COLORS = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kMagenta, ROOT.kOrange, ROOT.kYellow, ROOT.kCyan, ROOT.kCyan+1]

  fs = []
    
  ROOT.gROOT.LoadMacro("njets.cxx")
  from ROOT import njets


  x = np.linspace(xmin, xmax, npoints+1)
  ymin_stat = []
  ymax_stat = []
  ymin_syst = []
  ymax_syst = []


  for ii, xx in enumerate(x):
    #ymax.append(max(fs[i].Eval(xx) for i in range(0, len(fs))))
    statplus = 0.0
    statminus = 0.0
    ynom = njets(int(xx+halfbin),0)
    #print(" xx = ",xx)
    #print(" int(xx+halfbin) = ",xx)
    
    for i, syst in enumerate(systs):
      y = njets(int(xx+halfbin),i) - ynom
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
                      cfile.write("%0.3f, "%(njets(int(xx+halfbin),index)))
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
            cfile.write("//             This is a number of jets reweighting for wjets - from fit\n")
            cfile.write("//             To be used for both tau+jets and tau+lep channels!\n")
            cfile.write("//             in a the lookup table form (after compactification)\n")
            istring = "float njets(int n_jets,int var){\n"
            cfile.write(istring)
            cfile.write("\t //! xmin: %4.1f \n"%( xmin ) )
            cfile.write("\t //! xmax: %4.1f \n"%( xmax ) )
            cfile.write("\t //! npoints: %i \n"%( npoints ) )
            cfile.write("\t int i = static_cast<int>(%i*(n_jets - %4.1f)/(%4.1f - %4.1f)); \n"%(npoints, xmin, xmax, xmin))
            cfile.write("\t if ( i < 0 || i > %i ) i=%i; \n"%(npoints,npoints))
            cfile.write("\n")
    
    plot_njets(outfilename)
    

