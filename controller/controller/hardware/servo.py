import logging

from gpiozero import Servo
from gpiozero.pins.native import NativeFactory
from controller.hardware.hal import HAL


class ServoHAL(HAL):
    """
        Hardware interface to control the servos for the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def __init__(self, pin: int):
        """
            Initialize servo

            Arguments:
                pin: Pin to which the signal wire of the servo is connected (12, 13, 18, 19 for hardware PWM)
        """

        self.pin = pin

        self.pwm = Servo(pin, initial_value=0, min_pulse_width=0.615 / 1000, max_pulse_width=2.495 / 1000)

        logging.debug(f"Init turret at Pin {pin}")

    def setPosition(self, pos: int):
        """
            Set the position of the servo

            Arguments:
                pos: Servoposition between -90 and 90
        """
        self.pwm.value = pos / 90
        #logging.info(f"Turret moved to pos {self.pwm.value}")

    def close(self):
        """
            Release servo
        """
        self.pwm.value = None
        logging.debug(f"Turret interface closed")


class ServoInvertedHAL(ServoHAL):
    """
        Hardware interface to control inverted servos for the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def setPosition(self, pos: int):
        """
            Trigger Turret with specific force

            Arguments:
                force: Turretposition between -90 and 90
        """

        self.pwm.value = -1 * pos / 90
