from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from oop.core.domain.player.model import Player
from oop.core.domain.player.travel.strategy import TravelStrategy

TileDTO = TypeVar("TileDTO")


class TileInterface(ABC, Generic[TileDTO]):

    @abstractmethod
    def remove_player(
        self,
        player: Player,
    ):
        pass

    @abstractmethod
    def move_player(
        self,
        player: Player,
        strategy: TravelStrategy,
    ):
        pass

    @abstractmethod
    def to_dto(self) -> TileDTO:
        pass
