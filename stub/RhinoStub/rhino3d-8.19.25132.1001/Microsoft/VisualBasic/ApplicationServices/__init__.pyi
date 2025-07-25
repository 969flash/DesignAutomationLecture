"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["ApplicationBase", "ApplyApplicationDefaultsEventArgs", "AssemblyInfo", "CantStartSingleInstanceException", "ConsoleApplicationBase", "NoStartupFormException", "StartupEventArgs", "StartupNextInstanceEventArgs", "UnhandledExceptionEventArgs", "User", "AuthenticationMode", "ShutdownMode", "ApplyApplicationDefaultsEventHandler", "StartupEventHandler", "StartupNextInstanceEventHandler", "ShutdownEventHandler", "UnhandledExceptionEventHandler", "WindowsFormsApplicationBase"]
# endregion

# region: Imports
from Microsoft.VisualBasic import Logging
from System import ComponentModel
from System import Drawing
from System import Globalization
from System import Reflection
from System import Threading
from System.Collections import ObjectModel
from System.Runtime import CompilerServices
from System.Security import Principal
from System.Windows import Forms
from typing import overload
import enum
import System
# endregion

# region: Microsoft.VisualBasic.Forms, Version=7.0.0.0

class ApplicationBase(object):
    """    """
    def __init__(self): ...
    @overload
    def ChangeCulture(self, cultureName: str) -> None: ...
    @overload
    def ChangeUICulture(self, cultureName: str) -> None: ...
    @property
    def Culture(self) -> Globalization.CultureInfo: ...
    @property
    def Info(self) -> AssemblyInfo: ...
    @property
    def Log(self) -> Logging.Log: ...
    @property
    def UICulture(self) -> Globalization.CultureInfo: ...
    @overload
    def GetEnvironmentVariable(self, name: str) -> str: ...

class ApplyApplicationDefaultsEventArgs(System.EventArgs):
    """    """
    @property
    def Font(self) -> Drawing.Font: ...
    @property
    def HighDpiMode(self) -> Forms.HighDpiMode: ...
    @property
    def MinimumSplashScreenDisplayTime(self) -> int: ...
    @Font.setter
    def Font(self, value: System.Void): ...
    @HighDpiMode.setter
    def HighDpiMode(self, value: System.Void): ...
    @MinimumSplashScreenDisplayTime.setter
    def MinimumSplashScreenDisplayTime(self, value: System.Void): ...

class AssemblyInfo(object):
    """    """
    def __init__(self, currentAssembly: Reflection.Assembly): ...
    @property
    def AssemblyName(self) -> str: ...
    @property
    def CompanyName(self) -> str: ...
    @property
    def Copyright(self) -> str: ...
    @property
    def Description(self) -> str: ...
    @property
    def DirectoryPath(self) -> str: ...
    @property
    def LoadedAssemblies(self) -> ObjectModel.ReadOnlyCollection: ...
    @property
    def ProductName(self) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def Title(self) -> str: ...
    @property
    def Trademark(self) -> str: ...
    @property
    def Version(self) -> System.Version: ...
    @property
    def WorkingSet(self) -> System.Int64: ...

class CantStartSingleInstanceException(System.Exception):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: System.Exception): ...

class ConsoleApplicationBase(ApplicationBase):
    """    """
    def __init__(self): ...
    @property
    def CommandLineArgs(self) -> ObjectModel.ReadOnlyCollection: ...

class NoStartupFormException(System.Exception):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: System.Exception): ...

class StartupEventArgs(ComponentModel.CancelEventArgs):
    """    """
    def __init__(self, args: ObjectModel.ReadOnlyCollection): ...
    @property
    def CommandLine(self) -> ObjectModel.ReadOnlyCollection: ...

class StartupNextInstanceEventArgs(System.EventArgs):
    """    """
    def __init__(self, args: ObjectModel.ReadOnlyCollection, bringToForegroundFlag: bool): ...
    @property
    def BringToForeground(self) -> bool: ...
    @property
    def CommandLine(self) -> ObjectModel.ReadOnlyCollection: ...
    @BringToForeground.setter
    def BringToForeground(self, value: System.Void): ...

class UnhandledExceptionEventArgs(Threading.ThreadExceptionEventArgs):
    """    """
    def __init__(self, exitApplication: bool, exception: System.Exception): ...
    @property
    def ExitApplication(self) -> bool: ...
    @ExitApplication.setter
    def ExitApplication(self, value: System.Void): ...

class User(object):
    """    """
    def __init__(self): ...
    @property
    def CurrentPrincipal(self) -> Principal.IPrincipal: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @overload
    def IsInRole(self, role: str) -> bool: ...
    @CurrentPrincipal.setter
    def CurrentPrincipal(self, value: System.Void): ...

class AuthenticationMode(enum.Enum):
    Windows = 0
    ApplicationDefined = 1

class ShutdownMode(enum.Enum):
    AfterMainFormCloses = 0
    AfterAllFormsClose = 1

class ApplyApplicationDefaultsEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: ApplyApplicationDefaultsEventArgs, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: ApplyApplicationDefaultsEventArgs) -> None: ...

class StartupEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: StartupEventArgs, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: StartupEventArgs) -> None: ...

class StartupNextInstanceEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: StartupNextInstanceEventArgs, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: StartupNextInstanceEventArgs) -> None: ...

class ShutdownEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: System.EventArgs, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: System.EventArgs) -> None: ...

class UnhandledExceptionEventHandler(System.MulticastDelegate):
    """    """
    def __init__(self, TargetObject: object, TargetMethod: System.IntPtr): ...
    @overload
    def BeginInvoke(self, sender: object, e: UnhandledExceptionEventArgs, DelegateCallback: System.AsyncCallback, DelegateAsyncState: object) -> System.IAsyncResult: ...
    @overload
    def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
    @overload
    def Invoke(self, sender: object, e: UnhandledExceptionEventArgs) -> None: ...

class WindowsFormsApplicationBase(ConsoleApplicationBase):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, authenticationMode: AuthenticationMode): ...
    @overload
    def DoEvents() -> None: ...
    @property
    def ApplicationContext(self) -> Forms.ApplicationContext: ...
    @property
    def MinimumSplashScreenDisplayTime(self) -> int: ...
    @property
    def OpenForms(self) -> Forms.FormCollection: ...
    @property
    def SaveMySettingsOnExit(self) -> bool: ...
    @property
    def SplashScreen(self) -> Forms.Form: ...
    @overload
    def Run(self, commandLine: System.System.Array[str]) -> None: ...
    @MinimumSplashScreenDisplayTime.setter
    def MinimumSplashScreenDisplayTime(self, value: System.Void): ...
    @SaveMySettingsOnExit.setter
    def SaveMySettingsOnExit(self, value: System.Void): ...
    @SplashScreen.setter
    def SplashScreen(self, value: System.Void): ...
    @property
    def ApplyApplicationDefaults(self): ...
    @property
    def Startup(self): ...
    @property
    def StartupNextInstance(self): ...
    @property
    def Shutdown(self): ...
    @property
    def NetworkAvailabilityChanged(self): ...
    @property
    def UnhandledException(self): ...

# endregion
