import ROOT
import numpy as np
import math


def plot_SF(runnumber, titleLabel, fileName):

  #systs = [1001, 1002, 1003, 1004, 1005, 1006]
  systs = [1001, 1002, 1003, 1004, 1005, 1006, 1101,1102,1103,1104]
  #systs = [1101,1102,1103,1104,1105,1106,1107,1108]


  COLORS = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kMagenta, ROOT.kOrange, ROOT.kYellow, ROOT.kCyan, ROOT.kCyan+1]
  xmin = 50
  xmax = 250
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
  f1.SetLineColor(ROOT.kRed+1)
  f2.SetLineColor(ROOT.kGreen+1)
  fs[0].SetLineColor(ROOT.kBlue)
  Effi = ROOT.TCanvas("Effi","Effi",500,400)
  Effi.cd()
  f1.GetYaxis().SetRangeUser(0.0,1.2);
  f1.Draw()
  f2.Draw("Same")
  #fs[0].Draw("Same")
  f1.GetXaxis().SetTitle("E^{mis}_{T}   [GeV]")
  f1.GetYaxis().SetTitle("Trigger efficiency / SF")
  f1.SetTitle(titleLabel)


  npoints = 100
  gr = ROOT.TGraph()
  gr.SetFillColor(ROOT.kYellow);
  gr.SetFillColorAlpha(ROOT.kYellow, 0.45)
  gr.SetFillStyle(1001);
  x = np.linspace(xmin, xmax, npoints)
  ymin = []
  ymax = []

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
    ynom = fs[0].Eval(xx)
    
    #for i  in range(1, len(fs)):
    for i, syst in enumerate(systs):
      y = fs[i+1].Eval(xx) - ynom
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
        
    
    ymax.append(ynom+math.sqrt(statplus+systplus))
    ymin.append(ynom-math.sqrt(statminus+systminus))
    gr.SetPoint(ii,xx,ymax[-1])

  for ii, xx in enumerate(reversed(x)):
    #ymin.append(min(fs[i].Eval(xx) for i in range(0, len(fs))))
    #gr.SetPoint(npoints+ii,xx,ymin[-1])
    gr.SetPoint(npoints+ii,xx,ymin[npoints-1-ii])

  #draw graph with fill area option
  gr.Draw("fSame")
  fs[0].Draw("Same")

  #draw the horizontal line
  lh = ROOT.TLine(xmin,1.0,xmax,1.0)
  lh.SetLineColor(ROOT.kBlack)
  lh.SetLineWidth(1)
  lh.SetLineStyle(ROOT.kDotted)
  lh.Draw("Same")

  #draw delimiter line and an arrow:
  l = ROOT.TLine(150.0,0.0,150.0,1.2)
  l.SetLineColor(ROOT.kBlack)
  l.SetLineWidth(2)
  l.SetLineStyle(ROOT.kDashed)
  l.Draw("Same")
  a = ROOT.TArrow(150.0,0.6,180.0,0.6,0.03,"|>")
  a.SetLineWidth(2)
  a.Draw()

  #add a legend:
  legend = ROOT.TLegend(0.6,0.15,0.85,0.35)
  #legend.SetHeader("The Legend","C") # option "C" allows to center the header
  legend.AddEntry(f1,"erf fit to Data","l")
  #legend.AddEntry(f1,"erf fit to Data","lep")
  legend.AddEntry(f2,"erf fit to MC","l")
  legend.AddEntry(fs[0],"Scale Factor","l")
  legend.AddEntry(gr,"Systematics","f")
  legend.Draw()

   
  formats=[".png",".pdf", ".eps"]
  outname = "%s/MET_trig_SF_%s"%(".", fileName)
  #log.info("Saving %s"%outname_den)
  for fmt in formats:
      Effi.Print(outname+fmt)

  
##------------------------------------------------------------------------------------
## - - main driver
##------------------------------------------------------------------------------------
if __name__=="__main__":

    triggers=[
        {'run':280000, 'label':"2015_HLT_xe70_mht || xe70_tc_lcw", 'file':"2015_HLT_xe70_mht"},
        {'run':300000, 'label':"2016_HLT_xe90_mht || xe70_tc_lcw_L1XE50", 'file':"2016_HLT_xe90_mht"},
        {'run':305000, 'label':"2016_HLT_xe110_mht_L1XE50", 'file':"2016_HLT_xe110_mht_L1XE50"},
        {'run':327000, 'label':"2017_HLT_xe110_pufit_L1XE55", 'file':"2017_HLT_xe110_pufit_L1XE55"},
        {'run':333000, 'label':"2017_HLT_xe110_pufit_L1XE50", 'file':"2017_HLT_xe110_pufit_L1XE50"},
        {'run':350000, 'label':"2018_HLT_xe110_pufit_xe70_L1XE50", 'file':"2018_HLT_xe110_pufit_xe70_L1XE50"},
    ]
    

    for trigger in triggers:
       plot_SF(trigger['run'], trigger['label'], trigger['file'])
    

