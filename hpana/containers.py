"""
Container classes for histograms and workers.
"""

import ROOT

##---------------------------------------------------------------------------------------
## - - Hist container class
##--------------------------------------------------------------------------
class Histset:
    """simple container class for histograms
    """
    def __init__(self,
                 name="Histset",
                 sample=None,
                 variable=None,
                 category=None,
                 hist=None,
                 systematic="NOMINAL",):
        self.sample = sample
        self.name = name
        self.variable =variable
        self.category = category
        self.systematic = systematic
        self.hist = hist
    def __repr__(self):
        integral = "NAN"
        if self.hist:
            integral = self.hist.Integral(0, -1) if isinstance(self.hist, ROOT.TH1F) else self.hist.Integral()
            
        return "(name=%r, sample=%r, systematic=%r, "\
            "variable=%r, category=%r, hist=%r)\n"%(
                self.name, self.sample, self.systematic,
                self.variable, self.category, integral)
    

##---------------------------------------------------------------------------------------
## - - container class for histogram workers 
##---------------------------------------------------------------------------------------
class HistWorker:
    """
    lightweight container class for histogram workers
    """
    def __init__(self, name="HistWorker",
                 channel="taujet",
                 sample=None,
                 dataset=None,
                 systematic="NOMINAL",
                 fields=[],
                 categories=[],
                 weights=[],
                 hist_templates={}):
        self.name = name
        self.channel = channel
        self.sample = sample
        self.dataset = dataset
        self.fields = fields
        self.categories = categories
        self.systematic = systematic
        self.weights = weights
        self.hist_templates = hist_templates
        
    def __repr__(self):
        return "<<< \n name=%r, sample=%r, channel=%r, systematic=%r\n"\
            "<variables>=%r\n<categories>=%r\n<weights>=%r\n<hist templates>=%r\n>>>\n"%(
                self.name, self.channel, self.sample, self.systematic,
                self.fields, self.categories, self.weights, self.hist_templates)
    
    
