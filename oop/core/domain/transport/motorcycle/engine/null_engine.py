from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.motorcycle.engine.model import MotorcycleEngine


class NullMotorcycleEngine(MotorcycleEngine):

    def __init__(self):
        super().__init__(_id=NullId())

    def start(self):
        pass
