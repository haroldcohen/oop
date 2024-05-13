from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class MotorcycleEngineDTO:

    id: UUID

    running: bool
