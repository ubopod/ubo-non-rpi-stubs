"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class WimaxSettings(NetworkManagerSettingsMixin):
    """WiMax Settings"""
    mac_address: Optional[bytes] = ...
    network_name: Optional[str] = ...


