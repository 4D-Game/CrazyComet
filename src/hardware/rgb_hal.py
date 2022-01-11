from hardware.hal import HAL
import spidev
import numpy  # numpy und spidev falls notwendig zu den requirements hinzufügen

"""
    Docstrings!!!
    Datentypen für alle Argumente der Funktionen und evtl. für Attribute der Klasse
    Möglicherweise verwendung eines "gobalen" arrays self.data. So weiß das Programm
    immer welche LEDs gerade was anzeigen und einzelne LEDs können geändert werden
    ohne den Rest zu löschen
"""

# class RgbLedHAL(HAL):


class RgbHAL(HAL):
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)

    # def write_leds(self, spi, data)
    # spi argument notwendig?
    def write2812(self, spi, data):
        d = numpy.array(data).ravel()
        tx = numpy.zeros(len(d) * 4, dtype=numpy.uint8)
        for ibit in range(4):
            tx[3 - ibit::4] = ((d >> (2 * ibit + 1)) & 1) * 0x60 + ((d >> (2 * ibit + 0)) & 1) * 0x06 + 0x88
        self.spi.xfer(tx.tolist(), int(4 / 1.25e-6))  # works, on Zero

    # all_leds what??
    def all_leds(self, rgb_code):
        data = []
        for i in range(24):
            data.append(rgb_code)
        return data
        # self.write2812(self.spi, data)

    def close(self):
        data = self.all_leds([0, 0, 0])
        self.write2812(self.spi, data)
