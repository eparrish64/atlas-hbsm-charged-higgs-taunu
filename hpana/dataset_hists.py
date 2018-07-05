## local
from . import log

## ROOT
import ROOT


##---------------------------------------------------------------------------------------
## - - Hist container class
##--------------------------------------------------------------------------
class Histset:
    """simple container class for histograms
    """
    def __init__(self,
                 name="Histset",
                 sample=None,
                 variable=None,
                 category=None,
                 hist=None,
                 systematic="NOMINAL",):
        self.sample = sample
        self.name = name
        self.variable =variable
        self.category = category
        self.systematic = systematic
        self.hist = hist

    def __repr__(self):
        return "(name=%r, sample=%r, systematic=%r, "\
            "variable=%r, category=%r, hist=%r)\n"%(
                self.name, self.sample, self.systematic,
                self.variable, self.category, self.hist.Integral() if self.hist else "NAN")
    



##--------------------------------------------------------------------------
## - - helper for Pool processing (looping over events directly; slower!)
##--------------------------------------------------------------------------
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
## - - helper for Pool processing 
##--------------------------------------------------------------------------
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
    hist_templates = hist_worker.hist_templates
    log.debug("*********** processing %s dataset ***********"%dataset.name)
    if not dataset.files:
        log.warning("%s dataset is empty!!"%dataset.name)
        return []

    canvas = ROOT.TCanvas()
    # - - - - containers for hists
    hist_set = []
    hist_templates_tformuals = {} #<! since we have to update hists name, keep tformilas untouched
    for var in fields:
        if var.name in hist_templates:
            hist_templates_tformuals[var.name] = hist_templates[var.name].GetName()
        for category in categories:
            if var.name in hist_templates:
                hist = hist_templates[var.name]
            else:
                hist = ROOT.TH1F(
                    "category_%s_var_%s"%(category.name, var.name), var.name, *var.binning)
                
            hset = Histset(
                name=outname,
                sample=outname,
                variable=var.name,
                category=category.name,
                hist=hist.Clone(), #<! a copy per category 
                systematic=systematic)
            
            # - - make sure the newly created hist has no dummy value
            hset.hist.Reset()
            hist_set.append(hset)
    # - - loop over dataset's files
    nevents = 0
    for fn in dataset.files:
        fname = fn.split("/")[-1]
        tfile = ROOT.TFile(fn)
        # - - check if the file is healthy
        try:
            entries = tfile.Get(systematic).GetEntries()
            nevents += entries
            if entries==0:
                log.warning("%s tree in %s is empty, skipping!"%(systematic, fn))
                continue
        except:
            log.warning("%s has no %s tree!"%(fn, systematic))
            continue
    
        # - - prepares selection categories 
        for category in categories:
            # - - hists for the current category
            cat_hists = filter(lambda hs: hs.category==category.name, hist_set)
            
            # get the tree 
            tree = tfile.Get(systematic)

            # - - get the list of the events that pass the selections
            selection = category.cuts.GetTitle()
            eventweight = "*".join(weights[category.name])
            tree.Draw(">>eventlist_%s"%category.name, selection)
            eventlist = ROOT.gDirectory.Get("eventlist_%s"%category.name)
            tree.SetEventList(eventlist)

            # - - draw all the vars
            for var in fields:
                histname = "category_%s_%s_%s"%(category.name, var.name, fname)
                if var.name in hist_templates:
                    ht = hist_templates[var.name]
                    var_formula = hist_templates_tformuals[var.name]
                    if isinstance(ht, ROOT.TH1F):
                        nbins = ht.GetNbinsX()
                        ht_bins = (nbins, ht.GetBinLowEdge(1), ht.GetBinLowEdge(nbins) + ht.GetBinWidth(1))
                    elif isinstance(ht, ROOT.TH2F):
                        nbins_x = ht.GetNbinsX()
                        ht_x = ht.GetXaxis()
                        ht_bins_x = (nbins_x, ht_x.GetBinLowEdge(1), ht_x.GetBinLowEdge(nbins_x) + ht_x.GetBinWidth(1) )
                        
                        nbins_y = ht.GetNbinsY()
                        ht_y = ht.GetYaxis()
                        ht_bins_y = (nbins_y, ht_y.GetBinLowEdge(1), ht_y.GetBinLowEdge(nbins_y) + ht_y.GetBinWidth(1) )
                        ht_bins = ht_bins_x + ht_bins_y
                            
                    elif isinstance(ht, ROOT.TH3F):
                        nbins_x = ht.GetNbinsX()
                        ht_x = ht.GetXaxis()
                        ht_bins_x = (nbins_x, ht_x.GetBinLowEdge(1), ht_x.GetBinLowEdge(nbins_x) + ht_x.GetBinWidth(1) )
                        
                        nbins_y = ht.GetNbinsY()
                        ht_y = ht.GetYaxis()
                        ht_bins_y = (nbins_y, ht_y.GetBinLowEdge(1), ht_y.GetBinLowEdge(nbins_y) + ht_y.GetBinWidth(1) )
                        
                        nbins_z = ht.GetNbinsZ()
                        ht_z = ht.GetZaxis()
                        ht_bins_z = (nbins_z, ht_z.GetBinLowEdge(1), ht_z.GetBinLowEdge(nbins_z) + ht_z.GetBinWidth(1) )
                        
                        ht_bins = ht_bins_x + ht_bins_y + ht_bins_z
                    else:
                        raise TypeError("ROOT.TH type is required")
                    tree.Draw("{0} >> {1}{2}".format(var_formula, histname, ht_bins), eventweight)
                else:
                    tree.Draw("{0} >> {1}{2}".format(var.tformula, histname, var.binning), eventweight)
                
                log.debug("{0} >> {1}{2}".format(var.tformula, histname, var.binning))
                log.debug("({0}) * ({1})".format(selection, eventweight))

                htmp = ROOT.gDirectory.Get(histname)
                htmp.SetDirectory(0)
                hset = filter(lambda hs: hs.variable==var.name, cat_hists)[0]
                hset.hist.Add(htmp)
                hset.hist.SetName(histname)
                htmp.Delete()
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
    log.info("processed %s tree from %s dataset with %i events"%(systematic, dataset.name, nevents))
    return hist_set

