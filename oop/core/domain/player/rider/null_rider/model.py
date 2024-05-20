from oop.core.domain.player.rider.interface import RiderInterface
from oop.core.domain.player.rider.null_rider.dto import NullRiderDTO


class NullRider(RiderInterface):

    def mount(self, ride):
        pass

    def ride(self):
        pass

    def to_dto(self) -> NullRiderDTO:
        return NullRiderDTO()
