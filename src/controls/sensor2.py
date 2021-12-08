import logging
import sys
sys.path.insert(0, '/home/pi/CrazyComet/Controller/')
from game_sdk.controller.inputs.switch import Switch

class Sensor(Switch):
    """
        Input class for sensor 
    """

    def __init__(self, seat, name):
        super().__init__(seat, name)


sens = Sensor(1,"hi")
print(f"{sens}")