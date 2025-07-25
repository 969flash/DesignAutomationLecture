"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["BasicConsole", "CommandLine", "ConsoleHost", "ConsoleHostOptions", "ConsoleHostOptionsParser", "ConsoleOptions", "ICommandDispatcher", "IConsole", "InvalidOptionException", "OptionsParser", "Style", "SuperConsole", "Action"]
# endregion

# region: Imports
from Microsoft import Scripting
from Microsoft.Scripting import Hosting
from System import IO
from System import Text
from System.Collections import Generic
from System.Runtime import CompilerServices
from typing import overload
import enum
import System
# endregion

# region: Microsoft.Dynamic, Version=1.3.1.0

class BasicConsole(object):
    """    """
    def __init__(self, colorful: bool): ...
    @overload
    def Dispose() -> None: ...
    @property
    def ConsoleCancelEventHandler(self) -> System.ConsoleCancelEventHandler: ...
    @property
    def ErrorOutput(self) -> IO.TextWriter: ...
    @property
    def Output(self) -> IO.TextWriter: ...
    @overload
    def ReadLine(self, autoIndentSize: int) -> str: ...
    @ConsoleCancelEventHandler.setter
    def ConsoleCancelEventHandler(self, value: System.Void): ...
    @ErrorOutput.setter
    def ErrorOutput(self, value: System.Void): ...
    @Output.setter
    def Output(self, value: System.Void): ...
    @overload
    def Write(self, text: str, style: Style) -> None: ...
    @overload
    def WriteLine() -> None: ...
    @overload
    def WriteLine(self, text: str, style: Style) -> None: ...

class CommandLine(object):
    """    """
    def __init__(self): ...
    @property
    def ExitCode(self) -> int: ...
    @property
    def PromptContinuation(self) -> str: ...
    @property
    def ScriptScope(self) -> Hosting.ScriptScope: ...
    @overload
    def GetGlobals(self, name: str) -> Generic.IList: ...
    @overload
    def GetMemberNames(self, code: str) -> Generic.IList: ...
    @overload
    def Run(self, engine: Hosting.ScriptEngine, console: IConsole, options: ConsoleOptions) -> None: ...
    @overload
    def Terminate(self, exitCode: int) -> None: ...

class ConsoleHost(object):
    """    """
    @property
    def Engine(self) -> Hosting.ScriptEngine: ...
    @property
    def Options(self) -> ConsoleHostOptions: ...
    @property
    def Runtime(self) -> Hosting.ScriptRuntime: ...
    @property
    def RuntimeSetup(self) -> Hosting.ScriptRuntimeSetup: ...
    @overload
    def PrintLanguageHelp(self, output: Text.StringBuilder) -> None: ...
    @overload
    def Run(self, args: System.System.Array[str]) -> int: ...
    @overload
    def Terminate(self, exitCode: int) -> None: ...

class ConsoleHostOptions(object):
    """    """
    def __init__(self): ...
    @property
    def EnvironmentVars(self) -> Generic.List: ...
    @property
    def HasLanguageProvider(self) -> bool: ...
    @property
    def IgnoredArgs(self) -> Generic.List: ...
    @property
    def LanguageProvider(self) -> str: ...
    @property
    def RunAction(self) -> Action: ...
    @property
    def RunFile(self) -> str: ...
    @property
    def SourceUnitSearchPaths(self) -> System.System.Array[str]: ...
    @overload
    def GetHelp() -> System.System.Array[str]: ...
    @HasLanguageProvider.setter
    def HasLanguageProvider(self, value: System.Void): ...
    @LanguageProvider.setter
    def LanguageProvider(self, value: System.Void): ...
    @RunAction.setter
    def RunAction(self, value: System.Void): ...
    @RunFile.setter
    def RunFile(self, value: System.Void): ...
    @SourceUnitSearchPaths.setter
    def SourceUnitSearchPaths(self, value: System.Void): ...

class ConsoleHostOptionsParser(object):
    """    """
    def __init__(self, options: ConsoleHostOptions, runtimeSetup: Hosting.ScriptRuntimeSetup): ...
    @property
    def Options(self) -> ConsoleHostOptions: ...
    @property
    def RuntimeSetup(self) -> Hosting.ScriptRuntimeSetup: ...
    @overload
    def Parse(self, args: System.System.Array[str]) -> None: ...

