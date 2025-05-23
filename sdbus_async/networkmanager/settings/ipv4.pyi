"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import List, Optional
from .base import NetworkManagerSettingsMixin
from .datatypes import AddressData, RouteData, RoutingRules

@dataclass
class Ipv4Settings(NetworkManagerSettingsMixin):
    """IPv4 Settings"""
    address_data: Optional[List[AddressData]] = ...
    addresses: Optional[List[List[int]]] = ...
    dad_timeout: Optional[int] = ...
    dhcp_client_id: Optional[str] = ...
    dhcp_fqdn: Optional[str] = ...
    dhcp_hostname: Optional[str] = ...
    dhcp_hostname_flags: Optional[int] = ...
    dhcp_iaid: Optional[str] = ...
    dhcp_reject_servers: Optional[List[str]] = ...
    dhcp_send_hostname: Optional[bool] = ...
    dhcp_timeout: Optional[int] = ...
    dhcp_vendor_class_identifier: Optional[str] = ...
    dns: Optional[List[int]] = ...
    dns_data: Optional[List[str]] = ...
    dns_options: Optional[List[str]] = ...
    dns_priority: Optional[int] = ...
    dns_search: Optional[List[str]] = ...
    gateway: Optional[str] = ...
    ignore_auto_dns: Optional[bool] = ...
    ignore_auto_routes: Optional[bool] = ...
    link_local: Optional[int] = ...
    may_fail: Optional[bool] = ...
    method: Optional[str] = ...
    never_default: Optional[bool] = ...
    required_timeout: Optional[int] = ...
    route_data: Optional[List[RouteData]] = ...
    route_metric: Optional[int] = ...
    route_table: Optional[int] = ...
    routes: Optional[List[List[int]]] = ...
    routing_rules: Optional[List[RoutingRules]] = ...


