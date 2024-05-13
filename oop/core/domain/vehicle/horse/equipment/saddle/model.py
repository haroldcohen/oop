from uuid import UUID

from oop.core.domain.vehicle.horse.equipment.saddle.dto import SaddleDTO
from oop.core.domain.vehicle.horse.equipment.saddle.interface import SaddleInterface


class Saddle(SaddleInterface):

    def __init__(
        self,
        _id: UUID,
        is_equipped: bool = False,
    ):
        self._id = _id
        self._is_equipped = is_equipped

    def equip(self):
        self._is_equipped = True

    def to_dto(self) -> SaddleDTO:
        return SaddleDTO(
            id=self._id,
            is_equipped=self._is_equipped,
        )
