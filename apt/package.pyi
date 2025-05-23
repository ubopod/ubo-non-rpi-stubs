"""
This type stub file was generated by pyright.
"""

import threading
import apt_pkg
from typing import Any, Iterable, Iterator, List, Mapping, Optional, Sequence, Set, Tuple, Union
from apt.progress.base import AcquireProgress, InstallProgress

"""
This type stub file was generated by pyright.
"""
__all__ = ("BaseDependency", "Dependency", "Origin", "Package", "Record", "Version", "VersionList")
class FetchError(Exception):
    """Raised when a file could not be fetched."""
    ...


class UntrustedError(FetchError):
    """Raised when a file did not have a trusted hash."""
    ...


class BaseDependency:
    """A single dependency."""
    class __dstr(str):
        """Compare helper for compatibility with old third-party code.

        Old third-party code might still compare the relation with the
        previously used relations (<<,<=,==,!=,>=,>>,) instead of the curently
        used ones (<,<=,=,!=,>=,>,). This compare helper lets < match to <<,
        > match to >> and = match to ==.
        """
        def __eq__(self, other: object) -> bool:
            ...
        
        def __ne__(self, other: object) -> bool:
            ...
        
    
    
    def __init__(self, version: Version, dep: apt_pkg.Dependency) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def name(self) -> str:
        """The name of the target package."""
        ...
    
    @property
    def relation(self) -> str:
        """The relation (<, <=, =, !=, >=, >, '') in mathematical notation.

        The empty string will be returned in case of an unversioned dependency.
        """
        ...
    
    @property
    def relation_deb(self) -> str:
        """The relation (<<, <=, =, !=, >=, >>, '') in Debian notation.

        The empty string will be returned in case of an unversioned dependency.
        For more details see the Debian Policy Manual on the syntax of
        relationship fields:
        https://www.debian.org/doc/debian-policy/ch-relationships.html#s-depsyntax  # noqa

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def version(self) -> str:
        """The target version or an empty string.

        Note that the version is only an empty string in case of an unversioned
        dependency. In this case the relation is also an empty string.
        """
        ...
    
    @property
    def target_versions(self) -> List[Version]:
        """A list of all Version objects which satisfy this dependency.

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def installed_target_versions(self) -> List[Version]:
        """A list of all installed Version objects which satisfy this dep.

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def rawstr(self) -> str:
        """String represenation of the dependency.

        Returns the string representation of the dependency as it would be
        written in the debian/control file.  The string representation does not
        include the type of the dependency.

        Example for an unversioned dependency:
          python3

        Example for a versioned dependency:
          python3 >= 3.2

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def rawtype(self) -> str:
        """Type of the dependency.

        This should be one of 'Breaks', 'Conflicts', 'Depends', 'Enhances',
        'PreDepends', 'Recommends', 'Replaces', 'Suggests'.

        Additional types might be added in the future.
        """
        ...
    
    @property
    def pre_depend(self) -> bool:
        """Whether this is a PreDepends."""
        ...
    


