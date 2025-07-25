"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Hosting", "CacheEntryChangeMonitor", "CacheEntryRemovedArguments", "CacheEntryRemovedCallback", "CacheEntryRemovedReason", "CacheEntryUpdateArguments", "CacheEntryUpdateCallback", "CacheItem", "CacheItemPolicy", "CacheItemPriority", "ChangeMonitor", "DefaultCacheCapabilities", "FileChangeMonitor", "HostFileChangeMonitor", "MemoryCache", "ObjectCache", "OnChangedCallback"]
# endregion

# region: Imports
from System.Collections import Generic
from System.Collections import ObjectModel
from System.Collections import Specialized
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: System.Runtime.Caching, Version=4.0.0.0

class CacheEntryChangeMonitor(ChangeMonitor):
    """    """
    @property
    def CacheKeys(self) -> ObjectModel.ReadOnlyCollection: ...
    @property
    def LastModified(self) -> System.DateTimeOffset: ...
    @property
    def RegionName(self) -> str: ...

class CacheEntryRemovedArguments(object):
    """    """
    def __init__(self, source: ObjectCache, reason: CacheEntryRemovedReason, cacheItem: CacheItem): ...
    @property
    def CacheItem(self) -> CacheItem: ...
    @property
    def RemovedReason(self) -> CacheEntryRemovedReason: ...
    @property
    def Source(self) -> ObjectCache: ...

class CacheEntryRemovedCallback(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, arguments: CacheEntryRemovedArguments, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, arguments: CacheEntryRemovedArguments) -> None: ...

class CacheEntryRemovedReason(enum.Enum):
    Removed = 0
    Expired = 1
    Evicted = 2
    ChangeMonitorChanged = 3
    CacheSpecificEviction = 4

class CacheEntryUpdateArguments(object):
    """    """
    def __init__(self, source: ObjectCache, reason: CacheEntryRemovedReason, key: str, regionName: str): ...
    @property
    def Key(self) -> str: ...
    @property
    def RegionName(self) -> str: ...
    @property
    def RemovedReason(self) -> CacheEntryRemovedReason: ...
    @property
    def Source(self) -> ObjectCache: ...
    @property
    def UpdatedCacheItem(self) -> CacheItem: ...
    @property
    def UpdatedCacheItemPolicy(self) -> CacheItemPolicy: ...
    @UpdatedCacheItem.setter
    def UpdatedCacheItem(self, value: System.Void): ...
    @UpdatedCacheItemPolicy.setter
    def UpdatedCacheItemPolicy(self, value: System.Void): ...

class CacheEntryUpdateCallback(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, arguments: CacheEntryUpdateArguments, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, arguments: CacheEntryUpdateArguments) -> None: ...

class CacheItem(object):
    """    """
    @overload
    def __init__(self, key: str): ...
    @overload
    def __init__(self, key: str, value: object): ...
    @overload
    def __init__(self, key: str, value: object, regionName: str): ...
    @property
    def Key(self) -> str: ...
    @property
    def RegionName(self) -> str: ...
    @property
    def Value(self) -> object: ...
    @Key.setter
    def Key(self, value: System.Void): ...
    @RegionName.setter
    def RegionName(self, value: System.Void): ...
    @Value.setter
    def Value(self, value: System.Void): ...

class CacheItemPolicy(object):
    """    """
    def __init__(self): ...
    @property
    def AbsoluteExpiration(self) -> System.DateTimeOffset: ...
    @property
    def ChangeMonitors(self) -> ObjectModel.Collection: ...
    @property
    def Priority(self) -> CacheItemPriority: ...
    @property
    def RemovedCallback(self) -> CacheEntryRemovedCallback: ...
    @property
    def SlidingExpiration(self) -> System.TimeSpan: ...
    @property
    def UpdateCallback(self) -> CacheEntryUpdateCallback: ...
    @AbsoluteExpiration.setter
    def AbsoluteExpiration(self, value: System.Void): ...
    @Priority.setter
    def Priority(self, value: System.Void): ...
    @RemovedCallback.setter
    def RemovedCallback(self, value: System.Void): ...
    @SlidingExpiration.setter
    def SlidingExpiration(self, value: System.Void): ...
    @UpdateCallback.setter
    def UpdateCallback(self, value: System.Void): ...

class CacheItemPriority(enum.Enum):
    Default = 0
    NotRemovable = 1

class ChangeMonitor(object):
    """    """
    @overload
    def Dispose() -> None: ...
    @property
    def HasChanged(self) -> bool: ...
    @property
    def IsDisposed(self) -> bool: ...
    @property
    def UniqueId(self) -> str: ...
    @overload
    def NotifyOnChanged(self, onChangedCallback: OnChangedCallback) -> None: ...

class DefaultCacheCapabilities(enum.Enum):
    None_ = 0
    InMemoryProvider = 1
    OutOfProcessProvider = 2
    CacheEntryChangeMonitors = 4
    AbsoluteExpirations = 8
    SlidingExpirations = 16
    CacheEntryUpdateCallback = 32
    CacheEntryRemovedCallback = 64
    CacheRegions = 128

class FileChangeMonitor(ChangeMonitor):
    """    """
    @property
    def FilePaths(self) -> ObjectModel.ReadOnlyCollection: ...
    @property
    def LastModified(self) -> System.DateTimeOffset: ...

