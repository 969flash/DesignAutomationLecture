"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Generic"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Immutable"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Specialized"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["ObjectModel", "Specialized"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Specialized", "CaseInsensitiveComparer", "CollectionBase", "DictionaryBase", "Queue", "ReadOnlyCollectionBase", "SortedList", "Stack"]
# endregion

# region: Imports
from System import Globalization
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Exports
__all__ = ["Concurrent"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Generic", "BitArray", "StructuralComparisons"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Exports
__all__ = ["ObjectModel", "Concurrent", "Generic", "ArrayList", "Comparer", "DictionaryEntry", "Hashtable", "ICollection", "IComparer", "IDictionary", "IDictionaryEnumerator", "IEnumerable", "IEnumerator", "IEqualityComparer", "IList", "IStructuralComparable", "IStructuralEquatable", "ListDictionaryInternal"]
# endregion

# region: Imports
from System import Globalization
from System.Runtime import CompilerServices
from System.Runtime import Serialization
from typing import overload
import System
# endregion

# region: System.Private.CoreLib, Version=7.0.0.0

class ArrayList(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int): ...
    @overload
    def __init__(self, c: ICollection): ...
    @overload
    @staticmethod
    def Adapter(list_: IList) -> ArrayList: ...
    @overload
    def Add(self, value: object) -> int: ...
    @overload
    def AddRange(self, c: ICollection) -> None: ...
    @overload
    def BinarySearch(self, value: object) -> int: ...
    @overload
    def BinarySearch(self, value: object, comparer: IComparer) -> int: ...
    @overload
    def BinarySearch(self, index: int, count: int, value: object, comparer: IComparer) -> int: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Clone() -> object: ...
    @overload
    def Contains(self, item: object) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array) -> None: ...
    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None: ...
    @overload
    def CopyTo(self, index: int, array: System.Array, arrayIndex: int, count: int) -> None: ...
    @overload
    @staticmethod
    def FixedSize(list_: IList) -> IList: ...
    @overload
    @staticmethod
    def FixedSize(list_: ArrayList) -> ArrayList: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self) -> object: ...
    @property
    def SyncRoot(self) -> object: ...
    @overload
    def GetEnumerator() -> IEnumerator: ...
    @overload
    def GetEnumerator(self, index: int, count: int) -> IEnumerator: ...
    @overload
    def GetRange(self, index: int, count: int) -> ArrayList: ...
    @overload
    def IndexOf(self, value: object) -> int: ...
    @overload
    def IndexOf(self, value: object, startIndex: int) -> int: ...
    @overload
    def IndexOf(self, value: object, startIndex: int, count: int) -> int: ...
    @overload
    def Insert(self, index: int, value: object) -> None: ...
    @overload
    def InsertRange(self, index: int, c: ICollection) -> None: ...
    @overload
    def LastIndexOf(self, value: object) -> int: ...
    @overload
    def LastIndexOf(self, value: object, startIndex: int) -> int: ...
    @overload
    def LastIndexOf(self, value: object, startIndex: int, count: int) -> int: ...
    @overload
    @staticmethod
    def ReadOnly(list_: IList) -> IList: ...
    @overload
    @staticmethod
    def ReadOnly(list_: ArrayList) -> ArrayList: ...
    @overload
    def Remove(self, obj: object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def RemoveRange(self, index: int, count: int) -> None: ...
    @overload
    @staticmethod
    def Repeat(value: object, count: int) -> ArrayList: ...
    @overload
    def Reverse() -> None: ...
    @overload
    def Reverse(self, index: int, count: int) -> None: ...
    @Capacity.setter
    def Capacity(self, value: System.Void): ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def SetRange(self, index: int, c: ICollection) -> None: ...
    @overload
    def Sort() -> None: ...
    @overload
    def Sort(self, comparer: IComparer) -> None: ...
    @overload
    def Sort(self, index: int, count: int, comparer: IComparer) -> None: ...
    @overload
    @staticmethod
    def Synchronized(list_: IList) -> IList: ...
    @overload
    @staticmethod
    def Synchronized(list_: ArrayList) -> ArrayList: ...
    @overload
    def ToArray() -> System.System.Array[object]: ...
    @overload
    def ToArray(self, type_: System.Type) -> System.Array: ...
    @overload
    def TrimToSize() -> None: ...

class Comparer(object):
    """    """
    def __init__(self, culture: Globalization.CultureInfo): ...
    @property
    def Default(self) -> Comparer: ...
    @property
    def DefaultInvariant(self) -> Comparer: ...
    @overload
    def Compare(self, a: object, b: object) -> int: ...
    @overload
    def GetObjectData(self, info: Serialization.SerializationInfo, context: Serialization.StreamingContext) -> None: ...

class DictionaryEntry(System.ValueType):
    """    """
    def __init__(self, key: object, value: object): ...
    @overload
    def Deconstruct() -> (object, object): ...
    @property
    def Key(self) -> object: ...
    @property
    def Value(self) -> object: ...
    @Key.setter
    def Key(self, value: System.Void): ...
    @Value.setter
    def Value(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class Hashtable(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int): ...
    @overload
    def __init__(self, equalityComparer: IEqualityComparer): ...
    @overload
    def __init__(self, d: IDictionary): ...
    @overload
    def __init__(self, capacity: int, loadFactor: System.Single): ...
    @overload
    def __init__(self, hcp: IHashCodeProvider, comparer: IComparer): ...
    @overload
    def __init__(self, capacity: int, equalityComparer: IEqualityComparer): ...
    @overload
    def __init__(self, d: IDictionary, loadFactor: System.Single): ...
    @overload
    def __init__(self, d: IDictionary, equalityComparer: IEqualityComparer): ...
    @overload
    def __init__(self, capacity: int, loadFactor: System.Single, equalityComparer: IEqualityComparer): ...
    @overload
    def __init__(self, capacity: int, hcp: IHashCodeProvider, comparer: IComparer): ...
    @overload
    def __init__(self, d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer): ...
    @overload
    def __init__(self, d: IDictionary, loadFactor: System.Single, equalityComparer: IEqualityComparer): ...
    @overload
    def __init__(self, capacity: int, loadFactor: System.Single, hcp: IHashCodeProvider, comparer: IComparer): ...
    @overload
    def __init__(self, d: IDictionary, loadFactor: System.Single, hcp: IHashCodeProvider, comparer: IComparer): ...
    @overload
    def Add(self, key: object, value: object) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Clone() -> object: ...
    @overload
    def Contains(self, key: object) -> bool: ...
    @overload
    def ContainsKey(self, key: object) -> bool: ...
    @overload
    def ContainsValue(self, value: object) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self) -> object: ...
    @property
    def Keys(self) -> ICollection: ...
    @property
    def SyncRoot(self) -> object: ...
    @property
    def Values(self) -> ICollection: ...
    @overload
    def GetEnumerator() -> IDictionaryEnumerator: ...
    @overload
    def GetObjectData(self, info: Serialization.SerializationInfo, context: Serialization.StreamingContext) -> None: ...
    @overload
    def OnDeserialization(self, sender: object) -> None: ...
    @overload
    def Remove(self, key: object) -> None: ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    @staticmethod
    def Synchronized(table: Hashtable) -> Hashtable: ...

class ICollection:
    """    """
    @overload
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def SyncRoot(self) -> object: ...

class IComparer:
    """    """
    @overload
    def Compare(self, x: object, y: object) -> int: ...

class IDictionary:
    """    """
    @overload
    def Add(self, key: object, value: object) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Contains(self, key: object) -> bool: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self) -> object: ...
    @property
    def Keys(self) -> ICollection: ...
    @property
    def Values(self) -> ICollection: ...
    @overload
    def GetEnumerator() -> IDictionaryEnumerator: ...
    @overload
    def Remove(self, key: object) -> None: ...
    @Item.setter
    def Item(self, value: System.Void): ...

