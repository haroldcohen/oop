import pytest

from oop.core.domain.map.dto import MapDTO
from oop.core.domain.map.model import Map
from oop.core.domain.map.terrain.dirt.dto import DirtTileDTO
from oop.core.domain.map.terrain.dirt.model import DirtTile
from oop.core.domain.map.terrain.water.dto import WaterTileDTO
from oop.core.domain.map.terrain.water.model import WaterTile
from oop.core.domain.player.position import PlayerPosition
from oop.core.domain.player.travel.strategy import TravelStrategy
from tests.player.travel_by_foot.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        TravelByFootTestParams(
            ride_distance=1,
            expected_player_location=(0, 1),
        )
    ],
)
def test_travel_by_foot_on_dirt_should_move_the_player_on_the_map(
    test_params,
    player,
    game_map,
    expected_map,
    expected_player,
):
    player.travel(
        distance=test_params.ride_distance,
        game_map=game_map,
        strategy=TravelStrategy.BY_FOOT,
    )

    assert player.to_dto() == expected_player
    assert game_map.to_dto() == expected_map


@pytest.mark.parametrize(
    "test_params",
    [
        TravelByFootTestParams(
            ride_distance=2,
            expected_player_location=(0, 2),
        )
    ],
)
def test_travel_by_foot_in_shallow_water_should_move_the_player_on_the_map(
    test_params,
    player,
    expected_map,
    expected_player,
):
    base_terrain_dto = [[DirtTileDTO()], [WaterTileDTO()], [DirtTileDTO(players=[expected_player])]]
    expected_map = MapDTO(
        terrain=base_terrain_dto,
    )

    base_terrain = [[DirtTile(players=[player])], [WaterTile(players=[])], [DirtTile(players=[])]]
    game_map = Map(terrain=base_terrain)

    player.travel(
        distance=test_params.ride_distance,
        game_map=game_map,
        strategy=TravelStrategy.BY_FOOT,
    )

    assert player.to_dto() == expected_player
    assert game_map.to_dto() == expected_map
