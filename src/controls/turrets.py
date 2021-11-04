from typing import List
from ..hardware.turrets import TurretHAL
from surrortg.inputs import MouseJoystick
import logging


class TurretControl(MouseJoystick):
    """
        Joystick wich controls the turrets
    """

    def __init__(self):
        pin = 0  # Read config

        # init controller
        self.controller = TurretHAL(pin)

        logging.info("Turret initialized")

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
