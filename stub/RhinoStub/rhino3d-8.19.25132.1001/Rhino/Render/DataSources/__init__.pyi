"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Modes", "Shapes", "Sizes", "MetaData", "AssignBys", "RhinoSettings", "RdkSelectionNavigator", "ContentFactories", "ContentFactory", "RdkEdit"]
# endregion

# region: Imports
from Rhino import Display
from Rhino import DocObjects
from Rhino import Render
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: RhinoCommon, Version=8.19.25132.1001

class Modes(enum.Enum):
    Unset = 0
    Grid = 1
    List = 2
    Tree = 3

class Shapes(enum.Enum):
    Square = 0
    Wide = 1

class Sizes(enum.Enum):
    Unset = 0
    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4

class MetaData(object):
    """    """
    def __init__(self, pMetaData: System.IntPtr): ...
    @overload
    def ContentInstanceId() -> System.Guid: ...
    @overload
    def Dispose() -> None: ...
    @overload
    def Geometry() -> str: ...
    @property
    def CppPointer(self) -> System.IntPtr: ...

class AssignBys(enum.Enum):
    Unset = 0
    Layer = 1
    Parent = 2
    Object = 3
    Varies = 4
    PlugIn = 5

class RhinoSettings(object):
    """    """
    def __init__(self, pRhinoSettings: System.IntPtr): ...
    @overload
    def ActiveView() -> Display.RhinoView: ...
    @overload
    def Dispose() -> None: ...
    @property
    def CppPointer(self) -> System.IntPtr: ...
    @property
    def CustomImageSizeIsPreset(self) -> bool: ...
    @overload
    def GetCurrentRenderer() -> System.Guid: ...
    @overload
    def GetCustomRenderSizes() -> Generic.List: ...
    @overload
    def GetRenderSettings() -> Render.RenderSettings: ...
    @overload
    def GroundPlaneOnInViewDisplayMode(self, view: Display.RhinoView) -> bool: ...
    @overload
    def RenderingView() -> DocObjects.ViewInfo: ...
    @CustomImageSizeIsPreset.setter
    def CustomImageSizeIsPreset(self, value: System.Void): ...
    @overload
    def SetCurrentRenderer(self, g: System.Guid) -> None: ...
    @overload
    def SetGroundPlaneOnInViewDisplayMode(self, view: Display.RhinoView, bOn: bool) -> None: ...
    @overload
    def SetRenderSettings(self, renderSettings: Render.RenderSettings) -> None: ...
    @overload
    def ViewSupportsShading(self, view: Display.RhinoView) -> bool: ...

class RdkSelectionNavigator(object):
    """    """
    def __init__(self, pRhinoSettings: System.IntPtr): ...
    @overload
    def Add(self, selectedContentArray: Render.RenderContentCollection) -> None: ...
    @overload
    def CanGoBackwards() -> bool: ...
    @overload
    def CanGoForwards() -> bool: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Dispose() -> None: ...
    @property
    def CppPointer(self) -> System.IntPtr: ...
    @overload
    def GoBackwards() -> (bool, Render.RenderContentCollection): ...
    @overload
    def GoForwards() -> (bool, Render.RenderContentCollection): ...

class ContentFactories(object):
    """    """
    def __init__(self, pRdkContentFactories: System.IntPtr): ...
    @overload
    def Dispose() -> None: ...
    @overload
    def FindFactory(self, uuid: System.Guid) -> ContentFactory: ...
    @overload
    def FirstFactory() -> ContentFactory: ...
    @property
    def CppPointer(self) -> System.IntPtr: ...
    @overload
    def NextFactory() -> ContentFactory: ...

class ContentFactory(object):
    """    """
    def __init__(self, pRdkContentFactory: System.IntPtr): ...
    @overload
    def ContentTypeId() -> System.Guid: ...
    @overload
    def Dispose() -> None: ...
    @property
    def CppPointer(self) -> System.IntPtr: ...
    @overload
    def Kind() -> Render.RenderContentKind: ...
    @overload
    def NewContent() -> Render.RenderContent: ...

class RdkEdit(object):
    """    """
    def __init__(self, pRdkEdit: System.IntPtr): ...
    @overload
    def Dispose() -> None: ...
    @overload
    def Execute(self, collection: Render.RenderContentCollection) -> bool: ...
    @property
    def CppPointer(self) -> System.IntPtr: ...

# endregion
