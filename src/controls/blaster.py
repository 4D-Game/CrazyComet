import asyncio
from asyncio import sleep
from typing import Any, Callable
from gpiozero import Button, LED
import logging
from game_sdk.controller.inputs import Switch


class Blaster(Switch):
    """
        Input class to detect a shots and hits

        Attributes:
            sensor: Sensor, which detects the hits
            shoot_led: LED wich blinks on every shot
            points_led: LED wich blinks when a hit detected
            magazine: Number of shots left in the magazine
    """

    def __init__(self, seat: int, name: str, score_cb: Callable = None, magazine_size: int = 5):
        """
            Arguments:
                seat: controller seat
                name: Name of the control
                score_cb: Callback which can be called to increase the score
                magazine_size: maximum number of shots the magazine can hold before reloading
        """

        super().__init__(seat, name)

        self.sensor: Button = Button(24, pull_up=True, active_state=None, bounce_time=None, pin_factory=None)
        self.shoot_led: LED = LED(23)
        self.points_led: LED = LED(25)

        self._score_cb = score_cb

        self._max_magazine = magazine_size
        self.magazine: int = 5

        logging.info("Sensor initialized")

    async def on(self, seat: int):
        """
            Detect a hit when the blaster is shot

            Arguments:
                seat: controller seat
        """

        asyncio.create_task(self._led_on(self.shoot_led, 0.1))

        self.magazine -= 1

        if self.magazine >= 0:
            if self.sensor.is_pressed:
                self.magazine = 0
                asyncio.create_task(self._led_on(self.points_led, 1))
                await self._score_cb()

        if self.magazine is 0:
            asyncio.sleep(1)
            self.magazine = self._max_magazine

    async def _led_on(self, led, time: float):
        """
            Turn on a given LED
        """

        led.on()
        await asyncio.sleep(time)
        led.off()

    async def close(self, seat: int):
        """
            Release LEDs and the sensor
        """

        self.shoot_led.close()
        self.points_led.close()
        self.sensor.close()
        logging.info("Close")
