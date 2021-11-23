#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

# for GPIO numbering, choose BCM  
GPIO.setmode(GPIO.BCM) 

from hardware.turrets import TurretHAL

turret = TurretHAL(17)

time.sleep(50)
turret.setPosition(100)

