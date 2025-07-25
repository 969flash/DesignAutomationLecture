"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["PrintingPermissionLevel"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from typing import overload
import enum
# endregion

# region: Exports
__all__ = ["PrinterUnit", "PreviewPageInfo", "PreviewPrintController", "PrintEventHandler", "PrintAction", "PrintController", "PrintPageEventHandler", "QueryPageSettingsEventArgs", "QueryPageSettingsEventHandler", "Duplex", "InvalidPrinterException", "Margins", "MarginsConverter", "PaperKind", "PaperSize", "PaperSource", "PaperSourceKind", "PrinterResolution", "PrinterResolutionKind", "PrinterUnitConvert", "PrintRange", "StandardPrintController", "PageSettings", "PrintDocument", "PrinterSettings", "PrintEventArgs", "PrintPageEventArgs", "PaperSizeCollection", "PaperSourceCollection", "PrinterResolutionCollection", "StringCollection"]
# endregion

# region: Imports
from System import Collections
from System import ComponentModel
from System import Drawing
from System import Globalization
from System.Drawing import Imaging
from System.Runtime import CompilerServices
from System.Runtime import Serialization
from typing import overload
import enum
import System
# endregion

# region: System.Drawing.Common, Version=7.0.0.0

class PrinterUnit(enum.Enum):
    Display = 0
    ThousandthsOfAnInch = 1
    HundredthsOfAMillimeter = 2
    TenthsOfAMillimeter = 3

class PreviewPageInfo(object):
    """    """
    def __init__(self, image: Drawing.Image, physicalSize: Drawing.Size): ...
    @property
    def Image(self) -> Drawing.Image: ...
    @property
    def PhysicalSize(self) -> Drawing.Size: ...

class PreviewPrintController(PrintController):
    """    """
    def __init__(self): ...
    @property
    def IsPreview(self) -> bool: ...
    @property
    def UseAntiAlias(self) -> bool: ...
    @overload
    def GetPreviewPageInfo() -> System.Array[PreviewPageInfo]: ...
    @overload
    def OnEndPage(self, document: PrintDocument, e: PrintPageEventArgs) -> None: ...
    @overload
    def OnEndPrint(self, document: PrintDocument, e: PrintEventArgs) -> None: ...
    @overload
    def OnStartPage(self, document: PrintDocument, e: PrintPageEventArgs) -> Drawing.Graphics: ...
    @overload
    def OnStartPrint(self, document: PrintDocument, e: PrintEventArgs) -> None: ...
    @UseAntiAlias.setter
    def UseAntiAlias(self, value: System.Void): ...

class PrintEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: PrintEventArgs, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: PrintEventArgs) -> None: ...

class PrintAction(enum.Enum):
    PrintToFile = 0
    PrintToPreview = 1
    PrintToPrinter = 2

class PrintController(object):
    """    """
    @property
    def IsPreview(self) -> bool: ...
    @overload
    def OnEndPage(self, document: PrintDocument, e: PrintPageEventArgs) -> None: ...
    @overload
    def OnEndPrint(self, document: PrintDocument, e: PrintEventArgs) -> None: ...
    @overload
    def OnStartPage(self, document: PrintDocument, e: PrintPageEventArgs) -> Drawing.Graphics: ...
    @overload
    def OnStartPrint(self, document: PrintDocument, e: PrintEventArgs) -> None: ...

class PrintPageEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: PrintPageEventArgs, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: PrintPageEventArgs) -> None: ...

class QueryPageSettingsEventArgs(PrintEventArgs):
    """    """
    def __init__(self, pageSettings: PageSettings): ...
    @property
    def PageSettings(self) -> PageSettings: ...
    @PageSettings.setter
    def PageSettings(self, value: System.Void): ...

class QueryPageSettingsEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: QueryPageSettingsEventArgs, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: QueryPageSettingsEventArgs) -> None: ...

class Duplex(enum.Enum):
    Simplex = 1
    Vertical = 2
    Horizontal = 3
    Default = -1

class InvalidPrinterException(System.SystemException):
    """    """
    def __init__(self, settings: PrinterSettings): ...
    @overload
    def GetObjectData(self, info: Serialization.SerializationInfo, context: Serialization.StreamingContext) -> None: ...

