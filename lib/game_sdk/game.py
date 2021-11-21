import asyncio
import enum
import logging
from typing import Any, MutableMapping, Type

from evdev import InputDevice, categorize, ecodes
import toml

from game_sdk.game_io import GameIO, GameState


class LogLevel(enum.Enum):
    """
        Different logging levels defiend by the logging module
    """

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0


class Game:
    """
        Class to control the whole game. Inherit from this class and call `run()` to start your game
    """

    controls: list()
    config: MutableMapping[str, Any]
    _input_dev: InputDevice
    _is_running = False
    _game_io: GameIO

    @property
    def game_io(self):
        """
           Instance of `GameIO` used to control the whole game loop
        """

        if self._is_running:
            return self._game_io
        raise Exception('Execute Game.run() before accessing game_io')

    async def on_init(self):
        """
            Executed, when the game is startet with `Game.run()`
        """

        logging.info("ON INIT")

    async def on_pregame(self):
        """
            Executed, before a new game starts
        """

        logging.info("ON PREGAME")

    async def on_start(self):
        """
            Executed, when a new game starts
        """
        logging.info("ON START")

    async def on_end(self):
        """
            Executed, when the game ends
        """

        logging.info("ON END")

    async def on_exit(self, err: Exception = None):
        """
            Executed, when the game loop is exited

            Arguments:
                err: Value of the exception when the game exited with none zero code
        """

        logging.info("ON EXIT")

        if err:
            logging.error(err)

    async def _ctl_sub(self, ctl_conf: dict):
        """
            Subscribe to gamepad inputs

            Arguments:
                ctl_conf: Gamepad configuration
        """

        self._input_dev = InputDevice(ctl_conf['input_device'])

        async for ev in self._input_dev.async_read_loop():
            logging.info("CODE: %d, \tVALUE %d", ev.code, ev.value)

    async def _game_io_sub(self, mqtt_conf: dict):
        """
            Subscribe to changes of the game state

            Arguments:
                mqtt_conf: GameIO configuration
        """
        self._game_io = GameIO(mqtt_conf)

        async for game_state in self._game_io.subscribe():
            if game_state == GameState.START:
                await self.on_pregame()
            elif game_state == GameState.RUN:
                await self.on_start()
            elif game_state == GameState.END:
                await self.on_end()

    async def _run(self, conf_path: str = '/home/pi/Controller/config.toml'):
        """
            Asynchronous `run` function
        """

        self.config = toml.load(conf_path)
        logging.debug(self.config)

        main_loop = asyncio.gather(
            # self._ctl_sub(self.config['CONTROLLER']),
            self._game_io_sub(self.config['MQTT'])
        )

        await self.on_init()
        self._is_running = True

        # try:
        await main_loop
        await self.on_exit()
        # except Exception as err:
        #    await self.on_exit(err)

    def run(self, conf_path: str = '/home/pi/Controller/config.toml', log_level: LogLevel = 0):
        """
            Start the game engine

            Arguments:
                conf_path: Path to configuration.toml
                log_level: logging level
        """

        logging.getLogger().setLevel(log_level)

        asyncio.run(self._run(conf_path))
