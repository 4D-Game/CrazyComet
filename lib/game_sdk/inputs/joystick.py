from map.gamepad import JoystickCode
from .input import Input

class Joystick(Input):
    """
        Class for all joystick inputs 
    """

    joystick_pos : JoystickCode

    def __init__(self, seat:int, name:str, joystick_pos:JoystickCode):
        """
            Initializes the joystick 
            Arguments:
                seat: controller seat
                name: controller name
                joystick_pos = joystick position, x&y coordinates
        """
        super().__init__(seat, name)
        self.joystick_pos = joystick_pos

    def get_direction(self, x:int, y:int):
        """
            Returns directions from the joystick
            Arguments:
                x: x-coordinate of movement
                y: y-coordinate of movement
        """
        pass