import asyncio
from asyncio import sleep
from gpiozero import Button, LED  
import logging
from game_sdk.controller.inputs import Switch

class Sensor(Switch): 
    """
        Input class for sensor 
    """

    def on_init(self):
        self.sensor = Button(24, pull_up = True, active_state = None, bounce_time = None, pin_factory= None) 
        self.schoot_led = LED(23)
        self.points_led = LED(25)
        self.points = 0
        logging.info("Sensor initialized")

    async def points_detected(self):  #example if point detected
        asyncio.create_task(self.led_on(self.points_led, 1))

        self.points +=1
        await self.game_io.score(score=self.points, seat=self.config["seat"])

        logging.info("Points detected")

    async def event_detected(self):
        asyncio.create_task(self.led_on(self.schoot_led, 0.1))

        if self.sensor.is_pressed:
            await self.points_detected() #if point detected 
        
        logging.info("Event")

    async def led_on(self, name: str, time: float):
        self.name.on()
        await asyncio.sleep(time) 
        self.name.off()

    async def close(self):
        self.schoot_led.close()
        self.points_led.close()
        self.sensor.close()
        logging.info("Close")

if __name__ == "__main__":
    s = Sensor()
    s.on_init()
    s.event_detected()