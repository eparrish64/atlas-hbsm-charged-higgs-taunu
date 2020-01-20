## stdlib
import os, math, array
from contextlib import contextmanager
import threading

## local
from hpana import log

## ROOT
import ROOT
from ROOT import TCanvas, TPad, TH1F, TLine
ATLAS_LABEL = ''

__all__= [
    'SimplePlot',
    'RatioPlot',
    "uncertainty_band",
    "label_plot",
    "save_canvas",
    "fold_overflow",
    "create_canvas",
    "ratio_hist",
    "ATLAS_LABEL",
    "optimize_binning",
    "rebin",
]

"""
* Note about locks: we dont need this in cases where ROOT has a
* thread-specific variable, so gDirectory and gPad are safe.  Not so for
* gStyle, IsBatch and TH1.AddDirectory, so we use a lock in these
* cases. To prevent out-of-order lock grabbing, just use one reentrant
* lock for all of them.
"""
LOCK = threading.RLock()

##----------------------------------------------------------------------------
##
@contextmanager
def preserve_current_canvas():
    """
    Context manager which ensures that the current canvas remains the
    current canvas when the context is left.
    """
    old = ROOT.gPad.func()
    try:
        yield
    finally:
        if old:
            old.cd()
        elif ROOT.gPad.func():
            # Put things back how they were before.
            with invisible_canvas():
                # This is a round-about way of resetting gPad to None.
                # No other technique I tried could do it.
                pass


##----------------------------------------------------------------------------
##
@contextmanager
def preserve_batch_state():
    """
    Context manager which ensures the batch state is the same on exit
    as it was on entry."""
    with LOCK:
        old = ROOT.gROOT.IsBatch()
        try:
            yield
        finally:
            ROOT.gROOT.SetBatch(old)


##----------------------------------------------------------------------------
##
@contextmanager
def invisible_canvas():
    """
    Context manager yielding a temporary canvas drawn in batch mode,
    invisible to the user. Original state is restored on exit.
    Example use; obtain X axis object without interfering with
    anything:: with invisible_canvas() as c: efficiency.Draw() g =
    efficiency.GetPaintedGraph() return g.GetXaxis()
    """
    with preserve_current_canvas():
        with preserve_batch_state():
            ROOT.gROOT.SetBatch()
            c = ROOT.TCanvas()
        try:
            c.cd()
            yield c
        finally:
            c.Close()
            c.IsA().Destructor(c)



##----------------------------------------------------------------------------
##
class SimplePlot(ROOT.TCanvas):
    def __init__(self,
                 width=None,
                 height=None,
                 xtitle=None,
                 ytitle=None,
                 tick_length=15,
                 logy=False):

        super(SimplePlot, self).__init__()
        left, right = self.GetLeftMargin(), self.GetRightMargin()
        bottom, top = self.GetBottomMargin(), self.GetTopMargin() 
        self.SetMargin(0, 0, 0, 0)
        self.SetName('main')
        
        # top pad for histograms
        with self:
            main = ROOT.TPad('main', 'main', 0., 0., 1., 1.)
            if logy:
                main.SetLogy()
            main.SetMargin = (left, right, bottom, top)
            main.Draw()
        
        #draw axes
        try:
            main_hist = ROOT.TH1F('h', 'h', 1, 0, 1)
            main_hist.Draw('AXIS')
        finally:
            main.Close()
        if xtitle is not None:
            main_hist.GetXaxis().SetTitle(xtitle)
        if ytitle is not None:
            main_hist.GetYaxis().SetTitle(ytitle)

        # set the tick lengths
        # tick_length_pixels(main, main_hist.xaxis, main_hist.yaxis,
        #                    tick_length)

        self.main = main
        #self.main_hist = main_hist
        self.logy = logy
        
    def pad(self, region):
        if region == 'main':
            return self.main
        raise ValueError("SimplePlot region {0} does not exist".format(region))

    def cd(self, region=None):
        if region is not None:
            self.pad(region).cd()
        else:
            super(SimplePlot, self).cd()

    def axes(self, region):
        if region == 'main':
            return self.main_hist.GetXaxis(), self.main_hist.GetYaxis()
        raise ValueError("SimplePlot region {0} does not exist".format(region))
    
    def __enter__(self):
        self._prev_pad = ROOT.gPad.func()
        self.cd()
        return self

    def __exit__(self, type, value, traceback):
        if self._prev_pad:
            self._prev_pad.cd()
        elif ROOT.gPad.func():
            # Put things back how they were before.
            with invisible_canvas():
                # This is a round-about way of resetting gPad to None.
                # No other technique I tried could do it.
                pass
        self._prev_pad = None
        return False



