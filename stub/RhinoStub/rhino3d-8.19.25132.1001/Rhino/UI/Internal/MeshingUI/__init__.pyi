"""this file is auto-generated by rhinocode stubmaker. do not make changes"""

# region: Exports
__all__ = ["MeshParametersStyle", "MeshingStyleListViewModel", "MeshSettingsViewModel", "PageStyle"]
# endregion

# region: Imports
from Eto import Drawing
from Eto import Forms
from Rhino import Commands
from Rhino import Geometry
from Rhino import UI
from System.Collections import ObjectModel
from System.Runtime import CompilerServices
from typing import overload
import enum
import Rhino
import System
# endregion

# region: Rhino.UI, Version=8.19.25132.1001

class MeshParametersStyle(UI.ViewModel):
    """    """
    def __init__(self, id_: System.Guid, name: str, inputParams: Geometry.MeshingParameters, detailed: bool): ...
    @property
    def Custom(self) -> System.Guid: ...
    @property
    def Deleted(self) -> bool: ...
    @property
    def Detailed(self) -> bool: ...
    @property
    def Id(self) -> System.Guid: ...
    @property
    def Image(self) -> Drawing.Image: ...
    @property
    def IsCustom(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSeparator(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parameters(self) -> Geometry.MeshingParameters: ...
    @property
    def RhinoDefaults(self) -> System.Guid: ...
    @property
    def RhinoJaggedAndFast(self) -> System.Guid: ...
    @property
    def RhinoSmoothAndSlower(self) -> System.Guid: ...
    @property
    def SeparatorId(self) -> System.Guid: ...
    @Deleted.setter
    def Deleted(self, value: System.Void): ...
    @Detailed.setter
    def Detailed(self, value: System.Void): ...
    @Name.setter
    def Name(self, value: System.Void): ...
    @Parameters.setter
    def Parameters(self, value: System.Void): ...
    @overload
    def ToString() -> str: ...
    @property
    def PropertyChanged(self): ...
    @property
    def ModleUnitsChanged(self): ...
    @property
    def PageUnitsChanged(self): ...

class MeshingStyleListViewModel(UI.ViewModel):
    """    """
    def __init__(self, document: Rhino.RhinoDoc, input_mp: Geometry.MeshingParameters, bDetailedView: bool): ...
    @overload
    def AddStyle(self, style: MeshParametersStyle) -> bool: ...
    @overload
    def DeleteStyle(self, style: MeshParametersStyle) -> bool: ...
    @overload
    def DeleteStyleFromSettings(self, styleToDelete: MeshParametersStyle) -> None: ...
    @overload
    def EditStyle(self, style: MeshParametersStyle) -> bool: ...
    @overload
    def FindStyle(self, guid: System.Guid) -> MeshParametersStyle: ...
    @overload
    def FindStyleGuid(self, name: str, mp: Geometry.MeshingParameters) -> System.Guid: ...
    @overload
    def FindStyleGuidByName(self, name: str) -> System.Guid: ...
    @property
    def Document(self) -> Rhino.RhinoDoc: ...
    @property
    def MeshParameters(self) -> Geometry.MeshingParameters: ...
    @property
    def OriginalDetailedView(self) -> bool: ...
    @property
    def OriginalMeshParameters(self) -> Geometry.MeshingParameters: ...
    @property
    def SelectedStyle(self) -> MeshParametersStyle: ...
    @property
    def SelectedStyleId(self) -> System.Guid: ...
    @overload
    def RetrievePresetListFromSettings() -> ObjectModel.ObservableCollection: ...
    @overload
    def RetrieveStyleListFromFile(self, fileName: str) -> bool: ...
    @overload
    def SavePresetListToFile(self, fileName: str) -> bool: ...
    @overload
    def SavePresetListToSettings() -> None: ...
    @MeshParameters.setter
    def MeshParameters(self, value: System.Void): ...
    @SelectedStyle.setter
    def SelectedStyle(self, value: System.Void): ...
    @SelectedStyleId.setter
    def SelectedStyleId(self, value: System.Void): ...
    @property
    def SelectedStyleChanged(self): ...
    @property
    def PropertyChanged(self): ...
    @property
    def ModleUnitsChanged(self): ...
    @property
    def PageUnitsChanged(self): ...

class MeshSettingsViewModel(UI.ViewModel):
    """    """
    def __init__(self, docSn: System.UInt32, pageStyle: PageStyle, inputMp: Geometry.MeshingParameters, mode: int): ...
    @overload
    def AddPreset(self, style: MeshParametersStyle) -> bool: ...
    @overload
    def AddPresetToPersistentPresets(self, preset: MeshParametersStyle) -> bool: ...
    @overload
    def Defaults() -> None: ...
    @overload
    def DeletePreset(self, style: MeshParametersStyle) -> bool: ...
    @overload
    def DeletePresetFromPersistentSettings(self, styleToDelete: MeshParametersStyle) -> None: ...
    @overload
    def DeletePresetMenuClick() -> None: ...
    @overload
    def ExportPresetMenuClick() -> None: ...
    @overload
    def FindPresetAndSelectedIndex() -> None: ...
    @overload
    def FindPresetByName(self, name: str) -> System.Guid: ...
    @overload
    def FindPresetFromGuid(self, guid: System.Guid) -> MeshParametersStyle: ...
    @property
    def CancelAnalysisPreviewChanges(self) -> bool: ...
    @property
    def ChangedValueColor(self) -> Drawing.Color: ...
    @property
    def DefaultControlColor(self) -> Drawing.Color: ...
    @property
    def Density(self) -> float: ...
    @property
    def DensityChanged(self) -> bool: ...
    @property
    def DensityColor(self) -> Drawing.Color: ...
    @property
    def Detailed(self) -> bool: ...
    @property
    def DetailedOrSimpleChanged(self) -> bool: ...
    @property
    def DetailedOrSimpleColor(self) -> Drawing.Color: ...
    @property
    def DetailedOrSimpleText(self) -> str: ...
    @property
    def Document(self) -> Rhino.RhinoDoc: ...
    @property
    def EnablePreview(self) -> bool: ...
    @property
    def JaggedSeams(self) -> bool: ...
    @property
    def JaggedSeamsChanged(self) -> bool: ...
    @property
    def JaggedSeamsColor(self) -> Drawing.Color: ...
    @property
    def LabelDefaultColor(self) -> Drawing.Color: ...
    @property
    def MaxDistanceEdgeToSurface(self) -> float: ...
    @property
    def MaxDistanceEdgeToSurfaceChanged(self) -> bool: ...
    @property
    def MaxDistanceEdgeToSurfaceColor(self) -> Drawing.Color: ...
    @property
    def MaximumAngle(self) -> float: ...
    @property
    def MaximumAngleChanged(self) -> bool: ...
    @property
    def MaximumAngleColor(self) -> Drawing.Color: ...
    @property
    def MaximumAspectRatio(self) -> float: ...
    @property
    def MaximumAspectRatioChanged(self) -> bool: ...
    @property
    def MaximumAspectRatioColor(self) -> Drawing.Color: ...
    @property
    def MaximumEdgeLength(self) -> float: ...
    @property
    def MaximumEdgeLengthChanged(self) -> bool: ...
    @property
    def MaximumEdgeLengthColor(self) -> Drawing.Color: ...
    @property
    def MeshParameters(self) -> Geometry.MeshingParameters: ...
    @property
    def MinimumEdgeLength(self) -> float: ...
    @property
    def MinimumEdgeLengthChanged(self) -> bool: ...
    @property
    def MinimumEdgeLengthColor(self) -> Drawing.Color: ...
    @property
    def MinimumInitialGridQuads(self) -> int: ...
    @property
    def MinimumInitialGridQuadsChanged(self) -> bool: ...
    @property
    def MinimumInitialGridQuadsColor(self) -> Drawing.Color: ...
    @property
    def NurbsMeshingSliderPosition(self) -> int: ...
    @property
    def OriginalDetailedView(self) -> bool: ...
    @property
    def OriginalMeshParameters(self) -> Geometry.MeshingParameters: ...
    @property
    def PackTextures(self) -> bool: ...
    @property
    def PackTexturesChanged(self) -> bool: ...
    @property
    def PackTexturesColor(self) -> Drawing.Color: ...
    @property
    def PageStyle(self) -> PageStyle: ...
    @property
    def PersistentPresets(self) -> ObjectModel.ObservableCollection: ...
    @property
    def PreviewMeshingParameters(self) -> Geometry.MeshingParameters: ...
    @property
    def PreviousSubDAbsoluteSliderPosition(self) -> int: ...
    @property
    def PreviousSubDAdaptiveSliderPosition(self) -> int: ...
    @property
    def RefineMesh(self) -> bool: ...
    @property
    def RefineMeshChanged(self) -> bool: ...
    @property
    def RefineMeshColor(self) -> Drawing.Color: ...
    @property
    def SelectedPreset(self) -> MeshParametersStyle: ...
    @property
    def SelectedPresetIndex(self) -> int: ...
    @property
    def SettingPresetValues(self) -> bool: ...
    @property
    def SimplePlanes(self) -> bool: ...
    @property
    def SimplePlanesChanged(self) -> bool: ...
    @property
    def SimplePlanesColor(self) -> Drawing.Color: ...
    @property
    def SubDAbsoluteSliderPosition(self) -> int: ...
    @property
    def SubDAbsoluteSliderPositionChanged(self) -> bool: ...
    @property
    def SubDAbsoluteSliderPositionColor(self) -> Drawing.Color: ...
    @property
    def SubDAdaptiveSliderPosition(self) -> int: ...
    @property
    def SubDAdaptiveSliderPositionChanged(self) -> bool: ...
    @property
    def SubDAdaptiveSliderPositionColor(self) -> Drawing.Color: ...
    @overload
    def GetPresetsFromPersistentSettings() -> None: ...
    @overload
    def ImportPresetsMenuClick(self, windowOwner: Forms.Control) -> None: ...
    @overload
    def LoadPresetsFromFile(self, fileName: str) -> bool: ...
    @overload
    def PreviewMeshes() -> Commands.Result: ...
    @overload
    def ReloadPreset() -> None: ...
    @overload
    def Reset() -> None: ...
    @overload
    def RetrievePresetListFromSettings() -> ObjectModel.ObservableCollection: ...
    @overload
    def SaveAllPresetsToPersistentSettings() -> None: ...
    @overload
    def SavePreset(self, preset: MeshParametersStyle) -> None: ...
    @overload
    def SavePresetListToFile(self, fileName: str) -> None: ...
    @overload
    def SavePresetMenuClick() -> None: ...
    @overload
    def Set() -> None: ...
    @CancelAnalysisPreviewChanges.setter
    def CancelAnalysisPreviewChanges(self, value: System.Void): ...
    @ChangedValueColor.setter
    def ChangedValueColor(self, value: System.Void): ...
    @DefaultControlColor.setter
    def DefaultControlColor(self, value: System.Void): ...
    @Density.setter
    def Density(self, value: System.Void): ...
    @DensityChanged.setter
    def DensityChanged(self, value: System.Void): ...
    @Detailed.setter
    def Detailed(self, value: System.Void): ...
    @DetailedOrSimpleChanged.setter
    def DetailedOrSimpleChanged(self, value: System.Void): ...
    @DetailedOrSimpleText.setter
    def DetailedOrSimpleText(self, value: System.Void): ...
    @EnablePreview.setter
    def EnablePreview(self, value: System.Void): ...
    @JaggedSeams.setter
    def JaggedSeams(self, value: System.Void): ...
    @JaggedSeamsChanged.setter
    def JaggedSeamsChanged(self, value: System.Void): ...
    @LabelDefaultColor.setter
    def LabelDefaultColor(self, value: System.Void): ...
    @MaxDistanceEdgeToSurface.setter
    def MaxDistanceEdgeToSurface(self, value: System.Void): ...
    @MaxDistanceEdgeToSurfaceChanged.setter
    def MaxDistanceEdgeToSurfaceChanged(self, value: System.Void): ...
    @MaximumAngle.setter
    def MaximumAngle(self, value: System.Void): ...
    @MaximumAngleChanged.setter
    def MaximumAngleChanged(self, value: System.Void): ...
    @MaximumAspectRatio.setter
    def MaximumAspectRatio(self, value: System.Void): ...
    @MaximumAspectRatioChanged.setter
    def MaximumAspectRatioChanged(self, value: System.Void): ...
    @MaximumEdgeLength.setter
    def MaximumEdgeLength(self, value: System.Void): ...
    @MaximumEdgeLengthChanged.setter
    def MaximumEdgeLengthChanged(self, value: System.Void): ...
    @MeshParameters.setter
    def MeshParameters(self, value: System.Void): ...
    @MinimumEdgeLength.setter
    def MinimumEdgeLength(self, value: System.Void): ...
    @MinimumEdgeLengthChanged.setter
    def MinimumEdgeLengthChanged(self, value: System.Void): ...
    @MinimumInitialGridQuads.setter
    def MinimumInitialGridQuads(self, value: System.Void): ...
    @MinimumInitialGridQuadsChanged.setter
    def MinimumInitialGridQuadsChanged(self, value: System.Void): ...
    @NurbsMeshingSliderPosition.setter
    def NurbsMeshingSliderPosition(self, value: System.Void): ...
    @PackTextures.setter
    def PackTextures(self, value: System.Void): ...
    @PackTexturesChanged.setter
    def PackTexturesChanged(self, value: System.Void): ...
    @PageStyle.setter
    def PageStyle(self, value: System.Void): ...
    @PersistentPresets.setter
    def PersistentPresets(self, value: System.Void): ...
    @PreviewMeshingParameters.setter
    def PreviewMeshingParameters(self, value: System.Void): ...
    @PreviousSubDAbsoluteSliderPosition.setter
    def PreviousSubDAbsoluteSliderPosition(self, value: System.Void): ...
    @PreviousSubDAdaptiveSliderPosition.setter
    def PreviousSubDAdaptiveSliderPosition(self, value: System.Void): ...
    @RefineMesh.setter
    def RefineMesh(self, value: System.Void): ...
    @RefineMeshChanged.setter
    def RefineMeshChanged(self, value: System.Void): ...
    @SelectedPreset.setter
    def SelectedPreset(self, value: System.Void): ...
    @SelectedPresetIndex.setter
    def SelectedPresetIndex(self, value: System.Void): ...
    @SettingPresetValues.setter
    def SettingPresetValues(self, value: System.Void): ...
    @SimplePlanes.setter
    def SimplePlanes(self, value: System.Void): ...
    @SimplePlanesChanged.setter
    def SimplePlanesChanged(self, value: System.Void): ...
    @SubDAbsoluteSliderPosition.setter
    def SubDAbsoluteSliderPosition(self, value: System.Void): ...
    @SubDAbsoluteSliderPositionChanged.setter
    def SubDAbsoluteSliderPositionChanged(self, value: System.Void): ...
    @SubDAdaptiveSliderPosition.setter
    def SubDAdaptiveSliderPosition(self, value: System.Void): ...
    @SubDAdaptiveSliderPositionChanged.setter
    def SubDAdaptiveSliderPositionChanged(self, value: System.Void): ...
    @overload
    def SetMpSubDFromSubDSliderPosition() -> None: ...
    @overload
    def ShowUpdatePresetMenuItem() -> bool: ...
    @overload
    def TurnPreviewOff() -> None: ...
    @overload
    def UpdateDetailedOrSimpleButton(self, detailed: bool) -> None: ...
    @overload
    def UpdatePresetMenuClick() -> None: ...
    @property
    def PropertyChanged(self): ...
    @property
    def ModleUnitsChanged(self): ...
    @property
    def PageUnitsChanged(self): ...

class PageStyle(enum.Enum):
    Properties = 0
    Mesh = 1
    Stl = 2
    Analysis = 3
    ParamsOnly = 4
    PerObject = 5

# endregion
