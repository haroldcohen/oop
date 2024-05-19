from uuid import uuid4

import pytest

from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.bicycle.model import BicycleRider
from oop.core.domain.transport.bicycle.model import Bicycle
from tests.player.ride_bicycle.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        (
            TestRideBicycleParams(
                player_id=uuid4(),
                rider_id=uuid4(),
                bicycle_id=uuid4(),
            )
        ),
    ],
)
def test_ride_bicycle_should_seat_the_player(
    test_params,
    expected_player,
):
    player = Player(_id=test_params.player_id)
    rider = BicycleRider(_id=test_params.rider_id)
    bicycle = Bicycle(_id=test_params.bicycle_id)
    player.ride(
        rider=rider,
        ride=bicycle,
    )

    assert player.to_dto() == expected_player
