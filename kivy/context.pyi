"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__all__ = ('Context', 'ProxyContext', 'register_context', 'get_current_context')
_contexts = ...
_default_context = ...
_context_stack = ...
class ProxyContext:
    __slots__ = ...
    def __init__(self, obj) -> None:
        ...
    
    def __getattribute__(self, name):
        ...
    
    def __delattr__(self, name):
        ...
    
    def __setattr__(self, name, value):
        ...
    
    def __bool__(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self):
        ...
    


class Context(dict):
    def __init__(self, init=...) -> None:
        ...
    
    def push(self):
        ...
    
    def pop(self):
        ...
    


def register_context(name, cls, *args, **kwargs):
    '''Register a new context.
    '''
    ...

def get_current_context():
    '''Return the current context.
    '''
    ...

_default_context = ...
