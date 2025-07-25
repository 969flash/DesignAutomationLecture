"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["ViewModels", "SectionSource", "SectionStyleDialog", "PrintDialogUi", "PrintWidthDialog", "PropertyListBoxDialog", "BaseDialog", "CommandDialog", "ColorList", "ColorListEntry", "ColorListDialog", "ListProperty", "ShowButtons", "ICallback", "IHandler"]
# endregion

# region: Imports
from Eto import Drawing
from Eto import Forms
from Rhino import Commands
from Rhino import Display
from Rhino import DocObjects
from Rhino import FileIO
from System import Collections
from System.Collections import Generic
from System.Collections import ObjectModel
from System.Runtime import CompilerServices
from typing import overload
import enum
import Rhino
import System
# endregion

# region: Rhino.UI, Version=8.19.25132.1001

class SectionSource(enum.Enum):
    ByClippingPlane = 0
    Custom = 1

class SectionStyleDialog(CommandDialog):
    """    """
    @overload
    def __init__(self, documentSerialNumber: System.UInt32): ...
    @overload
    def __init__(self, documentSerialNumber: System.UInt32, hatchIndex: int, rotation: float, scale: float, backfillColor: Drawing.Color, showBoundary: bool, fillRule: DocObjects.ObjectSectionFillRule): ...
    @property
    def BackfillColor(self) -> Drawing.Color: ...
    @property
    def HatchIndex(self) -> int: ...
    @property
    def RotationDegrees(self) -> float: ...
    @property
    def RotationRadians(self) -> float: ...
    @property
    def Scale(self) -> float: ...
    @property
    def SectionFillRule(self) -> DocObjects.ObjectSectionFillRule: ...
    @property
    def SectionSource(self) -> SectionSource: ...
    @property
    def ShowBoundary(self) -> bool: ...
    @BackfillColor.setter
    def BackfillColor(self, value: System.Void): ...
    @HatchIndex.setter
    def HatchIndex(self, value: System.Void): ...
    @RotationDegrees.setter
    def RotationDegrees(self, value: System.Void): ...
    @Scale.setter
    def Scale(self, value: System.Void): ...
    @SectionFillRule.setter
    def SectionFillRule(self, value: System.Void): ...
    @ShowBoundary.setter
    def ShowBoundary(self, value: System.Void): ...
    @property
    def HelpButtonClick(self): ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def LocationChanged(self): ...
    @property
    def OwnerChanged(self): ...
    @property
    def WindowStateChanged(self): ...
    @property
    def LogicalPixelSizeChanged(self): ...
    @property
    def SizeChanged(self): ...
    @property
    def KeyDown(self): ...
    @property
    def KeyUp(self): ...
    @property
    def TextInput(self): ...
    @property
    def MouseDown(self): ...
    @property
    def MouseUp(self): ...
    @property
    def MouseMove(self): ...
    @property
    def MouseLeave(self): ...
    @property
    def MouseEnter(self): ...
    @property
    def MouseDoubleClick(self): ...
    @property
    def MouseWheel(self): ...
    @property
    def GotFocus(self): ...
    @property
    def LostFocus(self): ...
    @property
    def Shown(self): ...
    @property
    def PreLoad(self): ...
    @property
    def Load(self): ...
    @property
    def LoadComplete(self): ...
    @property
    def UnLoad(self): ...
    @property
    def DragDrop(self): ...
    @property
    def DragOver(self): ...
    @property
    def DragEnter(self): ...
    @property
    def DragLeave(self): ...
    @property
    def DragEnd(self): ...
    @property
    def EnabledChanged(self): ...
    @property
    def DataContextChanged(self): ...
    @property
    def StyleChanged(self): ...

class PrintDialogUi(object):
    """    """
    def __init__(self, documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings): ...
    @overload
    @staticmethod
    def EtoExportPdf(documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings) -> None: ...
    @overload
    @staticmethod
    def EtoExportPdf(documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings, selectedObjectsOnly: bool) -> Generic.List: ...
    @overload
    @staticmethod
    def EtoExportPdfPrintOptions(documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings, selectedObjectsOnly: bool) -> Generic.List: ...
    @overload
    @staticmethod
    def EtoExportSvg(documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings) -> Display.ViewCaptureSettings: ...
    @overload
    @staticmethod
    def EtoExportSvgArray(documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings, options: FileIO.FileWriteOptions) -> Display.System.Array[Display.ViewCaptureSettings]: ...
    @overload
    @staticmethod
    def IsFileInUse(filePath: str) -> bool: ...
    @overload
    @staticmethod
    def IsPdfInUse(path: str) -> bool: ...
    @overload
    @staticmethod
    def ShowPrintDialog(dialogTitle: str, documentRuntimeSerialNumber: System.UInt32, settings: Rhino.PersistentSettings, selectedObjectsOnly: bool, showPrinterDestinations: bool) -> Commands.Result: ...
    @overload
    @staticmethod
    def ShowSavePdfFileDialog(documentName: str, documentRuntimeSerial: System.UInt32) -> (Forms.DialogResult, str): ...

