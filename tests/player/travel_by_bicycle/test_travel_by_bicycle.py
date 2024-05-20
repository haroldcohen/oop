import pytest

from tests.player.travel_by_bicycle.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        TestTravelByBicycleParams(
            ride_distance=1,
            expected_player_location=(0, 1),
            expected_bicycle_location=(0, 1),
        ),
        TestTravelByBicycleParams(
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
