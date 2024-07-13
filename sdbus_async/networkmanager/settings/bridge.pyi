"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import List, Optional
from .base import NetworkManagerSettingsMixin
from .datatypes import Vlans

@dataclass
class BridgeSettings(NetworkManagerSettingsMixin):
    """Bridging Settings"""
    ageing_time: Optional[int] = ...
    forward_delay: Optional[int] = ...
    group_address: Optional[bytes] = ...
    group_forward_mask: Optional[int] = ...
    hello_time: Optional[int] = ...
    interface_name: Optional[str] = ...
    mac_address: Optional[bytes] = ...
    max_age: Optional[int] = ...
    multicast_hash_max: Optional[int] = ...
    multicast_last_member_count: Optional[int] = ...
    multicast_last_member_interval: Optional[int] = ...
    multicast_membership_interval: Optional[int] = ...
    multicast_querier: Optional[bool] = ...
    multicast_querier_interval: Optional[int] = ...
    multicast_query_interval: Optional[int] = ...
    multicast_query_response_interval: Optional[int] = ...
    multicast_query_use_ifaddr: Optional[bool] = ...
    multicast_router: Optional[str] = ...
    multicast_snooping: Optional[bool] = ...
    multicast_startup_query_count: Optional[int] = ...
    multicast_startup_query_interval: Optional[int] = ...
    priority: Optional[int] = ...
    stp: Optional[bool] = ...
    vlan_default_pvid: Optional[int] = ...
    vlan_filtering: Optional[bool] = ...
    vlan_protocol: Optional[str] = ...
    vlan_stats_enabled: Optional[bool] = ...
    vlans: Optional[List[Vlans]] = ...


