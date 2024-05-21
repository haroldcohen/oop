from dataclasses import dataclass
from typing import List

from oop.core.domain.player.dto import PlayerDTO


@dataclass(frozen=True)
class WaterTileDTO:

    players: List[PlayerDTO]
