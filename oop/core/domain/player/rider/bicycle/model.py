from uuid import UUID

from oop.core.domain.player.rider.bicycle.dto import BicycleRiderDTO
from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.transport.bicycle.interface import BicycleInterface
from oop.core.domain.transport.bicycle.model import Bicycle
from oop.core.domain.transport.bicycle.null_bicycle import NullBicycle


class BicycleRider(RiderInterface):

    def __init__(
        self,
        _id: UUID,
        bicycle: BicycleInterface = NullBicycle(),
    ):
        self._id = _id
        self._bicycle = bicycle

    def ride(self, ride: Bicycle):
        self._bicycle = ride
        self._bicycle.ride(rider_id=self._id)

    def to_dto(self) -> BicycleRiderDTO:
        return BicycleRiderDTO(
            id=self._id,
            bicycle=self._bicycle.to_dto(),
        )
