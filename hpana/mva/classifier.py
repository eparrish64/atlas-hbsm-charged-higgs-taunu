""" TMVA or Sklearn based Classifier to be trained in separating signals from backgrounds
"""
## stdl
import os, time, copy
from array import array 
from collections import OrderedDict
import multiprocessing

## PyPI
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from root_numpy import root2array, tree2array
import numpy as np
import pandas as pd
import pickle, cPickle
from sklearn import utils

## local 
from hpana import log 
from hpana.categories import CLASSIFIER_CATEGORIES, TAU_IS_TRUE, ANTI_TAU
from hpana.mva import NN_HYPERPARAMS

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
            
        ## instantiate Base 
        super(Classifier, self).__init__(factory_name, self.output, self.params)
        
        ## add input features to the TMVA.DataLoader
        for var in self.features:
            self.dataloader.AddVariable(var.tformula, var.title, 
                                        var.unit if hasattr(var, "unit") else "",)
            
        ## features dict in order to keep references for TMVA.Reader !
        self.features_dict = OrderedDict()
            
        ## retrieve trained model
        if weight_file:
            self.weight_file = weight_file
            ## instantiate Reader for model evaluation
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

        ## prepare bkg and sig tree
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
        ## update referenced features 
        for feat, val in features_dict.iteritems():
            self.features_dict[feat] = val
        return self.reader.EvaluateMVA(self.method_name)
        
