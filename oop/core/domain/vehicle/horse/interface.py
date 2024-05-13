from abc import ABC, abstractmethod
from uuid import UUID

from oop.core.domain.vehicle.horse.dto import HorseDTO
from oop.core.domain.vehicle.horse.equipment.saddle.model import Saddle


class HorseInterface(ABC):

    @abstractmethod
    def receive_pet(self):
        pass

    @abstractmethod
    def equip_saddle(self, saddle: Saddle):
        pass

    @abstractmethod
    def ride(self, rider_id: UUID):
        pass

    @abstractmethod
    def to_dto(self) -> HorseDTO:
        pass
