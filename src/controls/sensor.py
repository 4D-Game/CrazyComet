#!/usr/bin/env python3

import logging
import asyncio
from asyncio import sleep 
from gpiozero import Button, LED  #from gpiozero import * ?? or plus LED  or only import gpiozero 
#from gpiozero.pins.native import NativeFactory


class Sensor:
    """
        Input class for sensor 
    """

    def __init__(self):
        self.sensor = Button(24, pull_up=True, active_state = None, bounce_time=None, pin_factory=None)  #init sensor
        self.schoot_led = LED(23)
        self.points_led = LED(25)
        self. points = 0
        print (f"Sensor initialized")

    async def points_detected(self):  #example if point detected
        self.points_led.on()
        await asyncio.sleep(1) 
        self.points_led.off()
        await asyncio.sleep(1) 
        self.points +=1
        print (self.points)
        print (f"Point detected")
        #await self.close()


    async def event_detected(self, schoot:bool):
        if schoot:
            print (f"Event")
            self.schoot_led.on()
            await asyncio.sleep(0.1)
            self.schoot_led.off()
            if self.sensor.is_pressed:
                await self.points_detected() #if point detected 


    async def close(self):
        self.schoot_led.close()
        self.points_led.close()
        self.sensor.close()
        print (f"Close")

test_sensor = Sensor()
#asyncio.run (test_sensor.event_detected(0))
asyncio.run(test_sensor.event_detected(1))
asyncio.run(test_sensor.event_detected(0))
asyncio.run(test_sensor.event_detected(1))






