# local imports
import os, glob, copy, re
import ROOT 

from .sample import Sample, Histset, HistWorker
from ..categories import ANTI_TAU, TAU_IS_LEP
from .. import log
from ..cluster.parallel import FuncWorker, Job, run_pool, map_pool

##---------------------------------------------------------------------------------------
## jets faking a tau background 
class QCD(Sample):
    #WIP: - - - - - - - -  Fake-Factor weights are different for different selection categories
    FF_TYPES = {
        "taujet": {
            "PRESELECTION":1,
            "BVETO":2,
            "TTBAR":3,
            "SR_TAUJET":3,
            "QCD":111,},
        "taulep":{
            "BVETO":6,
            "TTBar":3,
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
        selection = super(QCD, self).cuts(tauid=tauid, **kwargs)
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
            ff_weight_index = QCD.FF_TYPES[self.config.channel][category.name.upper()]
            ff_weight = QCD.rQCD.format(v0, v1, ff_qcd, ff_wcr, ff_weight_index)
            ff_weights[category.name] = [ff_weight]
            
        return ff_weights
    

    def workers(self, categories=[],
                fields=[],
                systematics=["NOMINAL"],
                extra_cuts=None,
                extra_weights=None,
                weighted=True,
                **kwargs):
        
        """
        """

        tauid = kwargs.pop("tauid", self.tauid)
        # - - - - prepare categories; deep copy since we don't want change categories
        categories_cp = copy.deepcopy(categories)
        for category in categories_cp:
            # - - - - filters
            category.cuts += self.cuts(extra_cuts=extra_cuts, tauid=tauid)

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

        systematics = filter(lambda syst: syst in self.systematics(), systematics)

        # - - - - prepare the workers
        workers = self.workers(
            categories=categories,
            fields=fields,
            systematics=systematics,
            **kwargs)

        # - - - - assign the jobs to the workers
        jobs = []
        hist_sets = []
        for worker in workers:
            jobs.append(Job(Sample.dataset_hists,
                            worker.dataset,
                            worker.fields,
                            worker.categories,
                            systematic=worker.systematic,
                            outname=worker.name,
                            **kwargs) )
            
        # - - - - process samples' datasets in parallel
        parallel = kwargs.pop("parallel", False)    
        if parallel:
            log.info(
                "************** processing %s sample hists in parallel, njobs=%i ************"%(self.name, len(jobs) ) )
            run_pool(jobs, n_jobs=-1)
            
        # - - - - - - - - process datasets one after another
        else:
            log.info("************ processing %s sample hists sequentially ************"%self.name)
            for job in jobs:
                job.run()
                

    def merge_hists(self, histsdir=None, hists_file=None, overwrite=False, ncpu=1):
        """ needs a dedicated method since we have to subtract sum of MC from DATA.
        """
        log.info("merging %s hists"%self.name)

        assert histsdir, "hists dir is not provided!"

        # - - - - merged hists file
        if not hists_file:
            hists_file = self.config.hists_file
            
        # - - - - retrieve the samples hists
        data_hfiles = glob.glob("%s/%s.DATA*"%(histsdir, self.name) ) 
        mc_hfiles = list(set(glob.glob("%s/%s.*"%(histsdir, self.name) ) ) - set(data_hfiles) )

        if (not (data_hfiles and mc_hfiles)):
            log.warning(" incomplete hists for %s in %s dir"%(self.name, histsdir))
            return

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

        # - - - - add them up
        merged_hists_file = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")
        merged_hist_set = []
        for systematic in self.systematics:
            for var in fields:
                for cat in categories:
                    data_hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var and hs.category==cat), data_hist_set)
                    data_hsum = reduce(lambda h1, h2: h1 + h2, [hs.hist for hs in data_hists])
                    
                    mc_hists = filter(
                        lambda hs: (hs.systematic==systematic and hs.variable==var and hs.category==cat), mc_hist_set)
                    mc_hsum = reduce(lambda h1, h2: h1 + h2, [hs.hist for hs in mc_hists])

                    qcd_hsum = data_hsum - mc_hsum
                    outname = self.config.hist_name_template.format(self.name, cat, var)
                    qcd_hsum.SetTitle(outname)

                    # - - write it now
                    rdir = "%s"%(systematic)
                    if not merged_hists_file.GetDirectory(rdir):
                        merged_hists_file.mkdir(rdir)
                    merged_hists_file.cd(rdir)
                    qcd_hsum.Write(outname, ROOT.TObject.kOverwrite)
                    merged_hist_set.append(qcd_hsum)

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
        # - - - - prepare categories; deep copy since we don't want change categories
        categories_cp = copy.deepcopy(categories)
            
        # - - - - MC workers
        lepfake_workers = []
        for mc in self.mc:
            # - - - - turn off truth matching 
            lepfake_workers += mc.workers(
                categories=categories_cp,
                fields=fields,
                systematics=systematics,
                truth_match_tau=self.leptau,
                weighted=weighted,
                **kwargs)

        # - - - - add LepFake prefix to the workers names
        # - - - - so that are no mistaken with DATA/MC workers.
        for lw in lepfake_workers:
            lw.name="%s.%s"%(self.name, lw.name)

        return lepfake_workers
    
    def hists(self, category,
              fields=[],
              systematic="NOMINAL",
              extra_cuts=None,
              extra_weight=None,
              weighted=True,
              trigger=None,
              tauid=None,
              suffix=None,
              hists_file=None,
              parallel=False,
              write_hists=True,
              overwrite=True):
        """
        """
        log.info("processing %s tree from %s ; category: %s"%(
            systematic, self.name, category.name))
    
        # - - - - a lepton which passes tau ID  
        if not extra_cuts:
            extra_cuts = self.leptau
        else:
            extra_cuts += self.leptau
            
        # - - - - - - - - mc 
        mc_hists = []
        for m in self.mc:
            # - - - - turn off truth matching 
            m.truth_match_tau = False
            mc_hists += m.hists(
                categories=[category],
                fields=fields,
                extra_cuts=extra_cuts,
                weighted=weighted,
                trigger=trigger,
                parallel=parallel,
                write_hists=False)
        
        # - - - - - - - - 
        lepfake_hist_set = []
        for var in fields:
            h_mc = filter(lambda h: h.variable==var.name, mc_hists)
            h_mc = [h.hist for h in h_mc]
            h_mc_sum = reduce(lambda h1, h2: h1+h2, h_mc)

            # - - - - get the fakes hist and set it's name
            fname = self.hist_name_template.format(self.name, category.name, var.name)
            h_mc_sum.SetName(fname)
            h_mc_sum.SetTitle(fname)
            h_mc_sum.SetXTitle(var.title)
            
            lepfake_hist_set.append(Histset(
                sample=self.name,
                variable=var.name,
                category=category.name,
                hist=h_mc_sum,
                systematic=systematic) )
            
        log.info("proccessed %s tree from %s ; category=%s"%(
            systematic, self.name, category.name))

        if write_hists:
            if not hists_file:
                hists_file = self.config.hists_file
            self.write_hists(
                lepfake_hist_set, hists_file, systematic=systematic, overwrite=overwrite)

        return lepfake_hist_set
        
