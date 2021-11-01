""" Functionalities for evaluating a trained model. 
"""

## stdlib
import multiprocessing, os, re, shutil, array, time, logging
from multiprocessing import Process
from collections import OrderedDict
from os import environ
from math import ceil

## PyPI
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import cPickle
import csv
import pandas as pd

## local
from hpana.samples.fakes import QCD
from hpana import log 
from hpana.mva import plt, XML_FILE_PATTERN, PKL_FILE_PATTERN 

## ROOT
import ROOT 


##-------------------------------------------------------------------
## simple class for appending clf scores to TTrees
##-------------------------------------------------------------------
class AppendJob(Process):
    """
    simpel worker class for parallel
    processing. the run method is necessary,
    which will overload the run method of Procces.
    """
    def __init__(self, file_name, models, copy_file=False, outdir=None):
        super(AppendJob, self).__init__()
        self.file_name = file_name
        job_name = file_name
        if '/' in job_name:
            job_name = job_name.split('/')[-1]
        self.job_name = job_name.replace('.root','') 
        self.models = models
        self.copy_file = copy_file
        self.outdir = outdir
        
    def run(self):
        # copy to new file
        if self.copy_file:
            output = self.file_name + '.nn'
            if os.path.exists(output):
                log.warning(" {} already exists (will skip copying if file is in good shape)" .format(output))
                tf = ROOT.TFile.Open(output, 'READ')
                if not tf:
                    log.warning("{} exists but it's ZOMBIE, replacing it".format(output))
                    os.remove(output)
                    shutil.copy(self.file_name, output)
            else:
                if self.outdir:
                    reldir = self.file_name.split("/")[-2]
                    fname = self.file_name.split("/")[-1]
                    opath = os.path.join(self.outdir, reldir)
                    os.system("mkdir -p %s"%opath)
                    output = os.path.join(opath, fname)
                    
                log.info("copying {0} to {1} ...".format(self.file_name, output))
                shutil.copy(self.file_name, output)
        else:
            output = self.file_name
        
        # the actual calculation happens here
        evaluate_scores_on_trees(output, self.models)

        return 

def calculate_scores(model, 
        dframe=None, 
        backgrounds=[], 
        sig=None, 
        fold_var="event_number", 
        n_tracks_var="tau_0_n_charged_tracks",
        train_score=True,
        outdir="", 
        outname=None,
        inclusive_trks=False,
        isNN=False):
    """
    For single model. Will return roc_auc_score for given model.
    Currently only takes one signal point                           Sept 6, 2019
    """

    if not dframe:
        dframe = model.eval_df
    
    b_dframe = dframe.loc[[bkg.name for bkg in backgrounds]]
    s_dframe = dframe.loc[[sig.name]]
    log.debug(30*"*" + " Testing Data Frame " + 30*"*")
    log.debug(dframe)
   
    masses = model.mass_range
    if not (masses[0] <= sig.mass <= masses[-1]):
        return None

    feats = model.features

    b_test = b_dframe[[ft.name for ft in feats ]]
    s_test = s_dframe[[ft.name for ft in feats ]]

    ## evaluate score 
    if isNN == True:
        # import tensorflow as tf
        # import keras
        # from keras.models import Sequential
        # from keras.layers import Dense, Activation, BatchNormalization, Dropout, LeakyReLU
        # from keras.regularizers import l2
        # from keras import initializers
        # from keras.optimizers import SGD
        # from keras.wrappers.scikit_learn import KerasClassifier
        # from keras.models import load_model
        # from keras import backend as K
        # from keras.layers import LeakyReLU  
        # from tensorflow.python.client import device_lib
        
        b_score = model.predict(b_test)
        s_score = model.predict(s_test)
    else:
        b_score = model.predict_proba(b_test)[:, 1]
        s_score = model.predict_proba(s_test)[:, 1]


    b_arr = np.concatenate([b_score])
    s_arr = np.concatenate([s_score])

    Y_score = np.concatenate([b_arr, s_arr])
    b_true = np.zeros(b_arr.size)
    s_true = np.ones(s_arr.size)
    Y_true = np.concatenate([b_true, s_true])
    auc = roc_auc_score(Y_true, Y_score)

    # with open(r'%s%s_auc.csv'%(outdir,model.name.replace(".pkl", "")), 'a') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(("b_scores","s_scores","auc"))
    #     writer.writerow((b_score,s_score,auc))
    return auc


