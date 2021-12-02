from typing import List
from hardware.servo import ServoHAL
from game_sdk.inputs import Joystick
import logging


class TurretControl(Joystick):
    """
        Joystick wich controls the turrets
    """

    def __init__(self, seat: int, name: str):
        pin_l = 17  # Read config
        pin_u = 27

        # init controller
        self.controller = (ServoHAL(pin_l), ServoHAL(pin_u))

        logging.info("Turret initialized")
        super().__init__(seat, name)

    async def get_direction(self, seat: int, pos: float):
        """
            Set turretposition whenn the mouseposition changed on

            Arguments:
                seat: number of the seat
        """

        # trigger turret
        maped_pos = (pos + 1) / 2 * 100

        self.controller[0].setPosition(maped_pos)
        self.controller[1].setPosition(maped_pos)

        logging.info(f"Position turret for seat {seat}")

    def shutdown(self, seat: int = 0):
        self.controller[0].close()
        self.controller[1].close()