class Margins(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, left: int, right: int, top: int, bottom: int): ...
    @overload
    def Clone() -> object: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Bottom(self) -> int: ...
    @property
    def Left(self) -> int: ...
    @property
    def Right(self) -> int: ...
    @property
    def Top(self) -> int: ...
    @overload
    def GetHashCode() -> int: ...
    @Bottom.setter
    def Bottom(self, value: System.Void): ...
    @Left.setter
    def Left(self, value: System.Void): ...
    @Right.setter
    def Right(self, value: System.Void): ...
    @Top.setter
    def Top(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class MarginsConverter(ComponentModel.ExpandableObjectConverter):
    """    """
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ComponentModel.ITypeDescriptorContext, sourceType: System.Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ComponentModel.ITypeDescriptorContext, destinationType: System.Type) -> bool: ...
    @overload
    def ConvertFrom(self, context: ComponentModel.ITypeDescriptorContext, culture: Globalization.CultureInfo, value: object) -> object: ...
    @overload
    def ConvertTo(self, context: ComponentModel.ITypeDescriptorContext, culture: Globalization.CultureInfo, value: object, destinationType: System.Type) -> object: ...
    @overload
    def CreateInstance(self, context: ComponentModel.ITypeDescriptorContext, propertyValues: Collections.IDictionary) -> object: ...
    @overload
    def GetCreateInstanceSupported(self, context: ComponentModel.ITypeDescriptorContext) -> bool: ...

class PaperKind(enum.Enum):
    Custom = 0
    Letter = 1
    LetterSmall = 2
    Tabloid = 3
    Ledger = 4
    Legal = 5
    Statement = 6
    Executive = 7
    A3 = 8
    A4 = 9
    A4Small = 10
    A5 = 11
    B4 = 12
    B5 = 13
    Folio = 14
    Quarto = 15
    Standard10x14 = 16
    Standard11x17 = 17
    Note = 18
    Number9Envelope = 19
    Number10Envelope = 20
    Number11Envelope = 21
    Number12Envelope = 22
    Number14Envelope = 23
    CSheet = 24
    DSheet = 25
    ESheet = 26
    DLEnvelope = 27
    C5Envelope = 28
    C3Envelope = 29
    C4Envelope = 30
    C6Envelope = 31
    C65Envelope = 32
    B4Envelope = 33
    B5Envelope = 34
    B6Envelope = 35
    ItalyEnvelope = 36
    MonarchEnvelope = 37
    PersonalEnvelope = 38
    USStandardFanfold = 39
    GermanStandardFanfold = 40
    GermanLegalFanfold = 41
    IsoB4 = 42
    JapanesePostcard = 43
    Standard9x11 = 44
    Standard10x11 = 45
    Standard15x11 = 46
    InviteEnvelope = 47
    LetterExtra = 50
    LegalExtra = 51
    TabloidExtra = 52
    A4Extra = 53
    LetterTransverse = 54
    A4Transverse = 55
    LetterExtraTransverse = 56
    APlus = 57
    BPlus = 58
    LetterPlus = 59
    A4Plus = 60
    A5Transverse = 61
    B5Transverse = 62
    A3Extra = 63
    A5Extra = 64
    B5Extra = 65
    A2 = 66
    A3Transverse = 67
    A3ExtraTransverse = 68
    JapaneseDoublePostcard = 69
    A6 = 70
    JapaneseEnvelopeKakuNumber2 = 71
    JapaneseEnvelopeKakuNumber3 = 72
    JapaneseEnvelopeChouNumber3 = 73
    JapaneseEnvelopeChouNumber4 = 74
    LetterRotated = 75
    A3Rotated = 76
    A4Rotated = 77
    A5Rotated = 78
    B4JisRotated = 79
    B5JisRotated = 80
    JapanesePostcardRotated = 81
    JapaneseDoublePostcardRotated = 82
    A6Rotated = 83
    JapaneseEnvelopeKakuNumber2Rotated = 84
    JapaneseEnvelopeKakuNumber3Rotated = 85
    JapaneseEnvelopeChouNumber3Rotated = 86
    JapaneseEnvelopeChouNumber4Rotated = 87
    B6Jis = 88
    B6JisRotated = 89
    Standard12x11 = 90
    JapaneseEnvelopeYouNumber4 = 91
    JapaneseEnvelopeYouNumber4Rotated = 92
    Prc16K = 93
    Prc32K = 94
    Prc32KBig = 95
    PrcEnvelopeNumber1 = 96
    PrcEnvelopeNumber2 = 97
    PrcEnvelopeNumber3 = 98
    PrcEnvelopeNumber4 = 99
    PrcEnvelopeNumber5 = 100
    PrcEnvelopeNumber6 = 101
    PrcEnvelopeNumber7 = 102
    PrcEnvelopeNumber8 = 103
    PrcEnvelopeNumber9 = 104
    PrcEnvelopeNumber10 = 105
    Prc16KRotated = 106
    Prc32KRotated = 107
    Prc32KBigRotated = 108
    PrcEnvelopeNumber1Rotated = 109
    PrcEnvelopeNumber2Rotated = 110
    PrcEnvelopeNumber3Rotated = 111
    PrcEnvelopeNumber4Rotated = 112
    PrcEnvelopeNumber5Rotated = 113
    PrcEnvelopeNumber6Rotated = 114
    PrcEnvelopeNumber7Rotated = 115
    PrcEnvelopeNumber8Rotated = 116
    PrcEnvelopeNumber9Rotated = 117
    PrcEnvelopeNumber10Rotated = 118

