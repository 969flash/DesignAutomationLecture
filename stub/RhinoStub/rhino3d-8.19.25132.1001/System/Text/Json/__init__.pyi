"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Nodes", "Serialization", "JsonNamingPolicy", "JsonDocument", "JsonDocumentOptions", "JsonElement", "ArrayEnumerator", "ObjectEnumerator", "JsonProperty", "JsonValueKind", "JsonCommentHandling", "JsonEncodedText", "JsonException", "JsonTokenType", "JsonReaderOptions", "JsonReaderState", "JsonSerializer", "JsonSerializerDefaults", "JsonSerializerOptions", "JsonWriterOptions", "Utf8JsonWriter"]
# endregion

# region: Imports
from System import Buffers
from System import IO
from System import Threading
from System.Collections import Generic
from System.Runtime import CompilerServices
from System.Runtime import Serialization
from System.Text.Encodings import Web
from System.Text.Json import Nodes
from System.Text.Json import Serialization
from System.Text.Json.Serialization import Metadata
from System.Threading import Tasks
from typing import overload
import enum
import System
# endregion

# region: System.Text.Json, Version=7.0.0.0

class JsonNamingPolicy(object):
    """    """
    @overload
    def ConvertName(self, name: str) -> str: ...
    @property
    def CamelCase(self) -> JsonNamingPolicy: ...

