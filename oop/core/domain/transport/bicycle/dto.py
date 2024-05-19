from dataclasses import dataclass, field
from uuid import UUID

from oop.core.domain.transport.location.dto import TransportLocationDTO


@dataclass(frozen=True, slots=True)
class BicycleDTO:
    id: UUID

    rider_id: UUID

    location: TransportLocationDTO = field(default_factory=TransportLocationDTO)
