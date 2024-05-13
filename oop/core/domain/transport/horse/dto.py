from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.horse.equipment.saddle.dto import SaddleDTO


@dataclass(frozen=True)
class HorseDTO:
    id: UUID

    rider_id: UUID

    is_calm: bool

    saddle: SaddleDTO
