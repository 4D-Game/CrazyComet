import logging
from typing import Callable
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from game_sdk.key_map import KeyCode
from game_sdk import Game
from game_sdk.inputs import Switch

LED_PIN = 17

class LEDSwitch(Switch):
    def __init__(self, seat: int, name: str, score_cb: Callable = None):
        
        # Initialize LED pin
        GPIO.setup(LED_PIN, GPIO.OUT)
        # Store reference to score callback function
        self.score_cb = score_cb
        super().__init__(seat, name)

    async def on(self, seat=0):
        GPIO.output(LED_PIN, GPIO.HIGH)
        await self.score_cb()

    async def off(self, seat=0): 
        GPIO.output(LED_PIN, GPIO.LOW)

    async def shutdown(self, seat):
        # Set LED pin into safe state by setting it to input mode
        GPIO.cleanup()


class LedTestGame(Game):
    score = 0

    async def update_score(self):
        self.score += 1
        await self.game_io.score(score=self.score, seat=self.config["seat"])

    async def on_init(self):
        self.ready_control=KeyCode.BUT_1
        # Register LED input with update score callback function
        self.controls={KeyCode.BUT_0: LEDSwitch(self.config["seat"], 'LEDSwitch_1', self.update_score)}

    async def on_pregame(self):
        # Set score to 0 before game starts
        self.score = 0


if __name__ == "__main__":
    # Start running the game
    LedTestGame().run()