##----------------------------------------------------------------------------------
## Base classifier class
##----------------------------------------------------------------------------------
class SClassifier(GradientBoostingClassifier):
    """
    """
    # try:
    # MODEL_NAME_STR_FORMAT = "model_{0}_channel_{1}_mass_{2}_ntracks_{3}_nfolds_{4}_fold_{5}_nvars_{6}_learnRate_{7}_minSampsLeaf_{8}_nEst_{9}_minSampsSplit_{10}_maxDepth_{11}.pkl" #<! name, channel, ntracks, nfolds, fold, n_vars
    # except:
    MODEL_NAME_STR_FORMAT = "model_{0}_channel_{1}_mass_{2}_ntracks_{3}_nfolds_{4}_fold_{5}_nvars_{6}.pkl"
    
    def __init__(self, channel, 
                    name="GB", 
                    mass_range=[], 
                    features=[], 
                    train_df=None, 
                    valid_df=None,
                    eval_df=None,
                    weight_sample=False,
                    is_trained=False,
                    kfolds=5,
                    fold_num=0,
                    ntracks=1,
                    optimize=False,
                    sigs=[],
                    bkgs=[],
                    **params):
        log.debug("Initializing SClassifier ...")
        self.kparams = params
        self.channel = channel
        self.name = name 
        self.features = features
        self.mass_range = mass_range
        self.train_df = train_df
        self.valid_df = valid_df
        self.eval_df = eval_df
        self.weight_sample = weight_sample
        self.kfolds = kfolds
        self.fold_num = fold_num
        self.ntracks = ntracks
        self.is_trained = is_trained
        self.hyperparams = params
        self.optimize = optimize
        self.sigs = sigs
        self.bkgs = bkgs

        if self.optimize:
            MODEL_NAME_STR_FORMAT = "model_{0}_channel_{1}_mass_{2}_ntracks_{3}_nfolds_{4}_fold_{5}_nvars_{6}_learnRate_{7}_minSampsLeaf_{8}_nEst_{9}_minSampsSplit_{10}_maxDepth_{11}.pkl" #<! name, channel, ntracks, nfolds, fold, n_vars
        else:
            MODEL_NAME_STR_FORMAT = "model_{0}_channel_{1}_mass_{2}_ntracks_{3}_nfolds_{4}_fold_{5}_nvars_{6}.pkl" #<! name, channel, ntracks, nfolds, fold, n_vars 

        ## instantiate the base
        super(SClassifier, self).__init__(**params)

    @staticmethod
    def prepare_data(backgrounds, signals, features,
                     branches=[],
                     category=None,
                     channel="taujet",
                     treename="NOMINAL",
                     train_data="CLF_DATA.pkl",
                     data_lumi=36200, 
                     overwrite=False,
                     truth_match_tau=True):
        """Training input as pandas DataFrame
        """
        ## first check if all the samples are already available in the training Dataframe
        missing_bkgs = []
        missing_sigs = []
        cached_dframe = None
        if os.path.isfile(train_data) and not overwrite:
            log.info("Reading training data from %s"%train_data)
            with open(train_data, "r") as cache:
                cached_dframe = cPickle.load(cache)
            for b in backgrounds:
                if not (b.name in cached_dframe.index):
                    log.warning("missing %s in %s Dataframe"%(b.name, train_data))
                    missing_bkgs += [b]
                    
            for s in signals:
                if not (s.name in cached_dframe.index):
                    log.warning("missing %s in %s Dataframe"%(s.name, train_data))
                    missing_sigs += [s]
            if not missing_sigs and not missing_bkgs:
                log.info("All requested samples are available in %s Dataframe"%train_data)
                return cached_dframe
        else:
            missing_bkgs = backgrounds
            missing_sigs = signals
            
        if category is None:
            category = CLASSIFIER_CATEGORIES[channel]
        cuts = category.cuts

        ## keep event number (is needed for kfold training)
        if not branches:
            branches = ["event_number"] + [ft.tformula for ft in features]

        ## feature name as column label
        columns = {}
        for feat in features:
            columns[feat.tformula] = feat.name

        ## backgrounds 
        bkg_dfs = []
        for bkg in missing_bkgs:
            log.info("Adding %s bkg ..."%bkg.name)
            bfiles = []
            ## treat QCD fakes properly 
            if "QCD" in bkg.name:

                ## @NOTE defensive copying to avoid clashing with cuts for other samples
                category_cp = copy.deepcopy(category)
                ## only FF weights are applicable here
                ws = bkg.ff_weights(categories=[category_cp])["NOMINAL"][category.name]   
                ws = "*".join(ws)
                
                ## add antitau cut 
                category_cp.tauid = ANTI_TAU
                category_cp.truth_tau = None #<! not applicable to DATA   
                cuts = category_cp.cuts 

                log.debug("Cut: %r\n"%cuts.GetTitle())
                log.debug("Weight: %r\n"%ws)

                ## pool of workers 
                pool = multiprocessing.Pool() 
                pool_res = []

                log.debug(
                    "**"*30 + " Parallel processing %i datasets(%r)  for %s "%(len(bkg.data.datasets), bkg.data.streams, bkg.name) + "**"*30)
                for ds in bkg.data.datasets:
                    ##@FIXME missing 2018 triggers in 2015-2017 v06 ntuples 
                    if "DATA2018" in ds.name:
                        d_streams = ["2018"]
                    else:
                        d_streams = ["2015", "2016", "2017"]

                    trigger = bkg.triggers(categories=[category_cp], data_streams=d_streams, dtype="DATA")[category_cp.name]
                    selection = (trigger + cuts).GetTitle()
                
                    bfiles = ds.files                        
                    if not bfiles:
                        log.warning("No root file is found for %s"%ds.name)
                        continue
                    if empty_tree(bfiles, treename=treename):
                        log.warning("%s tree is empty for %s dataset; skipping!"%(treename, ds.name))
                        continue

                    kargs = {"treename": treename, "branches": branches+[ws], "selection": selection, "warn_missing_tree": True}    
                    pool_res += [pool.apply_async(root2array, (bfiles,), dict(kargs))]

                ## close the pool and wait for the workers to finish
                pool.close()
                pool.join()

                ## retrive the pool output and create Dataframes 
                b_dfs = []
                for res in pool_res:
                    r_arr = res.get(3600)
                    p_df = pd.DataFrame(r_arr.flatten())
                    columns[ws] = "weight"
                    p_df = p_df.rename(columns=columns)
                    log.debug("Weight sum: %r\n"%np.sum(p_df["weight"]))
                    log.debug("#events: %r\n"%p_df.shape[0])
                    b_dfs += [p_df]

                bkg_df = pd.concat(b_dfs, ignore_index=True, sort=False)
                ## class label for bkg 
                bkg_df["class_label"] = pd.Series(np.zeros(bkg_df.size))
                bkg_dfs += [bkg_df]
                log.debug("--"*70)

            else:
                b_dfs = []
                pool = multiprocessing.Pool() 
                pool_res = []
                pool_ws = []

                ## add trigger
                trigger = bkg.triggers(categories=[category], data_streams=bkg.config.data_streams, dtype="MC")[category.name]
                for ds in bkg.datasets:
                    log.debug("**"*30 + ds.name + "**"*30)
                    bfiles = ds.files
                    if not bfiles:
                        log.warning("No root file is found for %s"%ds.name)
                        continue
                    if empty_tree(bfiles, treename=treename):
                        log.warning("%s tree is empty for %s dataset; skipping!"%(treename, ds.name))
                        continue
                    if truth_match_tau:
                        cuts = category.cuts + TAU_IS_TRUE 

                    ## common Scale Factors
                    ws = bkg.weights(categories=[category]).values()[0]
                    ws = "*".join(ws)

                    ## add luminosity weight
                    if ds.lumi_weight:
                        lumi_weight = bkg.data_lumi(ds.stream) * ds.lumi_weight
                    else: 
                        lumi_weight = (bkg.data_lumi(ds.stream) * ds.xsec_kfact_effic) / ds.events  
                    ws = ws + "*{}".format(lumi_weight)
                    pool_ws += [ws] #<! @NOTE each dataset has a different weight --> keep them to properly rename all to 'weight'
                    selection = (trigger + cuts).GetTitle()
                    log.debug("Cut: %r\n"%selection)
                    log.debug("Weight: %r\n"%ws)
                    kargs = {"treename": treename, "branches": branches+[ws], "selection": selection, "warn_missing_tree": True}
                    pool_res += [pool.apply_async(root2array, (bfiles,), dict(kargs))]

                ## close the pool and wait for the workers to finish
                pool.close()
                pool.join()

                ## retrive the pool output and create Dataframes 
                for bds, pw, res in zip(bkg.datasets, pool_ws, pool_res):
                    r_arr = res.get(3600)
                    p_df = pd.DataFrame(r_arr.flatten())
                    ## @NOTE the weight string changes due to LUMI factor from dataset to dataset --> rename it to avoid concatenation confusion 
                    columns[pw] = "weight"
                    p_df = p_df.rename(columns=columns)
                    log.debug("Weight sum: %r\n"%np.sum(p_df["weight"]))
                    log.debug("#events: %r\n"%p_df.shape[0])
                    b_dfs += [p_df]

                bkg_df = pd.concat(b_dfs, ignore_index=True, sort=False)
                ## class label for bkg 
                bkg_df["class_label"] = pd.Series(np.zeros(bkg_df.size))
                bkg_dfs += [bkg_df]
                log.debug("--"*70)

        ## signals 
        sig_dfs = []
        for sig in missing_sigs:
            log.info("Adding %s signal ..."%sig.name)
            ## add trigger
            trigger = bkg.triggers(categories=[category], data_streams=sig.config.data_streams, dtype="MC")[category.name]            
            cuts = category.cuts 
            if truth_match_tau:
                cuts = category.cuts + TAU_IS_TRUE
            
            s_dfs = []
            for ds in sig.datasets:
                log.debug("**"*30 + ds.name +"**"*30)
                sfiles = ds.files
                if not sfiles:
                    log.warning("No root file is found for %s"%sig.name)
                    continue
                
                ## common Scale Factors 
                ws = sig.weights(categories=[category]).values()[0]
                ws = "*".join(ws)

                ## add luminosity weight 
                if ds.lumi_weight:
                    lumi_weight = bkg.data_lumi(ds.stream) * ds.lumi_weight
                else: 
                    lumi_weight = (bkg.data_lumi(ds.stream) * ds.xsec_kfact_effic) / ds.events                        
                ws = ws + "*{}".format(lumi_weight)
                selection = cuts.GetTitle()
                log.debug("Cut: %r\n"%selection)
                log.debug("Weight: %r\n"%ws)

                ## convert ROOT to numpy array 
                s_arr = root2array(sfiles, treename=treename, branches=branches+[ws], selection=selection, warn_missing_tree=True)
                df = pd.DataFrame(s_arr.flatten())

                columns[ws] = "weight"
                df = df.rename(columns=columns)
                log.debug("Weight sum: %r\n"%np.sum(df["weight"]))
                log.debug("#events: %r\n"%df.shape[0])
                log.debug("--"*70)
                s_dfs += [df]

            s_df = pd.concat(s_dfs, ignore_index=True, sort=False)
            ## class label for bkg 
            s_df["class_label"] = pd.Series(np.ones(s_df.size))
            sig_dfs += [s_df]

        ## concat sig & bkg and index based on the sample name
        m_keys = [bkg.name for bkg in missing_bkgs] + [sig.name for sig in missing_sigs]
        new_dframe = pd.concat(bkg_dfs+sig_dfs, keys=m_keys, sort=False)

        if cached_dframe is not None:
            keys = [sb.name for sb in backgrounds+signals]
            dframe = pd.concat([new_dframe, cached_dframe], sort=False)
        else:
            dframe = new_dframe   

        if overwrite:
            log.warning("caching training data")
            os.system("rm %s"%train_data)
            
        with open(train_data, "a") as cache:
            cPickle.dump(dframe, cache, protocol=2)
            
        return dframe
    


