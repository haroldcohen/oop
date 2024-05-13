from oop.core.domain.player.rider.interface import RiderInterface


class NullRider(RiderInterface):

    def ride(self, ride):
        pass

    def to_dto(self):
        pass
