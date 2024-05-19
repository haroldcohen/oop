from oop.core.domain.player.location.dto import PlayerLocationDTO


class PlayerLocation:

    def __init__(
        self,
        x_coordinates: int = 0,
        y_coordinates: int = 0,
    ):
        self._x_coordinates = x_coordinates
        self._y_coordinates = y_coordinates

    def move_forward(self):
        self._y_coordinates += 1

    def to_dto(self) -> PlayerLocationDTO:
        return PlayerLocationDTO(
            y_coordinates=self._y_coordinates,
        )
