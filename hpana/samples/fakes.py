# local imports
import os, glob, copy
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

        assert histsdir, "hists dir is not provided!"
            
        # - - - - retrieve the samples hists
        data_hfiles = glob.glob("%s/%s.%s*"%(histsdir, self.name, self.data.name) ) 
        mc_hfiles = list(set(glob.glob("%s/%s.*"%(histsdir, self.name) ) ) - set(data_hfiles) )

        if (not (data_hfiles and mc_hfiles)):
            log.warning(" incomplete hists for %s in %s dir"%(self.name, histsdir))
            return
        
        # - - - - merged hists_file
        if not hists_file:
            hists_file = self.config.hists_file
        merged_hists_tfile = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")
                               
        log.info("merging %s hists"%self.name)
        # - - - - merge data and merge MC separately
        qcd_DATA_hist_file = os.path.join(histsdir, "%s_%s.root"%(self.name, self.data.name.upper()) )
        qcd_MC_hist_file = os.path.join(histsdir, "%s_MC.root"%self.name)
        
        os.system("hadd -f -j {0} {1} {2}".format(ncpu, qcd_DATA_hist_file, " ".join(data_hfiles) ) )
        os.system("hadd -f -j {0} {1} {2}".format(1, qcd_MC_hist_file, " ".join(mc_hfiles) ) )

        # - - - - now lets subtract MC from DATA
        qcd_DATA_hist_tfile = ROOT.TFile(qcd_DATA_hist_file, "READ")
        qcd_MC_hist_tfile = ROOT.TFile(qcd_MC_hist_file, "READ")

        # - - - -
        log.info("QCD: subtracting MC from DATA")
        for rdir in [k.GetName() for k in qcd_DATA_hist_tfile.GetListOfKeys()]:
            if not merged_hists_tfile.GetDirectory(rdir):
                merged_hists_tfile.mkdir(rdir)
            # - - get the list of hists    
            tdir = qcd_DATA_hist_tfile.GetDirectory(rdir)
            hists = [k.GetName() for k in tdir.GetListOfKeys()]
            for hkey in hists:
                h_data = qcd_DATA_hist_tfile.Get("{0}/{1}".format(rdir, hkey ) )
                h_mc = qcd_MC_hist_tfile.Get("{0}/{1}".format(rdir, hkey ) )
                h_qcd = h_data - h_mc
                hname = "%s_%s"%(self.name, h_data.GetName())
                h_qcd.SetTitle(hname)
                
                merged_hists_tfile.cd(rdir)
                h_qcd.Write(hname, ROOT.TObject.kOverwrite)
            
        return 
    
    
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

    def workers(self, categories=[],
                fields=[],
                systematics=["NOMINAL"],
                weighted=True,
                **kwargs):
        """
        """

        # - - - - a lepton which passes tau ID
        extra_cuts = kwargs.pop("extra_cuts", self.leptau)
            
        # - - - - MC workers
        lepfake_workers = []
        for mc in self.mc:
            # - - - - turn off truth matching 
            mc.truth_match_tau = False
            lepfake_workers += mc.workers(
                categories=categories,
                fields=fields,
                systematics=systematics,
                extra_cuts=extra_cuts,
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
        
