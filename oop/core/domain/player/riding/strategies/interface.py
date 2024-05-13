from abc import ABC, abstractmethod

from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.vehicle.rideable_interface import RideableInterface


class RidingStrategyInterface(ABC):

    @abstractmethod
    def execute(
        self,
        rider: RiderInterface,
        ride: RideableInterface,
    ):
        pass
