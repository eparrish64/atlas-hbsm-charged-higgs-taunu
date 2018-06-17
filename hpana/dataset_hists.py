from .samples.sample import Histset

##--------------------------------------------------------------------------
## helper for Pool processing 
def dataset_hists_direct(dataset, fields, categories,
                  systematic="NOMINAL",
                  outname=None,
                  outdir="outdir",
                  **kwargs):
    """
    """
    if not dataset.files:
        log.warning("%s dataset is empty!!"%dataset.name)
        return []

    # - - - - containers for hists
    hist_set = []
    for var in fields:
        for category in categories:
            category_name = category.split(":=:")[0]
            hist_set.append(Histset(
                sample=dataset.name,
                variable=var.tformula,
                category=category_name,
                hist=ROOT.TH1F("category_%s_%s"%(category_name, var.name), var.name, *var.binning),
                systematic=systematic) )

    for _file in dataset.files:
        tf = ROOT.TFile(_file)
        for category in categories:
            category_name, selection, eventweight = category.split(":=:")
            # - - hists for the current category
            cat_hists = filter(lambda cat: cat.category==category_name, hist_set)

            tree = tf.Get(systematic)
            # - - event weight
            event_weight = ROOT.TTreeFormula("event_weight", eventweight, tree)
            event_weight.SetQuickLoad(True)

            # - - get the list of the events that pass the selections
            event_selection = ROOT.TTreeFormula("event_selection", selection, tree)
            event_selection.SetQuickLoad(True)

            # - - loop over the events
            for i, event in enumerate(tree):
                # - - does the event pass the selections ?
                if not event_selection.EvalInstance():
                    continue
                # - - fill the hists 
                [hs.hist.Fill(hs.variable, event_weight.EvalInstance() ) for hs in cat_hists]

            tree.Delete()

    # - - - - shall I write the hists to disk
    write_hists = kwargs.pop("write_hists", False)
    prefix = kwargs.pop("prefix", "")
    if write_hists and outname:
        hname = prefix
        hname += outname
        hpath = hname
        if not os.path.isdir(outdir):
            os.system("mkdir -p %s"%outdir)

        hpath = os.path.join(outdir, hname)
        hfile = ROOT.TFile(hpath, "UPDATE")
        for hset in hist_set:
            hist = hset.hist
            hist.SetTitle(hist.GetName())
            hfile.cd()
            hist.Write(hist.GetName(), ROOT.TObject.kOverwrite)
        hfile.Close()

    log.info("processed %s dataset"%(dataset.name))
    return hist_set



##--------------------------------------------------------------------------
## helper for Pool processing 
def dataset_hists(hist_worker,
                  outdir="histsdir",
                  **kwargs):
    """ produces histograms for a dataset. 
    This static method is mainly used for parallel processing.
    """
    dataset = hist_worker.dataset
    fields = hist_worker.fields
    categories = hist_worker.categories
    weights = hist_worker.weights
    systematic = hist_worker.systematic
    outname = kwargs.pop("outname", hist_worker.name)

    log.debug("*********** processing %s dataset ***********"%dataset.name)
    if not dataset.files:
        log.warning("%s dataset is empty!!"%dataset.name)
        return []

    canvas = ROOT.TCanvas()
    hist_set = []
    # - - - - containers for hists
    hist_set = []
    for var in fields:
        for category in categories:
            hset = Histset(
                sample=dataset.name,
                variable=var.name,
                category=category.name,
                hist=ROOT.TH1F(
                    "category_%s_%s"%(category.name, var.name), var.name, *var.binning),
                systematic=systematic) 
            # - - make sure the newly created hist has no dummy value
            hset.hist.Reset()
            hist_set.append(hset)

    # - - loop over dataset's files
    for fn in dataset.files:
        fname = fn.split("/")[-1]
        tfile = ROOT.TFile(fn)
        for category in categories:
            # - - hists for the current category
            cat_hists = filter(lambda hs: hs.category==category.name, hist_set)
            try:
                tree = tfile.Get(systematic)
            except:
                log.warning("%s has no %s tree!"%(fn, systematic))
                continue

            # - - get the list of the events that pass the selections
            selection = category.cuts.GetTitle()
            eventweight = "*".join(weights[category.name])
            tree.Draw(">>eventlist_%s"%category.name, selection)
            eventlist = ROOT.gDirectory.Get("eventlist_%s"%category.name)
            tree.SetEventList(eventlist)

            # - - draw all the vars
            for var in fields:
                histname = "category_%s_%s_%s"%(category.name, var.name, fname)
                log.debug("{0} >> {1}{2}".format(var.tformula, histname, var.binning))
                log.debug("({0}) * ({1})".format(selection, eventweight))

                tree.Draw("{0} >> {1}{2}".format(var.tformula, histname, var.binning), eventweight)
                htmp = ROOT.gPad.GetPrimitive(histname)
                hset = filter(lambda hs: hs.variable==var.name, cat_hists)[0]
                hset.hist += htmp

            tree.Delete()
        tfile.Close()

    write_hists = kwargs.pop("write_hists", False)
    prefix = kwargs.pop("prefix", outname.split(".")[0]) #<! FIX ME: should give the sample name a better solution 
    if write_hists:
        hname = "%s.root"%outname
        if not os.path.isdir(outdir):
            os.system("mkdir -p %s"%outdir)

        hpath = os.path.join(outdir, hname)
        hfile = ROOT.TFile(hpath, "UPDATE")

        rdir = "%s"%(systematic)
        if not hfile.GetDirectory(rdir):
            hfile.mkdir(rdir)
        hfile.cd(rdir)

        for hset in hist_set:
            hist = hset.hist
            hist.SetTitle(hist.GetName())
            hist.Write("%s_%s"%(prefix, hist.GetName()), ROOT.TObject.kOverwrite)
        hfile.Close()

    canvas.Close()
    log.info("processed %s dataset"%dataset.name)
    return hist_set

