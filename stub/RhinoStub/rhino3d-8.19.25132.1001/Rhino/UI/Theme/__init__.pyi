"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["ListThemeElement", "ListThemeState", "ButtonThemeElement", "ButtonThemeState", "CheckedThemeElement", "CheckedThemeState", "EntryThemeElement", "EntryThemeState", "LinkThemeElement", "LinkThemeState", "ScrollbarThemeElement", "ScrollbarThemeState", "ThemeBase", "TextThemeElement", "ThemeElementBase", "ThemeElement", "ThemeStateBase", "ThemeState", "IThemeEntry", "FrameThemeZone", "ContentThemeZone", "ThemeZone"]
# endregion

# region: Imports
from Eto import Drawing
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
# endregion

# region: Rhino.UI, Version=8.19.25132.1001

class ListThemeElement(CheckedThemeElement):
    """    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Focus(self) -> ListThemeState: ...
    @property
    def FocusHover(self) -> ListThemeState: ...

class ListThemeState(CheckedThemeState):
    """    """
    def __init__(self): ...

class ButtonThemeElement(CheckedThemeElement):
    """    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Default(self) -> ButtonThemeState: ...
    @property
    def DefaultHover(self) -> ButtonThemeState: ...
    @property
    def DefaultPressed(self) -> ButtonThemeState: ...
    @property
    def Unchecked(self) -> ButtonThemeState: ...
    @property
    def UncheckedPressed(self) -> ButtonThemeState: ...
    @property
    def UncheckedtHover(self) -> ButtonThemeState: ...

class ButtonThemeState(CheckedThemeState):
    """    """
    def __init__(self): ...

class CheckedThemeElement(ThemeElement):
    """    CheckedThemeElement[T]
    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Checked(self) -> T: ...
    @property
    def CheckedHover(self) -> T: ...
    @property
    def CheckedPressed(self) -> T: ...

class CheckedThemeState(ThemeState):
    """    """
    def __init__(self): ...

class EntryThemeElement(ThemeElement):
    """    """
    def __init__(self): ...

class EntryThemeState(ThemeState):
    """    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def PlaceholderText(self) -> Drawing.Color: ...

class LinkThemeElement(ThemeElement):
    """    """
    def __init__(self): ...

class LinkThemeState(ThemeState):
    """    """
    def __init__(self): ...

class ScrollbarThemeElement(ThemeElement):
    """    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def ArrowSize(self) -> float: ...
    @property
    def Radius(self) -> float: ...
    @property
    def Size(self) -> float: ...

class ScrollbarThemeState(ThemeStateBase):
    """    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Background(self) -> Drawing.Color: ...
    @property
    def Border(self) -> Drawing.Color: ...
    @property
    def Glyph(self) -> Drawing.Color: ...
    @property
    def Thumb(self) -> Drawing.Color: ...

class ThemeBase(object):
    """    """
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Id(self) -> str: ...

class TextThemeElement(ThemeElementBase):
    """    """
    def __init__(self): ...
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Disabled(self) -> Drawing.Color: ...
    @property
    def Enabled(self) -> Drawing.Color: ...
    @property
    def Highlight(self) -> Drawing.Color: ...
    @property
    def HighlightHover(self) -> Drawing.Color: ...

class ThemeElementBase(ThemeBase):
    """    """

class ThemeElement(ThemeElementBase):
    """    ThemeElement[T]
    """
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Disabled(self) -> T: ...
    @property
    def Enabled(self) -> T: ...
    @property
    def EnabledHover(self) -> T: ...
    @property
    def EnabledPressed(self) -> T: ...

class ThemeStateBase(ThemeBase):
    """    """

class ThemeState(ThemeStateBase):
    """    """
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Background(self) -> Drawing.Color: ...
    @property
    def Border(self) -> Drawing.Color: ...
    @property
    def Text(self) -> Drawing.Color: ...

class IThemeEntry:
    """    """
    @property
    def Id(self) -> str: ...
    @property
    def Value(self) -> object: ...

class FrameThemeZone(ThemeZone):
    """    """
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Edge(self) -> Drawing.Color: ...

class ContentThemeZone(ThemeZone):
    """    """
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def MessageBoxBackground(self) -> Drawing.Color: ...

class ThemeZone(ThemeBase):
    """    """
    @overload
    def Enumerate() -> Generic.IEnumerable: ...
    @property
    def Background(self) -> Drawing.Color: ...
    @property
    def Button(self) -> ButtonThemeElement: ...
    @property
    def Divider(self) -> Drawing.Color: ...
    @property
    def Entry(self) -> EntryThemeElement: ...
    @property
    def GripperDot(self) -> Drawing.Color: ...
    @property
    def Highlight(self) -> Drawing.Color: ...
    @property
    def HighlightHover(self) -> Drawing.Color: ...
    @property
    def Link(self) -> LinkThemeElement: ...
    @property
    def List(self) -> ListThemeElement: ...
    @property
    def Scrollbar(self) -> ScrollbarThemeElement: ...
    @property
    def Tab(self) -> ButtonThemeElement: ...
    @property
    def Text(self) -> TextThemeElement: ...

# endregion
