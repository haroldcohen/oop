from oop.core.domain.player.model import Player
from oop.core.domain.player.travel.strategies.interface import TravelStrategyInterface


class TravelByFootDefaultStrategy(TravelStrategyInterface):

    def execute(
        self,
        player: Player,
    ):
        player.walk()
