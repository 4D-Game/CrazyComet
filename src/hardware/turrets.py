import logging
from typing import Tuple

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


class TurretPosHAL():
    """
        Hardware interface to control the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def __init__(self, servo_pin: int = 17):
        self.servo_pin = servo_pin

        GPIO.setup(servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(servo_pin, 50)
        self.pwm.start(self.__mapPosToPWM__(0))

        logging.info(f"Init turret positioning at Pin {servo_pin}")

    def setPosition(self, pos: int = 50):
        """
            Trigger Turret with specific force

            Arguments:
                force: Turretposition between 0 and 100
        """

        self.pwm.ChangeDutyCycle(self.__mapPosToPWM(pos))
        logging.info(f"Turret moved to pos {pos}")

    def close():
        """
            Called when the Interface is not needed anymore
        """

        GPIO.cleanup()
        logging.info(f"Turret positioning interface closed")

    def __mapPosToPWM(self, pos: int) -> int:
        """
            Map a given position to PWM duty cycle

            Arguments:
                pos: Position between 0 and 100
        """

        min_deg = 0
        max_deg = 180

        pwm_range = (5, 10)

        min_pwm = pwm_range[0] + (180 / (pwm_range[1] - pwm_range[0]) * min_deg)
        max_pwm = pwm_range[0] + (180 / (pwm_range[1] - pwm_range[0]) * max_deg)

        return min_pwm + (100 / (max_pwm - min_pwm) * pos)


class TurretShootHAL():
    """
        Hardware interface to control the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def __init__(self, led_pins: Tuple[int] = (18, 19)):
        self.led_pins = led_pins

        GPIO.setup(led_pins, GPIO.OUT, initital=GPIO.LOW)

        logging.info(f"Init turret shooting at Pins {led_pins[0]}, {led_pins[1]}")

    def on(self):
        """
            Emmit light to shoot the UFO
        """

        GPIO.output(self.led_pins, GPIO.HIGH)

    def off(self):
        """
            Switch light emition of
        """

        GPIO.output(self.led_pins, GPIO.LOW)

    def close():
        """
            Called when the Interface is not needed anymore
        """

        GPIO.cleanup()
        logging.info(f"Turret shooting interface closed")
