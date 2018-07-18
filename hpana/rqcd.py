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
from . import log 

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
                bin_high = tmp_hz.FindBin(fitting_sub_bins[_bin])
                
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
