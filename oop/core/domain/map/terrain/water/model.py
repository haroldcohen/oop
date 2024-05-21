from typing import List

from oop.core.domain.map.terrain.tile_interface import TileInterface
from oop.core.domain.map.terrain.water.dto import WaterTileDTO
from oop.core.domain.player.model import Player


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
    ):
        self._players.append(player)
        player.fall()

    def to_dto(self) -> WaterTileDTO:
        return WaterTileDTO(
            players=[player.to_dto() for player in self._players],
        )
