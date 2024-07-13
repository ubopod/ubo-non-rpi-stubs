"""
This type stub file was generated by pyright.
"""

import ctypes

_log = ...
heapNames = ...
class dma_buf_sync(ctypes.Structure):
    _fields_ = ...


DMA_BUF_SYNC_READ = ...
DMA_BUF_SYNC_WRITE = ...
DMA_BUF_SYNC_RW = ...
DMA_BUF_SYNC_START = ...
DMA_BUF_SYNC_END = ...
DMA_BUF_BASE = ...
DMA_BUF_IOCTL_SYNC = ...
DMA_BUF_SET_NAME = ...
class dma_heap_allocation_data(ctypes.Structure):
    _fields_ = ...


DMA_HEAP_IOC_MAGIC = ...
DMA_HEAP_IOCTL_ALLOC = ...
class UniqueFD:
    """Libcamera UniqueFD Class"""
    def __init__(self, fd=...) -> None:
        ...
    
    def release(self): # -> int:
        ...
    
    def get(self): # -> int:
        ...
    
    def isValid(self): # -> bool:
        ...
    


class DmaHeap:
    """DmaHeap"""
    def __init__(self) -> None:
        ...
    
    @property
    def isValid(self): # -> bool:
        ...
    
    def alloc(self, name, size) -> UniqueFD:
        ...
    
    def close(self): # -> None:
        ...
    


