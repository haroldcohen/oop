# pylint: disable=duplicate-code
from dataclasses import dataclass, field
from typing import Tuple
from uuid import UUID, uuid4

import pytest

from oop.core.domain.map.dto import MapDTO
from oop.core.domain.map.model import Map
from oop.core.domain.map.terrain.dirt.dto import DirtTileDTO
from oop.core.domain.map.terrain.dirt.model import DirtTile
from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.location.dto import PlayerLocationDTO
from oop.core.domain.player.location.model import PlayerLocation
from oop.core.domain.player.model import Player
from oop.core.domain.player.position import PlayerPosition
from oop.core.domain.player.rider.null_rider.dto import NullRiderDTO
from oop.core.domain.player.rider.null_rider.model import NullRider

__all__ = [
    "TravelByFootTestParams",
    "expected_player",
    "expected_map",
    "player",
    "game_map",
]


@dataclass(frozen=True)
class TravelByFootTestParams:

    ride_distance: int

    expected_player_location: Tuple[int, int]

    player_id: UUID = field(default_factory=uuid4)


@pytest.fixture
def expected_player(
    test_params: TravelByFootTestParams,
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=NullRiderDTO(),
        position=PlayerPosition.STANDING,
        location=PlayerLocationDTO(
            y_coordinates=test_params.expected_player_location[1],
        ),
    )


@pytest.fixture
def expected_map(
    test_params: TravelByFootTestParams,
    expected_player,  # pylint: disable=redefined-outer-name
) -> MapDTO:
    base_terrain_dto = [[DirtTileDTO()] for _ in range(test_params.ride_distance)]
    base_terrain_dto.append(
        [
            DirtTileDTO(
                players=[expected_player],
            )
        ]
    )

    return MapDTO(
        terrain=base_terrain_dto,
    )


@pytest.fixture
def game_map(
    test_params: TravelByFootTestParams,
    player,  # pylint: disable=redefined-outer-name
) -> Map:
    base_terrain = [[DirtTile(players=[player])]]
    base_terrain.extend([DirtTile(players=[])] for _ in range(test_params.ride_distance - 1))
    base_terrain.append([DirtTile(players=[])])

    return Map(terrain=base_terrain)


@pytest.fixture
def player(
    test_params: TravelByFootTestParams,
) -> Player:
    return Player(
        _id=test_params.player_id,
        rider=NullRider(),
        location=PlayerLocation(),
    )
