from uuid import UUID

from oop.core.domain.map.interface import MapInterface
from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.interface import PlayerInterface
from oop.core.domain.player.location.model import PlayerLocation
from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.player.rider.null_rider.model import NullRider
from oop.core.domain.transport.rideable_interface import RideableInterface


class Player(PlayerInterface):

    def __init__(
        self,
        _id: UUID,
        rider: RiderInterface = NullRider(),
        location: PlayerLocation = PlayerLocation(),
    ):
        self._id = _id
        self._rider = rider
        self._location = location

    def mount(
        self,
        rider: RiderInterface,
        ride: RideableInterface,
    ):
        self._rider = rider
        self._rider.mount(ride=ride)

    def ride(
        self,
        distance: int,
        game_map: MapInterface,
    ):
        for _ in range(distance):
            game_map.navigate(
                player=self,
            )
            self._location.move_forward()
            self._rider.ride()

    def to_dto(self) -> PlayerDTO:
        return PlayerDTO(
            id=self._id,
            rider=self._rider.to_dto(),
            location=self._location.to_dto(),
        )
