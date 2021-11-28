#!/usr/bin/python3

<<<<<<< HEAD
import asyncio

=======
from hardware.turrets import TurretHAL
>>>>>>> 8069566b17763fcc7cf92c53cacc56c109f3728d
from controls.turrets import TurretControl
from hardware.turrets import TurretHAL
import RPi.GPIO as GPIO

# for GPIO numbering, choose BCM  
GPIO.setmode(GPIO.BCM) 

control = TurretControl(1, "turret_control")

asyncio.run(control.get_direction(1, -1))