class IDictionaryEnumerator:
    """    """
    @property
    def Entry(self) -> DictionaryEntry: ...
    @property
    def Key(self) -> object: ...
    @property
    def Value(self) -> object: ...

class IEnumerable:
    """    """
    @overload
    def GetEnumerator() -> IEnumerator: ...

class IEnumerator:
    """    """
    @property
    def Current(self) -> object: ...
    @overload
    def MoveNext() -> bool: ...
    @overload
    def Reset() -> None: ...

class IEqualityComparer:
    """    """
    @overload
    def Equals(self, x: object, y: object) -> bool: ...
    @overload
    def GetHashCode(self, obj: object) -> int: ...

class IList:
    """    """
    @overload
    def Add(self, value: object) -> int: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Contains(self, value: object) -> bool: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self) -> object: ...
    @overload
    def IndexOf(self, value: object) -> int: ...
    @overload
    def Insert(self, index: int, value: object) -> None: ...
    @overload
    def Remove(self, value: object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, value: System.Void): ...

class IStructuralComparable:
    """    """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int: ...

class IStructuralEquatable:
    """    """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool: ...
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int: ...

class ListDictionaryInternal(object):
    """    """
    def __init__(self): ...
    @overload
    def Add(self, key: object, value: object) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Contains(self, key: object) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self) -> object: ...
    @property
    def Keys(self) -> ICollection: ...
    @property
    def SyncRoot(self) -> object: ...
    @property
    def Values(self) -> ICollection: ...
    @overload
    def GetEnumerator() -> IDictionaryEnumerator: ...
    @overload
    def Remove(self, key: object) -> None: ...
    @Item.setter
    def Item(self, value: System.Void): ...

# endregion

# region: System.Collections, Version=7.0.0.0