class ConsoleOptions(object):
    """    """
    def __init__(self): ...
    @property
    def AutoIndent(self) -> bool: ...
    @property
    def AutoIndentSize(self) -> int: ...
    @property
    def ColorfulConsole(self) -> bool: ...
    @property
    def Command(self) -> str: ...
    @property
    def Exit(self) -> bool: ...
    @property
    def FileName(self) -> str: ...
    @property
    def HandleExceptions(self) -> bool: ...
    @property
    def Introspection(self) -> bool: ...
    @property
    def IsMta(self) -> bool: ...
    @property
    def PrintUsage(self) -> bool: ...
    @property
    def PrintVersion(self) -> bool: ...
    @property
    def RemainingArgs(self) -> System.System.Array[str]: ...
    @property
    def TabCompletion(self) -> bool: ...
    @AutoIndent.setter
    def AutoIndent(self, value: System.Void): ...
    @AutoIndentSize.setter
    def AutoIndentSize(self, value: System.Void): ...
    @ColorfulConsole.setter
    def ColorfulConsole(self, value: System.Void): ...
    @Command.setter
    def Command(self, value: System.Void): ...
    @Exit.setter
    def Exit(self, value: System.Void): ...
    @FileName.setter
    def FileName(self, value: System.Void): ...
    @HandleExceptions.setter
    def HandleExceptions(self, value: System.Void): ...
    @Introspection.setter
    def Introspection(self, value: System.Void): ...
    @IsMta.setter
    def IsMta(self, value: System.Void): ...
    @PrintUsage.setter
    def PrintUsage(self, value: System.Void): ...
    @PrintVersion.setter
    def PrintVersion(self, value: System.Void): ...
    @RemainingArgs.setter
    def RemainingArgs(self, value: System.Void): ...
    @TabCompletion.setter
    def TabCompletion(self, value: System.Void): ...

class ICommandDispatcher:
    """    """
    @overload
    def Execute(self, compiledCode: Hosting.CompiledCode, scope: Hosting.ScriptScope) -> object: ...

class IConsole:
    """    """
    @property
    def ErrorOutput(self) -> IO.TextWriter: ...
    @property
    def Output(self) -> IO.TextWriter: ...
    @overload
    def ReadLine(self, autoIndentSize: int) -> str: ...
    @ErrorOutput.setter
    def ErrorOutput(self, value: System.Void): ...
    @Output.setter
    def Output(self, value: System.Void): ...
    @overload
    def Write(self, text: str, style: Style) -> None: ...
    @overload
    def WriteLine() -> None: ...
    @overload
    def WriteLine(self, text: str, style: Style) -> None: ...

class InvalidOptionException(System.Exception):
    """    """
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: System.Exception): ...

class OptionsParser(object):
    """    """
    @property
    def CommonConsoleOptions(self) -> ConsoleOptions: ...
    @property
    def IgnoredArgs(self) -> Generic.IList: ...
    @property
    def LanguageSetup(self) -> Hosting.LanguageSetup: ...
    @property
    def Platform(self) -> Scripting.PlatformAdaptationLayer: ...
    @property
    def RuntimeSetup(self) -> Hosting.ScriptRuntimeSetup: ...
    @overload
    def GetHelp() -> (str, System.System.Array[str], System.System.Array[str], str): ...
    @overload
    def Parse(self, args: System.System.Array[str], setup: Hosting.ScriptRuntimeSetup, languageSetup: Hosting.LanguageSetup, platform: Scripting.PlatformAdaptationLayer) -> None: ...

class OptionsParser(OptionsParser):
    """    OptionsParser[TConsoleOptions]
    """
    def __init__(self): ...
    @property
    def CommonConsoleOptions(self) -> ConsoleOptions: ...
    @property
    def ConsoleOptions(self) -> TConsoleOptions: ...
    @overload
    def GetHelp() -> (str, System.System.Array[str], System.System.Array[str], str): ...
    @ConsoleOptions.setter
    def ConsoleOptions(self, value: System.Void): ...

class Style(enum.Enum):
    Prompt = 0
    Out = 1
    Error = 2
    Warning = 3

class SuperConsole(BasicConsole):
    """    """
    def __init__(self, commandLine: CommandLine, colorful: bool): ...
    @overload
    def ReadLine(self, autoIndentSize: int) -> str: ...

class Action(enum.Enum):
    None_ = 0
    RunConsole = 1
    RunFile = 2
    DisplayHelp = 3

# endregion
