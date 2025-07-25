"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["GH_MRU_Entry", "GH_MRU_Server", "GH_TimeLine", "GH_TimeSpan", "GH_FileResolveState", "GH_FileEntry", "VisibleRecordCountChangedEventHandler", "MRURecordCountChangedEventHandler", "FileSelectedEventHandler"]
# endregion

# region: Imports
from Grasshopper import GUI
from System import Drawing
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: Grasshopper, Version=8.19.25132.1001

class GH_MRU_Entry(object):
    """Represents a single entry in the MRU server.

    """
    def __init__(self, new_date: System.DateTime, new_path: str): ...
    @overload
    def CompareTo(self, other: GH_MRU_Entry) -> int: ...
    @property
    def FileDate(self) -> System.DateTime: ...
    @property
    def FileName(self) -> str: ...
    @property
    def FilePath(self) -> str: ...
    @FileDate.setter
    def FileDate(self, value: System.Void): ...
    @FileName.setter
    def FileName(self, value: System.Void): ...
    @FilePath.setter
    def FilePath(self, value: System.Void): ...

class GH_MRU_Server(object):
    """Maintains a list of MRU (Most Recently Used) records.

    """
    def __init__(self): ...
    @overload
    def AppendRecentFileRecord(self, new_date: System.DateTime, new_path: str) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def ClearMissingRecords() -> None: ...
    @property
    def RecordCount(self) -> int: ...
    @property
    def Records(self) -> Generic.List: ...
    @property
    def VisibleRecords(self) -> int: ...
    @overload
    def ReadList() -> None: ...
    @VisibleRecords.setter
    def VisibleRecords(self, value: System.Void): ...
    @overload
    def WriteList() -> None: ...
    @property
    def VisibleRecordCountChanged(self): ...
    @property
    def MRURecordCountChanged(self): ...

class GH_TimeLine(GUI.GH_DoubleBufferedPanel):
    """    """
    def __init__(self): ...
    @property
    def ScrollWidth(self) -> int: ...
    @property
    def ActiveEntry(self) -> GH_FileEntry: ...
    @property
    def Offset(self) -> int: ...
    @ActiveEntry.setter
    def ActiveEntry(self, value: System.Void): ...
    @overload
    def SetupTimeline() -> None: ...
    @overload
    def SetupTimeline(self, entries: Generic.IEnumerable) -> None: ...
    @property
    def FileSelected(self): ...
    @property
    def AutoSizeChanged(self): ...
    @property
    def KeyUp(self): ...
    @property
    def KeyDown(self): ...
    @property
    def KeyPress(self): ...
    @property
    def TextChanged(self): ...
    @property
    def Scroll(self): ...
    @property
    def BackColorChanged(self): ...
    @property
    def BackgroundImageChanged(self): ...
    @property
    def BackgroundImageLayoutChanged(self): ...
    @property
    def BindingContextChanged(self): ...
    @property
    def CausesValidationChanged(self): ...
    @property
    def ClientSizeChanged(self): ...
    @property
    def ContextMenuStripChanged(self): ...
    @property
    def CursorChanged(self): ...
    @property
    def DockChanged(self): ...
    @property
    def EnabledChanged(self): ...
    @property
    def FontChanged(self): ...
    @property
    def ForeColorChanged(self): ...
    @property
    def LocationChanged(self): ...
    @property
    def MarginChanged(self): ...
    @property
    def RegionChanged(self): ...
    @property
    def RightToLeftChanged(self): ...
    @property
    def SizeChanged(self): ...
    @property
    def TabIndexChanged(self): ...
    @property
    def TabStopChanged(self): ...
    @property
    def VisibleChanged(self): ...
    @property
    def Click(self): ...
    @property
    def ControlAdded(self): ...
    @property
    def ControlRemoved(self): ...
    @property
    def DataContextChanged(self): ...
    @property
    def DragDrop(self): ...
    @property
    def DragEnter(self): ...
    @property
    def DragOver(self): ...
    @property
    def DragLeave(self): ...
    @property
    def GiveFeedback(self): ...
    @property
    def HandleCreated(self): ...
    @property
    def HandleDestroyed(self): ...
    @property
    def HelpRequested(self): ...
    @property
    def Invalidated(self): ...
    @property
    def PaddingChanged(self): ...
    @property
    def Paint(self): ...
    @property
    def QueryContinueDrag(self): ...
    @property
    def QueryAccessibilityHelp(self): ...
    @property
    def DoubleClick(self): ...
    @property
    def Enter(self): ...
    @property
    def GotFocus(self): ...
    @property
    def Layout(self): ...
    @property
    def Leave(self): ...
    @property
    def LostFocus(self): ...
    @property
    def MouseClick(self): ...
    @property
    def MouseDoubleClick(self): ...
    @property
    def MouseCaptureChanged(self): ...
    @property
    def MouseDown(self): ...
    @property
    def MouseEnter(self): ...
    @property
    def MouseLeave(self): ...
    @property
    def DpiChangedBeforeParent(self): ...
    @property
    def DpiChangedAfterParent(self): ...
    @property
    def MouseHover(self): ...
    @property
    def MouseMove(self): ...
    @property
    def MouseUp(self): ...
    @property
    def MouseWheel(self): ...
    @property
    def Move(self): ...
    @property
    def PreviewKeyDown(self): ...
    @property
    def Resize(self): ...
    @property
    def ChangeUICues(self): ...
    @property
    def StyleChanged(self): ...
    @property
    def SystemColorsChanged(self): ...
    @property
    def Validating(self): ...
    @property
    def Validated(self): ...
    @property
    def ParentChanged(self): ...
    @property
    def ImeModeChanged(self): ...
    @property
    def Disposed(self): ...

