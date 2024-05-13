from uuid import UUID

from oop.core.domain.player.dto import PlayerDTO
from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.player.rider.null_rider.model import NullRider
from oop.core.domain.player.riding.context import RidingContext
from oop.core.domain.transport.rideable_interface import RideableInterface


class Player:

    def __init__(
        self,
        _id: UUID,
        rider: RiderInterface = NullRider(),
    ):
        self._id = _id
        self._rider = rider

    def ride(
        self,
        rider: RiderInterface,
        ride: RideableInterface,
        riding_context: RidingContext,
    ):
        self._rider = rider
        riding_context.execute_strategy(
            rider=rider,
            ride=ride,
        )

    def to_dto(self) -> PlayerDTO:
        return PlayerDTO(
            id=self._id,
            rider=self._rider.to_dto(),
        )