class PrintWidthDialog(BaseDialog):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, title: str, message: str, selectedWidth: float): ...
    @property
    def SelectedWidth(self) -> float: ...
    @property
    def StartingValue(self) -> float: ...
    @SelectedWidth.setter
    def SelectedWidth(self, value: System.Void): ...
    @StartingValue.setter
    def StartingValue(self, value: System.Void): ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def LocationChanged(self): ...
    @property
    def OwnerChanged(self): ...
    @property
    def WindowStateChanged(self): ...
    @property
    def LogicalPixelSizeChanged(self): ...
    @property
    def SizeChanged(self): ...
    @property
    def KeyDown(self): ...
    @property
    def KeyUp(self): ...
    @property
    def TextInput(self): ...
    @property
    def MouseDown(self): ...
    @property
    def MouseUp(self): ...
    @property
    def MouseMove(self): ...
    @property
    def MouseLeave(self): ...
    @property
    def MouseEnter(self): ...
    @property
    def MouseDoubleClick(self): ...
    @property
    def MouseWheel(self): ...
    @property
    def GotFocus(self): ...
    @property
    def LostFocus(self): ...
    @property
    def Shown(self): ...
    @property
    def PreLoad(self): ...
    @property
    def Load(self): ...
    @property
    def LoadComplete(self): ...
    @property
    def UnLoad(self): ...
    @property
    def DragDrop(self): ...
    @property
    def DragOver(self): ...
    @property
    def DragEnter(self): ...
    @property
    def DragLeave(self): ...
    @property
    def DragEnd(self): ...
    @property
    def EnabledChanged(self): ...
    @property
    def DataContextChanged(self): ...
    @property
    def StyleChanged(self): ...

class PropertyListBoxDialog(BaseDialog):
    """    """
    def __init__(self, title: str, message: str, items: Collections.IList, values: Generic.IList): ...
    @property
    def Collection(self) -> ObjectModel.ObservableCollection: ...
    @property
    def Values(self) -> System.System.Array[str]: ...
    @Collection.setter
    def Collection(self, value: System.Void): ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def LocationChanged(self): ...
    @property
    def OwnerChanged(self): ...
    @property
    def WindowStateChanged(self): ...
    @property
    def LogicalPixelSizeChanged(self): ...
    @property
    def SizeChanged(self): ...
    @property
    def KeyDown(self): ...
    @property
    def KeyUp(self): ...
    @property
    def TextInput(self): ...
    @property
    def MouseDown(self): ...
    @property
    def MouseUp(self): ...
    @property
    def MouseMove(self): ...
    @property
    def MouseLeave(self): ...
    @property
    def MouseEnter(self): ...
    @property
    def MouseDoubleClick(self): ...
    @property
    def MouseWheel(self): ...
    @property
    def GotFocus(self): ...
    @property
    def LostFocus(self): ...
    @property
    def Shown(self): ...
    @property
    def PreLoad(self): ...
    @property
    def Load(self): ...
    @property
    def LoadComplete(self): ...
    @property
    def UnLoad(self): ...
    @property
    def DragDrop(self): ...
    @property
    def DragOver(self): ...
    @property
    def DragEnter(self): ...
    @property
    def DragLeave(self): ...
    @property
    def DragEnd(self): ...
    @property
    def EnabledChanged(self): ...
    @property
    def DataContextChanged(self): ...
    @property
    def StyleChanged(self): ...

class BaseDialog(Forms.Dialog):
    """    """
    def __init__(self): ...
    @property
    def Content(self) -> Forms.Control: ...
    @property
    def Message(self) -> str: ...
    @Content.setter
    def Content(self, value: System.Void): ...
    @Message.setter
    def Message(self, value: System.Void): ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def LocationChanged(self): ...
    @property
    def OwnerChanged(self): ...
    @property
    def WindowStateChanged(self): ...
    @property
    def LogicalPixelSizeChanged(self): ...
    @property
    def SizeChanged(self): ...
    @property
    def KeyDown(self): ...
    @property
    def KeyUp(self): ...
    @property
    def TextInput(self): ...
    @property
    def MouseDown(self): ...
    @property
    def MouseUp(self): ...
    @property
    def MouseMove(self): ...
    @property
    def MouseLeave(self): ...
    @property
    def MouseEnter(self): ...
    @property
    def MouseDoubleClick(self): ...
    @property
    def MouseWheel(self): ...
    @property
    def GotFocus(self): ...
    @property
    def LostFocus(self): ...
    @property
    def Shown(self): ...
    @property
    def PreLoad(self): ...
    @property
    def Load(self): ...
    @property
    def LoadComplete(self): ...
    @property
    def UnLoad(self): ...
    @property
    def DragDrop(self): ...
    @property
    def DragOver(self): ...
    @property
    def DragEnter(self): ...
    @property
    def DragLeave(self): ...
    @property
    def DragEnd(self): ...
    @property
    def EnabledChanged(self): ...
    @property
    def DataContextChanged(self): ...
    @property
    def StyleChanged(self): ...

