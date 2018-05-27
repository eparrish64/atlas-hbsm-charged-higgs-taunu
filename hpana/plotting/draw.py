""" draw histograms from a histo file
"""
## ROOT
import ROOT

## local
from .plot import *
from .. import log


##----------------------------------------------------------------------------
##
def draw(hists_file, var, category, 
         data=None,
         backgrounds=[],
         signals=[],
         systematics=None,
         tree_name="NOMINAL",
         uncertainty_band=False,
         signal_scale=1.,
         show_signal_error=False,
         plot_label=None,
         ytitle='Events',
         xtitle=None,
         blind=False,
         show_ratio=False,
         output_formats=None,
         logy=False,
         logy_min=None,
         legend_position='right',
         output_dir=None,
         output_name=None,
         overflow=True,
         show_pvalue=False,
         top_label=None,
         poisson_errors=True,
         ylimits=None,
         ):

    """
    Parameters
    ----------
    hists_file:
        str; path of the file containing histograms
    data: 
        Analysis.data type; see ../analysis.py  
    backgrounds:
        Analysis.backgrounds; see ../analysis.py
    signals:
        Analysis.signals; see ../analysis.py
    ...

    Returns 
    -------
    fig: TCanvas, containing the plots.
    """
        
    if show_ratio and blind:
        show_ratio = False
    if not (data and backgrounds):
        show_ratio = False
        
    if not (backgrounds or data or signals):
        raise ValueError(
            "at least one of backgrounds, data or signal must be specified")

    # - - - - - - - - open hists file
    hfile = ROOT.TFile(hists_file, "READ")

    # - - - - - - - - insantiate the legend 
    legend = ROOT.TLegend(0.6, 0.75, 0.9, 0.9)
    legend.SetNColumns(2)
    legend.SetBorderSize(1)
    legend.SetFillColor(0)
    legend.SetTextSize(0.025)

    # - - - - - - - - list of all objects to be drawn
    extra_info = []
    main_hists = []
    main_errors = []

    # - - - - - - - - prepare the canvas and pads 
    fig, main_pad, ratio_pad = create_canvas(show_ratio=show_ratio)

    # - - - - - - - - backgrounds 
    if backgrounds:
        if not isinstance(backgrounds, (list, tuple)):
            backgrounds = [backgrounds]
        backgrounds_hists   = []
        bkg_stack = ROOT.THStack("bkgs", "bkgs")
        for bkg in reversed(backgrounds):
            bkg_hist = hfile.Get("{0}/{1}_category_{2}_{3}".format(
                tree_name, bkg.name, category.name, var.name))
            # - - - -  fold the overflow bin 
            if overflow:
                fold_overflow(bkg_hist)
            # - - - - hists should already be decorated when they're produced !
            bkg_hist.SetFillColor(bkg.color) 
            legend.AddEntry(bkg_hist, bkg.label, 'F')
            bkg_stack.Add(bkg_hist)
            backgrounds_hists.append(bkg_hist)
        main_hists.append(bkg_stack)
        
        # - - - - if you wish to add uncertainty band to the ratio plot
        if uncertainty_band:
            total_backgrounds, high_band_backgrounds, low_band_backgrounds = uncertainty_band(
                backgrounds, systematics, overflow=overflow)
        
            backgrounds_error = ROOT.TGraphAsymmErrors()
            for i in range(0, total_backgrounds.GetNbinsX()):
                backgrounds_error.SetPoint(i, total_backgrounds.GetXaxis().GetBinCenter(i), 
                                           total_backgrounds.GetBinContent(i))

                eyh = high_band_backgrounds.GetBinContent(i)
                eyl = low_band_backgrounds.GetBinContent(i)
                ## dummy x error for plotting
                exh = total_backgrounds.GetXaxis().GetBinWidth(i)/2.
                exl = exh
                backgrounds_error.SetPointError(i, exl, exh, eyl, eyh)

            backgrounds_error.SetFillColor(ROOT.kYellow-1)
            backgrounds_error.SetFillStyle(3004)
            main_errors.append(backgrounds_error)

            eleg = 'Stat+Syst' 
            if not systematics:
                eleg = 'Stat'
            legend.AddEntry(backgrounds_error, eleg ,'F')
        
    # - - - - - - - - signals
    if signals:
        if not isinstance(signals, (list, tuple)):
            signals = [signals]
        signals_hists   = []
        for sig in signals:
            sig_hist = hfile.Get("{0}/{1}_category_{2}_{3}".format(
                tree_name, bkg.name, category.name, var.name))

            # - - - - scale signals if needed 
            if signal_scale!=1.:
                sig_hist *= signal_scale
                sig.label = "%0.2f #times %s"%(signal_scale, sig.label)
                
            #- - - - fold the overflow bin to the last bin
            if overflow:
                fold_overflow(sig_hist)
                
            sig_hist.SetFillColor(sig.color)
            legend.AddEntry(sig_hist, sig.label, 'L')
            signals_hists.append(h_nom)
        main_hists += signals_hists

        # - - - - if you want to have signal errors on your plots
        if show_signal_error:
            total_signal, high_band_signal, low_band_signal = uncertainty_band(
                signal, systematics) 
            high = (total_signal + high_band_signal) * signal_scale
            low = (total_signal - low_band_signal) * signal_scale
            
            signal_error = ROOT.TGraphErrors()
            for i in range(0, total_signal.GetNbinsX()):
                signal_error.SetPoint(i, total_signal.GetXaxis().GetBinCenter(i), 
                                      total_total_signal.GetBinContent(i))
                signal_error.SetPointError(i, 0, total_signal.GetBinError(i))
        
            signal_error.SetFillColor(ROOT.kYellow-1)
            signal_error.SetFillStyle(3004)
            main_errors.append(signal_error)
                
    # - - - - - - - - data
    if data:
        data_hist = hfile.Get("{0}/{1}_category_{2}_{3}".format(
            tree_name, data.name, category.name, var.name))
        data_hist.SetXTitle(var.title)
        data_hist.SetYTitle("# events")
        if overflow:
            fold_overflow(data_hist)
        legend.AddEntry(data_hist, data.label, "P")
        
        # - - - - - - - - blind the data in a specific range
        if isinstance(blind, tuple):
            low, high = blind
            # - - - - zero out bins in blind category
            for i in range(0, data_hist.GetNbinsX()):
                bin_low  = data_hist.GetBinLowEdge(i)
                bin_high = bin_low + data_hist.GetBinWidth(i) 
                if (low < bin_low <= high or low <= bin_high < high):
                    data_hist.SetBinContent(i, -100)
        
        # - - -  - chi2 test info on plots
        if not blind:
            if backgrounds:
                total_backgrounds = reduce(lambda h1, h2: h1+h2, backgrounds_hists)
                if show_pvalue:
                    # show p-value and chi^2
                    pvalue = total_backgrounds.Chi2Test(data_hist, 'WW')
                    pvalue_label = ROOT.TLatex(
                        fig.GetLeftMargin() + 0.01,
                        1 - fig.GetTopMargin(),
                        "p-value={0:.2f}".format(pvalue))
                    pvalue_label.SetNDC(True)
                    pvalue_label.SetTextFont(43)
                    pvalue_label.SetTextSize(16)
                    extra_info.append(pvalue_label)

                    chi2 = total_backgrounds.Chi2Test(data_hist, 'WW CHI2/NDF')
                    chi2_label = ROOT.TLatex(
                        fig.GetLeftMargin() + 0.15,
                        1 - fig.GetTopMargin(),
                        "#chi^{{2}}/ndf={0:.2f}".format(chi2))
                    chi2_label.SetNDC(True)
                    chi2_label.SetTextFont(43)
                    chi2_label.SetTextSize(16)
                    extra_info.append(chi2_label)

    # - - - - - - - - the ratio plot
    if show_ratio:
        sum_bkgs = reduce(lambda h1, h2: h1+h2, backgrounds_hists)
        rhist = ratio_hist(data_hist, sum_bkgs)
        rhist.GetXaxis().SetTitle(var.title)
        rhist.GetYaxis().SetTitle('Data/Sum bkg')

        # - - - - draw band below points on ratio plot
        if uncertainty_band:
            # - - background uncertainty band
            total_backgrounds, high_band_backgrounds, low_band_backgrounds = uncertainty_band(
                backgrounds, systematics, overflow=overflow)
            ratio_hist_high = total_backgrounds + high_band_backgrounds
            ratio_hist_high.Divide(total_backgrounds)

            ratio_hist_low = total_backgrounds - low_band_backgrounds
            ratio_hist_low.Divide(total_backgrounds)

            ratio_error = ROOT.TGraphAsymmErrors()
            for i in range(0, ratio_hist.GetNbinsX()):
                ratio_error.SetPoint(i, ratio_hist.GetXaxis().GetBinCenter(i), 
                                     ratio_hist.GetBinContent(i))

                eyh = abs(ratio_hist_high.GetBinContent(i) - ratio_hist.GetBinContent(i))
                eyl = abs(ratio_hist.GetBinContent(i) - ratio_hist_low.GetBinContent(i))
                # - - dummy x error for plotting
                exh = ratio_hist.GetXaxis().GetBinWidth(i)/2.
                exl = exh
                ratio_error.SetPointError(i, exl, exh, eyl, eyh)

            ratio_error.SetFillColor(ROOT.kYellow-1)
            ratio_error.SetFillStyle(3004)
    
    # - - - - - - - - add lumi, category , ... labels 
    extra_info += label_plot(main_pad,
                             category=category.label,
                             data_info=(data.info if data else ""),
                             atlas_label=ATLAS_LABEL)
    
    # - - - - - - - - set y axis limit
    if ylimits:
        ymin, ymax = ylimits
    else:
        ymax = max([h.GetMaximum() for h in main_hists])
        ymin = min([h.GetMinimum() for h in main_hists])

    # - - - - - - - - draw hists
    main_pad.cd()
    for h in main_hists:
        h.SetMinimum(ymin)
        h.SetMaximum(ymax + 0.3 *ymax)
        h.Draw("HIST")
        if not show_ratio:
            if isinstance(h, ROOT.THStack):
                h.GetHistogram().GetXaxis().SetTitle(var.title)
            
    # - - - - - - - - draw errors
    for erf in main_errors:
        erf.Draw('SAME E2')

    # - - - - - - - - draw data
    if data:
        data_hist.Draw('SAME E1')

    legend.Draw("SAME")

    # - - - - - - - - draw extra info
    for xif in extra_info:
        xif.Draw("SAME")
    
    # - - - - - - - - ratio plot
    if show_ratio:
        ratio_pad.cd()
        rhist.Draw('SAME')
        if uncertainty_band:
            ratio_error.Draw('SAME E2')
    
    # - - - - - - - - create outputs
    if output_name is None:
        output_name = var.name
        output_name +='_%s'%category.name
    if logy:
        output_name += '_logy'
    if output_formats is None:
        output_formats = ('png',)
        
    # - - - - - - - -save the figure
    if output_dir is None:
        output_dir = "./plots"
    save_canvas(fig, output_dir, output_name, formats=output_formats)

    #- - - - - - - - release the memory
    hfile.Close()
    fig.Update()

    fig.Close()
    
    return 


