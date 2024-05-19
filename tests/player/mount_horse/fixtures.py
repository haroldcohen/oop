from dataclasses import dataclass
from uuid import UUID

import pytest

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.rider.horse.dto import HorseRiderDTO
from oop.core.domain.transport.horse.dto import HorseDTO
from oop.core.domain.transport.horse.equipment.saddle.dto import SaddleDTO

__all__ = ["TestMountHorseParams", "expected_player", "expected_rider", "expected_horse", "expected_saddle"]


@dataclass(frozen=True)
class TestMountHorseParams:
    player_id: UUID

    rider_id: UUID

    horse_id: UUID

    saddle_id: UUID


@pytest.fixture
def expected_player(
    test_params: TestMountHorseParams,
    expected_rider,  # pylint: disable=redefined-outer-name
) -> PlayerDTO:
    return PlayerDTO(id=test_params.player_id, rider=expected_rider)


@pytest.fixture
def expected_rider(
    test_params: TestMountHorseParams,
    expected_horse,  # pylint: disable=redefined-outer-name
    expected_saddle,  # pylint: disable=redefined-outer-name
) -> HorseRiderDTO:
    return HorseRiderDTO(
        id=test_params.rider_id,
        horse=expected_horse,
        saddle=expected_saddle,
    )


@pytest.fixture
def expected_horse(
    test_params: TestMountHorseParams,
    expected_saddle,  # pylint: disable=redefined-outer-name
) -> HorseDTO:
    return HorseDTO(
        id=test_params.horse_id,
        rider_id=test_params.rider_id,
        is_calm=True,
        saddle=expected_saddle,
    )


@pytest.fixture
def expected_saddle(
    test_params: TestMountHorseParams,
) -> SaddleDTO:
    return SaddleDTO(
        id=test_params.saddle_id,
        is_equipped=True,
    )
