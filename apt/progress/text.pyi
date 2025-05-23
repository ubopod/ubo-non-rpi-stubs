"""
This type stub file was generated by pyright.
"""

import io
import apt_pkg
from typing import Optional
from apt.progress import base

"""Progress reporting for text interfaces."""
__all__ = ["AcquireProgress", "CdromProgress", "OpProgress"]
def _(msg: str) -> str:
    """Translate the message, also try apt if translation is missing."""
    ...

class TextProgress:
    """Internal Base class for text progress classes."""
    def __init__(self, outfile: Optional[io.TextIOBase] = ...) -> None:
        ...
    


class OpProgress(base.OpProgress, TextProgress):
    """Operation progress reporting.

    This closely resembles OpTextProgress in libapt-pkg.
    """
    def __init__(self, outfile: Optional[io.TextIOBase] = ...) -> None:
        ...
    
    def update(self, percent: Optional[float] = ...) -> None:
        """Called periodically to update the user interface."""
        ...
    
    def done(self) -> None:
        """Called once an operation has been completed."""
        ...
    


class AcquireProgress(base.AcquireProgress, TextProgress):
    """AcquireProgress for the text interface."""
    def __init__(self, outfile: Optional[io.TextIOBase] = ...) -> None:
        ...
    
    def start(self) -> None:
        """Start an Acquire progress.

        In this case, the function sets up a signal handler for SIGWINCH, i.e.
        window resize signals. And it also sets id to 1.
        """
        ...
    
    def ims_hit(self, item: apt_pkg.AcquireItemDesc) -> None:
        """Called when an item is update (e.g. not modified on the server)."""
        ...
    
    def fail(self, item: apt_pkg.AcquireItemDesc) -> None:
        """Called when an item is failed."""
        ...
    
    def fetch(self, item: apt_pkg.AcquireItemDesc) -> None:
        """Called when some of the item's data is fetched."""
        ...
    
    def pulse(self, owner: apt_pkg.Acquire) -> bool:
        """Periodically invoked while the Acquire process is underway.

        Return False if the user asked to cancel the whole Acquire process."""
        ...
    
    def media_change(self, medium: str, drive: str) -> bool:
        """Prompt the user to change the inserted removable media."""
        ...
    
    def stop(self) -> None:
        """Invoked when the Acquire process stops running."""
        ...
    


class CdromProgress(base.CdromProgress, TextProgress):
    """Text CD-ROM progress."""
    def ask_cdrom_name(self) -> Optional[str]:
        """Ask the user to provide a name for the disc."""
        ...
    
    def update(self, text: str, current: int) -> None:
        """Set the current progress."""
        ...
    
    def change_cdrom(self) -> bool:
        """Ask the user to change the CD-ROM."""
        ...
    


