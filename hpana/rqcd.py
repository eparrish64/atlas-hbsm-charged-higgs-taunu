"""


"""

## stdlib
import os, sys

## PyPI
import numpy as np
import yaml

## ROOT
import ROOT

## local
from .samples.sample import Histset
from .categories import Category
from . import log 

##--------------------------------------------------------------------------
## - - Fakes sources
##--------------------------------------------------------------------------
def fake_sources(samples, category, ftypes={}, tauid=None, antitau=None):
    """
    Find fraction of medium tau and antitau arising from electrons, light quarks, c quarks, b quarks, gluons, etc.
    For the signal regions, a sample of tt bar events with at least one leptonically decaying top quark is used.
    For the multi-jet and W +jets control regions, the corresponding simulated samples (di-jet and W->lnu) are used to identify the sources
    """
    categories = []
    for part, cut in ftypes.iteritems():
        cname = "%s__%s"%(category.name, part)
        clabel = "%s(%s)"%(category.label, part)
        cuts = category.cuts_list + [cut]
        cat = Category(cname, label=clabel, cuts_list=cuts)
        categories.append(cat)

    events = {}
    for sample in samples:
        if not sample.name in events:
            events[sample.name] = {}
        events[sample.name]["TAU"] = sample.events(categories=categories, tauid=tauid, truth_match_tau=ROOT.TCut("1.>0")) 
        events[sample.name]["ANTITAU"] = sample.events(
            categories=categories, tauid=ROOT.TCut("tau_0_jet_bdt_loose==0"), truth_match_tau=ROOT.TCut("1.>0"))

    merged_events = {}
    for cat in categories:
        merged_events[cat.name] = {"TAU":0, "ANTITAU":0}
        merged_events[cat.name]["TAU"] += sum([events[s.name]["TAU"][cat.name] for s in samples]) 
        merged_events[cat.name]["ANTITAU"] += sum([events[s.name]["ANTITAU"][cat.name] for s in samples]) 

    merged_events["%s__sum"%category.name] = {
        "TAU": sum([merged_events[c]["TAU"] for c in merged_events.keys()]),
        "ANTITAU": sum([merged_events[c]["ANTITAU"] for c in merged_events.keys()])
    }
    return merged_events


##--------------------------------------------------------------------------
## - - organize the hists for calcualting FFs 
##--------------------------------------------------------------------------
def prep_ff_hists(ffs_hists,
                  ntracks=[1, 3],
                  target_regions=[],
                  control_regions=[],
                  shape_vars={},
                  fitting_bins={}):
    """ derive the fraction of q/g initiated tau jets for a template-fit of the a variable
    sensitive to the difference.
    Parameters
    - - - - - - 
    ffs_hists: 
        list(HistSet types): histograms for various target regions
    
    n_tracks:
        int : number of charged tau tracks
    target_regions:
         list(Category types): selection regions that we want to find the alpha for them.
    
    shape_vars: 
        dict with values are Variable type; variable that is most sensitive to q/g discrimination

    Return
    - - - -
    """
    # - - - - gather hists per bins of aux vars(ntracks, pt)
    hist_sets = []
    for itk in ntracks:
        tkey = "%i"%itk
        var = shape_vars[tkey] #<! different variable for 1p and 3p taus
        ffs_hists_itk = filter(lambda hs: hs.variable==var.name, ffs_hists)
        fitting_sub_bins = fitting_bins[tkey]
        for _bin in range(1, len(fitting_sub_bins)):
            pkey = "%i"%fitting_sub_bins[_bin]
            for hs in ffs_hists_itk:
                htmp = hs.hist.Clone()
                tmp_hz = htmp.Project3D("z").Clone()
                bin_low = tmp_hz.FindBin(fitting_sub_bins[_bin-1])
                bin_high = tmp_hz.FindBin(fitting_sub_bins[_bin])-1
                
                suffix = "TRACKS{0}_PT{1}TO{2}".format(itk, fitting_sub_bins[_bin-1], fitting_sub_bins[_bin])
                hist_var = htmp.ProjectionX(suffix, itk, itk+1, bin_low, bin_high, "e")

                # - - - - use special :=: token in the name to keep var 1 bin and var 2 bin info  
                hist_sets.append(
                    Histset(name="%s:=:%s:=:%s"%(hs.name, tkey, pkey), sample=hs.sample, variable=hs.variable,
                            category=hs.category, systematic=hs.systematic, hist=hist_var.Clone()))
                htmp.Delete()
                tmp_hz.Delete()
    return hist_sets

