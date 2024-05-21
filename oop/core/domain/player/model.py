from uuid import UUID

from oop.core.domain.map.interface import MapInterface
from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.interface import PlayerInterface
from oop.core.domain.player.location.model import PlayerLocation
from oop.core.domain.player.position import PlayerPosition
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
        self._position = PlayerPosition.SEATING

    def mount(
        self,
        rider: RiderInterface,
        ride: RideableInterface,
    ):
        self._rider = rider
        self._rider.mount(ride=ride)

    def travel(
        self,
        distance: int,
        game_map: MapInterface,
    ):
        distance_to_run = distance
        while self._position != PlayerPosition.LAYING_DOWN and distance_to_run:
            game_map.navigate(
                player=self,
            )
            self.ride()
            distance_to_run -= 1

    def ride(self):
        self._location.move_forward()
        self._rider.ride()

    def fall(self):
        self._position = PlayerPosition.LAYING_DOWN

    def to_dto(self) -> PlayerDTO:
        return PlayerDTO(
            id=self._id,
            rider=self._rider.to_dto(),
            location=self._location.to_dto(),
            position=self._position,
        )
