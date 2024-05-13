from typing import List

from oop.core.domain.player.rider.horse.model import HorseRider
from oop.core.domain.player.riding.strategies.interface import RidingStrategyInterface
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle
from oop.core.domain.transport.horse.model import Horse


class RideHorseStrategy(RidingStrategyInterface):

    def __init__(
        self,
        saddles: List[Saddle],
    ):
        self._saddles = saddles

    def execute(
        self,
        rider: HorseRider,
        ride: Horse,
    ):
        rider.pet(horse=ride)
        rider.equip_saddle(
            saddle=self._saddles[0],
            horse=ride,
        )
        rider.ride(ride)