class PaperSize(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str, width: int, height: int): ...
    @property
    def Height(self) -> int: ...
    @property
    def Kind(self) -> PaperKind: ...
    @property
    def PaperName(self) -> str: ...
    @property
    def RawKind(self) -> int: ...
    @property
    def Width(self) -> int: ...
    @Height.setter
    def Height(self, value: System.Void): ...
    @PaperName.setter
    def PaperName(self, value: System.Void): ...
    @RawKind.setter
    def RawKind(self, value: System.Void): ...
    @Width.setter
    def Width(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class PaperSource(object):
    """    """
    def __init__(self): ...
    @property
    def Kind(self) -> PaperSourceKind: ...
    @property
    def RawKind(self) -> int: ...
    @property
    def SourceName(self) -> str: ...
    @RawKind.setter
    def RawKind(self, value: System.Void): ...
    @SourceName.setter
    def SourceName(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class PaperSourceKind(enum.Enum):
    Upper = 1
    Lower = 2
    Middle = 3
    Manual = 4
    Envelope = 5
    ManualFeed = 6
    AutomaticFeed = 7
    TractorFeed = 8
    SmallFormat = 9
    LargeFormat = 10
    LargeCapacity = 11
    Cassette = 14
    FormSource = 15
    Custom = 257

class PrinterResolution(object):
    """    """
    def __init__(self): ...
    @property
    def Kind(self) -> PrinterResolutionKind: ...
    @property
    def X(self) -> int: ...
    @property
    def Y(self) -> int: ...
    @Kind.setter
    def Kind(self, value: System.Void): ...
    @X.setter
    def X(self, value: System.Void): ...
    @Y.setter
    def Y(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class PrinterResolutionKind(enum.Enum):
    Custom = 0
    High = -4
    Medium = -3
    Low = -2
    Draft = -1

class PrinterUnitConvert(object):
    """    """
    @overload
    @staticmethod
    def Convert(value: float, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> float: ...
    @overload
    @staticmethod
    def Convert(value: int, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> int: ...
    @overload
    @staticmethod
    def Convert(value: Drawing.Point, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Drawing.Point: ...
    @overload
    @staticmethod
    def Convert(value: Drawing.Size, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Drawing.Size: ...
    @overload
    @staticmethod
    def Convert(value: Drawing.Rectangle, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Drawing.Rectangle: ...
    @overload
    @staticmethod
    def Convert(value: Margins, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Margins: ...

class PrintRange(enum.Enum):
    AllPages = 0
    Selection = 1
    SomePages = 2
    CurrentPage = 4194304

class StandardPrintController(PrintController):
    """    """
    def __init__(self): ...
    @overload
    def OnEndPage(self, document: PrintDocument, e: PrintPageEventArgs) -> None: ...
    @overload
    def OnEndPrint(self, document: PrintDocument, e: PrintEventArgs) -> None: ...
    @overload
    def OnStartPage(self, document: PrintDocument, e: PrintPageEventArgs) -> Drawing.Graphics: ...
    @overload
    def OnStartPrint(self, document: PrintDocument, e: PrintEventArgs) -> None: ...

class PageSettings(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, printerSettings: PrinterSettings): ...
    @overload
    def Clone() -> object: ...
    @overload
    def CopyToHdevmode(self, hdevmode: System.IntPtr) -> None: ...
    @property
    def Bounds(self) -> Drawing.Rectangle: ...
    @property
    def Color(self) -> bool: ...
    @property
    def HardMarginX(self) -> System.Single: ...
    @property
    def HardMarginY(self) -> System.Single: ...
    @property
    def Landscape(self) -> bool: ...
    @property
    def Margins(self) -> Margins: ...
    @property
    def PaperSize(self) -> PaperSize: ...
    @property
    def PaperSource(self) -> PaperSource: ...
    @property
    def PrintableArea(self) -> Drawing.RectangleF: ...
    @property
    def PrinterResolution(self) -> PrinterResolution: ...
    @property
    def PrinterSettings(self) -> PrinterSettings: ...
    @Color.setter
    def Color(self, value: System.Void): ...
    @Landscape.setter
    def Landscape(self, value: System.Void): ...
    @Margins.setter
    def Margins(self, value: System.Void): ...
    @PaperSize.setter
    def PaperSize(self, value: System.Void): ...
    @PaperSource.setter
    def PaperSource(self, value: System.Void): ...
    @PrinterResolution.setter
    def PrinterResolution(self, value: System.Void): ...
    @PrinterSettings.setter
    def PrinterSettings(self, value: System.Void): ...
    @overload
    def SetHdevmode(self, hdevmode: System.IntPtr) -> None: ...
    @overload
    def ToString() -> str: ...

class PrintDocument(ComponentModel.Component):
    """    """
    def __init__(self): ...
    @property
    def DefaultPageSettings(self) -> PageSettings: ...
    @property
    def DocumentName(self) -> str: ...
    @property
    def OriginAtMargins(self) -> bool: ...
    @property
    def PrintController(self) -> PrintController: ...
    @property
    def PrinterSettings(self) -> PrinterSettings: ...
    @overload
    def Print() -> None: ...
    @DefaultPageSettings.setter
    def DefaultPageSettings(self, value: System.Void): ...
    @DocumentName.setter
    def DocumentName(self, value: System.Void): ...
    @OriginAtMargins.setter
    def OriginAtMargins(self, value: System.Void): ...
    @PrintController.setter
    def PrintController(self, value: System.Void): ...
    @PrinterSettings.setter
    def PrinterSettings(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @property
    def BeginPrint(self): ...
    @property
    def EndPrint(self): ...
    @property
    def PrintPage(self): ...
    @property
    def QueryPageSettings(self): ...
    @property
    def Disposed(self): ...

class PrinterSettings(object):
    """    """
    def __init__(self): ...
    @overload
    def Clone() -> object: ...
    @overload
    def CreateMeasurementGraphics() -> Drawing.Graphics: ...
    @overload
    def CreateMeasurementGraphics(self, pageSettings: PageSettings) -> Drawing.Graphics: ...
    @overload
    def CreateMeasurementGraphics(self, honorOriginAtMargins: bool) -> Drawing.Graphics: ...
    @overload
    def CreateMeasurementGraphics(self, pageSettings: PageSettings, honorOriginAtMargins: bool) -> Drawing.Graphics: ...
    @property
    def CanDuplex(self) -> bool: ...
    @property
    def Collate(self) -> bool: ...
    @property
    def Copies(self) -> System.Int16: ...
    @property
    def DefaultPageSettings(self) -> PageSettings: ...
    @property
    def Duplex(self) -> Duplex: ...
    @property
    def FromPage(self) -> int: ...
    @property
    def InstalledPrinters(self) -> StringCollection: ...
    @property
    def IsDefaultPrinter(self) -> bool: ...
    @property
    def IsPlotter(self) -> bool: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def LandscapeAngle(self) -> int: ...
    @property
    def MaximumCopies(self) -> int: ...
    @property
    def MaximumPage(self) -> int: ...
    @property
    def MinimumPage(self) -> int: ...
    @property
    def PaperSizes(self) -> PaperSizeCollection: ...
    @property
    def PaperSources(self) -> PaperSourceCollection: ...
    @property
    def PrinterName(self) -> str: ...
    @property
    def PrinterResolutions(self) -> PrinterResolutionCollection: ...
    @property
    def PrintFileName(self) -> str: ...
    @property
    def PrintRange(self) -> PrintRange: ...
    @property
    def PrintToFile(self) -> bool: ...
    @property
    def SupportsColor(self) -> bool: ...
    @property
    def ToPage(self) -> int: ...
    @overload
    def GetHdevmode() -> System.IntPtr: ...
    @overload
    def GetHdevmode(self, pageSettings: PageSettings) -> System.IntPtr: ...
    @overload
    def GetHdevnames() -> System.IntPtr: ...
    @overload
    def IsDirectPrintingSupported(self, imageFormat: Imaging.ImageFormat) -> bool: ...
    @overload
    def IsDirectPrintingSupported(self, image: Drawing.Image) -> bool: ...
    @Collate.setter
    def Collate(self, value: System.Void): ...
    @Copies.setter
    def Copies(self, value: System.Void): ...
    @Duplex.setter
    def Duplex(self, value: System.Void): ...
    @FromPage.setter
    def FromPage(self, value: System.Void): ...
    @MaximumPage.setter
    def MaximumPage(self, value: System.Void): ...
    @MinimumPage.setter
    def MinimumPage(self, value: System.Void): ...
    @PrinterName.setter
    def PrinterName(self, value: System.Void): ...
    @PrintFileName.setter
    def PrintFileName(self, value: System.Void): ...
    @PrintRange.setter
    def PrintRange(self, value: System.Void): ...
    @PrintToFile.setter
    def PrintToFile(self, value: System.Void): ...
    @ToPage.setter
    def ToPage(self, value: System.Void): ...
    @overload
    def SetHdevmode(self, hdevmode: System.IntPtr) -> None: ...
    @overload
    def SetHdevnames(self, hdevnames: System.IntPtr) -> None: ...
    @overload
    def ToString() -> str: ...

class PrintEventArgs(ComponentModel.CancelEventArgs):
    """    """
    def __init__(self): ...
    @property
    def PrintAction(self) -> PrintAction: ...

class PrintPageEventArgs(System.EventArgs):
    """    """
    def __init__(self, graphics: Drawing.Graphics, marginBounds: Drawing.Rectangle, pageBounds: Drawing.Rectangle, pageSettings: PageSettings): ...
    @property
    def Cancel(self) -> bool: ...
    @property
    def Graphics(self) -> Drawing.Graphics: ...
    @property
    def HasMorePages(self) -> bool: ...
    @property
    def MarginBounds(self) -> Drawing.Rectangle: ...
    @property
    def PageBounds(self) -> Drawing.Rectangle: ...
    @property
    def PageSettings(self) -> PageSettings: ...
    @Cancel.setter
    def Cancel(self, value: System.Void): ...
    @HasMorePages.setter
    def HasMorePages(self, value: System.Void): ...

class PaperSizeCollection(object):
    """    """
    def __init__(self, array: System.Array[PaperSize]): ...
    @overload
    def Add(self, paperSize: PaperSize) -> int: ...
    @overload
    def CopyTo(self, paperSizes: System.Array[PaperSize], index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> PaperSize: ...
    @overload
    def GetEnumerator() -> Collections.IEnumerator: ...

class PaperSourceCollection(object):
    """    """
    def __init__(self, array: System.Array[PaperSource]): ...
    @overload
    def Add(self, paperSource: PaperSource) -> int: ...
    @overload
    def CopyTo(self, paperSources: System.Array[PaperSource], index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> PaperSource: ...
    @overload
    def GetEnumerator() -> Collections.IEnumerator: ...

class PrinterResolutionCollection(object):
    """    """
    def __init__(self, array: System.Array[PrinterResolution]): ...
    @overload
    def Add(self, printerResolution: PrinterResolution) -> int: ...
    @overload
    def CopyTo(self, printerResolutions: System.Array[PrinterResolution], index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> PrinterResolution: ...
    @overload
    def GetEnumerator() -> Collections.IEnumerator: ...

class StringCollection(object):
    """    """
    def __init__(self, array: System.System.Array[str]): ...
    @overload
    def Add(self, value: str) -> int: ...
    @overload
    def CopyTo(self, strings: System.System.Array[str], index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> str: ...
    @overload
    def GetEnumerator() -> Collections.IEnumerator: ...

# endregion

# region: System.Security.Permissions, Version=7.0.0.0

class PrintingPermissionLevel(enum.Enum):
    NoPrinting = 0
    SafePrinting = 1
    DefaultPrinting = 2
    AllPrinting = 3

# endregion
