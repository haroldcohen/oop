from typing import List

from oop.core.domain.player.rider.motorcycle.model import MotorcycleRider
from oop.core.domain.player.riding.strategies.interface import RidingStrategyInterface
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.model import Motorcycle


class RideMotorcycleStrategy(RidingStrategyInterface):

    def __init__(
        self,
        keys: List[MotorcycleKey],
    ):
        self._keys = keys

    def execute(
        self,
        rider: MotorcycleRider,
        ride: Motorcycle,
    ):
        rider.ride(ride=ride)
        rider.start_motorcycle(motorcycle_key=self._keys[0])
