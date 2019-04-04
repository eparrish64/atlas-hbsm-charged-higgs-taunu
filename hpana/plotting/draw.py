""" draw histograms from a histo file
"""
# ROOT
import ROOT

# stdlib
import re, array

# local
from hpana.plotting.plot import *
from hpana import log

## consts
HIST_NAME_TEMPLATE = re.compile(
    "^(?P<sample>\w+)_category_(?P<category>\w+)_var_(?P<var>\w+)$")

# ----------------------------------------------------------------------------
#
def draw(var, category,
         hists_file=None,
         hists_set=[],
         data=None,
         backgrounds=[],
         signals=[],
         systematics=None,
         tree_name="NOMINAL",
         error_bars=False,
         signal_scale=1.,
         show_signal_error=False,
         plot_label=None,
         ytitle='Events',
         xtitle=None,
         blind=False,
         show_ratio=False,
         output_formats=None,
         logy=False,
         logx=False,
         logy_min=None,
         legend_position='right',
         output_dir=None,
         output_name=None,
         overflow=False,
         show_pvalue=False,
         top_label=None,
         poisson_errors=True,
         ylimits=None,
         bin_optimization=True,
         scale_sig_to_bkg_sum=True,
         integral_in_legends=False,
         ttbar_norm_factor=1,
         wtaunu_norm_factor=1,
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
    if not (hists_set or hists_file):
        raise RuntimeError("either hists file or hists list is required")

    if show_ratio and blind:
        show_ratio = False
    if not (data and backgrounds):
        show_ratio = False

    if not (backgrounds or data or signals):
        raise ValueError(
            "at least one of backgrounds, data or signal must be specified")

    # - - - - - - - - the ratio plot
    if data and category.name in data.blind_regions:
            show_ratio = False

    # - - - - - - - - open hists file
    if hists_file:
        hfile = ROOT.TFile(hists_file, "READ")

    # - - - - - - - - insantiate the legend
    legend = ROOT.TLegend(0.65, 0.75, 0.92, 0.92)
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetTextSize(0.030)

    # - - - - - - - - list of all objects to be drawn
    extra_info = []
    main_errors = []

    # - - - - - - - - binning
    opt_bins = []

    # - - - - - - - - prepare the canvas and pads
    fig, main_pad, ratio_pad = create_canvas(show_ratio=show_ratio)
    if logx:
        main_pad.SetLogx()
        ratio_pad.SetLogx()
        
    # gather histograms
    samples = backgrounds + signals 
    if data:
        samples += [data]

    hists_dict = {}
    for sample in samples:
        hists_dict[sample.name] = {}
        s_hist = None
        for systematic in sample.systematics:
            for syst_var in systematic.variations:
                if hists_file:
                    systdir = hfile.Get(syst_var.name)
                    if not systdir:
                        continue
                    keys = [k.GetName() for k in systdir.GetListOfKeys()]
                    for k in keys:
                        match = re.match(HIST_NAME_TEMPLATE, k)
                        if match:
                            if match.group("sample")==sample.name:
                                if match.group("category")==category.name and match.group("var")==var.name:
                                    s_hist = hfile.Get("%s/%s"%(syst_var.name,k))
                else:
                    for hs in hists_set:
                        if hs.systematic==syst_var.name:
                            if hs.sample==sample.name:
                                if hs.category==category.name:
                                    if hs.variable==var.name:
                                        s_hist =  hs

                if s_hist is None:
                    log.warning("No histogram is found for sample=%s, systematic=%s, category=%s, and field=%s"%(
                        sample.name, syst_var.name, category.name, var.name))
                    continue

                ## rebin histograms 
                if var.plot_bins is not None:
                    if isinstance(var.plot_bins, dict):
                        if category.name in var.plot_bins:
                            bins = var.plot_bins[category.name]
                        else:
                            bins = var.plot_bins["COMMON"]
                    else:
                        bins = var.plot_bins

                    s_hist = s_hist.Rebin(len(bins)-1, "hn", array.array("d", bins))

                ## normalize ttbar bkg
                if ttbar_norm_factor!=1 and sample.name=="TTbar":
                    s_hist.Scale(ttbar_norm_factor)

                ## normalize wtaunu bkg
                if wtaunu_norm_factor!=1 and sample.name=="Wtaunu":
                    s_hist.Scale(wtaunu_norm_factor)

                hists_dict[sample.name][syst_var.name] = s_hist


    log.debug("Retrieved histograms %r"%hists_dict)

    # backgrounds 
    backgrounds_stack = []
    if backgrounds:
        if not isinstance(backgrounds, (list, tuple)):
            backgrounds = [backgrounds]
        # retrieve NOMINAL hists and decorate them
        backgrounds_hists_nom = []
        for bkg in reversed(backgrounds):
            bkg_hist = hists_dict[bkg.name]["NOMINAL"]
            if bkg_hist:
                bkg_hist.SetFillColor(bkg.color) 
                legend.AddEntry(bkg_hist, bkg.label, "F")#, bkg_hist.Integral(0, -1)), 'F')
                backgrounds_hists_nom.append(bkg_hist)

        # all bkg hist (for systematic variations)
        backgrounds_hists_dict = dict((k, hists_dict[k]) for k in [b.name for b in backgrounds])

        # - - - - optimize binning
        hsum = reduce(lambda h1, h2: h1+h2, backgrounds_hists_nom)
        opt_bins = optimize_binning(hsum)

        ## build the bkg stack 
        bkg_stack = ROOT.THStack("bkgs", "bkgs")
        backgrounds_stack = []
        rebinned_bkg_hists = []
        for bkg_hist in backgrounds_hists_nom:
            if opt_bins and bin_optimization:
                hnew = rebin(bkg_hist, opt_bins)
                bkg_stack.Add(hnew)
                rebinned_bkg_hists.append(hnew)
            else:
                bkg_stack.Add(bkg_hist)
        backgrounds_stack.append(bkg_stack)
        if bin_optimization and opt_bins:
            backgrounds_hists = rebinned_bkg_hists[:]

        # - - - - if you wish to add uncertainty band to the ratio plot
        if error_bars:
            total_backgrounds, high_band_backgrounds, low_band_backgrounds = uncertainty_band(
            backgrounds_hists_dict, overflow=overflow)
        
            backgrounds_error = ROOT.TGraphAsymmErrors()
            for i in range(0, total_backgrounds.GetNbinsX()):
                tb_nom_cnt = total_backgrounds.GetBinContent(i)
                backgrounds_error.SetPoint(i, total_backgrounds.GetXaxis().GetBinCenter(i), tb_nom_cnt)

                eyh = high_band_backgrounds.GetBinContent(i)
                eyl = low_band_backgrounds.GetBinContent(i)
                ey = max(eyh, eyl)

                ## dummy x error for plotting
                exh = total_backgrounds.GetXaxis().GetBinWidth(i)/2.
                exl = exh
                backgrounds_error.SetPointError(i, exl, exh, ey, ey)

            backgrounds_error.SetFillStyle(3004)
            backgrounds_error.SetFillColor(ROOT.kRed)

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
            sig_hist = hists_dict[sig.name]["NOMINAL"]
            # - - - - scale signals if needed
            if scale_sig_to_bkg_sum:
                bkg_hsum = reduce(lambda h1, h2: h1+h2, backgrounds_hists_nom)
                sig_hist.Scale(bkg_hsum.Integral(0, -1)/sig_hist.Integral(0, -1))
            if signal_scale!=1.:
                sig_hist *= signal_scale
            init_label = sig.label
            sig_label = "%i #times %s"%(signal_scale, init_label) if signal_scale!=1. else init_label
                
            # - - - - fold the overflow bin to the last bin
            if overflow:
                fold_overflow(sig_hist)
            if bin_optimization and opt_bins:
                rebin(sig_hist, opt_bins)
                
            legend.AddEntry(sig_hist, sig_label, 'L')
            signals_hists.append(sig_hist)

        # - - - - if you want to have signal errors on your plots
        if show_signal_error:
            total_signal, high_band_signal, low_band_signal = uncertainty_band(signals) 
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
        if not category.name in data.blind_regions:
            try:
                data_hist = hists_dict[data.name]["NOMINAL"]
            except KeyError:
                raise RuntimeError("DATA histograms are not available!")

            data_hist.SetXTitle(var.title)
            data_hist.SetYTitle("# events")
            if overflow:
                fold_overflow(data_hist)
            legend.AddEntry(data_hist, data.label, "P")
            if bin_optimization and opt_bins:
                data_hist = rebin(data_hist, opt_bins)
            
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
                if backgrounds_hists_nom:
                    #total_backgrounds = reduce(lambda h1, h2: h1+h2, backgrounds_hists_nom)
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

    if show_ratio:        
        # - - background uncertainty band
        total_backgrounds, high_band_backgrounds, low_band_backgrounds = uncertainty_band(
            backgrounds_hists_dict, overflow=overflow)

        rhist = ratio_hist(data_hist, total_backgrounds)
        rhist.GetXaxis().SetTitle(var.title)
        rhist.GetYaxis().SetTitle('Data/Sum bkg')
        ratio_hist_high = ratio_hist(data_hist, total_backgrounds + high_band_backgrounds)
        ratio_hist_low = ratio_hist(data_hist, total_backgrounds - low_band_backgrounds)

        ratio_error = ROOT.TGraphAsymmErrors()
        for i in range(0, rhist.GetNbinsX()):
            h_cnt = ratio_hist_high.GetBinContent(i)
            l_cnt = ratio_hist_low.GetBinContent(i)
            m_cnt = rhist.GetBinContent(i)

            eyh = max(h_cnt-m_cnt, l_cnt-m_cnt, 0)
            eyl = abs(min(h_cnt-m_cnt, l_cnt-m_cnt, 0))
            ey = max(eyh, eyl)

            # - - dummy x error for plotting
            exh = rhist.GetXaxis().GetBinWidth(i)/2.
            exl = exh

            ratio_error.SetPoint(i, rhist.GetXaxis().GetBinCenter(i), 1)
            ratio_error.SetPointError(i, exl, exh, ey, ey)

        ratio_error.SetMarkerColor(ROOT.kMagenta+2)
        ratio_error.SetMarkerSize(2)
        ratio_error.SetFillColor(ROOT.kMagenta+2)
        ratio_error.SetFillStyle(3001)
            
    # - - - - - - - - add lumi, category , ... labels 
    extra_info += label_plot(main_pad,
                             category=category.label,
                             data_info=(data.info if data else ""),
                             atlas_label=ATLAS_LABEL)
    
    # - - - - - - - - set y axis limit
    ymin = 0 
    ymax = 0
    offset_fact = 1.5
    if logy:
        offset_fact = 1000.
    if ylimits:
        ymin, ymax = ylimits
    elif backgrounds:
        ymax = max(ymax, offset_fact*max([h.GetMaximum() for h in backgrounds_stack]))
    elif data:
        ymax = max(ymax, offset_fact*data_hist.GetMaximum())        
    elif signals:
        ymax = max(ymax, offset_fact*max([h.GetMaximum() for h in signals_hists]))
    if logy:
        # - - - - make sure ymin > 0 for log scale
        if ymin<=0:
            ymin = 0.01
        main_pad.cd()
        main_pad.SetLogy()
                    
    # - - - - - - - - draw bkg hists
    if backgrounds_stack:
        main_pad.cd()
        for h in backgrounds_stack:
            h.SetTitle("")
            h.SetMinimum(ymin)
            h.SetMaximum(ymax)            
            h.Draw("HIST")
            if not show_ratio:
                h.GetYaxis().SetTitle("# of events")
                h.GetXaxis().SetTitle(var.title)
                main_pad.Modified(); fig.Update()
                
    # - -  add on the signals
    if signals:
        main_pad.cd()
        for sig, sh in zip(signals, signals_hists):
            sh.SetTitle("")
            sh.SetMinimum(ymin)
            sh.SetMaximum(ymax + 0.3 *ymax)
            sh.Draw("HIST SAME")
            sh.SetLineColor(sig.color)
            sh.SetLineStyle(sig.hist_decor["line_style"])
            sh.SetLineWidth(2)

    if error_bars and show_ratio:
        # - - - - - - - - draw errors
        for erf in main_errors:
            erf.Draw('SAME E2')


    # - - - - - - - - draw data
    if data:
        if not category.name in data.blind_regions:
            data_hist.SetMarkerSize(1)
            data_hist.SetMarkerStyle(20)
            if backgrounds or signals:
                data_hist.Draw('SAME E1')
            else:
                data_hist.GetYaxis().SetTitle("# of events")
                data_hist.GetXaxis().SetTitle(var.title)
                data_hist.Draw('HIST')
            
    # - - - - - - - - draw extra info
    legend.Draw("SAME")
    for xif in extra_info:
        xif.Draw("SAME")
        
    # - - - - - - - - ratio plot
    if show_ratio:
        ratio_pad.cd()
        rhist.SetTitle("")
        rhist.SetMarkerSize(1)
        rhist.SetMarkerStyle(20)
        rhist.GetYaxis().SetRangeUser(0.8, 1.2)
        rhist.Draw('SAME')
        if error_bars:
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

    ## clean up
    if hists_file:
        hfile.Close()

    fig.Update()

    fig.Close()
    
    return 


