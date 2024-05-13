from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class BicycleDTO:
    id: UUID

    rider_id: UUID
