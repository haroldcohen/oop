from uuid import uuid4

import pytest

from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.motorcycle.model import MotorcycleRider
from oop.core.domain.transport.motorcycle.engine.model import MotorcycleEngine
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.model import Motorcycle
from tests.player.mount_motorcycle.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        (
            TestMountMotorcycleParams(
                player_id=uuid4(),
                rider_id=uuid4(),
                motorcycle_id=uuid4(),
                engine_id=uuid4(),
                key_id=uuid4(),
            )
        ),
    ],
)
def test_ride_motorcycle_should_seat_the_player_and_start_the_engine(
    test_params,
    expected_player,
):
    player = Player(_id=expected_player.id)
    rider = MotorcycleRider(
        _id=expected_player.rider.id,
        motorcycle_key=MotorcycleKey(_id=expected_player.rider.motorcycle.key.id),
    )
    motorcycle = Motorcycle(
        _id=expected_player.rider.motorcycle.id,
        engine=MotorcycleEngine(
            _id=expected_player.rider.motorcycle.engine.id,
        ),
    )
    player.mount(
        rider=rider,
        ride=motorcycle,
    )

    assert player.to_dto() == expected_player