##--------------------------------------------------------------------------
## plot predicted signal and background scores 
##--------------------------------------------------------------------------
def plot_scores(models,
        Keras_models=None,
        dframe=None, 
        backgrounds=[], 
        signals=[], 
        fold_var="event_number", 
        n_tracks_var="tau_0_n_charged_tracks",
        train_score=True,
        outdir="", 
        bins=None, 
        plot_roc=True, 
        overlay_rocs=False, 
        label=None, 
        outname=None,
        formats=[".png"],
        inclusive_trks=False,
        isNN=False):

    """
    """

    b_dframe = dframe.loc[[bkg.name for bkg in backgrounds]]
    s_dframe = dframe.loc[[sig.name for sig in signals]]
    log.debug(30*"*" + " Testing Data Frame " + 30*"*")
    log.debug(dframe)

    if isNN == True:
        scaler = StandardScaler()
        # import tensorflow as tf
        # import keras
        # from keras.models import Sequential
        # from keras.layers import Dense, Activation, BatchNormalization, Dropout, LeakyReLU
        # from keras.regularizers import l2
        # from keras import initializers
        # from keras.optimizers import SGD
        # from keras.wrappers.scikit_learn import KerasClassifier
        # from keras.models import load_model
        # from keras import backend as K
        # from keras.layers import LeakyReLU  
        # from tensorflow.python.client import device_lib
    rocs = []
    for sig in signals:
        sm_df = dframe.loc[[sig.name]]
        if isNN == True:
            b_dframe['TruthMass'] = sig.mass
        s_train_scores = []
        b_train_scores = []
        s_scores = []        
        b_scores = []        

        if isNN == True: ## NN Usage
            for m_model, m_Keras_model in zip(models, Keras_models):
                masses = m_model.mass_range
                if not (masses[0] <= sig.mass <= masses[-1]):
                    continue

                feats = m_model.features
                ## evaluate on the training samples
                if train_score:
                    if inclusive_trks:
                        b_train_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds!=m_model.fold_num)]
                        s_train_df = sm_df[(sm_df[fold_var]%m_model.kfolds!=m_model.fold_num)]
                    else:
                        b_train_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds!=m_model.fold_num) & (b_dframe[n_tracks_var]==m_model.ntracks)]
                        s_train_df = sm_df[(sm_df[fold_var]%m_model.kfolds!=m_model.fold_num) & (sm_df[n_tracks_var]==m_model.ntracks)]

                    b_train = b_train_df[[ft.name for ft in feats ]]
                    s_train = s_train_df[[ft.name for ft in feats ]]

                    b_tr_score = m_Keras_model.predict(b_train)
                    b_train_scores += [b_tr_score]
                    s_tr_score = m_Keras_model.predict(s_train)
                    s_train_scores += [s_tr_score]

                ## evaluate on unseen samples
                if inclusive_trks:
                    b_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds==m_model.fold_num)]
                    s_df = sm_df[(sm_df[fold_var]%m_model.kfolds==m_model.fold_num)]
                else:
                    b_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds==m_model.fold_num) & (b_dframe[n_tracks_var]==m_model.ntracks)]
                    s_df = sm_df[(sm_df[fold_var]%m_model.kfolds==m_model.fold_num) & (sm_df[n_tracks_var]==m_model.ntracks)]

                b_test = b_df[[ft.name for ft in feats ]]
                s_test = s_df[[ft.name for ft in feats ]]

                b_score = m_Keras_model.predict(b_test)
                b_scores += [b_score]
                s_score = m_Keras_model.predict(s_test)
                s_scores += [s_score]

        else: ## BDT Usage
            for m_model in models:
                masses = m_model.mass_range
                if not (masses[0] <= sig.mass <= masses[-1]):
                    continue

                feats = m_model.features
                ## evaluate on the training samples
                if train_score:
                    if inclusive_trks:
                        b_train_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds!=m_model.fold_num)]
                        s_train_df = sm_df[(sm_df[fold_var]%m_model.kfolds!=m_model.fold_num)]
                    else:
                        b_train_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds!=m_model.fold_num) & (b_dframe[n_tracks_var]==m_model.ntracks)]
                        s_train_df = sm_df[(sm_df[fold_var]%m_model.kfolds!=m_model.fold_num) & (sm_df[n_tracks_var]==m_model.ntracks)]

                    b_train = b_train_df[[ft.name for ft in feats ]]
                    s_train = s_train_df[[ft.name for ft in feats ]]

                    b_tr_score = m_model.predict_proba(b_train)[:, 1]
                    b_train_scores += [b_tr_score]
                    s_tr_score = m_model.predict_proba(s_train)[:, 1]
                    s_train_scores += [s_tr_score]

                ## evaluate on unseen samples
                if inclusive_trks:
                    b_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds==m_model.fold_num)]
                    s_df = sm_df[(sm_df[fold_var]%m_model.kfolds==m_model.fold_num)]
                else:
                    b_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds==m_model.fold_num) & (b_dframe[n_tracks_var]==m_model.ntracks)]
                    s_df = sm_df[(sm_df[fold_var]%m_model.kfolds==m_model.fold_num) & (sm_df[n_tracks_var]==m_model.ntracks)]

                b_test = b_df[[ft.name for ft in feats ]]
                s_test = s_df[[ft.name for ft in feats ]]

                ## evaluate score 
                b_score = m_model.predict_proba(b_test)[:, 1]
                b_scores += [b_score]
                s_score = m_model.predict_proba(s_test)[:, 1]
                s_scores += [s_score]



        if len(s_scores) < 1:
            continue
            
        b_arr = np.concatenate(b_scores)
        s_arr = np.concatenate(s_scores)

        if train_score:
            b_train_arr = np.concatenate(b_train_scores)
            s_train_arr = np.concatenate(s_train_scores)

        log.info("Evaluated mass %i, ntrack=%i, bkg events=%i, and sig events=%i"%(
                sig.mass, m_model.ntracks, b_arr.shape[0], s_arr.shape[0]))
        if bins is None:
            bins = np.linspace(0, 1, 50)

        arrs = [s_arr, b_arr]
        color = ['r', 'b']
        label = [r'$H^+$[%iGeV]'%sig.mass, r"$\sum BKG$"]
        if train_score:
            arrs += [s_train_arr, b_train_arr]
            color += ['purple', 'black']
            label += [r'train-$H^+$[%iGeV]'%sig.mass, r"train-$\sum BKG$"]

        ## plot hists
        plt.figure(10)
        plt.hist(arrs, bins, log=False, density=True, color=color, alpha=0.85, histtype="step", label=label) 
        plt.ylabel(r'$p.d.f$')
        if isNN == True:
            plt.xlabel('NN score')
        else:
            plt.xlabel('BDT score')
        plt.legend(loc='lower center')

        # bottom, top = plt.ylim()
        # plt.ylim(top=5*top)

        ## save plot
        if isNN == True:
            outname = os.path.join(outdir, "NN_score_{}_{}".format(sig.name, m_model.name.replace(".pkl", "")))
        else:
            outname = os.path.join(outdir, "BDT_score_{}_{}".format(sig.name, m_model.name.replace(".pkl", "")))
        for fmt in formats:
            plt.savefig(outname+fmt)
        plt.close()

        if plot_roc:
            Y_score = np.concatenate([b_arr, s_arr])
            b_true = np.zeros(b_arr.size)
            s_true = np.ones(s_arr.size)
            Y_true = np.concatenate([b_true, s_true])

            fpr_grd, tpr_grd, _ = roc_curve(Y_true, Y_score)
            auc = roc_auc_score(Y_true, Y_score)            
            rocs += [(m_model, fpr_grd, tpr_grd, auc)]

            if train_score:
                Y_train_score = np.concatenate([b_train_arr, s_train_arr])
                b_train_true = np.zeros(b_train_arr.size) #<! bkg 0
                s_train_true = np.ones(s_train_arr.size) #<! sig 1
                Y_train_true = np.concatenate([b_train_true, s_train_true])

                fpr_train_grd, tpr_train_grd, _ = roc_curve(Y_train_true, Y_train_score)
                auc_train = roc_auc_score(Y_train_true, Y_train_score)            
        
            ## plot roc 
            plt.figure(1)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.plot(fpr_grd, tpr_grd, label="AUC = %.4f"%auc)
            if train_score:
                plt.plot(fpr_train_grd, tpr_train_grd, label="train-AUC = %.4f"%auc_train, color="r")

            plt.ylabel('Signal efficiency ')
            plt.xlabel('Background rejection ')
            plt.title(r'ROC curve($H^+$[%iGeV])'%sig.mass)
            plt.legend(loc='best')

            outname = os.path.join(outdir, "ROC_{}_{}".format(sig.name, m_model.name.replace(".pkl", "")))
            for fmt in formats:
                plt.savefig(outname+fmt)
            plt.close()

    if overlay_rocs:
        fig = plt.figure(10)
        ax = plt.subplot(111)
        ax.plot([0, 1], [0, 1], 'k--')
        for roc in rocs:
            rmodel, fpr_grd, tpr_grd, auc = roc
            label = "{}_nvars_{}(AUC={:.4f})".format("_".join(rmodel.name.split("_")[1:6]), len(rmodel.features), auc)
            ax.plot(fpr_grd-1, tpr_grd, label=label)
            plt.ylabel('Signal efficiency ')
            plt.xlabel('Background rejection ')
            plt.title(r'ROC curve)')
        plt.legend(loc="best", fontsize="small")

        outname = os.path.join(outdir, "ROC_inclusive.png")
        plt.savefig(outname)
        plt.close()

    return 


