from uuid import uuid4

import pytest

from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.horse.model import HorseRider
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle
from oop.core.domain.transport.horse.model import Horse
from tests.player.mount_horse.fixtures import *


@pytest.mark.parametrize(
    "test_params",
    [
        TestMountHorseParams(
            player_id=uuid4(),
            rider_id=uuid4(),
            horse_id=uuid4(),
            saddle_id=uuid4(),
        )
    ],
)
def test_mount_horse_should_seat_the_player_on_a_calm_horse_with_a_saddle_on_its_back(
    test_params,
    expected_player,
):
    player = Player(_id=test_params.player_id)
    saddle = Saddle(_id=test_params.saddle_id)
    rider = HorseRider(
        _id=test_params.rider_id,
        saddle=saddle,
    )
    horse = Horse(_id=test_params.horse_id)
    player.mount(
        rider=rider,
        ride=horse,
    )

    assert player.to_dto() == expected_player
