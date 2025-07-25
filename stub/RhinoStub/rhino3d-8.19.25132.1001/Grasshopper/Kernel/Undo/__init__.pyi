"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Actions", "GH_UndoException", "GH_UndoState", "IGH_UndoAction", "GH_UndoAction", "GH_ObjectUndoAction", "GH_ArchivedUndoAction", "GH_UndoRecord", "GH_UndoServer"]
# endregion

# region: Imports
from GH_IO import Serialization
from Grasshopper import Kernel
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: Grasshopper, Version=8.19.25132.1001

class GH_UndoException(System.Exception):
    """Exception associated with undo events

    """
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, args: System.System.Array[object]): ...

class GH_UndoState(enum.Enum):
    undo = 0
    redo = 1

class IGH_UndoAction:
    """Base interface for all undo/redo actions

    """
    @property
    def ExpiresDisplay(self) -> bool: ...
    @property
    def ExpiresSolution(self) -> bool: ...
    @property
    def State(self) -> GH_UndoState: ...
    @overload
    def Redo(self, doc: Kernel.GH_Document) -> None: ...
    @overload
    def Undo(self, doc: Kernel.GH_Document) -> None: ...

class GH_UndoAction(object):
    """Base class implementation for undo actions.

    """
    @property
    def ExpiresDisplay(self) -> bool: ...
    @property
    def ExpiresSolution(self) -> bool: ...
    @property
    def State(self) -> GH_UndoState: ...
    @overload
    def Read(self, reader: Serialization.GH_IReader) -> bool: ...
    @overload
    def Redo(self, doc: Kernel.GH_Document) -> None: ...
    @overload
    def Undo(self, doc: Kernel.GH_Document) -> None: ...
    @overload
    def Write(self, writer: Serialization.GH_IWriter) -> bool: ...

class GH_ObjectUndoAction(GH_UndoAction):
    """Utility base class for undo actions that operate on a single IGH_DocumentObject.

    """

class GH_ArchivedUndoAction(GH_UndoAction):
    """Base class implementation for undo actions that require (de)serialization of data.

    """
    @overload
    def Read(self, reader: Serialization.GH_IReader) -> bool: ...
    @overload
    def Write(self, writer: Serialization.GH_IWriter) -> bool: ...

class GH_UndoRecord(object):
    """Represents a single undo/redo record. A single record may contain any number of undo actions.

    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, action: IGH_UndoAction): ...
    @overload
    def __init__(self, name: str, actions: System.Array[IGH_UndoAction]): ...
    @overload
    def __init__(self, name: str, actions: Generic.IEnumerable): ...
    @overload
    def AddAction(self, action: IGH_UndoAction) -> None: ...
    @property
    def ActionCount(self) -> int: ...
    @property
    def Actions(self) -> Generic.IList: ...
    @property
    def ExpiresDisplay(self) -> bool: ...
    @property
    def ExpiresSolution(self) -> bool: ...
    @property
    def Guid(self) -> System.Guid: ...
    @property
    def Name(self) -> str: ...
    @property
    def State(self) -> GH_UndoState: ...
    @property
    def Time(self) -> System.DateTime: ...
    @overload
    def Redo(self, doc: Kernel.GH_Document) -> None: ...
    @Name.setter
    def Name(self, value: System.Void): ...
    @overload
    def Undo(self, doc: Kernel.GH_Document) -> None: ...

class GH_UndoServer(object):
    """Provides access to a documents undo data.

    """
    def __init__(self, owner: Kernel.GH_Document): ...
    @overload
    def AppendToDebugLog(self, writer: Kernel.GH_DebugDescriptionWriter) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def ClearRedo() -> None: ...
    @overload
    def ClearUndo() -> None: ...
    @property
    def FirstRedoName(self) -> str: ...
    @property
    def FirstUndoName(self) -> str: ...
    @property
    def MaxRecords(self) -> int: ...
    @property
    def RedoCount(self) -> int: ...
    @property
    def RedoGuids(self) -> Generic.List: ...
    @property
    def RedoNames(self) -> Generic.List: ...
    @property
    def UndoCount(self) -> int: ...
    @property
    def UndoGuids(self) -> Generic.List: ...
    @property
    def UndoNames(self) -> Generic.List: ...
    @overload
    def MergeRecords(self, count: int) -> bool: ...
    @overload
    def PerformRedo() -> None: ...
    @overload
    def PerformUndo() -> None: ...
    @overload
    def PushUndoRecord(self, record: GH_UndoRecord) -> None: ...
    @overload
    def PushUndoRecord(self, name: str, action: GH_UndoAction) -> System.Guid: ...
    @overload
    def RemoveRecord(self, id_: System.Guid) -> bool: ...
    @MaxRecords.setter
    def MaxRecords(self, value: System.Void): ...

# endregion
