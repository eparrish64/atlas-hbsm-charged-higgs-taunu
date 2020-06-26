# stdlib
import os
import array
import numpy as np

# local
from . import log
from .mem_branches import MEM_BRANCHES, VETO_BRANCHES
from .containers import Histset

# ROOT
import ROOT

# --------------------------------------------------------------------------
# - - helper for Pool processing
# --------------------------------------------------------------------------
def dataset_hists(hist_worker,
                  outdir="histsdir",
                  **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    channel = hist_worker.channel
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematics = hist_worker.systematics
    outname = kwargs.pop("outname", hist_worker.name)
    hist_templates = hist_worker.hist_templates

    log.debug("*********** processing %s dataset ***********" % dataset.name)
    if not dataset.files:
        log.warning("%s dataset is empty!!" % dataset.name)
        return []
    log.debug("DATASET {} files: {}".format(dataset.name, dataset.files))

    canvas = ROOT.TCanvas()
    # - - - - containers for hists
    hist_set = []
    # <! since we have to update hists name, keep tformulas untouched
    hist_templates_tformuals = {}
    for systematic in systematics:
        for syst_var in systematic.variations:
            for var in fields:
                if hist_templates and var.name in hist_templates:
                    if not var.name in hist_templates_tformuals:
                        hist_templates_tformuals[var.name] = hist_templates[var.name].GetName(
                        )
                for category in categories:
                    if hist_templates and var.name in hist_templates:
                        hist = hist_templates[var.name]
                    else:
                        if var.bins:
                            hist = ROOT.TH1F(
                                "syst_%s_category_%s_var_%s" % (
                                    syst_var.name, category.name, var.name), var.name, len(var.bins)-1, array.array("d", var.bins))
                        else:
                            hist = ROOT.TH1F(
                                "syst_%s_category_%s_var_%s" % (
                                    syst_var.name, category.name, var.name), var.name, *var.binning)

                    hset = Histset(
                        name=outname,
                        sample=outname,
                        variable=var.name,
                        category=category.name,
                        hist=hist.Clone(),  # <! a copy per category
                        systematic=syst_var.name)

                    # - - make sure the newly created hist has no dummy value
                    hset.hist.Reset()
                    hist_set.append(hset)

    # - - loop over dataset's files
    nevents = 0
    for fn in dataset.files:
        fname = fn.split("/")[-1]
        tfile = ROOT.TFile(fn)
        for systematic in systematics:
            syst_type = systematic._type
            log.debug(
                "Doing systematic %s of type %s with %r variations"%(systematic.name, systematic._type, [v.name for v in systematic.variations]))
            for syst_var in systematic.variations:  
                # - - get hists for the current systematic
                syst_hists = filter(lambda hs: hs.systematic ==
                                    syst_var.name, hist_set)

                # - - check type of systematics
                if syst_type == "TREE":
                    tree_name = syst_var.name
                else:
                    tree_name = "NOMINAL"

                # - - check if the file is healthy
                try:
                    entries = tfile.Get(tree_name).GetEntries()
                    nevents += entries
                    if entries == 0:
                        log.warning("%s tree in %s is empty, skipping!" %
                                    (tree_name, fn))
                        continue
                except:
                    log.warning("%s has no %s tree!" % (fn, systematic))
                    continue

                # - - prepares selection categories
                for n, category in enumerate(categories):
                    # - - get hists for the current category
                    cat_hists = filter(lambda hs: hs.category ==
                                    category.name, syst_hists)

                    # - - get the tree
                    tree = tfile.Get(tree_name)

                    # - - cache only the events that pass the selections
                    selection = category.cuts.GetTitle()
                    tree.Draw(">>eventlist_%s" % category.name, selection)
                    eventlist = ROOT.gDirectory.Get("eventlist_%s" % category.name)
                    tree.SetEventList(eventlist)

                    # - - event weight
                    # - - if weights is not provided to the worker directly, then it's taken from systematic (the case for FFs weights)
                    eventweight = "1."
                    if weights:
                        eventweight = "*".join(weights[category.name])
                    if syst_type == "WEIGHT":
                        if isinstance(syst_var.title, dict):
                            sw = syst_var.title[category.name][0]
                        else:
                            sw = syst_var.title
                        eventweight = "(%s)*(%s)" % (eventweight, sw)

                    # - - draw all the vars
                    for var in fields:
                        histname = "category_%s_%s_%s" % (
                            category.name, var.name, fname)
                        if hist_templates and var.name in hist_templates:
                            ht = hist_templates[var.name]
                            var_formula = hist_templates_tformuals[var.name]
                            if isinstance(ht, ROOT.TH1F):
                                nbins = ht.GetNbinsX()
                                ht_bins = (nbins, ht.GetBinLowEdge(
                                    1), ht.GetBinLowEdge(nbins) + ht.GetBinWidth(1))
                            elif isinstance(ht, ROOT.TH2F):
                                nbins_x = ht.GetNbinsX()
                                ht_x = ht.GetXaxis()
                                ht_bins_x = (nbins_x, ht_x.GetBinLowEdge(
                                    1), ht_x.GetBinLowEdge(nbins_x) + ht_x.GetBinWidth(1))

                                nbins_y = ht.GetNbinsY()
                                ht_y = ht.GetYaxis()
                                ht_bins_y = (nbins_y, ht_y.GetBinLowEdge(
                                    1), ht_y.GetBinLowEdge(nbins_y) + ht_y.GetBinWidth(1))
                                ht_bins = ht_bins_x + ht_bins_y

                            elif isinstance(ht, ROOT.TH3F):
                                nbins_x = ht.GetNbinsX()
                                ht_x = ht.GetXaxis()
                                ht_bins_x = (nbins_x, ht_x.GetBinLowEdge(
                                    1), ht_x.GetBinLowEdge(nbins_x) + ht_x.GetBinWidth(1))

                                nbins_y = ht.GetNbinsY()
                                ht_y = ht.GetYaxis()
                                ht_bins_y = (nbins_y, ht_y.GetBinLowEdge(
                                    1), ht_y.GetBinLowEdge(nbins_y) + ht_y.GetBinWidth(1))

                                nbins_z = ht.GetNbinsZ()
                                ht_z = ht.GetZaxis()
                                ht_bins_z = (nbins_z, ht_z.GetBinLowEdge(
                                    1), ht_z.GetBinLowEdge(nbins_z) + ht_z.GetBinWidth(nbins_z))

                                ht_bins = ht_bins_x + ht_bins_y + ht_bins_z
                            else:
                                raise TypeError("ROOT.TH type is required")
                            tree.Draw("{0} >> {1}{2}".format(
                                var_formula, histname, ht_bins), eventweight)
                        else:
                            tree.Draw("{0} >> {1}{2}".format(var.tformula,
                                                            histname, var.binning), eventweight)
                        log.debug("{0} >> {1}{2}".format(var.tformula,
                                                        histname, var.bins if var.bins else var.binning))
                        log.debug("({0}) * ({1})".format(selection, eventweight))

                        htmp = ROOT.gDirectory.Get(histname)
                        if not htmp:
                            log.error("Failed to get %s histogram for %s dataset"%(histname, outname))
                            continue 
                        htmp.SetDirectory(0)
                        if var.bins:
                            htmp = htmp.Rebin(len(var.bins)-1, "hn",
                                            array.array("d", var.bins))

                        hset = filter(lambda hs: hs.variable ==
                                    var.name, cat_hists)[0]
                        hset.hist.Add(htmp)
                        # ! - - - - need to make the name unique to avoid stupid ROOT.TAppend Warnings
                        hset.hist.SetName("%s_category_%s_var_%s" %
                                        (outname, category.name, var.name))

                        htmp.Delete()
                    tree.Delete()
        tfile.Close()

    write_hists = kwargs.pop("write_hists", False)

    # <! FIX ME: should give the sample name a better solution
    prefix = kwargs.pop("prefix", outname.split(".")[0])
    if write_hists:
        if not os.path.isdir(outdir):
            os.system("mkdir -p %s" % outdir)
        for systematic in systematics:            
            hname = "%s.root"%(outname)
            hpath = os.path.join(outdir, hname)
            hfile = ROOT.TFile(hpath, "UPDATE")
            for syst_var in systematic.variations:
                rdir = syst_var.name
                if not hfile.GetDirectory(rdir):
                    hfile.mkdir(rdir)
                hfile.cd(rdir)

                for hset in filter(lambda hs: hs.systematic==syst_var.name, hist_set):
                    hist = hset.hist
                    hist.SetTitle(hist.GetName())
                    hist.Write("%s" % (hist.GetName().replace(
                        outname, prefix)), ROOT.TObject.kOverwrite)
            hfile.Close()

    canvas.Close()
    log.debug(hist_set)
    log.info("processed %s dataset with %i events" %
             (dataset.name, nevents))
    return hist_set


##--------------------------------------------------------------------------
## - - helper for Pool processing (looping over events directly; slower!)
##--------------------------------------------------------------------------
def dataset_hists_direct(hist_worker,
                  outdir="histsdir",
                  clf_models={},
                  clf_Keras_models={},
                  isNN=False,
                  **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    from hpana.mva.evaluation import fill_scores_mult

    channel = hist_worker.channel
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematics = hist_worker.systematics
    outname = kwargs.pop("outname", hist_worker.name)
    hist_templates = hist_worker.hist_templates

    log.debug("*********** processing %s dataset ***********" % dataset.name)
    if not dataset.files:
        log.warning("%s dataset is empty!!" % dataset.name)
        return []
    log.debug("DATASET {} files: {}".format(dataset.name, dataset.files))

    canvas = ROOT.TCanvas()
    # - - - - containers for hists
    hist_set = []
    # <! since we have to update hists name, keep tformulas untouched
    hist_templates_tformuals = {}
    for systematic in systematics:
        for syst_var in systematic.variations:
            for var in fields:
                if hist_templates and var.name in hist_templates:
                    if not var.name in hist_templates_tformuals:
                        hist_templates_tformuals[var.name] = hist_templates[var.name].GetName(
                        )
                for category in categories:
                    if hist_templates and var.name in hist_templates:
                        hist = hist_templates[var.name]
                    else:
                        if var.bins:
                            hist = ROOT.TH1F(
                                "syst_%s_category_%s_var_%s" % (
                                    syst_var.name, category.name, var.name), var.name, len(var.bins)-1, array.array("d", var.bins))
                        else:
                            hist = ROOT.TH1F(
                                "syst_%s_category_%s_var_%s" % (
                                    syst_var.name, category.name, var.name), var.name, *var.binning)

                    hset = Histset(
                        name=outname,
                        sample=outname,
                        variable=var.name,
                        category=category.name,
                        hist=hist.Clone(),  # <! a copy per category
                        systematic=syst_var.name)

                    # - - make sure the newly created hist has no dummy value
                    hset.hist.Reset()
                    hist_set.append(hset)

    if not dataset.files:
        log.warning("%s dataset is empty!!"%dataset.name)
        return []

    # - - loop over dataset's files
    nevents = 0
    for fn in dataset.files:
        fname = fn.split("/")[-1]
        tfile = ROOT.TFile(fn)
        for systematic in systematics:
            syst_type = systematic._type
            log.debug(
                "Doing systematic %s of type %s with %r variations"%(systematic.name, systematic._type, [v.name for v in systematic.variations]))
            for syst_var in systematic.variations:  
                # - - get hists for the current systematic
                syst_hists = filter(lambda hs: hs.systematic ==
                                    syst_var.name, hist_set)

                # - - check type of systematics
                if syst_type == "TREE":
                    tree_name = syst_var.name
                else:
                    tree_name = "NOMINAL"

                # - - check if the file is healthy
                try:
                    entries = tfile.Get(tree_name).GetEntries()
                    nevents += entries
                    if entries == 0:
                        log.warning("%s tree in %s is empty, skipping!" %
                                    (tree_name, fn))
                        continue
                except:
                    log.warning("%s has no %s tree!" % (fn, systematic))
                    continue

                # - - prepares selection categories
                for n, category in enumerate(categories):
                    # - - get hists for the current category
                    cat_hists = filter(lambda hs: hs.category ==
                                    category.name, syst_hists)

                    # - - get the tree
                    tree = tfile.Get(tree_name)
                    # - - speed up by reading to memory only the branches that are required
                    branches = [br.GetName() for br in tree.GetListOfBranches()]                    
                    keep_branches = filter(lambda b: not b in VETO_BRANCHES[channel], branches)
                    tree.SetBranchStatus("*", 0)
                    for br in keep_branches:
                        tree.SetBranchStatus(br, 1)

                    # - - cache only the events that pass the selections
                    selection = category.cuts.GetTitle()
                    selection = selection.replace("Name: CUT Title: ", "")
                    event_selection = ROOT.TTreeFormula("event_selection", selection, tree)


                    # - - event weight
                    # - - if weights is provided to the worker directly, then it's taken from systematic (the case for FFs weights)
                    eventweight = "1."
                    if weights:
                        eventweight = "*".join(weights[category.name])
                    if syst_type == "WEIGHT":
                        if isinstance(syst_var.title, dict):
                            sw = syst_var.title[category.name][0]
                        else:
                            sw = syst_var.title
                        eventweight = "(%s)*(%s)" % (eventweight, sw)
                    event_weight = ROOT.TTreeFormula("event_weight", eventweight, tree)
                    event_weight.SetQuickLoad(True)

                    if clf_Keras_models:
                        # - - create a TEventList of the events passing the selection
                        tree.Draw(">>event_list", selection)
                        event_list = ROOT.gDirectory.Get("event_list") # Used to skip over unselected events
                        hist_templates = dict()
                        correct_upsilon = False
                        if cat_hists[0].sample.startswith("QCD"):
                            correct_upsilon = True

                        for mtag in clf_Keras_models:
                            m_hists =  filter(lambda hs: mtag in hs.variable, cat_hists )
                            m_hists =  cat_hists
                            if len(m_hists)==0:
                                continue

                            for histogram in m_hists:
                                hist_tmp = histogram.hist
                                hist_tmp.SetName("%s_category_%s_var_%s" %(outname, category.name, histogram.variable))
                                #Method 1: More elegant, but slower, modify also hpana/mva/evaluation.py
                                #hist_templates[mtag] = hist_tmp
                                #fill_scores_mult(tree, clf_models, clf_Keras_models, hist_templates, event_list, event_weight=event_weight, correct_upsilon=correct_upsilon)
                                #Method 1: End

                                #Method 2: Hacked, less elegant, but faster, modify also hpana/mva/evaluation.py
                                hist_templates[histogram.variable] = hist_tmp

                        fill_scores_mult(tree, clf_models, hist_templates, event_list, all_Keras_models=clf_Keras_models, event_weight=event_weight, correct_upsilon=correct_upsilon, isNN=isNN) 
                        #Method 2: End

                    else:
                        # - - loop over the events
                        for i, event in enumerate(tree):
                            # - - does the event pass the selections ?
                            if not event_selection.EvalInstance():
                                continue
                            if i%10000==0:
                                log.debug("---------------- event #: %i"%i)
                                # - - fill the hists 
                                for hs in cat_hists:
                                    hs.hist.Fill(hs.variable, event_weight.EvalInstance())
                                    hs.hist.SetName("%s_category_%s_var_%s" %(outname, category.name, hs.variable))
                    tree.Delete()
        tfile.Close()                    

    write_hists = kwargs.pop("write_hists", False)

    # <! FIX ME: should give the sample name a better solution
    prefix = kwargs.pop("prefix", outname.split(".")[0])
    if write_hists:
        if not os.path.isdir(outdir):
            os.system("mkdir -p %s" % outdir)
        for systematic in systematics:            
            hname = "%s.root"%(outname)
            hpath = os.path.join(outdir, hname)
            hfile = ROOT.TFile(hpath, "UPDATE")
            for syst_var in systematic.variations:
                rdir = syst_var.name
                if not hfile.GetDirectory(rdir):
                    hfile.mkdir(rdir)
                hfile.cd(rdir)

                for hset in filter(lambda hs: hs.systematic==syst_var.name, hist_set):
                    hist = hset.hist
                    hist.SetTitle(hist.GetName())
                    hist.Write("%s" % (hist.GetName().replace(
                        outname, prefix)), ROOT.TObject.kOverwrite)
            hfile.Close()

    canvas.Close()
    log.debug(hist_set)
    log.info("processed %s dataset with %i events" %
             (dataset.name, nevents))
    return hist_set

