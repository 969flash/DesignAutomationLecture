"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["JsonArray", "JsonNode", "JsonNodeOptions", "JsonObject", "JsonValue"]
# endregion

# region: Imports
from System import IO
from System.Collections import Generic
from System.Runtime import CompilerServices
from System.Text import Json
from System.Text.Json.Serialization import Metadata
from typing import overload
import System
# endregion

# region: System.Text.Json, Version=7.0.0.0

class JsonArray(JsonNode):
    """    """
    @overload
    def __init__(self, options: System.Nullable): ...
    @overload
    def __init__(self, items: System.Array[JsonNode]): ...
    @overload
    def __init__(self, options: JsonNodeOptions, items: System.Array[JsonNode]): ...
    @overload
    def Add(self, value: T) -> None: ...
    @overload
    def Add(self, item: JsonNode) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Contains(self, item: JsonNode) -> bool: ...
    @overload
    @staticmethod
    def Create(element: Json.JsonElement, options: System.Nullable) -> JsonArray: ...
    @property
    def Count(self) -> int: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def IndexOf(self, item: JsonNode) -> int: ...
    @overload
    def Insert(self, index: int, item: JsonNode) -> None: ...
    @overload
    def Remove(self, item: JsonNode) -> bool: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def WriteTo(self, writer: Json.Utf8JsonWriter, options: Json.JsonSerializerOptions) -> None: ...

class JsonNode(object):
    """    """
    @overload
    def AsArray() -> JsonArray: ...
    @overload
    def AsObject() -> JsonObject: ...
    @overload
    def AsValue() -> JsonValue: ...
    @property
    def Item(self) -> JsonNode: ...
    @property
    def Item(self) -> JsonNode: ...
    @property
    def Options(self) -> System.Nullable: ...
    @property
    def Parent(self) -> JsonNode: ...
    @property
    def Root(self) -> JsonNode: ...
    @overload
    def GetPath() -> str: ...
    @overload
    def GetValue() -> T: ...
    @overload
    @staticmethod
    def Parse(nodeOptions: System.Nullable) -> (JsonNode, Json.Utf8JsonReader): ...
    @overload
    @staticmethod
    def Parse(utf8Json: System.ReadOnlySpan, nodeOptions: System.Nullable, documentOptions: Json.JsonDocumentOptions) -> JsonNode: ...
    @overload
    @staticmethod
    def Parse(utf8Json: IO.Stream, nodeOptions: System.Nullable, documentOptions: Json.JsonDocumentOptions) -> JsonNode: ...
    @overload
    @staticmethod
    def Parse(json: str, nodeOptions: System.Nullable, documentOptions: Json.JsonDocumentOptions) -> JsonNode: ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @Item.setter
    def Item(self, value: System.Void): ...
    @overload
    def ToJsonString(self, options: Json.JsonSerializerOptions) -> str: ...
    @overload
    def ToString() -> str: ...
    @overload
    def WriteTo(self, writer: Json.Utf8JsonWriter, options: Json.JsonSerializerOptions) -> None: ...

class JsonNodeOptions(System.ValueType):
    """    """
    @property
    def PropertyNameCaseInsensitive(self) -> bool: ...
    @PropertyNameCaseInsensitive.setter
    def PropertyNameCaseInsensitive(self, value: System.Void): ...

class JsonObject(JsonNode):
    """    """
    @overload
    def __init__(self, options: System.Nullable): ...
    @overload
    def __init__(self, properties: Generic.IEnumerable, options: System.Nullable): ...
    @overload
    def Add(self, property_: Generic.KeyValuePair) -> None: ...
    @overload
    def Add(self, propertyName: str, value: JsonNode) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def ContainsKey(self, propertyName: str) -> bool: ...
    @overload
    @staticmethod
    def Create(element: Json.JsonElement, options: System.Nullable) -> JsonObject: ...
    @property
    def Count(self) -> int: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def Remove(self, propertyName: str) -> bool: ...
    @overload
    def TryGetPropertyValue(self, propertyName: str) -> (bool, JsonNode): ...
    @overload
    def WriteTo(self, writer: Json.Utf8JsonWriter, options: Json.JsonSerializerOptions) -> None: ...

class JsonValue(JsonNode):
    """    """
    @overload
    @staticmethod
    def Create(value: bool, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.SByte, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Single, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: str, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.UInt64, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: Json.JsonElement, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: T, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.UInt32, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Int64, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.UInt16, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: int, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Byte, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Char, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.DateTime, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.DateTimeOffset, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: float, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Guid, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Int16, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Nullable, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: System.Decimal, options: System.Nullable) -> JsonValue: ...
    @overload
    @staticmethod
    def Create(value: T, jsonTypeInfo: Metadata.JsonTypeInfo, options: System.Nullable) -> JsonValue: ...
    @overload
    def TryGetValue() -> (bool, T): ...

# endregion
