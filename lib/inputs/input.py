from abc import ABC, abstractmethod

class Input(ABC):
    @abstractmethod
    def __init__(self, seat:int, name:str) -> None:
        self.seat = seat
        self.name = name

    @abstractmethod
    def reset(self, seat:int) -> None:
        pass
    
    @abstractmethod
    def getName(self) -> None:
        pass