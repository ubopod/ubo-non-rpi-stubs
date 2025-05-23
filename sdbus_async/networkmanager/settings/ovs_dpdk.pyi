"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class OvsDpdkSettings(NetworkManagerSettingsMixin):
    """OvsDpdk Link Settings"""
    devargs: Optional[str] = ...
    n_rxq: Optional[int] = ...


