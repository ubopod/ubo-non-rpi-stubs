"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__all__ = ('install_gobject_iteration', 'install_twisted_reactor', 'uninstall_twisted_reactor', 'install_android')
def install_gobject_iteration():
    '''Import and install gobject context iteration inside our event loop.
    This is used as soon as gobject is used (like gstreamer).
    '''
    ...

g_android_redraw_count = ...
_redraw_event = ...
def install_android():
    '''Install hooks for the android platform.

    * Automatically sleep when the device is paused.
    * Automatically kill the application when the return key is pressed.
    '''
    ...

_twisted_reactor_stopper = ...
_twisted_reactor_work = ...
def install_twisted_reactor(**kwargs):
    '''Installs a threaded twisted reactor, which will schedule one
    reactor iteration before the next frame only when twisted needs
    to do some work.

    Any arguments or keyword arguments passed to this function will be
    passed on the threadedselect reactors interleave function. These
    are the arguments one would usually pass to twisted's reactor.startRunning.

    Unlike the default twisted reactor, the installed reactor will not handle
    any signals unless you set the 'installSignalHandlers' keyword argument
    to 1 explicitly. This is done to allow kivy to handle the signals as
    usual unless you specifically want the twisted reactor to handle the
    signals (e.g. SIGINT).

    .. note::
        Twisted is not included in iOS build by default. To use it on iOS,
        put the twisted distribution (and zope.interface dependency) in your
        application directory.
    '''
    ...

def uninstall_twisted_reactor():
    '''Uninstalls the Kivy's threaded Twisted Reactor. No more Twisted
    tasks will run after this got called. Use this to clean the
    `twisted.internet.reactor` .

    .. versionadded:: 1.9.0
    '''
    ...

