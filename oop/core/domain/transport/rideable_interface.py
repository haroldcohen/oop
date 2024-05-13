from abc import ABC, abstractmethod
from uuid import UUID


class RideableInterface(ABC):

    @abstractmethod
    def ride(self, rider_id: UUID):
        pass
