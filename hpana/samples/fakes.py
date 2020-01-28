# stdlib
import os
import glob
import copy
import re
import random
import multiprocessing
from collections import OrderedDict

# ROOT
import ROOT

# local
from hpana.samples.sample import Sample, MC
from hpana.containers import Histset, HistWorker
from hpana.dataset_hists import dataset_hists
from hpana.systematics import Systematic, Variation
from hpana.categories import (
    Category, ANTI_TAU, TAU_IS_LEP, TAU_IS_TRUE, TAU_IS_LEP_OR_HAD, FF_CR_REGIONS, CATEGORIES)
from hpana import log


# ---------------------------------------------------------------------------------------
# - - dedicated sample class for jets faking taus background
# ---------------------------------------------------------------------------------------
class QCD(Sample):
    """ Base class for QCD fakes 
    """

    ## control region FFs are calcualted with a the following funtions, loaded in the global ROOT scope.
    TEMPLATE_VARS = ("tau_0_p4->Pt()", "tau_0_n_charged_tracks")

    ## variations based on tau RNN score for the anti-tau definition (tau_0_jet_rnn_score_trans>) or MC contamination
    FFs_VARIATIONS = ["NOMINAL", "RNN_1up", "RNN_1down", "MCSubt_1up", "MCSubt_1down"]
    FFs = {}
    for var in FFs_VARIATIONS:
        if not var in FFs:
            FFs[var] = {}
        FFs[var]["WCR"] = "GetFF_FF_CR_WJETS_{0}({1}, {2})".format(var, *TEMPLATE_VARS) 
        FFs[var]["MJCR"] = "GetFF_FF_CR_MULTIJET_{0}({1}, {2})".format(var, *TEMPLATE_VARS)
    
    FF_WCR = "GetFF_FF_CR_WJETS_NOMINAL({0}, {1})".format(*TEMPLATE_VARS)
    FF_MJCR = "GetFF_FF_CR_MULTIJET_NOMINAL({0}, {1})".format(*TEMPLATE_VARS)
    
    ## combinined FFs are calcualted with a the following fucntion, loaded in the global ROOT scope. 
    rQCD = {
        "NOMINAL": "GetFFCombined_NOMINAL({0}, {1}, {2}, {3}, {4})",
        "1up": "GetFFCombined_1up({0}, {1}, {2}, {3}, {4})",
        "1down": "GetFFCombined_1down({0}, {1}, {2}, {3}, {4})",
        }

    ## correction factor for  (1prong) tau polarization variable (using Inverse Smirnov transformation)
    UPSILON_CORRECTED = {
        "mc15": "CorrectUpsilon({0}, tau_0_n_tracks)", #< Y, ntracks
        "mc16": "CorrectUpsilon((-999*(tau_0_n_charged_tracks!=1)) + (tau_0_upsilon_pt_based*(tau_0_n_charged_tracks==1)), tau_0_n_charged_tracks, 9002)"
    }
    
    @staticmethod
    def sample_compatibility(data, mc):
        if not isinstance(mc, (list, tuple)):
            raise TypeError("mc must be a list or tuple of MC samples")
        if not mc:
            raise ValueError("mc must contain at least one MC sample")
    
    def __init__(self, config, data, mc,
                 name="QCD", label="fakes", correct_upsilon=True, **kwargs):
        
        ## quick sanity check
        QCD.sample_compatibility(data, mc)

        ## instantiate base 
        super(QCD, self).__init__(config, name=name, label=label, **kwargs)
        
        self.config = config
        self.data = data
        self.mc = mc
        self.tauid = self.config.antitau #<! set antitau for TAUID 
        self.correct_upsilon = correct_upsilon
        
    def cuts(self, **kwargs):
        """ fakes tauID MEDIUM corresponds to 
        ANTI_TAU * FF(tau_0_pt, tau_0_n_tracks) 
        """
        tauid = kwargs.pop("tauid", self.tauid)
        trigger = kwargs.pop("trigger", self.config.trigger(dtype="DATA") )
        truth_match_tau = kwargs.pop("truth_match_tau", ROOT.TCut(""))
        selection = super(QCD, self).cuts(tauid=tauid, trigger=trigger, truth_match_tau=truth_match_tau, **kwargs)
        log.debug(selection)
        return selection
    
    def ff_weights(self, categories=[], **kwargs):
        """ FF weights for QCD need special treatment.
        """
        if not categories:
            categories = self.config.categories + self.config.ff_cr_regions + self.config.clf_regions
            
        ff_weights = {"NOMINAL": {}}
        for category in categories:
            #!TMPFIX for cutflow 
            if category.name.upper() in ["CLEANEVENT", "TRIGGER",]:
                ff_weights["NOMINAL"][category.name] = ["1."]
                continue

            ff_weight_index = category.ff_index

            # nominal
            ff_weights["NOMINAL"][category.name] = [
                QCD.rQCD["NOMINAL"].format(
                    QCD.TEMPLATE_VARS[0], QCD.TEMPLATE_VARS[1], QCD.FFs["NOMINAL"]["MJCR"], QCD.FFs["NOMINAL"]["WCR"], ff_weight_index)]   

            # variations from antitau definition
            for var in QCD.FFs_VARIATIONS:
                if not "FFs_%s"%var in ff_weights:
                    ff_weights["FFs_%s"%var] = {}
                ff_wcr = QCD.FFs[var]["WCR"]
                ff_qcd = QCD.FFs[var]["MJCR"]
                ff_weight = QCD.rQCD["NOMINAL"].format(QCD.TEMPLATE_VARS[0], QCD.TEMPLATE_VARS[1], ff_qcd, ff_wcr, ff_weight_index)
                ff_weights["FFs_%s"%var][category.name] = [ff_weight]

            # variations from template-fit 
            for var in ["1up", "1down"]:
                if not "rQCD_%s"%var in ff_weights:
                    ff_weights["rQCD_%s"%var] = {}
                ff_wcr = QCD.FFs["NOMINAL"]["WCR"]
                ff_qcd = QCD.FFs["NOMINAL"]["MJCR"]
                ff_weight = QCD.rQCD[var].format(QCD.TEMPLATE_VARS[0], QCD.TEMPLATE_VARS[1], ff_qcd, ff_wcr, ff_weight_index)
                ff_weights["rQCD_%s"%var][category.name] = [ff_weight]

        return ff_weights

    @property
    def systematics(self):
        """
        FF_CRs: anti-tau definition
        FF_COM: fit 
        """
        ff_ws = self.ff_weights()

        ## NOMINAL (This is a special case where the FF weight is provided through Systematic)
        ffs_nom = Systematic(
            "NOMINAL", _type="WEIGHT", variations=[Variation("NOMINAL", title=ff_ws["NOMINAL"], _type="WEIGHT")], )

        # variations from antitau definition
        ffs_tauID_syst = Systematic("FFs_tauID", _type="WEIGHT")
        ffs_tauID_syst.variations = [
            Variation("FFs_RNN_1up", title=ff_ws["FFs_RNN_1up"], _type="WEIGHT"),
            Variation("FFs_RNN_1down", title=ff_ws["FFs_RNN_1down"], _type="WEIGHT"),
            Variation("FFs_MCSubt_1up", title=ff_ws["FFs_MCSubt_1up"], _type="WEIGHT"),
            Variation("FFs_MCSubt_1down", title=ff_ws["FFs_MCSubt_1down"], _type="WEIGHT"),
        ]
        
        # variations from template-fit 
        ffs_rQCD_syst = Systematic("FFs_rQCD", _type="WEIGHT")
        ffs_rQCD_syst.variations = [
            Variation("rQCD_1up", title=ff_ws["rQCD_1up"], _type="WEIGHT"),
            Variation("rQCD_1down", title=ff_ws["rQCD_1down"], _type="WEIGHT"),
        ]

        return [ffs_nom, ffs_tauID_syst, ffs_rQCD_syst]

    
    def cutflow(self, cuts, **kwargs):
        """
        """
        categories = []
        cuts_list = [ROOT.TCut("tau_0_jet_rnn_loose==0")]
        ff_index = 1001
        for name, cut in cuts.iteritems():
            if name.upper()=="TAUID":
                cut = ANTI_TAU #<! ANTI_TAU * FF
                ff_index = 2001
                if self.config.channel=="taujet":
                    ff_index = 1001 
            cuts_list += [cut]
            categories.append(Category(name, ff_index=ff_index, cuts_list=cuts_list, mc_camp=self.config.mc_camp))
            
        field = kwargs.pop("field", self.config.variables[0])
        systematics = kwargs.pop("systematics", self.systematics[:1])

        ## a little tweak is needed here to get the NOMINAL properly (it's complicated!)
        ffws = self.ff_weights(categories=categories)
        nominal = self.systematics[0]
        nominal.variations[0].title = dict(ffws["NOMINAL"])
        kwargs["trigger"] = None
        hists = self.hists(categories=categories, systematics=[nominal], fields=[field], **kwargs)
    
        return hists
    
    def workers(self, 
        categories=[],
        fields=[],
        systematics=[],
        trigger=None, 
        extra_cuts=None,
        extra_weights=None,
        weighted=True,
        **kwargs):
        
        """
        """
        if not fields:
            fields = self.config.variables

        ##@FIXME: for cutflow this block should be commented out!            
        qcd_systematics = self.systematics
        if len(systematics)>0:
            systematics = filter(lambda st: st.name in [s.name for s in systematics], qcd_systematics)
        else:
            systematics = qcd_systematics            

        ## correct tau polarization for fakes
        if self.correct_upsilon:
            fields = copy.deepcopy(fields) #<! to make sure not messing around with other samples' variabels
            log.debug("correcting upsilon for %s sample"%self.name)
            for field in fields:
                if field.name=="tau_0_upsilon":
                    mcc = field.mc_camp
                    field.tformula = QCD.UPSILON_CORRECTED
        
        if not categories:
            categories = self.config.categories

        if trigger is None:
            data_triggers = self.data.triggers(categories=categories, data_streams=self.data.streams, dtype="DATA")
            mc_triggers = self.mc[0].triggers(categories=categories, data_streams=self.data.streams, dtype="MC")

        ## tauID = ANTITAU * FF
        tauid = kwargs.pop("tauid", self.tauid)

        """
        # prepare categories; deep copy since we don't want to change categories.
        # in general selections might be different for DATA and MC 
        # due to additional filters like trigger, tauid, 
        # truth-match, etc. beside the selection category cuts.
        # keep in the mind that the trigger might be different for different selection categories.
        """

        ## make sure to truth match taus to lep or hadronic tau in MC
        ## drop default tau ID and Truth Match cuts
        mc_categories = copy.deepcopy(categories)
        for mc_category in mc_categories:
            mc_category.tauid = tauid
            mc_category.truth_tau = TAU_IS_LEP_OR_HAD
            mc_category.cuts += trigger if trigger else mc_triggers[mc_category.name]
            if extra_cuts:
                mc_category.cuts += extra_cuts

        data_categories = copy.deepcopy(categories)
        for data_category in data_categories:
            data_category.tauid = tauid
            data_category.truth_tau = None
            data_category.cuts += trigger if trigger else data_triggers[data_category.name]
            if extra_cuts:
                data_category.cuts += extra_cuts

        ## prepare MC and FF weights
        mc_weights = self.weights(categories=categories)
        ff_weights = self.ff_weights(categories=categories)

        ## MC workers
        mc_workers = []
        for mc in self.mc:
            for ds in mc.datasets:
                total_weights = {}
                for cat, weights in mc_weights.iteritems():
                    total_weights[cat] = mc_weights[cat][:]

                ## lumi weight  
                if weighted:
                    if ds.events !=0:
                        if ds.lumi_weight:
                            lumi_weight = self.data_lumi(ds.stream) * ds.lumi_weight
                        else:
                            lumi_weight = (self.data_lumi(ds.stream) * ds.xsec_kfact_effic) / ds.events
                    else:
                        log.warning(" 0 lumi weight for %s"%ds.name)
                        lumi_weight = 0
                    for cat in categories:    
                        total_weights[cat.name] += [str(lumi_weight)]
                        
                ## one worker per systematic per dataset
                worker = HistWorker(
                    name="%s.%s"%(self.name, ds.name),
                    sample=self.name,
                    dataset=ds,
                    systematics=systematics,
                    fields=fields,
                    categories=mc_categories,
                    weights=total_weights,
                    channel=self.config.channel)
                mc_workers.append(worker)

        ## DATA workers
        data_workers = []
        for ds in self.data.datasets:
            ## @FIXME 2018 triggers are not available in 2015-2017 samples (v06 ntuples)
            if not isinstance(self, MC):
                # - - defensive copy 
                data_categories = copy.deepcopy(categories)
                if not trigger:
                    if not "DATA2018" in ds.name: 
                        triggers = self.triggers(data_streams=["2015", "2016", "2017"], categories=data_categories, dtype="DATA")
                    else:
                        triggers = self.triggers(data_streams=["2018"], categories=data_categories, dtype="DATA")

                for data_category in data_categories:
                    data_category.tauid = tauid
                    data_category.truth_tau = None
                    data_category.cuts += trigger if trigger else triggers[data_category.name]

            ## one worker per systematic per dataset
            sname = self.name
            worker = HistWorker(
                name="%s.%s"%(self.name, ds.name),
                sample=self.name,
                dataset=ds,
                systematics=systematics,
                fields=fields,
                categories=data_categories,
                channel=self.config.channel)
            data_workers.append(worker)

        qcd_workers = mc_workers + data_workers
        return qcd_workers
        
    def hists(self,
              fields=[],
              categories=[],
              systematics=[],
              **kwargs):
        """
        Parameters
        ----------
        category: 
            Category object; specific category oof analysis.
        fields:
            Variable;  list of variables to get histograms for them
        systematics: 
            Systematic; list of systematics 
        
        Returns
        -------
        hist_set: fields histograms.
        """
        
        if not fields:
            raise RuntimeError("no field is selected to produce hists for it")

        if not categories:
            raise RuntimeError("no category is selected to produce hists for it")

        if not systematics:
            systematics = self.systematics[:1] #<! NOMINAL

        ## prepare the workers
        workers = self.workers(categories=categories,fields=fields, systematics=systematics, **kwargs)
        log.info(
            "************ processing %s sample hists in parallel, njobs=%i ************"%(self.name, len(workers) ) )
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = [pool.apply_async(dataset_hists, (wk,)) for wk in workers]
        hist_sets = []
        for res in results:
            hist_sets += res.get(3600) #<! without the timeout this blocking call ignores all signals.

        ## extract DATA/MC hists
        data_hist_set = filter(lambda hs: hs.sample.startswith("%s.DATA"%self.name), hist_sets)
        mc_hist_set = filter(lambda hs: not hs.sample.startswith("%s.DATA"%self.name), hist_sets)

        ## add DATA/MC dataset hists, then subtract sum of MC from DATA
        merged_hist_set = self.merge_hists(hist_set=data_hist_set+mc_hist_set, write=False)

        return merged_hist_set
                
    def merge_hists(self, hist_set=[], histsdir=None, hists_file=None, overwrite=False, write=False, **kwargs):
        """ needs a dedicated method since we have to subtract sum of MC from DATA.
        """
        log.info("merging %s hists"%self.name)

        if not hist_set:
            log.info("reading dataset hists from %s"%histsdir)
            assert histsdir, "hists dir is not provided!"
            
            ## retrieve the samples hists
            data_hfiles = glob.glob("%s/%s.DATA*"%(histsdir, self.name) )             
            mc_hfiles = list(set(glob.glob("%s/%s.*"%(histsdir, self.name) ) ) - set(data_hfiles) )
            
            if (not (data_hfiles and mc_hfiles)):
                log.warning(" incomplete hists for %s in %s dir"%(self.name, histsdir))
                return []

            ## extract the hists 
            fields = set()
            categories = set()
            systematics = []
            mc_hist_set = []
            ## get QCD MC component hists (to be subtracted)
            for hf in mc_hfiles:
                htf = ROOT.TFile(hf, "READ")
                systs = [k.GetName() for k in htf.GetListOfKeys()]
                for st in systs:
                    if not st in systematics:
                        systematics += [st]
                for syst in systs:
                    systdir = htf.Get(syst)
                    for hname in [k.GetName() for k in systdir.GetListOfKeys()]:
                        # - - regex match the hist name
                        match = re.match(self.config.hist_name_regex, hname)
                        if match:
                            sample = match.group("sample")
                            category = match.group("category")
                            variable = match.group("variable")
                            fields.add(variable)
                            categories.add(category)

                            hist = htf.Get("%s/%s"%(syst, hname))
                            hist.SetDirectory(0) #<! detach
                            hset = Histset(sample=sample, category=category, variable=variable,
                                            systematic=syst, hist=hist)
                            mc_hist_set.append(hset)
                htf.Close()

            ## get QCD data component hists
            data_hist_set = []
            for hf in data_hfiles:
                htf = ROOT.TFile(hf, "READ")
                systs = [k.GetName() for k in htf.GetListOfKeys()]
                for st in systs:
                    if not st in systematics:
                        systematics += [st]
                for syst in systs:
                    systdir = htf.Get(syst)
                    for hname in [k.GetName() for k in systdir.GetListOfKeys()]:
                        # - - regex match the hist name
                        match = re.match(self.config.hist_name_regex, hname)
                        if match:
                            sample = match.group("sample")
                            category = match.group("category")
                            variable = match.group("variable")

                            assert (variable in fields and category in categories), "sth missing!"

                            hist = htf.Get("%s/%s"%(syst, hname))
                            hist.SetDirectory(0) #<! detach from the htf
                            hset = Histset(sample=sample, category=category, variable=variable,
                                            systematic=syst, hist=hist)
                            data_hist_set.append(hset)
                htf.Close()
        else:
            ## get list of categories and fields available in hist_set
            fields = list(set([hs.variable for hs in hist_set] ) )
            categories = list(set([hs.category for hs in hist_set] ) )
            systematics = list(set([hs.systematic for hs in hist_set]))

            ## gather hists for this sample
            hist_set = filter(lambda hs: hs.sample.startswith(self.name), hist_set)
            data_hist_set = filter(lambda hs: hs.sample.startswith("%s.DATA"%self.name), hist_set)
            mc_hist_set = filter(lambda hs: not hs.sample.startswith("%s.DATA"%self.name), hist_set)
        
        ## bailing out if not hists    
        if not (mc_hist_set and data_hist_set):
            log.warning("no hist is found for %s; skipping the merge!"%self.name)
            return []

        if write:
            ## output file
            if not hists_file:
                hists_file = self.config.hists_file
            merged_hists_file = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")

        ## add them up
        merged_hist_set = []
        for systematic in systematics:
            for var in fields:
                for cat in categories:
                    data_hists = filter(lambda hs: (hs.systematic==systematic and hs.variable==var and hs.category==cat), data_hist_set)
                    data_hsum = data_hists[0].hist
                    for hs in data_hists[1:]:
                        data_hsum.Add(hs.hist)
        
                    mc_hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var and hs.category==cat), mc_hist_set)
                    mc_hsum = mc_hists[0].hist
                    for hs in mc_hists[1:]:
                        mc_hsum.Add(hs.hist)
                        
                    log.debug("Category {} >> DATA: {}; MC: {}".format(cat, data_hsum.Integral(0, -1), mc_hsum.Integral(0, -1)))
                    
                    # - - subtract MC from DATA
                    qcd_hsum = data_hsum.Clone()
                    qcd_hsum.Add(mc_hsum, -1)
                    
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    qcd_hsum.SetTitle(outname)
                    qcd_hsum.SetName(outname)
                    merged_hist_set.append(
                        Histset(sample=self.name, variable=var, category=cat, systematic=systematic, hist=qcd_hsum) )

                    if write:
                        # - - write it now
                        rdir = "%s"%(systematic)
                        if not merged_hists_file.GetDirectory(rdir):
                            merged_hists_file.mkdir(rdir)
                        merged_hists_file.cd(rdir)
                        qcd_hsum.Write(outname, ROOT.TObject.kOverwrite)
                        merged_hist_set.append(qcd_hsum)
        if write:
            merged_hists_file.Close()
        
        return merged_hist_set

    
    
