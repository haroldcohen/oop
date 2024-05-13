from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.player.riding.strategies.interface import RidingStrategyInterface
from oop.core.domain.vehicle.rideable_interface import RideableInterface


class RidingContext:

    def __init__(
        self,
        strategy: RidingStrategyInterface,
    ):
        self._strategy = strategy

    def change_strategy(
        self,
        strategy: RidingStrategyInterface,
    ):
        self._strategy = strategy

    def execute_strategy(self, rider: RiderInterface, ride: RideableInterface):
        self._strategy.execute(
            rider=rider,
            ride=ride,
        )
