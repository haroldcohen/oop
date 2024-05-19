from dataclasses import dataclass, field


@dataclass(frozen=True)
class PlayerLocationDTO:

    x_coordinates: int = field(default=0)

    y_coordinates: int = field(default=0)
