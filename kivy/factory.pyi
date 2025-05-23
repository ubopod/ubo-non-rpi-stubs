"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__all__ = ('Factory', 'FactoryBase', 'FactoryException')
class FactoryException(Exception):
    ...


class FactoryBase:
    def __init__(self) -> None:
        ...
    
    @classmethod
    def create_from(cls, factory):
        """Creates a instance of the class, and initializes to the state of
        ``factory``.

        :param factory: The factory to initialize from.
        :return: A new instance of this class.
        """
        ...
    
    def is_template(self, classname):
        '''Return True if the classname is a template from the
        :class:`~kivy.lang.Builder`.

        .. versionadded:: 1.0.5
        '''
        ...
    
    def register(self, classname, cls=..., module=..., is_template=..., baseclasses=..., filename=..., warn=...):
        '''Register a new classname referring to a real class or
        class definition in a module. Warn, if True will emit a warning message
        when a class is re-declared.

        .. versionchanged:: 1.9.0
            `warn` was added.

        .. versionchanged:: 1.7.0
            :attr:`baseclasses` and :attr:`filename` added

        .. versionchanged:: 1.0.5
            :attr:`is_template` has been added in 1.0.5.
        '''
        ...
    
    def unregister(self, *classnames):
        '''Unregisters the classnames previously registered via the
        register method. This allows the same classnames to be re-used in
        different contexts.

        .. versionadded:: 1.7.1
        '''
        ...
    
    def unregister_from_filename(self, filename):
        '''Unregister all the factory objects related to the filename passed in
        the parameter.

        .. versionadded:: 1.7.0
        '''
        ...
    
    def __getattr__(self, name):
        ...
    
    get = ...


Factory: FactoryBase = ...
if __name__ == '__main__':
    ...
