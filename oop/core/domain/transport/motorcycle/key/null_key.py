from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.motorcycle.key.model import MotorcycleKey
from oop.core.domain.transport.motorcycle.key.position import KeyPosition


class NullMotorcycleKey(MotorcycleKey):

    def __init__(self):
        super().__init__(_id=NullId(), position=KeyPosition.NULL)

    def turn_on(self):
        pass
