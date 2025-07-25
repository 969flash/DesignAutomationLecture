"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["LogFileLocation", "LogFileCreationScheduleOption", "DiskSpaceExhaustedOption", "FileLogTraceListener", "Log"]
# endregion

# region: Imports
from System import Diagnostics
from System import Text
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: Microsoft.VisualBasic.Forms, Version=7.0.0.0

class LogFileLocation(enum.Enum):
    TempDirectory = 0
    LocalUserApplicationDirectory = 1
    CommonApplicationDirectory = 2
    ExecutableDirectory = 3
    Custom = 4

class LogFileCreationScheduleOption(enum.Enum):
    None_ = 0
    Daily = 1
    Weekly = 2

class DiskSpaceExhaustedOption(enum.Enum):
    ThrowException = 0
    DiscardMessages = 1

class FileLogTraceListener(Diagnostics.TraceListener):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @overload
    def Close() -> None: ...
    @overload
    def Flush() -> None: ...
    @property
    def Append(self) -> bool: ...
    @property
    def AutoFlush(self) -> bool: ...
    @property
    def BaseFileName(self) -> str: ...
    @property
    def CustomLocation(self) -> str: ...
    @property
    def Delimiter(self) -> str: ...
    @property
    def DiskSpaceExhaustedBehavior(self) -> DiskSpaceExhaustedOption: ...
    @property
    def Encoding(self) -> Text.Encoding: ...
    @property
    def FullLogFileName(self) -> str: ...
    @property
    def IncludeHostName(self) -> bool: ...
    @property
    def Location(self) -> LogFileLocation: ...
    @property
    def LogFileCreationSchedule(self) -> LogFileCreationScheduleOption: ...
    @property
    def MaxFileSize(self) -> System.Int64: ...
    @property
    def ReserveDiskSpace(self) -> System.Int64: ...
    @Append.setter
    def Append(self, value: System.Void): ...
    @AutoFlush.setter
    def AutoFlush(self, value: System.Void): ...
    @BaseFileName.setter
    def BaseFileName(self, value: System.Void): ...
    @CustomLocation.setter
    def CustomLocation(self, value: System.Void): ...
    @Delimiter.setter
    def Delimiter(self, value: System.Void): ...
    @DiskSpaceExhaustedBehavior.setter
    def DiskSpaceExhaustedBehavior(self, value: System.Void): ...
    @Encoding.setter
    def Encoding(self, value: System.Void): ...
    @IncludeHostName.setter
    def IncludeHostName(self, value: System.Void): ...
    @Location.setter
    def Location(self, value: System.Void): ...
    @LogFileCreationSchedule.setter
    def LogFileCreationSchedule(self, value: System.Void): ...
    @MaxFileSize.setter
    def MaxFileSize(self, value: System.Void): ...
    @ReserveDiskSpace.setter
    def ReserveDiskSpace(self, value: System.Void): ...
    @overload
    def TraceData(self, eventCache: Diagnostics.TraceEventCache, source: str, eventType: Diagnostics.TraceEventType, id_: int, data: System.System.Array[object]) -> None: ...
    @overload
    def TraceData(self, eventCache: Diagnostics.TraceEventCache, source: str, eventType: Diagnostics.TraceEventType, id_: int, data: object) -> None: ...
    @overload
    def TraceEvent(self, eventCache: Diagnostics.TraceEventCache, source: str, eventType: Diagnostics.TraceEventType, id_: int, message: str) -> None: ...
    @overload
    def TraceEvent(self, eventCache: Diagnostics.TraceEventCache, source: str, eventType: Diagnostics.TraceEventType, id_: int, format_: str, args: System.System.Array[object]) -> None: ...
    @overload
    def Write(self, message: str) -> None: ...
    @overload
    def WriteLine(self, message: str) -> None: ...

class Log(object):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @property
    def DefaultFileLogWriter(self) -> FileLogTraceListener: ...
    @property
    def TraceSource(self) -> Diagnostics.TraceSource: ...
    @overload
    def WriteEntry(self, message: str) -> None: ...
    @overload
    def WriteEntry(self, message: str, severity: Diagnostics.TraceEventType) -> None: ...
    @overload
    def WriteEntry(self, message: str, severity: Diagnostics.TraceEventType, id_: int) -> None: ...
    @overload
    def WriteException(self, ex: System.Exception) -> None: ...
    @overload
    def WriteException(self, ex: System.Exception, severity: Diagnostics.TraceEventType, additionalInfo: str) -> None: ...
    @overload
    def WriteException(self, ex: System.Exception, severity: Diagnostics.TraceEventType, additionalInfo: str, id_: int) -> None: ...

# endregion
