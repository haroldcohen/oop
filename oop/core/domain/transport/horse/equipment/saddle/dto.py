from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class SaddleDTO:

    id: UUID

    is_equipped: True
