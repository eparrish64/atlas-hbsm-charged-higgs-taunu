
import os, math, array
from contextlib import contextmanager
import threading

import ROOT
from ROOT import TCanvas, TPad, TH1F, TLine
ATLAS_LABEL = 'ATLAS Internal'

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
    path = os.path.dirname(filepath)
    if not os.path.exists(path):
        os.mkdir(path, 0755)

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
    last_bin = hist.GetBinContent(nbins-1) + hist.GetBinContent(nbins)
    hist.SetBinContent(nbins-1, last_bin)
    return 

##----------------------------------------------------------------------------
##
def label_plot(pad, 
               category=None,
               data_info=None, 
               atlas_label=None,
               textsize=22):
    """ to create different labels for the plost
    """

    # draw the category label
    if category:
        rlabel = ROOT.TLatex(
            pad.GetLeftMargin() + 0.45,
            1 - pad.GetTopMargin() - 0.075,
            '#bf{%s}'%category)
        rlabel.SetNDC()
        rlabel.SetTextFont(43)
        rlabel.SetTextSize(textsize-2)
        rlabel.SetTextAlign(31)
        #rlabel.Draw()
    
    # draw the luminosity label
    if data_info is not None:
        dlabel = ROOT.TLatex(
            1. - pad.GetRightMargin(),
            1. - pad.GetTopMargin(),
            str(data_info))
        dlabel.SetNDC()
        dlabel.SetTextFont(43)
        dlabel.SetTextSize(textsize)
        dlabel.SetTextAlign(31)
        #dlabel.Draw()
            
    # # draw the ATLAS label
    if atlas_label:
        alabel = ROOT.TLatex(
            pad.GetLeftMargin() + 0.25,
            1 - pad.GetTopMargin() - 0.075,
            '#bf{#it{%s}}'%ATLAS_LABEL)
        alabel.SetNDC()
        alabel.SetTextFont(43)
        alabel.SetTextSize(textsize+4)
        alabel.SetTextAlign(31)
        #alabel.Draw()

    ## FIX ME: pad Draw doesn't update the pad, needed to return labels!
    pad.Update()
    pad.Modified()
    return [rlabel, dlabel, alabel]

##----------------------------------------------------------------------------
##
def uncertainty_band(hists, systematics, overflow=True):
    
    """
    add separate variations in quadrature,
    also include stat error in quadrature
    
    Parameters
    ----------
    hists = list (dict), holding backgrounds info and hists
    systematics:list, list of analysis systematics.
    
    Returns
    -------
    total_backgrounds, high_band, low_band: ROO.TH1F, 
    corrsponding to total nom, low band and high band error
    """

    if not isinstance(hists, (list, tuple)):
        hists = [hists]
    total_nom = reduce(lambda h1, h2: h1+h2, hists) 
    
    var_high = []
    var_low = []

    # include stat errors too
    total_model_stat_high = total_nom.Clone()
    total_model_stat_low = total_nom.Clone()
    for i in range(0, total_nom.GetNbinsX()):
        total_model_stat_high.SetBinContent(
            i, total_model_stat_high.GetBinContent(i) + total_nom.GetBinErrorUp(i))
        total_model_stat_low.SetBinContent(
            i, total_model_stat_low.GetBinContent(i) + total_nom.GetBinErrorLow(i))

    var_high.append(total_model_stat_high)
    var_low.append(total_model_stat_low)

    if systematics is not None:
        for syst, variations in systematics.items():
            if len(variations) == 2:
                high, low = variations
            elif len(variations) == 1:
                high = variations[0]
                low = 'NOMINAL'
            else:
                raise ValueError(
                    "only one or two variations "
                    "per term are allowed: {0}".format(syst))

            if high == 'NOMINAL' and low == 'NOMINAL':
                continue

            total_high = total_nom.Clone()
            total_high.Reset()
            total_low = total_high.Clone()
            total_max = total_high.Clone()
            total_min = total_high.Clone()
            for model in hists:
                mname = model.keys()[0]
                m_obj = model[mname]['INFO']
                nom_hist = model[m_obj.name]['HISTS']['NOMINAL']
                syst_hists = model[m_obj.name]['HISTS'][syst] #<! (UP, DOWN)
            
                if overflow:
                    [fold_overflow(sh) for sh in syst_hists]
                if high == 'NOMINAL':
                    total_high += nom_hist
                else:
                    ## retrieve the high syst componet hist
                    total_high += syst_hists[0]

                if low == 'NOMINAL':
                    total_low += nom_hist
                else:
                    ## retrieve the low syst componet hist
                    total_low += syst_hists[1]
                
            if total_low.Integral() <= 0:
                log.warning("{0} is non-positive".format(syst))
            if total_high.Integral() <= 0:
                log.warning("{0} is non-positive".format(syst))
    
            ## find min, max bin by bin
            for i in range(0, total_high.GetNbinsX()):
                total_max.SetBinContent(i, max(total_high.GetBinContent(i), 
                                               total_low.GetBinContent(i), 
                                               total_nom.GetBinContent(i)))
            
                total_min.SetBinContent(i, min(total_high.GetBinContent(i), 
                                               total_low.GetBinContent(i), 
                                               total_nom.GetBinContent(i)))

            if total_min.Integral() <= 0:
                log.warning("{0}_DOWN: lower bound is non-positive".format(syst))
            if total_max.Integral() <= 0:
                log.warning("{0}_UP: upper bound is non-positive".format(syst))

            var_high.append(total_max)
            var_low.append(total_min)

            log.debug("{0} {1}".format(str(syst), str(variations)))
            log.debug("{0} {1} {2}".format(
                    total_max.Integral(),
                    total_nom.Integral(),
                    total_min.Integral()))
    
            pass #<! syst loop

        pass #<! if systematics 

    # sum variations in quadrature bin-by-bin
    high_band = total_nom.Clone()
    high_band.Reset()
    low_band = high_band.Clone()
    for i in range(0, high_band.GetNbinsX()):
        sum_high = math.sqrt(
            sum([(v.GetBinContent(i) - total_nom.GetBinContent(i))**2 for v in var_high]))
        sum_low = math.sqrt(
            sum([(v.GetBinContent(i) - total_nom.GetBinContent(i))**2 for v in var_low]))
        high_band.SetBinContent(i, sum_high)
        low_band.SetBinContent(i, sum_low)

    return total_nom, high_band, low_band
            

##----------------------------------------------------------------------------
##
def create_canvas(show_ratio=True):
    c = TCanvas("c", "canvas", 800, 800)
    if show_ratio:
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
    else:
        pad1 = TPad("pad1", "pad1", 0, 0.1, 1, 1.0)
        pad1.SetBottomMargin(0.2)  #<! joins upper and lower plot
        pad1.Draw()

        pad2 = None
    return c, pad1, pad2

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
            ratio_hist.SetBinContent(i, 1)
            
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
    ratio_hist.GetYaxis().SetRangeUser(0.5, 1.5)
    
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
