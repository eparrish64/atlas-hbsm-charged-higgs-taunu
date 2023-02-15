# stdlib
import os
import array
import numpy as np
import time

# local
from . import log
from .mem_branches import MEM_BRANCHES, VETO_BRANCHES
from .containers import Histset
from .weights import get_sample_variation_weight

# ROOT
import ROOT

# --------------------------------------------------------------------------
# - - helper for Pool processing, meant to replace dataset_hists_legacy (which was renamed)
# --------------------------------------------------------------------------
def dataset_hists(hist_worker,
                  outdir="histsdir",
                  **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    sample = hist_worker.sample
    channel = hist_worker.channel
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematics = hist_worker.systematics
    outname = kwargs.pop("outname", hist_worker.name)
    hist_templates = hist_worker.hist_templates
    frienddir = None
    if "frienddir" in kwargs:
      frienddir = kwargs["frienddir"]
    friendfile = None

    log.debug("*********** processing %s dataset ***********" % dataset.name)
    if not dataset.files:
      log.warning("%s dataset is empty!!" % dataset.name)
      return []
    log.debug("DATASET {} files: {}".format(dataset.name, dataset.files))

    canvas = ROOT.TCanvas()
    # - - - - containers for hists
    hist_set = {}
    # <! since we have to update hists name, keep tformulas untouched
    hist_templates_tformuals = {}
    for systematic in systematics:
      for syst_var in systematic.variations:
        for var in fields:
          if hist_templates and var.name in hist_templates:
            if not var.name in hist_templates_tformuals:
              hist_templates_tformuals[var.name] = hist_templates[var.name].GetName()
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
            hset.hist.SetDirectory(0)
            ROOT.SetOwnership(hset.hist, True)
            hset.hist.SetName("%s_category_%s_var_%s" % (outname, category.name, var.name))
            if syst_var.name not in hist_set:
              hist_set[syst_var.name] = {}
            if category.name not in hist_set[syst_var.name]:
              hist_set[syst_var.name][category.name] = {}
            hist_set[syst_var.name][category.name][var.name] = hset

    syst_var_types = {}
    syst_var_trees = {}
    syst_var_systs = {}
    for systematic in systematics:
      syst_type = systematic._type
      for syst_var in systematic.variations:
        # - - check type of systematics
        if syst_type == "TREE":
            tree_name = syst_var.name
        else:
            tree_name = "NOMINAL"
        if tree_name not in syst_var_trees:
          syst_var_trees[tree_name] = []
        syst_var_trees[tree_name].append(syst_var)
        syst_var_types[syst_var.name] = syst_type
        syst_var_systs[syst_var.name] = systematic

    # - - loop over dataset's files
    nevents = 0
    for fn in dataset.files:
      fname = fn.split("/")[-1]
      tfile = ROOT.TFile(fn)
      if frienddir:
        friendpath = os.path.join(frienddir, fname+".friend")
        try:
          friendfile = ROOT.TFile.Open(friendpath, "READONLY")
        except:
          friendfile = None
          log.debug("Failed to open friendfile %s"%(friendpath))
      for tree_name, tree_syst_vars in syst_var_trees.iteritems():
        # - - check if the file is healthy
        try:
            tree = tfile.Get(tree_name)
            entries = tree.GetEntries()
            nevents += entries
            if entries == 0:
                log.warning("%s tree in %s is empty, skipping!" %
                            (tree_name, fn))
                continue
        except:
            log.warning("%s has no %s tree!" % (fn, tree_name))
            continue

        if friendfile:
            tree.AddFriend(tree_name, friendfile)

        cat_syst_weights = {}
        for category in categories:
          cat_syst_weights[category.name] = {}
        for syst_var in tree_syst_vars:
          syst_type = syst_var_types[syst_var.name]
          systematic = syst_var_systs[syst_var.name]
          # set up ttreeformula stuff for event weight
          # - - event weight
          # - - if weights is not provided to the worker directly, then it's taken from systematic (the case for FFs weights)
          eventweight = "1."
          for category in categories:
            if weights:
                eventweight = "*".join(weights[category.name])
            if syst_type == "WEIGHT":
                if isinstance(syst_var.title, dict):
                    ######
                    sw = syst_var.title[category.name][0]
                    # I do not like this fix. This works for cutflows, but I doubt it will work for run-analysis
                    ######
                    # sw = syst_var.title["SR_%s"%(channel.upper())][0]
                    # sw = syst_var.title["SR_TAUJET"][0]
                else:
                    sw = syst_var.title
                eventweight = "(%s)*(%s)" % (eventweight, sw)

            eventweight = "(%s)*(%s)" % (eventweight, get_sample_variation_weight(systematic, syst_var, dataset, sample, channel))
            cat_syst_weights[category.name][syst_var.name] = ROOT.TTreeFormula("f_eventweight", eventweight, tree)
            cat_syst_weights[category.name][syst_var.name].SetQuickLoad(True)

        # set up ttreeformula stuff for cuts per category
        form_categories = {}
        for category in categories:
          form_categories[category.name] = ROOT.TTreeFormula("f_cat_{}".format(category.name), category.cuts.GetTitle(), tree)
          form_categories[category.name].SetQuickLoad(True)
        
        # set up ttreeformula stuff for each variable
        form_vars = {}
        for var in fields:
          if var.name in hist_templates_tformuals:
            form_vars[var.name] = ROOT.TTreeFormula("f_var_{}".format(var.name), hist_templates_tformuals[var.name], tree)
            form_vars[var.name].SetQuickLoad(True)
          else:
            form_vars[var.name] = ROOT.TTreeFormula("f_var_{}".format(var.name), var.tformula, tree)
            form_vars[var.name].SetQuickLoad(True)

        cws = {}
        for category in categories:
          cws[category.name] = {}
        for entry in xrange(entries):
          tree.LoadTree(entry)
          cats = []
          for category in categories:
            if form_categories[category.name].EvalInstance():
              cats.append(category.name)
          if len(cats) > 0:
            for cat in cats:
              for syst_var_name in cat_syst_weights[cat]:
                cws[cat][syst_var_name] = cat_syst_weights[cat][syst_var_name].EvalInstance()
            for var in fields:
              v = form_vars[var.name].EvalInstance() # var value
              for cat in cats:
                for syst_var_name,w in cws[cat].iteritems():
                  hist_set[syst_var_name][cat][var.name].hist.Fill(v, w)
                # End loop over systematic variations
              # End loop over categories that passed the cut
            # End loop over fields
          # End check if any categories past the cut
        # End loop over entries
        # Cleanup, this seems to mitigate most of the memory leaks
        tree.Delete()

      if friendfile:
          friendfile.Close()
      tfile.Close()
    # End loop over files

    # write_hists = kwargs.pop("write_hists", False)
    write_hists = True

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

                for caths in hist_set[syst_var.name].itervalues():
                  for hset in caths.itervalues():
                    hist = hset.hist
                    hist.SetTitle(hist.GetName())
                    hist.Write("%s" % (hist.GetName().replace(
                        outname, prefix)), ROOT.TObject.kOverwrite)
            hfile.Close()

    canvas.Close()
    log.debug(hist_set)
    log.info("processed %s dataset with %i events" %
             (dataset.name, nevents))

    # flatten hist_set into a list, since this is what the caller expects us to return (to match the legacy version)
    flat_hist_set = []
    for s in hist_set.itervalues():
      for c in s.itervalues():
        flat_hist_set += c.values()
    hist_set = flat_hist_set
    return hist_set

# --------------------------------------------------------------------------
# - - helper for Pool processing
# --------------------------------------------------------------------------
def dataset_hists_legacy(hist_worker,
                         outdir="histsdir",
                         **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    sample = hist_worker.sample
    channel = hist_worker.channel
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematics = hist_worker.systematics
    outname = kwargs.pop("outname", hist_worker.name)
    hist_templates = hist_worker.hist_templates
    frienddir = None
    if "frienddir" in kwargs:
        frienddir = kwargs["frienddir"]
    friendfile = None

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
        if frienddir:
            friendpath = os.path.join(frienddir, fname+".friend")
            try:
              friendfile = ROOT.TFile.Open(friendpath, "READONLY")
            except:
              friendfile = None
              log.debug("Failed to open friendfile %s"%(friendpath))
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
                    if friendfile:
                        tree.AddFriend(tree_name, friendfile)

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
                            ######
                            sw = syst_var.title[category.name][0]
                            # I do not like this fix. This works for cutflows, but I doubt it will work for run-analysis
                            ######
                            # sw = syst_var.title["SR_%s"%(channel.upper())][0]
                            # sw = syst_var.title["SR_TAUJET"][0]
                        else:
                            sw = syst_var.title
                        eventweight = "(%s)*(%s)" % (eventweight, sw)

                    eventweight = "(%s)*(%s)" % (eventweight, get_sample_variation_weight(systematic, syst_var, dataset, sample, channel))

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
        if friendfile:
            friendfile.Close()
        tfile.Close()

    # write_hists = kwargs.pop("write_hists", False)
    write_hists = True

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
def dataset_hists_direct_legacy(hist_worker,
                  outdir="histsdir",
                  clf_models={},
                  clf_Keras_models={},
                  isNN=False,
                  **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    from hpana.mva.evaluation import fill_scores_mult

    sample = hist_worker.sample
    channel = hist_worker.channel
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematics = hist_worker.systematics
    outname = kwargs.pop("outname", hist_worker.name)
    hist_templates = hist_worker.hist_templates
    frienddir = None
    if "frienddir" in kwargs:
        frienddir = kwargs["frienddir"]
    friendfile = None

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
        if frienddir:
            friendpath = os.path.join(frienddir, fname+".friend")
            try:
              friendfile = ROOT.TFile.Open(friendpath, "READONLY")
            except:
              friendfile = None
              log.debug("Failed to open friendfile %s"%(friendpath))
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
                    if friendfile:
                        tree.AddFriend(tree_name, friendfile)
                    # - - speed up by reading to memory only the branches that are required
                    branches = [br.GetName() for br in tree.GetListOfBranches()]                    
                    keep_branches = filter(lambda b: not b in VETO_BRANCHES[channel], branches)
                    tree.SetBranchStatus("*", 0)
                    for br in keep_branches:
                        tree.SetBranchStatus(br, 1)
                    if friendfile:
                      tree.SetBranchStatus("80to3000_*", 1)

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
                    eventweight = "(%s)*(%s)" % (eventweight, get_sample_variation_weight(systematic, syst_var, dataset, sample, channel))
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
        if friendfile:
            friendfile.Close()  
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

#####

# --------------------------------------------------------------------------
# - - helper for Pool processing, meant to replace dataset_hists[_direct] for PNN use
# --------------------------------------------------------------------------
def dataset_hists_direct(hist_worker,
                  outdir="histsdir",
                  clf_models={},
                  clf_Keras_models={},
                  isNN=False,
                  **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    from hpana.samples.fakes import QCD
    sample = hist_worker.sample
    channel = hist_worker.channel
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematics = hist_worker.systematics
    outname = kwargs.pop("outname", hist_worker.name)
    hist_templates = hist_worker.hist_templates
    frienddir = None
    if "frienddir" in kwargs:
      frienddir = kwargs["frienddir"]
    friendfile = None

    assert clf_models and clf_Keras_models, "dataset_hists_direct must be run with clf_models and clf_Keras_models"

    log.debug("*********** processing %s dataset ***********" % dataset.name)
    if not dataset.files:
      log.warning("%s dataset is empty!!" % dataset.name)
      return []
    log.debug("DATASET {} files: {}".format(dataset.name, dataset.files))

    canvas = ROOT.TCanvas()
    # - - - - containers for hists
    hist_set = {}
    # <! since we have to update hists name, keep tformulas untouched
    hist_templates_tformuals = {}
    for systematic in systematics:
      for syst_var in systematic.variations:
        for var in fields:
          if hist_templates and var.name in hist_templates:
            if not var.name in hist_templates_tformuals:
              hist_templates_tformuals[var.name] = hist_templates[var.name].GetName()
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
            hset.hist.SetDirectory(0)
            ROOT.SetOwnership(hset.hist, True)
            hset.hist.SetName("%s_category_%s_var_%s" % (outname, category.name, var.name))
            if syst_var.name not in hist_set:
              hist_set[syst_var.name] = {}
            if category.name not in hist_set[syst_var.name]:
              hist_set[syst_var.name][category.name] = {}
            hist_set[syst_var.name][category.name][var.name] = hset

    syst_var_types = {}
    syst_var_trees = {}
    syst_var_systs = {}
    for systematic in systematics:
      syst_type = systematic._type
      for syst_var in systematic.variations:
        # - - check type of systematics
        if syst_type == "TREE":
            tree_name = syst_var.name
        else:
            tree_name = "NOMINAL"
        if tree_name not in syst_var_trees:
          syst_var_trees[tree_name] = []
        syst_var_trees[tree_name].append(syst_var)
        syst_var_types[syst_var.name] = syst_type
        syst_var_systs[syst_var.name] = systematic

    # - - loop over dataset's files
    nevents = 0
    for fn in dataset.files:
      fname = fn.split("/")[-1]
      tfile = ROOT.TFile(fn)
      if frienddir:
        friendpath = os.path.join(frienddir, fname+".friend")
        try:
          friendfile = ROOT.TFile.Open(friendpath, "READONLY")
        except:
          friendfile = None
          log.debug("Failed to open friendfile %s"%(friendpath))
      for tree_name, tree_syst_vars in syst_var_trees.iteritems():
        # - - check if the file is healthy
        try:
            tree = tfile.Get(tree_name)
            entries = tree.GetEntries()
            nevents += entries
            if entries == 0:
                log.warning("%s tree in %s is empty, skipping!" %
                            (tree_name, fn))
                continue
        except:
            log.warning("%s has no %s tree!" % (fn, tree_name))
            continue

        if friendfile:
            tree.AddFriend(tree_name, friendfile)

        cat_syst_weights = {}
        for category in categories:
          cat_syst_weights[category.name] = {}
        for syst_var in tree_syst_vars:
          syst_type = syst_var_types[syst_var.name]
          systematic = syst_var_systs[syst_var.name]
          # set up ttreeformula stuff for event weight
          # - - event weight
          # - - if weights is not provided to the worker directly, then it's taken from systematic (the case for FFs weights)
          eventweight = "1."
          for category in categories:
            if weights:
                eventweight = "*".join(weights[category.name])
            if syst_type == "WEIGHT":
                if isinstance(syst_var.title, dict):
                    ######
                    sw = syst_var.title[category.name][0]
                    # I do not like this fix. This works for cutflows, but I doubt it will work for run-analysis
                    ######
                    # sw = syst_var.title["SR_%s"%(channel.upper())][0]
                    # sw = syst_var.title["SR_TAUJET"][0]
                else:
                    sw = syst_var.title
                eventweight = "(%s)*(%s)" % (eventweight, sw)

            eventweight = "(%s)*(%s)" % (eventweight, get_sample_variation_weight(systematic, syst_var, dataset, sample, channel))
            cat_syst_weights[category.name][syst_var.name] = ROOT.TTreeFormula("f_eventweight", eventweight, tree)
            cat_syst_weights[category.name][syst_var.name].SetQuickLoad(True)

        # set up ttreeformula stuff for cuts per category
        form_categories = {}
        for category in categories:
          form_categories[category.name] = ROOT.TTreeFormula("f_cat_{}".format(category.name), category.cuts.GetTitle(), tree)
          form_categories[category.name].SetQuickLoad(True)

        # Lots of the below code was copy/pasted, these aliases are just to fix that, TODO: clean things up
        all_models = clf_models
        all_Keras_models = clf_Keras_models
        
        # set up ttreeformula stuff for each variable used as a PNN input
        # FIXME upsilon correction, this is different per sample, so we need some special logic for that one...
        # Specifically we actually need to set correct_upsilon at some point
        correct_upsilon = sample.startswith("QCD")
        
        clf_feats_tf = dict()
        for mtag in all_models:
          for feat in all_models[mtag][0].features:
              if feat.name in clf_feats_tf: continue
              if correct_upsilon and "upsilon" in feat.name.lower():
                  clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, QCD.UPSILON_CORRECTED["mc16"], tree)
                  clf_feats_tf[feat.name].SetQuickLoad(True)
              elif feat.name.lower() == "truthmass":
                clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, "80.", tree)
                clf_feats_tf[feat.name].SetQuickLoad(True)
                #Method 1: More elegant, but slower, modify also hpana/dataset_hists.py
                #clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, hist_templates[mtag].GetTitle().split("to")[1], tree)
                #Method 1: End
              else:
                  clf_feats_tf[feat.name] = ROOT.TTreeFormula(feat.name, feat.tformula, tree)

        # Used for kfolds
        event_number = ROOT.TTreeFormula("event_number", "event_number", tree)
        event_number.SetQuickLoad(True)
        # Tau tracks used to select 1p/3p networks
        tau_0_n_tracks =  ROOT.TTreeFormula("tau_0_n_charged_tracks", "tau_0_n_charged_tracks", tree)
        tau_0_n_tracks.SetQuickLoad(True)
        # TODO:
        # Loop over events
        # For each event, check if it passes at least 1 category
        # If yes, then evaluate the feats and weights for this event, and push them to a list
        # Also if yes, push a 0 or 1 to indicate category status for where the event is needed
        # After all the info has been extracted, then and only then do we run the PNNs and fill histograms
        # FIXME this needs to be per-prong (WIP) and *per fold*
        infos = dict()
        for mtag in all_models:
          infos[mtag] = dict() # Cache of features for events passing selection, indexed by folds    
        for model in all_models[mtag]:
            if model.ntracks not in infos[mtag]: infos[mtag][model.ntracks] = dict()
            if model.kfolds not in infos[mtag][model.ntracks]: infos[mtag][model.ntracks][model.kfolds] = dict()
            if model.fold_num not in infos[mtag][model.ntracks][model.kfolds]:
              infos[mtag][model.ntracks][model.kfolds][model.fold_num] = {"feats": [], "weights": {}, "categories": {}}
              for cat in categories:
                infos[mtag][model.ntracks][model.kfolds][model.fold_num]["categories"][cat.name] = []
                infos[mtag][model.ntracks][model.kfolds][model.fold_num]["weights"][cat.name] = {}
                for syst_var_name in cat_syst_weights[cat.name]:
                  infos[mtag][model.ntracks][model.kfolds][model.fold_num]["weights"][cat.name][syst_var_name] = []

        cws = {}
        for category in categories:
          cws[category.name] = {}

        for entry in xrange(entries):
          tree.LoadTree(entry)
          cats = set()
          for cat in form_categories:
            if form_categories[cat].EvalInstance():
              cats.add(cat)
          if len(cats) == 0: continue
          # Get event number, tracks, and PNN features
          eventnum = event_number.EvalInstance()
          ntracks = tau_0_n_tracks.EvalInstance()
          feats = { n:v.EvalInstance() for n,v in clf_feats_tf.iteritems() }
          # Now get the weights
          for cat in cats:
            for syst_var_name in cat_syst_weights[cat]:
              cws[cat][syst_var_name] = cat_syst_weights[cat][syst_var_name].EvalInstance()
          # Now the features
          
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
                      infos[mtag][ntracks][kfolds][fold]["feats"].append(event_feats)
                      for cat in form_categories:
                        infos[mtag][ntracks][kfolds][fold]["categories"][cat].append(1 if cat in cats else 0)
                        for syst_var_name in cat_syst_weights[cat]:
                          infos[mtag][ntracks][kfolds][fold]["weights"][cat][syst_var_name].append(cws[cat][syst_var_name])
                # End loop over folds
              # End lop over kfolds
            # End loop over ntracks
          # End loop over mtags
        # End loop over events
        tree.Delete()

        ## - - convert to np.array
        for mtag in infos:
          for ntracks in infos[mtag]:
            for kfolds in infos[mtag][ntracks]:
              for fold in infos[mtag][ntracks][kfolds]:
                if len(infos[mtag][ntracks][kfolds][fold]["feats"]) > 0:
                  infos[mtag][ntracks][kfolds][fold]["feats"] = np.array(infos[mtag][ntracks][kfolds][fold]["feats"])

        #for mtag in all_models:
        for mtag, mtag_Keras in zip(all_models, all_Keras_models):
          #for model in all_models[mtag]:
          for model, Keras_model in zip(all_models[mtag], all_Keras_models[mtag_Keras]):
            # Loop over models, evaluating events and filling trees
            # In theory we could do this periodically while looping over events, if memory becomes a problem
            events = infos[mtag][model.ntracks][model.kfolds][model.fold_num]
            #events = infos[mtag][model.kfolds][model.fold_num]
            if len(events["feats"]) == 0: continue # No events passed the selection

            # TODO only evaluate things once, not 100% sure that's happening right here... print some debug output to check or something
            ws = events["weights"]
            cs = events["categories"]
            for var in fields:
              mass = float(var.name.split("to")[1])
              events["feats"][:,-1] = mass
              scores = Keras_model.predict(events["feats"])
              for idx in xrange(len(scores)):
                for cat in cs:
                  if not cs[cat][idx]:
                    continue
                  for syst_var in ws[cat]:
                    hist_set[syst_var][cat][var.name].hist.Fill(scores[idx], ws[cat][syst_var][idx])

            # TODO basically method 2, but:
            # the mass comes from var.name for the histograms
            # the weights and category status come from events["weights"][syst_name][idx] and events["categories"][cat_name][idx]

            ##Method 2: Hacked, less elegant, but faster, modify also hpana/dataset_hists.py
            #for key in list(hist_templates.keys()):
            #  events["feats"][:,-1] = hist_templates[key].GetTitle().split("to")[1]
            #  scores = Keras_model.predict(events["feats"])
            #  continue
            #  # TODO fix the below, we need to fill the right histogram based on e.g. category and (weight) systematic
            #  for idx in xrange(len(scores)):
            #      hist_templates[key].Fill(scores[idx], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL
            #      if idx%100000==0:
            #          log.debug("%r : %r "%(events[0][idx], scores[idx]))
            #Method2: End

            #Method 1: More elegant, but slower, modify also hpana/dataset_hists.py
            #scores = Keras_model.predict(events[0])
            #for idx in xrange(len(scores)):
            #    hist_templates[mtag].Fill(scores[idx], events[1][idx]) # <! probability of belonging to class 1 (SIGNAL)
            #    if idx%100000==0:
            #        log.debug("%r : %r "%(events[0][idx], scores[idx]))
            #Method1: End

      if friendfile:
          friendfile.Close()
      tfile.Close()

    # End loop over files

    # write_hists = kwargs.pop("write_hists", False)
    write_hists = True

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

                for caths in hist_set[syst_var.name].itervalues():
                  for hset in caths.itervalues():
                    hist = hset.hist
                    hist.SetTitle(hist.GetName())
                    hist.Write("%s" % (hist.GetName().replace(
                        outname, prefix)), ROOT.TObject.kOverwrite)
            hfile.Close()

    canvas.Close()
    log.debug(hist_set)
    log.info("processed %s dataset with %i events" %
             (dataset.name, nevents))

    # flatten hist_set into a list, since this is what the caller expects us to return (to match the legacy version)
    flat_hist_set = []
    for s in hist_set.itervalues():
      for c in s.itervalues():
        flat_hist_set += c.values()
    hist_set = flat_hist_set
    return hist_set
