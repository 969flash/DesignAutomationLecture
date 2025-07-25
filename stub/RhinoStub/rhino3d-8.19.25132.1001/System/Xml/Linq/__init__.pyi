"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Extensions", "XAttribute", "XCData", "XComment", "XContainer", "XDeclaration", "XDocument", "XDocumentType", "XElement", "XObjectChange", "LoadOptions", "SaveOptions", "ReaderOptions", "XName", "XNamespace", "XNode", "XNodeDocumentOrderComparer", "XNodeEqualityComparer", "XObject", "XObjectChangeEventArgs", "XProcessingInstruction", "XStreamingElement", "XText"]
# endregion

# region: Imports
from System import IO
from System import Threading
from System import Xml
from System.Collections import Generic
from System.Runtime import CompilerServices
from System.Threading import Tasks
from typing import overload
import enum
import System
# endregion

# region: System.Private.Xml.Linq, Version=7.0.0.0

class Extensions(object):
    """    """
    @overload
    @staticmethod
    def Ancestors(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Ancestors(source: Generic.IEnumerable, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def AncestorsAndSelf(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def AncestorsAndSelf(source: Generic.IEnumerable, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Attributes(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Attributes(source: Generic.IEnumerable, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def DescendantNodes(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def DescendantNodesAndSelf(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Descendants(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Descendants(source: Generic.IEnumerable, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def DescendantsAndSelf(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def DescendantsAndSelf(source: Generic.IEnumerable, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Elements(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Elements(source: Generic.IEnumerable, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def InDocumentOrder(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Nodes(source: Generic.IEnumerable) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def Remove(source: Generic.IEnumerable) -> None: ...
    @overload
    @staticmethod
    def Remove(source: Generic.IEnumerable) -> None: ...

class XAttribute(XObject):
    """    """
    @overload
    def __init__(self, other: XAttribute): ...
    @overload
    def __init__(self, name: XName, value: object): ...
    @property
    def EmptySequence(self) -> Generic.IEnumerable: ...
    @property
    def IsNamespaceDeclaration(self) -> bool: ...
    @property
    def Name(self) -> XName: ...
    @property
    def NextAttribute(self) -> XAttribute: ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def PreviousAttribute(self) -> XAttribute: ...
    @property
    def Value(self) -> str: ...
    @overload
    def Remove() -> None: ...
    @Value.setter
    def Value(self, value: System.Void): ...
    @overload
    def SetValue(self, value: object) -> None: ...
    @overload
    def ToString() -> str: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XCData(XText):
    """    """
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, other: XCData): ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XComment(XNode):
    """    """
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, other: XComment): ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def Value(self) -> str: ...
    @Value.setter
    def Value(self, value: System.Void): ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XContainer(XNode):
    """    """
    @overload
    def Add(self, content: object) -> None: ...
    @overload
    def Add(self, content: System.System.Array[object]) -> None: ...
    @overload
    def AddFirst(self, content: object) -> None: ...
    @overload
    def AddFirst(self, content: System.System.Array[object]) -> None: ...
    @overload
    def CreateWriter() -> Xml.XmlWriter: ...
    @overload
    def DescendantNodes() -> Generic.IEnumerable: ...
    @overload
    def Descendants() -> Generic.IEnumerable: ...
    @overload
    def Descendants(self, name: XName) -> Generic.IEnumerable: ...
    @overload
    def Element(self, name: XName) -> XElement: ...
    @overload
    def Elements() -> Generic.IEnumerable: ...
    @overload
    def Elements(self, name: XName) -> Generic.IEnumerable: ...
    @property
    def FirstNode(self) -> XNode: ...
    @property
    def LastNode(self) -> XNode: ...
    @overload
    def Nodes() -> Generic.IEnumerable: ...
    @overload
    def RemoveNodes() -> None: ...
    @overload
    def ReplaceNodes(self, content: object) -> None: ...
    @overload
    def ReplaceNodes(self, content: System.System.Array[object]) -> None: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XDeclaration(object):
    """    """
    @overload
    def __init__(self, other: XDeclaration): ...
    @overload
    def __init__(self, version: str, encoding: str, standalone: str): ...
    @property
    def Encoding(self) -> str: ...
    @property
    def Standalone(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @Encoding.setter
    def Encoding(self, value: System.Void): ...
    @Standalone.setter
    def Standalone(self, value: System.Void): ...
    @Version.setter
    def Version(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class XDocument(XContainer):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, content: System.System.Array[object]): ...
    @overload
    def __init__(self, other: XDocument): ...
    @overload
    def __init__(self, declaration: XDeclaration, content: System.System.Array[object]): ...
    @property
    def Declaration(self) -> XDeclaration: ...
    @property
    def DocumentType(self) -> XDocumentType: ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def Root(self) -> XElement: ...
    @overload
    @staticmethod
    def Load(uri: str) -> XDocument: ...
    @overload
    @staticmethod
    def Load(stream: IO.Stream) -> XDocument: ...
    @overload
    @staticmethod
    def Load(textReader: IO.TextReader) -> XDocument: ...
    @overload
    @staticmethod
    def Load(reader: Xml.XmlReader) -> XDocument: ...
    @overload
    @staticmethod
    def Load(uri: str, options: LoadOptions) -> XDocument: ...
    @overload
    @staticmethod
    def Load(stream: IO.Stream, options: LoadOptions) -> XDocument: ...
    @overload
    @staticmethod
    def Load(textReader: IO.TextReader, options: LoadOptions) -> XDocument: ...
    @overload
    @staticmethod
    def Load(reader: Xml.XmlReader, options: LoadOptions) -> XDocument: ...
    @overload
    @staticmethod
    def LoadAsync(stream: IO.Stream, options: LoadOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def LoadAsync(textReader: IO.TextReader, options: LoadOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def LoadAsync(reader: Xml.XmlReader, options: LoadOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def Parse(text: str) -> XDocument: ...
    @overload
    @staticmethod
    def Parse(text: str, options: LoadOptions) -> XDocument: ...
    @overload
    def Save(self, fileName: str) -> None: ...
    @overload
    def Save(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def Save(self, textWriter: IO.TextWriter) -> None: ...
    @overload
    def Save(self, stream: IO.Stream) -> None: ...
    @overload
    def Save(self, textWriter: IO.TextWriter, options: SaveOptions) -> None: ...
    @overload
    def Save(self, fileName: str, options: SaveOptions) -> None: ...
    @overload
    def Save(self, stream: IO.Stream, options: SaveOptions) -> None: ...
    @overload
    def SaveAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    def SaveAsync(self, stream: IO.Stream, options: SaveOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    def SaveAsync(self, textWriter: IO.TextWriter, options: SaveOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @Declaration.setter
    def Declaration(self, value: System.Void): ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XDocumentType(XNode):
    """    """
    @overload
    def __init__(self, other: XDocumentType): ...
    @overload
    def __init__(self, name: str, publicId: str, systemId: str, internalSubset: str): ...
    @property
    def InternalSubset(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def PublicId(self) -> str: ...
    @property
    def SystemId(self) -> str: ...
    @InternalSubset.setter
    def InternalSubset(self, value: System.Void): ...
    @Name.setter
    def Name(self, value: System.Void): ...
    @PublicId.setter
    def PublicId(self, value: System.Void): ...
    @SystemId.setter
    def SystemId(self, value: System.Void): ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XElement(XContainer):
    """    """
    @overload
    def __init__(self, name: XName): ...
    @overload
    def __init__(self, other: XElement): ...
    @overload
    def __init__(self, other: XStreamingElement): ...
    @overload
    def __init__(self, name: XName, content: object): ...
    @overload
    def __init__(self, name: XName, content: System.System.Array[object]): ...
    @overload
    def AncestorsAndSelf() -> Generic.IEnumerable: ...
    @overload
    def AncestorsAndSelf(self, name: XName) -> Generic.IEnumerable: ...
    @overload
    def Attribute(self, name: XName) -> XAttribute: ...
    @overload
    def Attributes() -> Generic.IEnumerable: ...
    @overload
    def Attributes(self, name: XName) -> Generic.IEnumerable: ...
    @overload
    def DescendantNodesAndSelf() -> Generic.IEnumerable: ...
    @overload
    def DescendantsAndSelf() -> Generic.IEnumerable: ...
    @overload
    def DescendantsAndSelf(self, name: XName) -> Generic.IEnumerable: ...
    @property
    def EmptySequence(self) -> Generic.IEnumerable: ...
    @property
    def FirstAttribute(self) -> XAttribute: ...
    @property
    def HasAttributes(self) -> bool: ...
    @property
    def HasElements(self) -> bool: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def LastAttribute(self) -> XAttribute: ...
    @property
    def Name(self) -> XName: ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def Value(self) -> str: ...
    @overload
    def GetDefaultNamespace() -> XNamespace: ...
    @overload
    def GetNamespaceOfPrefix(self, prefix: str) -> XNamespace: ...
    @overload
    def GetPrefixOfNamespace(self, ns: XNamespace) -> str: ...
    @overload
    @staticmethod
    def Load(uri: str) -> XElement: ...
    @overload
    @staticmethod
    def Load(stream: IO.Stream) -> XElement: ...
    @overload
    @staticmethod
    def Load(reader: Xml.XmlReader) -> XElement: ...
    @overload
    @staticmethod
    def Load(textReader: IO.TextReader) -> XElement: ...
    @overload
    @staticmethod
    def Load(uri: str, options: LoadOptions) -> XElement: ...
    @overload
    @staticmethod
    def Load(stream: IO.Stream, options: LoadOptions) -> XElement: ...
    @overload
    @staticmethod
    def Load(reader: Xml.XmlReader, options: LoadOptions) -> XElement: ...
    @overload
    @staticmethod
    def Load(textReader: IO.TextReader, options: LoadOptions) -> XElement: ...
    @overload
    @staticmethod
    def LoadAsync(stream: IO.Stream, options: LoadOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def LoadAsync(textReader: IO.TextReader, options: LoadOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def LoadAsync(reader: Xml.XmlReader, options: LoadOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    @staticmethod
    def Parse(text: str) -> XElement: ...
    @overload
    @staticmethod
    def Parse(text: str, options: LoadOptions) -> XElement: ...
    @overload
    def RemoveAll() -> None: ...
    @overload
    def RemoveAttributes() -> None: ...
    @overload
    def ReplaceAll(self, content: System.System.Array[object]) -> None: ...
    @overload
    def ReplaceAll(self, content: object) -> None: ...
    @overload
    def ReplaceAttributes(self, content: System.System.Array[object]) -> None: ...
    @overload
    def ReplaceAttributes(self, content: object) -> None: ...
    @overload
    def Save(self, fileName: str) -> None: ...
    @overload
    def Save(self, stream: IO.Stream) -> None: ...
    @overload
    def Save(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def Save(self, textWriter: IO.TextWriter) -> None: ...
    @overload
    def Save(self, textWriter: IO.TextWriter, options: SaveOptions) -> None: ...
    @overload
    def Save(self, stream: IO.Stream, options: SaveOptions) -> None: ...
    @overload
    def Save(self, fileName: str, options: SaveOptions) -> None: ...
    @overload
    def SaveAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    def SaveAsync(self, stream: IO.Stream, options: SaveOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    def SaveAsync(self, textWriter: IO.TextWriter, options: SaveOptions, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @Name.setter
    def Name(self, value: System.Void): ...
    @Value.setter
    def Value(self, value: System.Void): ...
    @overload
    def SetAttributeValue(self, name: XName, value: object) -> None: ...
    @overload
    def SetElementValue(self, name: XName, value: object) -> None: ...
    @overload
    def SetValue(self, value: object) -> None: ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XObjectChange(enum.Enum):
    Add = 0
    Remove = 1
    Name = 2
    Value = 3

class LoadOptions(enum.Enum):
    None_ = 0
    PreserveWhitespace = 1
    SetBaseUri = 2
    SetLineInfo = 4

class SaveOptions(enum.Enum):
    None_ = 0
    DisableFormatting = 1
    OmitDuplicateNamespaces = 2

class ReaderOptions(enum.Enum):
    None_ = 0
    OmitDuplicateNamespaces = 1

class XName(object):
    """    """
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def LocalName(self) -> str: ...
    @property
    def Namespace(self) -> XNamespace: ...
    @property
    def NamespaceName(self) -> str: ...
    @overload
    @staticmethod
    def Get(expandedName: str) -> XName: ...
    @overload
    @staticmethod
    def Get(localName: str, namespaceName: str) -> XName: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class XNamespace(object):
    """    """
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def NamespaceName(self) -> str: ...
    @property
    def None_(self) -> XNamespace: ...
    @overload
    @staticmethod
    def Get(namespaceName: str) -> XNamespace: ...
    @property
    def Xml(self) -> XNamespace: ...
    @property
    def Xmlns(self) -> XNamespace: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def GetName(self, localName: str) -> XName: ...
    @overload
    def ToString() -> str: ...

class XNode(XObject):
    """    """
    @overload
    def AddAfterSelf(self, content: object) -> None: ...
    @overload
    def AddAfterSelf(self, content: System.System.Array[object]) -> None: ...
    @overload
    def AddBeforeSelf(self, content: object) -> None: ...
    @overload
    def AddBeforeSelf(self, content: System.System.Array[object]) -> None: ...
    @overload
    def Ancestors() -> Generic.IEnumerable: ...
    @overload
    def Ancestors(self, name: XName) -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def CompareDocumentOrder(n1: XNode, n2: XNode) -> int: ...
    @overload
    def CreateReader() -> Xml.XmlReader: ...
    @overload
    def CreateReader(self, readerOptions: ReaderOptions) -> Xml.XmlReader: ...
    @overload
    @staticmethod
    def DeepEquals(n1: XNode, n2: XNode) -> bool: ...
    @overload
    def ElementsAfterSelf() -> Generic.IEnumerable: ...
    @overload
    def ElementsAfterSelf(self, name: XName) -> Generic.IEnumerable: ...
    @overload
    def ElementsBeforeSelf() -> Generic.IEnumerable: ...
    @overload
    def ElementsBeforeSelf(self, name: XName) -> Generic.IEnumerable: ...
    @property
    def DocumentOrderComparer(self) -> XNodeDocumentOrderComparer: ...
    @property
    def EqualityComparer(self) -> XNodeEqualityComparer: ...
    @property
    def NextNode(self) -> XNode: ...
    @property
    def PreviousNode(self) -> XNode: ...
    @overload
    def IsAfter(self, node: XNode) -> bool: ...
    @overload
    def IsBefore(self, node: XNode) -> bool: ...
    @overload
    def NodesAfterSelf() -> Generic.IEnumerable: ...
    @overload
    def NodesBeforeSelf() -> Generic.IEnumerable: ...
    @overload
    @staticmethod
    def ReadFrom(reader: Xml.XmlReader) -> XNode: ...
    @overload
    @staticmethod
    def ReadFromAsync(reader: Xml.XmlReader, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @overload
    def Remove() -> None: ...
    @overload
    def ReplaceWith(self, content: object) -> None: ...
    @overload
    def ReplaceWith(self, content: System.System.Array[object]) -> None: ...
    @overload
    def ToString() -> str: ...
    @overload
    def ToString(self, options: SaveOptions) -> str: ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XNodeDocumentOrderComparer(object):
    """    """
    def __init__(self): ...
    @overload
    def Compare(self, x: XNode, y: XNode) -> int: ...

class XNodeEqualityComparer(object):
    """    """
    def __init__(self): ...
    @overload
    def Equals(self, x: XNode, y: XNode) -> bool: ...
    @overload
    def GetHashCode(self, obj: XNode) -> int: ...

class XObject(object):
    """    """
    @overload
    def AddAnnotation(self, annotation: object) -> None: ...
    @overload
    def Annotation() -> T: ...
    @overload
    def Annotation(self, type_: System.Type) -> object: ...
    @overload
    def Annotations() -> Generic.IEnumerable: ...
    @overload
    def Annotations(self, type_: System.Type) -> Generic.IEnumerable: ...
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @overload
    def RemoveAnnotations() -> None: ...
    @overload
    def RemoveAnnotations(self, type_: System.Type) -> None: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XObjectChangeEventArgs(System.EventArgs):
    """    """
    def __init__(self, objectChange: XObjectChange): ...
    @property
    def Add(self) -> XObjectChangeEventArgs: ...
    @property
    def Remove(self) -> XObjectChangeEventArgs: ...
    @property
    def Name(self) -> XObjectChangeEventArgs: ...
    @property
    def Value(self) -> XObjectChangeEventArgs: ...
    @property
    def ObjectChange(self) -> XObjectChange: ...

class XProcessingInstruction(XNode):
    """    """
    @overload
    def __init__(self, other: XProcessingInstruction): ...
    @overload
    def __init__(self, target: str, data: str): ...
    @property
    def Data(self) -> str: ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def Target(self) -> str: ...
    @Data.setter
    def Data(self, value: System.Void): ...
    @Target.setter
    def Target(self, value: System.Void): ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

class XStreamingElement(object):
    """    """
    @overload
    def __init__(self, name: XName): ...
    @overload
    def __init__(self, name: XName, content: object): ...
    @overload
    def __init__(self, name: XName, content: System.System.Array[object]): ...
    @overload
    def Add(self, content: object) -> None: ...
    @overload
    def Add(self, content: System.System.Array[object]) -> None: ...
    @property
    def Name(self) -> XName: ...
    @overload
    def Save(self, textWriter: IO.TextWriter) -> None: ...
    @overload
    def Save(self, fileName: str) -> None: ...
    @overload
    def Save(self, stream: IO.Stream) -> None: ...
    @overload
    def Save(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def Save(self, stream: IO.Stream, options: SaveOptions) -> None: ...
    @overload
    def Save(self, textWriter: IO.TextWriter, options: SaveOptions) -> None: ...
    @overload
    def Save(self, fileName: str, options: SaveOptions) -> None: ...
    @Name.setter
    def Name(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    def ToString(self, options: SaveOptions) -> str: ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...

class XText(XNode):
    """    """
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, other: XText): ...
    @property
    def NodeType(self) -> Xml.XmlNodeType: ...
    @property
    def Value(self) -> str: ...
    @Value.setter
    def Value(self, value: System.Void): ...
    @overload
    def WriteTo(self, writer: Xml.XmlWriter) -> None: ...
    @overload
    def WriteToAsync(self, writer: Xml.XmlWriter, cancellationToken: Threading.CancellationToken) -> Tasks.Task: ...
    @property
    def Changed(self): ...
    @property
    def Changing(self): ...

# endregion
