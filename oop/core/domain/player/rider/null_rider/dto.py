from dataclasses import dataclass, field
from uuid import UUID

from oop.core.domain.common.null_id import NullId


@dataclass(frozen=True)
class NullRiderDTO:

    id: UUID = field(default_factory=NullId)
