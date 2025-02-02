"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import List, Optional
from .base import NetworkManagerSettingsMixin

@dataclass
class DcbSettings(NetworkManagerSettingsMixin):
    """Data Center Bridging Settings"""
    app_fcoe_flags: Optional[int] = ...
    app_fcoe_mode: Optional[str] = ...
    app_fcoe_priority: Optional[int] = ...
    app_fip_flags: Optional[int] = ...
    app_fip_priority: Optional[int] = ...
    app_iscsi_flags: Optional[int] = ...
    app_iscsi_priority: Optional[int] = ...
    priority_bandwidth: Optional[List[int]] = ...
    priority_flow_control: Optional[List[int]] = ...
    priority_flow_control_flags: Optional[int] = ...
    priority_group_bandwidth: Optional[List[int]] = ...
    priority_group_flags: Optional[int] = ...
    priority_group_id: Optional[List[int]] = ...
    priority_strict_bandwidth: Optional[List[int]] = ...
    priority_traffic_class: Optional[List[int]] = ...


