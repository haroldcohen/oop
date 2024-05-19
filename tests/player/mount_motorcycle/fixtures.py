from dataclasses import dataclass
from uuid import UUID

import pytest

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.rider.motorcycle.dto import MotorcycleRiderDTO
from oop.core.domain.transport.motorcycle.dto import MotorCycleDTO
from oop.core.domain.transport.motorcycle.engine.dto import MotorcycleEngineDTO
from oop.core.domain.transport.motorcycle.key.dto import MotorcycleKeyDTO
from oop.core.domain.transport.motorcycle.key.position import KeyPosition

__all__ = [
    "TestMountMotorcycleParams",
    "expected_player",
    "expected_rider",
    "expected_motorcycle",
    "expected_key",
    "expected_engine",
]


@dataclass(frozen=True)
class TestMountMotorcycleParams:
    player_id: UUID

    rider_id: UUID

    motorcycle_id: UUID

    engine_id: UUID

    key_id: UUID


@pytest.fixture
def expected_player(
    test_params: TestMountMotorcycleParams,
    expected_rider: MotorcycleRiderDTO,  # pylint: disable=redefined-outer-name
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=expected_rider,
    )


@pytest.fixture
def expected_rider(
    test_params: TestMountMotorcycleParams,
    expected_motorcycle: MotorCycleDTO,  # pylint: disable=redefined-outer-name
    expected_key: MotorcycleKeyDTO,  # pylint: disable=redefined-outer-name
) -> MotorcycleRiderDTO:
    return MotorcycleRiderDTO(
        id=test_params.rider_id,
        motorcycle=expected_motorcycle,
        motorcycle_key=expected_key,
    )


@pytest.fixture
def expected_motorcycle(
    test_params: TestMountMotorcycleParams,
    expected_key: MotorcycleKeyDTO,  # pylint: disable=redefined-outer-name
    expected_engine: MotorcycleEngineDTO,  # pylint: disable=redefined-outer-name
) -> MotorCycleDTO:
    return MotorCycleDTO(
        id=test_params.motorcycle_id,
        rider_id=test_params.rider_id,
        key=expected_key,
        engine=expected_engine,
    )


@pytest.fixture
def expected_key(
    test_params: TestMountMotorcycleParams,
) -> MotorcycleKeyDTO:
    return MotorcycleKeyDTO(
        id=test_params.key_id,
        position=KeyPosition.ON,
    )


@pytest.fixture
def expected_engine(
    test_params: TestMountMotorcycleParams,
) -> MotorcycleEngineDTO:
    return MotorcycleEngineDTO(
        id=test_params.engine_id,
        running=True,
    )
