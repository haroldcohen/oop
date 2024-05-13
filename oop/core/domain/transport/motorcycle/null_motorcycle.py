from uuid import UUID

from oop.core.domain.transport.motorcycle.interface import MotorcycleInterface
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey


class NullMotorcycle(MotorcycleInterface):

    def start(self, key: MotorcycleKey):
        pass

    def ride(self, rider_id: UUID):
        pass

    def to_dto(self):
        pass
