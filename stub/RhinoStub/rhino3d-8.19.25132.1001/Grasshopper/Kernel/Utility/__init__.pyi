"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["GH_Point3dWrapperDelegate", "GH_Point3d_Wrapper", "GH_Point3d_Wrapper_TypeConverter", "GH_Vector3dWrapperDelegate", "GH_Vector3d_Wrapper", "GH_Vector3d_Wrapper_TypeConverter", "GH_IntervalWrapperDelegate", "GH_Interval_Wrapper", "GH_Interval_Wrapper_TypeConverter", "GH_PointRefUVWrapperDelegate", "GH_PointRefUV_Wrapper", "GH_PointRefUV_Wrapper_TypeConverter", "GH_PlaneModifier"]
# endregion

# region: Imports
from Grasshopper.Kernel import Types
from Rhino import Geometry
from System import ComponentModel
from System import Globalization
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Grasshopper, Version=8.19.25132.1001

class GH_Point3dWrapperDelegate(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: GH_Point3d_Wrapper, point: Geometry.Point3d, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: GH_Point3d_Wrapper, point: Geometry.Point3d) -> None: ...

class GH_Point3d_Wrapper(object):
    """    """
    def __init__(self, pt: Geometry.Point3d, wrapperdelegate: GH_Point3dWrapperDelegate): ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
    @overload
    def InternalPoint() -> Geometry.Point3d: ...
    @X.setter
    def X(self, value: System.Void): ...
    @Y.setter
    def Y(self, value: System.Void): ...
    @Z.setter
    def Z(self, value: System.Void): ...

class GH_Point3d_Wrapper_TypeConverter(ComponentModel.ExpandableObjectConverter):
    """    """
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ComponentModel.ITypeDescriptorContext, sourceType: System.Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ComponentModel.ITypeDescriptorContext, destinationType: System.Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ComponentModel.ITypeDescriptorContext, culture: Globalization.CultureInfo, value: object, destinationType: System.Type) -> object: ...

class GH_Vector3dWrapperDelegate(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: GH_Vector3d_Wrapper, vector: Geometry.Vector3d, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: GH_Vector3d_Wrapper, vector: Geometry.Vector3d) -> None: ...

class GH_Vector3d_Wrapper(object):
    """    """
    def __init__(self, vec: Geometry.Vector3d, wrapperdelegate: GH_Vector3dWrapperDelegate): ...
    @property
    def Length(self) -> str: ...
    @property
    def Tiny(self) -> str: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
    @overload
    def InternalVector() -> Geometry.Vector3d: ...
    @X.setter
    def X(self, value: System.Void): ...
    @Y.setter
    def Y(self, value: System.Void): ...
    @Z.setter
    def Z(self, value: System.Void): ...

class GH_Vector3d_Wrapper_TypeConverter(ComponentModel.ExpandableObjectConverter):
    """    """
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ComponentModel.ITypeDescriptorContext, sourceType: System.Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ComponentModel.ITypeDescriptorContext, destinationType: System.Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ComponentModel.ITypeDescriptorContext, culture: Globalization.CultureInfo, value: object, destinationType: System.Type) -> object: ...

class GH_IntervalWrapperDelegate(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: GH_Interval_Wrapper, interval: Geometry.Interval, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: GH_Interval_Wrapper, interval: Geometry.Interval) -> None: ...

class GH_Interval_Wrapper(object):
    """    """
    def __init__(self, interval: Geometry.Interval, wrapperdelegate: GH_IntervalWrapperDelegate): ...
    @property
    def A(self) -> float: ...
    @property
    def B(self) -> float: ...
    @property
    def Increasing(self) -> str: ...
    @property
    def Length(self) -> str: ...
    @overload
    def InternalInterval() -> Geometry.Interval: ...
    @A.setter
    def A(self, value: System.Void): ...
    @B.setter
    def B(self, value: System.Void): ...

class GH_Interval_Wrapper_TypeConverter(ComponentModel.ExpandableObjectConverter):
    """    """
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ComponentModel.ITypeDescriptorContext, sourceType: System.Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ComponentModel.ITypeDescriptorContext, destinationType: System.Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ComponentModel.ITypeDescriptorContext, culture: Globalization.CultureInfo, value: object, destinationType: System.Type) -> object: ...

class GH_PointRefUVWrapperDelegate(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: GH_PointRefUV_Wrapper, ref: Types.GH_PointRefData, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: GH_PointRefUV_Wrapper, ref: Types.GH_PointRefData) -> None: ...

class GH_PointRefUV_Wrapper(object):
    """    """
    def __init__(self, ref: Types.GH_PointRefData, wrapperdelegate: GH_PointRefUVWrapperDelegate): ...
    @property
    def U(self) -> float: ...
    @property
    def V(self) -> float: ...
    @overload
    def InternalRefence() -> Types.GH_PointRefData: ...
    @U.setter
    def U(self, value: System.Void): ...
    @V.setter
    def V(self, value: System.Void): ...

class GH_PointRefUV_Wrapper_TypeConverter(ComponentModel.ExpandableObjectConverter):
    """    """
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ComponentModel.ITypeDescriptorContext, sourceType: System.Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ComponentModel.ITypeDescriptorContext, destinationType: System.Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ComponentModel.ITypeDescriptorContext, culture: Globalization.CultureInfo, value: object, destinationType: System.Type) -> object: ...

class GH_PlaneModifier(object):
    """    """
    @overload
    @staticmethod
    def Set_X(P: Geometry.Plane, x_axis: Geometry.Vector3d) -> Geometry.Plane: ...
    @overload
    @staticmethod
    def Set_Y(P: Geometry.Plane, y_axis: Geometry.Vector3d) -> Geometry.Plane: ...
    @overload
    @staticmethod
    def Set_Z(P: Geometry.Plane, z_axis: Geometry.Vector3d) -> Geometry.Plane: ...

# endregion
