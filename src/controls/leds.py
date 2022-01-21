import logging
from hardware.led_hal import RgbLedHAL

class LEDControl():
    """
        Control RGB Leds
    """

    def __init__(self):
        """
            Initializes RGB strip
        """
        self.led = RgbLedHAL()
        self.led_numbers = 12 #half stripe

    def display_joystick_pos(self, pos):
        """
            Switch leds on and off depending on joystick position

            Parameters:
                pos: position of joystick, between -1 and 1
        """
        pos = pos * self.led_numbers
        self.led.configure_individual_leds([10,0,10], pos)

    def all_leds_green(self):
        """
            Turns all led green
        """
        self.led.configure_all_leds([10,0,0])
    
    def switch_off_leds(self):
        """
            Switches all leds off
        """
        self.led.close()