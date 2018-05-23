# local imports
from .sample import Sample, Background
from . import log


class Fakes(Sample, Background):
    
    @staticmethod
    def sample_compatibility(data, mc):
        if not isinstance(mc, (list, tuple)):
            raise TypeError("mc must be a list or tuple of MC samples")
        if not mc:
            raise ValueError("mc must contain at least one MC sample")

    def __init__(self, data, mc,
                 scale=1.,
                 scale_error=0.,
                 data_scale=1.,
                 mc_scales=None,
                 constrain_norm=False,
                 shape_systematic=True,
                 cuts=None,
                 name='Fakes',
                 label='Fakes',
                 **kwargs):
        
        # - - - - - - - - quick sanity check
        Fakes.sample_compatibility(data, mc)

        # - - - - - - - - instantiate base 
        super(Fakes, self).__init__(
            year=data.year,
            scale=scale,
            name=name,
            label=label,
            **kwargs)
        
        self.data = data
        self.mc = mc
        self.scale = 1.
        self.data_scale = data_scale
        if mc_scales is not None:
            if len(mc_scales) != len(mc):
                raise ValueError("length of MC scales must match number of MC")
            self.mc_scales = mc_scales
        else:
            # default scales to 1.
            self.mc_scales = [1. for m in self.mc]
    
    def cuts(self):
        pass

    def hist(self):
        pass
    