##-----------------------------------------------
##
##-----------------------------------------------
def get_models(model_files, backend="sklearn", isNN=False):
    """
    retrive all trained models from the given path.
    Parameters
    ----------
    models_path: str, path to trained models

    Return
    models: dict, holding all trained models for different masses and folds.
    """
    ## - - loop over trained models and setup weight readers 
    models = dict()
    if isNN == True:
        # import tensorflow as tf
        # import keras
        # from keras.models import Sequential
        # from keras.layers import Dense, Activation, BatchNormalization, Dropout, LeakyReLU
        # from keras.regularizers import l2
        # from keras import initializers
        # from keras.optimizers import SGD
        # from keras.wrappers.scikit_learn import KerasClassifier
        from keras.models import load_model
        # from keras import backend as K
        # from keras.layers import LeakyReLU  
        # from tensorflow.python.client import device_lib
        Keras_models = dict()
    for model_file in model_files:
        base, wname = os.path.split(model_file)
        if backend=="tmva":
            match = re.match(XML_FILE_PATTERN, wname)
        else:
            match = re.match(PKL_FILE_PATTERN, wname)
        if not match:
            log.warning(' %s not matched'%wname)

            continue

        log.info("Loading %s"%wname)

        name = match.group("name")
        mass = match.group("mass")
        fold = int(match.group("fold"))
        ntracks = int(match.group("ntracks"))
        
        if not mass in models: 
            models[mass] = []
            if isNN == True:
                Keras_models[mass] = []
                
        if backend=="tmva":
            model_name = wname.replace(".models.xml", "")

            ## - - instantiate the classifier and invoke it's reader
            clf = Classifier(method_type=TMVA.Types.kBDT,
                             method_name=model_name,
                             model_file=model_file)

            models[mass][fold]["%s_mass_%s_ntracks_%i"%(name, mass, ntracks)] = clf
        else:
            # if isNN == True:
            #     mfileh5 = model_file.replace("pkl", "h5")
            with open(model_file, "r") as mfile:
                #mfileh5 = mfile.replace("pkl", "h5")
                model = cPickle.load(mfile)
                if isNN == True:
                    mfileh5 = model_file.replace("pkl", "h5")
                    try:
                        Keras_model = load_model(mfileh5)
                    except:
                        Keras_model = cPickle.load(mfile)
                if mass in wname and "ntracks_%i"%ntracks in wname:
                    models[mass] += [model]
                    if isNN == True:
                        Keras_models[mass] += [Keras_model]

    assert models, "no trained model is found!; exiting!"
    if isNN == True:
        log.info("Returning Keras Models")
        return models, Keras_models
    else:
        return models, None

