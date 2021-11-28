#!/usr/bin/python3

import asyncio

from controls.turrets import TurretControl
from hardware.turrets import TurretHAL
import RPi.GPIO as GPIO

# for GPIO numbering, choose BCM  
GPIO.setmode(GPIO.BCM) 

control = TurretControl(1, "turret_control")

asyncio.run(control.get_direction(1, -1))
