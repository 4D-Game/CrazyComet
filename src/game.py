"""
Created: 26.04.21
by: Lukas Schüttler

Define Game class
"""

from typing import Union
import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), os.pardir, "lib", "surrortg-sdk"))

from surrortg.inputs import Directions, Joystick
from surrortg import Game


class LoopinLouie(Game):
    """
      Game class wich controlls the whole game

      Attributes:
        controls (dict): List of controls filled in on_init()
    """

    controls = dict()

    async def on_init(self):
        """
          Init function. Gets called when the game is started
          This function is used to register user inputs
        """

        self.controls = {}

    async def on_config(self):
        """
          Called every time the game engine starts
        """

    async def on_prepare(self):
        """
          Called every game before players connect
        """

    async def on_pre_game(self):
        """
          Called every game after players connect
        """

    async def on_countdown(self):
        """
          Called during the game countdown
        """

    async def on_start(self):
        """
          Called when the game starts. User inputs are now enabled. Scores, laps and progress are counted
        """

    async def on_finish(self):
        """
          Called when game ends. Reset game to start configuration
        """

    async def on_exit(self, reason: int, exception: Union[Exception, None]):
        """
          Called when the program exits. Used to reset GPIO configurations

          Arguments:
            reason: reason for the exit (see [docs.surrogate.tv](https://docs.surrogate.tv/modules/surrortg.html#module-surrortg.game) for exitcodes)
            exception: Exception that caused the exit
        """
