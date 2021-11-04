import logging


class TurretHAL():
    """
        Hardware interface to control the turrets

        Attributes:
            pin: number of the GPIO pin used to control the turret
    """

    def __init__(self, pin: int = 17):
        self.pin = pin
        logging.info(f"Init turret at Pin {pin}")

    def setPosition(self, pos: int = 50):
        """
            Trigger Turret with specific force

            Arguments:
                force: Turretposition between 0 and 100
        """

        logging.info(f"Turret triggered with force {pos}")

    def close():
        """
            Called when the Interface is not needed anymore
        """

        logging.info(f"Turret interface closed")
