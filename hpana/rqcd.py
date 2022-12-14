"""


"""

## stdlib
import os, sys, array, math
from collections import OrderedDict

## PyPI
import numpy as np
import yaml

## ROOT
import ROOT

## local
from hpana.samples.sample import Histset
from hpana.samples.fakes import QCD 
from hpana.categories import Category, ANTI_TAU
from hpana.variables import rQCD_VARS
from hpana.plotting.plot import label_plot
from . import log 


##--------------------------------------------------------------------------
## - - simple chi2 implementation
##--------------------------------------------------------------------------
def calculate_chi2(target_hist, template_hist, min_evts=10):
    """
    Chi squared/ndf  
    """
    #MB
    nbins_real= 0
    #MB
    chi2 = 0
    nbins = target_hist.GetNbinsX()
    for i in range(nbins):
        tr_cont = target_hist.GetBinContent(i)
        tr_err  = target_hist.GetBinError(i)
        tm_cont = template_hist.GetBinContent(i)
        tm_err  = template_hist.GetBinError(i)

        # n_tr = (tr_cont/tr_err)**2
        # n_tm = (tm_cont/tm_err)**2

        # if n_tr < min_evts or n_tm < min_evts:
        #     continue
        if tr_cont==0 or tm_cont==0:
            continue
        #MB
        nbins_real += 1
        #MB
        chi2 += ((tr_cont-tm_cont)**2)/(tr_err**2 + tm_err**2)
        
    #return chi2/nbins
    #MB
    return chi2/nbins_real , nbins_real
    #MB

