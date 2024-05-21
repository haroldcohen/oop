from dataclasses import dataclass, field
from typing import List

from oop.core.domain.player.dto import PlayerDTO


@dataclass(frozen=True)
class WaterTileDTO:

    players: List[PlayerDTO] = field(default_factory=list)
