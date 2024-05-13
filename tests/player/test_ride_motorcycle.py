from dataclasses import dataclass
from uuid import UUID, uuid4

import pytest

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.model import Player
from oop.core.domain.player.rider.motorcycle.dto import MotorcycleRiderDTO
from oop.core.domain.player.rider.motorcycle.model import MotorcycleRider
from oop.core.domain.player.riding.context import RidingContext
from oop.core.domain.player.riding.strategies.motorcycle import RideMotorcycleStrategy
from oop.core.domain.transport.motorcycle.dto import MotorCycleDTO
from oop.core.domain.transport.motorcycle.engine.dto import MotorcycleEngineDTO
from oop.core.domain.transport.motorcycle.engine.model import MotorcycleEngine
from oop.core.domain.transport.motorcycle.key.dto import MotorcycleKeyDTO
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.key.position import KeyPosition
from oop.core.domain.transport.motorcycle.model import Motorcycle


@dataclass(frozen=True)
class TestRideMotorcycleParams:
    player_id: UUID

    rider_id: UUID

    motorcycle_id: UUID

    engine_id: UUID

    key_id: UUID


@pytest.fixture
def expected_player(
    test_params: TestRideMotorcycleParams,
    expected_rider: MotorcycleRiderDTO,
) -> PlayerDTO:
    return PlayerDTO(
        id=test_params.player_id,
        rider=expected_rider,
    )


@pytest.fixture
def expected_rider(
    test_params: TestRideMotorcycleParams,
    expected_motorcycle: MotorCycleDTO,
) -> MotorcycleRiderDTO:
    return MotorcycleRiderDTO(
        id=test_params.rider_id,
        motorcycle=expected_motorcycle,
    )


@pytest.fixture
def expected_motorcycle(
    test_params: TestRideMotorcycleParams,
    expected_key: MotorcycleKeyDTO,
    expected_engine: MotorcycleEngineDTO,
) -> MotorCycleDTO:
    return MotorCycleDTO(
        id=test_params.motorcycle_id,
        rider_id=test_params.rider_id,
        key=expected_key,
        engine=expected_engine,
    )


@pytest.fixture
def expected_key(
    test_params: TestRideMotorcycleParams,
) -> MotorcycleKeyDTO:
    return MotorcycleKeyDTO(
        id=test_params.key_id,
        position=KeyPosition.ON,
    )


@pytest.fixture
def expected_engine(
    test_params: TestRideMotorcycleParams,
) -> MotorcycleEngineDTO:
    return MotorcycleEngineDTO(
        id=test_params.engine_id,
        running=True,
    )


@pytest.mark.parametrize(
    "test_params",
    [
        (
            TestRideMotorcycleParams(
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
    rider = MotorcycleRider(_id=expected_player.rider.id)
    motorcycle = Motorcycle(
        _id=expected_player.rider.motorcycle.id,
        engine=MotorcycleEngine(
            _id=expected_player.rider.motorcycle.engine.id,
        ),
    )
    riding_context = RidingContext(
        strategy=RideMotorcycleStrategy(keys=[MotorcycleKey(_id=expected_player.rider.motorcycle.key.id)])
    )
    player.ride(
        rider=rider,
        ride=motorcycle,
        riding_context=riding_context,
    )

    assert player.to_dto() == expected_player
