import os, time
from pygame import mixer
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341

class Music:

    def __init__(self):

        mixer.init()
        # Load the sounds
        self.sound_1 = mixer.Sound('test_1.mp3')
        self.sound_2 = mixer.Sound('test_2.mp3')
        # Configuration for CS and DC pins (these are PiTFT defaults):
        cs_pin = digitalio.DigitalInOut(board.CE0)
        dc_pin = digitalio.DigitalInOut(board.D25)
        reset_pin = digitalio.DigitalInOut(board.D24)

        # Config for display baudrate (default max is 24mhz):
        baudrate = 24000000

        # Setup SPI bus using hardware SPI:
        spi = board.SPI()

        self.disp = ili9341.ILI9341(
            spi,
            rotation=90,  #2.2", 2.4", 2.8", 3.2" ILI9341
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=baudrate,
        )

    
    def start_game(self):
        """
            Display until game starts (ready)
        """
        if self.disp.rotation % 180 == 90:
            height = self.disp.width  #we swap height/width to rotate it to landscape!
            width = self.disp.height
        else:
            width = self.disp.width  
            height = self.disp.height


        image = Image.new("RGB", (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 155, 250))
        draw.ellipse((80,50,230,200), fill = (0, 155, 250), outline ='white', width=10)
        #draw.ellipse((20, 180, 180, 20), outline ='white', fill=(0, 250, 0))
        self.disp.image(image)

        # Scale the image to the smaller screen dimension
        image_ratio = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width = image.width * height // image.height
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = image.height * width // image.width
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

        
        # Display image.
        self.disp.image(image)



    def play(self,event:int):
        if event ==1:
            self.start_game()
            self.sound_1.set_volume(10)
            self.sound_1.play()
            time.sleep(20)
            self.sound_1.stop() 
            # wait for sound to finish playing
            #time.sleep(10)
            #self.sound_1.stop()
        if event ==2:
            self.sound_2.set_volume(10)
            self.sound_2.play()
            # wait for sound to finish playing
            time.sleep(20)
            self.sound_2.stop() 



if __name__ == "__main__":
    test = Music()
    test.play(1)
    time.sleep(2)
    test.play(2)