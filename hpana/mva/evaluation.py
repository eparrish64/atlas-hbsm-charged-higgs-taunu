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
import numpy as np
import cPickle

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


##--------------------------------------------------------------------------
## plot predicted signal and background scores 
##--------------------------------------------------------------------------
def plot_scores(models, 
        dframe=None, 
        backgrounds=[], 
        signals=[], 
        fold_var="event_number", 
        n_tracks_var="tau_0_n_charged_tracks",
        outdir="", 
        bins=None, 
        plot_roc=True, 
        overlay_rocs=False, 
        label=None, 
        outname=None):

    """
    """
    b_dframe = dframe.loc[[bkg.name for bkg in backgrounds]]
    s_dframe = dframe.loc[[sig.name for sig in signals]]
    log.debug(30*"*" + " Testing Data Frame " + 30*"*")
    log.debug(dframe)

    rocs = []
    for sig in signals:
        sm_df = dframe.loc[[sig.name]]
        s_scores = []
        b_scores = []        
        for m_model in models:
            masses = m_model.mass_range
            if not (masses[0] <= sig.mass <= masses[-1]):
                continue

            feats = m_model.features
            b_df = b_dframe[(b_dframe[fold_var]%m_model.kfolds==m_model.fold_num) & (b_dframe[n_tracks_var]==m_model.ntracks)]
            b_test = b_df[[ft.name for ft in feats ]]

            s_df = sm_df[(sm_df[fold_var]%m_model.kfolds==m_model.fold_num) & (sm_df[n_tracks_var]==m_model.ntracks)]
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

        log.info("Evaluated mass %i, ntrack=%i, bkg events=%i, and sig events=%i"%(
                sig.mass, m_model.ntracks, b_arr.shape[0], s_arr.shape[0]))
        if bins is None:
            bins = np.linspace(0, 1, 50)

        ## plot hists
        plt.figure(10)
        plt.hist(
            [s_arr, b_arr], bins, log=True, density=True, histtype="stepfilled", color=['r', 'b'], alpha=0.85, label=[r'$H^+$[%iGeV]'%sig.mass, r"$\sum BKG$"])
        plt.ylabel(r'$p.d.f$')
        plt.xlabel('BDT score')
        plt.legend(loc='upper right')

        ## save plot
        outname = os.path.join(outdir, "BDT_score_{}_{}.png".format(sig.name, m_model.name.replace(".pkl", "")))
        plt.savefig(outname)
        plt.close()

        if plot_roc:
            Y_score = np.concatenate([b_arr, s_arr])
            b_true = np.zeros(b_arr.size)
            s_true = np.ones(s_arr.size)
            Y_true = np.concatenate([b_true, s_true])

            fpr_grd, tpr_grd, _ = roc_curve(Y_true, Y_score)
            auc = roc_auc_score(Y_true, Y_score)
            
            rocs += [(m_model, fpr_grd, tpr_grd, auc)]
            ## plot roc 
            plt.figure(1)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.plot(fpr_grd, tpr_grd, label="AUC = %.4f"%auc)
            plt.ylabel('Signal efficiency ')
            plt.xlabel('Background rejection ')
            plt.title(r'ROC curve($H^+$[%iGeV])'%sig.mass)
            plt.legend(loc='best')
            outname = os.path.join(outdir, "ROC_{}_{}.png".format(sig.name, m_model.name.replace(".pkl", "") ))
            plt.savefig(outname)
            plt.close()

    if overlay_rocs:
        fig = plt.figure(10)
        ax = plt.subplot(111)
        ax.plot([0, 1], [0, 1], 'k--')
        for roc in rocs:
            rmodel, fpr_grd, tpr_grd, auc = roc
            label = "{}_nvars_{}(AUC={:.4f})".format("_".join(rmodel.name.split("_")[1:6]), len(rmodel.features), auc)
            ax.plot(fpr_grd, tpr_grd, label=label)
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
def get_models(model_files, backend="sklearn"):
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
                
        if backend=="tmva":
            model_name = wname.replace(".models.xml", "")

            ## - - instantiate the classifier and invoke it's reader
            clf = Classifier(method_type=TMVA.Types.kBDT,
                             method_name=model_name,
                             model_file=model_file)

            models[mass][fold]["%s_mass_%s_ntracks_%i"%(name, mass, ntracks)] = clf
        else:
            with open(model_file, "r") as mfile:
                model = cPickle.load(mfile)
                if mass in wname and "ntracks_%i"%ntracks in wname:
                    models[mass] += [model]

    assert models, "no trained model is found!; exiting!"
    return models

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
            trees.add(tfile.Get(k))
        
    return trees

##-----------------------------------------------
##
##-----------------------------------------------
def setup_score_branches(tree, models):
    """
    # Setup MVA score output branches
    # TODO look up how many mass points there are based on number of trained Models...
    """
    
    scores = dict()
    score_branches = []
    for mass in sorted(list(models.keys())):
        for name in models[mass][0]:
            # if score branch is already in tree do nothing.
            if name in [b.GetName() for b in tree.GetListOfBranches()]:
                log.warning("%s is already in %s (skipping tree)"%(name, tree.GetName()))
                continue
            score = array.array('f', [-100.])
            scores[name] = score
            sb = tree.Branch(name, score, name+"/F")
            score_branches.append(sb)
    
    return scores, score_branches

