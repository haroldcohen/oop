from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.vehicle.motorcycle.engine.dto import MotorcycleEngineDTO
from oop.core.domain.vehicle.motorcycle.key.dto import MotorcycleKeyDTO


@dataclass(frozen=True, slots=True)
class MotorCycleDTO:
    id: UUID

    rider_id: UUID

    key: MotorcycleKeyDTO

    engine: MotorcycleEngineDTO
