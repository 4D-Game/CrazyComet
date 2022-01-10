from hardware.hal import HAL
import spidev, numpy

class RgbHAL(HAL):
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)

    def write2812(self, spi, data):
        d=numpy.array(data).ravel()
        tx=numpy.zeros(len(d)*4, dtype=numpy.uint8)
        for ibit in range(4):
            tx[3-ibit::4]=((d>>(2*ibit+1))&1)*0x60 + ((d>>(2*ibit+0))&1)*0x06 +  0x88
        self.spi.xfer(tx.tolist(), int(4/1.25e-6)) #works, on Zero

    def all_leds(self, rgb_code):
        data = []
        for i in range(24):
            data.append(rgb_code)
        return data

    def close(self):
        data = self.all_leds([0, 0, 0])
        self.write2812(self.spi, data)