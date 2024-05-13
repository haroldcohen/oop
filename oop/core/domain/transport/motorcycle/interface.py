from abc import ABC, abstractmethod

from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey


class MotorcycleInterface(ABC):

    @abstractmethod
    def start(self, key: MotorcycleKey):
        pass

    @abstractmethod
    def to_dto(self):
        pass
