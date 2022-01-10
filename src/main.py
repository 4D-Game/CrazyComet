#!/usr/bin/env python3

"""
Entrypoint for the Controller programm
"""

import logging

from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory

from game_sdk.controller import Game
from game_sdk.game import LogLevel
from game_sdk.controller.key_map import JoystickCode, KeyCode

from controls.blaster import Blaster
from controls.turrets import HorizontalTurretControl, VerticalTurretControl


class CrazyComet(Game):
    score: int = 0

    async def update_score(self):
        """
            Increase score by one and publish it with gameIO
        """

        self.score += 1
        await self.game_io.score(score=self.score, seat=self.config["seat"])

    async def on_init(self):
        """
            Initialize controls
        """

        self.ready_control = KeyCode.BUT_1
        self.controls = {
            JoystickCode.LEFT_Y: VerticalTurretControl(
                seat=1,
                name="horizontal_control",
                pin=13,
                offset=self.config['CrazyComet']['turrets']['vertical_offset']
            ),
            JoystickCode.LEFT_X: HorizontalTurretControl(
                seat=1,
                name="vertical_control",
                pin=12,
                offset=self.config['CrazyComet']['turrets']['horizontal_offset']
            ),
            KeyCode.R1: Blaster(
                seat=1,
                name="Blaster",
                score_cb=self.update_score,
                magazine_size=self.config['CrazyComet']['magazine_size']
            )
        }

    async def on_pregame(self):
        """
            Reset score
        """

        self.score = 0


if __name__ == "__main__":
    Device.pin_factory = PiGPIOFactory()

    game = CrazyComet()
    game.run("/home/pi/Controller/config.toml", LogLevel.INFO)
