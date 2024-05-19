from abc import ABC, abstractmethod
from uuid import UUID


class RideableInterface(ABC):

    @abstractmethod
    def mount(self, rider_id: UUID):
        pass
