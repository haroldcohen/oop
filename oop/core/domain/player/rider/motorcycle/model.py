from uuid import UUID

from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.player.rider.motorcycle.dto import MotorcycleRiderDTO
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.model import Motorcycle
from oop.core.domain.transport.motorcycle.null_motorcycle import NullMotorcycle


class MotorcycleRider(RiderInterface):

    def __init__(
        self,
        _id: UUID,
        motorcycle_key: MotorcycleKey,
        motorcycle: Motorcycle = NullMotorcycle(),
    ):
        self._id = _id
        self._motorcycle_key = motorcycle_key
        self._motorcycle = motorcycle

    def ride(
        self,
        ride: Motorcycle,
    ):
        self._motorcycle = ride
        self._motorcycle.start(
            key=self._motorcycle_key,
        )
        self._motorcycle.ride(
            rider_id=self._id,
        )

    def to_dto(self) -> MotorcycleRiderDTO:
        return MotorcycleRiderDTO(
            id=self._id,
            motorcycle=self._motorcycle.to_dto(),
            motorcycle_key=self._motorcycle_key.to_dto(),
        )
