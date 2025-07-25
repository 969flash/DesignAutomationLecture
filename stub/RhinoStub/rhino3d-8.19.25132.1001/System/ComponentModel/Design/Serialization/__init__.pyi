"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["InstanceDescriptor", "ComponentSerializationService", "ContextStack", "DefaultSerializationProviderAttribute", "DesignerLoader", "SerializationStore", "IDesignerLoaderHost", "IDesignerLoaderHost2", "IDesignerLoaderService", "IDesignerSerializationManager", "IDesignerSerializationProvider", "IDesignerSerializationService", "INameCreationService", "MemberRelationshipService", "MemberRelationship", "ResolveNameEventHandler", "ResolveNameEventArgs"]
# endregion

# region: Imports
from System import Collections
from System import ComponentModel
from System import IO
from System import Reflection
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Exports
__all__ = ["DesignerSerializerAttribute"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: System.ComponentModel.Primitives, Version=7.0.0.0

class DesignerSerializerAttribute(System.Attribute):
    """    """
    @overload
    def __init__(self, serializerType: System.Type, baseSerializerType: System.Type): ...
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerType: System.Type): ...
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerTypeName: str): ...
    @property
    def SerializerBaseTypeName(self) -> str: ...
    @property
    def SerializerTypeName(self) -> str: ...
    @property
    def TypeId(self) -> object: ...

# endregion

# region: System.ComponentModel.TypeConverter, Version=7.0.0.0

class InstanceDescriptor(object):
    """    """
    @overload
    def __init__(self, member: Reflection.MemberInfo, arguments: Collections.ICollection): ...
    @overload
    def __init__(self, member: Reflection.MemberInfo, arguments: Collections.ICollection, isComplete: bool): ...
    @property
    def Arguments(self) -> Collections.ICollection: ...
    @property
    def IsComplete(self) -> bool: ...
    @property
    def MemberInfo(self) -> Reflection.MemberInfo: ...
    @overload
    def Invoke() -> object: ...

class ComponentSerializationService(object):
    """    """
    @overload
    def CreateStore() -> SerializationStore: ...
    @overload
    def Deserialize(self, store: SerializationStore) -> Collections.ICollection: ...
    @overload
    def Deserialize(self, store: SerializationStore, container: ComponentModel.IContainer) -> Collections.ICollection: ...
    @overload
    def DeserializeTo(self, store: SerializationStore, container: ComponentModel.IContainer) -> None: ...
    @overload
    def DeserializeTo(self, store: SerializationStore, container: ComponentModel.IContainer, validateRecycledTypes: bool) -> None: ...
    @overload
    def DeserializeTo(self, store: SerializationStore, container: ComponentModel.IContainer, validateRecycledTypes: bool, applyDefaults: bool) -> None: ...
    @overload
    def LoadStore(self, stream: IO.Stream) -> SerializationStore: ...
    @overload
    def Serialize(self, store: SerializationStore, value: object) -> None: ...
    @overload
    def SerializeAbsolute(self, store: SerializationStore, value: object) -> None: ...
    @overload
    def SerializeMember(self, store: SerializationStore, owningObject: object, member: ComponentModel.MemberDescriptor) -> None: ...
    @overload
    def SerializeMemberAbsolute(self, store: SerializationStore, owningObject: object, member: ComponentModel.MemberDescriptor) -> None: ...

class ContextStack(object):
    """    """
    def __init__(self): ...
    @overload
    def Append(self, context: object) -> None: ...
    @property
    def Current(self) -> object: ...
    @property
    def Item(self) -> object: ...
    @property
    def Item(self) -> object: ...
    @overload
    def Pop() -> object: ...
    @overload
    def Push(self, context: object) -> None: ...

class DefaultSerializationProviderAttribute(System.Attribute):
    """    """
    @overload
    def __init__(self, providerType: System.Type): ...
    @overload
    def __init__(self, providerTypeName: str): ...
    @property
    def ProviderTypeName(self) -> str: ...