##----------------------------------------------------------------------------
##
class RatioPlot(TCanvas):

    def __init__(self, width=None, height=None,
                 offset=0,
                 ratio_height=None, ratio_margin=26,
                 ratio_limits=(0, 2), ratio_divisions=4,
                 prune_ratio_ticks=False,
                 ratio_line_values=(1,),
                 ratio_line_width=2,
                 ratio_line_style='dashed',
                 xtitle=None, ytitle=None, ratio_title=None,
                 tick_length=15,
                 logy=False):

        # first init as normal canvas
        super(RatioPlot, self).__init__(width=width, height=height)

        # get margins 
        left, right, bottom, top = self.GetMargin()
        default_height = self.GetWindowHeight()
        default_frame_height = default_height - bottom - top

        if ratio_height is None:
            ratio_height = default_height / 4.

        self.height += int(ratio_height) + ratio_margin + offset
        self.SetMargin = (0, 0, 0, 0)

        main_height = default_frame_height + top + ratio_margin / 2. + offset
        ratio_height += ratio_margin / 2. + bottom

        # top pad for histograms
        with self:
            main = TPad(0., ratio_height / self.height, 1., 1.)
            if logy:
                main.SetLogy()
            main.SetMargin = (left, right, ratio_margin / 2., top)
            main.Draw()

        # bottom pad for ratio plot
        with self:
            ratio = TPad(0, 0, 1, ratio_height / self.height)
            ratio.SetMargin = (left, right, bottom, ratio_margin / 2.)
            ratio.Draw()

        # draw main axes
        with main:
            main_hist = TH1F(1, 0, 1)
            main_hist.Draw('AXIS')

        # hide x-axis labels and title on main pad
        xaxis, yaxis = main_hist.GetXaxis(), main_hist.GetYaxis()
        xaxis.SetLabelOffset(1000)
        xaxis.SetTitleOffset(1000)
        # adjust y-axis title spacing
        yaxis.SetTitleOffset(
            yaxis.GetTitleOffset() * self.height / default_height)

        # draw ratio axes
        with ratio:
            ratio_hist = TH1F(1, 0, 1)
            ratio_hist.Draw('AXIS')

        # adjust x-axis label and title spacing
        xaxis, yaxis = ratio_hist.GetXaxis(), ratio_hist.GetYaxis()
        xaxis.SetLabelOffset(
            xaxis.GetLabelOffset() * self.height / ratio_height)
        xaxis.SetTitleOffset(
            xaxis.GetTitleOffset() * self.height / ratio_height)

        # adjust y-axis title spacing
        yaxis.SetTitleOffset(
            yaxis.GetTitleOffset() * self.height / default_height)

        if ratio_limits is not None:
            low, high = ratio_limits
            if prune_ratio_ticks:
                delta = 0.01 * (high - low) / float(ratio_divisions % 100)
                low += delta
                high -= delta
            yaxis.SetLimits(low, high)
            yaxis.SetRangeUser(low, high)
            yaxis.SetNdivisions(ratio_divisions)

        if xtitle is not None:
            ratio_hist.GetXaxis().SetTitle(xtitle)
        if ytitle is not None:
            main_hist.GetYaxis().SetTitle(ytitle)
        if ratio_title is not None:
            ratio_hist.GetYAxis().SetTitle(ratio_title)

        # # set the tick lengths
        # tick_length_pixels(main, main_hist.xaxis, main_hist.yaxis,
        #                    tick_length)
        # tick_length_pixels(ratio, ratio_hist.xaxis, ratio_hist.yaxis,
        #                    tick_length)

        # draw ratio lines
        lines = []
        if ratio_line_values:
            with ratio:
                for value in ratio_line_values:
                    line = TLine(0, value, 1, value)
                    line.SetLineStyle(ratio_line_style)
                    line.SetLineWidth(ratio_line_width)
                    line.Draw()
                    lines.append(line)
        self.lines = lines

        self.main = main
        self.main_hist = main_hist
        self.ratio = ratio
        self.ratio_hist = ratio_hist
        self.ratio_limits = ratio_limits
        self.logy = logy

    def pad(self, region):
        if region == 'main':
            return self.main
        elif region == 'ratio':
            return self.ratio
        raise ValueError("RatioPlot region {0} does not exist".format(region))

    def cd(self, region=None):
        if region is not None:
            self.pad(region).cd()
        else:
            super(RatioPlot, self).cd()

    def axes(self, region):
        if region == 'main':
            return self.main_hist.xaxis, self.main_hist.yaxis
        elif region == 'ratio':
            return self.ratio_hist.xaxis, self.ratio_hist.yaxis
        raise ValueError("RatioPlot region {0} does not exist".format(region))

    def update_lines(self):
        x, y = self.axes('ratio')
        # update ratio line lengths
        for line in self.lines:
            line.SetX1(x.GetXmin())
            line.SetX2(x.GetXmax())





