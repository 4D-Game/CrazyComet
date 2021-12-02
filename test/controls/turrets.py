#!/usr/bin/python3

import asyncio
import time
from controls.turrets import TurretControl
import RPi.GPIO as GPIO

# for GPIO numbering, choose BCM
GPIO.setmode(GPIO.BCM)

async def run():
    control1 = TurretControl(1, "turret_control")
    x=0

    while(x<5):
        for i in range(-10, 10):
            await control1.get_direction(1, i/10)
            await asyncio.sleep(2)
        x = x + 1

    control1.shutdown()

asyncio.run(run())