##-----------------------------------------------
##
##-----------------------------------------------
def get_trees(tfile, systs=False):
    """=
    Retrun a list of TTrees in a given root file.
    """
    trees = set()
    trees.add(tfile.Get('NOMINAL'))
    if systs:
        keys = [k.GetName() for k in tfile.GetListOfKeys()]
        keys = filter(lambda k: isinstance(tfile.Get(k), ROOT.TTree), keys)
        for k in keys:
            if k=='EventLoop_FileExecuted':
                continue
            tree = tfile.Get(k)
            tree.SetName(k) # Rename UNICORNBASE to systematic name
            trees.add(tree)
        
    return trees

##-----------------------------------------------
##
##-----------------------------------------------

def get_trees_and_keys(tfile, systs=False):
    trees = []
    trees.append((tfile.Get('NOMINAL'), ['NOMINAL']))
    if systs:
        keys = [k.GetName() for k in tfile.GetListOfKeys()]
        keys = filter(lambda k: isinstance(tfile.Get(k), ROOT.TTree), keys)
        baseKeys = []
        for k in keys:
            if k=='EventLoop_FileExecuted':
                continue
            if k == "NOMINAL": continue
            baseKeys.append(k)
        base = tfile.xCompression.Get('UNICORNBASE')
        trees.append((base, baseKeys))

    return trees

##-----------------------------------------------
##
##-----------------------------------------------
def setup_score_branches(tree, models, outTree=None, truthmasses=None):
    """
    # Setup MVA score output branches
    # TODO look up how many mass points there are based on number of trained Models...
    """
    
    scores = dict()
    score_branches = []
    for mass in sorted(list(models.keys())):
        for name in [models[mass][0].name]: #models[mass][0]:
            # if score branch is already in tree do nothing.
            if name in [b.GetName() for b in outTree.GetListOfBranches()]:
                log.warning("%s is already in %s (skipping tree)"%(name, tree.GetName()))
                continue
            if truthmasses is None:
                score = array.array('f', [-100.])
                scores[name] = score
                sb = outTree.Branch(name, score, name+"/F")
                score_branches.append(sb)
            else:
                for truthmass in truthmasses:
                    newname = mass+"_{}".format(truthmass)
                    score = array.array('B', [255])
                    scores[newname] = score
                    sb = outTree.Branch(newname, score, newname+"/b")
                    score_branches.append(sb)
    
    return scores, score_branches

##-----------------------------------------------
##
##-----------------------------------------------
def setup_tformulas(tree, features, truthmass=None):
    # Setup a TTreeFormula for each feature
    forms_tau, forms_fake = [], []
    for feat in features:
        if truthmass is not None and feat.name == "TruthMass": feat.tformula=str(truthmass)
        form = ROOT.TTreeFormula(feat.name, feat.tformula, tree)
        forms_tau.append(form)
        if "upsilong" in feat.name:
            form = ROOT.TTreeFormula(feat.name, QCD.UPSILON_CORRECTED["mc16"], tree)
        forms_fake.append(form)
    
    for form in forms_tau: form.SetQuickLoad(True)
    for form in forms_fake: form.SetQuickLoad(True)
    
    return forms_tau, forms_fake

