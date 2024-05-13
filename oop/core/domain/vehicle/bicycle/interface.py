from abc import ABC, abstractmethod
from uuid import UUID

from oop.core.domain.vehicle.bicycle.dto import BicycleDTO


class BicycleInterface(ABC):

    @abstractmethod
    def ride(self, rider_id: UUID):
        pass

    @abstractmethod
    def to_dto(self) -> BicycleDTO:
        pass
