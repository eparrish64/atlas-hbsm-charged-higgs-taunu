# numpy imports
import numpy as np
import glob, os, random, string  

# ROOT
import ROOT

# local imports
from . import log
from .sample import Sample, SystematicsSample, Histset
from ..lumi import LUMI
from ..cluster.parallel import FuncWorker, run_pool, map_pool

##----------------------------------------------------------------------------------
##
class DataInfo():
    """
    Class to hold lumi and collision energy info for plot labels
    """
    def __init__(self, lumi, energies):
        self.lumi = lumi
        if not isinstance(energies, (tuple, list)):
            self.energies = [energies]
        else:
            # defensive copy
            self.energies = energies[:]
        self.mode = 'root'

    def __add__(self, other):
        return DataInfo(self.lumi + other.lumi,
                        self.energies + other.energies)

    def __iadd__(self, other):
        self.lumi += other.lumi
        self.energies.extend(other.energies)

    def __str__(self):
        if self.mode == 'root':
            label = '#scale[0.7]{#int} L dt = %.1f fb^{-1}  ' % self.lumi
            label += '#sqrt{#font[52]{s}} = '
            label += '+'.join(map(lambda e: '%d TeV' % e,
                                  sorted(set(self.energies))))
        else:
            label = '$\int L dt = %.1f$ fb$^{-1}$ ' % self.lumi
            label += '$\sqrt{s} =$ '
            label += '$+$'.join(map(lambda e: '%d TeV' % e,
                                    sorted(set(self.energies))))
        return label


##----------------------------------------------------------------------------------
##
class Data(Sample):
    """
    """
    STREAMS = ("2015", "2016",)# "2017", "2018")
    def __init__(self, config,
                 name='Data',
                 label='Data',
                 blind=True,
                 **kwargs):
        # - - - - intantiate the base class
        super(Data, self).__init__(config, name=name, label=label, **kwargs)

        self.config = config
        
        # - - - - Database 
        self.db = self.config.database

        # - - - - get datasets for the streams
        self.datasets = []
        for stream in Data.STREAMS:
            dname = "data%s-Main"%stream
            self.datasets.append(self.db[dname])
        self.info = DataInfo(self.config.data_lumi / 1e3, self.config.energy)
        self.blind = blind
    
    def cuts(self, *args, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------

        Returns
        -------
        cut: Cut, updated Cut type.
        """
        cut = super(Data, self).cuts(*args, **kwargs)
        return cut
            
    @staticmethod
    def hists_from_dir(idir, fields, selection,
                       file_pattern="*",tree_name="NOMINAL"):
        files = glob.glob(os.path.join(idir, file_pattern))
        ds_chain = ROOT.TChain(tree_name)
        for f in files:
            ds_chain.Add(f)

        hists = {}
        # - - draw histograms
        for var in fields:
            if var.name in hists:
                hists[var.name] = None
            histname = var.name + "_" + ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(13))
            
            log.debug("{0} >> {1}{2}".format(var.tformula, histname, var.binning))
            log.debug(selection)
            ds_chain.Draw("{0} >> {1}{2}".format(
                var.tformula, histname, var.binning), selection)
            htmp = ROOT.gPad.GetPrimitive(histname)
            hists[var.name] = htmp.Clone()
            
        # - - - - reset the chain and go to the next dataset 
        ds_chain.Reset()

        return hists
    
    def hists(self, category,
              fields=[],
              systematic="NOMINAL",
              extra_cuts=None,
              extra_weight=None,
              weighted=False, #<! not needed; added just to benefit from Sample methods like events
              trigger=None,
              tauid=None,
              suffix=None,
              parallel=False):

        log.info("processing histograms for %s tree from %s ; category: %s"%(
            systematic, self.name, category.name))

        if not fields:
            fields = self.config.variables
            self.debug("creating hists for all the variables {}".format(fields))

        # - - - - create a default canvas for the TTree.Draw
        canvas = ROOT.TCanvas()
            
        #- - - - - - - - if blinded and SR return empty hists
        if self.blind and category.name=="SR":
            hist_set = []
            for var in fields:
                fname = "%s_category_%s_%s"%(self.name, category.name, var.name)
                hist = ROOT.TH1F(fname, fname, *var.binning)
                hist.SetXTitle(var.title)
                hist_set.append(Histset(
                    sample=self.name,
                    variable=var.name,
                    category=category.name,
                    hist=hist,
                    systematic=systematic) )
        else:
            # - - - - filters
            selection = self.cuts(
                category=category,
                trigger=trigger,
                tauid=tauid,
                systematic=systematic)
            if extra_cuts:
                selection += extra_cuts
            if tauid:
                selection +=tauid
            if extra_weight:
                selection *= extra_weight
                
            if parallel:
                hist_set = []
                workers = []
                for ds in self.datasets:
                    for idir in ds.dirs:
                        workers.append(FuncWorker(Data.hists_from_dir, idir, fields, selection,
                                                  file_pattern=ds.file_pattern) )

                run_pool(workers, n_jobs=-1)

                # - - - - merge all hists from workers  
                hists = [w.output for w in workers]

                for var in fields:
                    hlist = [hd[var.name] for hd in hists]    
                    hsum = reduce(lambda x, y: x + y, hlist)
                    fname = self.hist_name_template.format(self.name, category.name, var.name)
                    hsum.SetName(fname)
                    hsum.SetTitle(fname)
                    hsum.SetXTitle(var.title)

                    hist_set.append(Histset(
                        sample=self.name,
                        variable=var.name,
                        category=category.name,
                        hist=hsum,
                        systematic=systematic) )

            else:
                log.info("--"*60)
                data_chain =  ROOT.TChain("NOMINAL")
                for ds in self.datasets:
                    for ifile in ds.files:
                        log.debug(ifile)
                        data_chain.Add(ifile)
                log.info("DATA events (no selections): %i"%data_chain.GetEntries())
                hist_set = []
                # - - draw histograms
                for var in fields:
                    histname = var.name + "_" + ''.join(random.choice(
                        string.ascii_uppercase + string.digits) for _ in range(13))
                    log.debug(selection)
                    data_chain.Draw("{0} >> {1}{2}".format(
                        var.tformula, histname, var.binning), selection)
                    htmp = ROOT.gPad.GetPrimitive(histname)
                    hist = htmp.Clone()

                    hname = self.hist_name_template.format(self.name, category.name, var.name)
                    hist.SetName(hname)
                    hist.SetTitle(hname)
                    hist.SetXTitle(var.title)
                    hist_set.append(Histset(
                        sample=self.name,
                        variable=var.name,
                        category=category.name,
                        hist=hist,
                        systematic=systematic) )

                # - - - - reset the chain and go to the next dataset 
                data_chain.Reset()
            
        log.info("processed %s tree from %s sample; category: %s"%(
            systematic, self.name, category.name))
        canvas.Close()
        
        return hist_set 
