from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.bicycle.dto import BicycleDTO


@dataclass(frozen=True, slots=True)
class BicycleRiderDTO:
    id: UUID

    bicycle: BicycleDTO