##-----------------------------------------------
## 
##-----------------------------------------------
def fill_scores_histogram(tree, models, hist_template=None, event_selection=None, 
    event_weight=None, correct_upsilon=False, event_list=None, isNN=False):
    """ evaluate scores from a model on a tree and fill a histogram
    Parameters
    ----------
    tree: ROOT.TTree, 
        tree with the which has input features in
    hist_template: ROOT.TH1,
        histogram to fill
    model: sklrean Classification, 
        trained model
    event_selection: ROOT.TTreeFormula,
        cuts to be applied on the events
    event_weight: ROOT.TTFormula,
        event weight for the histogram
    event_list: ROOT.TEventList,
        preseleted list of events to consider

    Return
    ------
    hist_template: ROOT.TH1F,
        filled histogram
    """
    if isNN == True:
        scaler = StandardScaler()
        # import tensorflow as tf
        # import keras
        # from keras.models import Sequential
        # from keras.layers import Dense, Activation, BatchNormalization, Dropout, LeakyReLU
        # from keras.regularizers import l2
        # from keras import initializers
        # from keras.optimizers import SGD
        # from keras.wrappers.scikit_learn import KerasClassifier
        # from keras.models import load_model
        # from keras import backend as K
        # from keras.layers import LeakyReLU  
        # from tensorflow.python.client import device_lib
    if log.isEnabledFor(logging.DEBUG):
        # Converting these to strings is slow, even if the logger doesn't print anything
        log.debug("---------------- models:\n %r"%models)

    event_number = ROOT.TTreeFormula("event_number", "event_number", tree)

    clf_feats_tf = []
    for feat in models[0].features:
        if correct_upsilon and "upsilon" in feat.name.lower():
            clf_feats_tf.append(ROOT.TTreeFormula(feat.name, QCD.UPSILON_CORRECTED["mc16"], tree))
        else:
            clf_feats_tf.append(ROOT.TTreeFormula(feat.name, feat.tformula, tree))
    for f_tf in clf_feats_tf:
        f_tf.SetQuickLoad(True)

    ## - - cache Tree
    tree.SetCacheSize(32*2**20)
    tree.SetCacheLearnEntries()
    ents = tree.GetEntries()
    info = dict() # Cache of features for events passing selection, indexed by folds
    for model in models:
        if model.kfolds not in info: info[model.kfolds] = dict()
        if model.fold_num not in info[model.kfolds]: info[model.kfolds][model.fold_num] = [[], []] # Features and weights
    entries = xrange(ents)
    if event_list is not None:
      entries = []
      for entry in xrange(event_list.GetN()):
        entries.append(event_list.GetEntry(entry))
    for entry in entries:

        tree.LoadTree(entry)

        # Logging output
        #if (entry%10000==0): 
        #    log.info("Tree: {0}, Event: {1}/{2}".format(tree.GetName(), entry+1, ents))

        # - - does the event pass the selections ?
        if event_selection is not None:
            if not event_selection.EvalInstance():
                continue

        ## - - evaluate features vector
        feats = [f.EvalInstance() for f in clf_feats_tf]
        weight = event_weight.EvalInstance()
        eventnum = event_number.EvalInstance()
        for kfolds in info:
            for fold in info[kfolds]:
                if eventnum % kfolds == fold:
                    info[kfolds][fold][0].append(feats)
                    info[kfolds][fold][1].append(weight)
    # End loop over entries

    # Convert to np.array
    for kfolds in info:
        for fold in info[kfolds]:
            if len(info[kfolds][fold][0]) > 0:
                old = info[kfolds][fold]
                info[kfolds][fold][0] = np.array(info[kfolds][fold][0])

    for model in models:
        # Loop over models, evaluating events and filling trees
        # In theory we could do this periodically while looping over events, if memory becomes a problem
        events = info[model.kfolds][model.fold_num]
        if len(events[0]) == 0: continue # No events passed the selection
        if isNN == True:
            scores = model.predict(events[0])
        else:
            scores = model.predict_proba(events[0])
        for idx in xrange(len(scores)):
            hist_template.Fill(scores[idx][1], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL)
            if idx%100000==0:
                log.debug("%r : %r "%(events[0][idx], scores[idx][1]))
    # End loop over models
    return

