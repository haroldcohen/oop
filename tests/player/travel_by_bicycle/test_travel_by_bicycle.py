import pytest

from oop.core.domain.map.dto import MapDTO
from oop.core.domain.map.model import Map
from oop.core.domain.map.terrain.dirt.dto import DirtTileDTO
from oop.core.domain.map.terrain.dirt.model import DirtTile
from oop.core.domain.map.terrain.water.dto import WaterTileDTO
from oop.core.domain.map.terrain.water.model import WaterTile
from oop.core.domain.player.position import PlayerPosition
from tests.player.travel_by_bicycle.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        TravelByBicycleTestParams(
            ride_distance=1,
            expected_player_location=(0, 1),
            expected_bicycle_location=(0, 1),
        ),
        TravelByBicycleTestParams(
            ride_distance=2,
            expected_player_location=(0, 2),
            expected_bicycle_location=(0, 2),
        ),
    ],
)
def test_travel_by_bicycle_for_n_meters_on_dirt_should_move_the_player_and_bicycle_on_the_map(
    test_params,
    player,
    game_map,
    expected_player,
    expected_map,
):
    player.travel(
        distance=test_params.ride_distance,
        game_map=game_map,
    )

    assert player.to_dto() == expected_player
    assert game_map.to_dto() == expected_map


@pytest.mark.parametrize(
    "test_params",
    [
        TravelByBicycleTestParams(
            ride_distance=2,
            expected_player_location=(0, 1),
            expected_bicycle_location=(0, 1),
            expected_position=PlayerPosition.LAYING_DOWN,
        ),
        TravelByBicycleTestParams(
            ride_distance=3,
            expected_player_location=(0, 1),
            expected_bicycle_location=(0, 1),
            expected_position=PlayerPosition.LAYING_DOWN,
        ),
    ],
)
def test_travel_by_bicycle_in_shallow_waters_should_make_the_player_and_the_bicycle_fall(
    test_params,
    expected_player,
    player,
):
    base_terrain_dto = [[DirtTileDTO()], [WaterTileDTO(players=[expected_player])], [DirtTileDTO()]]
    expected_map = MapDTO(
        terrain=base_terrain_dto,
    )

    base_terrain = [[DirtTile(players=[player])], [WaterTile(players=[])], [DirtTile(players=[])]]
    game_map = Map(terrain=base_terrain)

    player.travel(
        distance=test_params.ride_distance,
        game_map=game_map,
    )

    assert player.to_dto() == expected_player
    assert game_map.to_dto() == expected_map
