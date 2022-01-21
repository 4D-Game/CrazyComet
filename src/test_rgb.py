import time
from controls.leds import LEDControl

if __name__ == '__main__':
    leds = LEDControl()
    #leds.configure_individual_leds([10,10,0], 7)
    #leds.configure_all_leds([10,0,0])
    leds.display_joystick_pos(0.05)
    #leds.close()
    for i in range(13):
        pos = -i/12
        leds.display_joystick_pos(pos)
        #time.sleep(1)
        for i in range(500000):
            pass
    