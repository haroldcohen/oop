from uuid import UUID

from oop.core.domain.common.null_id import NullId
from oop.core.domain.transport.horse.dto import HorseDTO
from oop.core.domain.transport.horse.equipment.saddle.interface import SaddleInterface
from oop.core.domain.transport.horse.equipment.saddle.model import Saddle
from oop.core.domain.transport.horse.equipment.saddle.null_saddle import NullSaddle
from oop.core.domain.transport.rideable_interface import RideableInterface


class Horse(RideableInterface):

    def __init__(
        self,
        _id: UUID,
        is_calm: bool = False,
        rider_id: UUID = NullId(),
        saddle: SaddleInterface = NullSaddle(),
    ):
        self._id = _id
        self._rider_id = rider_id
        self._is_calm = is_calm
        self._saddle = saddle

    def receive_pet(self):
        self._is_calm = True

    def equip_saddle(self, saddle: Saddle):
        self._saddle = saddle
        self._saddle.equip()

    def mount(self, rider_id: UUID):
        self._rider_id = rider_id

    def to_dto(self) -> HorseDTO:
        return HorseDTO(id=self._id, rider_id=self._rider_id, is_calm=self._is_calm, saddle=self._saddle.to_dto())
