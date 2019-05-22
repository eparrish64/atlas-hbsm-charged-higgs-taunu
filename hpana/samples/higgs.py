# stdlib imports
import os, pickle, glob, re
from math import pi, sqrt

# local imports
from . import log
from .sample import MC, Signal
from hpana.containers import Histset

import ROOT 

class Higgs(MC, Signal):
    # - - - - - - - - - signal mass points 
    TAUJET_SIGS ={
        "LOW":{ 
            80 : "346239",
            90 : "346241",
            100 : "346243",
            110 : "346245",
            120 : "346247",
            130 : "346249",
        },
        "INT":{
            140 : "346251",
            150 : "346253",
            160 : "346255",
            170 : "346257",
            180 : "346259",
            190 : "346261",
        },
        "HIGH":{        
            200 : "346263",
            225 : "346265",
            250 : "346267",
            275 : "346269",
            300 : "346271",
            350 : "346273",
            400 : "346275",
            500 : "346277",
            600 : "346279",
            700 : "346281",
            800 : "346283",
            900 : "346285",
            1000 : "346287",
            1200 : "346289",
            1400 : "346291",
            1600 : "346293",
            1800 : "346295",
            2000 : "346297",
            2500 : "346299",
            3000 : "346301",
        }   
    }

    TAULEP_SIGS = {
        "LOW":{ 
            80 : "346238",
            90 : "346240",
            100 : "346242",
            110 : "346244",
            120 : "346246",
            130 : "346248",
        },
        "INT":{
            140 : "346250",
            150 : "346252",
            160 : "346254",
            170 : "346256",
            180 : "346258",
            190 : "346260",
        },
        "HIGH":{
            200 : "346262",
            225 : "346264",
            250 : "346266",
            275 : "346268",
            300 : "346270",
            350 : "346272",
            400 : "346274",
            500 : "346276",
            600 : "346278",
            700 : "346280",
            800 : "346282",
            900 : "346284",
            1000 : "346286",
            1200 : "346288",
            1400 : "346290",
            1600 : "346292",
            1800 : "346294",
            2000 : "346296",
            2500 : "346298",
            3000 : "346300",
        }
    }

    MASS_REGIONS_DICT = {
        "taulep":TAULEP_SIGS,
        "taujet": TAUJET_SIGS,
    } 

    ## flat masses dict
    MASSES_DICT = {"taulep":{}, "taujet": {}}
    for key in ["LOW", "INT", "HIGH"]:
        for channel in ["taulep", "taujet"]:
            for m, did in MASS_REGIONS_DICT[channel][key].iteritems():
                MASSES_DICT[channel][m] = did

    ## all masses 
    MASSES = sorted(MASSES_DICT["taujet"])

    SAMPLE_PATTERN = {
        "LOW": "MadGraphPy8EvtGen_A14NNPDF30LO_HpL_H{}",
        "INT": "MadGraphPy8EvtGen_A14NNPDF30LO_HpI_H{}",
        "HIGH": "aMcAtNloPy8EvtGen_A14NNPDF30NLO_HpH_H{}",
    }
    
    NORM_BY_THEORY = True
    
    def __init__(self, config,
                 mass=None,
                 name=None,
                 suffix=None,
                 label=None,
                 scale=1,
                 **kwargs):
        
        ## check if this mass point is supported
        assert mass in Higgs.MASSES, "unsupported %r mass"%mass

        self.config = config

        if not name:
            name = "Hplus{}".format(mass)
            # name = Higgs.MASSES_DICT[self.config.channel][mass]     
        if label is None:
            if scale!=1:
                label = '{1}#times H^+{0}'.format(mass, scale)
            else:
                label = 'H^{{+}}{0}'.format(mass)

        self.name = name
        self.label=label
        
        if mass <= 130:
            mode = "LOW"
        elif mass <= 190:
            mode = "INT"
        elif 200 <= mass <= 3000:
            mode = "HIGH"
        else:
            raise ValueError("unknown mass {} for the signal!".format(mass))
        self.mass = mass
        self.mode = mode
        
        # - - - - the samples for this signal
        self.samples = [(Higgs.SAMPLE_PATTERN[mode].format(mass)) ]
        log.debug("signal: {}".format(self.samples[0]))
        
        database = kwargs.pop("database", None)
        # - - - - instantiate the base
        super(Higgs, self).__init__(config, label=label, database=database, name=name, **kwargs)

    
    def workers(self, categories=[],
            fields=[],
            systematics=[],
            trigger=None,
            extra_cuts=None,
            extra_weight=None,
            weighted=True,
            hist_templates=None,
            **kwargs):

        weighted_workers = super(Higgs, self).workers(categories=categories,
                fields=fields,
                systematics=systematics,
                trigger=trigger,
                extra_cuts=extra_cuts,
                extra_weight=extra_weight,
                weighted=weighted,
                hist_templates=hist_templates,
                **kwargs)

        for ww in weighted_workers:
            oname = "Hplus%i"%self.mass
            ww.name = ww.name.replace(oname, oname+"WEIGHTED")

        unweighted_workers = super(Higgs, self).workers(categories=categories,
                fields=fields,
                systematics=systematics,
                trigger=trigger,
                extra_cuts=extra_cuts,
                extra_weight=extra_weight,
                weighted=False,
                hist_templates=hist_templates,
                **kwargs)

        for ww in unweighted_workers:
            oname = "Hplus%i"%self.mass
            ww.name = ww.name.replace(oname, oname+"UNWEIGHTED")

        return weighted_workers + unweighted_workers

    def merge_hists(self, hist_set=[], histsdir=None, hists_file=None, write=False, **kwargs):
        """
        first we make a histogram with the mc event weights applied normally, lets call it weighted
        then a histogram with no mc event weights, unweighted
        final = unweighted.Clone()
        norm = weighted.Integral()/unweighted.Integral() 
        final.Scale(norm)
        so the shape of the histogram is from the unweighted events, but the normalization is from the weighted events
        """

        if len(hist_set)==0:
            log.info("reading dataset hists from %s"%histsdir)
            assert histsdir, "hists dir is not provided!"
            # - - retrieve the samples hists
            w_hfiles = glob.glob("%s/%sWEIGHTED.*"%(histsdir, self.name))
            uw_hfiles = glob.glob("%s/%sUNWEIGHTED.*"%(histsdir, self.name))

            if len(w_hfiles)!=len(uw_hfiles):
                log.error("number of weighted  and unweighted histograms don't match!")
                return[]
            if len(w_hfiles)==0:
                log.warning("no hists found for the %s in %s dir"%(self.name, histsdir))
                return []

            # - - extract the hists 
            fields = set()
            categories = set()
            systematics = []
            w_hset = []
            for hf in w_hfiles:
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
                            hist.SetDirectory(0) #<! detach from htf
                            hset = Histset(sample=sample, category=category, variable=variable,
                                            systematic=syst, hist=hist)
                            w_hset.append(hset)
                htf.Close()

            uw_hset = []
            for hf in uw_hfiles:
                htf = ROOT.TFile(hf, "READ")
                systs = [k.GetName() for k in htf.GetListOfKeys()]
                for syst in systs:
                    systdir = htf.Get(syst)
                    for hname in [k.GetName() for k in systdir.GetListOfKeys()]:
                        # - - regex match the hist name
                        match = re.match(self.config.hist_name_regex, hname)
                        if match:
                            sample = match.group("sample")
                            category = match.group("category")
                            variable = match.group("variable")
                            hist = htf.Get("%s/%s"%(syst, hname))
                            hist.SetDirectory(0) #<! detach from htf
                            hset = Histset(sample=sample, category=category, variable=variable,
                                            systematic=syst, hist=hist)
                            uw_hset.append(hset)
                htf.Close()
        else:
            w_hset = filter(lambda hs: hs.sample==self.name+"WEIGHTED", hist_set)
            uw_hset = filter(lambda hs: hs.sample==self.name+"UNWEIGHTED" in hs.sample, hist_set)

        ## merge weighted/unweighted hists separately and write them to disk
        mr_w_hset = super(Higgs, self).merge_hists(hist_set=w_hset, histsdir=histsdir, hists_file=hists_file, write=False, **kwargs)
        mr_uw_hset = super(Higgs, self).merge_hists(hist_set=uw_hset, histsdir=histsdir, hists_file=hists_file, write=False, **kwargs)
        
        ## output file
        if write:
            if hists_file is None:
                hists_file = self.config.hists_file
            ofile = ROOT.TFile(os.path.join(histsdir, hists_file), "UPDATE")

        ## normalized unweighted to weighted and use that in the analysis! 
        norm_hset = []
        for uw_hs in mr_uw_hset:
            final_hist = uw_hs.hist.Clone()
            w_hs = filter(
                lambda _hs: _hs.variable==uw_hs.variable and _hs.category==uw_hs.category and _hs.systematic==uw_hs.systematic, mr_w_hset)[0]

            ## proper name for outputs 
            uw_hs.sample = self.name +"UNWEIGHTED"
            w_hs.sample = self.name +"WEIGHTED"

            w_hist = w_hs.hist
            uw_hist = uw_hs.hist

            w_intg = w_hist.Integral()
            uw_intg = final_hist.Integral()

            if(w_intg<=0):
                log.warning("%s integral is <=0  for %s sample! skipping scaling to the weighted histogram and using weighted histogram"%(final_hist.GetName(), self.name))
                final_hist = w_hist.Clone()    
            else:
                final_hist.Scale(w_intg/uw_intg)

            outname = self.config.hist_name_template.format(self.name, uw_hs.category, uw_hs.variable)
            w_outname = self.config.hist_name_template.format(self.name+"WEIGHTED", uw_hs.category, uw_hs.variable)
            uw_outname = self.config.hist_name_template.format(self.name+"UNWEIGHTED", uw_hs.category, uw_hs.variable)

            final_hist.SetName(outname)
            final_hist.SetTitle(outname)

            w_hist.SetName(w_outname)
            w_hist.SetTitle(w_outname)

            uw_hist.SetName(uw_outname)
            uw_hist.SetTitle(uw_outname)

            n_hs = Histset(sample=self.name, category=uw_hs.category, variable=uw_hs.variable, systematic=uw_hs.systematic, hist=final_hist.Clone())
            norm_hset.append(n_hs)

            print uw_hist.Integral(), w_hist.Integral(), final_hist.Integral()
            if write:
                # - - write it now
                rdir = "%s"%(uw_hs.systematic)
                if not ofile.GetDirectory(rdir):
                    ofile.mkdir(rdir)
                ofile.cd(rdir)
                final_hist.Write(outname, ROOT.TObject.kOverwrite)
                w_hist.Write(w_outname, ROOT.TObject.kOverwrite)
                uw_hist.Write(uw_outname, ROOT.TObject.kOverwrite)

        return norm_hset