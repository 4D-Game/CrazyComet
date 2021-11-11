from time import sleep
from typing import List

from surrortg.inputs.switch import Switch
from ..hardware.turrets import TurretPosHAL, TurretShootHAL
from surrortg.inputs import MouseJoystick
import logging


class TurretPositionControl(MouseJoystick):
    """
        Joystick wich controls the turrets
    """

    def __init__(self):
        pin = 0  # Read config

        # init controller
        self.controller = TurretPosHAL(pin)

        logging.info("Turret Positioncontrol initialized")

    async def handle_coordinates(self, x, y, seat: int = 0, dx=None, dy=None):
        """
            Set turretposition whenn the mouseposition changed on

            Arguments:
                seat: number of the seat
        """

        # trigger turret
        pos = (y + 1) / 2 * 100
        self.controller.setPosition(pos)

        logging.info(f"Position turret for seat {seat}")

    def shutdown(self, seat: int = 0):
        self.controller.close()


class TurretShootControl(Switch):
    """
        Switch wich controls the shooting of the turrets
    """

    shooting_time = 1

    def __init__(self):
        pin = (0, 0)  # Read config

        # init controller
        self.controller = TurretShootHAL(pin)

        logging.info("Turret Shootingcontrol initialized")

    async def on(self, seat: int = 0):
        """
            Shoot with the turrent when keyboardswitch is pressed

            Arguments:
                seat: number of the seat
        """

        self.controller.on()
        sleep(self.shooting_time)
        self.controller.off()

        logging.info(f"Shot turret for seat {seat}")

    def shutdown(self, seat: int = 0):
        self.controller.close()