##--------------------------------------------------------------------------
## - - chi2 fit error 
##--------------------------------------------------------------------------
def chi2_error(chi2_graph, template_bins=20):
    """

    """
    # - - find the min and draw a line there
    xarr = chi2_graph.GetX()
    yarr = chi2_graph.GetY()
    
    ymin = min(yarr)
    xmin_index = [i for i, y in enumerate(yarr) if y==ymin][0]
    xmin = xarr[xmin_index]
    ymax = max(yarr)

    ##  See this paper: https://arxiv.org/pdf/1012.3754.pdf
    ## large number of bins 
    std = math.sqrt(2./template_bins)

    ## small number of bins 
    # std = (2./template_bins)
    
    #err_up = std
    #for n in range(xmin_index+1, len(xarr)):
     #   if err_up < (xarr[n]- xmin):
      #      err_up = xarr[n] - xmin
          #  break
        
    #err_dn = std
    #n = xmin_index-1
    #while n > 0:
     #   if err_dn < (xmin - xarr[n]):
      #      err_dn = xmin - xarr[n]
       #     break
        #n -= 1
    
    #MB 
   
    #chi2_sigma 
    #std =  1./template_bins 
    err_up =0
    for n in range(xmin_index+1, len(xarr)):
        if std <(yarr[n]- ymin):
            err_up = xarr[n] - xmin
            break
        
    err_dn = 0
    n = xmin_index-1
    while n > 0:
        if std < (yarr[n]-ymin):
            err_dn = xmin - xarr[n]
            break
        n -= 1
    #MB
    return xmin, err_up, err_dn
        
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
            categories=categories, tauid=ANTI_TAU, truth_match_tau=ROOT.TCut("1.>0"))

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
## - - calculate CR FFs 
##--------------------------------------------------------------------------
def get_cr_ffs(hist_sets, 
                control_regions=[], 
            #LD tau_jet_bdt_score_trans_wps={"NOMINAL":0.02, "1up": 0.01, "1down": 0.03}, 
              	tau_jet_rnn_score_trans={"NOMINAL":0.01, "1up": 0.01, "1down": 0.01}, 
	 	        n_charged_tracks=[],
                subtract_mc=True,
                cache_file=None,
                write_cxx_macro=True,
                validation_plots=False,
                pdir="ffplots",
                template_hist_bins=[], 
                **kwargs):
    """

    """

        # - - - -  organize the output
    data_tau_hists = filter(lambda hs: hs.name.startswith("Data") and hs.name.endswith("_TAU"), hist_sets)
    data_antitau_hists = filter(lambda hs: hs.name.startswith("Data") and hs.name.endswith("_ANTITAU"), hist_sets)

    if subtract_mc:
        mc_tau_hists = filter(lambda hs: not hs.name.startswith("Data") and hs.name.endswith("_TAU"), hist_sets)
        mc_antitau_hists = filter(lambda hs: not hs.name.startswith("Data") and hs.name.endswith("_ANTITAU"), hist_sets)
    
    # - - - - add up the histograms for each CR region 
    ffs_dict = {}
    for cr in control_regions:
        cr_name = cr.name
        ffs_dict[cr_name] = OrderedDict()
        
        # - - data tau
        data_tau_hists_cat = filter(lambda hs: hs.category==cr_name, data_tau_hists)
        assert data_tau_hists_cat, "no (TAU) %s hist for %s CR"%("DATA", cr_name)
        data_tau_hsum = data_tau_hists_cat[0].hist.Clone()
        if len(data_tau_hists_cat) > 1:
            for hs in data_tau_hists_cat[1:]:
                data_tau_hsum.Add(hs.hist)
        
        # - - data antitau
        data_antitau_hists_cat = filter(lambda hs: hs.category==cr_name, data_antitau_hists)
        assert data_antitau_hists_cat, "no (ANTITAU) %s hist for %s CR"%("DATA", cr_name)
        data_antitau_hsum = data_antitau_hists_cat[0].hist.Clone()
        if len(data_antitau_hists_cat) > 1:
            for hs in data_antitau_hists_cat[1:]:
                data_antitau_hsum.Add(hs.hist)

        if subtract_mc:
            # - - mc tau
            mc_tau_hists_cat = filter(lambda hs: hs.category==cr_name, mc_tau_hists)
            assert mc_tau_hists_cat, "no (TAU) %s hist for %s CR"%("MC", cr_name)
            mc_tau_hsum = mc_tau_hists_cat[0].hist.Clone()
            for hs in mc_tau_hists_cat[1:]:
                mc_tau_hsum.Add(hs.hist)

            # - - mc antitau
            mc_antitau_hists_cat = filter(lambda hs: hs.category==cr_name, mc_antitau_hists)
            assert mc_antitau_hists_cat, "no (ANTITAU) %s hist for %s CR"%("MC", cr_name)
            mc_antitau_hsum = mc_antitau_hists_cat[0].hist.Clone()
            for hs in mc_antitau_hists_cat[1:]:
                mc_antitau_hsum.Add(hs.hist)
                
        data_mc_tau_h = data_tau_hsum.Clone()
        data_mc_antitau_h = data_antitau_hsum.Clone()

        ## variations for MC subtraction (0.5, 1.5)
        data_mc_mcsub05_tau_h = data_tau_hsum.Clone()
        data_mc_mcsub05_antitau_h = data_antitau_hsum.Clone()
        data_mc_mcsub15_tau_h = data_tau_hsum.Clone()
        data_mc_mcsub15_antitau_h = data_antitau_hsum.Clone()

        # - - subtract MC from DATA
        if subtract_mc:
            data_mc_tau_h.Add(mc_tau_hsum, -1)
            data_mc_antitau_h.Add(mc_antitau_hsum, -1)

            data_mc_mcsub05_tau_h.Add(mc_tau_hsum, -1)
            data_mc_mcsub05_antitau_h.Add(mc_antitau_hsum, -0.5) # 50 percent MC variation only on antitau

            data_mc_mcsub15_tau_h.Add(mc_tau_hsum, -1)
            data_mc_mcsub15_antitau_h.Add(mc_antitau_hsum, -1.5) # 50 percent MC variation only on antitau
        
        log.info("Region:{}; TAU events; DATA: {}, MC: {}".format(cr_name,
            data_tau_hsum.Integral(), mc_tau_hsum.Integral() if subtract_mc else "NAN") )
        log.info("Region:{}; ANTITAU events; DATA: {}, MC: {}".format(cr_name, 
            data_antitau_hsum.Integral(), mc_antitau_hsum.Integral() if subtract_mc else "NAN") )

        htmp_tau = data_mc_tau_h.Clone()
        htmp_antitau = data_mc_antitau_h.Clone()

        htmp_tau_mcsub05 = data_mc_mcsub05_tau_h.Clone()
        htmp_antitau_mcsub05 = data_mc_mcsub05_antitau_h.Clone()
        htmp_tau_mcsub15 = data_mc_mcsub15_tau_h.Clone()
        htmp_antitau_mcsub15 = data_mc_mcsub15_antitau_h.Clone()
        

        # - - project along X and Y to get the bins
        htmp_X = htmp_antitau.ProjectionX().Clone()
        htmp_Y = htmp_antitau.ProjectionY().Clone()
        htmp_Z = htmp_antitau.ProjectionZ().Clone()
        
        if validation_plots:
            os.system("mkdir -p %s"%pdir)
            canvas = ROOT.TCanvas()
            
            htmp_tau.Draw("")
            canvas.Print("%s/h3_tau.png"%pdir)
            canvas.Clear()

            htmp_antitau.Draw("")
            canvas.Print("%s/h3_antitau.png"%pdir)
            canvas.Clear()

            htmp_X.Draw()
            canvas.Print("%s/hX_antitau.png"%pdir)
            canvas.Clear()

            htmp_Y.Draw()
            canvas.Print("%s/hY_antitau.png"%pdir)
            canvas.Clear()

            htmp_Z.Draw()
            canvas.Print("%s/hZ_antitau.png"%pdir)
            canvas.Clear()

            canvas.Close()
        
        # - - gather hists per tau pT and ntracks bin and also tau_jet_bdt_score WPs
        #LD for jkey, jbs_wp in tau_jet_bdt_score_trans_wps.iteritems(): switch to RNN
	for jkey, jbs_wp in tau_jet_rnn_score_trans.iteritems():
            # jkey = "tauJetBDT_0%i"%(100*jbs_wp)
            ffs_dict[cr_name][jkey] = {}
            if jkey=="NOMINAL" and subtract_mc:
                ffs_dict[cr_name]["MCSubt_1up"] = {}
                ffs_dict[cr_name]["MCSubt_1down"] = {}

            for itk_n, itk in enumerate(n_charged_tracks):
                tkey = "%i"%itk
                ffs_dict[cr_name][jkey][tkey]= {}
                if jkey=="NOMINAL" and subtract_mc:
                    ffs_dict[cr_name]["MCSubt_1up"][tkey] = {}
                    ffs_dict[cr_name]["MCSubt_1down"][tkey] = {}
                
                # - - keep jet BDT score along X (only a lower cut)
                x_low = htmp_X.FindBin(jbs_wp)
                x_high = -1 #<! to include overflow bin too
                
                # - - ntracks along Y
                y_low = htmp_Y.FindBin(itk)
                y_high = htmp_Y.FindBin(itk)+1
                
                # - - fitting bins for the actual shape variable
                fitting_bins = template_hist_bins[tkey]
                for _bin in range(1, len(fitting_bins)):
                    pkey = "%i"%fitting_bins[_bin]
                    z_low = htmp_Z.FindBin(fitting_bins[_bin-1])
                    z_high = htmp_Z.FindBin(fitting_bins[_bin])-1

                    stat_tau_err = ROOT.Double(0)
                    stat_antitau_err = ROOT.Double(0)
                    tau_bin_cont = htmp_tau.IntegralAndError(x_low, x_high, y_low, y_high, z_low, z_high, stat_tau_err)
                    antitau_bin_cont = htmp_antitau.IntegralAndError(x_low, x_high, y_low, y_high, z_low, z_high, stat_antitau_err)

                    #tau_bin_cont = htmp_tau.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                    #antitau_bin_cont = htmp_antitau.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                    if antitau_bin_cont==0:
                        log.warning("{} bin for antitau is empty, setting tau/antitau to 1!".format(pkey))
                        tau_antitau_ratio = 1.
                        tau_antitau_ratio_err = 1.
                        #tau_antitau_err  = 0.
                    else:
                        tau_antitau_ratio = "%.6f"%(tau_bin_cont/float(antitau_bin_cont))
                        tau_antitau_ratio_err = stat_tau_err/float(antitau_bin_cont)
                    #ffs_dict[cr_name][jkey][tkey][pkey] = tau_antitau_ratio
                    log.info("error  in CR << {}  >> bin: tau:{}, antitau: {}, ratio: {} , stat_error: {} ".format((cr_name,jkey,tkey,pkey), tau_bin_cont, antitau_bin_cont, tau_antitau_ratio,tau_antitau_ratio_err))                    
                    ffs_dict[cr_name][jkey][tkey][pkey] = tau_antitau_ratio
                    
                    ##  MC subtraction variations
                    if jkey=="NOMINAL" and subtract_mc:
                        tau_mcsub05_bin_cont = htmp_tau_mcsub05.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                        antitau_mcsub05_bin_cont = htmp_antitau_mcsub05.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                        if antitau_mcsub05_bin_cont==0:
                            log.debug("{} bin for antitau is empty, setting tau/antitau to 1 for non-empty tau bin".format(pkey))
                            if tau_mcsub05_bin_cont==0:
                                tau_antitau_ratio_mcsub05 = 0.
                            else:
                                tau_antitau_ratio_mcsub05 = 1. 
                        else:
                            tau_antitau_ratio_mcsub05 = "%.4f"%(tau_mcsub05_bin_cont/float(antitau_mcsub05_bin_cont))                    
                        ffs_dict[cr_name]["MCSubt_1up"][tkey][pkey] = tau_antitau_ratio_mcsub05

                        tau_mcsub15_bin_cont = htmp_tau_mcsub15.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                        antitau_mcsub15_bin_cont = htmp_antitau_mcsub15.Integral(x_low, x_high, y_low, y_high, z_low, z_high)
                        if antitau_mcsub15_bin_cont==0:
                            log.debug("{} bin for antitau is empty, setting tau/antitau to 1 for non-empty tau bin".format(pkey))
                            if tau_mcsub15_bin_cont==0:
                                tau_antitau_ratio_mcsub15 = 0.
                            else:
                                tau_antitau_ratio_mcsub15 = 1. 
                        else:
                            tau_antitau_ratio_mcsub15 = "%.4f"%(tau_mcsub15_bin_cont/float(antitau_mcsub15_bin_cont))                    
                        ffs_dict[cr_name]["MCSubt_1down"][tkey][pkey] = tau_antitau_ratio_mcsub15

                    log.debug("bins: {}".format((x_low, x_high, y_low, y_high, z_low, z_high)))
                    log.debug("ratio in << {}  >> bin: tau:{}, antitau: {}, ratio: {} ".format(
                        (jkey, tkey, pkey), tau_bin_cont, antitau_bin_cont, tau_antitau_ratio))
                    log.debug("--"*60)
                    
        # - - clean up
        htmp_X.Delete()
        htmp_Y.Delete()
        htmp_Z.Delete()
        htmp_tau.Delete()
        htmp_antitau.Delete()
                
    if not cache_file:
        yml_file = "FFs_CR.yml"
    else:
        yml_file = cache_file
        
    with open (yml_file, "a") as yml_cache:
        log.info("caching the fake factors")
        yaml.dump(ffs_dict, yml_cache, default_flow_style=False)

    log.info("FFs: {} ".format(ffs_dict))

    if write_cxx_macro:
        if yml_file.endswith(".yml"): 
            cxx_file = yml_file.replace(".yml", ".cxx")
        else:
            cxx_file = yml_file + ".cxx"
            
        with open(cxx_file, "a") as cxx_cache:
            cxx_cache.write("#include <iostream>\n")
            for cr in [c.name for c in control_regions]:
                for jkey in ffs_dict[cr].keys():
                    cxx_cache.write("//! {} \n".format(jkey))
                    cxx_cache.write(
                        "float GetFF_{0}_{1}(float pt, int nTracks){{\n".format(cr, jkey) )
                    for itk in n_charged_tracks:
                        tkey = "%i"%itk
                        cxx_cache.write("\t if(nTracks==%i){\n"%itk)
                        for pT in template_hist_bins[tkey][1:]:
                            pkey = "%i"%pT
                            ff = ffs_dict[cr][jkey][tkey][pkey]
                            cxx_cache.write("\t\t if(pt < {0}) return {1};\n".format(pT, ff))

                        # - - - -  close ntracks block   
                        cxx_cache.write("\t\t else return 0;\n")   
                        cxx_cache.write("\t\t }\n")

                    # - - - - close tauJetBDTscore block
                    cxx_cache.write("\t else return 0;\n")   
                    cxx_cache.write("}\n\n\n")
                
    return ffs_dict
    

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
def fit_alpha(cr_hists, target_hists, regions,
              ntracks=[1, 3],
              fitting_bins={},
              shape_vars=[],
              cache=None,
              pdir=None,
              validation_plots=False):
    
    """ give the template shapes for different FFs dedicated control regions 
    and the the other selection regions. A transformation factor is derived in order 
    to combin FFs taking into account the differences between FFs CR regions and other reiogns. 
    
    Parameters
    - - - - - 
    cr_hitsts:
        dict; keys corresponding to the anlysis channels/aux var1/aux var2 binning (n_tracks, pt)
        and values list(Histset), which contain different hists for FFs control regions 

    target_hists:
        dict; keys corresponding to the anlysis channels/aux var1/aux var2 binning (n_tracks, pt)
        and values list(Histset), which contain different hists for other regions/signal regions. 

    Return 
    - - - - 

    """
    ## - - - - fit regions 
    # cr_regions = []
    # target_regions = []
    # for hset in cr_hists:
    #     if not hset.category in cr_regions:
    #         cr_regions.append(hset.category)
    # for hset in target_hists:
    #     if not hset.category in (target_regions + cr_regions):
    #         target_regions.append(hset.category)
            
    # regions = cr_regions + target_regions
    
    # - - - - output containers
    chi2s = {}
    alphas = {}
    cr_hists_dict = {}
    target_hists_dict = {}
    
    # - - - - gather hists per bins of aux vars(ntracks, pt)
    for itk in ntracks:
        tkey = "%i"%itk
        chi2s[tkey] = {}
        alphas[tkey] = {}
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
            alphas[tkey][pkey] = {}
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
            assert mj_hist and wj_hist, "CR hists are not availabel"
            
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
                target_hist.Sumw2()   
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
                    template_hist.Sumw2()
                    
                    # - - - - CHI2 fit; other option: KolmogorovTest(template_hist, "U O") 
                    #c2 = target_hist.Chi2Test(template_hist, "WW CHI2/NDF ")
                    #MB
                    c2, nbins_real =calculate_chi2(target_hist, template_hist, min_evts=10)
                    #MB
                    chi2.append((a, c2))
                    
                    scaled_mj_hist.Delete()
                    scaled_wj_hist.Delete()
                    template_hist.Delete()

                # - - - - get chi2 function
                chi2_graph = ROOT.TGraph(len(chi2))
                for i, point in enumerate(chi2):
                    chi2_graph.SetPoint(i, *point)
                chi2_graph.SetName("chi2_graph")
                chi2s[tkey][pkey][hs.category] = chi2_graph

                #alpha, err_up, err_down = chi2_error(chi2_graph, template_bins=len(fitting_sub_bins))
                #MB
                alpha, err_up, err_down = chi2_error(chi2_graph, nbins_real)
                # - - - - keep alpha corresponding to min Chi2 distribution        
                if not hs.category in alphas[tkey][pkey]:
                    alphas[tkey][pkey][hs.category] = {"NOMINAL":0.0, "1up":0.0, "1down":0.0}
                    
                alphas[tkey][pkey][hs.category]["NOMINAL"] = alpha
                alphas[tkey][pkey][hs.category]["1up"] = alpha + err_up
                alphas[tkey][pkey][hs.category]["1down"] = alpha - err_down
                
                # - - - - fit to the target hist (P_target = aP_mj + (1-a)P_wj) 
                alpha_mj_hist = mj_hist.Clone()
                alpha_mj_hist.Scale(alpha)

                alpha_wj_hist = wj_hist.Clone()
                alpha_wj_hist.Scale(1 - alpha)

                target_fit_hist = alpha_mj_hist.Clone()
                target_fit_hist.Add(alpha_wj_hist)

                # - - - - get the fit function
                target_fit_func = ROOT.TGraph(target_fit_hist)
                target_hists_dict[tkey][pkey][hs.category] += [target_fit_func]
    
    ## - - - - cache alphas to yml and cxx macros
    if cache:
        with open(cache, "w") as cfile:
            yaml.dump(alphas, cfile, default_flow_style=False)

        cxx_file = cache.replace(".yml", ".cxx")
        with open(cxx_file, "w") as cxx_cache:
            cxx_cache.write("#include <iostream>\n")
            for syst in ["NOMINAL", "1up", "1down"]:
                cxx_cache.write(
                    "float GetFFCombined_%s(float pt, int ntracks, float FF_CR_MULTIJET, float FF_CR_WJETS, int index){\n"%syst)
                for index, cat in enumerate(regions):
                    cxx_cache.write("\t //! Combined FFs for ({}) target region\n".format(cat.name))
                    cxx_cache.write("\t if (index==%i) {\n"%(cat.ff_index))

                    ## special categories 
                    if cat.name=="DILEP_BTAG": #<! 99 % ttbar! no fakes 
                        cxx_cache.write("\t return 0;\n\t}\n")
                        continue
                    if cat.name in ["FF_CR_MULTIJET", "FF_CR_WJETS"]:
                        cxx_cache.write("\t return %s;\n\t}\n"%cat.name)
                        continue

                    for itk in ntracks:
                        tkey = "%i"%itk
                        cxx_cache.write("\t\t if(ntracks==%i){\n"%itk)
                        for pT in fitting_bins[tkey][2:]:
                            pkey = "%i"%pT
                            if not cat.name in alphas[tkey][pkey]:
                                log.warning("alpha for %s category is missing; skipping"%cat.name)
                                continue
                            alpha = alphas[tkey][pkey][cat.name][syst]
                            cxx_cache.write("\t\t\t if(pt < {0}) return ({1}*FF_CR_MULTIJET) + ({2}*FF_CR_WJETS);\n".format(pT, alpha, 1 - alpha ))
                        cxx_cache.write("\t\t\t else return 0;\n")                                
                        cxx_cache.write("\t\t }\n")

                    # - - - -  close ntracks block
                    cxx_cache.write("\t\t else return 0;\n")
                    cxx_cache.write("\t }\n")

                # - - - - close index block
                cxx_cache.write("\t else return 0;\n")
                cxx_cache.write("}\n\n\n")

    if validation_plots:
        log.info("processing validation plots")
        validate_template_fit(cr_hists_dict, target_hists_dict, chi2s,
                              ntracks=ntracks, fitting_bins=fitting_bins, target_regions=regions, shape_vars=shape_vars, pdir=pdir)
            
    return alphas

        
