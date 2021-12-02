#!/usr/bin/python3

import logging
import time
import RPi.GPIO as GPIO

# for GPIO numbering, choose BCM
GPIO.setmode(GPIO.BCM)

from hardware.servo import ServoHAL

try:
  logging.getLogger().setLevel(logging.DEBUG)

  turret1 = ServoHAL(13)
  turret2 = ServoHAL(12)

  input('Press return to stop:')
  turret1.setPosition(45)
  turret2.setPosition(45)

  input('Press return to stop:')
  turret1.setPosition(0)
  turret2.setPosition(0)

  input('Press return to stop:')
except KeyboardInterrupt:
  logging.info("Keyboard Interrupt")
finally:
  turret1.close()
  turret2.close()
  GPIO.cleanup()
