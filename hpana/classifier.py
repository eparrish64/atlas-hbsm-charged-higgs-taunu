"""

"""
import ROOT
from ROOT import TMVA

##----------------------------------------------------------------------------------
## Base classifier class
##----------------------------------------------------------------------------------

class Classifier(TMVA.Factory):
    def __init__(self,
                 output="TMVA.root",
                 features=[],
                 channel="taujet",
                 outdir="./",
                 factory_name="TMVAClassification",
                 params="V:!Silent:Color:DrawProgressBar:Transformations=D,G:AnalysisType=Classification",):
        self.output = ROOT.TFile("%s/%s"%(outdir, output), "RECREATE")
        self.features = features
        self.factory_name = factory_name
        self.channel = channel
        self.outdir = outdir
        self.params = params
        self.dataloader = TMVA.DataLoader(self.outdir)

        ## - - add features 
        for var in self.features:
            self.dataloader.AddVariable(
                var.tformula, 
                var.title, 
                var.unit if hasattr(var, "unit") else "",)
        super(Classifier, self).__init__(factory_name, self.output, self.params)
            
    def book(self, method_type, method_name, params):
        """
        Book the Classifier method (set all the parameters)
        """
        pstring = ""
        if isinstance(params, dict):
            plist = []
            for p, val in params.iteritems():
                plist.append("%s=%s"%(p, val))
                pstring = ":".join(plist)
        elif isinstance(params, (list, tuple)):
            pstring = ":".join(params)

        elif isinstance(params, str):
            pstring = params
        else:
            raise TypeError("unsupported type, {}".format(params))
        
        self.BookMethod(self.dataloader, method_type, method_name, pstring)
        
    def train(self, backgrounds, signals,
              method_type=TMVA.Types.kBDT,
              method_name="BDT",
              method_params={},
              signal_masses=[],
              fold_cut=None,
              selections=ROOT.TCut(""),
              bkg_weights=None,
              sig_weights=None,
              treename="NOMINAL"):
        """
        
        """
        if signal_masses:
            signals = filter(lambda s: s.mass in signal_masses, signals)

        ## - - prepare bkg and sig tree
        bkg_tchain = ROOT.TChain(treename)
        bkg_files = []
        for bkg in backgrounds:
            for ds in bkg.datasets:
                for ifile in ds.files:
                    bkg_tchain.Add(ifile)
                    
        sig_tchain = ROOT.TChain(treename)
        for sig in signals:
            for ds in sig.datasets:
                for ifile in ds.files:
                    sig_tchain.Add(ifile)


        if not isinstance(selections, ROOT.TCut):
            selections = ROOT.TCut(selections)
            
        bkg_cuts = selections
        sig_cuts = selections
        if bkg_weights:
            bkg_cuts *= bkg_weights
        if sig_weights:
            sig_cuts *= sig_weights
        if fold_cut:
            bkg_cuts *= fold_cut
            sig_cuts *= fold_cut
            
        self.dataloader.AddSignalTree(sig_tchain, 1.0)
        self.dataloader.AddBackgroundTree(bkg_tchain, 1.0)
    
        self.book(method_type, method_name, method_params)
        self.dataloader.PrepareTrainingAndTestTree(
            sig_cuts, bkg_cuts,'SplitMode=Random:NormMode=NumEvents:!V')
        self.TrainAllMethods()
            
        