##--------------------------------------------------------------------------
## - - control regions Fake Factors plotting funtions 
##--------------------------------------------------------------------------
def plot_cr_ffs(cr_ffs, cr_labels={},
                jet_rnn_key="NOMINAL", suffix="", pdir="", pname="FFs_inclusive_tracks_pT.png",
                logy=True, logx=True, formats=[".png"], data_info="#sqrt{13} TeV",
                colors=[ROOT.kBlack, ROOT.kGreen, ROOT.kRed, ROOT.kBlue,]):
    """
    
    """
    canvas = ROOT.TCanvas("c", "c", 800, 700)
    cr_ff_legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    
    # - - - - retrive hists 
    graphs = []
    for cr in cr_ffs.keys():
        for itk, bins in cr_ffs[cr][jet_rnn_key].iteritems():
            bin_keys = sorted([float(b) for b in bins.keys()])
            e_graph = ROOT.TGraphAsymmErrors(len(bins)-1)
            for n in range(len(bin_keys)-1):
                pt = bin_keys[n]

                ## NOMINAL 
                ff = float(cr_ffs[cr][jet_rnn_key][itk]["%i"%pt])

                ## syst error (variation of LOOSE TAU)
                ff_up = float(cr_ffs[cr][jet_rnn_key.replace("NOMINAL", "1up")][itk]["%i"%pt]) #not used anymore
                ff_dn = float(cr_ffs[cr][jet_rnn_key.replace("NOMINAL", "1down")][itk]["%i"%pt]) #not used anymore

                ## syst error (varaition of MC subtraction) 
                ff_mcsubt_up = float(cr_ffs[cr][jet_rnn_key.replace("NOMINAL", "MCSubt_1up")][itk]["%i"%pt])
                ff_mcsubt_dn = float(cr_ffs[cr][jet_rnn_key.replace("NOMINAL", "MCSubt_1down")][itk]["%i"%pt])

                up = math.sqrt((ff-ff_up)**2 + (ff-ff_mcsubt_up)**2)
                dn = math.sqrt((ff-ff_dn)**2 + (ff-ff_mcsubt_dn)**2)

                x_dumm = (bin_keys[n]+bin_keys[n+1])/2. #<! just to make plots look nicer 
                e_graph.SetPoint(n, x_dumm, ff)
                e_graph.SetPointError(n, x_dumm-pt, x_dumm-pt, dn, up)
                
            graphs += [e_graph]
            label = cr_labels[cr] if cr_labels else cr
            if "MULTIJET" in cr:
                label = "Mj CR"
            if "WJETS" in cr:
                label = "Wj CR"

            cr_ff_legend.AddEntry(e_graph, "%s (%sp)"%(label, itk), "LP")

    ## set log scales before any plot is drwan !
    if logx:
        canvas.SetLogx()
    if logy:    
        canvas.SetLogy()

    # - - - - plot them
    while len(graphs) > len(colors):
        colors += [c+2 for c in colors]
        
    n = 0
    for gr, cl in zip(graphs, colors):
        gr.SetMarkerStyle(20+n)
        gr.SetMarkerSize(2)
        gr.SetLineWidth(3)
        gr.SetMarkerColor(cl)
        gr.SetLineColor(cl)
        if n==0:
            gr.SetMaximum(10)
            gr.SetMinimum(0.001)
            gr.Draw("APSAME")
            canvas.Update()
            gr.SetTitle("")
            gr.GetYaxis().SetTitle("Fake-Factor")
            gr.GetXaxis().SetTitle("p^{#tau}_{T} [GeV]")
            canvas.Modified()
        else:
            gr.Draw("PSAME")
        n += 1

    cr_ff_legend.Draw("SAME")

    region_label, data_label, atlas_label = label_plot(canvas, 
        data_info=data_info, atlas_label="")
    data_label.Draw("SAME")
    atlas_label.Draw("SAME")

    os.system("mkdir -p %s"%pdir)
    log.info(os.path.join(pdir, pname))
    for fmt in formats:
        canvas.Print(os.path.join(pdir, pname+fmt))
    canvas.Close()

    return canvas 

