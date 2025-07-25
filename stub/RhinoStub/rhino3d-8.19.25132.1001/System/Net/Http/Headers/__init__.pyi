"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["AuthenticationHeaderValue", "CacheControlHeaderValue", "ContentDispositionHeaderValue", "ContentRangeHeaderValue", "EntityTagHeaderValue", "HeaderStringValues", "Enumerator", "HttpContentHeaders", "HttpHeaders", "HttpHeadersNonValidated", "HttpHeaderValueCollection", "HttpRequestHeaders", "HttpResponseHeaders", "MediaTypeHeaderValue", "MediaTypeWithQualityHeaderValue", "NameValueHeaderValue", "NameValueWithParametersHeaderValue", "ProductHeaderValue", "ProductInfoHeaderValue", "RangeConditionHeaderValue", "RangeHeaderValue", "RangeItemHeaderValue", "RetryConditionHeaderValue", "StringWithQualityHeaderValue", "TransferCodingHeaderValue", "TransferCodingWithQualityHeaderValue", "ViaHeaderValue", "WarningHeaderValue"]
# endregion

# region: Imports
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: System.Net.Http, Version=7.0.0.0

class AuthenticationHeaderValue(object):
    """    """
    @overload
    def __init__(self, scheme: str): ...
    @overload
    def __init__(self, scheme: str, parameter: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Parameter(self) -> str: ...
    @property
    def Scheme(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> AuthenticationHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, AuthenticationHeaderValue): ...

class CacheControlHeaderValue(object):
    """    """
    def __init__(self): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Extensions(self) -> Generic.ICollection: ...
    @property
    def MaxAge(self) -> System.Nullable: ...
    @property
    def MaxStale(self) -> bool: ...
    @property
    def MaxStaleLimit(self) -> System.Nullable: ...
    @property
    def MinFresh(self) -> System.Nullable: ...
    @property
    def MustRevalidate(self) -> bool: ...
    @property
    def NoCache(self) -> bool: ...
    @property
    def NoCacheHeaders(self) -> Generic.ICollection: ...
    @property
    def NoStore(self) -> bool: ...
    @property
    def NoTransform(self) -> bool: ...
    @property
    def OnlyIfCached(self) -> bool: ...
    @property
    def Private(self) -> bool: ...
    @property
    def PrivateHeaders(self) -> Generic.ICollection: ...
    @property
    def ProxyRevalidate(self) -> bool: ...
    @property
    def Public(self) -> bool: ...
    @property
    def SharedMaxAge(self) -> System.Nullable: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> CacheControlHeaderValue: ...
    @MaxAge.setter
    def MaxAge(self, value: System.Void): ...
    @MaxStale.setter
    def MaxStale(self, value: System.Void): ...
    @MaxStaleLimit.setter
    def MaxStaleLimit(self, value: System.Void): ...
    @MinFresh.setter
    def MinFresh(self, value: System.Void): ...
    @MustRevalidate.setter
    def MustRevalidate(self, value: System.Void): ...
    @NoCache.setter
    def NoCache(self, value: System.Void): ...
    @NoStore.setter
    def NoStore(self, value: System.Void): ...
    @NoTransform.setter
    def NoTransform(self, value: System.Void): ...
    @OnlyIfCached.setter
    def OnlyIfCached(self, value: System.Void): ...
    @Private.setter
    def Private(self, value: System.Void): ...
    @ProxyRevalidate.setter
    def ProxyRevalidate(self, value: System.Void): ...
    @Public.setter
    def Public(self, value: System.Void): ...
    @SharedMaxAge.setter
    def SharedMaxAge(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, CacheControlHeaderValue): ...

class ContentDispositionHeaderValue(object):
    """    """
    def __init__(self, dispositionType: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def CreationDate(self) -> System.Nullable: ...
    @property
    def DispositionType(self) -> str: ...
    @property
    def FileName(self) -> str: ...
    @property
    def FileNameStar(self) -> str: ...
    @property
    def ModificationDate(self) -> System.Nullable: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parameters(self) -> Generic.ICollection: ...
    @property
    def ReadDate(self) -> System.Nullable: ...
    @property
    def Size(self) -> System.Nullable: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> ContentDispositionHeaderValue: ...
    @CreationDate.setter
    def CreationDate(self, value: System.Void): ...
    @DispositionType.setter
    def DispositionType(self, value: System.Void): ...
    @FileName.setter
    def FileName(self, value: System.Void): ...
    @FileNameStar.setter
    def FileNameStar(self, value: System.Void): ...
    @ModificationDate.setter
    def ModificationDate(self, value: System.Void): ...
    @Name.setter
    def Name(self, value: System.Void): ...
    @ReadDate.setter
    def ReadDate(self, value: System.Void): ...
    @Size.setter
    def Size(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, ContentDispositionHeaderValue): ...

class ContentRangeHeaderValue(object):
    """    """
    @overload
    def __init__(self, length: System.Int64): ...
    @overload
    def __init__(self, from_: System.Int64, to: System.Int64): ...
    @overload
    def __init__(self, from_: System.Int64, to: System.Int64, length: System.Int64): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def From(self) -> System.Nullable: ...
    @property
    def HasLength(self) -> bool: ...
    @property
    def HasRange(self) -> bool: ...
    @property
    def Length(self) -> System.Nullable: ...
    @property
    def To(self) -> System.Nullable: ...
    @property
    def Unit(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> ContentRangeHeaderValue: ...
    @Unit.setter
    def Unit(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, ContentRangeHeaderValue): ...

class EntityTagHeaderValue(object):
    """    """
    @overload
    def __init__(self, tag: str): ...
    @overload
    def __init__(self, tag: str, isWeak: bool): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Any(self) -> EntityTagHeaderValue: ...
    @property
    def IsWeak(self) -> bool: ...
    @property
    def Tag(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> EntityTagHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, EntityTagHeaderValue): ...

class HeaderStringValues(System.ValueType):
    """    """
    @property
    def Count(self) -> int: ...
    @overload
    def GetEnumerator() -> Enumerator: ...
    @overload
    def ToString() -> str: ...

class Enumerator(System.ValueType):
    """    """
    @overload
    def Dispose() -> None: ...
    @property
    def Current(self) -> str: ...
    @overload
    def MoveNext() -> bool: ...

class HttpContentHeaders(HttpHeaders):
    """    """
    @property
    def Allow(self) -> Generic.ICollection: ...
    @property
    def ContentDisposition(self) -> ContentDispositionHeaderValue: ...
    @property
    def ContentEncoding(self) -> Generic.ICollection: ...
    @property
    def ContentLanguage(self) -> Generic.ICollection: ...
    @property
    def ContentLength(self) -> System.Nullable: ...
    @property
    def ContentLocation(self) -> System.Uri: ...
    @property
    def ContentMD5(self) -> System.System.Array[System.Byte]: ...
    @property
    def ContentRange(self) -> ContentRangeHeaderValue: ...
    @property
    def ContentType(self) -> MediaTypeHeaderValue: ...
    @property
    def Expires(self) -> System.Nullable: ...
    @property
    def LastModified(self) -> System.Nullable: ...
    @ContentDisposition.setter
    def ContentDisposition(self, value: System.Void): ...
    @ContentLength.setter
    def ContentLength(self, value: System.Void): ...
    @ContentLocation.setter
    def ContentLocation(self, value: System.Void): ...
    @ContentMD5.setter
    def ContentMD5(self, value: System.Void): ...
    @ContentRange.setter
    def ContentRange(self, value: System.Void): ...
    @ContentType.setter
    def ContentType(self, value: System.Void): ...
    @Expires.setter
    def Expires(self, value: System.Void): ...
    @LastModified.setter
    def LastModified(self, value: System.Void): ...

class HttpHeaders(object):
    """    """
    @overload
    def Add(self, name: str, value: str) -> None: ...
    @overload
    def Add(self, name: str, values: Generic.IEnumerable) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Contains(self, name: str) -> bool: ...
    @property
    def NonValidated(self) -> HttpHeadersNonValidated: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def GetValues(self, name: str) -> Generic.IEnumerable: ...
    @overload
    def Remove(self, name: str) -> bool: ...
    @overload
    def ToString() -> str: ...
    @overload
    def TryAddWithoutValidation(self, name: str, value: str) -> bool: ...
    @overload
    def TryAddWithoutValidation(self, name: str, values: Generic.IEnumerable) -> bool: ...
    @overload
    def TryGetValues(self, name: str) -> (bool, Generic.IEnumerable): ...

class HttpHeadersNonValidated(System.ValueType):
    """    """
    @overload
    def Contains(self, headerName: str) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> HeaderStringValues: ...
    @overload
    def GetEnumerator() -> Enumerator: ...
    @overload
    def TryGetValues(self, headerName: str) -> (bool, HeaderStringValues): ...

class Enumerator(System.ValueType):
    """    """
    @overload
    def Dispose() -> None: ...
    @property
    def Current(self) -> Generic.KeyValuePair: ...
    @overload
    def MoveNext() -> bool: ...

class HttpHeaderValueCollection(object):
    """    HttpHeaderValueCollection[T]
    """
    @overload
    def Add(self, item: T) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Contains(self, item: T) -> bool: ...
    @overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @overload
    def GetEnumerator() -> Generic.IEnumerator: ...
    @overload
    def ParseAdd(self, input_: str) -> None: ...
    @overload
    def Remove(self, item: T) -> bool: ...
    @overload
    def ToString() -> str: ...
    @overload
    def TryParseAdd(self, input_: str) -> bool: ...

class HttpRequestHeaders(HttpHeaders):
    """    """
    @property
    def Accept(self) -> HttpHeaderValueCollection: ...
    @property
    def AcceptCharset(self) -> HttpHeaderValueCollection: ...
    @property
    def AcceptEncoding(self) -> HttpHeaderValueCollection: ...
    @property
    def AcceptLanguage(self) -> HttpHeaderValueCollection: ...
    @property
    def Authorization(self) -> AuthenticationHeaderValue: ...
    @property
    def CacheControl(self) -> CacheControlHeaderValue: ...
    @property
    def Connection(self) -> HttpHeaderValueCollection: ...
    @property
    def ConnectionClose(self) -> System.Nullable: ...
    @property
    def Date(self) -> System.Nullable: ...
    @property
    def Expect(self) -> HttpHeaderValueCollection: ...
    @property
    def ExpectContinue(self) -> System.Nullable: ...
    @property
    def From(self) -> str: ...
    @property
    def Host(self) -> str: ...
    @property
    def IfMatch(self) -> HttpHeaderValueCollection: ...
    @property
    def IfModifiedSince(self) -> System.Nullable: ...
    @property
    def IfNoneMatch(self) -> HttpHeaderValueCollection: ...
    @property
    def IfRange(self) -> RangeConditionHeaderValue: ...
    @property
    def IfUnmodifiedSince(self) -> System.Nullable: ...
    @property
    def MaxForwards(self) -> System.Nullable: ...
    @property
    def Pragma(self) -> HttpHeaderValueCollection: ...
    @property
    def Protocol(self) -> str: ...
    @property
    def ProxyAuthorization(self) -> AuthenticationHeaderValue: ...
    @property
    def Range(self) -> RangeHeaderValue: ...
    @property
    def Referrer(self) -> System.Uri: ...
    @property
    def TE(self) -> HttpHeaderValueCollection: ...
    @property
    def Trailer(self) -> HttpHeaderValueCollection: ...
    @property
    def TransferEncoding(self) -> HttpHeaderValueCollection: ...
    @property
    def TransferEncodingChunked(self) -> System.Nullable: ...
    @property
    def Upgrade(self) -> HttpHeaderValueCollection: ...
    @property
    def UserAgent(self) -> HttpHeaderValueCollection: ...
    @property
    def Via(self) -> HttpHeaderValueCollection: ...
    @property
    def Warning(self) -> HttpHeaderValueCollection: ...
    @Authorization.setter
    def Authorization(self, value: System.Void): ...
    @CacheControl.setter
    def CacheControl(self, value: System.Void): ...
    @ConnectionClose.setter
    def ConnectionClose(self, value: System.Void): ...
    @Date.setter
    def Date(self, value: System.Void): ...
    @ExpectContinue.setter
    def ExpectContinue(self, value: System.Void): ...
    @From.setter
    def From(self, value: System.Void): ...
    @Host.setter
    def Host(self, value: System.Void): ...
    @IfModifiedSince.setter
    def IfModifiedSince(self, value: System.Void): ...
    @IfRange.setter
    def IfRange(self, value: System.Void): ...
    @IfUnmodifiedSince.setter
    def IfUnmodifiedSince(self, value: System.Void): ...
    @MaxForwards.setter
    def MaxForwards(self, value: System.Void): ...
    @Protocol.setter
    def Protocol(self, value: System.Void): ...
    @ProxyAuthorization.setter
    def ProxyAuthorization(self, value: System.Void): ...
    @Range.setter
    def Range(self, value: System.Void): ...
    @Referrer.setter
    def Referrer(self, value: System.Void): ...
    @TransferEncodingChunked.setter
    def TransferEncodingChunked(self, value: System.Void): ...

class HttpResponseHeaders(HttpHeaders):
    """    """
    @property
    def AcceptRanges(self) -> HttpHeaderValueCollection: ...
    @property
    def Age(self) -> System.Nullable: ...
    @property
    def CacheControl(self) -> CacheControlHeaderValue: ...
    @property
    def Connection(self) -> HttpHeaderValueCollection: ...
    @property
    def ConnectionClose(self) -> System.Nullable: ...
    @property
    def Date(self) -> System.Nullable: ...
    @property
    def ETag(self) -> EntityTagHeaderValue: ...
    @property
    def Location(self) -> System.Uri: ...
    @property
    def Pragma(self) -> HttpHeaderValueCollection: ...
    @property
    def ProxyAuthenticate(self) -> HttpHeaderValueCollection: ...
    @property
    def RetryAfter(self) -> RetryConditionHeaderValue: ...
    @property
    def Server(self) -> HttpHeaderValueCollection: ...
    @property
    def Trailer(self) -> HttpHeaderValueCollection: ...
    @property
    def TransferEncoding(self) -> HttpHeaderValueCollection: ...
    @property
    def TransferEncodingChunked(self) -> System.Nullable: ...
    @property
    def Upgrade(self) -> HttpHeaderValueCollection: ...
    @property
    def Vary(self) -> HttpHeaderValueCollection: ...
    @property
    def Via(self) -> HttpHeaderValueCollection: ...
    @property
    def Warning(self) -> HttpHeaderValueCollection: ...
    @property
    def WwwAuthenticate(self) -> HttpHeaderValueCollection: ...
    @Age.setter
    def Age(self, value: System.Void): ...
    @CacheControl.setter
    def CacheControl(self, value: System.Void): ...
    @ConnectionClose.setter
    def ConnectionClose(self, value: System.Void): ...
    @Date.setter
    def Date(self, value: System.Void): ...
    @ETag.setter
    def ETag(self, value: System.Void): ...
    @Location.setter
    def Location(self, value: System.Void): ...
    @RetryAfter.setter
    def RetryAfter(self, value: System.Void): ...
    @TransferEncodingChunked.setter
    def TransferEncodingChunked(self, value: System.Void): ...

class MediaTypeHeaderValue(object):
    """    """
    @overload
    def __init__(self, mediaType: str): ...
    @overload
    def __init__(self, mediaType: str, charSet: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def CharSet(self) -> str: ...
    @property
    def MediaType(self) -> str: ...
    @property
    def Parameters(self) -> Generic.ICollection: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> MediaTypeHeaderValue: ...
    @CharSet.setter
    def CharSet(self, value: System.Void): ...
    @MediaType.setter
    def MediaType(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, MediaTypeHeaderValue): ...

class MediaTypeWithQualityHeaderValue(MediaTypeHeaderValue):
    """    """
    @overload
    def __init__(self, mediaType: str): ...
    @overload
    def __init__(self, mediaType: str, quality: float): ...
    @property
    def Quality(self) -> System.Nullable: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> MediaTypeWithQualityHeaderValue: ...
    @Quality.setter
    def Quality(self, value: System.Void): ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, MediaTypeWithQualityHeaderValue): ...

class NameValueHeaderValue(object):
    """    """
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, value: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> NameValueHeaderValue: ...
    @Value.setter
    def Value(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, NameValueHeaderValue): ...

class NameValueWithParametersHeaderValue(NameValueHeaderValue):
    """    """
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, value: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Parameters(self) -> Generic.ICollection: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> NameValueWithParametersHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, NameValueWithParametersHeaderValue): ...

class ProductHeaderValue(object):
    """    """
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, version: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> ProductHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, ProductHeaderValue): ...

class ProductInfoHeaderValue(object):
    """    """
    @overload
    def __init__(self, product: ProductHeaderValue): ...
    @overload
    def __init__(self, comment: str): ...
    @overload
    def __init__(self, productName: str, productVersion: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Comment(self) -> str: ...
    @property
    def Product(self) -> ProductHeaderValue: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> ProductInfoHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, ProductInfoHeaderValue): ...

class RangeConditionHeaderValue(object):
    """    """
    @overload
    def __init__(self, date: System.DateTimeOffset): ...
    @overload
    def __init__(self, entityTag: EntityTagHeaderValue): ...
    @overload
    def __init__(self, entityTag: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Date(self) -> System.Nullable: ...
    @property
    def EntityTag(self) -> EntityTagHeaderValue: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> RangeConditionHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, RangeConditionHeaderValue): ...

class RangeHeaderValue(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, from_: System.Nullable, to: System.Nullable): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Ranges(self) -> Generic.ICollection: ...
    @property
    def Unit(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> RangeHeaderValue: ...
    @Unit.setter
    def Unit(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, RangeHeaderValue): ...

class RangeItemHeaderValue(object):
    """    """
    def __init__(self, from_: System.Nullable, to: System.Nullable): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def From(self) -> System.Nullable: ...
    @property
    def To(self) -> System.Nullable: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    def ToString() -> str: ...

class RetryConditionHeaderValue(object):
    """    """
    @overload
    def __init__(self, date: System.DateTimeOffset): ...
    @overload
    def __init__(self, delta: System.TimeSpan): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Date(self) -> System.Nullable: ...
    @property
    def Delta(self) -> System.Nullable: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> RetryConditionHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, RetryConditionHeaderValue): ...

class StringWithQualityHeaderValue(object):
    """    """
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, value: str, quality: float): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Quality(self) -> System.Nullable: ...
    @property
    def Value(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> StringWithQualityHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, StringWithQualityHeaderValue): ...