class Dependency(List[BaseDependency]):
    """Represent an Or-group of dependencies.

    Attributes defined here:
        or_dependencies - The possible choices
        rawstr - String represenation of the Or-group of dependencies
        rawtype - The type of the dependencies in the Or-group
        target_version - A list of Versions which satisfy this Or-group of deps
    """
    def __init__(self, version: Version, base_deps: List[BaseDependency], rawtype: str) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def or_dependencies(self) -> Dependency:
        ...
    
    @property
    def rawstr(self) -> str:
        """String represenation of the Or-group of dependencies.

        Returns the string representation of the Or-group of dependencies as it
        would be written in the debian/control file.  The string representation
        does not include the type of the Or-group of dependencies.

        Example:
          python2 >= 2.7 | python3

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def rawtype(self) -> str:
        """Type of the Or-group of dependency.

        This should be one of 'Breaks', 'Conflicts', 'Depends', 'Enhances',
        'PreDepends', 'Recommends', 'Replaces', 'Suggests'.

        Additional types might be added in the future.

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def target_versions(self) -> List[Version]:
        """A list of all Version objects which satisfy this Or-group of deps.

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def installed_target_versions(self) -> List[Version]:
        """A list of all installed Version objects which satisfy this dep.

        .. versionadded:: 1.0.0
        """
        ...
    


class Origin:
    """The origin of a version.

    Attributes defined here:
        archive   - The archive (eg. unstable)
        component - The component (eg. main)
        label     - The Label, as set in the Release file
        origin    - The Origin, as set in the Release file
        codename  - The Codename, as set in the Release file
        site      - The hostname of the site.
        trusted   - Boolean value whether this is trustworthy.
    """
    def __init__(self, pkg: Package, packagefile: apt_pkg.PackageFile) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    


class Record(Mapping[Any, Any]):
    """Record in a Packages file

    Represent a record as stored in a Packages file. You can use this like
    a dictionary mapping the field names of the record to their values::

        >>> record = Record("Package: python-apt\\nVersion: 0.8.0\\n\\n")
        >>> record["Package"]
        'python-apt'
        >>> record["Version"]
        '0.8.0'

    For example, to get the tasks of a package from a cache, you could do::

        package.candidate.record["Tasks"].split()

    Of course, you can also use the :attr:`Version.tasks` property.

    """
    def __init__(self, record_str: str) -> None:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __getitem__(self, key: str) -> str:
        ...
    
    def __contains__(self, key: object) -> bool:
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    def iteritems(self) -> Iterable[Tuple[object, str]]:
        """An iterator over the (key, value) items of the record."""
        ...
    
    def get(self, key: str, default: object = ...) -> object:
        """Return record[key] if key in record, else *default*.

        The parameter *default* must be either a string or None.
        """
        ...
    
    def has_key(self, key: str) -> bool:
        """deprecated form of ``key in x``."""
        ...
    
    def __len__(self) -> int:
        ...
    


class Version:
    """Representation of a package version.

    The Version class contains all information related to a
    specific package version.

    .. versionadded:: 0.7.9
    """
    def __init__(self, package: Package, cand: apt_pkg.Version) -> None:
        ...
    
    def __eq__(self, other: object) -> bool:
        ...
    
    def __ge__(self, other: Version) -> bool:
        ...
    
    def __gt__(self, other: Version) -> bool:
        ...
    
    def __le__(self, other: Version) -> bool:
        ...
    
    def __lt__(self, other: Version) -> bool:
        ...
    
    def __ne__(self, other: object) -> Union[bool, Any]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def installed_size(self) -> int:
        """Return the size of the package when installed."""
        ...
    
    @property
    def homepage(self) -> str:
        """Return the homepage for the package."""
        ...
    
    @property
    def size(self) -> int:
        """Return the size of the package."""
        ...
    
    @property
    def architecture(self) -> str:
        """Return the architecture of the package version."""
        ...
    
    @property
    def downloadable(self) -> bool:
        """Return whether the version of the package is downloadable."""
        ...
    
    @property
    def is_installed(self) -> bool:
        """Return wether this version of the package is currently installed.

        .. versionadded:: 1.0.0
        """
        ...
    
    @property
    def version(self) -> str:
        """Return the version as a string."""
        ...
    
    @property
    def summary(self) -> Optional[str]:
        """Return the short description (one line summary)."""
        ...
    
    @property
    def raw_description(self) -> str:
        """return the long description (raw)."""
        ...
    
    @property
    def section(self) -> str:
        """Return the section of the package."""
        ...
    
    @property
    def description(self) -> str:
        """Return the formatted long description.

        Return the formatted long description according to the Debian policy
        (Chapter 5.6.13).
        See http://www.debian.org/doc/debian-policy/ch-controlfields.html
        for more information.
        """
        ...
    
    @property
    def source_name(self) -> str:
        """Return the name of the source package."""
        ...
    
    @property
    def source_version(self) -> str:
        """Return the version of the source package."""
        ...
    
    @property
    def priority(self) -> str:
        """Return the priority of the package, as string."""
        ...
    
    @property
    def policy_priority(self) -> int:
        """Return the internal policy priority as a number.
        See apt_preferences(5) for more information about what it means.
        """
        ...
    
    @property
    def record(self) -> Record:
        """Return a Record() object for this version.

        Return a Record() object for this version which provides access
        to the raw attributes of the candidate version
        """
        ...
    
    def get_dependencies(self, *types: str) -> List[Dependency]:
        """Return a list of Dependency objects for the given types.

        Multiple types can be specified. Possible types are:
        'Breaks', 'Conflicts', 'Depends', 'Enhances', 'PreDepends',
        'Recommends', 'Replaces', 'Suggests'

        Additional types might be added in the future.
        """
        ...
    
    @property
    def provides(self) -> List[str]:
        """Return a list of names that this version provides."""
        ...
    
    @property
    def enhances(self) -> List[Dependency]:
        """Return the list of enhances for the package version."""
        ...
    
    @property
    def dependencies(self) -> List[Dependency]:
        """Return the dependencies of the package version."""
        ...
    
    @property
    def recommends(self) -> List[Dependency]:
        """Return the recommends of the package version."""
        ...
    
    @property
    def suggests(self) -> List[Dependency]:
        """Return the suggests of the package version."""
        ...
    
    @property
    def origins(self) -> List[Origin]:
        """Return a list of origins for the package version."""
        ...
    
    @property
    def filename(self) -> str:
        """Return the path to the file inside the archive.

        .. versionadded:: 0.7.10
        """
        ...
    
    @property
    def md5(self) -> str:
        """Return the md5sum of the binary.

        .. versionadded:: 0.7.10
        """
        ...
    
    @property
    def sha1(self) -> str:
        """Return the sha1sum of the binary.

        .. versionadded:: 0.7.10
        """
        ...
    
    @property
    def sha256(self) -> str:
        """Return the sha256sum of the binary.

        .. versionadded:: 0.7.10
        """
        ...
    
    @property
    def tasks(self) -> Set[str]:
        """Get the tasks of the package.

        A set of the names of the tasks this package belongs to.

        .. versionadded:: 0.8.0
        """
        ...
    
    @property
    def uris(self) -> List[str]:
        """Return a list of all available uris for the binary.

        .. versionadded:: 0.7.10
        """
        ...
    
    @property
    def uri(self) -> Optional[str]:
        """Return a single URI for the binary.

        .. versionadded:: 0.7.10
        """
        ...
    
    def fetch_binary(self, destdir: str = ..., progress: Optional[AcquireProgress] = ..., allow_unauthenticated: Optional[bool] = ...) -> str:
        """Fetch the binary version of the package.

        The parameter *destdir* specifies the directory where the package will
        be fetched to.

        The parameter *progress* may refer to an apt_pkg.AcquireProgress()
        object. If not specified or None, apt.progress.text.AcquireProgress()
        is used.

        The keyword-only parameter *allow_unauthenticated* specifies whether
        to allow unauthenticated downloads. If not specified, it defaults to
        the configuration option `APT::Get::AllowUnauthenticated`.

        .. versionadded:: 0.7.10
        """
        ...
    
    def fetch_source(self, destdir: str = ..., progress: Optional[AcquireProgress] = ..., unpack: bool = ..., allow_unauthenticated: Optional[bool] = ...) -> str:
        """Get the source code of a package.

        The parameter *destdir* specifies the directory where the source will
        be fetched to.

        The parameter *progress* may refer to an apt_pkg.AcquireProgress()
        object. If not specified or None, apt.progress.text.AcquireProgress()
        is used.

        The parameter *unpack* describes whether the source should be unpacked
        (``True``) or not (``False``). By default, it is unpacked.

        If *unpack* is ``True``, the path to the extracted directory is
        returned. Otherwise, the path to the .dsc file is returned.

        The keyword-only parameter *allow_unauthenticated* specifies whether
        to allow unauthenticated downloads. If not specified, it defaults to
        the configuration option `APT::Get::AllowUnauthenticated`.
        """
        ...
    


class VersionList(Sequence[Version]):
    """Provide a mapping & sequence interface to all versions of a package.

    This class can be used like a dictionary, where version strings are the
    keys. It can also be used as a sequence, where integers are the keys.

    You can also convert this to a dictionary or a list, using the usual way
    of dict(version_list) or list(version_list). This is useful if you need
    to access the version objects multiple times, because they do not have to
    be recreated this way.

    Examples ('package.versions' being a version list):
        '0.7.92' in package.versions # Check whether 0.7.92 is a valid version.
        package.versions[0] # Return first version or raise IndexError
        package.versions[0:2] # Return a new VersionList for objects 0-2
        package.versions['0.7.92'] # Return version 0.7.92 or raise KeyError
        package.versions.keys() # All keys, as strings.
        max(package.versions)
    """
    def __init__(self, package: Package, slice_: Optional[slice] = ...) -> None:
        ...
    
    def __getitem__(self, item: Union[int, slice, str]) -> Any:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __iter__(self) -> Iterator[Version]:
        """Return an iterator over all value objects."""
        ...
    
    def __contains__(self, item: object) -> bool:
        ...
    
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __len__(self) -> int:
        ...
    
    def keys(self) -> List[str]:
        """Return a list of all versions, as strings."""
        ...
    
    def get(self, key: str, default: Optional[Version] = ...) -> Optional[Version]:
        """Return the key or the default."""
        ...
    


class Package:
    """Representation of a package in a cache.

    This class provides methods and properties for working with a package. It
    lets you mark the package for installation, check if it is installed, and
    much more.
    """
    def __init__(self, pcache: apt.Cache, pkgiter: apt_pkg.Package) -> None:
        """Init the Package object"""
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __lt__(self, other: Package) -> bool:
        ...
    
    @property
    def candidate(self) -> Optional[Version]:
        """Return the candidate version of the package.

        This property is writeable to allow you to set the candidate version
        of the package. Just assign a Version() object, and it will be set as
        the candidate version.
        """
        ...
    
    @candidate.setter
    def candidate(self, version: Version) -> None:
        """Set the candidate version of the package."""
        ...
    
    @property
    def installed(self) -> Optional[Version]:
        """Return the currently installed version of the package.

        .. versionadded:: 0.7.9
        """
        ...
    
    @property
    def name(self) -> str:
        """Return the name of the package, possibly including architecture.

        If the package is not part of the system's preferred architecture,
        return the same as :attr:`fullname`, otherwise return the same
        as :attr:`shortname`

        .. versionchanged:: 0.7.100.3

        As part of multi-arch, this field now may include architecture
        information.
        """
        ...
    
    @property
    def fullname(self) -> str:
        """Return the name of the package, including architecture.

        Note that as for :meth:`architecture`, this returns the
        native architecture for Architecture: all packages.

        .. versionadded:: 0.7.100.3"""
        ...
    
    @property
    def shortname(self) -> str:
        """Return the name of the package, without architecture.

        .. versionadded:: 0.7.100.3"""
        ...
    
    @property
    def id(self) -> int:
        """Return a uniq ID for the package.

        This can be used eg. to store additional information about the pkg."""
        ...
    
    @property
    def essential(self) -> bool:
        """Return True if the package is an essential part of the system."""
        ...
    
    def architecture(self) -> str:
        """Return the Architecture of the package.

        Note that for Architecture: all packages, this returns the
        native architecture, as they are internally treated like native
        packages. To get the concrete architecture, look at the
        :attr:`Version.architecture` attribute.

        .. versionchanged:: 0.7.100.3
            This is now the package's architecture in the multi-arch sense,
            previously it was the architecture of the candidate version
            and deprecated.
        """
        ...
    
    @property
    def marked_install(self) -> bool:
        """Return ``True`` if the package is marked for install."""
        ...
    
    @property
    def marked_upgrade(self) -> bool:
        """Return ``True`` if the package is marked for upgrade."""
        ...
    
    @property
    def marked_delete(self) -> bool:
        """Return ``True`` if the package is marked for delete."""
        ...
    
    @property
    def marked_keep(self) -> bool:
        """Return ``True`` if the package is marked for keep."""
        ...
    
    @property
    def marked_downgrade(self) -> bool:
        """Package is marked for downgrade"""
        ...
    
    @property
    def marked_reinstall(self) -> bool:
        """Return ``True`` if the package is marked for reinstall."""
        ...
    
    @property
    def is_installed(self) -> bool:
        """Return ``True`` if the package is installed."""
        ...
    
    @property
    def is_upgradable(self) -> bool:
        """Return ``True`` if the package is upgradable."""
        ...
    
    @property
    def is_auto_removable(self) -> bool:
        """Return ``True`` if the package is no longer required.

        If the package has been installed automatically as a dependency of
        another package, and if no packages depend on it anymore, the package
        is no longer required.
        """
        ...
    
    @property
    def is_auto_installed(self) -> bool:
        """Return whether the package is marked as automatically installed."""
        ...
    
    @property
    def installed_files(self) -> List[str]:
        """Return a list of files installed by the package.

        Return a list of unicode names of the files which have
        been installed by this package
        """
        ...
    
    def get_changelog(self, uri: Optional[str] = ..., cancel_lock: Optional[threading.Event] = ...) -> str:
        """
        Download the changelog of the package and return it as unicode
        string.

        The parameter *uri* refers to the uri of the changelog file. It may
        contain multiple named variables which will be substitued. These
        variables are (src_section, prefix, src_pkg, src_ver). An example is
        the Ubuntu changelog::

            "http://changelogs.ubuntu.com/changelogs/pool" \\
                "/%(src_section)s/%(prefix)s/%(src_pkg)s" \\
                "/%(src_pkg)s_%(src_ver)s/changelog"

        The parameter *cancel_lock* refers to an instance of threading.Event,
        which if set, prevents the download.
        """
        ...
    
    @property
    def versions(self) -> VersionList:
        """Return a VersionList() object for all available versions.

        .. versionadded:: 0.7.9
        """
        ...
    
    @property
    def is_inst_broken(self) -> bool:
        """Return True if the to-be-installed package is broken."""
        ...
    
    @property
    def is_now_broken(self) -> bool:
        """Return True if the installed package is broken."""
        ...
    
    @property
    def has_config_files(self) -> bool:
        """Checks whether the package is is the config-files state."""
        ...
    
    def mark_keep(self) -> None:
        """Mark a package for keep."""
        ...
    
    def mark_delete(self, auto_fix: bool = ..., purge: bool = ...) -> None:
        """Mark a package for deletion.

        If *auto_fix* is ``True``, the resolver will be run, trying to fix
        broken packages.  This is the default.

        If *purge* is ``True``, remove the configuration files of the package
        as well.  The default is to keep the configuration.
        """
        ...
    
    def mark_install(self, auto_fix: bool = ..., auto_inst: bool = ..., from_user: bool = ...) -> None:
        """Mark a package for install.

        If *autoFix* is ``True``, the resolver will be run, trying to fix
        broken packages.  This is the default.

        If *autoInst* is ``True``, the dependencies of the packages will be
        installed automatically.  This is the default.

        If *fromUser* is ``True``, this package will not be marked as
        automatically installed. This is the default. Set it to False if you
        want to be able to automatically remove the package at a later stage
        when no other package depends on it.
        """
        ...
    
    def mark_upgrade(self, from_user: bool = ...) -> None:
        """Mark a package for upgrade."""
        ...
    
    def mark_auto(self, auto: bool = ...) -> None:
        """Mark a package as automatically installed.

        Call this function to mark a package as automatically installed. If the
        optional parameter *auto* is set to ``False``, the package will not be
        marked as automatically installed anymore. The default is ``True``.
        """
        ...
    
    def commit(self, fprogress: AcquireProgress, iprogress: InstallProgress) -> None:
        """Commit the changes.

        The parameter *fprogress* refers to a apt_pkg.AcquireProgress() object,
        like apt.progress.text.AcquireProgress().

        The parameter *iprogress* refers to an InstallProgress() object, as
        found in apt.progress.base.
        """
        ...
    


if __name__ == "__main__":
    ...
