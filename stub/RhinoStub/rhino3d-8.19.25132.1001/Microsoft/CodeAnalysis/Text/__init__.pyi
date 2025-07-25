"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["LinePosition", "LinePositionSpan", "SourceHashAlgorithm", "SourceText", "SourceTextContainer", "TextChange", "TextChangeEventArgs", "TextChangeRange", "TextLine", "TextLineCollection", "TextSpan", "Enumerator"]
# endregion

# region: Imports
from System import IO
from System import Text
from System import Threading
from System.Collections import Generic
from System.Collections import Immutable
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: Microsoft.CodeAnalysis, Version=4.6.0.0

class LinePosition(System.ValueType):
    """    """
    def __init__(self, line: int, character: int): ...
    @overload
    def CompareTo(self, other: LinePosition) -> int: ...
    @overload
    def Equals(self, other: LinePosition) -> bool: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Character(self) -> int: ...
    @property
    def Line(self) -> int: ...
    @property
    def Zero(self) -> LinePosition: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class LinePositionSpan(System.ValueType):
    """    """
    def __init__(self, start: LinePosition, end: LinePosition): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def Equals(self, other: LinePositionSpan) -> bool: ...
    @property
    def End(self) -> LinePosition: ...
    @property
    def Start(self) -> LinePosition: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class SourceHashAlgorithm(enum.Enum):
    None_ = 0
    Sha1 = 1
    Sha256 = 2

class SourceText(object):
    """    """
    @overload
    def ContentEquals(self, other: SourceText) -> bool: ...
    @overload
    def CopyTo(self, sourceIndex: int, destination: System.System.Array[System.Char], destinationIndex: int, count: int) -> None: ...
    @overload
    @staticmethod
    def From(text: str, encoding: Text.Encoding, checksumAlgorithm: SourceHashAlgorithm) -> SourceText: ...
    @overload
    @staticmethod
    def From(reader: IO.TextReader, length: int, encoding: Text.Encoding, checksumAlgorithm: SourceHashAlgorithm) -> SourceText: ...
    @overload
    @staticmethod
    def From(stream: IO.Stream, encoding: Text.Encoding, checksumAlgorithm: SourceHashAlgorithm, throwIfBinaryDetected: bool) -> SourceText: ...
    @overload
    @staticmethod
    def From(stream: IO.Stream, encoding: Text.Encoding, checksumAlgorithm: SourceHashAlgorithm, throwIfBinaryDetected: bool, canBeEmbedded: bool) -> SourceText: ...
    @overload
    @staticmethod
    def From(buffer: System.System.Array[System.Byte], length: int, encoding: Text.Encoding, checksumAlgorithm: SourceHashAlgorithm, throwIfBinaryDetected: bool) -> SourceText: ...
    @overload
    @staticmethod
    def From(buffer: System.System.Array[System.Byte], length: int, encoding: Text.Encoding, checksumAlgorithm: SourceHashAlgorithm, throwIfBinaryDetected: bool, canBeEmbedded: bool) -> SourceText: ...
    @property
    def CanBeEmbedded(self) -> bool: ...
    @property
    def ChecksumAlgorithm(self) -> SourceHashAlgorithm: ...
    @property
    def Container(self) -> SourceTextContainer: ...
    @property
    def Encoding(self) -> Text.Encoding: ...
    @property
    def Item(self) -> System.Char: ...
    @property
    def Length(self) -> int: ...
    @property
    def Lines(self) -> TextLineCollection: ...
    @overload
    def GetChangeRanges(self, oldText: SourceText) -> Generic.IReadOnlyList: ...
    @overload
    def GetChecksum() -> Immutable.ImmutableArray: ...
    @overload
    def GetSubText(self, start: int) -> SourceText: ...
    @overload
    def GetSubText(self, span: TextSpan) -> SourceText: ...
    @overload
    def GetTextChanges(self, oldText: SourceText) -> Generic.IReadOnlyList: ...
    @overload
    def Replace(self, span: TextSpan, newText: str) -> SourceText: ...
    @overload
    def Replace(self, start: int, length: int, newText: str) -> SourceText: ...
    @overload
    def ToString() -> str: ...
    @overload
    def ToString(self, span: TextSpan) -> str: ...
    @overload
    def WithChanges(self, changes: Generic.IEnumerable) -> SourceText: ...
    @overload
    def WithChanges(self, changes: System.Array[TextChange]) -> SourceText: ...
    @overload
    def Write(self, textWriter: IO.TextWriter, cancellationToken: Threading.CancellationToken) -> None: ...
    @overload
    def Write(self, writer: IO.TextWriter, span: TextSpan, cancellationToken: Threading.CancellationToken) -> None: ...

