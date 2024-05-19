from uuid import UUID

from oop.core.domain.transport.bicycle.dto import BicycleDTO
from oop.core.domain.transport.null_rider_id import NullRiderId
from oop.core.domain.transport.rideable_interface import RideableInterface


class Bicycle(RideableInterface):

    def __init__(
        self,
        _id: UUID,
        rider_id: UUID = NullRiderId(),
    ):
        self._id = _id
        self._rider_id = rider_id

    def ride(
        self,
        rider_id: UUID,
    ):
        self._rider_id = rider_id

    def to_dto(self) -> BicycleDTO:
        return BicycleDTO(
            id=self._id,
            rider_id=self._rider_id,
        )
