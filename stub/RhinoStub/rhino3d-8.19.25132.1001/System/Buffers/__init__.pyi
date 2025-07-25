"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["BuffersExtensions", "IBufferWriter", "MemoryPool", "ReadOnlySequence", "Enumerator", "ReadOnlySequenceSegment", "SequenceReaderExtensions", "ArrayBufferWriter"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Exports
__all__ = ["Text", "Binary", "SpanAction", "ReadOnlySpanAction", "ArrayPool", "IMemoryOwner", "IPinnable", "MemoryHandle", "MemoryManager", "OperationStatus", "StandardFormat"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from System.Runtime import InteropServices
from typing import overload
import enum
import System
# endregion

# region: System.Private.CoreLib, Version=7.0.0.0

class SpanAction(System.MulticastDelegate):
    """    SpanAction[T, TArg]
    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, span: System.Span, arg: TArg, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, span: System.Span, arg: TArg) -> None: ...

class ReadOnlySpanAction(System.MulticastDelegate):
    """    ReadOnlySpanAction[T, TArg]
    """
    def __init__(self, object_: object, method: System.IntPtr): ...
    @overload
    def BeginInvoke(self, span: System.ReadOnlySpan, arg: TArg, callback: System.AsyncCallback, object_: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, span: System.ReadOnlySpan, arg: TArg) -> None: ...

class ArrayPool(object):
    """    ArrayPool[T]
    """
    @overload
    @staticmethod
    def Create() -> ArrayPool: ...
    @overload
    @staticmethod
    def Create(maxArrayLength: int, maxArraysPerBucket: int) -> ArrayPool: ...
    @property
    def Shared(self) -> ArrayPool: ...
    @overload
    def Rent(self, minimumLength: int) -> System.Array[T]: ...
    @overload
    def Return(self, array: System.Array[T], clearArray: bool) -> None: ...

class IMemoryOwner:
    """    IMemoryOwner[T]
    """
    @property
    def Memory(self) -> System.Memory: ...

class IPinnable:
    """    """
    @overload
    def Pin(self, elementIndex: int) -> MemoryHandle: ...
    @overload
    def Unpin() -> None: ...

class MemoryHandle(System.ValueType):
    """    """
    def __init__(self, pointer: System.Void, handle: InteropServices.GCHandle, pinnable: IPinnable): ...
    @overload
    def Dispose() -> None: ...
    @property
    def Pointer(self) -> System.Void: ...

class MemoryManager(object):
    """    MemoryManager[T]
    """
    @property
    def Memory(self) -> System.Memory: ...
    @overload
    def GetSpan() -> System.Span: ...
    @overload
    def Pin(self, elementIndex: int) -> MemoryHandle: ...
    @overload
    def Unpin() -> None: ...

class OperationStatus(enum.Enum):
    Done = 0
    DestinationTooSmall = 1
    NeedMoreData = 2
    InvalidData = 3

class StandardFormat(System.ValueType):
    """    """
    def __init__(self, symbol: System.Char, precision: System.Byte): ...
    @property
    def NoPrecision(self) -> System.Byte: ...
    @property
    def MaxPrecision(self) -> System.Byte: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def Equals(self, other: StandardFormat) -> bool: ...
    @property
    def HasPrecision(self) -> bool: ...
    @property
    def IsDefault(self) -> bool: ...
    @property
    def Precision(self) -> System.Byte: ...
    @property
    def Symbol(self) -> System.Char: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(format_: System.ReadOnlySpan) -> StandardFormat: ...
    @overload
    @staticmethod
    def Parse(format_: str) -> StandardFormat: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(format_: System.ReadOnlySpan) -> (bool, StandardFormat): ...

# endregion

# region: System.Memory, Version=7.0.0.0

class BuffersExtensions(object):
    """    """
    @overload
    @staticmethod
    def CopyTo(destination: System.Span) -> (ReadOnlySequence): ...
    @overload
    @staticmethod
    def PositionOf(value: T) -> (System.Nullable, ReadOnlySequence): ...
    @overload
    @staticmethod
    def ToArray() -> (System.Array[T], ReadOnlySequence): ...
    @overload
    @staticmethod
    def Write(writer: IBufferWriter, value: System.ReadOnlySpan) -> None: ...

class IBufferWriter:
    """    IBufferWriter[T]
    """
    @overload
    def Advance(self, count: int) -> None: ...
    @overload
    def GetMemory(self, sizeHint: int) -> System.Memory: ...
    @overload
    def GetSpan(self, sizeHint: int) -> System.Span: ...

class MemoryPool(object):
    """    MemoryPool[T]
    """
    @overload
    def Dispose() -> None: ...
    @property
    def MaxBufferSize(self) -> int: ...
    @property
    def Shared(self) -> MemoryPool: ...
    @overload
    def Rent(self, minBufferSize: int) -> IMemoryOwner: ...

class ReadOnlySequence(System.ValueType):
    """    ReadOnlySequence[T]
    """
    @overload
    def __init__(self, array: System.Array[T]): ...
    @overload
    def __init__(self, memory: System.ReadOnlyMemory): ...
    @overload
    def __init__(self, array: System.Array[T], start: int, length: int): ...
    @overload
    def __init__(self, startSegment: ReadOnlySequenceSegment, startIndex: int, endSegment: ReadOnlySequenceSegment, endIndex: int): ...
    @property
    def Empty(self) -> ReadOnlySequence: ...
    @property
    def End(self) -> System.SequencePosition: ...
    @property
    def First(self) -> System.ReadOnlyMemory: ...
    @property
    def FirstSpan(self) -> System.ReadOnlySpan: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def IsSingleSegment(self) -> bool: ...
    @property
    def Length(self) -> System.Int64: ...
    @property
    def Start(self) -> System.SequencePosition: ...
    @overload
    def GetEnumerator() -> Enumerator: ...
    @overload
    def GetOffset(self, position: System.SequencePosition) -> System.Int64: ...
    @overload
    def GetPosition(self, offset: System.Int64) -> System.SequencePosition: ...
    @overload
    def GetPosition(self, offset: System.Int64, origin: System.SequencePosition) -> System.SequencePosition: ...
    @overload
    def Slice(self, start: System.SequencePosition) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: System.Int64) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: int, end: System.SequencePosition) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: int, length: int) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: System.SequencePosition, length: System.Int64) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: System.Int64, end: System.SequencePosition) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: System.Int64, length: System.Int64) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: System.SequencePosition, end: System.SequencePosition) -> ReadOnlySequence: ...
    @overload
    def Slice(self, start: System.SequencePosition, length: int) -> ReadOnlySequence: ...
    @overload
    def ToString() -> str: ...
    @overload
    def TryGet(self, advance: bool) -> (bool, System.SequencePosition, System.ReadOnlyMemory): ...

class Enumerator(System.ValueType):
    """    Enumerator[T]
    """
    def __init__(self, sequence: ReadOnlySequence): ...
    @property
    def Current(self) -> System.ReadOnlyMemory: ...
    @overload
    def MoveNext() -> bool: ...

class ReadOnlySequenceSegment(object):
    """    ReadOnlySequenceSegment[T]
    """
    @property
    def Memory(self) -> System.ReadOnlyMemory: ...
    @property
    def Next(self) -> ReadOnlySequenceSegment: ...
    @property
    def RunningIndex(self) -> System.Int64: ...

class SequenceReaderExtensions(object):
    """    """
    @overload
    @staticmethod
    def TryReadBigEndian() -> (bool, SequenceReader, System.Int16): ...
    @overload
    @staticmethod
    def TryReadBigEndian() -> (bool, SequenceReader, int): ...
    @overload
    @staticmethod
    def TryReadBigEndian() -> (bool, SequenceReader, System.Int64): ...
    @overload
    @staticmethod
    def TryReadLittleEndian() -> (bool, SequenceReader, System.Int16): ...
    @overload
    @staticmethod
    def TryReadLittleEndian() -> (bool, SequenceReader, int): ...
    @overload
    @staticmethod
    def TryReadLittleEndian() -> (bool, SequenceReader, System.Int64): ...

class ArrayBufferWriter(object):
    """    ArrayBufferWriter[T]
    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, initialCapacity: int): ...
    @overload
    def Advance(self, count: int) -> None: ...
    @overload
    def Clear() -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def FreeCapacity(self) -> int: ...
    @property
    def WrittenCount(self) -> int: ...
    @property
    def WrittenMemory(self) -> System.ReadOnlyMemory: ...
    @property
    def WrittenSpan(self) -> System.ReadOnlySpan: ...
    @overload
    def GetMemory(self, sizeHint: int) -> System.Memory: ...
    @overload
    def GetSpan(self, sizeHint: int) -> System.Span: ...

# endregion
