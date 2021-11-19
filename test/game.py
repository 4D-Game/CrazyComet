#!/usr/bin/env python3

from game_sdk import Game
from game_sdk.game import LogLevel


class GameTest(Game):
    pass


if __name__ == "__main__":
    test_game = GameTest()
    test_game.run(log_level=LogLevel.DEBUG.value)
