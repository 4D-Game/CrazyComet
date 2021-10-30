import logging


class Paddle():
    """
        Hardware interface to control the paddles

        Attributes:
            pin: number of the GPIO pin used to control the paddle
    """

    def __init__(self, pin: int = 17):
        self.pin = pin
        logging.info(f"Init paddle at Pin {pin}")

    def trigger(self, force: int = 100):
        """
            Trigger Paddle with specific force

            Arguments:
                force: Paddleforce between 0 and 100
        """

        logging.info(f"Paddle triggered with force {force}")

    def close():
        """
            Called when the Interface is not needed anymore
        """

        logging.info(f"Paddle interface closed")