class JsonDocument(object):
    """    """
    @overload
    def Dispose() -> None: ...
    @property
    def RootElement(self) -> JsonElement: ...
    @overload
    @staticmethod
    def Parse(utf8Json: System.ReadOnlyMemory, options: JsonDocumentOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def Parse(utf8Json: Buffers.ReadOnlySequence, options: JsonDocumentOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def Parse(utf8Json: IO.Stream, options: JsonDocumentOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def Parse(json: System.ReadOnlyMemory, options: JsonDocumentOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def Parse(json: str, options: JsonDocumentOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def ParseAsync(utf8Json: IO.Stream, options: JsonDocumentOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def ParseValue() -> (JsonDocument, Utf8JsonReader): ...
    @overload
    @staticmethod
    def TryParseValue() -> (bool, Utf8JsonReader, JsonDocument): ...
    @overload
    def WriteTo(self, writer: Utf8JsonWriter) -> None: ...

class JsonDocumentOptions(System.ValueType):
    """    """
    @property
    def AllowTrailingCommas(self) -> bool: ...
    @property
    def CommentHandling(self) -> JsonCommentHandling: ...
    @property
    def MaxDepth(self) -> int: ...
    @AllowTrailingCommas.setter
    def AllowTrailingCommas(self, value: System.Void): ...
    @CommentHandling.setter
    def CommentHandling(self, value: System.Void): ...
    @MaxDepth.setter
    def MaxDepth(self, value: System.Void): ...

class JsonElement(System.ValueType):
    """    """
    @overload
    def Clone() -> JsonElement: ...
    @overload
    def EnumerateArray() -> ArrayEnumerator: ...
    @overload
    def EnumerateObject() -> ObjectEnumerator: ...
    @property
    def Item(self) -> JsonElement: ...
    @property
    def ValueKind(self) -> JsonValueKind: ...
    @overload
    def GetArrayLength() -> int: ...
    @overload
    def GetBoolean() -> bool: ...
    @overload
    def GetByte() -> System.Byte: ...
    @overload
    def GetBytesFromBase64() -> System.System.Array[System.Byte]: ...
    @overload
    def GetDateTime() -> System.DateTime: ...
    @overload
    def GetDateTimeOffset() -> System.DateTimeOffset: ...
    @overload
    def GetDecimal() -> System.Decimal: ...
    @overload
    def GetDouble() -> float: ...
    @overload
    def GetGuid() -> System.Guid: ...
    @overload
    def GetInt16() -> System.Int16: ...
    @overload
    def GetInt32() -> int: ...
    @overload
    def GetInt64() -> System.Int64: ...
    @overload
    def GetProperty(self, propertyName: System.ReadOnlySpan) -> JsonElement: ...
    @overload
    def GetProperty(self, propertyName: str) -> JsonElement: ...
    @overload
    def GetProperty(self, utf8PropertyName: System.ReadOnlySpan) -> JsonElement: ...
    @overload
    def GetRawText() -> str: ...
    @overload
    def GetSByte() -> System.SByte: ...
    @overload
    def GetSingle() -> System.Single: ...
    @overload
    def GetString() -> str: ...
    @overload
    def GetUInt16() -> System.UInt16: ...
    @overload
    def GetUInt32() -> System.UInt32: ...
    @overload
    def GetUInt64() -> System.UInt64: ...
    @overload
    @staticmethod
    def ParseValue() -> (JsonElement, Utf8JsonReader): ...
    @overload
    def ToString() -> str: ...
    @overload
    def TryGetByte() -> (bool, System.Byte): ...
    @overload
    def TryGetBytesFromBase64() -> (bool, System.System.Array[System.Byte]): ...
    @overload
    def TryGetDateTime() -> (bool, System.DateTime): ...
    @overload
    def TryGetDateTimeOffset() -> (bool, System.DateTimeOffset): ...
    @overload
    def TryGetDecimal() -> (bool, System.Decimal): ...
    @overload
    def TryGetDouble() -> (bool, float): ...
    @overload
    def TryGetGuid() -> (bool, System.Guid): ...
    @overload
    def TryGetInt16() -> (bool, System.Int16): ...
    @overload
    def TryGetInt32() -> (bool, int): ...
    @overload
    def TryGetInt64() -> (bool, System.Int64): ...
    @overload
    def TryGetProperty(self, propertyName: str) -> (bool, JsonElement): ...
    @overload
    def TryGetProperty(self, propertyName: System.ReadOnlySpan) -> (bool, JsonElement): ...
    @overload
    def TryGetProperty(self, utf8PropertyName: System.ReadOnlySpan) -> (bool, JsonElement): ...
    @overload
    def TryGetSByte() -> (bool, System.SByte): ...
    @overload
    def TryGetSingle() -> (bool, System.Single): ...
    @overload
    def TryGetUInt16() -> (bool, System.UInt16): ...
    @overload
    def TryGetUInt32() -> (bool, System.UInt32): ...
    @overload
    def TryGetUInt64() -> (bool, System.UInt64): ...
    @overload
    @staticmethod
    def TryParseValue() -> (bool, Utf8JsonReader, System.Nullable): ...
    @overload
    def ValueEquals(self, text: System.ReadOnlySpan) -> bool: ...
    @overload
    def ValueEquals(self, text: str) -> bool: ...
    @overload
    def ValueEquals(self, utf8Text: System.ReadOnlySpan) -> bool: ...
    @overload
    def WriteTo(self, writer: Utf8JsonWriter) -> None: ...

class ArrayEnumerator(System.ValueType):
    """    """
    @overload
    def Dispose() -> None: ...
    @property
    def Current(self) -> JsonElement: ...
    @overload
    def GetEnumerator() -> ArrayEnumerator: ...
    @overload
    def MoveNext() -> bool: ...
    @overload
    def Reset() -> None: ...

class ObjectEnumerator(System.ValueType):
    """    """
    @overload
    def Dispose() -> None: ...
    @property
    def Current(self) -> JsonProperty: ...
    @overload
    def GetEnumerator() -> ObjectEnumerator: ...
    @overload
    def MoveNext() -> bool: ...
    @overload
    def Reset() -> None: ...

class JsonProperty(System.ValueType):
    """    """
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> JsonElement: ...
    @overload
    def NameEquals(self, text: str) -> bool: ...
    @overload
    def NameEquals(self, utf8Text: System.ReadOnlySpan) -> bool: ...
    @overload
    def NameEquals(self, text: System.ReadOnlySpan) -> bool: ...
    @overload
    def ToString() -> str: ...
    @overload
    def WriteTo(self, writer: Utf8JsonWriter) -> None: ...

class JsonValueKind(enum.Enum):
    Undefined = 0
    Object = 1
    Array = 2
    String = 3
    Number = 4
    True_ = 5
    False_ = 6
    Null = 7

class JsonCommentHandling(enum.Enum):
    Disallow = 0
    Skip = 1
    Allow = 2

class JsonEncodedText(System.ValueType):
    """    """
    @overload
    @staticmethod
    def Encode(value: str, encoder: Web.JavaScriptEncoder) -> JsonEncodedText: ...
    @overload
    @staticmethod
    def Encode(value: System.ReadOnlySpan, encoder: Web.JavaScriptEncoder) -> JsonEncodedText: ...
    @overload
    @staticmethod
    def Encode(utf8Value: System.ReadOnlySpan, encoder: Web.JavaScriptEncoder) -> JsonEncodedText: ...
    @overload
    def Equals(self, other: JsonEncodedText) -> bool: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def EncodedUtf8Bytes(self) -> System.ReadOnlySpan: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class JsonException(System.Exception):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: System.Exception): ...
    @overload
    def __init__(self, message: str, path: str, lineNumber: System.Nullable, bytePositionInLine: System.Nullable): ...
    @overload
    def __init__(self, message: str, path: str, lineNumber: System.Nullable, bytePositionInLine: System.Nullable, innerException: System.Exception): ...
    @property
    def BytePositionInLine(self) -> System.Nullable: ...
    @property
    def LineNumber(self) -> System.Nullable: ...
    @property
    def Message(self) -> str: ...
    @property
    def Path(self) -> str: ...
    @overload
    def GetObjectData(self, info: Serialization.SerializationInfo, context: Serialization.StreamingContext) -> None: ...

class JsonTokenType(enum.Enum):
    None_ = 0
    StartObject = 1
    EndObject = 2
    StartArray = 3
    EndArray = 4
    PropertyName = 5
    Comment = 6
    String = 7
    Number = 8
    True_ = 9
    False_ = 10
    Null = 11

class JsonReaderOptions(System.ValueType):
    """    """
    @property
    def AllowTrailingCommas(self) -> bool: ...
    @property
    def CommentHandling(self) -> JsonCommentHandling: ...
    @property
    def MaxDepth(self) -> int: ...
    @AllowTrailingCommas.setter
    def AllowTrailingCommas(self, value: System.Void): ...
    @CommentHandling.setter
    def CommentHandling(self, value: System.Void): ...
    @MaxDepth.setter
    def MaxDepth(self, value: System.Void): ...

class JsonReaderState(System.ValueType):
    """    """
    def __init__(self, options: JsonReaderOptions): ...
    @property
    def Options(self) -> JsonReaderOptions: ...

class JsonSerializer(object):
    """    """
    @overload
    @staticmethod
    def Deserialize(document: JsonDocument, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: IO.Stream, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: IO.Stream, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: System.ReadOnlySpan, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: System.ReadOnlySpan, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(json: str, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(json: System.ReadOnlySpan, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(json: str, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(options: JsonSerializerOptions) -> (TValue, Utf8JsonReader): ...
    @overload
    @staticmethod
    def Deserialize(jsonTypeInfo: Metadata.JsonTypeInfo) -> (TValue, Utf8JsonReader): ...
    @overload
    @staticmethod
    def Deserialize(json: System.ReadOnlySpan, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(document: JsonDocument, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(node: Nodes.JsonNode, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(element: JsonElement, options: JsonSerializerOptions) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(node: Nodes.JsonNode, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(element: JsonElement, jsonTypeInfo: Metadata.JsonTypeInfo) -> TValue: ...
    @overload
    @staticmethod
    def Deserialize(node: Nodes.JsonNode, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(document: JsonDocument, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: IO.Stream, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: System.ReadOnlySpan, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(document: JsonDocument, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: System.ReadOnlySpan, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def Deserialize(element: JsonElement, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def Deserialize(json: System.ReadOnlySpan, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def Deserialize(element: JsonElement, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(utf8Json: IO.Stream, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(json: str, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(json: System.ReadOnlySpan, returnType: System.Type, context: Serialization.JsonSerializerContext) -> object: ...
    @overload
    @staticmethod
    def Deserialize(returnType: System.Type, options: JsonSerializerOptions) -> (object, Utf8JsonReader): ...
    @overload
    @staticmethod
    def Deserialize(node: Nodes.JsonNode, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def Deserialize(returnType: System.Type, context: Serialization.JsonSerializerContext) -> (object, Utf8JsonReader): ...
    @overload
    @staticmethod
    def Deserialize(json: str, returnType: System.Type, options: JsonSerializerOptions) -> object: ...
    @overload
    @staticmethod
    def DeserializeAsync(utf8Json: IO.Stream, options: JsonSerializerOptions, cancellationToken: Threading.CancellationToken) -> Tasks.ValueTask: ...
    @overload
    @staticmethod
    def DeserializeAsync(utf8Json: IO.Stream, jsonTypeInfo: Metadata.JsonTypeInfo, cancellationToken: Threading.CancellationToken) -> Tasks.ValueTask: ...
    @overload
    @staticmethod
    def DeserializeAsync(utf8Json: IO.Stream, returnType: System.Type, options: JsonSerializerOptions, cancellationToken: Threading.CancellationToken) -> Tasks.ValueTask: ...
    @overload
    @staticmethod
    def DeserializeAsync(utf8Json: IO.Stream, returnType: System.Type, context: Serialization.JsonSerializerContext, cancellationToken: Threading.CancellationToken) -> Tasks.ValueTask: ...
    @overload
    @staticmethod
    def DeserializeAsyncEnumerable(utf8Json: IO.Stream, jsonTypeInfo: Metadata.JsonTypeInfo, cancellationToken: Threading.CancellationToken) -> Generic.IAsyncEnumerable: ...
    @overload
    @staticmethod
    def DeserializeAsyncEnumerable(utf8Json: IO.Stream, options: JsonSerializerOptions, cancellationToken: Threading.CancellationToken) -> Generic.IAsyncEnumerable: ...
    @overload
    @staticmethod
    def Serialize(value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> str: ...
    @overload
    @staticmethod
    def Serialize(value: TValue, options: JsonSerializerOptions) -> str: ...
    @overload
    @staticmethod
    def Serialize(writer: Utf8JsonWriter, value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> None: ...
    @overload
    @staticmethod
    def Serialize(writer: Utf8JsonWriter, value: TValue, options: JsonSerializerOptions) -> None: ...
    @overload
    @staticmethod
    def Serialize(value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> str: ...
    @overload
    @staticmethod
    def Serialize(value: object, inputType: System.Type, options: JsonSerializerOptions) -> str: ...
    @overload
    @staticmethod
    def Serialize(utf8Json: IO.Stream, value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> None: ...
    @overload
    @staticmethod
    def Serialize(utf8Json: IO.Stream, value: TValue, options: JsonSerializerOptions) -> None: ...
    @overload
    @staticmethod
    def Serialize(utf8Json: IO.Stream, value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> None: ...
    @overload
    @staticmethod
    def Serialize(writer: Utf8JsonWriter, value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> None: ...
    @overload
    @staticmethod
    def Serialize(writer: Utf8JsonWriter, value: object, inputType: System.Type, options: JsonSerializerOptions) -> None: ...
    @overload
    @staticmethod
    def Serialize(utf8Json: IO.Stream, value: object, inputType: System.Type, options: JsonSerializerOptions) -> None: ...
    @overload
    @staticmethod
    def SerializeAsync(utf8Json: IO.Stream, value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def SerializeAsync(utf8Json: IO.Stream, value: TValue, options: JsonSerializerOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def SerializeAsync(utf8Json: IO.Stream, value: object, inputType: System.Type, context: Serialization.JsonSerializerContext, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def SerializeAsync(utf8Json: IO.Stream, value: object, inputType: System.Type, options: JsonSerializerOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def SerializeToDocument(value: TValue, options: JsonSerializerOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def SerializeToDocument(value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> JsonDocument: ...
    @overload
    @staticmethod
    def SerializeToDocument(value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> JsonDocument: ...
    @overload
    @staticmethod
    def SerializeToDocument(value: object, inputType: System.Type, options: JsonSerializerOptions) -> JsonDocument: ...
    @overload
    @staticmethod
    def SerializeToElement(value: TValue, options: JsonSerializerOptions) -> JsonElement: ...
    @overload
    @staticmethod
    def SerializeToElement(value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> JsonElement: ...
    @overload
    @staticmethod
    def SerializeToElement(value: object, inputType: System.Type, options: JsonSerializerOptions) -> JsonElement: ...
    @overload
    @staticmethod
    def SerializeToElement(value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> JsonElement: ...
    @overload
    @staticmethod
    def SerializeToNode(value: TValue, options: JsonSerializerOptions) -> Nodes.JsonNode: ...
    @overload
    @staticmethod
    def SerializeToNode(value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> Nodes.JsonNode: ...
    @overload
    @staticmethod
    def SerializeToNode(value: object, inputType: System.Type, options: JsonSerializerOptions) -> Nodes.JsonNode: ...
    @overload
    @staticmethod
    def SerializeToNode(value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> Nodes.JsonNode: ...
    @overload
    @staticmethod
    def SerializeToUtf8Bytes(value: TValue, jsonTypeInfo: Metadata.JsonTypeInfo) -> System.System.Array[System.Byte]: ...
    @overload
    @staticmethod
    def SerializeToUtf8Bytes(value: TValue, options: JsonSerializerOptions) -> System.System.Array[System.Byte]: ...
    @overload
    @staticmethod
    def SerializeToUtf8Bytes(value: object, inputType: System.Type, context: Serialization.JsonSerializerContext) -> System.System.Array[System.Byte]: ...
    @overload
    @staticmethod
    def SerializeToUtf8Bytes(value: object, inputType: System.Type, options: JsonSerializerOptions) -> System.System.Array[System.Byte]: ...

class JsonSerializerDefaults(enum.Enum):
    General = 0
    Web = 1

class JsonSerializerOptions(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, options: JsonSerializerOptions): ...
    @overload
    def __init__(self, defaults: JsonSerializerDefaults): ...
    @overload
    def AddContext() -> None: ...
    @property
    def AllowTrailingCommas(self) -> bool: ...
    @property
    def Converters(self) -> Generic.IList: ...
    @property
    def Default(self) -> JsonSerializerOptions: ...
    @property
    def DefaultBufferSize(self) -> int: ...
    @property
    def DefaultIgnoreCondition(self) -> Serialization.JsonIgnoreCondition: ...
    @property
    def DictionaryKeyPolicy(self) -> JsonNamingPolicy: ...
    @property
    def Encoder(self) -> Web.JavaScriptEncoder: ...
    @property
    def IgnoreNullValues(self) -> bool: ...
    @property
    def IgnoreReadOnlyFields(self) -> bool: ...
    @property
    def IgnoreReadOnlyProperties(self) -> bool: ...
    @property
    def IncludeFields(self) -> bool: ...
    @property
    def MaxDepth(self) -> int: ...
    @property
    def NumberHandling(self) -> Serialization.JsonNumberHandling: ...
    @property
    def PropertyNameCaseInsensitive(self) -> bool: ...
    @property
    def PropertyNamingPolicy(self) -> JsonNamingPolicy: ...
    @property
    def ReadCommentHandling(self) -> JsonCommentHandling: ...
    @property
    def ReferenceHandler(self) -> Serialization.ReferenceHandler: ...
    @property
    def TypeInfoResolver(self) -> Metadata.IJsonTypeInfoResolver: ...
    @property
    def UnknownTypeHandling(self) -> Serialization.JsonUnknownTypeHandling: ...
    @property
    def WriteIndented(self) -> bool: ...
    @overload
    def GetConverter(self, typeToConvert: System.Type) -> Serialization.JsonConverter: ...
    @overload
    def GetTypeInfo(self, type_: System.Type) -> Metadata.JsonTypeInfo: ...
    @AllowTrailingCommas.setter
    def AllowTrailingCommas(self, value: System.Void): ...
    @DefaultBufferSize.setter
    def DefaultBufferSize(self, value: System.Void): ...
    @DefaultIgnoreCondition.setter
    def DefaultIgnoreCondition(self, value: System.Void): ...
    @DictionaryKeyPolicy.setter
    def DictionaryKeyPolicy(self, value: System.Void): ...
    @Encoder.setter
    def Encoder(self, value: System.Void): ...
    @IgnoreNullValues.setter
    def IgnoreNullValues(self, value: System.Void): ...
    @IgnoreReadOnlyFields.setter
    def IgnoreReadOnlyFields(self, value: System.Void): ...
    @IgnoreReadOnlyProperties.setter
    def IgnoreReadOnlyProperties(self, value: System.Void): ...
    @IncludeFields.setter
    def IncludeFields(self, value: System.Void): ...
    @MaxDepth.setter
    def MaxDepth(self, value: System.Void): ...
    @NumberHandling.setter
    def NumberHandling(self, value: System.Void): ...
    @PropertyNameCaseInsensitive.setter
    def PropertyNameCaseInsensitive(self, value: System.Void): ...
    @PropertyNamingPolicy.setter
    def PropertyNamingPolicy(self, value: System.Void): ...
    @ReadCommentHandling.setter
    def ReadCommentHandling(self, value: System.Void): ...
    @ReferenceHandler.setter
    def ReferenceHandler(self, value: System.Void): ...
    @TypeInfoResolver.setter
    def TypeInfoResolver(self, value: System.Void): ...
    @UnknownTypeHandling.setter
    def UnknownTypeHandling(self, value: System.Void): ...
    @WriteIndented.setter
    def WriteIndented(self, value: System.Void): ...

class JsonWriterOptions(System.ValueType):
    """    """
    @property
    def Encoder(self) -> Web.JavaScriptEncoder: ...
    @property
    def Indented(self) -> bool: ...
    @property
    def MaxDepth(self) -> int: ...
    @property
    def SkipValidation(self) -> bool: ...
    @Encoder.setter
    def Encoder(self, value: System.Void): ...
    @Indented.setter
    def Indented(self, value: System.Void): ...
    @MaxDepth.setter
    def MaxDepth(self, value: System.Void): ...
    @SkipValidation.setter
    def SkipValidation(self, value: System.Void): ...

class Utf8JsonWriter(object):
    """    """
    @overload
    def __init__(self, bufferWriter: Buffers.IBufferWriter, options: JsonWriterOptions): ...
    @overload
    def __init__(self, utf8Json: IO.Stream, options: JsonWriterOptions): ...
    @overload
    def Dispose() -> None: ...
    @overload
    def DisposeAsync() -> Tasks.ValueTask: ...
    @overload
    def Flush() -> None: ...
    @overload
    def FlushAsync(self, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def BytesCommitted(self) -> System.Int64: ...
    @property
    def BytesPending(self) -> int: ...
    @property
    def CurrentDepth(self) -> int: ...
    @property
    def Options(self) -> JsonWriterOptions: ...
    @overload
    def Reset() -> None: ...
    @overload
    def Reset(self, utf8Json: IO.Stream) -> None: ...
    @overload
    def Reset(self, bufferWriter: Buffers.IBufferWriter) -> None: ...
    @overload
    def WriteBase64String(self, propertyName: JsonEncodedText, bytes_: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteBase64String(self, propertyName: str, bytes_: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteBase64String(self, propertyName: System.ReadOnlySpan, bytes_: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteBase64String(self, utf8PropertyName: System.ReadOnlySpan, bytes_: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteBase64StringValue(self, bytes_: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteBoolean(self, propertyName: JsonEncodedText, value: bool) -> None: ...
    @overload
    def WriteBoolean(self, utf8PropertyName: System.ReadOnlySpan, value: bool) -> None: ...
    @overload
    def WriteBoolean(self, propertyName: str, value: bool) -> None: ...
    @overload
    def WriteBoolean(self, propertyName: System.ReadOnlySpan, value: bool) -> None: ...
    @overload
    def WriteBooleanValue(self, value: bool) -> None: ...
    @overload
    def WriteCommentValue(self, utf8Value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteCommentValue(self, value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteCommentValue(self, value: str) -> None: ...
    @overload
    def WriteEndArray() -> None: ...
    @overload
    def WriteEndObject() -> None: ...
    @overload
    def WriteNull(self, utf8PropertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteNull(self, propertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteNull(self, propertyName: JsonEncodedText) -> None: ...
    @overload
    def WriteNull(self, propertyName: str) -> None: ...
    @overload
    def WriteNullValue() -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: int) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: System.UInt64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: int) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: int) -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: System.Int64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: System.Int64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: System.UInt64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: System.Int64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: System.UInt32) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: System.UInt32) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: System.UInt32) -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: System.UInt32) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: System.UInt64) -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: System.UInt64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: int) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: System.Int64) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: System.Decimal) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: System.Decimal) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: System.Decimal) -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: System.Decimal) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: float) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: float) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: float) -> None: ...
    @overload
    def WriteNumber(self, propertyName: JsonEncodedText, value: System.Single) -> None: ...
    @overload
    def WriteNumber(self, propertyName: str, value: System.Single) -> None: ...
    @overload
    def WriteNumber(self, propertyName: System.ReadOnlySpan, value: System.Single) -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: System.Single) -> None: ...
    @overload
    def WriteNumber(self, utf8PropertyName: System.ReadOnlySpan, value: float) -> None: ...
    @overload
    def WriteNumberValue(self, value: int) -> None: ...
    @overload
    def WriteNumberValue(self, value: float) -> None: ...
    @overload
    def WriteNumberValue(self, value: System.Decimal) -> None: ...
    @overload
    def WriteNumberValue(self, value: System.UInt64) -> None: ...
    @overload
    def WriteNumberValue(self, value: System.UInt32) -> None: ...
    @overload
    def WriteNumberValue(self, value: System.Single) -> None: ...
    @overload
    def WriteNumberValue(self, value: System.Int64) -> None: ...
    @overload
    def WritePropertyName(self, propertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WritePropertyName(self, propertyName: str) -> None: ...
    @overload
    def WritePropertyName(self, propertyName: JsonEncodedText) -> None: ...
    @overload
    def WritePropertyName(self, utf8PropertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteRawValue(self, utf8Json: System.ReadOnlySpan, skipInputValidation: bool) -> None: ...
    @overload
    def WriteRawValue(self, json: System.ReadOnlySpan, skipInputValidation: bool) -> None: ...
    @overload
    def WriteRawValue(self, json: str, skipInputValidation: bool) -> None: ...
    @overload
    def WriteStartArray() -> None: ...
    @overload
    def WriteStartArray(self, propertyName: JsonEncodedText) -> None: ...
    @overload
    def WriteStartArray(self, utf8PropertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteStartArray(self, propertyName: str) -> None: ...
    @overload
    def WriteStartArray(self, propertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteStartObject() -> None: ...
    @overload
    def WriteStartObject(self, propertyName: JsonEncodedText) -> None: ...
    @overload
    def WriteStartObject(self, utf8PropertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteStartObject(self, propertyName: str) -> None: ...
    @overload
    def WriteStartObject(self, propertyName: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: str, value: System.DateTime) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, value: System.DateTime) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, value: System.DateTime) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, value: JsonEncodedText) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, value: System.DateTimeOffset) -> None: ...
    @overload
    def WriteString(self, propertyName: str, value: System.Guid) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, value: System.Guid) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, value: System.DateTimeOffset) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, value: System.DateTimeOffset) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, value: JsonEncodedText) -> None: ...
    @overload
    def WriteString(self, propertyName: str, value: JsonEncodedText) -> None: ...
    @overload
    def WriteString(self, propertyName: str, value: str) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, utf8Value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, value: System.DateTime) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, value: str) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, value: System.Guid) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: JsonEncodedText, utf8Value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: str, value: System.DateTimeOffset) -> None: ...
    @overload
    def WriteString(self, utf8PropertyName: System.ReadOnlySpan, value: str) -> None: ...
    @overload
    def WriteString(self, propertyName: str, utf8Value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, utf8Value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, value: JsonEncodedText) -> None: ...
    @overload
    def WriteString(self, propertyName: str, value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, value: System.Guid) -> None: ...
    @overload
    def WriteString(self, propertyName: System.ReadOnlySpan, value: str) -> None: ...
    @overload
    def WriteStringValue(self, value: JsonEncodedText) -> None: ...
    @overload
    def WriteStringValue(self, value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteStringValue(self, value: str) -> None: ...
    @overload
    def WriteStringValue(self, value: System.DateTime) -> None: ...
    @overload
    def WriteStringValue(self, value: System.DateTimeOffset) -> None: ...
    @overload
    def WriteStringValue(self, utf8Value: System.ReadOnlySpan) -> None: ...
    @overload
    def WriteStringValue(self, value: System.Guid) -> None: ...

# endregion