##-----------------------------------------------
## 
##-----------------------------------------------
def fill_scores_mult(tree, all_models, hist_templates, 
    event_list, all_Keras_models=None, event_weight=None, correct_upsilon=False, isNN=False):
    """ evaluate scores from a model on a tree and fill a histogram
    Parameters
    ----------
    ...

    Return
    ------
    ...
    """

    #if log.isEnabledFor(logging.DEBUG):
    #    # Converting these to strings is slow, even if the logger doesn't print anything
    #    log.debug("---------------- models:\n %r"%models)

    if isNN == True:
        scaler = StandardScaler()
        # import tensorflow as tf
        # import keras
        # from keras.models import Sequential
        # from keras.layers import Dense, Activation, BatchNormalization, Dropout, LeakyReLU
        # from keras.regularizers import l2
        # from keras import initializers
        # from keras.optimizers import SGD
        # from keras.wrappers.scikit_learn import KerasClassifier
        # from keras.models import load_model
        # from keras import backend as K
        # from keras.layers import LeakyReLU  
        # from tensorflow.python.client import device_lib
    event_number = ROOT.TTreeFormula("event_number", "event_number", tree)

    clf_feats_tf = dict()
    for mtag in all_models:
      for feat in all_models[mtag][0].features:
          if feat.name in clf_feats_tf: continue
          if correct_upsilon and "upsilon" in feat.name.lower():
              clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, QCD.UPSILON_CORRECTED["mc16"], tree)
          elif feat.name.lower() == "truthmass":
            clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, "80.", tree)
            #Method 1: More elegant, but slower, modify also hpana/dataset_hists.py
            #clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, hist_templates[mtag].GetTitle().split("to")[1], tree)
            #Method 1: End
          else:
              clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, feat.tformula, tree)

      for f_tf in clf_feats_tf.values():
          f_tf.SetQuickLoad(True)

    ## - - cache Tree
    tree.SetCacheSize(32*2**20)
    tree.SetCacheLearnEntries()
    infos = dict()

    for mtag in all_models:
      infos[mtag] = dict() # Cache of features for events passing selection, indexed by folds    
      for model in all_models[mtag]:
          if model.ntracks not in infos[mtag]: infos[mtag][model.ntracks] = dict()
          if model.kfolds not in infos[mtag][model.ntracks]: infos[mtag][model.ntracks][model.kfolds] = dict()
          if model.fold_num not in infos[mtag][model.ntracks][model.kfolds]: infos[mtag][model.ntracks][model.kfolds][model.fold_num] = [[], []] # Features and weights
          #if model.kfolds not in infos[mtag]: infos[mtag][model.kfolds] = dict()
          #if model.fold_num not in infos[mtag][model.kfolds]: infos[mtag][model.kfolds][model.fold_num] = [[], []] # Features and weights
    entries = []

    for entry in xrange(event_list.GetN()):
      entries.append(event_list.GetEntry(entry))

    for entry in entries:
        tree.LoadTree(entry)

        # Logging output
        #if (entry%10000==0): 
        #    log.info("Tree: {0}, Event: {1}/{2}".format(tree.GetName(), entry+1, ents))

        ## - - evaluate features
        feats = { n:v.EvalInstance() for n,v in clf_feats_tf.iteritems() }
        weight = event_weight.EvalInstance()
        eventnum = event_number.EvalInstance()

        tau_0_n_tracks =  ROOT.TTreeFormula("tau_0_n_charged_tracks", "tau_0_n_charged_tracks", tree)

        ## - - build features vectors per fold
        for mtag in all_models:
            #event_feats = [feats[feat.name] for feat in all_models[mtag][0].features]
            for ntracks in infos[mtag]:
                for model in all_models[mtag]:
                    if model.ntracks == ntracks:
                        event_feats = [feats[feat.name] for feat in model.features]
                        break
                for kfolds in infos[mtag][ntracks]:
                    for fold in infos[mtag][ntracks][kfolds]:
                        #if eventnum % kfolds == fold:
                        # tau_0_n_tracks.EvalInstance() == 0 means that there are no taus, e.g. in DILEP_BTAG region
                        if ( ntracks == tau_0_n_tracks.EvalInstance() or (ntracks == 3 and tau_0_n_tracks.EvalInstance() == 0) ) and eventnum % kfolds == fold:
                            infos[mtag][ntracks][kfolds][fold][0].append(event_feats)
                            infos[mtag][ntracks][kfolds][fold][1].append(weight)
#          for kfolds in infos[mtag]:
#              for fold in infos[mtag][kfolds]:
#                  if eventnum % kfolds == fold:
#                      infos[mtag][kfolds][fold][0].append(event_feats)
#                      infos[mtag][kfolds][fold][1].append(weight)

    # End loop over entries

    ## - - convert to np.array
    for mtag in infos:
        for ntracks in infos[mtag]:
            for kfolds in infos[mtag][ntracks]:
                for fold in infos[mtag][ntracks][kfolds]:
                    if len(infos[mtag][ntracks][kfolds][fold][0]) > 0:
                        old = infos[mtag][ntracks][kfolds][fold]
                        infos[mtag][ntracks][kfolds][fold][0] = np.array(infos[mtag][ntracks][kfolds][fold][0])