class DesignerLoader(object):
    """    """
    @overload
    def BeginLoad(self, host: IDesignerLoaderHost) -> None: ...
    @overload
    def Dispose() -> None: ...
    @overload
    def Flush() -> None: ...
    @property
    def Loading(self) -> bool: ...

class SerializationStore(object):
    """    """
    @overload
    def Close() -> None: ...
    @property
    def Errors(self) -> Collections.ICollection: ...
    @overload
    def Save(self, stream: IO.Stream) -> None: ...

class IDesignerLoaderHost:
    """    """
    @overload
    def EndLoad(self, baseClassName: str, successful: bool, errorCollection: Collections.ICollection) -> None: ...
    @overload
    def Reload() -> None: ...

class IDesignerLoaderHost2:
    """    """
    @property
    def CanReloadWithErrors(self) -> bool: ...
    @property
    def IgnoreErrorsDuringReload(self) -> bool: ...
    @CanReloadWithErrors.setter
    def CanReloadWithErrors(self, value: System.Void): ...
    @IgnoreErrorsDuringReload.setter
    def IgnoreErrorsDuringReload(self, value: System.Void): ...

class IDesignerLoaderService:
    """    """
    @overload
    def AddLoadDependency() -> None: ...
    @overload
    def DependentLoadComplete(self, successful: bool, errorCollection: Collections.ICollection) -> None: ...
    @overload
    def Reload() -> bool: ...

class IDesignerSerializationManager:
    """    """
    @overload
    def AddSerializationProvider(self, provider: IDesignerSerializationProvider) -> None: ...
    @overload
    def CreateInstance(self, type_: System.Type, arguments: Collections.ICollection, name: str, addToContainer: bool) -> object: ...
    @property
    def Context(self) -> ContextStack: ...
    @property
    def Properties(self) -> ComponentModel.PropertyDescriptorCollection: ...
    @overload
    def GetInstance(self, name: str) -> object: ...
    @overload
    def GetName(self, value: object) -> str: ...
    @overload
    def GetSerializer(self, objectType: System.Type, serializerType: System.Type) -> object: ...
    @overload
    def GetType(self, typeName: str) -> System.Type: ...
    @overload
    def RemoveSerializationProvider(self, provider: IDesignerSerializationProvider) -> None: ...
    @overload
    def ReportError(self, errorInformation: object) -> None: ...
    @overload
    def SetName(self, instance: object, name: str) -> None: ...
    @property
    def ResolveName(self): ...
    @property
    def SerializationComplete(self): ...

class IDesignerSerializationProvider:
    """    """
    @overload
    def GetSerializer(self, manager: IDesignerSerializationManager, currentSerializer: object, objectType: System.Type, serializerType: System.Type) -> object: ...

class IDesignerSerializationService:
    """    """
    @overload
    def Deserialize(self, serializationData: object) -> Collections.ICollection: ...
    @overload
    def Serialize(self, objects: Collections.ICollection) -> object: ...

class INameCreationService:
    """    """
    @overload
    def CreateName(self, container: ComponentModel.IContainer, dataType: System.Type) -> str: ...
    @overload
    def IsValidName(self, name: str) -> bool: ...
    @overload
    def ValidateName(self, name: str) -> None: ...

class MemberRelationshipService(object):
    """    """
    @property
    def Item(self) -> MemberRelationship: ...
    @property
    def Item(self) -> MemberRelationship: ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def SupportsRelationship(self, source: MemberRelationship, relationship: MemberRelationship) -> bool: ...

class MemberRelationship(System.ValueType):
    """    """
    def __init__(self, owner: object, member: ComponentModel.MemberDescriptor): ...
    @property
    def Empty(self) -> MemberRelationship: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def Equals(self, other: MemberRelationship) -> bool: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Member(self) -> ComponentModel.MemberDescriptor: ...
    @property
    def Owner(self) -> object: ...
    @overload
    def GetHashCode() -> int: ...

class ResolveNameEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: ResolveNameEventArgs, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: ResolveNameEventArgs) -> None: ...

class ResolveNameEventArgs(System.EventArgs):
    """    """
    def __init__(self, name: str): ...
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> object: ...
    @Value.setter
    def Value(self, value: System.Void): ...

# endregion
