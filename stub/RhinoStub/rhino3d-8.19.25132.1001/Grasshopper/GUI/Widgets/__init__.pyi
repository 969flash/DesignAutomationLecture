"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["GH_AlignWidget", "IGH_Widget", "GH_Widget", "GH_CanvasWidget_FixedObject", "GH_CompassWidget", "GH_MarkovWidgetDock", "GH_MarkovWidget", "GH_MessageWidget", "GH_ProfilerWidget", "WidgetVisibleChangedEventHandler", "WidgetDrawModeChangedEventHandler", "IconLimitChangedEventHandler", "DockCornerChangedEventHandler", "WidgetLevelChangedEventHandler", "ShowDurationChangedEventHandler", "ProfilerThresholdChangedEventHandler"]
# endregion

# region: Imports
from Grasshopper import GUI
from Grasshopper.GUI import Canvas
from System import Drawing
from System.Runtime import CompilerServices
from System.Windows import Forms
from typing import overload
import enum
import System
# endregion

# region: Grasshopper, Version=8.19.25132.1001

class GH_AlignWidget(GH_Widget):
    """    """
    def __init__(self): ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def Name(self) -> str: ...
    @property
    def SharedVisible(self) -> bool: ...
    @property
    def TooltipText(self) -> str: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def Render(self, canvas: Canvas.GH_Canvas) -> None: ...
    @overload
    def RespondToMouseDown(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseMove(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @SharedVisible.setter
    def SharedVisible(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...
    @property
    def WidgetVisibleChanged(self): ...

class IGH_Widget:
    """    """
    @overload
    def AppendToMenu(self, menu: Forms.ToolStripDropDownMenu) -> None: ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def Name(self) -> str: ...
    @property
    def Owner(self) -> Canvas.GH_Canvas: ...
    @property
    def TooltipText(self) -> str: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def Render(self, Canvas: Canvas.GH_Canvas) -> None: ...
    @Owner.setter
    def Owner(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...

class GH_Widget(object):
    """    """
    @overload
    def AppendToMenu(self, menu: Forms.ToolStripDropDownMenu) -> None: ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def Name(self) -> str: ...
    @property
    def Owner(self) -> Canvas.GH_Canvas: ...
    @property
    def TooltipEnabled(self) -> bool: ...
    @property
    def TooltipText(self) -> str: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def IsTooltipRegion(self, canvas_coordinate: Drawing.PointF) -> bool: ...
    @overload
    def Render(self, Canvas: Canvas.GH_Canvas) -> None: ...
    @overload
    def RespondToKeyDown(self, sender: Canvas.GH_Canvas, e: Forms.KeyEventArgs) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToKeyUp(self, sender: Canvas.GH_Canvas, e: Forms.KeyEventArgs) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseDoubleClick(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseDown(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseMove(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseUp(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @Owner.setter
    def Owner(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...
    @overload
    def SetupTooltip(self, canvasPoint: Drawing.PointF, e: GUI.GH_TooltipDisplayEventArgs) -> None: ...

class GH_CanvasWidget_FixedObject(GH_Widget):
    """    """
    @overload
    def CanvasLocation(self, vp: Canvas.GH_Viewport) -> Drawing.PointF: ...
    @overload
    def ControlLocation(self, vp: Canvas.GH_Viewport) -> Drawing.Point: ...
    @property
    def Padding(self) -> int: ...
    @property
    def Ratio(self) -> Drawing.SizeF: ...
    @property
    def Size(self) -> Drawing.Size: ...
    @overload
    def Render(self, canvas: Canvas.GH_Canvas) -> None: ...
    @Ratio.setter
    def Ratio(self, value: System.Void): ...

class GH_CompassWidget(GH_CanvasWidget_FixedObject):
    """    """
    def __init__(self): ...
    @overload
    def AppendToMenu(self, menu: Forms.ToolStripDropDownMenu) -> None: ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def DrawObjects(self) -> bool: ...
    @property
    def DrawSelectionOnly(self) -> bool: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def Name(self) -> str: ...
    @property
    def Padding(self) -> int: ...
    @property
    def Radius(self) -> int: ...
    @property
    def Ratio(self) -> Drawing.SizeF: ...
    @property
    def SharedVisible(self) -> bool: ...
    @property
    def Size(self) -> Drawing.Size: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def RespondToKeyDown(self, sender: Canvas.GH_Canvas, e: Forms.KeyEventArgs) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseDown(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseMove(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseUp(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @DrawObjects.setter
    def DrawObjects(self, value: System.Void): ...
    @DrawSelectionOnly.setter
    def DrawSelectionOnly(self, value: System.Void): ...
    @Ratio.setter
    def Ratio(self, value: System.Void): ...
    @SharedVisible.setter
    def SharedVisible(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...
    @property
    def WidgetVisibleChanged(self): ...
    @property
    def WidgetDrawModeChanged(self): ...

class GH_MarkovWidgetDock(enum.Enum):
    TopLeft = 0
    BottomLeft = 1
    TopRight = 2
    BottomRight = 3

class GH_MarkovWidget(GH_Widget):
    """Markov chain widget.

    """
    def __init__(self): ...
    @overload
    def AppendToMenu(self, menu: Forms.ToolStripDropDownMenu) -> None: ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def DockCorner(self) -> GH_MarkovWidgetDock: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def IconLimit(self) -> int: ...
    @property
    def Name(self) -> str: ...
    @property
    def SharedVisible(self) -> bool: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def Render(self, Canvas: Canvas.GH_Canvas) -> None: ...
    @overload
    def RespondToMouseDown(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseMove(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @overload
    def RespondToMouseUp(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @DockCorner.setter
    def DockCorner(self, value: System.Void): ...
    @IconLimit.setter
    def IconLimit(self, value: System.Void): ...
    @SharedVisible.setter
    def SharedVisible(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...
    @overload
    def SetupTooltip(self, canvasPoint: Drawing.PointF, e: GUI.GH_TooltipDisplayEventArgs) -> None: ...
    @property
    def IconLimitChanged(self): ...
    @property
    def DockCornerChanged(self): ...
    @property
    def WidgetVisibleChanged(self): ...

class GH_MessageWidget(GH_Widget):
    """    """
    def __init__(self): ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def Name(self) -> str: ...
    @property
    def SharedVisible(self) -> bool: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def Render(self, canvas: Canvas.GH_Canvas) -> None: ...
    @overload
    def RespondToMouseDown(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @SharedVisible.setter
    def SharedVisible(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...
    @overload
    def SetupTooltip(self, canvasPoint: Drawing.PointF, e: GUI.GH_TooltipDisplayEventArgs) -> None: ...
    @property
    def WidgetVisibleChanged(self): ...
    @property
    def WidgetLevelChanged(self): ...

class GH_ProfilerWidget(GH_Widget):
    """    """
    def __init__(self): ...
    @overload
    def AppendToMenu(self, menu: Forms.ToolStripDropDownMenu) -> None: ...
    @overload
    def Contains(self, pt_control: Drawing.Point, pt_canvas: Drawing.PointF) -> bool: ...
    @property
    def Description(self) -> str: ...
    @property
    def Icon_24x24(self) -> Drawing.Bitmap: ...
    @property
    def Name(self) -> str: ...
    @property
    def SharedVisible(self) -> bool: ...
    @property
    def ShowDuration(self) -> bool: ...
    @property
    def Threshold(self) -> int: ...
    @property
    def TooltipText(self) -> str: ...
    @property
    def Visible(self) -> bool: ...
    @overload
    def Render(self, Canvas: Canvas.GH_Canvas) -> None: ...
    @overload
    def RespondToMouseDoubleClick(self, sender: Canvas.GH_Canvas, e: GUI.GH_CanvasMouseEvent) -> Canvas.GH_ObjectResponse: ...
    @SharedVisible.setter
    def SharedVisible(self, value: System.Void): ...
    @ShowDuration.setter
    def ShowDuration(self, value: System.Void): ...
    @Threshold.setter
    def Threshold(self, value: System.Void): ...
    @Visible.setter
    def Visible(self, value: System.Void): ...
    @property
    def ShowDurationChanged(self): ...
    @property
    def ProfilerThresholdChanged(self): ...
    @property
    def WidgetVisibleChanged(self): ...

class WidgetVisibleChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class WidgetVisibleChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class WidgetDrawModeChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class IconLimitChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class DockCornerChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class WidgetVisibleChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class WidgetVisibleChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class WidgetLevelChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class ShowDurationChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class ProfilerThresholdChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

class WidgetVisibleChangedEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke() -> None: ...

# endregion
