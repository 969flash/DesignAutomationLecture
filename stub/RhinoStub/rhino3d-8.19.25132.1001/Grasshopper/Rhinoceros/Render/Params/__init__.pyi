"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Param_ModelRenderEnvironment", "Param_ModelRenderMaterial", "Param_ModelRenderTexture", "Param_ObjectRender", "Param_ObjectRenderMaterial"]
# endregion

# region: Imports
from Grasshopper import Kernel
from Grasshopper.Rhinoceros import Params
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Grasshopper, Version=8.19.25132.1001

class Param_ModelRenderEnvironment(Params.ModelContentParam):
    """    """
    def __init__(self): ...
    @property
    def ComponentGuid(self) -> System.Guid: ...
    @property
    def Exposure(self) -> Kernel.GH_Exposure: ...
    @property
    def ObjectChanged(self): ...
    @property
    def AttributesChanged(self): ...
    @property
    def SolutionExpired(self): ...
    @property
    def DisplayExpired(self): ...
    @property
    def PreviewExpired(self): ...
    @property
    def PingDocument(self): ...

class Param_ModelRenderMaterial(Params.ModelContentParam):
    """    """
    def __init__(self): ...
    @property
    def ComponentGuid(self) -> System.Guid: ...
    @property
    def Exposure(self) -> Kernel.GH_Exposure: ...
    @property
    def ObjectChanged(self): ...
    @property
    def AttributesChanged(self): ...
    @property
    def SolutionExpired(self): ...
    @property
    def DisplayExpired(self): ...
    @property
    def PreviewExpired(self): ...
    @property
    def PingDocument(self): ...

class Param_ModelRenderTexture(Params.ModelContentParam):
    """    """
    def __init__(self): ...
    @property
    def ComponentGuid(self) -> System.Guid: ...
    @property
    def Exposure(self) -> Kernel.GH_Exposure: ...
    @property
    def ObjectChanged(self): ...
    @property
    def AttributesChanged(self): ...
    @property
    def SolutionExpired(self): ...
    @property
    def DisplayExpired(self): ...
    @property
    def PreviewExpired(self): ...
    @property
    def PingDocument(self): ...

class Param_ObjectRender(Params.ModelDataParam):
    """    """
    def __init__(self): ...
    @property
    def ComponentGuid(self) -> System.Guid: ...
    @property
    def Exposure(self) -> Kernel.GH_Exposure: ...
    @property
    def ObjectChanged(self): ...
    @property
    def AttributesChanged(self): ...
    @property
    def SolutionExpired(self): ...
    @property
    def DisplayExpired(self): ...
    @property
    def PreviewExpired(self): ...
    @property
    def PingDocument(self): ...

class Param_ObjectRenderMaterial(Kernel.GH_PersistentParam):
    """    """
    def __init__(self): ...
    @overload
    def ClearData() -> None: ...
    @property
    def ComponentGuid(self) -> System.Guid: ...
    @property
    def Exposure(self) -> Kernel.GH_Exposure: ...
    @overload
    def RegisterRemoteIDs(self, table: Kernel.GH_GuidTable) -> None: ...
    @property
    def ObjectChanged(self): ...
    @property
    def AttributesChanged(self): ...
    @property
    def SolutionExpired(self): ...
    @property
    def DisplayExpired(self): ...
    @property
    def PreviewExpired(self): ...
    @property
    def PingDocument(self): ...

# endregion