class GH_TimeSpan(object):
    """    """
    def __init__(self, owner: GH_TimeLine): ...
    @property
    def TextColumnWidth(self) -> int: ...
    @overload
    def ContainsDate(self, d: System.DateTime) -> bool: ...
    @property
    def Bounds(self) -> Drawing.Rectangle: ...
    @property
    def Entries(self) -> Generic.List: ...
    @property
    def SpanEnd(self) -> System.DateTime: ...
    @property
    def SpanStart(self) -> System.DateTime: ...
    @property
    def SpanText(self) -> str: ...
    @overload
    def Layout(self, y: int, width: int) -> None: ...
    @overload
    def LayoutWidth(self, width: int) -> None: ...
    @overload
    def PaintSpan(self, graphics: Drawing.Graphics) -> None: ...
    @Bounds.setter
    def Bounds(self, value: System.Void): ...
    @SpanEnd.setter
    def SpanEnd(self, value: System.Void): ...
    @SpanStart.setter
    def SpanStart(self, value: System.Void): ...
    @SpanText.setter
    def SpanText(self, value: System.Void): ...

class GH_FileResolveState(enum.Enum):
    Unresolved = 0
    Invalid = 1
    Valid = 2

class GH_FileEntry(object):
    """    """
    def __init__(self, owner: GH_TimeLine, path: str, date: System.DateTime, name: str): ...
    @property
    def EntryHeight(self) -> int: ...
    @overload
    def CompareTo(self, other: GH_FileEntry) -> int: ...
    @property
    def Bounds(self) -> Drawing.Rectangle: ...
    @property
    def FileDate(self) -> System.DateTime: ...
    @property
    def FileName(self) -> str: ...
    @property
    def FilePath(self) -> str: ...
    @property
    def Icon(self) -> Drawing.Bitmap: ...
    @property
    def ResolvedState(self) -> GH_FileResolveState: ...
    @overload
    def LayoutWidth(self, width: int) -> None: ...
    @overload
    def PaintEntry(self, graphics: Drawing.Graphics) -> None: ...
    @overload
    def ResolveFileState() -> None: ...
    @Bounds.setter
    def Bounds(self, value: System.Void): ...

class VisibleRecordCountChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, newCount: int, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, newCount: int) -> None: ...

class MRURecordCountChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, server: GH_MRU_Server, count: int, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, server: GH_MRU_Server, count: int) -> None: ...

class FileSelectedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: GH_TimeLine, path: str, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: GH_TimeLine, path: str) -> None: ...

# endregion
