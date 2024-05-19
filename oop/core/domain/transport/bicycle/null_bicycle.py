from uuid import UUID

from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.bicycle.model import Bicycle


class NullBicycle(Bicycle):

    def __init__(
        self,
    ):
        super().__init__(_id=NullId())

    def ride(self, rider_id: UUID):
        pass
