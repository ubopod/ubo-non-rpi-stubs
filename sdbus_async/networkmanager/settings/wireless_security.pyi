"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import List, Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class WirelessSecuritySettings(NetworkManagerSettingsMixin):
    """Wi-Fi Security Settings"""
    secret_fields_names = ...
    secret_name = ...
    auth_alg: Optional[str] = ...
    fils: Optional[int] = ...
    group: Optional[List[str]] = ...
    key_mgmt: Optional[str] = ...
    leap_password: Optional[str] = ...
    leap_password_flags: Optional[int] = ...
    leap_username: Optional[str] = ...
    pairwise: Optional[List[str]] = ...
    pmf: Optional[int] = ...
    proto: Optional[List[str]] = ...
    psk: Optional[str] = ...
    psk_flags: Optional[int] = ...
    wep_key_flags: Optional[int] = ...
    wep_key_type: Optional[int] = ...
    wep_key0: Optional[str] = ...
    wep_key1: Optional[str] = ...
    wep_key2: Optional[str] = ...
    wep_key3: Optional[str] = ...
    wep_tx_keyidx: Optional[int] = ...
    wps_method: Optional[int] = ...