##--------------------------------------------------------------------------
## - - organize the hists for calcualting FFs 
##--------------------------------------------------------------------------
def fit_alpha(cr_hists, target_hists, ntracks=[1, 3], fitting_bins={}, shape_vars=[],):
    """ give the template shapes for different FFs dedicated control regions 
    and the the other selection regions. A transformation factor is derived in order 
    to combin FFs taking into account the differences between FFs CR regions and other reiogns. 
    
    Parameters
    - - - - - 
    cr_hitsts:
        dict; keys corresponding to the anlysis channels/aux var1/aux var2 binning (n_tracks, pt)
        and values list(Histset), which contain different hists for FFs control regions 

    cr_hitsts:
        dict; keys corresponding to the anlysis channels/aux var1/aux var2 binning (n_tracks, pt)
        and values list(Histset), which contain different hists for other control regions/signal regions. 

    Return 
    - - - - 

    """

    # - - - - output containers
    chi2s = {}
    alphas_min = {}
    cr_hists_dict = {}
    target_hists_dict = {}
    
    # - - - - gather hists per bins of aux vars(ntracks, pt)
    for itk in ntracks:
        tkey = "%i"%itk
        chi2s[tkey] = {}
        alphas_min[tkey] = {}
        cr_hists_dict[tkey] = {}
        target_hists_dict[tkey] = {}
        
        # - - get the right hists 
        var = shape_vars[tkey]
        cr_hists_itk = filter(lambda hs: hs.variable==var.name, cr_hists)
        target_hists_itk = filter(lambda hs: hs.variable==var.name, target_hists)
        
        fitting_sub_bins = fitting_bins[tkey]
        for _bin in fitting_sub_bins[1:]:
            pkey = "%i"%_bin
            chi2s[tkey][pkey] = {}
            alphas_min[tkey][pkey] = {}
            cr_hists_dict[tkey][pkey] = {}
            target_hists_dict[tkey][pkey] = {}

            # - - hists for ntracks and pT bin 
            cr_hists_per_bin = filter(lambda hs: hs.name.split(":=:")[-2]==tkey and hs.name.split(":=:")[-1]==pkey, cr_hists_itk)
            tr_hists_per_bin = filter(lambda hs: hs.name.split(":=:")[-2]==tkey and hs.name.split(":=:")[-1]==pkey, target_hists_itk)
            
            # - - - - add the hists from CRs with a coefficent to fit to in the target regions (assuming only two FF CRs)
            for hs in cr_hists_per_bin:
                if "WJETS" in hs.category:
                    wj_hist = hs.hist
                if "MULTIJET" in hs.category:    
                    mj_hist = hs.hist
            assert mj_hist and wj_hist, "CR hists are not available"
            
            if wj_hist.Integral()==0 or mj_hist.Integral()==0:
                log.warning(" one of the CRs hist is empty! skipping fitting in (ntracks=%s, pT=%s)bin"%(tkey, pkey))
                continue

            # - - - - scale them to one
            wj_hist.Scale(1./wj_hist.Integral())
            mj_hist.Scale(1./mj_hist.Integral())

            # - - - - keep them for plotting
            cr_hists_dict[tkey][pkey] = [wj_hist, mj_hist]
                                    
            # - - - - now for each target region perform the fitting
            for hs in tr_hists_per_bin:
                target_hist = hs.hist
                if target_hist.Integral()==0:
                    log.warning(" target region %s hist is empty! skipping fitting in (ntracks=%s, pT=%s)bin"%(hs.category, tkey, pkey))
                    continue
                target_hist.Scale(1./target_hist.Integral())
                target_hists_dict[tkey][pkey][hs.category] = [target_hist]
                                
                # - - - - varying the coefficient
                chi2 = []
                alpha = np.arange (-4, 4, 0.01)

                # - - - - fit to aP_mj + (1-a)P_wj
                for a in alpha:
                    scaled_mj_hist = mj_hist.Clone()
                    scaled_mj_hist.Scale(a)
                    
                    scaled_wj_hist = wj_hist.Clone()

                    template_hist = scaled_mj_hist.Clone()
                    template_hist.Add(scaled_wj_hist, 1 - a)
                    
                    if template_hist.Integral()==0 or target_hist.Integral()==0:
                        log.warning("target or template hist is zero, wont fit anything")
                        continue
                    template_hist.Scale(1/template_hist.Integral())

                    # - - - - CHI2 fit; other option: KolmogorovTest(template_hist, "U O") 
                    c2 = target_hist.Chi2Test(template_hist, "WW CHI2/NDF ")
                    chi2.append((a, c2))

                    scaled_mj_hist.Delete()
                    scaled_wj_hist.Delete()
                    template_hist.Delete()
                    
                alpha_min = alpha[0]
                c2min = chi2[0]
                for c in chi2:
                    if c[1] < c2min:
                        c2min = c[1]
                        alpha_min = c[0]
                        
                # - - - - keep alpha corresponding to min Chi2 distribution        
                if not hs.category in alphas_min[tkey][pkey]:
                    alphas_min[tkey][pkey][hs.category] = {}
                alphas_min[tkey][pkey][hs.category] = alpha_min

                # - - - - get chi2 function
                chi2_func = ROOT.TGraph(len(chi2))
                for i, point in enumerate(chi2):
                    chi2_func.SetPoint(i, *point)
                chi2_func.SetName("chi2_func")
                chi2s[tkey][pkey][hs.category] = chi2_func

                # - - - - fit to the target hist (P_target = aP_mj + (1-a)P_wj) 
                alpha_mj_hist = mj_hist.Clone()
                alpha_mj_hist.Scale(alpha_min)

                alpha_wj_hist = wj_hist.Clone()
                alpha_wj_hist.Scale(1 - alpha_min)

                target_fit_hist = alpha_mj_hist.Clone()
                target_fit_hist.Add(alpha_wj_hist)

                # - - - - get the fit function
                target_fit_func = ROOT.TGraph(target_fit_hist)
                target_hists_dict[tkey][pkey][hs.category] += [target_fit_func]
    
            
    return cr_hists_dict, target_hists_dict, alphas_min, chi2s



