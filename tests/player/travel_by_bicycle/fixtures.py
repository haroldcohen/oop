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
from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.player.rider.bicycle.model import BicycleRider
from oop.core.domain.transport.bicycle.dto import BicycleDTO
from oop.core.domain.transport.bicycle.model import Bicycle
from oop.core.domain.transport.location.dto import TransportLocationDTO
from oop.core.domain.transport.location.model import TransportLocation

__all__ = [
    "TravelByBicycleTestParams",
    "expected_player",
    "expected_bicycle",
    "expected_rider",
    "expected_map",
    "player",
    "bicycle_rider",
    "game_map",
]


@dataclass(frozen=True)
class TravelByBicycleTestParams:

    ride_distance: int

    expected_player_location: Tuple[int, int]

    expected_bicycle_location: Tuple[int, int]

    player_id: UUID = field(default_factory=uuid4)

    rider_id: UUID = field(default_factory=uuid4)

    bicycle_id: UUID = field(default_factory=uuid4)

    expected_position: PlayerPosition = field(default=PlayerPosition.SEATING)


@pytest.fixture
def expected_player(
    test_params: TravelByBicycleTestParams,
    expected_rider,  # pylint: disable=redefined-outer-name
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=expected_rider,
        location=PlayerLocationDTO(
            x_coordinates=0,
            y_coordinates=test_params.expected_player_location[1],
        ),
        position=test_params.expected_position,
    )


@pytest.fixture
def expected_rider(
    test_params: TravelByBicycleTestParams,
    expected_bicycle,  # pylint: disable=redefined-outer-name
):
    return BicycleRiderDTO(
        id=test_params.rider_id,
        bicycle=expected_bicycle,
    )


@pytest.fixture
def expected_bicycle(
    test_params: TravelByBicycleTestParams,
) -> BicycleDTO:
    return BicycleDTO(
        id=test_params.bicycle_id,
        rider_id=test_params.rider_id,
        location=TransportLocationDTO(
            y_coordinates=test_params.expected_player_location[1],
        ),
    )


@pytest.fixture
def expected_map(
    test_params: TravelByBicycleTestParams,
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
def player(
    test_params: TravelByBicycleTestParams,
    bicycle_rider,  # pylint: disable=redefined-outer-name
) -> Player:
    return Player(
        _id=test_params.player_id,
        rider=bicycle_rider,
        location=PlayerLocation(
            x_coordinates=0,
            y_coordinates=0,
        ),
    )


@pytest.fixture
def bicycle_rider(
    test_params: TravelByBicycleTestParams,
) -> BicycleRider:
    return BicycleRider(
        _id=test_params.rider_id,
        bicycle=Bicycle(
            _id=test_params.bicycle_id,
            rider_id=test_params.rider_id,
            location=TransportLocation(
                x_coordinates=0,
                y_coordinates=0,
            ),
        ),
    )


@pytest.fixture
def game_map(
    test_params: TravelByBicycleTestParams,
    player,  # pylint: disable=redefined-outer-name
) -> Map:
    base_terrain = [[DirtTile(players=[player])]]
    base_terrain.extend([DirtTile(players=[])] for _ in range(test_params.ride_distance - 1))
    base_terrain.append([DirtTile(players=[])])

    return Map(terrain=base_terrain)
