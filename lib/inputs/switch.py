from gamepad import KeyCode
from input import Input

class Switch(Input):
    keybind : KeyCode

    def __init__(self, seat:int, name:str, keybind:KeyCode) -> None:
        super().__init__(seat, name)
        self.keybind = keybind

    def reset(self, seat:int) -> None:
        pass
    
    def getName(self) -> None:
        super().getName()

    def on(self, seat:int) -> None:
        self.seat = seat

    def off(self, seat:int) -> None:
        self.seat = seat