from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.vehicle.bicycle.dto import BicycleDTO


@dataclass(frozen=True, slots=True)
class BicycleRiderDTO:
    id: UUID

    bicycle: BicycleDTO
