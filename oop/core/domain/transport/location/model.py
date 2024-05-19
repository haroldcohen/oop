from oop.core.domain.transport.location.dto import TransportLocationDTO


class TransportLocation:

    def __init__(
        self,
        x_coordinates: int = 0,
        y_coordinates: int = 0,
    ):
        self._x_coordinates = x_coordinates
        self._y_coordinates = y_coordinates

    def move_forward(self):
        self._y_coordinates += 1

    def to_dto(self) -> TransportLocationDTO:
        return TransportLocationDTO(y_coordinates=self._y_coordinates)
