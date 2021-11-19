from . import GameIO
import asyncio
import enum
import logging
from typing import Any, MutableMapping, Type
from evdev import InputDevice, categorize, ecodes
import toml


class LogLevel(enum.Enum):
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0


class Game:
    controls: list()
    config: MutableMapping[str, Any]
    input_dev: InputDevice
    _is_running = False
    _game_io: GameIO

    @property
    def game_io(self):
        if self._is_running:
            return self._game_io
        raise Exception('Execute Game.run() before accessing game_io')

    async def on_init(self):
        pass

    async def on_start(self):
        pass

    async def on_end(self):
        pass

    async def on_exit(self, err: Exception = None):
        pass

    async def _run(self):
        async for ev in self.input_dev.async_read_loop():
            logging.info("CODE: %d, \tVALUE %d", ev.code, ev.value)
        pass

    def run(self, conf_path: str = '/home/pi/Controller/config.toml', log_level: LogLevel = 0):
        logging.getLogger().setLevel(log_level)

        self.config = toml.load(conf_path)
        logging.debug(self.config)

        self.input_dev = InputDevice(self.config.get('input_device'))

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run())

        self.on_exit()
