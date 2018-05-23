
## std-lib
import math, os

## ROOT
import ROOT

## local
from . import SYSTEMATICS_TAUJET, ATLAS_LABEL, log
from .variables import VARIABLES as VARS

##------------------------------------------------------
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

##------------------------------------------------------
def fold_overflow(hist):
    nbins = hist.GetNbinsX()
    first_bin = hist.GetBinContent(0) + hist.GetBinContent(1)  
    hist.SetBinContent(1, first_bin)
    last_bin = hist.GetBinContent(nbins-1) + hist.GetBinContent(nbins)
    hist.SetBinContent(nbins-1, last_bin)
    return 

##------------------------------------------------------
def label_plot(pad, 
               region_label=None,
               data_info=None, 
               atlas_label=None,
               textsize=22):
    """ to create different labels for the plost
    """

    # draw the category label
    if region_label:
        rlabel = ROOT.TLatex(
            pad.GetLeftMargin() + 0.45,
            1 - pad.GetTopMargin() - 0.075,
            '#bf{%s}'%region_label)
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
    #pad.Update()
    #pad.Modified()
    return rlabel, dlabel, alabel

##------------------------------------------------------
def uncertainty_band(models, systematics, overflow=True):
    
    """
    add separate variations in quadrature,
    also include stat error in quadrature
    
    Parameters
    ----------
    models = list (dict), holding backgrounds info and hists
    systematics:list, list of analysis systematics.
    
    Returns
    -------
    total_backgrounds, high_band, low_band: ROO.TH1F, 
    corrsponding to total nom, low band and high band error
    """

    if not isinstance(models, (list, tuple)):
        models = [models]

    ## nom hists
    nom_hists = []
    for model in models:
        mname = model.keys()[0]
        m_obj = model[mname]['INFO']
        nom_hists.append(model[m_obj.name]['HISTS']['NOMINAL'])

    if overflow:
        [fold_overflow(h) for h in nom_hists]

    total_nom = reduce(lambda h1, h2: h1+h2,nom_hists) 
    
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
            for model in models:
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

