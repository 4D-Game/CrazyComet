import spidev
import numpy
from game_sdk.passive.game import Game
from hardware.rgb_hal import RgbHAL

class Rgb(Game):
    """
        Class to manage rgb colors
    """

    async def on_init(self):
        """
            Configure spi
        """
        self.rgb = RgbHAL()
        logging.info("RGB initialized")

    async def on_pregame(self):
        """
            RGB until game starts (ready)
        """
        data = self.rgb.all_leds([180,0,255])
        self.rgb.write2812(self.spi, data)
        logging.info("RGB ready (ECE color)")

    async def on_score(self):
        """
            RGB when point is detected
        """
        data = self.rgb.all_leds([100, 0, 0])
        self.rgb.write2812(self.spi, data)
        logging.info("RGB green (score)")

    async def on_end(self):
        """
            RGB when game is finished 
        """
        data = self.rgb.all_leds([180,0,255])
        self.rgb.write2812(self.spi, data)
        logging.info("RGB blue (ECE color)")
    
    async def on_exit(self):
        """
            RGB when whole game ends
        """
        self.rgb.close()
        logging.info("All LEDs out")

if __name__ == '__main__':
    rgb = Rgb()
    rgb.run("/home/pi/CrazyComet/Gamecontrol/config.toml")

