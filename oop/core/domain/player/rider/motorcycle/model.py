from uuid import UUID

from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.player.rider.motorcycle.dto import MotorcycleRiderDTO
from oop.core.domain.vehicle.motorcycle.interface import MotorcycleInterface
from oop.core.domain.vehicle.motorcycle.key.model import MotorcycleKey
from oop.core.domain.vehicle.motorcycle.null_motorcycle import NullMotorcycle


class MotorcycleRider(RiderInterface):

    def __init__(
        self,
        _id: UUID,
        motorcycle: MotorcycleInterface = NullMotorcycle(),
    ):
        self._id = _id
        self._motorcycle = motorcycle

    def ride(
        self,
        ride: MotorcycleInterface,
    ):
        self._motorcycle = ride
        self._motorcycle.ride(
            rider_id=self._id,
        )

    def start_motorcycle(
        self,
        motorcycle_key: MotorcycleKey,
    ):
        self._motorcycle.start(
            key=motorcycle_key,
        )

    def to_dto(self) -> MotorcycleRiderDTO:
        return MotorcycleRiderDTO(id=self._id, motorcycle=self._motorcycle.to_dto())
