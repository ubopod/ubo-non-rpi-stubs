"""
This type stub file was generated by pyright.
"""

from sdbus import DbusFailedError

class NetworkManagerBaseError(Exception):
    """Base of all NetworkManager errors."""
    ...


class NmAgentManagerFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NmAgentManagerPermissionDeniedError(DbusFailedError, NetworkManagerBaseError):
    """The caller does not have permission to register a secret agent,
    or is trying to register the same secret agent twice."""
    dbus_error_name = ...


class NmAgentManagerInvalidIdentifierError(DbusFailedError):
    """The identifier is not a valid secret agent identifier."""
    dbus_error_name = ...


class NmAgentManagerNotRegisteredError(DbusFailedError, NetworkManagerBaseError):
    """The caller tried to unregister an agent that was not registered."""
    dbus_error_name = ...


class NmAgentManagerNoSecretsError(DbusFailedError, NetworkManagerBaseError):
    """No secret agent returned secrets for this request."""
    dbus_error_name = ...


class NmAgentManagerUserCanceledError(DbusFailedError, NetworkManagerBaseError):
    """The user canceled the secrets request."""
    dbus_error_name = ...


class NmConnectionFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NmConnectionSettingNotFoundError(DbusFailedError, NetworkManagerBaseError):
    """Connection object did not contain the specified Setting object."""
    dbus_error_name = ...


class NmConnectionPropertyNotFoundError(DbusFailedError, NetworkManagerBaseError):
    """Connection object did not contain the requested Setting property"""
    dbus_error_name = ...


class NmConnectionPropertyNotSecretError(DbusFailedError, NetworkManagerBaseError):
    """An operation which requires a secret was attempted on a
    non-secret property."""
    dbus_error_name = ...


class NmConnectionMissingSettingError(DbusFailedError, NetworkManagerBaseError):
    """Connection object is missing an Setting which is required
    for its configuration."""
    dbus_error_name = ...


class NmConnectionInvalidSettingError(DbusFailedError, NetworkManagerBaseError):
    """Connection object contains an invalid or inappropriate Setting."""
    dbus_error_name = ...


class NmConnectionMissingPropertyError(DbusFailedError, NetworkManagerBaseError):
    """Connection object is invalid because it is missing a
    required property."""
    dbus_error_name = ...


class NmConnectionInvalidPropertyError(DbusFailedError, NetworkManagerBaseError):
    """Connection object is invalid because a property has an invalid value."""
    dbus_error_name = ...


class NmDeviceFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NmDeviceCreationFailedError(DbusFailedError, NetworkManagerBaseError):
    """NetworkManager failed to create the device."""
    dbus_error_name = ...


class NmDeviceInvalidConnectionError(DbusFailedError, NetworkManagerBaseError):
    """The specified connection is not valid."""
    dbus_error_name = ...


class NmDeviceIncompatibleConnectionError(DbusFailedError, NetworkManagerBaseError):
    """Specified connection is not compatible with this device."""
    dbus_error_name = ...


class NmDeviceNotActiveError(DbusFailedError, NetworkManagerBaseError):
    """Device does not have an active connection."""
    dbus_error_name = ...


class NmDeviceNotSoftwareError(DbusFailedError, NetworkManagerBaseError):
    """Requested operation is only valid on software devices."""
    dbus_error_name = ...


class NmDeviceNotAllowedError(DbusFailedError, NetworkManagerBaseError):
    """Requested operation is not allowed at this time."""
    dbus_error_name = ...


class NmDeviceSpecificObjectNotFoundError(DbusFailedError, NetworkManagerBaseError):
    """Specific object in the activation request
    (eg, the AccessPoint or WimaxNsp) was not found."""
    dbus_error_name = ...


class NmDeviceVersionIdMismatchError(DbusFailedError, NetworkManagerBaseError):
    """Version id did not match."""
    dbus_error_name = ...


class NmDeviceMissingDependenciesError(DbusFailedError, NetworkManagerBaseError):
    """Requested operation could not be completed
    due to missing dependencies."""
    dbus_error_name = ...


class NmDeviceInvalidArgumentError(DbusFailedError, NetworkManagerBaseError):
    """Invalid argument.

    Since: 1.16."""
    dbus_error_name = ...


class NetworkManagerFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NetworkManagerPermissionDeniedError(DbusFailedError, NetworkManagerBaseError):
    """Permission denied."""
    dbus_error_name = ...


class NetworkManagerUnknownConnectionError(DbusFailedError, NetworkManagerBaseError):
    """The requested connection is not known."""
    dbus_error_name = ...


class NetworkManagerUnknownDeviceError(DbusFailedError, NetworkManagerBaseError):
    """The requested device is not known."""
    dbus_error_name = ...


class NetworkManagerConnectionNotAvailableError(DbusFailedError, NetworkManagerBaseError):
    """The requested connection cannot be activated at this time."""
    dbus_error_name = ...


class NetworkManagerConnectionNotActiveError(DbusFailedError, NetworkManagerBaseError):
    """The request could not be completed because a required connection
    is not active."""
    dbus_error_name = ...


class NetworkManagerConnectionAlreadyActiveError(DbusFailedError, NetworkManagerBaseError):
    """The connection to be activated was already active on another device."""
    dbus_error_name = ...


class NetworkManagerDependencyFailedError(DbusFailedError, NetworkManagerBaseError):
    """An activation request failed due to a dependency being unavailable."""
    dbus_error_name = ...