##--------------------------------------------------------------------------
## - - template fit validation plots
##--------------------------------------------------------------------------
def validate_template_fit(cr_hists_dict, target_hists_dict, chi2s,
                          ntracks=[1, 3], fitting_bins=[], target_regions=[], shape_vars=[], pdir="ffplots", formats=[".png"]):
    """
    """

    # - - - - prep out dir for the plots
    os.system("mkdir -p %s"%pdir)
    
    canvas = ROOT.TCanvas("c","c", 1800, 600)
    canvas.Divide(3,1)

    for itk in ntracks:
        tkey = "%i"%(itk)
        # - - - - different vars for 1p and 3p taus
        var = rQCD_VARS[tkey]
        pt_bins = fitting_bins[tkey]   
        for n in range(1, len(pt_bins)):
            pkey = "%i"%pt_bins[n]

            ## - - prep labels for the plots
            pad = canvas.GetPad(1)
            dinfo = " #sqrt{#font[52]{s}} = 13 TeV"
            _, data_label, atlas_label, = label_plot(pad,
                                data_info=dinfo,
                                atlas_label="",
                                textsize=15,)
            binning_label = ROOT.TLatex(pad.GetLeftMargin() + 0.0, 1 - pad.GetTopMargin() - 0.15,
                                       "%ip; %i GeV < p^{#tau}_{T} < %i GeV"%(itk, int(pt_bins[n-1]), int(pt_bins[n])))
            binning_label.SetNDC()
            binning_label.SetTextFont(43)
            binning_label.SetTextSize(15)
            labels = [data_label, atlas_label, binning_label]
            
            ##--------------------------------------------------------
            # - - plot FF CR hists
            ##--------------------------------------------------------
            canvas.cd(1)
            cr_legend = ROOT.TLegend(0.6, 0.8, 0.9, 0.9)
            if not cr_hists_dict[tkey][pkey]:
                log.warning("Missing (%s, %s) bin in CR hists"%(tkey, pkey))
                continue

            wj_hist, mj_hist = cr_hists_dict[tkey][pkey]
            mj_hist.Sumw2()
            wj_hist.Sumw2()

            ymax = 1.5* max(mj_hist.GetMaximum(), wj_hist.GetMaximum())
            mj_hist.GetYaxis().SetRangeUser(0, ymax)
            wj_hist.GetYaxis().SetRangeUser(0, ymax)
            
            wj_hist.SetMarkerColor(ROOT.kRed)
            wj_hist.SetLineColor(ROOT.kRed)
            wj_hist.GetXaxis().SetTitle(var.title)

            wj_hist.GetYaxis().SetTitle("fraction of events")
            cr_legend.AddEntry(wj_hist, "W-jets CR", "P")

            mj_hist.SetMarkerColor(ROOT.kBlack)
            mj_hist.SetLineColor(ROOT.kBlack)
            cr_legend.AddEntry(mj_hist, "Multi-jets CR", "P")

            wj_hist.Draw("")
            mj_hist.Draw("SAME")

            ## - - draw all the labels
            for label in labels:
                label.Draw("SAME")
            cr_legend.Draw("SAME")

            ##--------------------------------------------------------
            # - - plot target regions hists and fitted functions
            ##--------------------------------------------------------
            for cat in [tr.name for tr in target_regions]:
                canvas.cd(2)
                if not pkey in target_hists_dict[tkey]:
                    log.warning("missing TARGET %s %s "%(tkey, pkey))
                    continue
                if not cat in target_hists_dict[tkey][pkey]:
                    log.warning("missing TARGET %s %s  %s"%(cat, tkey, pkey))
                    continue

                tr_legend = ROOT.TLegend(0.6, 0.8, 0.9, 0.9) 
                target_hist, target_fit = target_hists_dict[tkey][pkey][cat]

                tr_ymax = 1.5* target_hist.GetMaximum()
                target_fit.GetYaxis().SetRangeUser(0, tr_ymax)
                target_fit.SetMarkerColor(ROOT.kRed)
                target_fit.SetLineColor(ROOT.kRed)
                target_fit.Draw("APC")

                target_hist.SetMarkerColor(ROOT.kBlack)
                target_hist.SetLineColor(ROOT.kBlack)
                target_fit.GetXaxis().SetTitle(var.title)
                target_fit.GetYaxis().SetTitle("Normalized Events")
                target_hist.Draw("SAME")


                lg = "%s region"%cat
                if cat=="SR_TAUJET":
                    lg = "#tau-jet"
                if cat=="SR_TAULEP":
                    lg = "#tau-lep"

                tr_legend.AddEntry(target_hist, lg, "P")
                tr_legend.AddEntry(target_fit, "fit", "L")

                # - - add legends, labels and save canvas
                tr_legend.Draw("SAME")
                for label in labels: 
                    label.Draw("SAME")
                
                ##--------------------------------------------------------
                # - - plot chi2
                ##--------------------------------------------------------

                canvas.cd(3)
                a_legend = ROOT.TLegend(0.6, 0.8, 0.9, 0.9) 

                chi2_graph = chi2s[tkey][pkey][cat]
                ci_ymax = 1.3 * max(chi2_graph.GetY())
                ci_ymin = min(chi2_graph.GetY())
                chi2_graph.SetLineWidth(4)
                chi2_graph.SetLineColor(ROOT.kBlack)
                chi2_graph.GetYaxis().SetRangeUser(0, ci_ymax)
                chi2_graph.Draw("AL")
                chi2_graph.GetXaxis().SetTitle("#alpha_{MJ}")
                chi2_graph.GetYaxis().SetTitle("#chi^{2}/n.d.f")

                for label in labels:
                    label.Draw("SAME")

                # - - find up/dn error on the Chi2 min and draw a line there
                xmin, err_up, err_dn =  chi2_error(chi2_graph)
                
                ymax = 0.6*ci_ymax
                tline = ROOT.TLine(xmin, 0, xmin , ymax)
                tline.SetLineColor(ROOT.kRed)
                tline.SetLineWidth(4)
                tline.Draw("SAME")

                tline_up = ROOT.TLine(xmin+err_up, 0, xmin+err_up, ymax)
                tline_up.SetLineColor(ROOT.kRed)
                tline_up.SetLineWidth(3)
                tline_up.SetLineStyle(4)
                tline_up.Draw("SAME")
                
                tline_dn = ROOT.TLine(xmin-err_dn, 0, xmin-err_dn, ymax)
                tline_dn.SetLineColor(ROOT.kRed)
                tline_dn.SetLineWidth(3)
                tline_dn.SetLineStyle(4)
                tline_dn.Draw("SAME")

                a_legend.AddEntry(chi2_graph, "#chi^{2}/n.d.f=%0.2f"%(ci_ymin), "L")
                a_legend.AddEntry(tline, "#alpha_{MJ}=%0.2f"%(xmin), "L")
                a_legend.AddEntry(tline_up, "#pm#sigma", "L")
                a_legend.Draw("SAME")

                outname = os.path.join(pdir, "FFs_FIT_%s_%s_%i_%s"%(cat, tkey, pt_bins[n-1], pkey))
                for fmt in formats:
                    canvas.Print(outname+fmt) 
                
    return canvas 