##------------------------------------------------------
def draw(var,
         data=None,
         backgrounds=None,
         signals=None,
         systematics=None,
         region='TTBar', 
         signal_scale=1.,
         show_signal_error=False,
         stack_signal=True,
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
    data: dict; holding data info and hists
    backgrounds: list of bkg dicts, holding bkg info and hists 
    signals: list of signal dicts, holding signal info and hists

    Returns 
    -------
    fig: TCanvas, containing the plots.
    """
    
    if show_ratio and (blind is True or data is None or backgrounds is None):
        # cannot show the ratio if data or backgrounds was not specified
        show_ratio=False
    
    ## prepare samples objects and samples hists
    if backgrounds is None and data is None and signal is None:
        # insufficient input
        raise ValueError(
            "at least one of backgrounds, data, "
            "or signal must be specified")

    ## ---------------------------
    # retrive bkg hists, objs
    ## ---------------------------
    if backgrounds is not None:
        if not isinstance(backgrounds, (list, tuple)):
            backgrounds = [backgrounds]
        backgrounds_hists   = []
        backgrounds_objects = []
        for bkg in backgrounds:
            bkg_name = bkg.keys()[0] #<! FIX ME: clumsy!
            bkg_obj = bkg[bkg_name]['INFO']
            h_nom = bkg[bkg_obj.name]['HISTS']['NOMINAL']
            backgrounds_hists.append(h_nom)
            backgrounds_objects.append(bkg_obj)
        
        if overflow:
            for hist in backgrounds_hists:
                fold_overflow(hist)

    ## ---------------------------
    # retrive sig hists, objs
    ## ---------------------------
    if signals is not None:
        if not isinstance(signals, (list, tuple)):
            signals = [signals]
        signals_hists   = []
        signals_objects = []
        for sig in signals:
            sig_name = bkg.keys()[0]
            sig_obj = sig[sig_name]['INFO']
            h_nom = sig[sig_obj.name]['HISTS']['NOMINAL']

            ## scale signals if needed 
            if signal_scale != 1.:
                h_nom = h_nom*signal_scale
                sig_obj.label = '%s #time %s'%(signal_scale, sig_obj.label)
            signals_hists.append(h_nom)
            signals_objects.append(sig_obj)
        if overflow:
            for hist in signals_hists:
                fold_overflow(hist)

    ## ---------------------------
    # retrive data hist, obj
    ## ---------------------------
    if data is not None:
        data_obj = data['data']['INFO']
        data_hist = data[data_obj.name]['HISTS']['NOMINAL']
        if overflow:
            fold_overflow(data_hist)
    
    ## all histograms in the main pad
    plots = []
    legends = []

    ## ---------------------------
    # create canvas, pads, legends, 
    # and labels
    ## ---------------------------
    fig = ROOT.TCanvas('c', 'c', 800, 700) 
    if show_ratio:
        main_pad  = ROOT.TPad('main', 'main', 0., 0.4, 1., 0.95)
        ratio_pad = ROOT.TPad('ratio', 'ratio', 0., 0.15, 1., 0.39)
        main_pad.SetBottomMargin(.04)
        ratio_pad.SetTopMargin(-3.)  # joins upper and lower plot
        ratio_pad.SetBottomMargin(0.0)
        main_pad.Draw()
        ratio_pad.Draw()
    else:
        main_pad = ROOT.TPad('main', 'main', 0., 0.0, 1., .95)
        main_pad.Draw()

    legend = ROOT.TLegend(0.6, 0.75, 0.9, 0.9)
    legend.SetNColumns(2)
    legend.SetBorderSize(1)
    legend.SetFillColor(0)
    legend.SetTextSize(0.025)
    legend.Draw()
    
    labels = label_plot(main_pad, 
                        region_label=region,
                        data_info=data_obj.info, 
                        atlas_label=True,
                        textsize=22)
    for l in labels:
        l.Draw()

    ## ---------------------------
    # backgrounds hists configurations
    ## ---------------------------
    if backgrounds is not None:
        # create the backgrounds stack
        model_stack = ROOT.THStack()
        if xtitle is None:
            xtitle = VARS[var]['root']
    
        for bkg_obj, bkg_hist in zip(reversed(backgrounds_objects),
                                     reversed(backgrounds_hists)):
            bkg_hist.SetFillColor(bkg_obj.color) 
            bkg_hist.GetXaxis().SetTitle(xtitle)
            bkg_hist.GetXaxis().SetLabelOffset(0.4)

            legend.AddEntry(bkg_hist, bkg_obj.label, 'F')
            model_stack.Add(bkg_hist)
      
        # stack signal on top of bkgs
        if signals is not None and signal_on_top:
            for sig_obj, sig_hist in zip(signals_objects ,signals_hists):
                sig_hist.SetFillColor(sig_obj.color)
                legend.AddEntry(sig_hist, sig_obj.name, 'L')
                model_stack.Add(sig_hist)
        plots.append(model_stack)
        
        # background uncertainty band
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
        plots.append(backgrounds_error)
        
        eleg = 'Stat+Syst' 
        if systematics is None: eleg = 'Stat'
        legend.AddEntry(backgrounds_error, eleg ,'F')

    ## stack signals or not
    if signals is not None and not signal_on_top:
        if stack_signal:
            # create the signal stack
            signal_stack = ROOT.THStack()
            for sig_obj, sig_hist in zip(signals_objects ,signals_hist):
                sig_hist.SetFillColor(sig_obj.color)
                legend.AddEntry(sig_hist, sig_obj.name, 'L')
                signal_stack.Add(sig_hist)
            plots.append(signal_stack)
        else:
            # draw all signals separately
            plots.extend(signals_hist)

        if show_signal_error:
            total_signal, high_band_signal, low_band_signal = uncertainty_band(
                signal, systematics) 
            high = (total_signal + high_band_signal) * signal_scale
            low = (total_signal - low_band_signal) * signal_scale
            if signal_on_top:
                high += total_backgrounds
                low += total_backgrounds
            signal_error = ROOT.TGraphErrors()
            for i in range(0, total_backgrounds.GetNbinsX()):
                signal_error.SetPoint(i, total_backgrounds.GetXaxis().GetBinCenter(i), 
                                      total_backgrounds.GetBinContent(i))
                signal_error.SetPointError(i, 0, total_backgrounds.GetBinError(i))
        
            signal_error.SetFillColor(kYellow-1)
            signal_error.SetFillStyle(3004)
            plots.append(signal_error)

    ## ---------------------------
    # data hist configuration
    ## ---------------------------
    if data is not None and blind is not True:
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
                pvalue_label.Draw()

                chi2 = total_backgrounds.Chi2Test(data_hist, 'WW CHI2/NDF')
                chi2_label = ROOT.TLatex(
                    fig.GetLeftMargin() + 0.15,
                    1 - fig.GetTopMargin(),
                    "#chi^{{2}}/ndf={0:.2f}".format(chi2))
                chi2_label.SetNDC(True)
                chi2_label.SetTextFont(43)
                chi2_label.SetTextSize(16)
                chi2_label.Draw()

            pass #<! if backgrounds

        # create the blind data histogram
        if isinstance(blind, tuple):
            low, high = blind
            # zero out bins in blind region
            for i in range(0, data_hist.GetNbinsX()):
                bin_low  = data_hist.GetBinLowEdge(i)
                bin_high = bin_low + data_hist.GetBinWidth(i) 
                if (low < bin_low <= high or low <= bin_high < high):
                    data_hist.SetBinContent(i, -100)
            
        # if poisson_errors:
                    # TODO: get data poisson error

        # draw ratio plot
        if show_ratio:
            # background uncertainty band
            total_backgrounds, high_band_backgrounds, low_band_backgrounds = uncertainty_band(
                backgrounds, systematics, overflow=overflow)
            
            ratio_hist = data_hist.Clone()
            ratio_hist.Divide(total_backgrounds)
                # remove bins where data is zero
            for i in range(0, data_hist.GetNbinsX()):
                if data_hist.GetBinContent(i) <= 0:
                    ratio_hist.SetBinContent(i, 1)

            ratio_hist.GetXaxis().SetLabelFont(43)
            ratio_hist.GetXaxis().SetLabelSize(16)
            ratio_hist.GetXaxis().SetLabelOffset(0.02)
            ratio_hist.GetXaxis().SetTitleFont(43)
            ratio_hist.GetXaxis().SetTitleSize(16)
            ratio_hist.GetXaxis().SetTitleOffset(5)
            ratio_hist.GetXaxis().SetTickLength(0.2)
            ratio_hist.GetXaxis().SetTitle(VARS[var]['root'])

            ratio_hist.GetYaxis().SetLabelFont(43)
            ratio_hist.GetYaxis().SetLabelSize(16)
            ratio_hist.GetYaxis().SetLabelOffset(0.01)
            ratio_hist.GetYaxis().SetTitleFont(43)
            ratio_hist.GetYaxis().SetTitleSize(16)
            ratio_hist.GetYaxis().SetTitleOffset(1.8)
            ratio_hist.GetYaxis().SetTitle('Data/#sum Bkg')


            ## draw band below points on ratio plot
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
                ## dummy x error for plotting
                exh = ratio_hist.GetXaxis().GetBinWidth(i)/2.
                exl = exh
                ratio_error.SetPointError(i, exl, exh, eyl, eyh)

            ratio_error.SetFillColor(ROOT.kYellow-1)
            ratio_error.SetFillStyle(3004)
            plots.append(ratio_error)

            pass #< if show_ratio

        plots.append(data_hist)
        pass #<! if data
 

    #if logy and logy_min is not None:
       # TODO : logy option 

    
    ## ---------------------------
    # plot bkgs stack and errors
    ## ---------------------------
    main_pad.cd()
    
    # set y limit
    ymax = max([h.GetMaximum() for h in plots])
    ymin = min([h.GetMinimum() for h in plots])
    if ylimits is not None:
        ymin, ymax = ylimits
    model_stack.SetMinimum(ymin)
    model_stack.SetMaximum(ymax + 0.3 *ymax)
    model_stack.Draw("HIST")
    if not show_ratio:
        model_stack.GetXaxis().SetTitleOffset(1.4)
        model_stack.GetXaxis().SetTitle(xtitle)

    backgrounds_error.Draw('SAME E2')

    ## ---------------------------
    # plot singal
    ## ---------------------------
        #TODO
        

    ## ---------------------------
    # plot data
    ## ---------------------------
    if data is not None and blind is not True:
        data_info = data_obj.info
        legend.AddEntry(data_hist, data_obj.label, 'LP')
        data_hist.Draw('SAME E1')
        
        if show_ratio:
            ratio_pad.cd()

            ratio_hist.Draw('SAME')
            ratio_error.Draw('SAME E2')

    
    ## ---------------------------
    # create outputs
    ## ---------------------------
    if output_name is None:
        # create the output filename
        output_name = VARS[var]['file_name']
        output_name +='_%s'%region
    if logy:
        output_name += '_logy'
    if output_formats is None:
        output_formats = ('png',)
    # save the figure
    if output_dir is None:
        output_dir = os.getcwd()
        log.warning('output_dir is not set, saving plots in %s'%output_dir)
    output_dir = '%s/%s'%(output_dir, region) 
    save_canvas(fig, output_dir, output_name, formats=output_formats)
    
    return fig


