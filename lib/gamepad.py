from enum import IntEnum

class JoystickCode(IntEnum):
    LEFT_Y = 0
    LEFT_X = 1
    RIGHT_Y = 2
    RIGHT_X = 3

class KeyCode(IntEnum):
    BUT_0 = 0
    BUT_1 = 1
    BUT_2 = 2
    BUT_3 = 3
    DPAD_X = 4
    DPAD_Y = 5
    L1 = 6
    L2 = 7 
    R1 = 8
    R2 = 9

class GamePad:
    key_map : dict 
    joystick_map : dict 