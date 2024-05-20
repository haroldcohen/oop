import pytest

from tests.player.travel_by_foot.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [TestTravelByFootParams(ride_distance=1, expected_player_location=(0, 1))],
)
def test_travel_by_foot_should_move_the_player_on_the_map(
    test_params,
    player,
    game_map,
    expected_map,
    expected_player,
):
    player.travel(
        distance=test_params.ride_distance,
        game_map=game_map,
    )

    assert player.to_dto() == expected_player
    assert game_map.to_dto() == expected_map
