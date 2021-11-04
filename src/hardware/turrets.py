import logging
import RPi.GPIO as GPIO


class TurretHAL():
    """
        Hardware interface to control the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def __init__(self, pin: int = 17):
        self.pin = pin

        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(self.__mapPosToPWM__(0))

        logging.info(f"Init turret at Pin {pin}")

    def setPosition(self, pos: int = 50):
        """
            Trigger Turret with specific force

            Arguments:
                force: Turretposition between 0 and 100
        """

        self.pwm.ChangeDutyCycle(self.__mapPosToPWM__(pos))
        logging.info(f"Turret moved to pos {pos}")

    def close():
        """
            Called when the Interface is not needed anymore
        """

        GPIO.cleanup()
        logging.info(f"Turret interface closed")

    def __mapPosToPWM__(self, pos: int) -> int:
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
