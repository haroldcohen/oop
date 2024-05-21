from abc import ABC, abstractmethod

from oop.core.domain.player.model import Player


class TravelStrategyInterface(ABC):

    @abstractmethod
    def execute(
        self,
        player: Player,
    ):
        pass
