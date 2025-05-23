"""
This type stub file was generated by pyright.
"""

from kivy.clock import Clock
from kivy.event import EventDispatcher

"""
This type stub file was generated by pyright.
"""
class AbstractStore(EventDispatcher):
    '''Abstract class used to implement a Store
    '''
    def __init__(self, **kwargs) -> None:
        ...
    
    def exists(self, key):
        '''Check if a key exists in the store.
        '''
        ...
    
    def async_exists(self, callback, key):
        '''Asynchronous version of :meth:`exists`.

        :Callback arguments:
            `store`: :class:`AbstractStore` instance
                Store instance
            `key`: string
                Name of the key to search for
            `result`: boo
                Result of the query, None if any error
        '''
        ...
    
    def get(self, key):
        '''Get the key-value pairs stored at `key`. If the key is not found, a
        `KeyError` exception will be thrown.
        '''
        ...
    
    def async_get(self, callback, key):
        '''Asynchronous version of :meth:`get`.

        :Callback arguments:
            `store`: :class:`AbstractStore` instance
                Store instance
            `key`: string
                Name of the key to search for
            `result`: dict
                Result of the query, None if any error
        '''
        ...
    
    def put(self, key, **values):
        '''Put new key-value pairs (given in *values*) into the storage. Any
        existing key-value pairs will be removed.
        '''
        ...
    
    def async_put(self, callback, key, **values):
        '''Asynchronous version of :meth:`put`.

        :Callback arguments:
            `store`: :class:`AbstractStore` instance
                Store instance
            `key`: string
                Name of the key to search for
            `result`: bool
                Indicate True if the storage has been updated, or False if
                nothing has been done (no changes). None if any error.
        '''
        ...
    
    def delete(self, key):
        '''Delete a key from the storage. If the key is not found, a `KeyError`
        exception will be thrown.'''
        ...
    
    def async_delete(self, callback, key):
        '''Asynchronous version of :meth:`delete`.

        :Callback arguments:
            `store`: :class:`AbstractStore` instance
                Store instance
            `key`: string
                Name of the key to search for
            `result`: bool
                Indicate True if the storage has been updated, or False if
                nothing has been done (no changes). None if any error.
        '''
        ...
    
    def find(self, **filters):
        '''Return all the entries matching the filters. The entries are
        returned through a generator as a list of (key, entry) pairs
        where *entry* is a dict of key-value pairs ::

            for key, entry in store.find(name='Mathieu'):
                print('key:', key, ', entry:', entry)

        Because it's a generator, you cannot directly use it as a list. You can
        do::

            # get all the (key, entry) availables
            entries = list(store.find(name='Mathieu'))
            # get only the entry from (key, entry)
            entries = list((x[1] for x in store.find(name='Mathieu')))
        '''
        ...
    
    def async_find(self, callback, **filters):
        '''Asynchronous version of :meth:`find`.

        The callback will be called for each entry in the result.

        :Callback arguments:
            `store`: :class:`AbstractStore` instance
                Store instance
            `key`: string
                Name of the key to search for, or None if we reach the end of
                the results
            `result`: bool
                Indicate True if the storage has been updated, or False if
                nothing has been done (no changes). None if any error.
        '''
        ...
    
    def keys(self):
        '''Return a list of all the keys in the storage.
        '''
        ...
    
    def async_keys(self, callback):
        '''Asynchronously return all the keys in the storage.
        '''
        ...
    
    def count(self):
        '''Return the number of entries in the storage.
        '''
        ...
    
    def async_count(self, callback):
        '''Asynchronously return the number of entries in the storage.
        '''
        ...
    
    def clear(self):
        '''Wipe the whole storage.
        '''
        ...
    
    def async_clear(self, callback):
        '''Asynchronous version of :meth:`clear`.
        '''
        ...
    
    def __setitem__(self, key, values):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __contains__(self, key):
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    def store_load(self):
        ...
    
    def store_sync(self):
        ...
    
    def store_get(self, key):
        ...
    
    def store_put(self, key, value):
        ...
    
    def store_exists(self, key):
        ...
    
    def store_delete(self, key):
        ...
    
    def store_find(self, filters):
        ...
    
    def store_keys(self):
        ...
    
    def store_count(self):
        ...
    
    def store_clear(self):
        ...
    
    def store_get_async(self, key, callback):
        ...
    
    def store_put_async(self, key, value, callback):
        ...
    
    def store_exists_async(self, key, callback):
        ...
    
    def store_delete_async(self, key, callback):
        ...
    
    def store_find_async(self, filters, callback):
        ...
    
    def store_count_async(self, callback):
        ...
    
    def store_keys_async(self, callback):
        ...
    
    def store_clear_async(self, callback):
        ...
    


