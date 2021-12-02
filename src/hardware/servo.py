import logging
import RPi.GPIO as GPIO


class ServoHAL:
    """
        Hardware interface to control the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def __init__(self, pin: int):
        self.pin = pin

        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(self._mapPosToPWM(90))

        logging.debug(f"Init turret at Pin {pin}")

    def setPosition(self, pos: int):
        """
            Trigger Turret with specific force

            Arguments:
                force: Turretposition between 0 and 180°
        """

        self.pwm.ChangeDutyCycle(self._mapPosToPWM(pos))
        logging.debug(f"Turret moved to pos {pos}")

    def close(self):   #wird nie ausgeführt?
        """
            Called when the Interface is not needed anymore
        """
        self.pwm.stop()
        logging.debug(f"Turret interface closed")

    def _mapPosToPWM(self, pos: int) -> int:
        """
            Map a given position to PWM duty cycle

            Arguments:
                pos: Position between 0 and 180°
        """
        if pos < 0:
            pos = 0
        elif pos > 180:
            pos = 180

        pwm_range = (2.5, 12.5)
        duty_cycle = pwm_range[0] + ((pwm_range[1] - pwm_range[0]) / 180 * pos)

        logging.debug(duty_cycle)

        return duty_cycle

