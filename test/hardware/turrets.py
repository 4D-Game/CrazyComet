#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

# for GPIO numbering, choose BCM  
GPIO.setmode(GPIO.BCM) 

from hardware.turrets import TurretHAL



turret1 = TurretHAL(17)
#turret2 = TurretHAL(27)

time.sleep(2)
turret1.setPosition(0)
time.sleep(2)
turret1.setPosition(180)

turret1.close()

