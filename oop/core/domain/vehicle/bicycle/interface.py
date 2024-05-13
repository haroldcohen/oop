from abc import ABC, abstractmethod

from oop.core.domain.vehicle.bicycle.dto import BicycleDTO


class BicycleInterface(ABC):

    @abstractmethod
    def to_dto(self) -> BicycleDTO:
        pass