##--------------------------------------------------------------------------
## - - plot alpha
##--------------------------------------------------------------------------
def plot_alpha(alphas, cr_ffs,
               regions=[], pdir="ffplots", suffix=None, data_info=None, formats=[".png"],logy=True, 
               colors=[ROOT.kRed, ROOT.kBlue, ROOT.kBlack, ROOT.kMagenta, ROOT.kOrange, ROOT.kGreen, ROOT.kYellow, ROOT.kGray]):
    """plot alpha as a function of pT for 1p/3p taus
    """
    
    ## - - prep outdir 
    os.system("mkdir -p %s"%pdir)

    ## - - make sure enough color is registered :D
    while len(regions) > len(colors):
        colors += [c+4 for c in colors]
    
    alpha_graphs = []
    comb_ff_graphs = []
    a_legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    tkeys = alphas.keys()
    for itk in tkeys:

       #different pt bins for FF_CR and alpha_MJ estimation
       pt_bins = sorted([int(k) for k in alphas[itk].keys()])  
       ff_pt_bins = sorted([int(k) for k in cr_ffs["FF_CR_MULTIJET"]["MCSubt_1up"][itk].keys()])
                   
       for ic, cat in enumerate(regions):
           log.info("\n****************** rQCD estimation (category:{0}, nTracks={1}) ******************".format(cat.name, itk))
           alpha_g = ROOT.TGraphAsymmErrors(len(pt_bins) - 1)
           #mj comb_ff_g = ROOT.TGraphAsymmErrors(len(pt_bins) - 1) -> differebt
           comb_ff_g = ROOT.TGraphAsymmErrors(len(ff_pt_bins) - 1)

           for nbin in range(len(ff_pt_bins)-1):
               pt = ff_pt_bins[nbin]
               pt_alpha = ff_pt_bins[nbin+1]
               pkey = "%i"%pt
               pkey_alpha = "%i"%pt_alpha

               ## Correction due to different pt binning -> above 80 GeV take last pt bin
               if pkey in ('80', '100', '200'):
                   pkey_alpha = '3500'

               if not pkey_alpha in alphas[itk]:
                   log.warning("No alpha is fitted for %s bin; combined FF is set to Mj FF!"%pkey_alpha)
                   alpha = 1
                   alpha_up = alpha_down = 0.001
               else:
                   if not cat.name in alphas[itk][pkey_alpha]:
                       log.warning("Missing %s in %s; setting alpha to 1"%(cat.name, pkey_alpha)) 
                       alpha = 1
                       alpha_up = alpha_down = 0.001                    
                   else:
                       alpha = alphas[itk][pkey_alpha][cat.name]["NOMINAL"]
                       alpha_up = abs(alpha-alphas[itk][pkey_alpha][cat.name]["1up"])
                       alpha_down = abs(alpha-alphas[itk][pkey_alpha][cat.name]["1down"])
                       
                       
               ## symmetric error (too large errors --> not beautiful plots --> drop them from plots)
               symt_alpha_err = max(alpha_up, alpha_down)
               # if logy:
                #     symt_alpha_err = 0.434*symt_alpha_err/alpha 

               ## - - ff_com = alpha * ff_mj + (1-alpha)ff_wj

               ff_mj_nom = float(cr_ffs["FF_CR_MULTIJET"]["NOMINAL"][itk][pkey]) #not used anymore
               ff_wj_nom = float(cr_ffs["FF_CR_WJETS"]["NOMINAL"][itk][pkey]) #not used anymore
               
               ff_mj_up = abs(ff_mj_nom - float(cr_ffs["FF_CR_MULTIJET"]["MCSubt_1up"][itk][pkey]))
               ff_wj_up = abs(ff_wj_nom - float(cr_ffs["FF_CR_WJETS"]["MCSubt_1up"][itk][pkey]))

               ff_mj_down = abs(ff_mj_nom - float(cr_ffs["FF_CR_MULTIJET"]["MCSubt_1down"][itk][pkey]))
               ff_wj_down = abs(ff_wj_nom - float(cr_ffs["FF_CR_WJETS"]["MCSubt_1down"][itk][pkey]))

               ## error propagation 
               ff = alpha*ff_mj_nom + (1-alpha)*ff_wj_nom 
               ff_up = math.sqrt((ff_mj_nom - ff_wj_nom)**2 * alpha_up**2 + (alpha*ff_mj_up)**2 + ((1-alpha)*ff_wj_up)**2)
               ff_down = math.sqrt((ff_mj_nom - ff_wj_nom)**2 * alpha_down**2 + (alpha*ff_mj_down)**2 + ((1-alpha)*ff_wj_down)**2)

               ## symmetric error 
               symt_ff_err = max(ff_up, ff_down)

               x_dumm = (ff_pt_bins[nbin]+ff_pt_bins[nbin+1])/2. #<! just to make plots look nicer 

               ## Correction due to different pt binning
               if pkey not in ('80', '100', '200'):
                   alpha_g.SetPoint(nbin, x_dumm, alpha)
                   alpha_g.SetPointError(nbin, x_dumm-pt, x_dumm-pt, symt_alpha_err, symt_alpha_err)
               if pkey == '80':
                   x_dumm = (pt_bins[nbin]+pt_bins[nbin+1])/2.
                   alpha_g.SetPoint(nbin, x_dumm, alpha)
                   alpha_g.SetPointError(nbin, x_dumm-pt, x_dumm-pt, symt_alpha_err, symt_alpha_err)
                   
               x_dumm = (ff_pt_bins[nbin]+ff_pt_bins[nbin+1])/2. #<! just to make plots look nicer

               comb_ff_g.SetPoint(nbin, x_dumm, ff)
               comb_ff_g.SetPointError(nbin, x_dumm-pt, x_dumm-pt, symt_ff_err, symt_ff_err)
               log.info("(pT, alpha, FF): {}, {}, {}".format(x_dumm, alpha, ff))


           alpha_graphs.append(alpha_g)            
           comb_ff_graphs.append(comb_ff_g)
           a_legend.AddEntry(alpha_g, "%s(%sp)"%(cat.label, itk), "LP")


    canvas = ROOT.TCanvas("c", "c", 800, 600)
    ## - - prep labels for the plots
    cat_label, data_label, atlas_label, = label_plot(canvas, data_info=data_info)
    labels = [data_label, atlas_label]
    for cnt, ah in enumerate(alpha_graphs):
        ah.SetLineColor(colors[cnt])
        ah.SetMarkerColor(colors[cnt])
        ah.SetMarkerStyle(21+cnt)
        ah.SetMarkerSize(2)
        ah.SetLineWidth(3)
        if cnt==0:
            ah.Draw("AP")
        else:
            ah.Draw("PSAME")
        canvas.SetLogx() #<! CALL IT BEFORE DOING ANYTHING WITH AXIS RANGE!
        ah.GetYaxis().SetTitle("#alpha_{MJ}")
        ah.GetXaxis().SetTitle("p^{#tau}_{T} [GeV]")
        ah.GetXaxis().SetRangeUser(30, 4000)
        ah.GetYaxis().SetRangeUser(-4, 4)
        # MM pT binning needs to be fixed 
            
    for label in labels:
        label.Draw("SAME")
    a_legend.Draw("SAME")
    
    for fmt in formats:
        a_outname = os.path.join(pdir, "ALPHA_inclusive_%s%s"%( "_"+suffix if suffix else "", fmt) )
        log.info("Saving %s ..."%a_outname)
        canvas.Print(a_outname)
    canvas.Clear()
    canvas.Close()

    canvas = ROOT.TCanvas("c", "c", 800, 600)
    
    ## plot combined Fake-Factors 
    ym = 0
    for cnt, fh in enumerate(comb_ff_graphs):
        fh.SetLineColor(colors[cnt])
        fh.SetMarkerColor(colors[cnt])
        fh.SetMarkerSize(2)
        fh.SetMarkerStyle(21+cnt)
        fh.SetLineWidth(3)
        if cnt==0:
            fh.Draw("AP")
        else:
            fh.Draw("PSAME")
        canvas.SetLogx()
        fh.GetYaxis().SetTitle("Combined Fake-Factor")
        fh.GetXaxis().SetTitle("p^{#tau}_{T} [GeV]")
        fh.GetXaxis().SetRangeUser(30, 4000)
        fh.GetYaxis().SetRangeUser(0.0, 0.25)
        #fh.GetYaxis().SetRangeUser(0.0, 0.04) 
        
    #canvas.SetLogy()
    for label in labels:
        label.Draw("SAME")
    a_legend.Draw("SAME")

    for fmt in formats:
        ff_outname = os.path.join(pdir, "FFs_COM_inclusive_%s%s"%( "_"+suffix if suffix else "", fmt))
        log.info("Saving %s ..."%ff_outname)
        canvas.Print(ff_outname) 
    
    canvas.Clear()
    canvas.Close()


