from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.motorcycle.dto import MotorCycleDTO


@dataclass(frozen=True)
class MotorcycleRiderDTO:

    id: UUID

    motorcycle: MotorCycleDTO
