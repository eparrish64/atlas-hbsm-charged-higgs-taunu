"""
config.py
contains a simple class for analysis channel specific settings, 
like selections , variables, weights, etc.
"""
from . import variables, categories, weights


class Configuration():
    def __init__(self, channel):
        self.channel = channel
        
    @property
    def variables(self):
        return self.VARIABLES[self.channel]

    @property
    def weights(self):
        return WEIGHTS[self.channel]

    @property
    def categories(self):
        return CATEGORIES[self.channel]
