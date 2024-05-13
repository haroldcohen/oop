from dataclasses import dataclass
from typing import Union
from uuid import UUID

from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.player.rider.motorcycle.dto import MotorcycleRiderDTO


@dataclass(frozen=True)
class PlayerDTO:
    id: UUID

    rider: Union[
        MotorcycleRiderDTO,
        BicycleRiderDTO,
    ]
