import ROOT
import numpy as np
import math

xmin = 50
xmax = 250
npoints = 100
halfbin = 0.5*(xmax-xmin)/npoints
outfilename = "metTrigEff.cxx"

def plot_SF(runnumber, run_first, run_last, year, titleLabel, fileName):

  #systs = [1001, 1002, 1003, 1004, 1005, 1006]
  systs = [1001, 1002, 1003, 1004, 1005, 1006, 1101,1102,1103,1104]
  #systs = [1101,1102,1103,1104,1105,1106,1107,1108]
  #systs = [1001, 1002, 1003, 1004, 1005, 1006, 1101,1102,1103,1104, 1105,1106,1107,1108]

  COLORS = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kMagenta, ROOT.kOrange, ROOT.kYellow, ROOT.kCyan, ROOT.kCyan+1]

  fs = []
    
  ROOT.gROOT.LoadMacro("../Data_metTrigEff.cxx")
  from ROOT import Data_metTrigEff
  ROOT.gROOT.LoadMacro("../MonteCarlo_metTrigEff.cxx")
  from ROOT import MonteCarlo_metTrigEff
  ROOT.gROOT.LoadMacro("../MC_metTrigEff.cxx")
  from ROOT import MC_metTrigEff
  f1 = ROOT.TF1("f1",Data_metTrigEff,xmin,xmax,2)
  f2 = ROOT.TF1("f2",MonteCarlo_metTrigEff,xmin,xmax,2)
  #f3 = ROOT.TF1("f3",MC_metTrigEff,xmin,xmax,2)
  fs.append(ROOT.TF1("f3",MC_metTrigEff,xmin,xmax,2))
  f1.SetParNames("var_index","run_number")
  f1.SetParameters(1000,runnumber)
  f2.SetParameters(1000,runnumber)
  fs[0].SetParameters(1000,runnumber)


  x = np.linspace(xmin, xmax, npoints+1)
  ymin_stat = []
  ymax_stat = []
  ymin_syst = []
  ymax_syst = []

  for syst in systs:
    fs.append(ROOT.TF1(fs[0]))
    fs[-1].SetParameters(syst,runnumber)
    fs[-1].SetLineColor(ROOT.kOrange)
    if syst > 1100:
      fs[-1].SetLineColor(ROOT.kOrange+4)
    fs[-1].SetLineStyle(ROOT.kDotted)
    fs[-1].Draw("Same")

  for ii, xx in enumerate(x):
    #ymax.append(max(fs[i].Eval(xx) for i in range(0, len(fs))))
    statplus = 0.0
    statminus = 0.0
    systplus = 0.0
    systminus = 0.0
    ynom = fs[0].Eval(xx+halfbin)
    #print(" xx = ",xx)
    
    #for i  in range(1, len(fs)):
    for i, syst in enumerate(systs):
      y = fs[i+1].Eval(xx+halfbin) - ynom
      if syst < 1100:
        if y>0:
          systplus += y*y
        else:
          systminus += y*y
      else:
        if y>0:
          statplus += y*y
        else:
          statminus += y*y
        
    
    ymax_stat.append(ynom+math.sqrt(statplus))
    ymin_stat.append(ynom-math.sqrt(statminus))
    ymax_syst.append(ynom+math.sqrt(systplus))
    ymin_syst.append(ynom-math.sqrt(systminus))

  ### Try writing out the mergged systematics )in form of lookup table:

  with open(outfilename, "a") as cfile:
                index = 1000

                cfile.write("\t // year: %s \n"%year)
                cfile.write("\t // trigger: %s \n"%titleLabel)
                cfile.write("\t if(run_number >= %i && run_number <= %i){\n"%(run_first, run_last))
                # cfile.write("\t //! variation: %s\n"%variation.name)

                cfile.write("\t\t if(variation_index==%i){\n"%(index))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(fs[0].Eval(xx+halfbin)))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )

                cfile.write("\t\t //! systematic variation UP\n")
                cfile.write("\t\t if(variation_index==%i){\n"%(index+1))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(ymax_syst[ii]))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )

                cfile.write("\t\t //! systematic variation DOWN\n")
                cfile.write("\t\t if(variation_index==%i){\n"%(index+2))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(ymin_syst[ii]))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )


                cfile.write("\t\t //! statistical variation UP\n")
                cfile.write("\t\t if(variation_index==%i){\n"%(index+101))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(ymax_stat[ii]))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )

                cfile.write("\t\t //! statistical variation DOWN\n")
                cfile.write("\t\t if(variation_index==%i){\n"%(index+102))
                cfile.write("\t\t\t float SF_temp[%i] = { \n"%(npoints+2))
                for ii, xx in enumerate(x):
                      cfile.write("%0.3f, "%(ymin_stat[ii]))
                cfile.write("%0.3f \n"%(1.0))
                cfile.write("\t\t\t  }; \n")
                cfile.write("\t\t\t return SF_temp[i]; \n")
                cfile.write("\t\t  }; \n")
                #cfile.write("\t\t  \n" )

                cfile.write("\t\t std::cout << \"MET triger SF ERROR:   Unrecognized variation index! \" << variation_index << std::endl; \n")
                cfile.write("\t\t return 1.0; \n")
                cfile.write("\t }; \n")
                cfile.write("\t  \n" )

      
  