class BitArray(object):
    """    """
    @overload
    def __init__(self, length: int): ...
    @overload
    def __init__(self, bytes_: System.System.Array[System.Byte]): ...
    @overload
    def __init__(self, values: System.System.Array[bool]): ...
    @overload
    def __init__(self, values: System.System.Array[int]): ...
    @overload
    def __init__(self, bits: BitArray): ...
    @overload
    def __init__(self, length: int, defaultValue: bool): ...
    @overload
    def And(self, value: BitArray) -> BitArray: ...
    @overload
    def Clone() -> object: ...
    @overload
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @overload
    def Get(self, index: int) -> bool: ...
    @property
    def SyncRoot(self) -> object: ...
    @overload
    def GetEnumerator() -> IEnumerator: ...
    @overload
    def LeftShift(self, count: int) -> BitArray: ...
    @overload
    def Not() -> BitArray: ...
    @overload
    def Or(self, value: BitArray) -> BitArray: ...
    @overload
    def RightShift(self, count: int) -> BitArray: ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @Length.setter
    def Length(self, value: System.Void): ...
    @overload
    def Set(self, index: int, value: bool) -> None: ...
    @overload
    def SetAll(self, value: bool) -> None: ...
    @overload
    def Xor(self, value: BitArray) -> BitArray: ...

class StructuralComparisons(object):
    """    """
    @property
    def StructuralComparer(self) -> IComparer: ...
    @property
    def StructuralEqualityComparer(self) -> IEqualityComparer: ...

# endregion

# region: System.Collections.NonGeneric, Version=7.0.0.0

class CaseInsensitiveComparer(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, culture: Globalization.CultureInfo): ...
    @overload
    def Compare(self, a: object, b: object) -> int: ...
    @property
    def Default(self) -> CaseInsensitiveComparer: ...
    @property
    def DefaultInvariant(self) -> CaseInsensitiveComparer: ...

class CollectionBase(object):
    """    """
    @overload
    def Clear() -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @overload
    def GetEnumerator() -> IEnumerator: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Capacity.setter
    def Capacity(self, value: System.Void): ...

class DictionaryBase(object):
    """    """
    @overload
    def Clear() -> None: ...
    @overload
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @overload
    def GetEnumerator() -> IDictionaryEnumerator: ...

class Queue(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int): ...
    @overload
    def __init__(self, col: ICollection): ...
    @overload
    def __init__(self, capacity: int, growFactor: System.Single): ...
    @overload
    def Clear() -> None: ...
    @overload
    def Clone() -> object: ...
    @overload
    def Contains(self, obj: object) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @overload
    def Dequeue() -> object: ...
    @overload
    def Enqueue(self, obj: object) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def SyncRoot(self) -> object: ...
    @overload
    def GetEnumerator() -> IEnumerator: ...
    @overload
    def Peek() -> object: ...
    @overload
    @staticmethod
    def Synchronized(queue: Queue) -> Queue: ...
    @overload
    def ToArray() -> System.System.Array[object]: ...
    @overload
    def TrimToSize() -> None: ...

class ReadOnlyCollectionBase(object):
    """    """
    @property
    def Count(self) -> int: ...
    @overload
    def GetEnumerator() -> IEnumerator: ...

class SortedList(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, initialCapacity: int): ...
    @overload
    def __init__(self, comparer: IComparer): ...
    @overload
    def __init__(self, d: IDictionary): ...
    @overload
    def __init__(self, comparer: IComparer, capacity: int): ...
    @overload
    def __init__(self, d: IDictionary, comparer: IComparer): ...
    @overload
    def Add(self, key: object, value: object) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Clone() -> object: ...
    @overload
    def Contains(self, key: object) -> bool: ...
    @overload
    def ContainsKey(self, key: object) -> bool: ...
    @overload
    def ContainsValue(self, value: object) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self) -> object: ...
    @property
    def Keys(self) -> ICollection: ...
    @property
    def SyncRoot(self) -> object: ...
    @property
    def Values(self) -> ICollection: ...
    @overload
    def GetByIndex(self, index: int) -> object: ...
    @overload
    def GetEnumerator() -> IDictionaryEnumerator: ...
    @overload
    def GetKey(self, index: int) -> object: ...
    @overload
    def GetKeyList() -> IList: ...
    @overload
    def GetValueList() -> IList: ...
    @overload
    def IndexOfKey(self, key: object) -> int: ...
    @overload
    def IndexOfValue(self, value: object) -> int: ...
    @overload
    def Remove(self, key: object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Capacity.setter
    def Capacity(self, value: System.Void): ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def SetByIndex(self, index: int, value: object) -> None: ...
    @overload
    @staticmethod
    def Synchronized(list_: SortedList) -> SortedList: ...
    @overload
    def TrimToSize() -> None: ...

class Stack(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, initialCapacity: int): ...
    @overload
    def __init__(self, col: ICollection): ...
    @overload
    def Clear() -> None: ...
    @overload
    def Clone() -> object: ...
    @overload
    def Contains(self, obj: object) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def SyncRoot(self) -> object: ...
    @overload
    def GetEnumerator() -> IEnumerator: ...
    @overload
    def Peek() -> object: ...
    @overload
    def Pop() -> object: ...
    @overload
    def Push(self, obj: object) -> None: ...
    @overload
    @staticmethod
    def Synchronized(stack: Stack) -> Stack: ...
    @overload
    def ToArray() -> System.System.Array[object]: ...

# endregion

