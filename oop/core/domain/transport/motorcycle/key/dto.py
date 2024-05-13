from dataclasses import dataclass
from uuid import UUID

from oop.core.domain.transport.motorcycle.key.position import KeyPosition


@dataclass(frozen=True)
class MotorcycleKeyDTO:

    id: UUID

    position: KeyPosition
