from dataclasses import dataclass
from uuid import UUID

import pytest

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.position import PlayerPosition
from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.transport.bicycle.dto import BicycleDTO

__all__ = ["expected_player", "expected_bicycle_rider", "expected_bicycle", "MountBicycleTestParams"]


@dataclass(frozen=True)
class MountBicycleTestParams:
    player_id: UUID

    rider_id: UUID

    bicycle_id: UUID


@pytest.fixture
def expected_player(
    test_params: MountBicycleTestParams,
    expected_bicycle_rider: BicycleRiderDTO,  # pylint: disable=redefined-outer-name
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=expected_bicycle_rider,
        position=PlayerPosition.SEATING,
    )


@pytest.fixture
def expected_bicycle_rider(
    test_params: MountBicycleTestParams,
    expected_bicycle: BicycleDTO,  # pylint: disable=redefined-outer-name
) -> BicycleRiderDTO:
    return BicycleRiderDTO(
        id=test_params.rider_id,
        bicycle=expected_bicycle,
    )


@pytest.fixture
def expected_bicycle(
    test_params: MountBicycleTestParams,
) -> BicycleDTO:
    return BicycleDTO(
        id=test_params.bicycle_id,
        rider_id=test_params.rider_id,
    )
