## stdlib
import os, glob, copy, re, random 
import multiprocessing, signal 

## ROOT
import ROOT 

## local
from .sample import Sample, Histset, HistWorker
from ..dataset_hists import dataset_hists
from ..categories import ANTI_TAU, TAU_IS_LEP, Category
from ..cluster.parallel import close_pool
from .. import log

##---------------------------------------------------------------------------------------
## - - dedicated sample class for jets faking taus background 
##---------------------------------------------------------------------------------------
class QCD(Sample):
    #WIP: - - - - - - - -  Fake-Factor weights are different for different selection categories
    FF_TYPES = {
        "taujet": {
            "PRESELECTION":1,
            "BVETO":2,
            "TTBAR":3,
            "SR_TAUJET":3,
            "QCD":111,
            "FF_CR_MULTIJET":111},
        "taulep":{
            "FF_CR_WJETS":222,
            "TAUMU_BVETO":6,
            "TAUEL_BVETO":6,
            "DILEP_BTAG":3,
            "ZEE":4,
            "SR_TAUMU":7,
            "SR_TAUEL":7,
            "SR_TAULEP":7,
        }
    }

    FF_WCR = "GetFF02_WCR({0}, {1})"
    FF_QCD = "GetFF02_QCD({0}, {1})" 
    TEMPLATE_VARS = {
        "mc16": ("tau_0_p4->Pt()/1000.", "tau_0_n_charged_tracks"),
        "mc15": ("tau_0_pt/1000.", "tau_0_n_tracks"),}
    
    rQCD = "GetFFCombined({0}, {1}, {2}, {3}, {4})"
    
    
    @staticmethod
    def sample_compatibility(data, mc):
        if not isinstance(mc, (list, tuple)):
            raise TypeError("mc must be a list or tuple of MC samples")
        if not mc:
            raise ValueError("mc must contain at least one MC sample")
    
    def __init__(self, config, data, mc, name="QCD", label="fakes", **kwargs):
        
        # - - - - quick sanity check
        QCD.sample_compatibility(data, mc)

        # - - - - instantiate base 
        super(QCD, self).__init__(config, name=name, label=label, **kwargs)
        
        self.config = config
        self.data = data
        self.mc = mc
        self.tauid = ANTI_TAU[self.config.mc_camp]
        
    def cuts(self, **kwargs):
        """ fakes tauID MEDIUM corresponds to 
        QCD.ANTI_TAU * FF(tau_0_pt, tau_0_n_tracks) 
        """
        tauid = kwargs.pop("tauid", self.tauid)
        trigger = kwargs.pop("trigger", self.config.trigger(dtype="DATA") )
        selection = super(QCD, self).cuts(tauid=tauid, trigger=trigger, **kwargs)
        log.debug(selection)
        return selection
    
    def ff_weights(self, categories=[], **kwargs):
        """ FF weights for QCD need special treatment.
        """
        if not categories:
            categories = self.config.categories
            
        ff_weights = {}
        v0, v1 = QCD.TEMPLATE_VARS[self.config.mc_camp]
        ff_wcr = QCD.FF_WCR.format(v0, v1)
        ff_qcd = QCD.FF_QCD.format(v0, v1)
        for category in categories:
            if not category.name.upper() in QCD.FF_TYPES[self.config.channel]:
                log.warning("no dedicated FFs for %s region; using the PRESEL one"%category.name)
                ff_weight_index = 1
            else:
                ff_weight_index = QCD.FF_TYPES[self.config.channel][category.name.upper()]
            ff_weight = QCD.rQCD.format(v0, v1, ff_qcd, ff_wcr, ff_weight_index)
            ff_weights[category.name] = [ff_weight]

            #!TMPFIX for cutflow 
            if category.name.upper() in ["CLEANEVENT", "TRIGGER", "TAUPT40"]:
                ff_weights[category.name] = ["1."]
            
        return ff_weights
    
    def cutflow(self, cuts, **kwargs):
        """
        """
        categories = []
        cuts_list = []
        for name, cut in cuts.iteritems():
            if name.upper()=="TAUID":
                cut = ANTI_TAU #<! ANTI_TAU * FF 
            elif name.upper()=="TRIGGER":
                cut = self.config.trigger(dtype="DATA")
            cuts_list += [cut]
            categories.append(Category(name, cuts_list=cuts_list, mc_camp=self.config.mc_camp))
            
        field = kwargs.pop("field", self.config.variables[0])
        hists = self.hists(categories=categories,
                           fields=[field],
                           systematics=["NOMINAL"],
                           **kwargs)
        
        return hists
    
    def workers(self, categories=[],
                fields=[],
                systematics=["NOMINAL"],
                trigger=None, 
                extra_cuts=None,
                extra_weights=None,
                weighted=True,
                **kwargs):
        
        """
        """
        if not fields:
            fields = self.config.variables
        if not categories:
            categories = self.config.categories

        tauid = kwargs.pop("tauid", self.tauid)
        trigger = kwargs.pop("trigger", self.config.trigger(dtype="DATA"))
        
        # - - - - prepare categories; deep copy since we don't want change categories
        categories_cp = copy.deepcopy(categories)
        for category in categories_cp:
            # - - - - filters
            category.cuts += self.cuts(extra_cuts=extra_cuts, tauid=tauid, trigger=trigger)

        # - - - - prepare MC and FF weights
        mc_weights = self.weights(categories=categories)
        ff_weights = self.ff_weights(categories=categories)

        # - - - - MC workers
        mc_workers = []
        for mc in self.mc:
            for ds in mc.datasets:
                total_weights = {}
                for cat, weights in mc_weights.iteritems():
                    total_weights[cat] = mc_weights[cat] + ff_weights[cat]
                # - - - - lumi weight  
                if weighted:
                    # - - lumi weight
                    if ds.events !=0:
                        lumi_weight = self.config.data_lumi * reduce(
                            lambda x,y:x*y, ds.xsec_kfact_effic) / ds.events
                    else:
                        log.warning(" 0 lumi weight for %s"%ds.name)
                        lumi_weight = 0
                    for cat in categories:    
                        total_weights[cat.name] += [str(lumi_weight)]
                        
                    # - - - - one worker per systematic per dataset
                    for systematic in systematics:
                        worker = HistWorker(
                            name="%s.%s.%s"%(self.name, ds.name, systematic),
                            sample=self.name,
                            dataset=ds,
                            systematic=systematic,
                            fields=fields,
                            categories=categories_cp,
                            weights=total_weights)

                    mc_workers.append(worker)

        # - - - - DATA workers
        data_workers = []
        for ds in self.data.datasets:
            # - - - - one worker per systematic per dataset
            for systematic in systematics:
                sname = self.name
                worker = HistWorker(
                    name="%s.%s.%s"%(self.name, ds.name, systematic),
                    sample=self.name,
                    dataset=ds,
                    systematic=systematic,
                    fields=fields,
                    categories=categories_cp,
                    weights=ff_weights)

                data_workers.append(worker)

        qcd_workers = mc_workers + data_workers
        return qcd_workers

    @property
    def systematics(self):
        return ["NOMINAL"]
        
    def hists(self,
              fields=[],
              categories=[],
              systematics=["NOMINAL"],
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

        systematics = filter(lambda syst: syst in self.systematics, systematics)

        # - - - - prepare the workers
        workers = self.workers(categories=categories,fields=fields, systematics=systematics, **kwargs)
        log.info(
            "************ processing %s sample hists in parallel, njobs=%i ************"%(self.name, len(workers) ) )
        
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = [pool.apply_async(dataset_hists, (wk,)) for wk in workers]
        hist_sets = []
        for res in results:
            hist_sets += res.get(3600) #<! without the timeout this blocking call ignores all signals.

        # - - close the pool 
        close_pool(pool)

        # - - - - extract DATA/MC hists
        data_hist_set = filter(lambda hs: hs.sample.startswith("%s.DATA"%self.name), hist_sets)
        mc_hist_set = filter(lambda hs: not hs.sample.startswith("%s.DATA"%self.name), hist_sets)

        # - - - - add DATA/MC dataset hists, then subtract sum of MC from DATA
        merged_hist_set = []
        for systematic in systematics:
            for var in fields:
                for cat in categories:
                    data_hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var.name and hs.category==cat.name), data_hist_set)
                    data_hsum = reduce(lambda h1, h2: h1 + h2, [hs.hist for hs in data_hists])
                    
                    mc_hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var.name and hs.category==cat.name), mc_hist_set)
                    mc_hsum = reduce(lambda h1, h2: h1 + h2, [hs.hist for hs in mc_hists])

                    # - - subtract MC from DATA
                    qcd_hsum = data_hsum - mc_hsum
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    qcd_hsum.SetTitle(outname)
                    merged_hist_set.append(Histset(sample=self.name, category=cat.name, variable=var.name, hist=qcd_hsum) )
                    
        return merged_hist_set
                
    def merge_hists(self, hist_set=[], histsdir=None, hists_file=None, overwrite=False, write=False, **kwargs):
        """ needs a dedicated method since we have to subtract sum of MC from DATA.
        """
        log.info("merging %s hists"%self.name)

        if not hist_set:
            log.info("reading dataset hists from %s"%histsdir)
            assert histsdir, "hists dir is not provided!"
            
            # - - - - retrieve the samples hists
            data_hfiles = glob.glob("%s/%s.DATA*"%(histsdir, self.name) ) 
            mc_hfiles = list(set(glob.glob("%s/%s.*"%(histsdir, self.name) ) ) - set(data_hfiles) )

            if (not (data_hfiles and mc_hfiles)):
                log.warning(" incomplete hists for %s in %s dir"%(self.name, histsdir))
                return []

            # - - - - extract the hists 
            fields = set()
            categories = set()
            mc_hist_set = []
            # - - - - get QCD MC component hists (to be subtracted)
            for hf in mc_hfiles:
                htf = ROOT.TFile(hf, "READ")
                for systematic in self.systematics:
                    systdir = htf.Get(systematic)
                    for hname in [k.GetName() for k in systdir.GetListOfKeys()]:
                        # - - regex match the hist name
                        match = re.match(self.config.hist_name_regex, hname)
                        if match:
                            sample = match.group("sample")
                            category = match.group("category")
                            variable = match.group("variable")

                            fields.add(variable)
                            categories.add(category)

                            hist = htf.Get("%s/%s"%(systematic, hname))
                            hist.SetDirectory(0) #<! detach
                            hset = Histset(sample=sample, category=category, variable=variable,
                                           systematic=systematic, hist=hist)
                            mc_hist_set.append(hset)
                htf.Close()

            # - - - - get QCD data component hists
            data_hist_set = []
            for hf in data_hfiles:
                htf = ROOT.TFile(hf, "READ")
                for systematic in self.systematics:
                    systdir = htf.Get(systematic)
                    for hname in [k.GetName() for k in systdir.GetListOfKeys()]:
                        # - - regex match the hist name
                        match = re.match(self.config.hist_name_regex, hname)
                        if match:
                            sample = match.group("sample")
                            category = match.group("category")
                            variable = match.group("variable")

                            assert (variable in fields and category in categories), "sth missing!"

                            hist = htf.Get("%s/%s"%(systematic, hname))
                            hist.SetDirectory(0) #<! detach from the htf
                            hset = Histset(sample=sample, category=category, variable=variable,
                                           systematic=systematic, hist=hist)
                            data_hist_set.append(hset)
                htf.Close()
        else:
            # - - - - get list of categories and fields available in hist_set
            fields = list(set([hs.variable for hs in hist_set] ) )
            categories = list(set([hs.category for hs in hist_set] ) )

            # - - - - gather hists for this sample
            hist_set = filter(lambda hs: hs.sample.startswith(self.name), hist_set)
            data_hist_set = filter(lambda hs: hs.sample.startswith("%s.DATA"%self.name), hist_set)
            mc_hist_set = filter(lambda hs: not hs.sample.startswith("%s.DATA"%self.name), hist_set)
        
        # - - - - bailing out if not hists    
        if not (mc_hist_set and data_hist_set):
            log.warning("no hist is found for %s; skipping the merge!"%self.name)
            return []

        if write:
            # - - - - output file
            if not hists_file:
                hists_file = self.config.hists_file
            merged_hists_file = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")
        
        # - - - - add them up
        merged_hist_set = []
        for systematic in self.systematics:
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

                    # - - subtract MC from DATA
                    qcd_hsum = data_hsum.Clone()
                    qcd_hsum.Add(mc_hsum, -1)
                    
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    qcd_hsum.SetTitle(outname)
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

    
    