class NetworkManagerAlreadyAsleepOrAwakeError(DbusFailedError, NetworkManagerBaseError):
    """The manager is already in the requested sleep/wake state."""
    dbus_error_name = ...


class NetworkManagerAlreadyEnabledOrDisabledError(DbusFailedError, NetworkManagerBaseError):
    """The network is already enabled/disabled."""
    dbus_error_name = ...


class NetworkManagerUnknownLogLevelError(DbusFailedError, NetworkManagerBaseError):
    """Unknown log level in
    :py:func:`NetworkManagerInterfaceAsync.set_logging`."""
    dbus_error_name = ...


class NetworkManagerUnknownLogDomainError(DbusFailedError, NetworkManagerBaseError):
    """Unknown log domain in
    :py:func:`NetworkManagerInterfaceAsync.set_logging`."""
    dbus_error_name = ...


class NetworkManagerInvalidArgumentsError(DbusFailedError, NetworkManagerBaseError):
    """Invalid arguments for D-Bus request."""
    dbus_error_name = ...


class NetworkManagerMissingPluginError(DbusFailedError, NetworkManagerBaseError):
    """A plug-in was needed to complete the
    activation but is not available."""
    dbus_error_name = ...


class NmSecretManagerFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NmSecretManagerPermissionDeniedError(DbusFailedError, NetworkManagerBaseError):
    """The caller (ie, NetworkManager) is
    not authorized to make this request."""
    dbus_error_name = ...


class NmSecretManagerInvalidConnectionError(DbusFailedError, NetworkManagerBaseError):
    """Connection for which secrets were requested is invalid."""
    dbus_error_name = ...


class NmSecretManagerUserCanceledError(DbusFailedError, NetworkManagerBaseError):
    """Request was canceled by the user."""
    dbus_error_name = ...


class NmSecretManagerAgentCanceledError(DbusFailedError, NetworkManagerBaseError):
    """Agent canceled the request because it was requested
    to do so by NetworkManager."""
    dbus_error_name = ...


class NmSecretManagerNoSecretsError(DbusFailedError, NetworkManagerBaseError):
    """The agent cannot find any secrets for this connection."""
    dbus_error_name = ...


class NmSettingsFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NmSettingsPermissionDeniedError(DbusFailedError, NetworkManagerBaseError):
    """Permission denied."""
    dbus_error_name = ...


class NmSettingsNotSupportedError(DbusFailedError, NetworkManagerBaseError):
    """Requested operation is not supported by any
    active settings backend."""
    dbus_error_name = ...


class NmSettingsInvalidConnectionError(DbusFailedError, NetworkManagerBaseError):
    """Connection was invalid."""
    dbus_error_name = ...


class NmSettingsReadOnlyConnectionError(DbusFailedError, NetworkManagerBaseError):
    """Attempted to modify a read-only connection."""
    dbus_error_name = ...


class NmSettingsUuidExistsError(DbusFailedError, NetworkManagerBaseError):
    """Connection with that UUID already exists."""
    dbus_error_name = ...


class NmSettingsInvalidHostnameError(DbusFailedError, NetworkManagerBaseError):
    """Attempted to set an invalid hostname."""
    dbus_error_name = ...


class NmSettingsInvalidArgumentsError(DbusFailedError, NetworkManagerBaseError):
    """Invalid arguments."""
    dbus_error_name = ...


class NmVpnPluginFailedError(DbusFailedError, NetworkManagerBaseError):
    """Unknown or unspecified error."""
    dbus_error_name = ...


class NmVpnPluginStartingInProgressError(DbusFailedError, NetworkManagerBaseError):
    """Plugin is already starting and another connect
    request was received."""
    dbus_error_name = ...


class NmVpnPluginAlreadyStartedError(DbusFailedError, NetworkManagerBaseError):
    """Plugin is already connected and another connect
    request was received."""
    dbus_error_name = ...


class NmVpnPluginStoppingInProgressError(DbusFailedError, NetworkManagerBaseError):
    """Plugin is already stopping and another stop
    request was received."""
    dbus_error_name = ...


class NmVpnPluginAlreadyStoppedError(DbusFailedError, NetworkManagerBaseError):
    """Plugin is already stopped and another disconnect
    request was received."""
    dbus_error_name = ...


class NmVpnPluginWrongStateError(DbusFailedError, NetworkManagerBaseError):
    """Operation could not be performed in this state."""
    dbus_error_name = ...


class NmVpnPluginBadArgumentsError(DbusFailedError, NetworkManagerBaseError):
    """Operation could not be performed as the request contained
    malformed arguments, or arguments of unexpected type.

    Usually means that one of the VPN setting data items or secrets
    was not of the expected type (ie int, string, bool, etc).
    """
    dbus_error_name = ...


class NmVpnPluginLaunchFailedError(DbusFailedError, NetworkManagerBaseError):
    """Child process failed to launch."""
    dbus_error_name = ...


class NmVpnPluginInvalidConnectionError(DbusFailedError, NetworkManagerBaseError):
    """Operation could not be performed because the connection was invalid.

    Usually means that the connection's VPN setting was missing
    some required data item or secret.
    """
    dbus_error_name = ...


class NmVpnPluginInteractiveNotSupportedError(DbusFailedError, NetworkManagerBaseError):
    """Operation could not be performed as the plugin
    does not support interactive operations.

    Interactive operations such as
    :py:func:`NetworkManagerVPNPluginInterfaceAsync.connect_interactive`
    or :py:func:`NetworkManagerVPNPluginInterfaceAsync.new_secrets`.
    """
    dbus_error_name = ...


