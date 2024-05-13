from uuid import UUID

from oop.core.domain.vehicle.motorcycle.engine.dto import MotorcycleEngineDTO


class MotorcycleEngine:

    def __init__(
        self,
        _id: UUID,
        running: bool = False,
    ):
        self._id = _id
        self._running = running

    def start(self):
        self._running = True

    def to_dto(self) -> MotorcycleEngineDTO:
        return MotorcycleEngineDTO(
            id=self._id,
            running=self._running,
        )
