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
from controls.leds import LEDControl
from controls.ready import ReadyControl


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
        self.rgb_leds = LEDControl()

        self.ready_control = {
            "key": KeyCode.BUT_1,
            "input": ReadyControl(seat=self.config["seat"], name="Ready Control", led_ctl=self.rgb_leds)}

        self.controls = {
            JoystickCode.LEFT_Y: VerticalTurretControl(
                seat=self.config["seat"],
                name="vertical_control",
                pin=13,
                offset=self.config['CrazyComet']['turrets']['vertical_offset']

            ),
            JoystickCode.LEFT_X: HorizontalTurretControl(
                seat=self.config["seat"],
                name="horizontal_control",
                pin=12,
                rgb_cb=self.rgb_leds.display_joystick_pos,
                offset=self.config['CrazyComet']['turrets']['horizontal_offset']
            ),
            KeyCode.R1: Blaster(
                seat=1,
                name="Blaster",
                score_cb=self.update_score,
                magazine_size=self.config['CrazyComet']['blaster']['magazine_size'],
                inverted_logic=self.config['CrazyComet']['blaster']['inverted_logic'],
                led_cb=self.rgb_leds.score_leds
            )
        }

    async def on_pregame(self):
        """
            Reset score
        """

        self.score = 0

    async def on_end(self):
        self.rgb_leds.all_leds_blue()

    async def on_exit(self, err: Exception = None):
        self.rgb_leds.switch_off_leds()

        return await super().on_exit(err)


if __name__ == "__main__":
    Device.pin_factory = PiGPIOFactory()

    game = CrazyComet()
    game.run("/home/pi/Controller/config.toml", LogLevel.INFO)