##--------------------------------------------------------------------------
## - - correct upsilon
##--------------------------------------------------------------------------
def correct_upsilon(hists, cr_regions, 
    cache="UpsilonCorrection.cxx", outdir="./", formats=[".png"]):
    """ MED tau and anti-tau have different upsilon shapes --> need 
    ## a correction for QCD fakes estimated with FFs method.
    ## Smirnov transform: https://en.wikipedia.org/wiki/Inverse_transform_sampling
    ## Y_corr = CDF^-1 (CDF_tau(Y))
    """
    
    ## prep outdir 
    os.system("mkdir -p %s"%outdir)

    ## tmp containers
    cdfs = {}
    fits = {}
    upsilon_corrected = {}
    ufile = open(cache, "w")
    ufile.write("//! Upsilon Correction Macro\n")

    canvas = ROOT.TCanvas("c", "c", 800, 600)
    legend = ROOT.TLegend(0.75, 0.8, 0.9, 0.9)        
    cdf_leg = ROOT.TLegend(0.7, 0.3, 0.9, 0.4)
    labels = label_plot(canvas, data_info="139 fb^{-1}; #sqrt{13} TeV")
    for cr in cr_regions:
        if not cr.name in cdfs:
            cdfs[cr.name] = {"TAU":  [], "ANTITAU": []}
        if not cr.name in fits:
            fits[cr.name] = {"TAU":  [], "ANTITAU": []}
        if not cr.name in upsilon_corrected:
            upsilon_corrected[cr.name] = []

        tau_hist = filter(lambda h: h.category==cr.name+"_TAU", hists)[0].hist.Clone()
        antitau_hist = filter(lambda h: h.category==cr.name+"_ANTITAU", hists)[0].hist.Clone()
        
        tau_hist.Scale(1./tau_hist.Integral())
        antitau_hist.Scale(1./antitau_hist.Integral())

        tau_hist.SetMarkerColor(ROOT.kBlack)
        antitau_hist.SetMarkerColor(ROOT.kRed)
        tau_hist.SetLineColor(ROOT.kBlack)
        antitau_hist.SetLineColor(ROOT.kRed)

        tau_hist.GetYaxis().SetTitle("Normalized Events")
        tau_hist.GetXaxis().SetTitle("#Upsilon_{#tau}")

        legend.AddEntry(tau_hist, "MED #tau", "P")
        legend.AddEntry(antitau_hist, "anti-#tau", "P")

        tau_hist.Draw("P")
        antitau_hist.Draw("SAME P")
        legend.Draw("SAME")
        for lb in labels:
            lb.Draw("SAME")

        ## save fig    
        outname = "Upsilon_distribution_%s"%cr.name
        for fmt in formats:
            canvas.Print(os.path.join(outdir, outname+fmt))
        legend.Clear()
        canvas.Clear()

        ## calculate cumulative distribution functions
        tau_int = tau_hist.Integral("width")
        antitau_int = antitau_hist.Integral("width")
        for cnt in range(1, tau_hist.GetNbinsX()-1):
            cdfs[cr.name]["TAU"].append((tau_hist.GetBinLowEdge(cnt), tau_hist.Integral(1, cnt+1))) 
            cdfs[cr.name]["ANTITAU"].append((antitau_hist.GetBinLowEdge(cnt), antitau_hist.Integral(1, cnt+1)))

        tau_cdf = ROOT.TGraph(len(cdfs[cr.name]["TAU"]), 
            array.array("d", [it[0] for it in cdfs[cr.name]["TAU"]]), array.array("d", [it[1] for it in cdfs[cr.name]["TAU"]]))
        antitau_cdf = ROOT.TGraph(len(cdfs[cr.name]["ANTITAU"]), 
            array.array("d", [it[0] for it in cdfs[cr.name]["ANTITAU"]]), array.array("d", [it[1] for it in cdfs[cr.name]["ANTITAU"]]))
        
        tau_cdf.SetMarkerColor(ROOT.kBlack)
        tau_cdf.SetLineColor(ROOT.kBlack)
        tau_cdf.SetLineWidth(3)

        antitau_cdf.SetMarkerColor(ROOT.kRed)
        antitau_cdf.SetLineColor(ROOT.kRed)
        antitau_cdf.SetLineWidth(3)

        tau_cdf.GetYaxis().SetTitle("CDF")
        tau_cdf.GetXaxis().SetTitle("#Upsilon_{#tau}")

        cdf_leg.AddEntry(tau_cdf, "MED #tau", "L")
        cdf_leg.AddEntry(antitau_cdf, "anti-#tau", "L")

        tau_cdf.Draw("AC")
        antitau_cdf.Draw("SAME")
        cdf_leg.Draw("SAME")
        for lb in labels:
            lb.Draw("SAME")

        ## save fig
        cdf_outname = "Upsilon_CDF_distribution_%s"%cr.name
        for fmt in formats:
            canvas.Print(os.path.join(outdir, cdf_outname+fmt))
        canvas.Clear()
        cdf_leg.Clear()

        ## @FIXME: more elegant way would be to do a fit
        # tau_func1 = ROOT.TF1("tau_func1", "pol3", -1, 0.9)
        # tau_func2 = ROOT.TF1("tau_func2", "pol2", 0.9, 1.2)
        # tau_func3 = ROOT.TF1("tau_func3", "pol2", 1.2, 2)
        # tau_cdf.Fit(tau_func1, "R")
        # tau_cdf.Fit(tau_func2, "R+")
        # tau_cdf.Fit(tau_func3, "R+")

        # fit = tau_cdf.GetFunction("tau_func1")
        # fit.SetMarkerColor(ROOT.kBlue)
        # fit.SetLineColor(ROOT.kBlue)
        # fit.Draw("SAME")
        

        ## direct calculation 
        nbins = len(cdfs[cr.name]["TAU"])
        Ymin = tau_hist.GetBinLowEdge(1)
        Ymax = tau_hist.GetBinLowEdge(nbins)

        ufile.write("//! Smirnov transform derived from %s control region\n"%cr.name)
        ufile.write("const float CorrectedUpsilon_%s[%i] = {\n"%(cr.name, nbins))                        

        for bn in range(1, nbins):            
            _yi = cdfs[cr.name]["ANTITAU"][bn][1]
            cnt = 1
            while(cdfs[cr.name]["TAU"][cnt][1] < _yi and cnt < nbins-1):
                cnt += 1
            y_corr = Ymin + float(cnt)*(Ymax-Ymin)/float(nbins)
            upsilon_corrected[cr.name].append(y_corr)
            ufile.write("\t %.4f,\n"%y_corr)
        ufile.write("};\n\n")

    ufile.write("float CorrectUpsilon(float upsilon, int ntracks, int ff_region){\n")
    ufile.write("\t if (ntracks!=1)\n")
    ufile.write("\t\t return upsilon;\n")

    ufile.write("\t int bin = ((upsilon-(%.4f))/(%.4f-(%.4f))) * %i;\n"%(Ymin, Ymax, Ymin, nbins))
    ufile.write("\t if (ff_region==9001)\n")
    ufile.write("\t\t return (upsilon<1.500) ? CorrectedUpsilon_%s[bin] : -2 ;\n"%cr_regions[0].name) #<! MJ CR
    ufile.write("\t else if (ff_region==9002)\n")
    ufile.write("\t\treturn (upsilon<1.500) ? CorrectedUpsilon_%s[bin] : -2 ;\n"%cr_regions[1].name) #<! WJ CR
    ufile.write("\t else\n")
    ufile.write("\t\t return upsilon;\n")
    ufile.write("}\n")
    ufile.close()

    canvas.Clear()
    canvas.Close()

    return