##--------------------------------------------------------------------------
## - - control regions Fake Factors plotting funtions 
##--------------------------------------------------------------------------
def cr_ffs_plots(cr_ffs,
                 cr_labels={},
                 jet_bdt_key="tauJetBDT_02",
                 suffix="",
                 pdir="",
                 colors=[ROOT.kBlack, ROOT.kGreen, ROOT.kRed, ROOT.kBlue,]):
    """
    
    """
    canvas = ROOT.TCanvas("c", "c", 800, 600)
    cr_ff_legend = ROOT.TLegend(0.6, 0.8, 0.9, 0.9)
    with open(cr_ffs, "r") as crfile:
        CR_FFs = yaml.load(crfile)
        
    # - - - - retrive hists 
    hists = []
    for cr in CR_FFs.keys():
        for itk, bins in CR_FFs[cr][jet_bdt_key].iteritems():
            bin_keys = sorted([float(b) for b in bins.keys()])
            hist = ROOT.TH1F("%s__%i"%(cr, itk), "", len(bins)-1, array.array("d", bins))
            nbin = 1
            for pt, ff in bins.iteritems():
                hist.SetBinContent(nbin, float(ff))
                hist.SetBinError(nbin, 0.001)
            hists += [hist]
            label = cr_labels[cr] if cr_labels else cr 
            cr_ff_legend.AddEntry(hist, "%s (nprongs=%s)"%(itk, label), "L")
            h.SetMarkerColor(colors[len(hists)-1])
            h.SetLineColor(cl[len(hists)-1])

    # - - - - plot them
    for n, h in enumerate(hists):
        if n==0:
            h.SetMaximum(10)
            h.SetMinimum(0.01)
            h.Draw("")
            h.GetYaxis().SetTitle("FF")
            h.GetXaxis().SetTitle("#tau p_{T} GeV")
        else:
            h.Draw("SAME")
    cr_ff_legend.Draw("SAME")

    canvas.SetLogx()
    canvas.SetLogy()

    os.system("mkdir -p %s"%pdir)
    canvas.Print(os.path.join(pdir, "FFs_inclusive_tracks_pT.png"))
    canvas.Close()

    return canvas 

