from oop.core.domain.player.rider.bicycle.model import BicycleRider
from oop.core.domain.player.riding.strategies.interface import RidingStrategyInterface
from oop.core.domain.transport.bicycle.model import Bicycle


class RideBicycleStrategy(RidingStrategyInterface):

    def execute(
        self,
        rider: BicycleRider,
        ride: Bicycle,
    ):
        rider.ride(ride=ride)
