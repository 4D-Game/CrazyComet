import asyncio
from asyncio import sleep, Lock
from typing import Any, Callable, Coroutine
from gpiozero import Button, LED
import logging
from game_sdk.controller.inputs import Switch


class Blaster(Switch):
    """
        Input class to detect a shots and hits

        Attributes:
            sensor: Sensor, which detects the hits
            shoot_led: LED which blinks on every shot
            points_led: LED which blinks when a hit detected
            magazine: Number of shots left in the magazine
    """

    _shoot_lock = Lock()
    _reload_lock = Lock()

    def __init__(self, seat: int, name: str, score_cb: Callable = None, led_cb: Coroutine = None, magazine_size: int = 5, inverted_logic: bool = False):
        """
            Arguments:
                seat: controller seat
                name: Name of the control
                score_cb: Callback which can be called to increase the score
                magazine_size: maximum number of shots the magazine can hold before reloading
        """

        super().__init__(seat, name)

        self.sensor: Button = Button(24, pull_up=inverted_logic)
        self.shoot_led: LED = LED(23)
        self.points_led: LED = LED(25)

        self._score_cb = score_cb
        self._led_cb = led_cb

        self._max_magazine = magazine_size
        self.magazine: int = magazine_size

        logging.info("Sensor initialized")

    async def on(self, seat: int):
        """
            Detect a hit when the blaster is shot

            Arguments:
                seat: controller seat
        """

        async with self._shoot_lock:
            if self.magazine > 0:
                self.magazine -= 1

                asyncio.create_task(self._led_on(self.shoot_led, 0.1))

                if self.sensor.is_pressed:
                    self.magazine = 0
                    asyncio.create_task(self._led_on(self.points_led, 1))
                    asyncio.create_task(self._led_cb(1))
                    await self._score_cb()

        if not self._reload_lock.locked() and self.magazine <= 0:
            async with self._reload_lock:
                await asyncio.sleep(3)
                async with self._shoot_lock:
                    self.magazine = self._max_magazine

    async def off(self, _: int):
        pass

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