# ---------------------------------------------------------------------------------------
# - - leptons faking a tau 
# ---------------------------------------------------------------------------------------
class LepFake(Sample):
    """
    """
    def __init__(self, config, mc, name="LepFake", label="l->#tau", **kwargs):
        ## instantiate base 
        super(LepFake, self).__init__(config, name=name, label=label, **kwargs)
        
        self.config = config
        self.mc = mc
        self.name = name
        self.label = label
        self.leptau = TAU_IS_LEP

    def cuts(self, *args, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------
        
        Returns
        -------
        cut: Cut, updated Cut type.
        """
        ## drop the truth matching on lep fakes first
        kwargs.pop("truth_match_tau", None)
        cut = super(MC, self).cuts(*args, **kwargs)

        ## lep-match the tau
        cut += self.leptau
        return cut
    
    def workers(self, categories=[],
                fields=[],
                systematics=[],
                weighted=True,
                **kwargs):
        """
        """
        if not fields:
            fields = self.config.variables
        if not categories:
            categories = self.config.categories
            
        ## prepare categories; deep copy since we don't want change categories
        mc_categories = copy.deepcopy(categories)

        ## get leps faking tau
        for mc_cat in mc_categories:
            mc_cat.truth_tau = self.leptau
        
        ## MC workers
        lepfake_workers = []
        for mc in self.mc:
            ## turn off truth matching 
            lepfake_workers += mc.workers(categories=mc_categories, fields=fields,systematics=systematics,
                                        weighted=weighted,channel=self.config.channel, **kwargs)

        ## add LepFake prefix to the workers names
        ## so that are no mistaken with DATA/MC workers.
        for lw in lepfake_workers:
            lw.name="%s.%s"%(self.name, lw.name)

        return lepfake_workers
    
