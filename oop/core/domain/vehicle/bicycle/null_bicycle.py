from uuid import UUID

from oop.core.domain.vehicle.bicycle.dto import BicycleDTO
from oop.core.domain.vehicle.bicycle.interface import BicycleInterface


class NullBicycle(BicycleInterface):

    def ride(self, rider_id: UUID):
        pass

    def to_dto(self) -> BicycleDTO:
        pass
