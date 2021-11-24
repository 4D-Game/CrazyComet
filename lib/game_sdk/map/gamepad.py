from enum import IntEnum

class JoystickCode(IntEnum):
    """
        Shortcuts for the joystick
    """
    LEFT_Y = 0
    LEFT_X = 1
    RIGHT_Y = 2
    RIGHT_X = 3


class KeyCode(IntEnum):
    """
        Shortcuts for buttons
    """
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


class GamePad():
    """
        Stores key- and joystick maps. 
    """
    
    key_map : dict 
    joystick_map : dict 

    #wireless xbox360 controller
    key_map_xbox360 = {
        304 : KeyCode.BUT_0,
        305 : KeyCode.BUT_1,
        307 : KeyCode.BUT_2,
        308 : KeyCode.BUT_3,
        16 : KeyCode.DPAD_X,
        17 : KeyCode.DPAD_Y,
        310 : KeyCode.L1,
        10 : KeyCode.L2,
        311 : KeyCode.R1,
        9 : KeyCode.R2
    }

    joystick_map_xbox360 = {
        0 :	JoystickCode.LEFT_X,
        1 :	JoystickCode.LEFT_Y,
        3 :	JoystickCode.RIGHT_X,
        4 :	JoystickCode.RIGHT_Y
    }

    #wireless xbox controller
    key_map_xbox = {
        304 : KeyCode.BUT_0,
        305 : KeyCode.BUT_1,
        307 : KeyCode.BUT_2,
        308 : KeyCode.BUT_3,
        16 : KeyCode.DPAD_X,
        17 : KeyCode.DPAD_Y,
        310 : KeyCode.L1,
        10 : KeyCode.L2,
        311 : KeyCode.R1,
        9 : KeyCode.R2
    }

    joystick_map_xbox = {
        0 :	JoystickCode.LEFT_X,
        1 :	JoystickCode.LEFT_Y,
        2 :	JoystickCode.RIGHT_X,
        5 :	JoystickCode.RIGHT_Y
    }


    def __init__(self, name:str, key_map:dict, joystick_map:dict):
        """
            Creates used controller with related maps
            Arguments:
                name: name of controller
                key_map: contains code from controller and associated sdk-code for the switch
                joystick_map: contains code from controller and associated sdk-code the joystick
        """
        self.name = name
        self._key_map = key_map
        self._joystick_map = joystick_map

    def mapKey(self, code:int):
        """
            Get sdk-code for switch and joystick movements
            Arguments:
                code: original code from controller
        """
        if(code in self._key_map):
            return self._key_map[code]
        elif(code in self._joystick_map):
            return self._joystick_map[code]
        else:
            print("No key")
             
