from abc import ABC, abstractmethod

from oop.core.domain.vehicle.motorcycle.key.dto import MotorcycleKeyDTO


class MotorcycleKeyInterface(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def to_dto(self) -> MotorcycleKeyDTO:
        pass
