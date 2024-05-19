from dataclasses import dataclass, field
from typing import Tuple
from uuid import UUID, uuid4

import pytest

__all__ = [
    "TestRideBicycleParams",
    "expected_player",
    "expected_bicycle",
    "expected_rider",
]

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.location.dto import PlayerLocationDTO
from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.transport.bicycle.dto import BicycleDTO
from oop.core.domain.transport.location.dto import TransportLocationDTO


@dataclass(frozen=True)
class TestRideBicycleParams:

    ride_distance: int

    expected_player_location: Tuple[int, int]

    expected_bicycle_location: Tuple[int, int]

    player_id: UUID = field(default_factory=uuid4)

    rider_id: UUID = field(default_factory=uuid4)

    bicycle_id: UUID = field(default_factory=uuid4)


@pytest.fixture
def expected_player(
    test_params: TestRideBicycleParams,
    expected_rider,  # pylint: disable=redefined-outer-name
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=expected_rider,
        location=PlayerLocationDTO(
            x_coordinates=0,
            y_coordinates=test_params.expected_player_location[1],
        ),
    )


@pytest.fixture
def expected_rider(
    test_params: TestRideBicycleParams,
    expected_bicycle,  # pylint: disable=redefined-outer-name
):
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
        location=TransportLocationDTO(
            y_coordinates=test_params.expected_player_location[1],
        ),
    )
