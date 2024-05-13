from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.motorcycle.engine.dto import MotorcycleEngineDTO
from oop.core.domain.transport.motorcycle.key.dto import MotorcycleKeyDTO


@dataclass(frozen=True, slots=True)
class MotorCycleDTO:
    id: UUID

    rider_id: UUID

    key: MotorcycleKeyDTO

    engine: MotorcycleEngineDTO
