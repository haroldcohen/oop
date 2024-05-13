from abc import ABC, abstractmethod

from oop.core.domain.transport.horse.dto import HorseDTO
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle


class HorseInterface(ABC):

    @abstractmethod
    def receive_pet(self):
        pass

    @abstractmethod
    def equip_saddle(self, saddle: Saddle):
        pass

    @abstractmethod
    def to_dto(self) -> HorseDTO:
        pass
