"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["ChannelDispatcher", "ChannelDispatcherBase", "ClientOperationCompatBase", "ClientOperation", "ClientRuntimeCompatBase", "ClientRuntime", "DispatchOperation", "DispatchRuntime", "EndpointDispatcher", "FaultContractInfo", "FaultFormatter", "IChannelInitializer", "IClientMessageFormatter", "IClientMessageInspector", "IClientOperationSelector", "IDispatchMessageInspector", "IErrorHandler", "IInstanceContextProvider", "IInstanceProvider", "IInteractiveChannelInitializer", "IMessageFilterTable", "InstanceBehavior", "IOperationInvoker", "IParameterInspector", "MessageFilter", "OperationInvokerBehavior", "SyncMethodInvoker", "TaskMethodInvoker", "OperationFault"]
# endregion

# region: Imports
from System import Reflection
from System import ServiceModel
from System import Threading
from System.Collections import Generic
from System.Collections import ObjectModel
from System.Runtime import CompilerServices
from System.Runtime import Serialization
from System.ServiceModel import Channels
from typing import overload
import System
# endregion

# region: System.Private.ServiceModel, Version=4.9.0.0

class ChannelDispatcher(ChannelDispatcherBase):
    """    """
    @overload
    def CloseInput() -> None: ...
    @property
    def Endpoints(self) -> Generic.SynchronizedCollection: ...
    @property
    def ErrorHandlers(self) -> ObjectModel.Collection: ...
    @property
    def IncludeExceptionDetailInFaults(self) -> bool: ...
    @property
    def Listener(self) -> Channels.IChannelListener: ...
    @property
    def ManualAddressing(self) -> bool: ...
    @property
    def MaxPendingReceives(self) -> int: ...
    @property
    def MaxTransactedBatchSize(self) -> int: ...
    @property
    def MessageVersion(self) -> Channels.MessageVersion: ...
    @property
    def ReceiveContextEnabled(self) -> bool: ...
    @property
    def ReceiveSynchronously(self) -> bool: ...
    @property
    def SendAsynchronously(self) -> bool: ...
    @IncludeExceptionDetailInFaults.setter
    def IncludeExceptionDetailInFaults(self, value: System.Void): ...
    @ManualAddressing.setter
    def ManualAddressing(self, value: System.Void): ...
    @MaxPendingReceives.setter
    def MaxPendingReceives(self, value: System.Void): ...
    @MaxTransactedBatchSize.setter
    def MaxTransactedBatchSize(self, value: System.Void): ...
    @MessageVersion.setter
    def MessageVersion(self, value: System.Void): ...
    @ReceiveContextEnabled.setter
    def ReceiveContextEnabled(self, value: System.Void): ...
    @ReceiveSynchronously.setter
    def ReceiveSynchronously(self, value: System.Void): ...
    @SendAsynchronously.setter
    def SendAsynchronously(self, value: System.Void): ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def Faulted(self): ...
    @property
    def Opened(self): ...
    @property
    def Opening(self): ...

class ChannelDispatcherBase(Channels.CommunicationObject):
    """    """
    @overload
    def CloseInput() -> None: ...
    @property
    def Listener(self) -> Channels.IChannelListener: ...
    @property
    def Closed(self): ...
    @property
    def Closing(self): ...
    @property
    def Faulted(self): ...
    @property
    def Opened(self): ...
    @property
    def Opening(self): ...

class ClientOperationCompatBase(object):
    """    """
    @property
    def ParameterInspectors(self) -> Generic.IList: ...

