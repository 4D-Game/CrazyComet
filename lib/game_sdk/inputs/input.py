from abc import ABC, abstractmethod


class Input(ABC):
    """
        Base class for all user inputs
    """

    @abstractmethod
    def __init__(self, seat: int, name: str):
        """
            Abstract init method
            Arguments:
                seat: controller seat
                name: controller name
        """
        self._name = name

    def reset(self, seat: int):
        """
            Executed at the end of the game. Resets all controller inputs
        """
        pass

    @property
    def name(self):
        """
            control name
        """
        return self._name
