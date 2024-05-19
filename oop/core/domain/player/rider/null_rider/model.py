from oop.core.domain.player.rider.interface import RiderInterface


class NullRider(RiderInterface):

    def mount(self, ride):
        pass

    def ride(self):
        pass

    def to_dto(self):
        pass
