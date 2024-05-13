from uuid import UUID

from oop.core.domain.vehicle.horse.dto import HorseDTO
from oop.core.domain.vehicle.horse.equipment.saddle.model import Saddle
from oop.core.domain.vehicle.horse.interface import HorseInterface


class NullHorse(HorseInterface):

    def receive_pet(self):
        pass

    def equip_saddle(self, saddle: Saddle):
        pass

    def ride(self, rider_id: UUID):
        pass

    def to_dto(self) -> HorseDTO:
        pass
