"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class BluetoothSettings(NetworkManagerSettingsMixin):
    """Bluetooth Settings"""
    bdaddr: Optional[bytes] = ...
    bluetooth_type: Optional[str] = ...


