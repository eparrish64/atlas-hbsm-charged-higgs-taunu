""" Functionalities for evaluating a trained model. 
"""

## stdlib
import multiprocessing, os, re, shutil, array 
from multiprocessing import Process
from collections import OrderedDict
from os import environ

## PyPI
from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np
import cPickle

## local
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
        evaluate_scores(output, self.models)

        return 


##--------------------------------------------------------------------------
## plot predicted signal and background scores 
##--------------------------------------------------------------------------
def plot_scores(models, dframe=None, backgrounds=[], signals=[], ntracks=[1], kfolds=5,
                outdir="", bins=None, plot_roc=True, overlay_rocs=False, label=None, outname=None):
    """
    """
    b_dframe = dframe.loc[[bkg.name for bkg in backgrounds]]
    s_dframe = dframe.loc[[sig.name for sig in signals]]
    log.debug(30*"*" + " Testing Data Frame " + 30*"*")
    log.debug(dframe)
    log.info("Signals: {0} || #events: {1} ; backgrounds: {2} || #events: {3}".format(
        [s.name for s in signals], s_dframe.shape[0], [b.name for b in backgrounds], b_dframe.shape[0]))

    rocs = []
    for mtag, tdict in models.iteritems():
        ## evaluate based on the mass region that the model is trained on
        masses = [int(m) for m in mtag.split("to")] 
        r_signals = filter(lambda s: masses[0] <= s.mass <= masses[1], signals)
        log.info("*"*80)
        for sig in r_signals:
            sm_df = dframe.loc[[sig.name]]
            for ntrack in ntracks:
                m_models = models[mtag][ntrack]
                ## trained on fold !=rem --> test on the complementary fold
                s_scores = []
                b_scores = []
                for rem in range(kfolds):
                    m_model = filter(lambda m: "fold_%i"%rem in m.name, m_models)[0]
                    if not m_model:
                        log.warning("Failed to retrive trained model in mass range %s, ntracks=%i, and for fold %i"%(mtag, ntrack, rem))
                        continue
                    if m_model.kfolds!=kfolds:
                        log.warning(
                            "The %s model is trained with %i folds while you want to evaluate it on %i folds, this will bias the perofrmance!!!"%(
                                m_model.name, m_model.kfolds, kfolds))

                    feats = m_model.features
                    b_df = b_dframe[(b_dframe["event_number"]%kfolds==rem) & (b_dframe["tau_0_n_charged_tracks"]==ntrack)]
                    b_test = b_df[[ft.name for ft in feats ]]

                    s_df = sm_df[(sm_df["event_number"]%kfolds==rem) & (sm_df["tau_0_n_charged_tracks"]==ntrack)]
                    s_test = s_df[[ft.name for ft in feats ]]

                    ## evaluate score 
                    b_score = m_model.predict_proba(b_test)[:, 1]
                    b_scores += [b_score]
                    s_score = m_model.predict_proba(s_test)[:, 1]
                    s_scores += [s_score]

                b_arr = np.concatenate(b_scores)
                s_arr = np.concatenate(s_scores)

                ## - - plot
                log.info("Testing on mass %i, ntrack=%i, bkg events=%i, and sig events=%i"%(
                        sig.mass, ntrack, b_arr.shape[0], s_arr.shape[0]))
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
            models[mass] = dict()

        if not ntracks in models[mass]: 
            models[mass][ntracks] = []
                
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
                    models[mass][ntracks] += [model]

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
