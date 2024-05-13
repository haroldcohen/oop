from uuid import UUID

from oop.core.domain.transport.motorcycle.key.dto import MotorcycleKeyDTO
from oop.core.domain.transport.motorcycle.key.position import KeyPosition


class MotorcycleKey:

    def __init__(
        self,
        _id: UUID,
        position: KeyPosition = KeyPosition.OFF,
    ):
        self._id = _id
        self._position = position

    def turn_on(self):
        self._position = KeyPosition.ON

    def to_dto(self) -> MotorcycleKeyDTO:
        return MotorcycleKeyDTO(
            id=self._id,
            position=self._position,
        )
