from oop.core.domain.player.model import Player
from oop.core.domain.player.travel.strategies.interface import TravelStrategyInterface


class TravelContext:

    def __init__(
        self,
        strategy: TravelStrategyInterface,
    ):
        self._strategy = strategy

    def execute_strategy(
        self,
        player: Player,
    ):
        self._strategy.execute(player=player)
