from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.motorcycle.dto import MotorCycleDTO
from oop.core.domain.transport.motorcycle.key.dto import MotorcycleKeyDTO


@dataclass(frozen=True)
class MotorcycleRiderDTO:

    id: UUID

    motorcycle: MotorCycleDTO

    motorcycle_key: MotorcycleKeyDTO
