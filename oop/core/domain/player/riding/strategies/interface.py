from abc import ABC, abstractmethod
from typing import Union

from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.vehicle.bicycle.interface import BicycleInterface
from oop.core.domain.vehicle.motorcycle.interface import MotorcycleInterface


class RidingStrategyInterface(ABC):

    @abstractmethod
    def execute(
        self,
        rider: RiderInterface,
        ride: Union[
            MotorcycleInterface,
            BicycleInterface,
        ],
    ):
        pass