##------------------------------------------------------------------------------------
## - - main driver
##------------------------------------------------------------------------------------
if __name__=="__main__":

    triggers=[
        {'run':280000, 'run_first':266904, 'run_last':284484,  'year':"2015",  'label':"2015_HLT_xe70_mht || xe70_tc_lcw", 'file':"2015_HLT_xe70_mht"},
        {'run':300000, 'run_first':296939, 'run_last':302872,  'year':"2016",  'label':"2016_HLT_xe90_mht || xe70_tc_lcw_L1XE50", 'file':"2016_HLT_xe90_mht"},
        {'run':305000, 'run_first':302873, 'run_last':311481,  'year':"2016",  'label':"2016_HLT_xe110_mht_L1XE50", 'file':"2016_HLT_xe110_mht_L1XE50"},
        {'run':327000, 'run_first':325713, 'run_last':331975,  'year':"2017",  'label':"2017_HLT_xe110_pufit_L1XE55", 'file':"2017_HLT_xe110_pufit_L1XE55"},
        {'run':333000, 'run_first':332303, 'run_last':341649,  'year':"2017",  'label':"2017_HLT_xe110_pufit_L1XE50", 'file':"2017_HLT_xe110_pufit_L1XE50"},
        {'run':350000, 'run_first':348885, 'run_last':364485,  'year':"2018",  'label':"2018_HLT_xe110_pufit_xe70_L1XE50", 'file':"2018_HLT_xe110_pufit_xe70_L1XE50"},
    ]
    
    with open(outfilename, "w") as cfile:
            cfile.write("//   CAREFUL!  This is a MonteCarlo Scale Factor data file!\n")
            cfile.write("//             Use together with MC trigger decision!\n")
            istring = "float metTrigEff(float met_et, int variation_index, int run_number){\n"
            cfile.write(istring)
            cfile.write("\t //! xmin: %4.1f \n"%( xmin ) )
            cfile.write("\t //! xmax: %4.1f \n"%( xmax ) )
            cfile.write("\t //! npoints: %i \n"%( npoints ) )
            cfile.write("\t int i = static_cast<int>(%i*(met_et - %4.1f)/(%4.1f - %4.1f)); \n"%(npoints, xmin, xmax, xmin))
            cfile.write("\t if ( i < 0 || i > %i ) i=100; \n"%(npoints))
            cfile.write("\n")
    
    for trigger in triggers:
       plot_SF(trigger['run'], trigger['run_first'], trigger['run_last'], trigger['year'], trigger['label'], trigger['file'])
    
    with open(outfilename, "a") as cfile:
            cfile.write("\t std::cout << \"MET triger SF ERROR:   Unrecognized run! \" << run_number << std::endl; \n")
            cfile.write("\t return 1.0; \n")

            cfile.write("} \n")