##--------------------------------------------------------------------------
## - - template fit validation plots
##--------------------------------------------------------------------------
def validate_template_fit(target_hists_dict, alpha_qcd, target_regions=[], colors=[]):
    """
    """
    ntracks = target_hists_dict.keys()
    pt_bins = target_hists_dict[ntracks[0]].keys()
    for cat in target_regions:
        if not pkey in target_hists_dict[tkey]:
            log.warning("missing TARGET %s %s "%(tkey, pkey))
            continue
        if not cat.name in target_hists_dict[tkey][pkey]:
            log.warning("missing TARGET %s %s  %s"%(cat.name, tkey, pkey))
            continue

        tr_legend = ROOT.TLegend(0.6, 0.8, 0.9, 0.9) 
        target_hist, target_fit = target_hists_dict[tkey][pkey][cat.name]

        target_fit.SetMarkerColor(ROOT.kRed)
        target_fit.SetLineColor(ROOT.kRed)
        target_fit.Draw("PAC")

        target_hist.SetMarkerColor(ROOT.kBlack)
        target_hist.SetLineColor(ROOT.kBlack)
        target_fit.GetXaxis().SetTitle(var.title)
        target_fit.GetYaxis().SetTitle("fraction of events")
        target_hist.Draw("SAME")

        tr_legend.AddEntry(target_hist, "%s region"%cat.name, "P")

        tr_legend.AddEntry(target_fit, "fit", "L")

        # - - add legends, labels and save canvas
        tr_legend.Draw("SAME")
        tlabel.Draw("SAME")
        canvas.Print(os.path.join(FFs_ARGS.pdir, "TARGET_%s_%s_%s.png"%(cat.name, tkey, pkey) ) )
        canvas.Clear()

        ##--------------------------------------------------------
        # - - plot chi2
        ##--------------------------------------------------------
        chi2_graph = chi2s[tkey][pkey][cat.name]
        chi2_graph.SetLineWidth(3)
        chi2_graph.SetLineColor(ROOT.kBlue)
        chi2_graph.Draw("AL")
        chi2_graph.GetXaxis().SetTitle("#alpha_{MJ}")
        chi2_graph.GetYaxis().SetTitle("#chi^{2}/ndf")
        tlabel.Draw("SAME")
        tr_legend.Draw("SAME")

        # - - find the min and draw a line there
        xarr = chi2_graph.GetX()
        yarr = chi2_graph.GetY()

        ymin = min(yarr)
        xmin_index = [i for i, y in enumerate(yarr) if y==ymin][0]
        xmin = xarr[xmin_index]
        ymax = max(yarr)

        chi2_graph.SetMinimum(0)
        chi2_graph.SetMaximum(1.2*ymax)
        tline = ROOT.TLine(xmin, 0, xmin , ymax)
        tline.SetLineColor(ROOT.kRed)
        tline.SetLineWidth(2)
        tline.Draw("SAME")

        tline_up = ROOT.TLine(1.2*xmin, 0, 1.2*xmin , ymax)
        tline_up.SetLineColor(ROOT.kRed)
        tline_up.SetLineWidth(2)
        tline_up.SetLineStyle(10)
        tline_up.Draw("SAME")

        tline_dn = ROOT.TLine(0.8*xmin, 0, 0.8*xmin , ymax)
        tline_dn.SetLineColor(ROOT.kRed)
        tline_dn.SetLineWidth(2)
        tline_dn.SetLineStyle(10)
        tline_dn.Draw("SAME")

        canvas.Print(os.path.join(FFs_ARGS.pdir, "CHI2_%s_%s_%s.png"%(cat.name, tkey, pkey) ) )
        canvas.Clear()

    ##--------------------------------------------------------
    # - -  plot ALPHA as a function of pT for 1p/3p taus
    ##--------------------------------------------------------

    # - - n tracks lable for the plots
    alabel = ROOT.TLatex(
        canvas.GetLeftMargin() + 0.6, canvas.GetBottomMargin() + 0.5,"n-prongs = %i"%itk)
    alabel.SetNDC()
    alabel.SetTextFont(43)
    alabel.SetTextSize(15)
    alabel.SetTextAlign(11)

    alphas = alphas_min[tkey]
    pt_bins = sorted([int(k) for k in alphas.keys()])

    alpha_hists = []
    comb_ff_hists = []
    a_legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    for ic, cat in enumerate(target_regions):
        log.info("\n****************** rQCD estimation (category:{0}, nTracks={1}) ******************".format(cat.name, itk))
        alpha_h = ROOT.TH1F(
            "alpha_%s_%s"%(cat, itk), "#alpha_{MJ}",len(pt_bins) - 1, array.array("d", pt_bins))

        comb_ff_h = ROOT.TH1F(
            "comb_ff_%s_%s"%(cat, itk), "#COM_{FF}",len(pt_bins) - 1, array.array("d", pt_bins))
        for nbin, pt in enumerate(pt_bins[1:]):
            pkey = "%i"%pt
            if not pkey in alphas:
                log.warning(" no alpha is fitted for %i bin! setting it to 0"%pt)
                alpha_h.SetBinContent(nbin+1, 0) 
                alpha_h.SetBinError(nbin+1, 0.0001) #<! dummy error for plotting purpose only

                comb_ff_h.SetBinContent(nbin+1, 0) 
                comb_ff_h.SetBinError(nbin+1, 0.0001) #<! dummy error for plotting purpose only
                continue
            if not cat.name in alphas[pkey]:
                continue
            alpha = alphas[pkey][cat.name]
            log.info("(pT, alpha): {}, {}".format(pkey, alpha))

            alpha_h.SetBinContent(nbin+1, alpha) 
            alpha_h.SetBinError(nbin+1, 0.001) #<! dummy error for plotting purpose only

            ff = alpha*float(CR_FFs["FF_CR_MULTIJET"]["tauJetBDT_02"][tkey][pkey]) + (1-alpha)*float(CR_FFs["FF_CR_WJETS"]["tauJetBDT_02"][tkey][pkey])
            comb_ff_h.SetBinContent(nbin+1, ff) 
            comb_ff_h.SetBinError(nbin+1, 0.0001) #<! dummy error for plotting purpose only

        alpha_h.SetLineColor(COLORS[ic])
        alpha_h.SetLineWidth(2)
        alpha_h.GetYaxis().SetTitle("#alpha_{MJ}")
        alpha_h.GetXaxis().SetTitle("p^{T}_{#tau} GeV")
        alpha_hists.append(alpha_h)

        alpha_h.Draw("E1")
        alpha_h.GetYaxis().SetRangeUser(-2., 5)
        a_legend.AddEntry(alpha_h, "%s"%cat.label, "L")

        comb_ff_h.SetLineColor(COLORS[ic])
        comb_ff_h.SetLineWidth(2)
        comb_ff_h.GetYaxis().SetTitle("FF_{COM}")
        comb_ff_h.GetXaxis().SetTitle("p^{T}_{#tau} GeV")

        comb_ff_h.GetYaxis().SetRangeUser(0.001, 10)
        comb_ff_hists.append(comb_ff_h)

    for i, ah in enumerate(alpha_hists):
        if i==0:
            ah.Draw("E1")
        else:
            ah.Draw("E1 SAME")
    alabel.Draw("SAME")
    a_legend.Draw("SAME")
    canvas.SetLogx()
    canvas.Print(os.path.join(FFs_ARGS.pdir, "ALPHA_inclusive_%s.png"%(tkey)) )
    canvas.Clear()

    for i, fh in enumerate(comb_ff_hists):
        if i==0:
            fh.Draw("E1")
        else:
            fh.Draw("E1 SAME")
    canvas.SetLogy()
    canvas.SetLogx()
    alabel.Draw("SAME")
    a_legend.Draw("SAME")
    canvas.Print(os.path.join(FFs_ARGS.pdir, "FFs_COM_inclusive_%s.png"%(tkey)) )
    canvas.Clear()

    canvas.Close()

