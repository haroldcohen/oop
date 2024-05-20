from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class MapDTO:
    terrain: List
