from dataclasses import dataclass
from uuid import UUID, uuid4

import pytest

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.player.rider.bicycle.model import BicycleRider
from oop.core.domain.transport.bicycle.dto import BicycleDTO
from oop.core.domain.transport.bicycle.model import Bicycle


@dataclass(frozen=True)
class TestRideBicycleParams:
    player_id: UUID

    rider_id: UUID

    bicycle_id: UUID


@pytest.fixture
def expected_player(
    test_params: TestRideBicycleParams,
    expected_bicycle_rider: BicycleRiderDTO,
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=expected_bicycle_rider,
    )


@pytest.fixture
def expected_bicycle_rider(
    test_params: TestRideBicycleParams,
    expected_bicycle: BicycleDTO,
) -> BicycleRiderDTO:
    return BicycleRiderDTO(
        id=test_params.rider_id,
        bicycle=expected_bicycle,
    )


@pytest.fixture
def expected_bicycle(
    test_params: TestRideBicycleParams,
) -> BicycleDTO:
    return BicycleDTO(
        id=test_params.bicycle_id,
        rider_id=test_params.rider_id,
    )


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
