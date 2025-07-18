"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import s2clientprotocol.common_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ObservationFeatureLayer(google.protobuf.message.Message):
    """
    Observation - Feature Layer
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RENDERS_FIELD_NUMBER: builtins.int
    MINIMAP_RENDERS_FIELD_NUMBER: builtins.int
    @property
    def renders(self) -> global___FeatureLayers: ...
    @property
    def minimap_renders(self) -> global___FeatureLayersMinimap: ...
    def __init__(
        self, *, renders: global___FeatureLayers | None = ..., minimap_renders: global___FeatureLayersMinimap | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["minimap_renders", b"minimap_renders", "renders", b"renders"]
    ) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["minimap_renders", b"minimap_renders", "renders", b"renders"]) -> None: ...

global___ObservationFeatureLayer = ObservationFeatureLayer

@typing.final
class FeatureLayers(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_MAP_FIELD_NUMBER: builtins.int
    VISIBILITY_MAP_FIELD_NUMBER: builtins.int
    CREEP_FIELD_NUMBER: builtins.int
    POWER_FIELD_NUMBER: builtins.int
    PLAYER_ID_FIELD_NUMBER: builtins.int
    UNIT_TYPE_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    UNIT_HIT_POINTS_FIELD_NUMBER: builtins.int
    UNIT_HIT_POINTS_RATIO_FIELD_NUMBER: builtins.int
    UNIT_ENERGY_FIELD_NUMBER: builtins.int
    UNIT_ENERGY_RATIO_FIELD_NUMBER: builtins.int
    UNIT_SHIELDS_FIELD_NUMBER: builtins.int
    UNIT_SHIELDS_RATIO_FIELD_NUMBER: builtins.int
    PLAYER_RELATIVE_FIELD_NUMBER: builtins.int
    UNIT_DENSITY_AA_FIELD_NUMBER: builtins.int
    UNIT_DENSITY_FIELD_NUMBER: builtins.int
    EFFECTS_FIELD_NUMBER: builtins.int
    HALLUCINATIONS_FIELD_NUMBER: builtins.int
    CLOAKED_FIELD_NUMBER: builtins.int
    BLIP_FIELD_NUMBER: builtins.int
    BUFFS_FIELD_NUMBER: builtins.int
    BUFF_DURATION_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    BUILD_PROGRESS_FIELD_NUMBER: builtins.int
    BUILDABLE_FIELD_NUMBER: builtins.int
    PATHABLE_FIELD_NUMBER: builtins.int
    PLACEHOLDER_FIELD_NUMBER: builtins.int
    @property
    def height_map(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Terrain height. World space units of [-200, 200] encoded into [0, 255]."""

    @property
    def visibility_map(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. 0=Hidden, 1=Fogged, 2=Visible, 3=FullHidden"""

    @property
    def creep(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Zerg creep."""

    @property
    def power(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Protoss power."""

    @property
    def player_id(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Participants: [1, 15] Neutral: 16"""

    @property
    def unit_type(self) -> s2clientprotocol.common_pb2.ImageData:
        """int32. Unique identifier for type of unit."""

    @property
    def selected(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Selected units."""

    @property
    def unit_hit_points(self) -> s2clientprotocol.common_pb2.ImageData:
        """int32."""

    @property
    def unit_hit_points_ratio(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Ratio of current health to max health. [0%, 100%] encoded into [0, 255]."""

    @property
    def unit_energy(self) -> s2clientprotocol.common_pb2.ImageData:
        """int32."""

    @property
    def unit_energy_ratio(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Ratio of current energy to max energy. [0%, 100%] encoded into [0, 255]."""

    @property
    def unit_shields(self) -> s2clientprotocol.common_pb2.ImageData:
        """int32."""

    @property
    def unit_shields_ratio(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Ratio of current shields to max shields. [0%, 100%] encoded into [0, 255]."""

    @property
    def player_relative(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. See "Alliance" enum in raw.proto. Range: [1, 4]"""

    @property
    def unit_density_aa(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Density of units overlapping a pixel, anti-aliased. [0.0, 16.0f] encoded into [0, 255]."""

    @property
    def unit_density(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Count of units overlapping a pixel."""

    @property
    def effects(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Visuals of persistent abilities. (eg. Psistorm)"""

    @property
    def hallucinations(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether the unit here is a hallucination."""

    @property
    def cloaked(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether the unit here is cloaked. Hidden units will show up too, but with less details in other layers."""

    @property
    def blip(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether the unit here is a blip."""

    @property
    def buffs(self) -> s2clientprotocol.common_pb2.ImageData:
        """int32. One of the buffs applied to this unit. Extras are ignored."""

    @property
    def buff_duration(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Ratio of buff remaining. [0%, 100%] encoded into [0, 255]."""

    @property
    def active(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether the unit here is active."""

    @property
    def build_progress(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. How far along the building is building something. [0%, 100%] encoded into [0, 255]."""

    @property
    def buildable(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether a building can be built here."""

    @property
    def pathable(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether a unit can walk here."""

    @property
    def placeholder(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether the unit here is a placeholder building to be constructed."""

    def __init__(
        self,
        *,
        height_map: s2clientprotocol.common_pb2.ImageData | None = ...,
        visibility_map: s2clientprotocol.common_pb2.ImageData | None = ...,
        creep: s2clientprotocol.common_pb2.ImageData | None = ...,
        power: s2clientprotocol.common_pb2.ImageData | None = ...,
        player_id: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_type: s2clientprotocol.common_pb2.ImageData | None = ...,
        selected: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_hit_points: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_hit_points_ratio: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_energy: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_energy_ratio: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_shields: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_shields_ratio: s2clientprotocol.common_pb2.ImageData | None = ...,
        player_relative: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_density_aa: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_density: s2clientprotocol.common_pb2.ImageData | None = ...,
        effects: s2clientprotocol.common_pb2.ImageData | None = ...,
        hallucinations: s2clientprotocol.common_pb2.ImageData | None = ...,
        cloaked: s2clientprotocol.common_pb2.ImageData | None = ...,
        blip: s2clientprotocol.common_pb2.ImageData | None = ...,
        buffs: s2clientprotocol.common_pb2.ImageData | None = ...,
        buff_duration: s2clientprotocol.common_pb2.ImageData | None = ...,
        active: s2clientprotocol.common_pb2.ImageData | None = ...,
        build_progress: s2clientprotocol.common_pb2.ImageData | None = ...,
        buildable: s2clientprotocol.common_pb2.ImageData | None = ...,
        pathable: s2clientprotocol.common_pb2.ImageData | None = ...,
        placeholder: s2clientprotocol.common_pb2.ImageData | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "active",
            b"active",
            "blip",
            b"blip",
            "buff_duration",
            b"buff_duration",
            "buffs",
            b"buffs",
            "build_progress",
            b"build_progress",
            "buildable",
            b"buildable",
            "cloaked",
            b"cloaked",
            "creep",
            b"creep",
            "effects",
            b"effects",
            "hallucinations",
            b"hallucinations",
            "height_map",
            b"height_map",
            "pathable",
            b"pathable",
            "placeholder",
            b"placeholder",
            "player_id",
            b"player_id",
            "player_relative",
            b"player_relative",
            "power",
            b"power",
            "selected",
            b"selected",
            "unit_density",
            b"unit_density",
            "unit_density_aa",
            b"unit_density_aa",
            "unit_energy",
            b"unit_energy",
            "unit_energy_ratio",
            b"unit_energy_ratio",
            "unit_hit_points",
            b"unit_hit_points",
            "unit_hit_points_ratio",
            b"unit_hit_points_ratio",
            "unit_shields",
            b"unit_shields",
            "unit_shields_ratio",
            b"unit_shields_ratio",
            "unit_type",
            b"unit_type",
            "visibility_map",
            b"visibility_map",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "active",
            b"active",
            "blip",
            b"blip",
            "buff_duration",
            b"buff_duration",
            "buffs",
            b"buffs",
            "build_progress",
            b"build_progress",
            "buildable",
            b"buildable",
            "cloaked",
            b"cloaked",
            "creep",
            b"creep",
            "effects",
            b"effects",
            "hallucinations",
            b"hallucinations",
            "height_map",
            b"height_map",
            "pathable",
            b"pathable",
            "placeholder",
            b"placeholder",
            "player_id",
            b"player_id",
            "player_relative",
            b"player_relative",
            "power",
            b"power",
            "selected",
            b"selected",
            "unit_density",
            b"unit_density",
            "unit_density_aa",
            b"unit_density_aa",
            "unit_energy",
            b"unit_energy",
            "unit_energy_ratio",
            b"unit_energy_ratio",
            "unit_hit_points",
            b"unit_hit_points",
            "unit_hit_points_ratio",
            b"unit_hit_points_ratio",
            "unit_shields",
            b"unit_shields",
            "unit_shields_ratio",
            b"unit_shields_ratio",
            "unit_type",
            b"unit_type",
            "visibility_map",
            b"visibility_map",
        ],
    ) -> None: ...

global___FeatureLayers = FeatureLayers

@typing.final
class FeatureLayersMinimap(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_MAP_FIELD_NUMBER: builtins.int
    VISIBILITY_MAP_FIELD_NUMBER: builtins.int
    CREEP_FIELD_NUMBER: builtins.int
    CAMERA_FIELD_NUMBER: builtins.int
    PLAYER_ID_FIELD_NUMBER: builtins.int
    PLAYER_RELATIVE_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    ALERTS_FIELD_NUMBER: builtins.int
    BUILDABLE_FIELD_NUMBER: builtins.int
    PATHABLE_FIELD_NUMBER: builtins.int
    UNIT_TYPE_FIELD_NUMBER: builtins.int
    @property
    def height_map(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Terrain height. World space units of [-200, 200] encoded into [0, 255]."""

    @property
    def visibility_map(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. 0=Hidden, 1=Fogged, 2=Visible, 3=FullHidden"""

    @property
    def creep(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Zerg creep."""

    @property
    def camera(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Area covered by the camera."""

    @property
    def player_id(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. Participants: [1, 15] Neutral: 16"""

    @property
    def player_relative(self) -> s2clientprotocol.common_pb2.ImageData:
        """uint8. See "Alliance" enum in raw.proto. Range: [1, 4]"""

    @property
    def selected(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Selected units."""

    @property
    def alerts(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Shows 'UnitAttacked' alert location."""

    @property
    def buildable(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether a building can be built here."""

    @property
    def pathable(self) -> s2clientprotocol.common_pb2.ImageData:
        """1-bit. Whether a unit can walk here."""

    @property
    def unit_type(self) -> s2clientprotocol.common_pb2.ImageData:
        """Cheat layers, enable with SpatialCameraSetup.allow_cheating_layers.
        int32. Unique identifier for type of unit.
        """

    def __init__(
        self,
        *,
        height_map: s2clientprotocol.common_pb2.ImageData | None = ...,
        visibility_map: s2clientprotocol.common_pb2.ImageData | None = ...,
        creep: s2clientprotocol.common_pb2.ImageData | None = ...,
        camera: s2clientprotocol.common_pb2.ImageData | None = ...,
        player_id: s2clientprotocol.common_pb2.ImageData | None = ...,
        player_relative: s2clientprotocol.common_pb2.ImageData | None = ...,
        selected: s2clientprotocol.common_pb2.ImageData | None = ...,
        alerts: s2clientprotocol.common_pb2.ImageData | None = ...,
        buildable: s2clientprotocol.common_pb2.ImageData | None = ...,
        pathable: s2clientprotocol.common_pb2.ImageData | None = ...,
        unit_type: s2clientprotocol.common_pb2.ImageData | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "alerts",
            b"alerts",
            "buildable",
            b"buildable",
            "camera",
            b"camera",
            "creep",
            b"creep",
            "height_map",
            b"height_map",
            "pathable",
            b"pathable",
            "player_id",
            b"player_id",
            "player_relative",
            b"player_relative",
            "selected",
            b"selected",
            "unit_type",
            b"unit_type",
            "visibility_map",
            b"visibility_map",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "alerts",
            b"alerts",
            "buildable",
            b"buildable",
            "camera",
            b"camera",
            "creep",
            b"creep",
            "height_map",
            b"height_map",
            "pathable",
            b"pathable",
            "player_id",
            b"player_id",
            "player_relative",
            b"player_relative",
            "selected",
            b"selected",
            "unit_type",
            b"unit_type",
            "visibility_map",
            b"visibility_map",
        ],
    ) -> None: ...

global___FeatureLayersMinimap = FeatureLayersMinimap

@typing.final
class ObservationRender(google.protobuf.message.Message):
    """
    Observation - Rendered
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAP_FIELD_NUMBER: builtins.int
    MINIMAP_FIELD_NUMBER: builtins.int
    @property
    def map(self) -> s2clientprotocol.common_pb2.ImageData: ...
    @property
    def minimap(self) -> s2clientprotocol.common_pb2.ImageData: ...
    def __init__(
        self,
        *,
        map: s2clientprotocol.common_pb2.ImageData | None = ...,
        minimap: s2clientprotocol.common_pb2.ImageData | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["map", b"map", "minimap", b"minimap"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["map", b"map", "minimap", b"minimap"]) -> None: ...

global___ObservationRender = ObservationRender

@typing.final
class ActionSpatial(google.protobuf.message.Message):
    """
    Action
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UNIT_COMMAND_FIELD_NUMBER: builtins.int
    CAMERA_MOVE_FIELD_NUMBER: builtins.int
    UNIT_SELECTION_POINT_FIELD_NUMBER: builtins.int
    UNIT_SELECTION_RECT_FIELD_NUMBER: builtins.int
    @property
    def unit_command(self) -> global___ActionSpatialUnitCommand: ...
    @property
    def camera_move(self) -> global___ActionSpatialCameraMove: ...
    @property
    def unit_selection_point(self) -> global___ActionSpatialUnitSelectionPoint: ...
    @property
    def unit_selection_rect(self) -> global___ActionSpatialUnitSelectionRect: ...
    def __init__(
        self,
        *,
        unit_command: global___ActionSpatialUnitCommand | None = ...,
        camera_move: global___ActionSpatialCameraMove | None = ...,
        unit_selection_point: global___ActionSpatialUnitSelectionPoint | None = ...,
        unit_selection_rect: global___ActionSpatialUnitSelectionRect | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "action",
            b"action",
            "camera_move",
            b"camera_move",
            "unit_command",
            b"unit_command",
            "unit_selection_point",
            b"unit_selection_point",
            "unit_selection_rect",
            b"unit_selection_rect",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "action",
            b"action",
            "camera_move",
            b"camera_move",
            "unit_command",
            b"unit_command",
            "unit_selection_point",
            b"unit_selection_point",
            "unit_selection_rect",
            b"unit_selection_rect",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["action", b"action"]
    ) -> typing.Literal["unit_command", "camera_move", "unit_selection_point", "unit_selection_rect"] | None: ...

global___ActionSpatial = ActionSpatial

@typing.final
class ActionSpatialUnitCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ABILITY_ID_FIELD_NUMBER: builtins.int
    TARGET_SCREEN_COORD_FIELD_NUMBER: builtins.int
    TARGET_MINIMAP_COORD_FIELD_NUMBER: builtins.int
    QUEUE_COMMAND_FIELD_NUMBER: builtins.int
    ability_id: builtins.int
    queue_command: builtins.bool
    """Equivalent to shift+command."""
    @property
    def target_screen_coord(self) -> s2clientprotocol.common_pb2.PointI: ...
    @property
    def target_minimap_coord(self) -> s2clientprotocol.common_pb2.PointI: ...
    def __init__(
        self,
        *,
        ability_id: builtins.int | None = ...,
        target_screen_coord: s2clientprotocol.common_pb2.PointI | None = ...,
        target_minimap_coord: s2clientprotocol.common_pb2.PointI | None = ...,
        queue_command: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "ability_id",
            b"ability_id",
            "queue_command",
            b"queue_command",
            "target",
            b"target",
            "target_minimap_coord",
            b"target_minimap_coord",
            "target_screen_coord",
            b"target_screen_coord",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "ability_id",
            b"ability_id",
            "queue_command",
            b"queue_command",
            "target",
            b"target",
            "target_minimap_coord",
            b"target_minimap_coord",
            "target_screen_coord",
            b"target_screen_coord",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["target", b"target"]
    ) -> typing.Literal["target_screen_coord", "target_minimap_coord"] | None: ...

global___ActionSpatialUnitCommand = ActionSpatialUnitCommand

@typing.final
class ActionSpatialCameraMove(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CENTER_MINIMAP_FIELD_NUMBER: builtins.int
    @property
    def center_minimap(self) -> s2clientprotocol.common_pb2.PointI:
        """Simulates a click on the minimap to move the camera."""

    def __init__(self, *, center_minimap: s2clientprotocol.common_pb2.PointI | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["center_minimap", b"center_minimap"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["center_minimap", b"center_minimap"]) -> None: ...

global___ActionSpatialCameraMove = ActionSpatialCameraMove

@typing.final
class ActionSpatialUnitSelectionPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ActionSpatialUnitSelectionPoint._Type.ValueType],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Select: ActionSpatialUnitSelectionPoint._Type.ValueType  # 1
        """Equivalent to normal click. Changes selection to unit."""
        Toggle: ActionSpatialUnitSelectionPoint._Type.ValueType  # 2
        """Equivalent to shift+click. Toggle selection of unit."""
        AllType: ActionSpatialUnitSelectionPoint._Type.ValueType  # 3
        """Equivalent to control+click. Selects all units of a given type."""
        AddAllType: ActionSpatialUnitSelectionPoint._Type.ValueType  # 4
        """Equivalent to shift+control+click. Selects all units of a given type."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    Select: ActionSpatialUnitSelectionPoint.Type.ValueType  # 1
    """Equivalent to normal click. Changes selection to unit."""
    Toggle: ActionSpatialUnitSelectionPoint.Type.ValueType  # 2
    """Equivalent to shift+click. Toggle selection of unit."""
    AllType: ActionSpatialUnitSelectionPoint.Type.ValueType  # 3
    """Equivalent to control+click. Selects all units of a given type."""
    AddAllType: ActionSpatialUnitSelectionPoint.Type.ValueType  # 4
    """Equivalent to shift+control+click. Selects all units of a given type."""

    SELECTION_SCREEN_COORD_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    type: global___ActionSpatialUnitSelectionPoint.Type.ValueType
    @property
    def selection_screen_coord(self) -> s2clientprotocol.common_pb2.PointI: ...
    def __init__(
        self,
        *,
        selection_screen_coord: s2clientprotocol.common_pb2.PointI | None = ...,
        type: global___ActionSpatialUnitSelectionPoint.Type.ValueType | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["selection_screen_coord", b"selection_screen_coord", "type", b"type"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["selection_screen_coord", b"selection_screen_coord", "type", b"type"]
    ) -> None: ...

global___ActionSpatialUnitSelectionPoint = ActionSpatialUnitSelectionPoint

@typing.final
class ActionSpatialUnitSelectionRect(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SELECTION_SCREEN_COORD_FIELD_NUMBER: builtins.int
    SELECTION_ADD_FIELD_NUMBER: builtins.int
    selection_add: builtins.bool
    """Equivalent to shift+drag. Adds units to selection."""
    @property
    def selection_screen_coord(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[s2clientprotocol.common_pb2.RectangleI]:
        """Eventually this should not be an array, but a single field (multiple would be cheating)."""

    def __init__(
        self,
        *,
        selection_screen_coord: collections.abc.Iterable[s2clientprotocol.common_pb2.RectangleI] | None = ...,
        selection_add: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["selection_add", b"selection_add"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["selection_add", b"selection_add", "selection_screen_coord", b"selection_screen_coord"]
    ) -> None: ...

global___ActionSpatialUnitSelectionRect = ActionSpatialUnitSelectionRect
