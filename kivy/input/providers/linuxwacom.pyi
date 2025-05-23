"""
This type stub file was generated by pyright.
"""

import os
from kivy.input.motionevent import MotionEvent
from kivy.input.provider import MotionEventProvider

"""
This type stub file was generated by pyright.
"""
__all__ = ('LinuxWacomMotionEventProvider', 'LinuxWacomMotionEvent')
class LinuxWacomMotionEvent(MotionEvent):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def depack(self, args):
        ...
    
    def __str__(self) -> str:
        ...
    


if 'KIVY_DOC' in os.environ:
    LinuxWacomMotionEventProvider = ...
else:
    EV_SYN = ...
    EV_KEY = ...
    EV_REL = ...
    EV_ABS = ...
    EV_MSC = ...
    EV_SW = ...
    EV_LED = ...
    EV_SND = ...
    EV_REP = ...
    EV_FF = ...
    EV_PWR = ...
    EV_FF_STATUS = ...
    EV_MAX = ...
    EV_CNT = ...
    KEY_MAX = ...
    SYN_REPORT = ...
    SYN_CONFIG = ...
    SYN_MT_REPORT = ...
    MSC_SERIAL = ...
    MSC_PULSELED = ...
    MSC_GESTURE = ...
    MSC_RAW = ...
    MSC_SCAN = ...
    MSC_MAX = ...
    MSC_CNT = ...
    ABS_X = ...
    ABS_Y = ...
    ABS_PRESSURE = ...
    ABS_MISC = ...
    ABS_MT_TOUCH_MAJOR = ...
    ABS_MT_TOUCH_MINOR = ...
    ABS_MT_WIDTH_MAJOR = ...
    ABS_MT_WIDTH_MINOR = ...
    ABS_MT_ORIENTATION = ...
    ABS_MT_POSITION_X = ...
    ABS_MT_POSITION_Y = ...
    ABS_MT_TOOL_TYPE = ...
    ABS_MT_BLOB_ID = ...
    ABS_MT_TRACKING_ID = ...
    ABS_MT_PRESSURE = ...
    EVIOCGNAME = ...
    EVIOCGBIT = ...
    EVIOCGABS = ...
    struct_input_event_sz = ...
    struct_input_absinfo_sz = ...
    sz_l = ...
    class LinuxWacomMotionEventProvider(MotionEventProvider):
        options = ...
        def __init__(self, device, args) -> None:
            ...
        
        def start(self):
            ...
        
        def update(self, dispatch_fn):
            ...
        
    
    