##--------------------------------------------------------------------------
## util for parallel processing
##--------------------------------------------------------------------------
def train_model(model, 
    train_df=None,
    features=[], 
    positive_weights=True, 
    balanced=False,
    outdir="", 
    weight_sample=False, 
    scale_features=True, 
    save_model=True, 
    overwrite=False,
    is_NN=False):
    """ Train a classifier and produce some validation plots.
    Parameters
    ----------
    model: DecisionTree;
        sklearn classifier 
    train_df: pandas.DataFrame; 
        training dataframe  
    outdir: str;
        path to save the model and roc curve 
    weight_sample: bool;
        whether to use the sample weight or go with the sklearn's default balanced weight procedure for the classes. 
    save_model: bool;
        whether to save the trained model to disk or not

    Return
    ------
    trained model 
    """
    if weight_sample:
        balanced = False

    if train_df is None:
        tr_df = model.train_df
    else:
        tr_df = train_df
    if not features :
        features = model.features

    b_df = tr_df[tr_df["class_label"]==0]
    s_df = tr_df[tr_df["class_label"]==1]

    if is_NN == True:
        s_df["TruthMass"] = s_df.index.get_level_values(0)
        s_df["TruthMass"] = pd.to_numeric(s_df.TruthMass.replace({"Hplus": ""}, regex=True))
        b_df["TruthMass"] = np.random.choice( a=s_df["TruthMass"], size=b_df.shape[0] )
        train_masses = np.unique(s_df["TruthMass"].values)
        for i in train_masses:
            b_df["SampleWeight"] = float(s_df.loc[s_df["TruthMass"]==i].shape[0])/b_df.shape[0]
            b_df["TruthMass"] = i
            if (i==80): b_df_masses = b_df.copy()
            else: b_df_masses = pd.concat([b_df_masses, b_df])


    if balanced: 
        ## Set training weight of bkg events to 1. Signal events to N_bkg / N_sig.
        weight_sample = False  
        b_df["BDT_Weight"] = 1
        s_df["BDT_Weight"] = float(b_df.shape[0])/float(s_df.shape[0])
        # X_weight = tr_df_ud["BDT_Weight"]
        log.info("Balancing training classes via weights in classifier. Setting signal weights to %s" %(float(b_df.shape[0])/float(s_df.shape[0])))

    else:
        log.info("Unbalanced training classes; signal events:{} | bkg events: {}".format(s_df.shape[0], b_df.shape[0]))

    background_weight = float(s_df.shape[0])/b_df.shape[0]
    train_weights = {0: background_weight, 1: 1}

    if is_NN == True:
        tr_df_ud = pd.concat([b_df_masses, s_df], axis=0)
    else:
        tr_df_ud = pd.concat([b_df, s_df], axis=0)

    tr_df_ud = sklearn.utils.shuffle(tr_df_ud, random_state=123)


    ## - - training arrays
    X_train = tr_df_ud[[ft.name for ft in features]]    
    Y_train = tr_df_ud["class_label"]

    if weight_sample:
        log.info("Using event weight for training, events with negative weight are thrown away")        
        X_weight = tr_df_ud["weight"] 
        ## in order to avoid events with negative weight thrown away        
        if positive_weights: 
            log.info("using abs(weights)!")
            X_weight = np.absolute(X_weight.values)

    if scale_features:
        log.info("Scaling features using StandardScaler ...")
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train.values)

    mpath = os.path.join(outdir, model.name)
    is_trained = False 
    if os.path.isfile(mpath):
        log.info("Loading %s model from disk ..."%mpath)
        with open(mpath, "r") as cache:
            model = cPickle.load(cache)
            if is_NN == True:
                try:
                    Keras_model = cPickle.load(cache)
                except:
                    pass
            else:
                Keras_model = None
            is_trained =  model.is_trained
            if is_trained:
                log.warning("The %s model is already trained! set overwrite=True, if you want to overwrite it"%mpath)
                if overwrite:
                    os.remove(mpath)
                    is_trained = False                                    

    if not is_trained:
        ## train the model,
        try:
            if is_NN == True:
                Keras_model.fit(X_train.values, Y_train.values, batch_size=NN_HYPERPARAMS["batch_size"], epochs=NN_HYPERPARAMS["epochs"], class_weight=train_weights, verbose=1)
            else:
                model = model.fit(X_train.values, Y_train.values, sample_weight=X_weight if weight_sample else None)
        except:
            if is_NN == True:
                Keras_model.fit(X_train, Y_train.values, batch_size=NN_HYPERPARAMS["batch_size"], epochs=NN_HYPERPARAMS["epochs"], class_weight=train_weights, verbose=1)
            else:
                model = model.fit(X_train, Y_train.values, sample_weight=X_weight if weight_sample else None)

        model.is_trained = True
        if save_model:
            mpath = os.path.join(outdir, model.name)
            mpathh5 = mpath.replace("pkl", "h5")
            with open(mpath, "w") as cache:
                cPickle.dump(model, cache, protocol=2)
                if is_NN == True:
                    cPickle.dump(Keras_model, cache, protocol=2)
                    Keras_model.save(mpathh5)
    
    log.info("Trained %s model"%(model.name))
    return model


##--------------------------------------------------------------------------
## 
##--------------------------------------------------------------------------
def empty_tree(files, treename="NOMINAL"):
    """ given a list of ROOT files see if at least one of them has treename 
    """
    evts = 0
    log.debug(files)
    for fl in files:
        log.debug(fl)
        if not os.path.isfile(fl):
            raise Exception("%s does not exist" %(fl))
        tf = ROOT.TFile(fl, "READ")
        log.debug("line 584")
        if not tf.GetListOfKeys().Contains(treename):
            raise Exception("%s does not contain %s tree"%(fl,treename))
        if tf.IsZombie():
            raise Exception("%s is a Zombie." %(fl))
        log.debug("line 587")
        tr = tf.Get(treename)
        log.debug("line 589")
        if tr:
            evts += tr.GetEntries()
        log.debug("**"*100)
        tf.Close()
    return evts==0


