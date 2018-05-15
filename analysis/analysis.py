# stdlib imports
import random
from collections import namedtuple

# numpy imports
import numpy as np

# rootpy imports
from rootpy.stats import histfactory
from rootpy.plotting import Hist

# root_numpy imports
from root_numpy import rec2array

# local imports
from statstools.utils import efficiency_cut
from . import log; log = log[__name__]
from . import norm_cache, CONST_PARAMS
from . import samples
from .samples import Higgs
from .categories.hadhad import CATEGORIES as HH_CATEGORIES
from .categories.lephad import CATEGORIES as LH_CATEGORIES
from .classify import histogram_scores, Classifier
from .regressor import Regressor, BRT_FEATURES
from .defaults import (
    TRAIN_FAKES_REGION, 
    FAKES_REGION, TARGET_REGION, 
    NORM_FIELD, NORM_FIELD_LH,
    TRIGGER_TYPE)

from .config import Configuration


MC_GENERATORS={
    'ztt': 'sherpa2', 
    'zll': 'sherpa2', 
    'wj' : 'sherpa2', 
    'diboson':'powpy' 
    }

def get_analysis(args, **kwargs):
    if 'year' in kwargs:
        year = kwargs.pop('year')
    else:
        year = args.year
    for name, value in kwargs.items():
        if hasattr(args, name):
            setattr(args, name, value)
        else:
            raise ValueError("invalid Analysis kwarg {0}".format(name))
    analysis = Analysis(
        year=year,
        channel=args.channel,
        systematics=args.systematics,
        use_embedding=args.embedding,
        target_region=args.target_region,
        fakes_region=args.fakes_region,
        decouple_qcd_shape=args.decouple_qcd_shape,
        constrain_norms=args.constrain_norms,
        qcd_shape_systematic=args.qcd_shape_systematic,
        random_mu=args.random_mu,
        mu=args.mu,
        ggf_weight=args.ggf_weight,
        suffix=args.suffix,
        trigger_type=args.trigger_type)
    return analysis