##-----------------------------------------------
##
##-----------------------------------------------
def setup_tformulas(tree, features):
    # Setup a TTreeFormula for each feature
    forms_tau = []
    for feat in features:
        forms_tau.append(ROOT.TTreeFormula(feat.name, feat.tformula, tree) )
    forms_fake = forms_tau[:]
    
    for form in forms_tau: form.SetQuickLoad(True)
    for form in forms_fake: form.SetQuickLoad(True)
    
    return forms_tau, forms_fake

##-----------------------------------------------
## 
##-----------------------------------------------
def fill_scores_histogram(tree, models, hist_template=None, event_selection=None, event_weight=None, correct_upsilon=False):
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

    Return
    ------
    hist_template: ROOT.TH1F,
        filled histogram
    """

    if log.isEnabledFor(logging.DEBUG):
        # Converting these to strings to call the logger is slow, so skip it if debug logging isn't enabled
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

    ## - - cache Tree block by block 
    tree.SetCacheSize(32*2**20)
    tree.SetCacheLearnEntries()
    ents = tree.GetEntries()
    blockSize = 2**18
    blocks = int(ceil(float(ents)/blockSize))
    for block in xrange(blocks+1):
        info = dict()
        for model in models:
            if model.kfolds not in info: info[model.kfolds] = dict()
            if model.fold_num not in info[model.kfolds]: info[model.kfolds][model.fold_num] = [[], []] # Features and weights
        for entry in xrange(block*blockSize, min(ents, (block+1)*blockSize)):
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
            # Note that this could be a bit more efficient if we created each list of events per fold once instead of multiple times
            events = info[model.kfolds][model.fold_num]
            if len(events[0]) == 0: continue # No events passed the selection
            scores = model.predict_proba(events[0])
            for idx in xrange(len(scores)):
                hist_template.Fill(scores[idx][1], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL)
        # End loop over models
    # End loop over blocks

##-----------------------------------------------
##
##-----------------------------------------------
def evaluate_scores_on_trees(file_name, models, features=[], backend="sklearn"):
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
    # retrive trees in the tfile and loop over them
    tfile = ROOT.TFile.Open(file_name, 'UPDATE')
    trees = get_trees(tfile)
    for tree in trees:
        ## - - setup input features tformulas and score branches
        tree_name = tree.GetName()
        tau_0_n_tracks =  ROOT.TTreeFormula("tau_0_n_charged_tracks", "tau_0_n_charged_tracks", tree)
        tau_0_decay_mode = ROOT.TTreeFormula("tau_0_decay_mode", "tau_0_decay_mode", tree)
        event_number = ROOT.TTreeFormula("event_number", "event_number", tree)
        isFake = ROOT.TTreeFormula("tau_0_jet_bdt_loose==0", "tau_0_jet_bdt_loose==0", tree)
        
        forms_tau, forms_fake = setup_tformulas(tree, features)
        scores, score_branches = setup_score_branches(tree, models)
        ## - - if all branches exist in tree, nothing to do!
        if len(score_branches)==0:
            continue
        
        ## - - cache Tree block by block 
        tree.SetCacheSize(32*2**20)
        tree.SetCacheLearnEntries()
        totalEntries = tree.GetEntries()
        blockSize = 2**18
        blocks = totalEntries/blockSize
        for block in xrange(blocks+1):
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
                feats = []
                for form in forms_tau:
                    feats.append(float(form.EvalInstance()))

                ## - - event number is used in kfold cut, use proper offset for evaluation
                event_num = int(event_number.EvalInstance())
                
                ## - - get prediction from each classifier
                for mass, rem_dict in models.iteritems():
                    for rem, clf_dict in rem_dict.iteritems():
                        ## - - trained on all with rem!= event_numbr%kFOLDS --> evaluate on the complementary
                        if int(rem)!= event_num%kFOLDS: 
                            continue
                        ## - - set clf's features vector
                        for name, clf in clf_dict.iteritems():
                            if backend=="tmva":
                                features_dict = OrderedDict()
                                for i, ft in enumerate(features):
                                    ## - - update features_dict in place, 
                                    clf.features_dict[ft.tformula] = array.array("f", [feats[i]])
                                log.debug(clf.features_dict)
                                scores[name][0] = clf.predict(features_dict)
                            else:
                                ifeats = np.array([feats])
                                log.debug(ifeats)
                                scores[name][0] = clf.predict_proba(ifeats)[0][1] #<! probability of belonging to class 1 (SIGNAL)
                log.debug(scores)
                log.debug("--"*70)
                for sb in score_branches:
                    sb.Fill()
        tree.Write(tree.GetName(), ROOT.TObject.kOverwrite)
    pass #<! trees loop
    tfile.Close()

    return 
