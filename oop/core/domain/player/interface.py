from abc import ABC, abstractmethod


class PlayerInterface(ABC):

    @abstractmethod
    def ride(self):
        pass
