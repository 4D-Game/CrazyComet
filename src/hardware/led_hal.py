from hardware.hal import HAL
import spidev
import numpy 

class RgbLedHAL(HAL):
    """
        Class to manage RGB Leds
    """

    def __init__(self):
        """
            Configure SPI and RGB Leds
        """
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.data = []
        for i in range(24):
            self.data.append([0, 0, 0])
        self.write_led(self.data) #no color at the beginning

    def write_led(self, data):
        """
            Set colors to one or more leds (depending on data parameter)

            Parameters:
                data: 2-dimensional array which includes rgb code of needed leds
        """
        d = numpy.array(data).ravel()
        tx = numpy.zeros(len(d) * 4, dtype=numpy.uint8)
        for ibit in range(4):
            tx[3 - ibit::4] = ((d >> (2 * ibit + 1)) & 1) * 0x60 + ((d >> (2 * ibit + 0)) & 1) * 0x06 + 0x88
        self.spi.xfer(tx.tolist(), int(4 / 1.25e-6))  

    def configure_all_leds(self, rgb_code):
        """
            Configure all leds to same rgb code

            Parameter:
                rgb_code: np.array which includes the rgb color code [RED, GREEN, BLUE]
        """
        for i in range(len(self.data)):
            self.data[i] = rgb_code
        self.write_led(self.data)

    def led_score_on(self, rgb_code):
        """
            Turns on 4 led when player scores
        """
        self.data[0] = rgb_code
        self.data[1] = rgb_code
        self.data[-1] = rgb_code
        self.data[-2] = rgb_code
        self.write_led(self.data)

    def led_score_off(self):
        """
            Turns off leds when player has scored
        """
        self.data[0] = [0,0,0]
        self.data[1] = [0,0,0]
        self.data[-1] = [0,0,0]
        self.data[-2] = [0,0,0]
        self.write_led(self.data)

    def configure_individual_leds(self, rgb_code, pixel):
        """
            Configures rgb strip with specific rgb code till determined led

            Parameters:
                rgb_code: np.array with the color code
                pixel: how many leds should be changed
        """
        if pixel < 0:
            count = -3
            for i in range(len(self.data)-3):
                if count >= pixel:
                    self.data[count] = rgb_code
                else:
                    self.data[count] = [0, 0, 0]
                count = count - 1
        else:
            count = 2
            for i in range(len(self.data)-2):
                if count < pixel:
                    self.data[count] = rgb_code
                else:
                    self.data[count] = [0, 0, 0]
                count = count + 1

        self.write_led(self.data)

    def close(self):
        """
            Switch all leds off
        """
        self.configure_all_leds([0, 0, 0])