class SourceTextContainer(object):
    """    """
    @property
    def CurrentText(self) -> SourceText: ...
    @property
    def TextChanged(self): ...

class TextChange(System.ValueType):
    """    """
    def __init__(self, span: TextSpan, newText: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def Equals(self, other: TextChange) -> bool: ...
    @property
    def NewText(self) -> str: ...
    @property
    def NoChanges(self) -> Generic.IReadOnlyList: ...
    @property
    def Span(self) -> TextSpan: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class TextChangeEventArgs(System.EventArgs):
    """    """
    @overload
    def __init__(self, oldText: SourceText, newText: SourceText, changes: Generic.IEnumerable): ...
    @overload
    def __init__(self, oldText: SourceText, newText: SourceText, changes: System.Array[TextChangeRange]): ...
    @property
    def Changes(self) -> Generic.IReadOnlyList: ...
    @property
    def NewText(self) -> SourceText: ...
    @property
    def OldText(self) -> SourceText: ...

class TextChangeRange(System.ValueType):
    """    """
    def __init__(self, span: TextSpan, newLength: int): ...
    @overload
    @staticmethod
    def Collapse(changes: Generic.IEnumerable) -> TextChangeRange: ...
    @overload
    def Equals(self, other: TextChangeRange) -> bool: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def NewLength(self) -> int: ...
    @property
    def NoChanges(self) -> Generic.IReadOnlyList: ...
    @property
    def Span(self) -> TextSpan: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class TextLine(System.ValueType):
    """    """
    @overload
    def Equals(self, other: TextLine) -> bool: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    @staticmethod
    def FromSpan(text: SourceText, span: TextSpan) -> TextLine: ...
    @property
    def End(self) -> int: ...
    @property
    def EndIncludingLineBreak(self) -> int: ...
    @property
    def LineNumber(self) -> int: ...
    @property
    def Span(self) -> TextSpan: ...
    @property
    def SpanIncludingLineBreak(self) -> TextSpan: ...
    @property
    def Start(self) -> int: ...
    @property
    def Text(self) -> SourceText: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class TextLineCollection(object):
    """    """
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> TextLine: ...
    @overload
    def GetEnumerator() -> Enumerator: ...
    @overload
    def GetLineFromPosition(self, position: int) -> TextLine: ...
    @overload
    def GetLinePosition(self, position: int) -> LinePosition: ...
    @overload
    def GetLinePositionSpan(self, span: TextSpan) -> LinePositionSpan: ...
    @overload
    def GetPosition(self, position: LinePosition) -> int: ...
    @overload
    def GetTextSpan(self, span: LinePositionSpan) -> TextSpan: ...
    @overload
    def IndexOf(self, position: int) -> int: ...

class TextSpan(System.ValueType):
    """    """
    def __init__(self, start: int, length: int): ...
    @overload
    def CompareTo(self, other: TextSpan) -> int: ...
    @overload
    def Contains(self, position: int) -> bool: ...
    @overload
    def Contains(self, span: TextSpan) -> bool: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def Equals(self, other: TextSpan) -> bool: ...
    @overload
    @staticmethod
    def FromBounds(start: int, end: int) -> TextSpan: ...
    @property
    def End(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Start(self) -> int: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def Intersection(self, span: TextSpan) -> System.Nullable: ...
    @overload
    def IntersectsWith(self, span: TextSpan) -> bool: ...
    @overload
    def IntersectsWith(self, position: int) -> bool: ...
    @overload
    def Overlap(self, span: TextSpan) -> System.Nullable: ...
    @overload
    def OverlapsWith(self, span: TextSpan) -> bool: ...
    @overload
    def ToString() -> str: ...

class Enumerator(System.ValueType):
    """    """
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Current(self) -> TextLine: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def MoveNext() -> bool: ...

# endregion
