#!/usr/bin/python3

import logging
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory
from hardware.servo import ServoHAL


Device.pin_factory = PiGPIOFactory()

try:
    logging.getLogger().setLevel(logging.DEBUG)

    turret1 = ServoHAL(13)

    while True:
        val = int(input('Enter Servo position in degree:'))
        turret1.setPosition(val)

except KeyboardInterrupt:
    logging.info("Keyboard Interrupt")
finally:
    turret1.close()
    # GPIO.cleanup()
