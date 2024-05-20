from typing import List

from oop.core.domain.map.terrain.dirt.dto import DirtTileDTO
from oop.core.domain.player.model import Player


class DirtTile:

    def __init__(
        self,
        players: List[Player],
    ):
        self._players = players

    def remove_player(
        self,
        player,
    ):
        self._players.remove(player)

    def move_player(
        self,
        player,
    ):
        self._players.append(player)

    def to_dto(self) -> DirtTileDTO:
        return DirtTileDTO(
            players=[player.to_dto() for player in self._players],
        )
