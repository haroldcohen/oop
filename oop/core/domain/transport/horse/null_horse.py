from uuid import UUID

from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle
from oop.core.domain.transport.horse.model import Horse


class NullHorse(Horse):

    def __init__(self):
        super().__init__(_id=NullId())

    def receive_pet(self):
        pass

    def equip_saddle(self, saddle: Saddle):
        pass

    def ride(self, rider_id: UUID):
        pass
