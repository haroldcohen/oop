from uuid import UUID

from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.motorcycle.dto import MotorCycleDTO
from oop.core.domain.transport.motorcycle.engine.model import MotorcycleEngine
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.key.null_key import NullMotorcycleKey
from oop.core.domain.transport.rideable_interface import RideableInterface


class Motorcycle(RideableInterface):

    def __init__(
        self,
        _id: UUID,
        engine: MotorcycleEngine,
        key: MotorcycleKey = NullMotorcycleKey(),
        rider_id: UUID = NullId(),
    ):
        self._id = _id
        self._key = key
        self._rider_id = rider_id
        self._engine = engine

    def mount(
        self,
        rider_id: UUID,
    ):
        self._rider_id = rider_id

    def start(
        self,
        key: MotorcycleKey,
    ):
        self._key = key
        self._key.turn_on()
        self._engine.start()

    def to_dto(self) -> MotorCycleDTO:
        return MotorCycleDTO(
            id=self._id,
            rider_id=self._rider_id,
            key=self._key.to_dto(),
            engine=self._engine.to_dto(),
        )
