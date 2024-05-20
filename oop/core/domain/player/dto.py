from dataclasses import dataclass, field
from typing import Generic, TypeVar
from uuid import UUID

from oop.core.domain.player.location.dto import PlayerLocationDTO

RiderDTO = TypeVar("RiderDTO")


@dataclass(frozen=True)
class PlayerDTO(Generic[RiderDTO]):
    id: UUID

    rider: RiderDTO

    location: PlayerLocationDTO = field(default_factory=PlayerLocationDTO)
