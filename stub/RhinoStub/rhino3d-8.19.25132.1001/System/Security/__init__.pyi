"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["Principal", "Claims"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Authentication"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Principal"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Policy", "AccessControl"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Authentication"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Cryptography"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Cryptography"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Authentication"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["AccessControl"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Cryptography"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Cryptography"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["AccessControl"]
# endregion

# region: Imports
from typing import overload
# endregion

# region: Exports
__all__ = ["Policy", "Permissions", "HostSecurityManager", "HostSecurityManagerOptions", "IEvidenceFactory", "ISecurityPolicyEncodable", "PolicyLevelType", "SecurityContextSource", "SecurityState", "SecurityZone", "XmlSyntaxException"]
# endregion

# region: Imports
from System import Reflection
from System.Runtime import CompilerServices
from System.Security import Policy
from typing import overload
import enum
import System
# endregion

# region: Exports
__all__ = ["SecureStringMarshal"]
# endregion

# region: Imports
from System.Runtime import CompilerServices
from typing import overload
import System
# endregion

# region: Exports
__all__ = ["Principal", "Permissions", "Cryptography", "AllowPartiallyTrustedCallersAttribute", "ISecurityEncodable", "PartialTrustVisibilityLevel", "SecureString", "SecurityCriticalAttribute", "SecurityElement", "SecurityException", "SecurityRulesAttribute", "SecurityRuleSet", "SecuritySafeCriticalAttribute", "SecurityTransparentAttribute", "SuppressUnmanagedCodeSecurityAttribute", "UnverifiableCodeAttribute", "VerificationException"]
# endregion

# region: Imports
from System import Collections
from System import Reflection
from System.Runtime import CompilerServices
from System.Runtime import Serialization
from typing import overload
import enum
import System
# endregion

# region: System.Private.CoreLib, Version=7.0.0.0

class AllowPartiallyTrustedCallersAttribute(System.Attribute):
    """    """
    def __init__(self): ...
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: System.Void): ...

class ISecurityEncodable:
    """    """
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def ToXml() -> SecurityElement: ...

class PartialTrustVisibilityLevel(enum.Enum):
    VisibleToAllHosts = 0
    NotVisibleByDefault = 1

class SecureString(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: System.Char, length: int): ...
    @overload
    def AppendChar(self, c: System.Char) -> None: ...
    @overload
    def Clear() -> None: ...
    @overload
    def Copy() -> SecureString: ...
    @overload
    def Dispose() -> None: ...
    @property
    def Length(self) -> int: ...
    @overload
    def InsertAt(self, index: int, c: System.Char) -> None: ...
    @overload
    def IsReadOnly() -> bool: ...
    @overload
    def MakeReadOnly() -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def SetAt(self, index: int, c: System.Char) -> None: ...

class SecurityCriticalAttribute(System.Attribute):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, scope: SecurityCriticalScope): ...
    @property
    def Scope(self) -> SecurityCriticalScope: ...

class SecurityElement(object):
    """    """
    @overload
    def __init__(self, tag: str): ...
    @overload
    def __init__(self, tag: str, text: str): ...
    @overload
    def AddAttribute(self, name: str, value: str) -> None: ...
    @overload
    def AddChild(self, child: SecurityElement) -> None: ...
    @overload
    def Attribute(self, name: str) -> str: ...
    @overload
    def Copy() -> SecurityElement: ...
    @overload
    def Equal(self, other: SecurityElement) -> bool: ...
    @overload
    @staticmethod
    def Escape(str_: str) -> str: ...
    @overload
    @staticmethod
    def FromString(xml: str) -> SecurityElement: ...
    @property
    def Attributes(self) -> Collections.Hashtable: ...
    @property
    def Children(self) -> Collections.ArrayList: ...
    @property
    def Tag(self) -> str: ...
    @property
    def Text(self) -> str: ...
    @overload
    @staticmethod
    def IsValidAttributeName(name: str) -> bool: ...
    @overload
    @staticmethod
    def IsValidAttributeValue(value: str) -> bool: ...
    @overload
    @staticmethod
    def IsValidTag(tag: str) -> bool: ...
    @overload
    @staticmethod
    def IsValidText(text: str) -> bool: ...
    @overload
    def SearchForChildByTag(self, tag: str) -> SecurityElement: ...
    @overload
    def SearchForTextOfTag(self, tag: str) -> str: ...
    @Attributes.setter
    def Attributes(self, value: System.Void): ...
    @Children.setter
    def Children(self, value: System.Void): ...
    @Tag.setter
    def Tag(self, value: System.Void): ...
    @Text.setter
    def Text(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class SecurityException(System.SystemException):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: System.Exception): ...
    @overload
    def __init__(self, message: str, type_: System.Type): ...
    @overload
    def __init__(self, message: str, type_: System.Type, state: str): ...
    @property
    def Demanded(self) -> object: ...
    @property
    def DenySetInstance(self) -> object: ...
    @property
    def FailedAssemblyInfo(self) -> Reflection.AssemblyName: ...
    @property
    def GrantedSet(self) -> str: ...
    @property
    def Method(self) -> Reflection.MethodInfo: ...
    @property
    def PermissionState(self) -> str: ...
    @property
    def PermissionType(self) -> System.Type: ...
    @property
    def PermitOnlySetInstance(self) -> object: ...
    @property
    def RefusedSet(self) -> str: ...
    @property
    def Url(self) -> str: ...
    @overload
    def GetObjectData(self, info: Serialization.SerializationInfo, context: Serialization.StreamingContext) -> None: ...
    @Demanded.setter
    def Demanded(self, value: System.Void): ...
    @DenySetInstance.setter
    def DenySetInstance(self, value: System.Void): ...
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: System.Void): ...
    @GrantedSet.setter
    def GrantedSet(self, value: System.Void): ...
    @Method.setter
    def Method(self, value: System.Void): ...
    @PermissionState.setter
    def PermissionState(self, value: System.Void): ...
    @PermissionType.setter
    def PermissionType(self, value: System.Void): ...
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: System.Void): ...
    @RefusedSet.setter
    def RefusedSet(self, value: System.Void): ...
    @Url.setter
    def Url(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...

class SecurityRulesAttribute(System.Attribute):
    """    """
    def __init__(self, ruleSet: SecurityRuleSet): ...
    @property
    def RuleSet(self) -> SecurityRuleSet: ...
    @property
    def SkipVerificationInFullTrust(self) -> bool: ...
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: System.Void): ...

