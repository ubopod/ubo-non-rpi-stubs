"""
This type stub file was generated by pyright.
"""

from os import environ
from kivy.event import EventDispatcher

"""
This type stub file was generated by pyright.
"""
__all__ = ('Metrics', 'MetricsBase', 'pt', 'inch', 'cm', 'mm', 'dp', 'sp', 'dpi2px', 'NUMERIC_FORMATS')
_default_dpi = ...
_default_density = ...
_default_fontscale = ...
if environ.get('KIVY_DOC_INCLUDE', None) == '1':
    _default_dpi = ...
    _default_density = ...
else:
    _custom_dpi = ...
    _custom_density = ...
    _custom_fontscale = ...
def pt(value) -> float:
    '''Convert from points to pixels
    '''
    ...

def inch(value) -> float:
    '''Convert from inches to pixels
    '''
    ...

def cm(value) -> float:
    '''Convert from centimeters to pixels
    '''
    ...

def mm(value) -> float:
    '''Convert from millimeters to pixels
    '''
    ...

def dp(value) -> float:
    '''Convert from density-independent pixels to pixels
    '''
    ...

def sp(value) -> float:
    '''Convert from scale-independent pixels to pixels
    '''
    ...

class MetricsBase(EventDispatcher):
    '''Class that contains the default attributes for Metrics. Don't use this
    class directly, but use the `Metrics` instance.
    '''
    _dpi = ...
    _density = ...
    _fontscale = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def get_dpi(self, force_recompute=...):
        ...
    
    def set_dpi(self, value):
        ...
    
    dpi: float = ...
    def get_dpi_rounded(self):
        ...
    
    dpi_rounded: int = ...
    def get_density(self, force_recompute=...):
        ...
    
    def set_density(self, value):
        ...
    
    density: float = ...
    def get_fontscale(self, force_recompute=...):
        ...
    
    def set_fontscale(self, value):
        ...
    
    fontscale: float = ...
    def get_in(self):
        ...
    
    inch: float = ...
    def get_dp(self):
        ...
    
    dp: float = ...
    def get_sp(self):
        ...
    
    sp: float = ...
    def get_pt(self):
        ...
    
    pt: float = ...
    def get_cm(self):
        ...
    
    cm: float = ...
    def get_mm(self):
        ...
    
    mm: float = ...
    def reset_metrics(self):
        """Resets the dpi/density/fontscale to the platform values, overwriting
        any manually set values.
        """
        ...
    
    def reset_dpi(self, *args):
        """Resets the dpi (and possibly density) to the platform values,
        overwriting any manually set values.
        """
        ...
    


Metrics: MetricsBase = ...
