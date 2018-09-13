"""

"""
## stdl
import os
from array import array 
from collections import OrderedDict
import threading

## PyPI
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
    
from root_numpy import root2array, tree2array
import numpy as np
import pandas as pd
import pickle, cPickle

## local 
from . import log 
from categories import CLASSIFIER_CATEGORIES, TAU_IS_TRUE

## ROOT 
import ROOT
from ROOT import TMVA

##----------------------------------------------------------------------------------
## Base classifier class
##----------------------------------------------------------------------------------
class Classifier(TMVA.Factory):
    def __init__(self,
                 method_type=TMVA.Types.kBDT,
                 method_name="BDT",
                 weight_file=None, 
                 features=[],
                 output="TMVA.root",
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
        self.method_type = method_type
        self.method_name = method_name
            
        ## - - instantiate Base 
        super(Classifier, self).__init__(factory_name, self.output, self.params)
        
        ## - - add input features to the TMVA.DataLoader
        for var in self.features:
            self.dataloader.AddVariable(var.tformula, var.title, 
                                        var.unit if hasattr(var, "unit") else "",)
            
        ## - - features dict in order to keep references for TMVA.Reader !
        self.features_dict = OrderedDict()
            
        ## - - retrieve trained model
        if weight_file:
            self.weight_file = weight_file
            ## - - instantiate Reader for model evaluation
            self.reader = TMVA.Reader()

            for feat in self.features:
                self.features_dict[feat.tformula] = array('f', [-1.])
                self.reader.AddVariable(feat.tformula, self.features_dict[feat.tformula]) #<! PASS REFRENCES HERE 
                
            self.reader.BookMVA(self.method_name, self.weight_file)

        
    def book(self, params):
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
        
        self.BookMethod(self.dataloader, self.method_type, self.method_name, pstring)
        
    def train(self, backgrounds, signals,
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
    
        self.book(method_params)
        self.dataloader.PrepareTrainingAndTestTree(
            sig_cuts, bkg_cuts,'SplitMode=Random:NormMode=NumEvents:!V')
        self.TrainAllMethods()
        self.EvaluateAllMethods()
        
    def predict(self, features_dict):
        """
        """
        assert os.path.isfile(self.weight_file), "weight file is not provided"
        ## - - update referenced features 
        for feat, val in features_dict.iteritems():
            self.features_dict[feat] = val
        return self.reader.EvaluateMVA(self.method_name)
        
##----------------------------------------------------------------------------------
## Base classifier class
##----------------------------------------------------------------------------------
class SClassifier(GradientBoostingClassifier):
    """

    """
    MODEL_NAME_STR_FORMAT = "model_{0}_channel_{1}_mass_{2}_ntracks_{3}_nfolds_{4}_fold_{5}_nvars_{6}.pkl" #<! name, channel, ntracks, nfolds, fold, n_vars 
    
    def __init__(self, channel, name="GB",**params):
        self.params = params
        self.channel = channel
        self.name = name 
        super(SClassifier, self).__init__(**params)

    @staticmethod
    def prepare_data(backgrounds, signals, features,
                     branches=[],
                     category=None,
                     channel="taujet",
                     treename="NOMINAL",
                     train_data="CLF_DATA.pkl",
                     overwrite=False,
                     truth_match_tau=True):
        """Training input as pandas DataFrame
        """

        ## - - first check if all the samples are already available in the training Dataframe
        missing_bkgs = []
        missing_sigs = []
        if os.path.isfile(train_data) and not overwrite:
            log.info("Reading training data from %s"%train_data)
            with open(train_data, "r") as cache:
                dframe = cPickle.load(cache)
            for b in backgrounds:
                if not (b.name in dframe.index):
                    log.warning("missing %s in %s Dataframe"%(b.name, train_data))
                    missing_bkgs += [b]
                    
            for s in signals:
                if not (s.name in dframe.index):
                    log.warning("missing %s in %s Dataframe"%(s.name, train_data))
                    missing_sigs += [s]
            if not missing_sigs and not missing_bkgs:
                log.info("All requested samples are available in %s Dataframe"%train_data)
                return dframe
        else:
            missing_bkgs = backgrounds
            missing_sigs = signals
            
        if not category:
            category = CLASSIFIER_CATEGORIES[channel]
        cuts = category.cuts

        ## - - keep event number (is needed for kfold training)
        if not branches:
            branches = ["event_number"] + [ft.tformula for ft in features]

        ## - - feature name as column label
        columns = {}
        for feat in features:
            columns[feat.tformula] = feat.name

        bkg_dfs = []
        for bkg in missing_bkgs:
            log.info("Adding %s bkg"%bkg.name)
            bfiles = []

            ## - - treat QCD fakes properly 
            if "QCD" in bkg.name:
                ## - - only FF weights are applicable here
                ws = bkg.ff_weights(categories=[category]).values()[0]
                ws = "*".join(ws)
                for ds in bkg.data.datasets:
                    bfiles += ds.files
                ## - - add antitau cut    
                cuts = category.cuts * ROOT.TCut("tau_0_jet_bdt_score_trans > 0.02 && tau_0_jet_bdt_loose==0")
            else:
                ws = bkg.weights(categories=[category]).values()[0]
                ws = "*".join(ws)
                for ds in bkg.datasets:
                    bfiles += ds.files
                if truth_match_tau:
                    cuts = category.cuts * TAU_IS_TRUE 
             
            ## - - keep total event weight too
            log.debug(ws)
            b_arr = root2array(bfiles, treename=treename, branches=branches+[ws], selection=cuts.GetTitle())
            df = pd.DataFrame(b_arr.flatten())

            ## - - rename columns 
            columns[ws] = "weight"
            bkg_df = df.rename(columns=columns)

            ## - - class label for bkg 
            bkg_df["class_label"] = pd.Series(np.zeros(bkg_df.size))
            bkg_dfs += [bkg_df]

        sig_dfs = []
        for sig in missing_sigs:
            log.info("Adding %s signal"%sig.name)
            ws = sig.weights(categories=[category]).values()[0]
            ws = "*".join(ws)
            log.debug(ws)
            
            if truth_match_tau:
                cuts = category.cuts * TAU_IS_TRUE
            
            ## - - keep total event weight too
            sfiles = []
            for ds in sig.datasets:
                sfiles += ds.files
            s_arr = root2array(sfiles, treename=treename, branches=branches+[ws], selection=cuts.GetTitle())
            df = pd.DataFrame(s_arr.flatten())
            columns[ws] = "weight"
            sig_df = df.rename(columns=columns)
            
            ## - - class label for sig
            sig_df["class_label"] = pd.Series(np.ones(sig_df.size))
            sig_dfs += [sig_df]
        
        ## - - index based on the sample name
        keys = [bkg.name for bkg in missing_bkgs] + [sig.name for sig in missing_sigs]
        dframe = pd.concat(bkg_dfs+sig_dfs, keys=keys)
            
        if overwrite:
            log.warning("caching training data")
            os.system("rm %s"%train_data)
            
        with open(train_data, "a") as cache:
            cPickle.dump(dframe, cache, protocol=2)
            
        return dframe
    


    
##--------------------------------------------------------------------------
## util for parallel processing
##--------------------------------------------------------------------------
def train_model(model, X_train, Y_train, X_weight,
                outdir="", weight_sample=False, save_model=True, validation_plots=False):
    """
    """
    if validation_plots:
        test_size = 0.2
    else:
        test_size = 0.0
    X_train, X_test, Y_train, Y_test, X_weight_tr, X_weight_ts = train_test_split(X_train, Y_train, X_weight, test_size=test_size)
    mpath = os.path.join(outdir, model.name)
    
    if os.path.isfile(mpath):
        log.info("found already trained model %s"%mpath)
        with open(mpath, "r") as cache:
            model = cPickle.load(cache)
    else:
        ## - - train the model,
        ## - - please note that signals might have negetive weights and therefore will be thrown away for training!
        model = model.fit(X_train, Y_train, sample_weight=X_weight_tr if weight_sample else None)
        if save_model:
            mpath = os.path.join(outdir, model.name)
            with open(mpath, "w") as cache:
                cPickle.dump(model, cache, protocol=2)
    
    if validation_plots:
        Y_score = model.predict_proba(X_test)[:, 1]
        fpr_grd, tpr_grd, _ = roc_curve(Y_test, Y_score)
        auc = roc_auc_score(Y_test, Y_score)
        
        ## plot roc 
        plt.figure(1)
        plt.plot([0, 1], [0, 1], 'k--')
        plt.plot(fpr_grd, tpr_grd, label="AUC = %.4f"%auc)
        plt.ylabel('Signal efficiency (sensitivity)')
        plt.xlabel('Background rejection (specificity)')
        plt.title('ROC curve')
        plt.legend(loc='best')
        plt.savefig(os.path.join(outdir, model.name.replace(".pkl", ".png") ) )

    log.info("Trained %s model"%(model.name))
    return model

    