class SecurityRuleSet(enum.Enum):
    None_ = 0
    Level1 = 1
    Level2 = 2

class SecuritySafeCriticalAttribute(System.Attribute):
    """    """
    def __init__(self): ...

class SecurityTransparentAttribute(System.Attribute):
    """    """
    def __init__(self): ...

class SuppressUnmanagedCodeSecurityAttribute(System.Attribute):
    """    """
    def __init__(self): ...

class UnverifiableCodeAttribute(System.Attribute):
    """    """
    def __init__(self): ...

class VerificationException(System.SystemException):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: System.Exception): ...

# endregion

# region: System.Runtime.InteropServices, Version=7.0.0.0

class SecureStringMarshal(object):
    """    """
    @overload
    @staticmethod
    def SecureStringToCoTaskMemAnsi(s: SecureString) -> System.IntPtr: ...
    @overload
    @staticmethod
    def SecureStringToCoTaskMemUnicode(s: SecureString) -> System.IntPtr: ...
    @overload
    @staticmethod
    def SecureStringToGlobalAllocAnsi(s: SecureString) -> System.IntPtr: ...
    @overload
    @staticmethod
    def SecureStringToGlobalAllocUnicode(s: SecureString) -> System.IntPtr: ...

# endregion

# region: System.Security.Permissions, Version=7.0.0.0

class HostSecurityManager(object):
    """    """
    def __init__(self): ...
    @overload
    def DetermineApplicationTrust(self, applicationEvidence: Policy.Evidence, activatorEvidence: Policy.Evidence, context: Policy.TrustManagerContext) -> Policy.ApplicationTrust: ...
    @overload
    def GenerateAppDomainEvidence(self, evidenceType: System.Type) -> Policy.EvidenceBase: ...
    @overload
    def GenerateAssemblyEvidence(self, evidenceType: System.Type, assembly: Reflection.Assembly) -> Policy.EvidenceBase: ...
    @property
    def DomainPolicy(self) -> Policy.PolicyLevel: ...
    @property
    def Flags(self) -> HostSecurityManagerOptions: ...
    @overload
    def GetHostSuppliedAppDomainEvidenceTypes() -> System.System.Array[System.Type]: ...
    @overload
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Reflection.Assembly) -> System.System.Array[System.Type]: ...
    @overload
    def ProvideAppDomainEvidence(self, inputEvidence: Policy.Evidence) -> Policy.Evidence: ...
    @overload
    def ProvideAssemblyEvidence(self, loadedAssembly: Reflection.Assembly, inputEvidence: Policy.Evidence) -> Policy.Evidence: ...

class HostSecurityManagerOptions(enum.Enum):
    None_ = 0
    HostAppDomainEvidence = 1
    HostPolicyLevel = 2
    HostAssemblyEvidence = 4
    HostDetermineApplicationTrust = 8
    HostResolvePolicy = 16
    AllFlags = 31

class IEvidenceFactory:
    """    """
    @property
    def Evidence(self) -> Policy.Evidence: ...

class ISecurityPolicyEncodable:
    """    """
    @overload
    def FromXml(self, e: SecurityElement, level: Policy.PolicyLevel) -> None: ...
    @overload
    def ToXml(self, level: Policy.PolicyLevel) -> SecurityElement: ...

class PolicyLevelType(enum.Enum):
    User = 0
    Machine = 1
    Enterprise = 2
    AppDomain = 3

class SecurityContextSource(enum.Enum):
    CurrentAppDomain = 0
    CurrentAssembly = 1

class SecurityState(object):
    """    """
    @overload
    def EnsureState() -> None: ...
    @overload
    def IsStateAvailable() -> bool: ...

class SecurityZone(enum.Enum):
    MyComputer = 0
    Intranet = 1
    Trusted = 2
    Internet = 3
    Untrusted = 4
    NoZone = -1

class XmlSyntaxException(System.SystemException):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, lineNumber: int): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, lineNumber: int, message: str): ...
    @overload
    def __init__(self, message: str, inner: System.Exception): ...

# endregion

