"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["TwistSpaceMorph", "BendSpaceMorph", "TaperSpaceMorph", "MaelstromSpaceMorph", "StretchSpaceMorph", "SporphSpaceMorph", "FlowSpaceMorph", "SplopSpaceMorph"]
# endregion

# region: Imports
from Rhino import Geometry
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: RhinoCommon, Version=8.19.25132.1001

class TwistSpaceMorph(Geometry.SpaceMorph):
    """Deforms objects by rotating them around an axis.

    """
    def __init__(self): ...
    @overload
    def Dispose() -> None: ...
    @property
    def InfiniteTwist(self) -> bool: ...
    @property
    def TwistAngleRadians(self) -> float: ...
    @property
    def TwistAxis(self) -> Geometry.Line: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...
    @InfiniteTwist.setter
    def InfiniteTwist(self, value: System.Void): ...
    @TwistAngleRadians.setter
    def TwistAngleRadians(self, value: System.Void): ...
    @TwistAxis.setter
    def TwistAxis(self, value: System.Void): ...

class BendSpaceMorph(Geometry.SpaceMorph):
    """Deforms objects by bending along a spine arc.

    """
    @overload
    def __init__(self, start: Geometry.Point3d, end: Geometry.Point3d, point: Geometry.Point3d, straight: bool, symmetric: bool): ...
    @overload
    def __init__(self, start: Geometry.Point3d, end: Geometry.Point3d, point: Geometry.Point3d, angle: float, straight: bool, symmetric: bool): ...
    @overload
    def Dispose() -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...

class TaperSpaceMorph(Geometry.SpaceMorph):
    """Deforms objects toward or away from a specified axis.

    """
    def __init__(self, start: Geometry.Point3d, end: Geometry.Point3d, startRadius: float, endRadius: float, bFlat: bool, infiniteTaper: bool): ...
    @overload
    def Dispose() -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...

class MaelstromSpaceMorph(Geometry.SpaceMorph):
    """Deforms objects in a spiral as if they were caught in a whirlpool.

    """
    def __init__(self, plane: Geometry.Plane, radius0: float, radius1: float, angle: float): ...
    @overload
    def Dispose() -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...

class StretchSpaceMorph(Geometry.SpaceMorph):
    """Deforms objects toward or away from a specified axis.

    """
    @overload
    def __init__(self, start: Geometry.Point3d, end: Geometry.Point3d, point: Geometry.Point3d): ...
    @overload
    def __init__(self, start: Geometry.Point3d, end: Geometry.Point3d, length: float): ...
    @overload
    def Dispose() -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...

class SporphSpaceMorph(Geometry.SpaceMorph):
    """Deforms an object from a source surface to a target surface.

    """
    @overload
    def __init__(self, surface0: Geometry.Surface, surface1: Geometry.Surface): ...
    @overload
    def __init__(self, surface0: Geometry.Surface, surface1: Geometry.Surface, surface0Param: Geometry.Point2d, surface1Param: Geometry.Point2d): ...
    @overload
    def Dispose() -> None: ...
    @property
    def ConstrainNormal(self) -> Geometry.Vector3d: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...
    @ConstrainNormal.setter
    def ConstrainNormal(self, value: System.Void): ...

class FlowSpaceMorph(Geometry.SpaceMorph):
    """Re-aligns objects from a base curve to a target curve.

    """
    @overload
    def __init__(self, curve0: Geometry.Curve, curve1: Geometry.Curve, preventStretching: bool): ...
    @overload
    def __init__(self, curve0: Geometry.Curve, curve1: Geometry.Curve, reverseCurve0: bool, reverseCurve1: bool, preventStretching: bool): ...
    @overload
    def Dispose() -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...

class SplopSpaceMorph(Geometry.SpaceMorph):
    """Rotates, scales, and wraps objects on a surface.

    """
    @overload
    def __init__(self, plane: Geometry.Plane, surface: Geometry.Surface, surfaceParam: Geometry.Point2d): ...
    @overload
    def __init__(self, plane: Geometry.Plane, surface: Geometry.Surface, surfaceParam: Geometry.Point2d, scale: float): ...
    @overload
    def __init__(self, plane: Geometry.Plane, surface: Geometry.Surface, surfaceParam: Geometry.Point2d, scale: float, angle: float): ...
    @overload
    def Dispose() -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @overload
    def MorphPoint(self, point: Geometry.Point3d) -> Geometry.Point3d: ...

# endregion