##----------------------------------------------------------------------------
##
def save_canvas(canvas, directory, name, formats=None):
    # save plots to disk 
    filepath = os.path.join(directory, name)
    if not os.path.isdir(directory):
        os.mkdir(directory, 0755)

    if formats is not None:
        if isinstance(formats, basestring):
            formats = formats.split()
        for fmt in formats:
            if fmt[0] != '.':
                fmt = '.' + fmt
            canvas.SaveAs(filepath + fmt)
    else:
        canvas.SaveAs(filepath)

##----------------------------------------------------------------------------
##
def fold_overflow(hist):
    nbins = hist.GetNbinsX()
    first_bin = hist.GetBinContent(0) + hist.GetBinContent(1)  
    hist.SetBinContent(1, first_bin)
    last_bin = hist.GetBinContent(nbins+1) + hist.GetBinContent(nbins)
    hist.SetBinContent(nbins-1, last_bin)
    return 

##----------------------------------------------------------------------------
##
def label_plot(pad, 
               category="",
               data_info="#sqrt{13} TeV Data", 
               atlas_label=ATLAS_LABEL,
               textsize=20):
    """ to create different labels for the plost
    """

    ## selection region label    
    rlabel = ROOT.TLatex(
        pad.GetLeftMargin() + 0.05,
        1 - pad.GetTopMargin() - 0.16,
        '#bf{%s}'%category)
    rlabel.SetNDC()
    rlabel.SetTextFont(43)
    rlabel.SetTextSize(textsize-2)
    rlabel.SetTextAlign(ROOT.kHAlignLeft)
    
    ## lumi label
    dlabel = ROOT.TLatex(
        pad.GetLeftMargin() + 0.05,
        1 - pad.GetTopMargin() - 0.12,
        str(data_info))
    dlabel.SetNDC()
    dlabel.SetTextFont(43)
    dlabel.SetTextSize(textsize-2)
    dlabel.SetTextAlign(ROOT.kHAlignLeft)
            
    ## the ATLAS label
    alabel = ROOT.TLatex(
        pad.GetLeftMargin() + 0.05,
        1 - pad.GetTopMargin() - 0.05,
        '#bf{#it{%s}}'%atlas_label)
    alabel.SetNDC()
    alabel.SetTextFont(43)
    alabel.SetTextSize(textsize+6)
    alabel.SetTextAlign(ROOT.kHAlignLeft)

    return [rlabel, dlabel, alabel]

##----------------------------------------------------------------------------
##
def uncertainty_band(hists_dict, overflow=True):
    
    """
    add separate variations in quadrature,
    also include stat error in quadrature
    
    Parameters
    ----------
    hists = dict, holding backgrounds info and hists
    
    Returns
    -------
    total_backgrounds, high_band, low_band: ROO.TH1F, 
    corrsponding to total nom, low band and high band error
    """

    ## explicit copy and don't touch the original hists
    hists_dict = dict(hists_dict) 

    ## get list of the samples 
    samples = hists_dict.keys()

    ## get all the systematics
    systematics = []
    for sample in samples:
        for st in hists_dict[sample].keys():
            if not st in systematics:
                systematics += [st]

    ## retrieve the total nominal/syst hists and aggregate them if needed
    total_nom = hists_dict[samples[0]]["NOMINAL"].Clone()
    
    #skip first entry, as it is already accounted for by initial clone
    for s in samples[1:]:
        total_nom.Add(hists_dict[s]["NOMINAL"])

    for syst in systematics:
        total_syst = total_nom.Clone()
        total_syst.Reset()
        for s in samples:
            if syst in hists_dict[s]:
                total_syst.Add(hists_dict[s][syst])
            else:
                total_syst.Add(hists_dict[s]["NOMINAL"]) 

        if not "TOTAL" in hists_dict:
            hists_dict["TOTAL"] = {}
        hists_dict["TOTAL"][syst] = total_syst

    ## containers for the variations 
    var_high = {}
    var_low = {}

    ## include stat errors 
    for i in range(1, total_nom.GetNbinsX()+1):
        bkey = "BIN%i"%i
        if not bkey in var_high:
            var_high[bkey] = []
        if not bkey in var_low:
            var_low[bkey] = []

        var_high[bkey] += [total_nom.GetBinErrorUp(i)]
        var_low[bkey] += [total_nom.GetBinErrorLow(i)] 

    ## deal with the systematics 
    if len(systematics) > 1:
        total_high = total_nom.Clone()
        total_high.Reset()
        total_low = total_high.Clone()
        total_max = total_high.Clone()
        total_min = total_high.Clone()
        
        for syst in systematics:
            for i in range(1, total_nom.GetNbinsX()+1):
                bkey = "BIN%i"%i
            
                ## get bin variation 
                bnom = total_nom.GetBinContent(i)

                ## be extra cautious 
                if bnom==0:
                    continue
                if math.isnan(bnom) or math.isinf(bnom):
                    log.warning(
                        "Content of bin %i is %r while a float is expected; check %s histogram; skipping this bin!"%(i, bnom, total_nom.GetName()))
                    continue
                bvar = bnom - hists_dict["TOTAL"][syst].GetBinContent(i)
                if math.isnan(bvar) or math.isinf(bvar):
                    log.warning(
                        "Content of bin %i is %r while a float is expected; check %s histogram; skipping this bin!"%(i, bvar, hists_dict["TOTAL"][syst].GetName()))
                    continue

                ## spot suspiciously larg variations  
                var_pcnt = (abs(bvar)/bnom) * 100
                if  var_pcnt> 200 and bnom > 10:
                    log.warning("Suspiciously large variation for %s: %i%%; check %s histogram; skipping!"%(syst, var_pcnt, hists_dict["TOTAL"][syst].GetName()))
                    continue

                if bvar > 0:
                    var_low[bkey] += [bvar]
                else:
                    var_high[bkey] += [bvar]

    # sum variations in quadrature bin-by-bin
    high_band = total_nom.Clone()
    high_band.Reset()
    low_band = high_band.Clone()
    for i in range(1, high_band.GetNbinsX()+1):
        bkey="BIN%i"%i
        sum_high = math.sqrt(sum([v**2 for v in var_high[bkey]]))
        sum_low = math.sqrt(sum([v**2 for v in var_low[bkey]]))

        high_band.SetBinContent(i, sum_high)
        low_band.SetBinContent(i, sum_low)
    return total_nom, high_band, low_band
            

