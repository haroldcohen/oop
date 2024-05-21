# pylint: disable=duplicate-code
from typing import List

from oop.core.domain.map.terrain.tile_interface import TileInterface
from oop.core.domain.map.terrain.water.dto import WaterTileDTO
from oop.core.domain.player.model import Player
from oop.core.domain.player.travel.context import TravelContext
from oop.core.domain.player.travel.strategies.bicycle.water import TravelByBicycleOnWaterStrategy
from oop.core.domain.player.travel.strategies.foot.default import TravelByFootDefaultStrategy
from oop.core.domain.player.travel.strategy import TravelStrategy


class WaterTile(TileInterface):

    def __init__(
        self,
        players: List[Player],
    ):
        self._players = players

    def remove_player(
        self,
        player: Player,
    ):
        self._players.remove(player)

    def move_player(
        self,
        player: Player,
        strategy: TravelStrategy,
    ):
        self._players.append(player)
        travel_strategy = TravelByFootDefaultStrategy()
        if strategy == TravelStrategy.BY_BICYCLE:
            travel_strategy = TravelByBicycleOnWaterStrategy()
        travel_context = TravelContext(strategy=travel_strategy)
        travel_context.execute_strategy(player=player)

    def to_dto(self) -> WaterTileDTO:
        return WaterTileDTO(
            players=[player.to_dto() for player in self._players],
        )
