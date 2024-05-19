from uuid import UUID

from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.bicycle.dto import BicycleDTO
from oop.core.domain.transport.location.model import TransportLocation
from oop.core.domain.transport.rideable_interface import RideableInterface


class Bicycle(RideableInterface):

    def __init__(
        self,
        _id: UUID,
        rider_id: UUID = NullId(),
        location: TransportLocation = TransportLocation(),
    ):
        self._id = _id
        self._rider_id = rider_id
        self._location = location

    def mount(
        self,
        rider_id: UUID,
    ):
        self._rider_id = rider_id

    def move_forward(self):
        self._location.move_forward()

    def to_dto(self) -> BicycleDTO:
        return BicycleDTO(
            id=self._id,
            rider_id=self._rider_id,
            location=self._location.to_dto(),
        )
