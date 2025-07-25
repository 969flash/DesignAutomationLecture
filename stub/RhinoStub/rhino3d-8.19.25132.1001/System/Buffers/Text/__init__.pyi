"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Base64", "Utf8Formatter", "Utf8Parser"]
# endregion

# region: Imports
from System import Buffers
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: System.Private.CoreLib, Version=7.0.0.0

class Base64(object):
    """    """
    @overload
    @staticmethod
    def DecodeFromUtf8(utf8: System.ReadOnlySpan, bytes_: System.Span, isFinalBlock: bool) -> (Buffers.OperationStatus, int, int): ...
    @overload
    @staticmethod
    def DecodeFromUtf8InPlace(buffer: System.Span) -> (Buffers.OperationStatus, int): ...
    @overload
    @staticmethod
    def EncodeToUtf8(bytes_: System.ReadOnlySpan, utf8: System.Span, isFinalBlock: bool) -> (Buffers.OperationStatus, int, int): ...
    @overload
    @staticmethod
    def EncodeToUtf8InPlace(buffer: System.Span, dataLength: int) -> (Buffers.OperationStatus, int): ...
    @overload
    @staticmethod
    def GetMaxDecodedFromUtf8Length(length: int) -> int: ...
    @overload
    @staticmethod
    def GetMaxEncodedToUtf8Length(length: int) -> int: ...

class Utf8Formatter(object):
    """    """
    @overload
    @staticmethod
    def TryFormat(value: System.TimeSpan, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.Int64, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.UInt64, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: int, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.UInt32, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.Int16, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.UInt16, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.Byte, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.Guid, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.Single, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: float, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.Decimal, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.DateTime, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.DateTimeOffset, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: System.SByte, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...
    @overload
    @staticmethod
    def TryFormat(value: bool, destination: System.Span, format_: Buffers.StandardFormat) -> (bool, int): ...

class Utf8Parser(object):
    """    """
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.TimeSpan, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.UInt64, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.UInt32, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.UInt16, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.Byte, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.Int64, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, int, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.SByte, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.Guid, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, float, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.Single, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.Decimal, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.DateTimeOffset, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.DateTime, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, System.Int16, int): ...
    @overload
    @staticmethod
    def TryParse(source: System.ReadOnlySpan, standardFormat: System.Char) -> (bool, bool, int): ...

# endregion