class ClientOperation(ClientOperationCompatBase):
    """    """
    @overload
    def __init__(self, parent: ClientRuntime, name: str, action: str): ...
    @overload
    def __init__(self, parent: ClientRuntime, name: str, action: str, replyAction: str): ...
    @property
    def Action(self) -> str: ...
    @property
    def BeginMethod(self) -> Reflection.MethodInfo: ...
    @property
    def ClientParameterInspectors(self) -> Generic.ICollection: ...
    @property
    def DeserializeReply(self) -> bool: ...
    @property
    def EndMethod(self) -> Reflection.MethodInfo: ...
    @property
    def FaultContractInfos(self) -> Generic.SynchronizedCollection: ...
    @property
    def Formatter(self) -> IClientMessageFormatter: ...
    @property
    def IsInitiating(self) -> bool: ...
    @property
    def IsOneWay(self) -> bool: ...
    @property
    def IsTerminating(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParameterInspectors(self) -> Generic.SynchronizedCollection: ...
    @property
    def Parent(self) -> ClientRuntime: ...
    @property
    def ReplyAction(self) -> str: ...
    @property
    def SerializeRequest(self) -> bool: ...
    @property
    def SyncMethod(self) -> Reflection.MethodInfo: ...
    @property
    def TaskMethod(self) -> Reflection.MethodInfo: ...
    @property
    def TaskTResult(self) -> System.Type: ...
    @BeginMethod.setter
    def BeginMethod(self, value: System.Void): ...
    @DeserializeReply.setter
    def DeserializeReply(self, value: System.Void): ...
    @EndMethod.setter
    def EndMethod(self, value: System.Void): ...
    @Formatter.setter
    def Formatter(self, value: System.Void): ...
    @IsInitiating.setter
    def IsInitiating(self, value: System.Void): ...
    @IsOneWay.setter
    def IsOneWay(self, value: System.Void): ...
    @IsTerminating.setter
    def IsTerminating(self, value: System.Void): ...
    @SerializeRequest.setter
    def SerializeRequest(self, value: System.Void): ...
    @SyncMethod.setter
    def SyncMethod(self, value: System.Void): ...
    @TaskMethod.setter
    def TaskMethod(self, value: System.Void): ...
    @TaskTResult.setter
    def TaskTResult(self, value: System.Void): ...

class ClientRuntimeCompatBase(object):
    """    """
    @property
    def MessageInspectors(self) -> Generic.IList: ...
    @property
    def Operations(self) -> ObjectModel.KeyedCollection: ...

class ClientRuntime(ClientRuntimeCompatBase):
    """    """
    @property
    def CallbackClientType(self) -> System.Type: ...
    @property
    def CallbackDispatchRuntime(self) -> DispatchRuntime: ...
    @property
    def ChannelInitializers(self) -> Generic.SynchronizedCollection: ...
    @property
    def ClientMessageInspectors(self) -> Generic.ICollection: ...
    @property
    def ClientOperations(self) -> Generic.ICollection: ...
    @property
    def ContractClientType(self) -> System.Type: ...
    @property
    def ContractName(self) -> str: ...
    @property
    def ContractNamespace(self) -> str: ...
    @property
    def DispatchRuntime(self) -> DispatchRuntime: ...
    @property
    def InteractiveChannelInitializers(self) -> Generic.SynchronizedCollection: ...
    @property
    def ManualAddressing(self) -> bool: ...
    @property
    def MaxFaultSize(self) -> int: ...
    @property
    def MessageInspectors(self) -> Generic.SynchronizedCollection: ...
    @property
    def MessageVersionNoneFaultsEnabled(self) -> bool: ...
    @property
    def Operations(self) -> Generic.SynchronizedKeyedCollection: ...
    @property
    def OperationSelector(self) -> IClientOperationSelector: ...
    @property
    def UnhandledClientOperation(self) -> ClientOperation: ...
    @property
    def ValidateMustUnderstand(self) -> bool: ...
    @property
    def Via(self) -> System.Uri: ...
    @CallbackClientType.setter
    def CallbackClientType(self, value: System.Void): ...
    @ContractClientType.setter
    def ContractClientType(self, value: System.Void): ...
    @ManualAddressing.setter
    def ManualAddressing(self, value: System.Void): ...
    @MaxFaultSize.setter
    def MaxFaultSize(self, value: System.Void): ...
    @MessageVersionNoneFaultsEnabled.setter
    def MessageVersionNoneFaultsEnabled(self, value: System.Void): ...
    @OperationSelector.setter
    def OperationSelector(self, value: System.Void): ...
    @ValidateMustUnderstand.setter
    def ValidateMustUnderstand(self, value: System.Void): ...
    @Via.setter
    def Via(self, value: System.Void): ...

class DispatchOperation(object):
    """    """
    @overload
    def __init__(self, parent: DispatchRuntime, name: str, action: str): ...
    @overload
    def __init__(self, parent: DispatchRuntime, name: str, action: str, replyAction: str): ...
    @property
    def Action(self) -> str: ...
    @property
    def AutoDisposeParameters(self) -> bool: ...
    @property
    def DeserializeRequest(self) -> bool: ...
    @property
    def FaultContractInfos(self) -> Generic.SynchronizedCollection: ...
    @property
    def Invoker(self) -> IOperationInvoker: ...
    @property
    def IsOneWay(self) -> bool: ...
    @property
    def IsTerminating(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParameterInspectors(self) -> Generic.SynchronizedCollection: ...
    @property
    def Parent(self) -> DispatchRuntime: ...
    @property
    def ReplyAction(self) -> str: ...
    @property
    def SerializeReply(self) -> bool: ...
    @AutoDisposeParameters.setter
    def AutoDisposeParameters(self, value: System.Void): ...
    @DeserializeRequest.setter
    def DeserializeRequest(self, value: System.Void): ...
    @Invoker.setter
    def Invoker(self, value: System.Void): ...
    @IsTerminating.setter
    def IsTerminating(self, value: System.Void): ...
    @SerializeReply.setter
    def SerializeReply(self, value: System.Void): ...

class DispatchRuntime(object):
    """    """
    @property
    def AutomaticInputSessionShutdown(self) -> bool: ...
    @property
    def CallbackClientRuntime(self) -> ClientRuntime: ...
    @property
    def ChannelDispatcher(self) -> ChannelDispatcher: ...
    @property
    def ConcurrencyMode(self) -> ServiceModel.ConcurrencyMode: ...
    @property
    def EndpointDispatcher(self) -> EndpointDispatcher: ...
    @property
    def EnsureOrderedDispatch(self) -> bool: ...
    @property
    def InstanceContextProvider(self) -> IInstanceContextProvider: ...
    @property
    def InstanceProvider(self) -> IInstanceProvider: ...
    @property
    def MessageInspectors(self) -> Generic.SynchronizedCollection: ...
    @property
    def Operations(self) -> Generic.SynchronizedKeyedCollection: ...
    @property
    def SynchronizationContext(self) -> Threading.SynchronizationContext: ...
    @property
    def Type(self) -> System.Type: ...
    @property
    def UnhandledDispatchOperation(self) -> DispatchOperation: ...
    @AutomaticInputSessionShutdown.setter
    def AutomaticInputSessionShutdown(self, value: System.Void): ...
    @ConcurrencyMode.setter
    def ConcurrencyMode(self, value: System.Void): ...
    @EnsureOrderedDispatch.setter
    def EnsureOrderedDispatch(self, value: System.Void): ...
    @InstanceContextProvider.setter
    def InstanceContextProvider(self, value: System.Void): ...
    @InstanceProvider.setter
    def InstanceProvider(self, value: System.Void): ...
    @SynchronizationContext.setter
    def SynchronizationContext(self, value: System.Void): ...
    @Type.setter
    def Type(self, value: System.Void): ...
    @UnhandledDispatchOperation.setter
    def UnhandledDispatchOperation(self, value: System.Void): ...

class EndpointDispatcher(object):
    """    """
    def __init__(self): ...
    @property
    def ChannelDispatcher(self) -> ChannelDispatcher: ...
    @property
    def ContractName(self) -> str: ...
    @property
    def ContractNamespace(self) -> str: ...
    @property
    def DispatchRuntime(self) -> DispatchRuntime: ...
    @property
    def EndpointAddress(self) -> ServiceModel.EndpointAddress: ...
    @property
    def FilterPriority(self) -> int: ...
    @FilterPriority.setter
    def FilterPriority(self, value: System.Void): ...

class FaultContractInfo(object):
    """    """
    def __init__(self, action: str, detail: System.Type): ...
    @property
    def Action(self) -> str: ...
    @property
    def Detail(self) -> System.Type: ...

class FaultFormatter(object):
    """    """
    @overload
    def Deserialize(self, messageFault: Channels.MessageFault, action: str) -> ServiceModel.FaultException: ...
    @overload
    def Serialize(self, faultException: ServiceModel.FaultException) -> (Channels.MessageFault, str): ...

class IChannelInitializer:
    """    """
    @overload
    def Initialize(self, channel: ServiceModel.IClientChannel) -> None: ...

class IClientMessageFormatter:
    """    """
    @overload
    def DeserializeReply(self, message: Channels.Message, parameters: System.System.Array[object]) -> object: ...
    @overload
    def SerializeRequest(self, messageVersion: Channels.MessageVersion, parameters: System.System.Array[object]) -> Channels.Message: ...

class IClientMessageInspector:
    """    """
    @overload
    def AfterReceiveReply(self, correlationState: object) -> (Channels.Message): ...
    @overload
    def BeforeSendRequest(self, channel: ServiceModel.IClientChannel) -> (object, Channels.Message): ...

class IClientOperationSelector:
    """    """
    @property
    def AreParametersRequiredForSelection(self) -> bool: ...
    @overload
    def SelectOperation(self, method: Reflection.MethodBase, parameters: System.System.Array[object]) -> str: ...

class IDispatchMessageInspector:
    """    """
    @overload
    def AfterReceiveRequest(self, channel: ServiceModel.IClientChannel, instanceContext: ServiceModel.InstanceContext) -> (object, Channels.Message): ...
    @overload
    def BeforeSendReply(self, correlationState: object) -> (Channels.Message): ...

class IErrorHandler:
    """    """
    @overload
    def HandleError(self, error: System.Exception) -> bool: ...
    @overload
    def ProvideFault(self, error: System.Exception, version: Channels.MessageVersion) -> (Channels.Message): ...

class IInstanceContextProvider:
    """    """
    @overload
    def GetExistingInstanceContext(self, message: Channels.Message, channel: ServiceModel.IContextChannel) -> ServiceModel.InstanceContext: ...

class IInstanceProvider:
    """    """
    @overload
    def GetInstance(self, instanceContext: ServiceModel.InstanceContext) -> object: ...
    @overload
    def GetInstance(self, instanceContext: ServiceModel.InstanceContext, message: Channels.Message) -> object: ...
    @overload
    def ReleaseInstance(self, instanceContext: ServiceModel.InstanceContext, instance: object) -> None: ...

class IInteractiveChannelInitializer:
    """    """
    @overload
    def BeginDisplayInitializationUI(self, channel: ServiceModel.IClientChannel, callback: System.AsyncCallback, state: object) -> System.IAsyncResult: ...
    @overload
    def EndDisplayInitializationUI(self, result: System.IAsyncResult) -> None: ...

class IMessageFilterTable:
    """    IMessageFilterTable[TFilterData]
    """
    @overload
    def GetMatchingFilter(self, message: Channels.Message) -> (bool, MessageFilter): ...
    @overload
    def GetMatchingFilter(self, messageBuffer: Channels.MessageBuffer) -> (bool, MessageFilter): ...
    @overload
    def GetMatchingFilters(self, message: Channels.Message, results: Generic.ICollection) -> bool: ...
    @overload
    def GetMatchingFilters(self, messageBuffer: Channels.MessageBuffer, results: Generic.ICollection) -> bool: ...
    @overload
    def GetMatchingValue(self, message: Channels.Message) -> (bool, TFilterData): ...
    @overload
    def GetMatchingValue(self, messageBuffer: Channels.MessageBuffer) -> (bool, TFilterData): ...
    @overload
    def GetMatchingValues(self, message: Channels.Message, results: Generic.ICollection) -> bool: ...
    @overload
    def GetMatchingValues(self, messageBuffer: Channels.MessageBuffer, results: Generic.ICollection) -> bool: ...

class InstanceBehavior(object):
    """    """

class IOperationInvoker:
    """    """
    @overload
    def AllocateInputs() -> System.System.Array[object]: ...
    @overload
    def InvokeBegin(self, instance: object, inputs: System.System.Array[object], callback: System.AsyncCallback, state: object) -> System.IAsyncResult: ...
    @overload
    def InvokeEnd(self, instance: object, result: System.IAsyncResult) -> (object, System.System.Array[object]): ...

class IParameterInspector:
    """    """
    @overload
    def AfterCall(self, operationName: str, outputs: System.System.Array[object], returnValue: object, correlationState: object) -> None: ...
    @overload
    def BeforeCall(self, operationName: str, inputs: System.System.Array[object]) -> object: ...

class MessageFilter(object):
    """    """
    @overload
    def Match(self, buffer: Channels.MessageBuffer) -> bool: ...
    @overload
    def Match(self, message: Channels.Message) -> bool: ...

class OperationInvokerBehavior(object):
    """    """
    def __init__(self): ...

class SyncMethodInvoker(object):
    """    """
    def __init__(self, method: Reflection.MethodInfo): ...
    @overload
    def AllocateInputs() -> System.System.Array[object]: ...
    @property
    def Method(self) -> Reflection.MethodInfo: ...
    @property
    def MethodName(self) -> str: ...
    @overload
    def InvokeBegin(self, instance: object, inputs: System.System.Array[object], callback: System.AsyncCallback, state: object) -> System.IAsyncResult: ...
    @overload
    def InvokeEnd(self, instance: object, result: System.IAsyncResult) -> (object, System.System.Array[object]): ...

class TaskMethodInvoker(object):
    """    """
    def __init__(self, taskMethod: Reflection.MethodInfo, taskType: System.Type): ...
    @overload
    def AllocateInputs() -> System.System.Array[object]: ...
    @property
    def Method(self) -> Reflection.MethodInfo: ...
    @property
    def MethodName(self) -> str: ...
    @overload
    def InvokeBegin(self, instance: object, inputs: System.System.Array[object], callback: System.AsyncCallback, state: object) -> System.IAsyncResult: ...
    @overload
    def InvokeEnd(self, instance: object, result: System.IAsyncResult) -> (object, System.System.Array[object]): ...

class OperationFault(Channels.XmlObjectSerializerFault):
    """    OperationFault[T]
    """
    def __init__(self, serializer: Serialization.XmlObjectSerializer, faultException: ServiceModel.FaultException): ...

# endregion
