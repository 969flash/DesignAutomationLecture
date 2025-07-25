"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["BlockingCollection", "ConcurrentBag", "ConcurrentDictionary", "ConcurrentStack", "OrderablePartitioner", "Partitioner", "EnumerablePartitionerOptions"]
# endregion

# region: Imports
from System import Threading
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: Exports
__all__ = ["ConcurrentQueue", "IProducerConsumerCollection"]
# endregion

# region: Imports
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: System.Private.CoreLib, Version=7.0.0.0

class ConcurrentQueue(object):
    """    ConcurrentQueue[T]
    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, collection: Generic.IEnumerable): ...
    @overload
    def Clear() -> None: ...
    @overload
    def CopyTo(self, array: System.Array[T], index: int) -> None: ...
    @overload
    def Enqueue(self, item: T) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def ToArray() -> System.Array[T]: ...
    @overload
    def TryDequeue() -> (bool, T): ...
    @overload
    def TryPeek() -> (bool, T): ...

class IProducerConsumerCollection:
    """    IProducerConsumerCollection[T]
    """
    @overload
    def CopyTo(self, array: System.Array[T], index: int) -> None: ...
    @overload
    def ToArray() -> System.Array[T]: ...
    @overload
    def TryAdd(self, item: T) -> bool: ...
    @overload
    def TryTake() -> (bool, T): ...

# endregion

# region: System.Collections.Concurrent, Version=7.0.0.0

class BlockingCollection(object):
    """    BlockingCollection[T]
    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, boundedCapacity: int): ...
    @overload
    def __init__(self, collection: IProducerConsumerCollection): ...
    @overload
    def __init__(self, collection: IProducerConsumerCollection, boundedCapacity: int): ...
    @overload
    def Add(self, item: T) -> None: ...
    @overload
    def Add(self, item: T, cancellationToken: Threading.CancellationToken) -> None: ...
    @overload
    @staticmethod
    def AddToAny(collections: System.Array[BlockingCollection], item: T) -> int: ...
    @overload
    @staticmethod
    def AddToAny(collections: System.Array[BlockingCollection], item: T, cancellationToken: Threading.CancellationToken) -> int: ...
    @overload
    def CompleteAdding() -> None: ...
    @overload
    def CopyTo(self, array: System.Array[T], index: int) -> None: ...
    @overload
    def Dispose() -> None: ...
    @property
    def BoundedCapacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsAddingCompleted(self) -> bool: ...
    @property
    def IsCompleted(self) -> bool: ...
    @overload
    def GetConsumingEnumerable() -> Generic.IEnumerable: ...
    @overload
    def GetConsumingEnumerable(self, cancellationToken: Threading.CancellationToken) -> Generic.IEnumerable: ...
    @overload
    def Take() -> T: ...
    @overload
    def Take(self, cancellationToken: Threading.CancellationToken) -> T: ...
    @overload
    @staticmethod
    def TakeFromAny(collections: System.Array[BlockingCollection]) -> (int, T): ...
    @overload
    @staticmethod
    def TakeFromAny(collections: System.Array[BlockingCollection], cancellationToken: Threading.CancellationToken) -> (int, T): ...
    @overload
    def ToArray() -> System.Array[T]: ...
    @overload
    def TryAdd(self, item: T) -> bool: ...
    @overload
    def TryAdd(self, item: T, timeout: System.TimeSpan) -> bool: ...
    @overload
    def TryAdd(self, item: T, millisecondsTimeout: int) -> bool: ...
    @overload
    def TryAdd(self, item: T, millisecondsTimeout: int, cancellationToken: Threading.CancellationToken) -> bool: ...
    @overload
    @staticmethod
    def TryAddToAny(collections: System.Array[BlockingCollection], item: T) -> int: ...
    @overload
    @staticmethod
    def TryAddToAny(collections: System.Array[BlockingCollection], item: T, millisecondsTimeout: int) -> int: ...
    @overload
    @staticmethod
    def TryAddToAny(collections: System.Array[BlockingCollection], item: T, timeout: System.TimeSpan) -> int: ...
    @overload
    @staticmethod
    def TryAddToAny(collections: System.Array[BlockingCollection], item: T, millisecondsTimeout: int, cancellationToken: Threading.CancellationToken) -> int: ...
    @overload
    def TryTake() -> (bool, T): ...
    @overload
    def TryTake(self, millisecondsTimeout: int) -> (bool, T): ...
    @overload
    def TryTake(self, timeout: System.TimeSpan) -> (bool, T): ...
    @overload
    def TryTake(self, millisecondsTimeout: int, cancellationToken: Threading.CancellationToken) -> (bool, T): ...
    @overload
    @staticmethod
    def TryTakeFromAny(collections: System.Array[BlockingCollection]) -> (int, T): ...
    @overload
    @staticmethod
    def TryTakeFromAny(collections: System.Array[BlockingCollection], timeout: System.TimeSpan) -> (int, T): ...
    @overload
    @staticmethod
    def TryTakeFromAny(collections: System.Array[BlockingCollection], millisecondsTimeout: int) -> (int, T): ...
    @overload
    @staticmethod
    def TryTakeFromAny(collections: System.Array[BlockingCollection], millisecondsTimeout: int, cancellationToken: Threading.CancellationToken) -> (int, T): ...

