# numpy imports
import numpy as np

# local imports
from . import log
from .sample import Sample, SystematicsSample
from ..lumi import LUMI

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
    
    def __init__(self, config, name='Data', label='Data', **kwargs):
        super(Data, self).__init__(config,
                                   scale=1.,
                                   name=name,
                                   label=label,
                                   **kwargs)
        self.config = config
        dataname = 'data%i_Main'%(int(int(self.config.year)) % 1E3)
        self.info = DataInfo(LUMI[self.config.year] / 1e3, self.config.energy)
    
    def cuts(self, *args, **kwargs):
        """Additional run number specific cuts.
        Parameters
        ----------


        Returns
        -------
        cut: Cut, updated Cut type.
        """
        # make sure year is as 4 digits
        year = self.config.year % 1000 + 2000
        run_cut = cutYearRunNum[str(year)]['data']
        cut = super(Data, self).cuts(*args, **kwargs)
        cut &= run_cut 
        return cut
        
    def draw_array(self, field_hist, category, region,
                   cuts=None,
                   weighted=True,
                   field_scale=None,
                   weight_hist=None,
                   clf=None,
                   scores=None,
                   min_score=None,
                   max_score=None,
                   regressor=None,
                   systematics=True,
                   systematics_components=None,
                   bootstrap_data=False):
        if bootstrap_data:
            scores = None
        elif scores is None and clf is not None:
            scores = self.scores(clf, category, region, cuts=cuts)
        elif isinstance(scores, dict):
            scores = scores['NOMINAL']
            if isinstance(scores, tuple):
                # ignore weights
                scores = scores[0]
        return self.draw_array_helper(field_hist, category, region,
                                      cuts=cuts,
                                      weighted=weighted,
                                      field_scale=field_scale,
                                      weight_hist=weight_hist,
                                      clf=clf,
                                      scores=scores,
                                      min_score=min_score,
                                      max_score=max_score,
                                      regressor=regressor,
                                      bootstrap_data=bootstrap_data)

