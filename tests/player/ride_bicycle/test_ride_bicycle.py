import pytest

from oop.core.domain.player.location.model import PlayerLocation
from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.bicycle.model import BicycleRider
from oop.core.domain.transport.bicycle.model import Bicycle
from oop.core.domain.transport.location.model import TransportLocation
from tests.player.ride_bicycle.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        TestRideBicycleParams(
            ride_distance=1,
            expected_player_location=(0, 1),
            expected_bicycle_location=(0, 1),
        ),
        TestRideBicycleParams(
            ride_distance=2,
            expected_player_location=(0, 2),
            expected_bicycle_location=(0, 2),
        ),
    ],
)
def test_ride_bicycle_for_n_meters_on_the_road_should_move_the_player_and_bicycle_on_the_map(
    test_params, expected_player
):
    bicycle_rider = BicycleRider(
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
    player = Player(
        _id=test_params.player_id,
        rider=bicycle_rider,
        location=PlayerLocation(
            x_coordinates=0,
            y_coordinates=0,
        ),
    )
    player.ride(
        distance=test_params.ride_distance,
    )

    assert player.to_dto() == expected_player