class ConcurrentBag(object):
    """    ConcurrentBag[T]
    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, collection: Generic.IEnumerable): ...
    @overload
    def Add(self, item: T) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def CopyTo(self, array: System.Array[T], index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def ToArray() -> System.Array[T]: ...
    @overload
    def TryPeek() -> (bool, T): ...
    @overload
    def TryTake() -> (bool, T): ...

class ConcurrentDictionary(object):
    """    ConcurrentDictionary[TKey, TValue]
    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, collection: Generic.IEnumerable): ...
    @overload
    def __init__(self, comparer: Generic.IEqualityComparer): ...
    @overload
    def __init__(self, concurrencyLevel: int, capacity: int): ...
    @overload
    def __init__(self, collection: Generic.IEnumerable, comparer: Generic.IEqualityComparer): ...
    @overload
    def __init__(self, concurrencyLevel: int, collection: Generic.IEnumerable, comparer: Generic.IEqualityComparer): ...
    @overload
    def __init__(self, concurrencyLevel: int, capacity: int, comparer: Generic.IEqualityComparer): ...
    @overload
    def AddOrUpdate(self, key: TKey, addValue: TValue, updateValueFactory: System.Func) -> TValue: ...
    @overload
    def AddOrUpdate(self, key: TKey, addValueFactory: System.Func, updateValueFactory: System.Func) -> TValue: ...
    @overload
    def AddOrUpdate(self, key: TKey, addValueFactory: System.Func, updateValueFactory: System.Func, factoryArgument: TArg) -> TValue: ...
    @overload
    def Clear() -> None: ...
    @overload
    def ContainsKey(self, key: TKey) -> bool: ...
    @property
    def Comparer(self) -> Generic.IEqualityComparer: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Item(self) -> TValue: ...
    @property
    def Keys(self) -> Generic.ICollection: ...
    @property
    def Values(self) -> Generic.ICollection: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def GetOrAdd(self, key: TKey, value: TValue) -> TValue: ...
    @overload
    def GetOrAdd(self, key: TKey, valueFactory: System.Func) -> TValue: ...
    @overload
    def GetOrAdd(self, key: TKey, valueFactory: System.Func, factoryArgument: TArg) -> TValue: ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def ToArray() -> Generic.System.Array[Generic.KeyValuePair]: ...
    @overload
    def TryAdd(self, key: TKey, value: TValue) -> bool: ...
    @overload
    def TryGetValue(self, key: TKey) -> (bool, TValue): ...
    @overload
    def TryRemove(self, item: Generic.KeyValuePair) -> bool: ...
    @overload
    def TryRemove(self, key: TKey) -> (bool, TValue): ...
    @overload
    def TryUpdate(self, key: TKey, newValue: TValue, comparisonValue: TValue) -> bool: ...

class ConcurrentStack(object):
    """    ConcurrentStack[T]
    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, collection: Generic.IEnumerable): ...
    @overload
    def Clear() -> None: ...
    @overload
    def CopyTo(self, array: System.Array[T], index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def Push(self, item: T) -> None: ...
    @overload
    def PushRange(self, items: System.Array[T]) -> None: ...
    @overload
    def PushRange(self, items: System.Array[T], startIndex: int, count: int) -> None: ...
    @overload
    def ToArray() -> System.Array[T]: ...
    @overload
    def TryPeek() -> (bool, T): ...
    @overload
    def TryPop() -> (bool, T): ...
    @overload
    def TryPopRange(self, items: System.Array[T]) -> int: ...
    @overload
    def TryPopRange(self, items: System.Array[T], startIndex: int, count: int) -> int: ...

class OrderablePartitioner(Partitioner):
    """    OrderablePartitioner[TSource]
    """
    @property
    def KeysNormalized(self) -> bool: ...
    @property
    def KeysOrderedAcrossPartitions(self) -> bool: ...
    @property
    def KeysOrderedInEachPartition(self) -> bool: ...
    @overload
    def GetDynamicPartitions() -> Generic.IEnumerable: ...
    @overload
    def GetOrderableDynamicPartitions() -> Generic.IEnumerable: ...
    @overload
    def GetOrderablePartitions(self, partitionCount: int) -> Generic.IList: ...
    @overload
    def GetPartitions(self, partitionCount: int) -> Generic.IList: ...

class Partitioner(object):
    """    Partitioner[TSource]
    """
    @property
    def SupportsDynamicPartitions(self) -> bool: ...
    @overload
    def GetDynamicPartitions() -> Generic.IEnumerable: ...
    @overload
    def GetPartitions(self, partitionCount: int) -> Generic.IList: ...

class EnumerablePartitionerOptions(enum.Enum):
    None_ = 0
    NoBuffering = 1

class Partitioner(object):
    """    """
    @overload
    @staticmethod
    def Create(source: Generic.IEnumerable) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(list_: Generic.IList, loadBalance: bool) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(array: System.Array[TSource], loadBalance: bool) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(source: Generic.IEnumerable, partitionerOptions: EnumerablePartitionerOptions) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(fromInclusive: System.Int64, toExclusive: System.Int64) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(fromInclusive: int, toExclusive: int) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(fromInclusive: System.Int64, toExclusive: System.Int64, rangeSize: System.Int64) -> OrderablePartitioner: ...
    @overload
    @staticmethod
    def Create(fromInclusive: int, toExclusive: int, rangeSize: int) -> OrderablePartitioner: ...

# endregion
