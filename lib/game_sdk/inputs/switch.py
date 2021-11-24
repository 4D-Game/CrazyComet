from map.gamepad import KeyCode
from .input import Input

class Switch(Input):
    """
        Class for button inputs
    """

    keybind : KeyCode

    def __init__(self, seat:int, name:str, keybind:KeyCode):
        """
            Initializes the switch 
            Arguments:
                seat: controller seat
                name: controller name
                keybind = controller buttons
        """
        super().__init__(seat, name)
        self.keybind = keybind

    def on(self, seat:int):
        """
            Turn switch on
            Arguments:
                seat: controller seat 
        """
        pass
    
    def off(self, seat:int):            
        """"
            Turn switch off
            Arguments:
                seat: controller seat 
        """
        pass