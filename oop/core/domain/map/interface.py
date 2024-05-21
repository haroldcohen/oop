from abc import ABC, abstractmethod

from oop.core.domain.player.interface import PlayerInterface
from oop.core.domain.player.travel.strategy import TravelStrategy


class MapInterface(ABC):

    @abstractmethod
    def navigate(
        self,
        player: PlayerInterface,
        strategy: TravelStrategy,
    ):
        pass
