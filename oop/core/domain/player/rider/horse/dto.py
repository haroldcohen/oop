from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.horse.dto import HorseDTO


@dataclass(frozen=True)
class HorseRiderDTO:
    id: UUID

    horse: HorseDTO
