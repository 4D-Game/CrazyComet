from typing import List
from ..hardware.paddles import Paddle
from surrortg.inputs import Switch
import logging


class PaddleControl(Switch):
    """
        Switch wich controls the paddles
    """

    def __init__(self):
        pin = 0  # Read config

        # init controller
        self.controller = Paddle(pin)

        logging.info("Paddle initialized")

    async def on(self, seat: int = 0):
        """
            Trigger paddle whenn the switch is turned on

            Arguments:
                seat: number of the seat
        """

        # trigger paddle
        self.controller.trigger()

        logging.info(f"paddle on for seat {seat}")

    async def off(self, seat: int = 0):

        logging.info(f"paddle off for seat {seat}")

    def shutdown(self, seat: int = 0):
        self.controller.close()
