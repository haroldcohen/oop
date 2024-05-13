from dataclasses import dataclass
from uuid import UUID, uuid4

import pytest

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.horse.dto import HorseRiderDTO
from oop.core.domain.player.rider.horse.model import HorseRider
from oop.core.domain.player.riding.context import RidingContext
from oop.core.domain.player.riding.strategies.horse import RideHorseStrategy
from oop.core.domain.vehicle.horse.dto import HorseDTO
from oop.core.domain.vehicle.horse.equipment.saddle.dto import SaddleDTO
from oop.core.domain.vehicle.horse.equipment.saddle.model import Saddle
from oop.core.domain.vehicle.horse.model import Horse


@dataclass(frozen=True)
class TestRideHorseParams:
    player_id: UUID

    rider_id: UUID

    horse_id: UUID

    saddle_id: UUID


@pytest.fixture
def expected_player(
    test_params: TestRideHorseParams,
    expected_rider,
) -> PlayerDTO:
    return PlayerDTO(id=test_params.player_id, rider=expected_rider)


@pytest.fixture
def expected_rider(
    test_params: TestRideHorseParams,
    expected_horse,
) -> HorseRiderDTO:
    return HorseRiderDTO(
        id=test_params.rider_id,
        horse=expected_horse,
    )


@pytest.fixture
def expected_horse(
    test_params: TestRideHorseParams,
    expected_saddle,
) -> HorseDTO:
    return HorseDTO(
        id=test_params.horse_id,
        rider_id=test_params.rider_id,
        is_calm=True,
        saddle=expected_saddle,
    )


@pytest.fixture
def expected_saddle(
    test_params: TestRideHorseParams,
) -> SaddleDTO:
    return SaddleDTO(
        id=test_params.saddle_id,
        is_equipped=True,
    )


@pytest.mark.parametrize(
    "test_params",
    [
        TestRideHorseParams(
            player_id=uuid4(),
            rider_id=uuid4(),
            horse_id=uuid4(),
            saddle_id=uuid4(),
        )
    ],
)
def test_ride_horse_should_seat_the_player_on_a_calm_horse_with_a_saddle_on_its_back(
    test_params,
    expected_player,
):
    player = Player(_id=test_params.player_id)
    rider = HorseRider(_id=test_params.rider_id)
    saddle = Saddle(_id=test_params.saddle_id)
    horse = Horse(_id=test_params.horse_id)
    player.ride(
        rider=rider,
        ride=horse,
        riding_context=RidingContext(strategy=RideHorseStrategy(saddles=[saddle])),
    )

    assert player.to_dto() == expected_player
