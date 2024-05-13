from abc import ABC, abstractmethod
from uuid import UUID

from oop.core.domain.vehicle.motorcycle.key.model import MotorcycleKey


class MotorcycleInterface(ABC):

    @abstractmethod
    def start(self, key: MotorcycleKey):
        pass

    @abstractmethod
    def ride(self, rider_id: UUID):
        pass

    @abstractmethod
    def to_dto(self):
        pass
