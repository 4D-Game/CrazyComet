from gamepad import JoystickCode
from input import Input

class Joystick(Input):
    joystick_pos : JoystickCode

    def __init__(self, seat:int, name:str, joystick_pos:JoystickCode) -> None:
        super().__init__(seat, name)
        self.joystick_pos = joystick_pos

    def reset(self, seat:int) -> None:
        pass
    
    def getName(self) -> None:
        super().getName()

    def get_direction(self, x:int, y:int) -> None:
        pass