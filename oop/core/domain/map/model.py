from typing import List

from oop.core.domain.map.dto import MapDTO
from oop.core.domain.map.interface import MapInterface
from oop.core.domain.map.terrain.tile_interface import TileInterface
from oop.core.domain.player.model import Player
from oop.core.domain.player.travel.strategy import TravelStrategy


class Map(MapInterface):

    def __init__(
        self,
        terrain: List[List[TileInterface]],
    ):
        self._terrain = terrain

    def navigate(
        self,
        player: Player,
        strategy: TravelStrategy,
    ):
        player_dto = player.to_dto()
        player_y_coordinates = player_dto.location.y_coordinates
        current_tile = self._terrain[player_y_coordinates][0]
        current_tile.remove_player(player=player)
        destination_tile = self._terrain[player_y_coordinates + 1][0]
        destination_tile.move_player(
            player=player,
            strategy=strategy,
        )

    def to_dto(self) -> MapDTO:
        terrain = [[tile.to_dto() for tile in _] for _ in self._terrain]
        return MapDTO(terrain=terrain)
