"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from functools import lru_cache
from typing import Any, ClassVar, Dict, List, Type
from ..types import NetworkManagerSettingsDomain

@dataclass
class NetworkManagerSettingsMixin:
    secret_fields_names: ClassVar[List[str]] = ...
    secret_name: ClassVar[str] = ...
    def to_dbus(self) -> NetworkManagerSettingsDomain:
        """Return a dbus dictionary for NetworkManager to add/update profiles

        The key names provided are exactly as documented in these tables:
        https://networkmanager.dev/docs/api/latest/nm-settings-dbus.html
        """
        ...
    
    def to_settings_dict(self, defaults: bool = ...) -> Dict[str, Any]:
        """Return a simple dictionary using the same key names like the dbus
        dict from to_dbus(), but without the dbus signatures returned by it.

        The key names provided are exactly as documented in these tables:
        https://networkmanager.dev/docs/api/latest/nm-settings-dbus.html

        Contrary to dataclasses.asdict(), it provides the original dbus keys,
        e.g. with numerical prefixes like "802-11-", dashes, and "id"/"type".

        In addition, it can be selected if defaults shall be omitted in output,
        like NetworkConnectionSettings.get_settings() omits default values:

        Because of this, all NetworkManager clients which read profiles have
        to have hard-coded knowledge of these defaults. By this omission, they
        are part of the stable API: They can be relied upon to never change.
        Omitting the defaults makes the typical output really small for review.
        """
        ...
    
    @classmethod
    def from_dbus(cls, dbus_dict: NetworkManagerSettingsDomain) -> NetworkManagerSettingsMixin:
        """TODO: Add proper docstring"""
        ...
    
    @classmethod
    def from_dict(cls, plain_dict: Dict[str, Any]) -> NetworkManagerSettingsMixin:
        ...
    
    @classmethod
    @lru_cache(maxsize=None)
    def setting_name_reverse_mapping(cls) -> Dict[str, str]:
        ...
    
    @classmethod
    @lru_cache(maxsize=None)
    def setting_name_to_inner_class(cls, setting_name: str) -> Type[Any]:
        ...
    


