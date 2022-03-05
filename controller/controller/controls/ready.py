import asyncio
from asyncio import sleep, Lock
import logging
from game_sdk.controller.inputs import Switch
from controller.controls.leds import LEDControl


class ReadyControl(Switch):
    """
          Input class to display if player is ready

          Attributes:
              led_ctl: Instance to control RGB LEDs
      """

    def __init__(self, seat: int, name: str, led_ctl: LEDControl):
        """
            Arguments:
                seat: controller seat
                name: Name of the control
                led_ctl: Instance to control RGB LEDs
        """

        super().__init__(seat, name)

        self.led_ctl = led_ctl

        logging.info(f"{name} initialized")

    async def init(self, seat: int):
        """
            Turn off all LEDs

            Arguments:
                seat: controller seat
        """

        self.led_ctl.switch_off_leds()

    async def on(self, seat: int):
        """
            Turn on LEDs

            Arguments:
                seat: controller seat
        """

        self.led_ctl.all_leds_green()

    async def off(self, _: int):
        pass

    async def close(self, seat: int):
        """
            Release LEDs and the sensor
        """

        logging.info(f"Close {self.name}")
