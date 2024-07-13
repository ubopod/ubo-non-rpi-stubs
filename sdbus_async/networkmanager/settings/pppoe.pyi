"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class PppoeSettings(NetworkManagerSettingsMixin):
    """PPP-over-Ethernet Settings"""
    secret_fields_names = ...
    secret_name = ...
    parent: Optional[str] = ...
    password: Optional[str] = ...
    password_flags: Optional[int] = ...
    service: Optional[str] = ...
    username: Optional[str] = ...


