from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.horse.dto import HorseDTO
from oop.core.domain.transport.horse.equipment.saddle.dto import SaddleDTO


@dataclass(frozen=True)
class HorseRiderDTO:
    id: UUID

    horse: HorseDTO

    saddle: SaddleDTO
