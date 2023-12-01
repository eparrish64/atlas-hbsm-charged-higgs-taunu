#!/usr/bin/env python2

import ROOT

inputPath = "/cvmfs/atlas.cern.ch/repo/sw/database/GroupData/dev/SUSYTools/Vjets_SysParameterization/VJetsWeights.root"

f = ROOT.TFile.Open(inputPath, "READONLY")

zptBinNames = ["0to70", "70to140", "140to280", "280to500", "500to1000", "1000toECMS"]
zptBins = {
  "0to70": 1,
  "70to140": 2,
  "140to280": 3,
  "280to500": 4,
  "500to1000": 5,
  "1000toECMS": 7,
}

varNames = ["ckkw15", "ckkw30", "fac025", "fac4", "qsf025", "qsf4", "renorm025", "renorm4"]

print "// Generated by generate-wtaunu-macros.py, do not edit!\n\n"

for varName in varNames:
  h = f.Get("Wenu{}".format(varName))
  for zptBinName in zptBinNames:
    zptBin = zptBins[zptBinName]
    print "float wtaunu_{}_{}(int nTruthJets)".format(varName, zptBinName)
    print "{"
    print "    int jetBin = nTruthJets+1;"
    print "    if (jetBin > 12) jetBin = 12;"
    for nTruthJets in range(12):
      truthJetBin = nTruthJets+1 #goes 1-11, do 12 as a last step
      print "    if (jetBin == {}) return {};".format(truthJetBin, h.GetBinContent(zptBin, truthJetBin))
    print "    return 0; // This never happens"
    print "}\n"

