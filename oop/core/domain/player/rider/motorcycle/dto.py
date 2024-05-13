from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.vehicle.motorcycle.dto import MotorCycleDTO


@dataclass(frozen=True)
class MotorcycleRiderDTO:

    id: UUID

    motorcycle: MotorCycleDTO
