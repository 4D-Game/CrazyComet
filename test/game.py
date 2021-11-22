#!/usr/bin/env python3

import logging
from game_sdk import Game
from game_sdk.game import LogLevel
import asyncio


class GameTest(Game):

    async def on_pregame(self):
        return await super().on_pregame()

    async def on_start(self):
        return await super().on_start()


if __name__ == "__main__":
    test_game = GameTest()
    test_game.run(log_level=LogLevel.DEBUG)