class Analysis(object):

    """ main analysis class.
    Attributes
    ----------
    systematics : bool(default=True)
              whether to do the systematics calculations or not.
    use_embedding : bool(default=True)
                if True will use the tau-embedded ztautau for z-background,
    trigger : bool(default=True) 
          if True will use trigger.
    target_region: str(default='OS_ISOL')
                analysis signal region. see .region/* for more.  
    fakes_region: str(default='nOS_ISOL') 
               region for the fakes
    
    decouple_qcd_shape : bool(default=False)
                     if True, do the qcd shape systematics separately,
                     
    coherent_qcd_shape: bool(default=False)
                     if True, do the qcd shape systematics along side others.

    qcd_workspace_norm: float 
                     Val for qcd systmatics.

    ztt_workspace_norm: float 
                     Val,  for qcd systmatics.
                     
    constrain_norms: bool(default=False)
                  asks whether to set Low, High for systmatics.

    random_mu: bool(default=False)
            whether to set signal strength randomly or not, 
    mu:float(default=1.) 
     signal strength

    ggf_weight: bool(default=True)
             if True, weights the systematics.

    suffix: str
         specific suffix for analysis to be added to the output files name.
    
    norm_field: str
             variable used to normalize qcd, ztt
    """
    
    @staticmethod
    def get_analysis(args, **kwargs):
        """
        default constructor.
        """
        if 'year' in kwargs:
            year = kwargs.pop('year')
        else:
            year = args.year
        for name, value in kwargs.items():
            if hasattr(args, name):
                setattr(args, name, value)
            else:
                raise ValueError("invalid Analysis kwarg {0}".format(name))
        analysis = Analysis(
            year=year,
            channel=args.channel,
            systematics=args.systematics,
            use_embedding=args.embedding,
            target_region=args.target_region,
            fakes_region=args.fakes_region,
            decouple_qcd_shape=args.decouple_qcd_shape,
            constrain_norms=args.constrain_norms,
            qcd_shape_systematic=args.qcd_shape_systematic,
            random_mu=args.random_mu,
            mu=args.mu,
            ggf_weight=args.ggf_weight,
            suffix=args.suffix)
        return analysis


    def __init__(self, year,
                 systematics=False,
                 use_embedding=False,
                 trigger=True,
                 trigger_type=TRIGGER_TYPE,
                 target_region=TARGET_REGION,
                 fakes_region=FAKES_REGION,
                 decouple_qcd_shape=False,
                 coherent_qcd_shape=True,
                 qcd_workspace_norm=None,
                 ztt_workspace_norm=None,
                 constrain_norms=False,
                 qcd_shape_systematic=True,
                 random_mu=False,
                 mu=1.,
                 ggf_weight=True,
                 suffix=None,
                 channel='hadhad',
                 norm_field=NORM_FIELD_LH,
                 mc_generator=MC_GENERATORS):

        # - - - - - - - - basic flags
        self.year = year
        self.systematics = systematics
        self.use_embedding = use_embedding
        self.target_region = target_region
        self.fakes_region = fakes_region
        self.suffix = suffix
        self.channel=channel
        self.norm_field = norm_field
        if self.channel == 'lephad':
            self.norm_field = NORM_FIELD_LH 
        self.trigger = trigger
        self.trigger_type = trigger_type
        if random_mu:
            log.info("using a random mu (signal strength)")
            self.mu = random.uniform(10, 1000)
        else:
            log.info("using a mu (signal strength) of {0:.1f}".format(mu))
            self.mu = mu

        self.qcd.scale = 1.
        self.ztautau.scale = 1.
        self.ggf_weight = ggf_weight

        mc_params = {}
        mc_params['year'] = year
        mc_params['channel'] =self.channel
        mc_params['trigger'] =self.trigger
        mc_params['trigger_type'] = self.trigger_type
        #mc_params['systematics'] = self.systematics,

        # - - - - - - - - analysis' main configuration 
        self.conf = Configuration(self.channel)


        # - - - - - - - - analysis MC samples 
        if use_embedding:
            log.info("Using embedded Ztautau")
            self.ztautau = samples.Embedded_Ztautau(
                workspace_norm=ztt_workspace_norm,
                constrain_norm=constrain_norms,
                color='#00A3FF',
                **mc_params)
        else:
            log.info("Using Pythia Ztautau")
            self.ztautau = samples.Pythia_Ztautau(
                name='ZTauTau',
                label='Z#rightarrow#tau#tau',
                workspace_norm=ztt_workspace_norm,
                constrain_norm=constrain_norms,
                color='#157991',#'#00A3FF',
                **mc_params)

        self.others = samples.Others(
            name='Others',
            label='Others',
            color='#8A0F0F',
            **mc_params)
        self.diboson = samples.Diboson(
            name='DiBoson',
            label='DiBoson',
            color='#7D560C',
            **mc_params)
        self.top = samples.Top(
            name='Top',
            label='Top',
            color='#B0AF0B',
            **mc_params)
        self.zll = samples.MC_Zll(
            name='Zll',
            label='Z#rightarrow ll',
            color='#061c44',
            **mc_params)
        self.wj = samples.MC_WJ(
            name='WJets',
            label='W+J',
            color='#B00B71',
            **mc_params)
        
        # - - - - - - - - Fakes drived from FF method
        self.qcd = samples.Fakes(
            name='Fakes',
            label='fakes',
            data=self.data,
            mc=[self.ztautau, self.zll, self.wj, self.others], #order Ztt then Others
            channel=self.channel,
            trigger = self.trigger,
            trigger_type = self.trigger_type,
            shape_region=fakes_region,
            decouple_shape=decouple_qcd_shape,
            coherent_shape=coherent_qcd_shape,
            workspace_norm=qcd_workspace_norm,
            constrain_norm=constrain_norms,
            shape_systematic=qcd_shape_systematic,
            color='#f8970c')

        # - - - - - - - - BKG components 
        self.backgrounds = [
            self.qcd,
            self.others,
            self.zll,
            self.wj,
            #self.top,
            #self.diboson,
            self.ztautau,
            ]

        # - - - - - - - - DATA 
        self.data = samples.Data(
            year=year,
            name='Data',
            label='Data',
            channel=self.channel,
            trigger=self.trigger,
            trigger_type=self.trigger_type,
            markersize=1.2,
            linewidth=1)

        # - - - - - - - - signals 
        self.signals = self.get_signals(mass=125)
        
        
    def get_signals(self, masses=[], mode=None, scale=False):

        """ prepare signals for the analysis.
        Parameters
        ----------
        mass : list (default=[])
           signals masses.
        mode : str(default=None)
        scale : bool,(default=False)
                should we scale signal ?.

        Returns
        -------
        signals : a list of samples.Higgs objects.
        """
        signals = []
        if not isinstance(masses, list):
            masses = [masses]
        for m in masses:
            signals.append(samples.Higgs(
                year=self.year,
                channel=self.channel,
                mass=m,
                mode=mode,
                systematics=self.systematics,
                scale=self.mu,
                ggf_weight=self.ggf_weight))
            
        return signals

    def normalize(self, category):
        """ normalize qcd, ztautau.
        Parameters:
        -----------
        category : Category object, for more see ../catgories/__init__.py

        Returns
        -------
        self : updated object
        """
        norm_cache.qcd_ztautau_norm(
            ztautau=self.ztautau,
            qcd=self.qcd,
            category=category,
            param=self.norm_field,
            target_region=self.target_region)
        return self

    def iter_categories(self, *definitions, **kwargs):
        """ A generator To iterate over categories, print the categories name and cuts on fly.
        Parameters
        ----------
        definitions: list
                  list of categories names.
        Yiels:
        -------
        category : Category object
        """
        
        categories = self.conf.categories
        names = kwargs.pop('names', None)
        for definition in definitions:
            for category in categories[definition]:
                if names is not None and category.name not in names:
                    continue
                log.info("")
                log.info("=" * 40)
                log.info("%s category" % category.name)
                log.info("=" * 40)
                log.info("Cuts: %s" % self.ztautau.cuts(category, self.target_region))
                log.info("Weights: %s" % (', '.join(map(str, self.ztautau.weights('NOMINAL')))))
                self.normalize(category)
                yield category

    def get_suffix(self):
        """ To prepare a string suffix for the final results/plots for each specific analysis.
        Parameters
        -----------
        year: bool(default=True); to label data11 as data12

        Returns
        --------
         output_suffix: str; output suffix
        """
        
        output_suffix += '_%d' % (self.year % 1000)
        if not self.systematics:
            output_suffix += '_stat'
        return  output_suffix

    
    def fit_norms(self, field, template, category, region=None,
                  max_iter=10, thresh=1e-7):
        """
        Derive the normalizations of Ztt and QCD from a fit of some variable
        """
        if region is None:
            region = self.target_region
        # initialize QCD and Ztautau normalizations to 50/50 of data yield
        data_yield = self.data.events(category, region)[1].value
        ztt_yield  = self.ztautau.events(category, region)[1].value
        qcd_yield  = self.qcd.events(category, region)[1].value
        log.info(
            'Normalize z_tt and qcd BKG to data'
            '\n data yield: {0}'
            '\n z_tt yield: {1}'
            '\n qcd yield: {2}'.format(
                data_yield,ztt_yield,qcd_yield)
            )

        qcd_scale = data_yield / (2 * qcd_yield)
        ztt_scale = data_yield / (2 * ztt_yield)
        qcd_scale_error = 0.
        ztt_scale_error = 0.
        qcd_scale_diff = 100.
        ztt_scale_diff = 100.
        it = 0
        while (ztt_scale_diff > thresh or qcd_scale_diff > thresh) and it < max_iter:
            it += 1
            # keep fitting until normalizations converge
            self.qcd.scale = qcd_scale
            self.ztautau.scale = ztt_scale

            channels = self.make_var_channels(
                template, field, [category],
                region, include_signal=False,
                normalize=False)

            # create a workspace
            measurement = histfactory.make_measurement(
                'normalization_{0}'.format(field), channels,POI=None,
                const_params=CONST_PARAMS)
            workspace = histfactory.make_workspace(measurement, silence=False)

            # fit workspace
            minim = workspace.fit()
            fit_result = minim.save()

            # get fitted norms and errors
            qcd = fit_result.floatParsFinal().find(
                'ATLAS_norm_HH_{0:d}_QCD'.format(self.year))
            ztt = fit_result.floatParsFinal().find(
                'ATLAS_norm_HH_{0:d}_Ztt'.format(self.year))
            qcd_scale_new = qcd.getVal()
            qcd_scale_error = qcd.getError()
            ztt_scale_new = ztt.getVal()
            ztt_scale_error = ztt.getError()

            qcd_scale_diff = abs(qcd_scale_new - 1.)
            ztt_scale_diff = abs(ztt_scale_new - 1.)

            qcd_scale_error *= qcd_scale / qcd_scale_new
            qcd_scale *= qcd_scale_new
            ztt_scale_error *= ztt_scale / ztt_scale_new
            ztt_scale *= ztt_scale_new

        self.qcd.scale = qcd_scale
        self.ztautau.scale = ztt_scale
        self.qcd.scale_error = qcd_scale_error
        self.ztautau.scale_error = ztt_scale_error

        return qcd_scale, qcd_scale_error, ztt_scale, ztt_scale_error

    def run(self):
        """
        run the analysis and produce the histograms.
        
        ## loop over analysis categories
        ## loop over analysis variables 
        ## apply scale factors
        ## apply truth matching
        ## 
        
        """
