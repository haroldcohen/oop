from abc import ABC, abstractmethod

from oop.core.domain.player.interface import PlayerInterface


class MapInterface(ABC):

    @abstractmethod
    def navigate(
        self,
        player: PlayerInterface,
    ):
        pass