class TransferCodingHeaderValue(object):
    """    """
    def __init__(self, value: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Parameters(self) -> Generic.ICollection: ...
    @property
    def Value(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> TransferCodingHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, TransferCodingHeaderValue): ...

class TransferCodingWithQualityHeaderValue(TransferCodingHeaderValue):
    """    """
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, value: str, quality: float): ...
    @property
    def Quality(self) -> System.Nullable: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> TransferCodingWithQualityHeaderValue: ...
    @Quality.setter
    def Quality(self, value: System.Void): ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, TransferCodingWithQualityHeaderValue): ...

class ViaHeaderValue(object):
    """    """
    @overload
    def __init__(self, protocolVersion: str, receivedBy: str): ...
    @overload
    def __init__(self, protocolVersion: str, receivedBy: str, protocolName: str): ...
    @overload
    def __init__(self, protocolVersion: str, receivedBy: str, protocolName: str, comment: str): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Comment(self) -> str: ...
    @property
    def ProtocolName(self) -> str: ...
    @property
    def ProtocolVersion(self) -> str: ...
    @property
    def ReceivedBy(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> ViaHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, ViaHeaderValue): ...

class WarningHeaderValue(object):
    """    """
    @overload
    def __init__(self, code: int, agent: str, text: str): ...
    @overload
    def __init__(self, code: int, agent: str, text: str, date: System.DateTimeOffset): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def Agent(self) -> str: ...
    @property
    def Code(self) -> int: ...
    @property
    def Date(self) -> System.Nullable: ...
    @property
    def Text(self) -> str: ...
    @overload
    def GetHashCode() -> int: ...
    @overload
    @staticmethod
    def Parse(input_: str) -> WarningHeaderValue: ...
    @overload
    def ToString() -> str: ...
    @overload
    @staticmethod
    def TryParse(input_: str) -> (bool, WarningHeaderValue): ...

# endregion
