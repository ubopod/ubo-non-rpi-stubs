"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class OvsPatchSettings(NetworkManagerSettingsMixin):
    """OvsPatch Link Settings"""
    peer: Optional[str] = ...


