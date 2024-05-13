from uuid import UUID

from oop.core.domain.transport.bicycle.dto import BicycleDTO
from oop.core.domain.transport.bicycle.interface import BicycleInterface


class NullBicycle(BicycleInterface):

    def ride(self, rider_id: UUID):
        pass

    def to_dto(self) -> BicycleDTO:
        pass