class HostFileChangeMonitor(FileChangeMonitor):
    """    """
    def __init__(self, filePaths: Generic.IList): ...
    @property
    def FilePaths(self) -> ObjectModel.ReadOnlyCollection: ...
    @property
    def LastModified(self) -> System.DateTimeOffset: ...
    @property
    def UniqueId(self) -> str: ...

class MemoryCache(ObjectCache):
    """    """
    @overload
    def __init__(self, name: str, config: Specialized.NameValueCollection): ...
    @overload
    def __init__(self, name: str, config: Specialized.NameValueCollection, ignoreConfigSection: bool): ...
    @overload
    def Add(self, item: CacheItem, policy: CacheItemPolicy) -> bool: ...
    @overload
    def AddOrGetExisting(self, item: CacheItem, policy: CacheItemPolicy) -> CacheItem: ...
    @overload
    def AddOrGetExisting(self, key: str, value: object, absoluteExpiration: System.DateTimeOffset, regionName: str) -> object: ...
    @overload
    def AddOrGetExisting(self, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> object: ...
    @overload
    def Contains(self, key: str, regionName: str) -> bool: ...
    @overload
    def CreateCacheEntryChangeMonitor(self, keys: Generic.IEnumerable, regionName: str) -> CacheEntryChangeMonitor: ...
    @overload
    def Dispose() -> None: ...
    @property
    def CacheMemoryLimit(self) -> System.Int64: ...
    @property
    def Default(self) -> MemoryCache: ...
    @property
    def DefaultCacheCapabilities(self) -> DefaultCacheCapabilities: ...
    @property
    def Item(self) -> object: ...
    @property
    def Name(self) -> str: ...
    @property
    def PhysicalMemoryLimit(self) -> System.Int64: ...
    @property
    def PollingInterval(self) -> System.TimeSpan: ...
    @overload
    def Get(self, key: str, regionName: str) -> object: ...
    @overload
    def GetCacheItem(self, key: str, regionName: str) -> CacheItem: ...
    @overload
    def GetCount(self, regionName: str) -> System.Int64: ...
    @overload
    def GetLastSize(self, regionName: str) -> System.Int64: ...
    @overload
    def GetValues(self, keys: Generic.IEnumerable, regionName: str) -> Generic.IDictionary: ...
    @overload
    def Remove(self, key: str, regionName: str) -> object: ...
    @overload
    def Remove(self, key: str, reason: CacheEntryRemovedReason, regionName: str) -> object: ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def Set(self, item: CacheItem, policy: CacheItemPolicy) -> None: ...
    @overload
    def Set(self, key: str, value: object, absoluteExpiration: System.DateTimeOffset, regionName: str) -> None: ...
    @overload
    def Set(self, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> None: ...
    @overload
    def Trim(self, percent: int) -> System.Int64: ...

class ObjectCache(object):
    """    """
    @property
    def InfiniteAbsoluteExpiration(self) -> System.DateTimeOffset: ...
    @property
    def NoSlidingExpiration(self) -> System.TimeSpan: ...
    @overload
    def Add(self, item: CacheItem, policy: CacheItemPolicy) -> bool: ...
    @overload
    def Add(self, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> bool: ...
    @overload
    def Add(self, key: str, value: object, absoluteExpiration: System.DateTimeOffset, regionName: str) -> bool: ...
    @overload
    def AddOrGetExisting(self, value: CacheItem, policy: CacheItemPolicy) -> CacheItem: ...
    @overload
    def AddOrGetExisting(self, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> object: ...
    @overload
    def AddOrGetExisting(self, key: str, value: object, absoluteExpiration: System.DateTimeOffset, regionName: str) -> object: ...
    @overload
    def Contains(self, key: str, regionName: str) -> bool: ...
    @overload
    def CreateCacheEntryChangeMonitor(self, keys: Generic.IEnumerable, regionName: str) -> CacheEntryChangeMonitor: ...
    @property
    def DefaultCacheCapabilities(self) -> DefaultCacheCapabilities: ...
    @property
    def Host(self) -> System.IServiceProvider: ...
    @property
    def Item(self) -> object: ...
    @property
    def Name(self) -> str: ...
    @overload
    def Get(self, key: str, regionName: str) -> object: ...
    @overload
    def GetCacheItem(self, key: str, regionName: str) -> CacheItem: ...
    @overload
    def GetCount(self, regionName: str) -> System.Int64: ...
    @overload
    def GetValues(self, keys: Generic.IEnumerable, regionName: str) -> Generic.IDictionary: ...
    @overload
    def GetValues(self, regionName: str, keys: System.System.Array[str]) -> Generic.IDictionary: ...
    @overload
    def Remove(self, key: str, regionName: str) -> object: ...
    @Host.setter
    def Host(self, value: System.Void): ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def Set(self, item: CacheItem, policy: CacheItemPolicy) -> None: ...
    @overload
    def Set(self, key: str, value: object, absoluteExpiration: System.DateTimeOffset, regionName: str) -> None: ...
    @overload
    def Set(self, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> None: ...

class OnChangedCallback(System.MulticastDelegate):
    """    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, state: object, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, state: object) -> None: ...

# endregion