class CommandDialog(Forms.Dialog):
    """    """
    def __init__(self): ...
    @property
    def ButtonOptions(self) -> Forms.Control: ...
    @property
    def Buttons(self) -> ShowButtons: ...
    @property
    def Content(self) -> Forms.Control: ...
    @property
    def DefaultShowButtons(self) -> ShowButtons: ...
    @property
    def FocusDefaultButtonOnLoad(self) -> bool: ...
    @property
    def SavePosition(self) -> bool: ...
    @property
    def ShowHelpButton(self) -> bool: ...
    @property
    def UpdateSourceOnApply(self) -> bool: ...
    @ButtonOptions.setter
    def ButtonOptions(self, value: System.Void): ...
    @Buttons.setter
    def Buttons(self, value: System.Void): ...
    @Content.setter
    def Content(self, value: System.Void): ...
    @FocusDefaultButtonOnLoad.setter
    def FocusDefaultButtonOnLoad(self, value: System.Void): ...
    @SavePosition.setter
    def SavePosition(self, value: System.Void): ...
    @ShowHelpButton.setter
    def ShowHelpButton(self, value: System.Void): ...
    @UpdateSourceOnApply.setter
    def UpdateSourceOnApply(self, value: System.Void): ...
    @property
    def HelpButtonClick(self): ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def LocationChanged(self): ...
    @property
    def OwnerChanged(self): ...
    @property
    def WindowStateChanged(self): ...
    @property
    def LogicalPixelSizeChanged(self): ...
    @property
    def SizeChanged(self): ...
    @property
    def KeyDown(self): ...
    @property
    def KeyUp(self): ...
    @property
    def TextInput(self): ...
    @property
    def MouseDown(self): ...
    @property
    def MouseUp(self): ...
    @property
    def MouseMove(self): ...
    @property
    def MouseLeave(self): ...
    @property
    def MouseEnter(self): ...
    @property
    def MouseDoubleClick(self): ...
    @property
    def MouseWheel(self): ...
    @property
    def GotFocus(self): ...
    @property
    def LostFocus(self): ...
    @property
    def Shown(self): ...
    @property
    def PreLoad(self): ...
    @property
    def Load(self): ...
    @property
    def LoadComplete(self): ...
    @property
    def UnLoad(self): ...
    @property
    def DragDrop(self): ...
    @property
    def DragOver(self): ...
    @property
    def DragEnter(self): ...
    @property
    def DragLeave(self): ...
    @property
    def DragEnd(self): ...
    @property
    def EnabledChanged(self): ...
    @property
    def DataContextChanged(self): ...
    @property
    def StyleChanged(self): ...

class ColorList(Generic.List):
    """    """
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, entries: Generic.IEnumerable): ...
    @property
    def Default(self) -> ColorList: ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: System.Void): ...

class ColorListEntry(object):
    """    """
    def __init__(self, name: str, color: Drawing.Color): ...
    @property
    def Color(self) -> Drawing.Color: ...
    @property
    def Name(self) -> str: ...

class ColorListDialog(Forms.ColorDialog):
    """    """
    def __init__(self): ...
    @property
    def IsActiveChangedEvent(self) -> str: ...
    @overload
    def Deactivate() -> None: ...
    @property
    def AutoDetatch(self) -> bool: ...
    @property
    def ColorList(self) -> ColorList: ...
    @property
    def IsActive(self) -> bool: ...
    @property
    def SelectedEntry(self) -> ColorListEntry: ...
    @AutoDetatch.setter
    def AutoDetatch(self, value: System.Void): ...
    @ColorList.setter
    def ColorList(self, value: System.Void): ...
    @SelectedEntry.setter
    def SelectedEntry(self, value: System.Void): ...
    @overload
    def ShowDialog(self, parent: Forms.Control) -> Forms.DialogResult: ...
    @property
    def SelectedEntryChanged(self): ...
    @property
    def IsActiveChanged(self): ...
    @property
    def ColorChanged(self): ...
    @property
    def StyleChanged(self): ...

class ListProperty(object):
    """    """
    def __init__(self): ...
    @property
    def PropertyName(self) -> str: ...
    @property
    def Value(self) -> str: ...
    @PropertyName.setter
    def PropertyName(self, value: System.Void): ...
    @Value.setter
    def Value(self, value: System.Void): ...

class ShowButtons(enum.Enum):
    Close = 1
    OKCancel = 3
    CloseHelp = 5
    OKCancelHelp = 7

class ICallback:
    """    """
    @overload
    def OnIsActiveChanged(self, widget: ColorListDialog, e: System.EventArgs) -> None: ...

class IHandler:
    """    """
    @overload
    def Deactivate() -> None: ...
    @property
    def AutoDetatch(self) -> bool: ...
    @property
    def ColorList(self) -> ColorList: ...
    @property
    def IsActive(self) -> bool: ...
    @AutoDetatch.setter
    def AutoDetatch(self, value: System.Void): ...
    @ColorList.setter
    def ColorList(self, value: System.Void): ...
    @overload
    def ShowDialog(self, parent: Forms.Control) -> Forms.DialogResult: ...

# endregion
