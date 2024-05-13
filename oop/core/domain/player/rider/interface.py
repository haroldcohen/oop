from abc import ABC, abstractmethod


class RiderInterface(ABC):

    @abstractmethod
    def ride(
        self,
        ride,
    ):
        pass

    @abstractmethod
    def to_dto(self):
        pass
