from uuid import UUID

from oop.core.domain.player.rider.horse.dto import HorseRiderDTO
from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle
from oop.core.domain.transport.horse.interface import HorseInterface
from oop.core.domain.transport.horse.null_horse import NullHorse


class HorseRider(RiderInterface):

    def __init__(
        self,
        _id: UUID,
        horse: HorseInterface = NullHorse(),
    ):
        self._id = _id
        self._horse = horse

    def pet(self, horse: HorseInterface):
        horse.receive_pet()

    def equip_saddle(
        self,
        saddle: Saddle,
        horse: HorseInterface,
    ):
        horse.equip_saddle(saddle=saddle)

    def ride(self, ride: HorseInterface):
        self._horse = ride
        self._horse.ride(rider_id=self._id)

    def to_dto(self) -> HorseRiderDTO:
        return HorseRiderDTO(id=self._id, horse=self._horse.to_dto())
