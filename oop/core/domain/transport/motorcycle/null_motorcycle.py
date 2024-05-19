from uuid import UUID

from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.motorcycle.engine.null_engine import NullMotorcycleEngine
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.model import Motorcycle


class NullMotorcycle(Motorcycle):

    def __init__(
        self,
    ):
        super().__init__(_id=NullId(), engine=NullMotorcycleEngine())

    def start(self, key: MotorcycleKey):
        pass

    def ride(self, rider_id: UUID):
        pass

    def to_dto(self):
        pass