##----------------------------------------------------------------------------
##
def create_canvas(show_ratio=True):
    if show_ratio:
        c = TCanvas("c", "canvas", 800, 800)
        # - - - - Upper histogram plot is pad1
        pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        pad1.SetBottomMargin(0.15)  #<! joins upper and lower plot
        pad1.Draw()
    
        # - - - - Lower ratio plot is pad2
        c.cd()  #<! returns to main canvas before defining pad2
        pad2 = TPad("pad2", "pad2", 0, 0.1, 1, 0.35)
        pad2.SetTopMargin(0.1)  # joins upper and lower plot
        pad2.SetBottomMargin(0.25)
        pad2.SetGridy()
        pad2.Draw()
        return c, pad1, pad2 

    c = TCanvas("c", "canvas", 700, 600)
    pad1 = TPad("pad1", "pad1", 0, 0, 1, 1)
    pad1.Draw()
    return c, pad1, None

##----------------------------------------------------------------------------
##
def ratio_hist(h1, h2):

    h1.Sumw2()
    h2.Sumw2()
    ratio_hist = h1.Clone()
    ratio_hist.Divide(h2)
    
    # - - - - remove bins where data is zero
    for i in range(0, h1.GetNbinsX()):
        if h1.GetBinContent(i) <= 0:
            ratio_hist.SetBinContent(i, -1)
            
    ratio_hist.GetXaxis().SetLabelFont(43)
    ratio_hist.GetXaxis().SetLabelSize(16)
    ratio_hist.GetXaxis().SetLabelOffset(0.02)
    ratio_hist.GetXaxis().SetTitleFont(43)
    ratio_hist.GetXaxis().SetTitleSize(16)
    ratio_hist.GetXaxis().SetTitleOffset(5)
    ratio_hist.GetXaxis().SetTickLength(0.2)
    
    ratio_hist.GetYaxis().SetLabelFont(43)
    ratio_hist.GetYaxis().SetLabelSize(16)
    ratio_hist.GetYaxis().SetLabelOffset(0.01)
    ratio_hist.GetYaxis().SetTitleFont(43)
    ratio_hist.GetYaxis().SetTitleSize(16)
    ratio_hist.GetYaxis().SetTitleOffset(1.8)
    ratio_hist.GetYaxis().SetRangeUser(0.2, 1.8)
    return ratio_hist 

##----------------------------------------------------------------------------
##
def optimize_binning(hist):
    """
    rebin histogram 
    """

    nbins = hist.GetNbinsX()
    axis = hist.GetXaxis()
    new_bins = []
    i = 1
    x0 = hist.GetBinLowEdge(1) 
    dx = hist.GetBinWidth(1)
    while i <= nbins:
        y = hist.GetBinContent(i)
        if y <=10:
            i += 1
            continue
        else:
            new_bins.append(x0 + i*dx)
            i +=1
            
    new_bins.insert(0, hist.GetBinLowEdge(1)) #<! include underflow bin
    return new_bins

##----------------------------------------------------------------------------
##
def rebin(hist, bins):
    return hist.Rebin(len(bins)-1, hist.GetTitle(), array.array("d", bins))
