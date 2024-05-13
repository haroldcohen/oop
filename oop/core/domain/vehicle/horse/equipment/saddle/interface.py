from abc import ABC, abstractmethod

from oop.core.domain.vehicle.horse.equipment.saddle.dto import SaddleDTO


class SaddleInterface(ABC):

    @abstractmethod
    def to_dto(self) -> SaddleDTO:
        pass
