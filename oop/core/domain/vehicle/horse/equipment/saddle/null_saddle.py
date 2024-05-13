from oop.core.domain.vehicle.horse.equipment.saddle.dto import SaddleDTO
from oop.core.domain.vehicle.horse.equipment.saddle.interface import SaddleInterface


class NullSaddle(SaddleInterface):

    def to_dto(self) -> SaddleDTO:
        pass
