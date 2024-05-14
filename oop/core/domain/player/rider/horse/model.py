from uuid import UUID

from oop.core.domain.player.rider.horse.dto import HorseRiderDTO
from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle
from oop.core.domain.transport.horse.interface import HorseInterface
from oop.core.domain.transport.horse.model import Horse
from oop.core.domain.transport.horse.null_horse import NullHorse


class HorseRider(RiderInterface):

    def __init__(
        self,
        _id: UUID,
        saddle: Saddle,
        horse: HorseInterface = NullHorse(),
    ):
        self._id = _id
        self._saddle = saddle
        self._horse = horse

    def ride(self, ride: Horse):
        ride.receive_pet()
        ride.equip_saddle(saddle=self._saddle)
        self._horse = ride
        self._horse.ride(rider_id=self._id)

    def to_dto(self) -> HorseRiderDTO:
        return HorseRiderDTO(
            id=self._id,
            horse=self._horse.to_dto(),
            saddle=self._saddle.to_dto(),
        )
