from dataclasses import dataclass, field
from typing import Union
from uuid import UUID

from oop.core.domain.player.location.dto import PlayerLocationDTO
from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.player.rider.horse.dto import HorseRiderDTO
from oop.core.domain.player.rider.motorcycle.dto import MotorcycleRiderDTO


@dataclass(frozen=True)
class PlayerDTO:
    id: UUID

    rider: Union[
        MotorcycleRiderDTO,
        BicycleRiderDTO,
        HorseRiderDTO,
    ]

    location: PlayerLocationDTO = field(default_factory=PlayerLocationDTO)
