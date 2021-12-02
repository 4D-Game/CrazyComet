#!/usr/bin/python3

import logging
import time
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory
from hardware.servo import ServoHAL


Device.pin_factory = PiGPIOFactory()

try:
  logging.getLogger().setLevel(logging.DEBUG)

  turret1 = ServoHAL(13)
  turret2 = ServoHAL(12)

  input('Press return to stop:')
  turret1.setPosition(-0.5)
  turret2.setPosition(0.5)

  input('Press return to stop:')
  turret1.setPosition(-1)
  turret2.setPosition(1)

  input('Press return to stop:')
except KeyboardInterrupt:
  logging.info("Keyboard Interrupt")
finally:
  turret1.close()
  turret2.close()
  #GPIO.cleanup()
