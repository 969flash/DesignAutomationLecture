"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["ObjectiveCMarshal", "UnhandledExceptionPropagationHandler", "MessageSendFunction", "ObjectiveCTrackedTypeAttribute"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from System.Runtime import InteropServices
from typing import overload
import enum
import System
# endregion

# region: System.Private.CoreLib, Version=7.0.0.0

class ObjectiveCMarshal(object):
    """    """
    @overload
    @staticmethod
    def CreateReferenceTrackingHandle(obj: object) -> (InteropServices.GCHandle, System.Span): ...
    @overload
    @staticmethod
    def Initialize(beginEndCallback: System.IntPtr, isReferencedCallback: System.IntPtr, trackedObjectEnteredFinalization: System.IntPtr, unhandledExceptionPropagationHandler: UnhandledExceptionPropagationHandler) -> None: ...
    @overload
    @staticmethod
    def SetMessageSendCallback(msgSendFunction: MessageSendFunction, func: System.IntPtr) -> None: ...
    @overload
    @staticmethod
    def SetMessageSendPendingException(exception: System.Exception) -> None: ...

class UnhandledExceptionPropagationHandler(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, exception: System.Exception, lastMethod: System.RuntimeMethodHandle, callback: System.AsyncCallback, object_: object) -> (System.IAsyncResult, System.IntPtr): ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> (System.IntPtr, System.IntPtr): ...
    @overload
    def Invoke(self, exception: System.Exception, lastMethod: System.RuntimeMethodHandle) -> (System.IntPtr, System.IntPtr): ...

class MessageSendFunction(enum.Enum):
    MsgSend = 0
    MsgSendFpret = 1
    MsgSendStret = 2
    MsgSendSuper = 3
    MsgSendSuperStret = 4

class ObjectiveCTrackedTypeAttribute(System.Attribute):
    """    """
    def __init__(self): ...

# endregion
