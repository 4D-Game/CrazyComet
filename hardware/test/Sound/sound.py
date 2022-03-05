import pygame
from pygame import mixer
import time

class Sound:
    """
        Class for managing sounds during the game
    """

    def __init__(self):
        """
            Configures the mixer to play and load needed sounds
        """
        pygame.init()
        mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.shoot_sound = mixer.Sound('laser.wav')
        self.start_sound = mixer.Sound('start1.wav')
        self.win_sound = mixer.Sound('win16.wav')
       
    def play_sound(self, event: int):
        """
            Plays sound depending on event (score, shoot)
        """
        if event == 1:
            self.shoot_sound.set_volume(10)
            self.shoot_sound.play()

        elif event == 2:
            self.start_sound.set_volume(10)
            self.start_sound.play() 
        elif event == 3:
            self.win_sound.set_volume(10)
            self.win_sound.play()

    def stop_sound(self, event: int):
        """
            Stops sound depending on the event
        """
        if event == 1:
            self.shoot_sound.stop()
        elif event == 2:
            self.start_sound.stop() 
        elif event == 3:
            self.win_sound.stop() 
if __name__ == "__main__":
    test = Sound()
    
    test.play_sound(1)
    time.sleep(3) #just for the test
    test.stop_sound(1)
    time.sleep(2)
    test.play_sound(2)
    time.sleep(30) #just for the test
    test.stop_sound(2)
    time.sleep(2)
    test.play_sound(3)
    time.sleep(10) #just for the test
    test.stop_sound(3)