##---------------------------------------------------------------------------------------
## leptons faking a tau 
class LepFake(Sample):
        
    def __init__(self, config, mc, name="LepFake", label="l->#tau", **kwargs):
        # - - - - instantiate base 
        super(LepFake, self).__init__(config, name=name, label=label, **kwargs)
        
        self.config = config
        self.mc = mc
        self.name = name
        self.label = label
        self.leptau = TAU_IS_LEP[self.config.mc_camp]

    def cuts(self, *args, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------
        
        Returns
        -------
        cut: Cut, updated Cut type.
        """
        # - - - - drop the truth matching on lep fakes first
        kwargs.pop("truth_match_tau", None)
        cut = super(MC, self).cuts(*args, **kwargs)

        # - - - - lep-match the tau
        cut += self.leptau
        return cut
    
    def workers(self, categories=[],
                fields=[],
                systematics=["NOMINAL"],
                weighted=True,
                **kwargs):
        """
        """
        if not fields:
            fields = self.config.variables
        if not categories:
            categories = self.config.categories
            
        # - - - - prepare categories; deep copy since we don't want change categories
        categories_cp = copy.deepcopy(categories)
            
        truth_match_tau = kwargs.pop("truth_match_tau", None)
        
        # - - - - MC workers
        lepfake_workers = []
        for mc in self.mc:
            # - - - - turn off truth matching 
            lepfake_workers += mc.workers(categories=categories_cp, fields=fields,systematics=systematics,
                                          weighted=weighted,truth_match_tau=self.leptau,**kwargs)

        # - - - - add LepFake prefix to the workers names
        # - - - - so that are no mistaken with DATA/MC workers.
        for lw in lepfake_workers:
            lw.name="%s.%s"%(self.name, lw.name)

        return lepfake_workers
    

    def hists(self,
              fields=[],
              categories=[],
              systematics=["NOMINAL"],
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

        systematics = filter(lambda syst: syst in self.systematics, systematics)

        truth_match_tau = kwargs.pop("truth_match_tau", None)

        
        # - - - - prepare the workers
        workers = self.workers(categories=categories, fields=fields, systematics=systematics,
                               truth_match_tau=self.leptau, **kwargs)

        log.info(
            "************** processing %s sample hists in parallel, njobs=%i ************"%(self.name, len(workers) ) )
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = [pool.apply_async(dataset_hists, (wk,)) for wk in workers]

        hist_sets = []
        for res in results:
            hist_sets += res.get(3600) #<! without the timeout this blocking call ignores all signals.

        # - - close the pool 
        close_pool(pool)
        
        # - - - - add MC dataset hists
        merged_hist_set = []
        for systematic in systematics:
            for var in fields:
                for cat in categories:
                    mc_hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var.name and hs.category==cat.name), hist_sets)
                    mc_hsum = reduce(lambda h1, h2: h1 + h2, [hs.hist for hs in mc_hists])
                    outname = self.config.hist_name_template.format(self.name, cat.name, var.name)
                    mc_hsum.SetTitle(outname)
                    merged_hist_set.append(Histset(sample=self.name, category=cat.name, variable=var.name, hist=mc_hsum) )
                    
        return merged_hist_set
        