#      for kfolds in infos[mtag]:
#          for fold in infos[mtag][kfolds]:
#              if len(infos[mtag][kfolds][fold][0]) > 0:
#                  old = infos[mtag][kfolds][fold]
#                  infos[mtag][kfolds][fold][0] = np.array(infos[mtag][kfolds][fold][0])

    if isNN == True:
        #for mtag in all_models:
        for mtag, mtag_Keras in zip(all_models, all_Keras_models):
            #for model in all_models[mtag]:
            for model, Keras_model in zip(all_models[mtag], all_Keras_models[mtag_Keras]):
                # Loop over models, evaluating events and filling trees
                # In theory we could do this periodically while looping over events, if memory becomes a problem
                events = infos[mtag][model.ntracks][model.kfolds][model.fold_num]
                #events = infos[mtag][model.kfolds][model.fold_num]
                if len(events[0]) == 0: continue # No events passed the selection

                #Method 2: Hacked, less elegant, but faster, modify also hpana/dataset_hists.py
                for key in list(hist_templates.keys()):
                  events[0][:,-1] = hist_templates[key].GetTitle().split("to")[1]
                  scores = Keras_model.predict(events[0])
                  for idx in xrange(len(scores)):
                      hist_templates[key].Fill(scores[idx], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL
                      if idx%100000==0:
                          log.debug("%r : %r "%(events[0][idx], scores[idx]))
                #Method2: End

                #Method 1: More elegant, but slower, modify also hpana/dataset_hists.py
                #scores = Keras_model.predict(events[0])
                #for idx in xrange(len(scores)):
                #    hist_templates[mtag].Fill(scores[idx], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL)
                #    if idx%100000==0:
                #        log.debug("%r : %r "%(events[0][idx], scores[idx]))
                #Method1: End

    else:  
        for mtag in all_models:
          for model in all_models[mtag]:
              # Loop over models, evaluating events and filling trees
              # In theory we could do this periodically while looping over events, if memory becomes a problem
              events = infos[mtag][model.kfolds][model.fold_num]
              if len(events[0]) == 0: continue # No events passed the selection
              scores = model.predict_proba(events[0])
              for idx in xrange(len(scores)):
                  hist_templates[mtag].Fill(scores[idx][1], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL)
                  if idx%100000==0:
                      log.debug("%r : %r "%(events[0][idx], scores[idx]))

    # End loop over models

##-----------------------------------------------
##
##-----------------------------------------------
def evaluate_scores_on_trees(file_name, models, features=[], backend="keras"):
    """
    Update tree with score branches which are
    evaluated using the available trained models.
    
    Parameters
    ----------
    tree: ROOT.TTree, tree to evaluate and append bdt scores to it
    models: dict, holding available trained models

    Return
    ------
    None
    """

    models, Keras_models = models[0], models[1]
    scaler = StandardScaler()
    # retrive trees in the tfile and loop over them
    tfile = ROOT.TFile.Open(file_name, 'READONLY')
    #trees = get_trees(tfile)
    #trees = get_trees(tfile, systs=True) # With systematics
    trees = get_trees_and_keys(tfile, systs=True)
    FRIEND_FILE_DIR="/afs/cern.ch/work/b/bburghgr/private/hpana/workarea/run/friendfiles/"
    reldir = file_name.split('/')[-2]
    fname = file_name.split('/')[-1]
    opath = os.path.join(FRIEND_FILE_DIR, reldir)
    os.system("mkdir -p {}".format(opath))
    fpath = os.path.join(opath, fname) + ".friend"
    ffile = ROOT.TFile.Open(fpath, "RECREATE") # TODO writeable
    features = []
    for mass in models:
        features += models[mass][0].features
        break
    # TODO load this from somewhere, instead of hard-coding it here
    truthmasses = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 225, 250, 275, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000]
    for treeInfo in trees:
        ## - - setup input features tformulas and score branches
        tree = treeInfo[0]
        treeKeys = treeInfo[1]
        tree_name = tree.GetName()
        # TODO correctly use tau_0_n_tracks for prong numbers
        tau_0_n_tracks =  ROOT.TTreeFormula("tau_0_n_charged_tracks", "tau_0_n_charged_tracks", tree)
        tau_0_decay_mode = ROOT.TTreeFormula("tau_0_decay_mode", "tau_0_decay_mode", tree)
        event_number = ROOT.TTreeFormula("event_number", "event_number", tree)
        # TODO use isFake to apply the upsilon transformation
        isFake = ROOT.TTreeFormula("tau_0_jet_rnn_loose==0", "tau_0_jet_rnn_loose==0", tree)
        
        forms_tau, forms_fake = dict(), dict()
        for truthmass in truthmasses:
          forms_tau[truthmass], forms_fake[truthmass] = setup_tformulas(tree, features, truthmass)
        #forms_tau, forms_fake = setup_tformulas(tree, features)
        outTree = ROOT.TTree(tree_name, tree_name) # in the friend file (ffile)
        scores, score_branches = setup_score_branches(tree, models, outTree, truthmasses)
        ## - - if all branches exist in tree, nothing to do!
        if len(score_branches)==0:
            continue
        
        ## - - cache Tree block by block 
        tree.SetCacheSize(32*2**20)
        tree.SetCacheLearnEntries()
        totalEntries = tree.GetEntries()
        blockSize = 2**10
        blocks = totalEntries/blockSize
        for block in xrange(blocks+1):
            eventNums = []
            inputs = dict()
            outputs = dict()
            offsets = dict()
            for mass, rem_dict in models.iteritems():
                    #for rem, clf_dict in rem_dict.iteritems():
                    for clf_dict in rem_dict:
                        kfolds = clf_dict.kfolds
                        break
                    break
            for rem in xrange(kfolds):
                inputs[rem] = dict()
                outputs[rem] = dict()
                offsets[rem] = 0
                for mass in truthmasses:
                    inputs[rem][mass] = []
                    outputs[rem][mass] = []
            for entry in xrange(block*blockSize, 
                                min(totalEntries, (block+1)*blockSize)):
                if (entry%10000==0): 
                    log.info("Tree: {0}, Event: {1}/{2}".format(tree_name, entry+1, totalEntries))
                tree.LoadTree(entry)
                if False: 
                    t.GetEntry(entry) # Try with this on a small file, to make sure the output is identical
                    
                #--------------------------
                # Evaluate features vector
                #--------------------------
                ## - - event number is used in kfold cut, use proper offset for evaluation
                event_num = int(event_number.EvalInstance())
                eventNums.append(event_num)
                rem = event_num % kfolds

                if isFake.EvalInstance():
                    forms = forms_fake
                else:
                    forms = forms_tau

                for truthmass in truthmasses:
                    feats = []
                    for form in forms[truthmass]:
                        feats.append(float(form.EvalInstance()))
                    inputs[rem][truthmass].append(feats)

                ## - - get prediction from each classifier
                for mass, rem_dict in models.iteritems():
                    break
                    #for rem, clf_dict in rem_dict.iteritems():
                    for clf_dict in rem_dict:
                        rem = clf_dict.fold_num
                        ## - - trained on all with rem!= event_numbr%kFOLDS --> evaluate on the complementary
                        if int(rem)!= event_num%clf_dict.kfolds: 
                            continue
                        ## - - set clf's features vector
                        #for name, clf in clf_dict.iteritems():
                        #for clf in [clf_dict]:
                        for clf in [Keras_models[mass][rem]]:
                            name = scores.keys()[0] #clf.name
                            if backend=="tmva":
                                features_dict = OrderedDict()
                                for i, ft in enumerate(features):
                                    ## - - update features_dict in place, 
                                    clf.features_dict[ft.tformula] = array.array("f", [feats[i]])
                                log.debug(clf.features_dict)
                                #scores[name][0] = clf.predict(scaler.fit_transform(features_dict))
                                scores[name][0] = clf.predict(features_dict)
                            else:
                                for name in scores.keys():
                                    truthmass = int(name.split('_')[-1])
                                    ifeats = np.array([feats[truthmass]])
                                    log.debug(ifeats)
                                    #scores[name][0] = clf.predict_proba(scaler.fit_transform(ifeats))[0][1] #<! probability of belonging to class 1 (SIGNAL)
                                    #scores[name][0] = clf.predict(ifeats)[0][1] #<! probability of belonging to class 1 (SIGNAL)
                                    #print "DEBUG: about to predict:", name
                                    scores[name][0] = int(255*clf.predict(ifeats)[0]) #<! only 1 output score? (not bkg/sig proba)
                                    #print "DEBUG: did predict" # FIXME we don't get here -- predict hangs, why?
                log.debug(scores)
                log.debug("--"*70)
                #for sb in score_branches:
                #    sb.Fill()
                #outTree.Fill()
            # End loop over entries (within a block)
            # This is where we should evaluate models and fill branches... if we can get the kfolds working right
            for mass in models:
                for rem in xrange(kfolds):
                    clf = Keras_models[mass][rem]
                    for name in scores.keys():
                        truthmass = int(name.split('_')[-1])
                        ifeats = np.array(inputs[rem][truthmass])
                        outputs[rem][truthmass] = clf.predict(ifeats)
            for event_num in eventNums:
                rem = event_num % kfolds
                for name in scores.keys():
                    truthmass = int(name.split('_')[-1])
                    scores[name][0] = int(255*outputs[rem][truthmass][offsets[rem]])
                offsets[rem] += 1
                outTree.Fill()
        #tree.Write(tree.GetName(), ROOT.TObject.kOverwrite)
        #outTree.Write(outTree.GetName(), ROOT.TObject.kOverwrite)
        for key in treeKeys:
          outTree.SetName(key)
          outTree.Write(key, ROOT.TObject.kOverwrite)
    pass #<! trees loop
    tfile.Close()
    ffile.Close()

    return 
