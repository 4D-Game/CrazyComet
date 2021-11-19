from . import Game
import logging
import asyncio
import enum
from asyncio_mqtt import Client, MqttError


class GameState(enum.Enum):
    IDLE = "idle"
    START = "start"
    RUN = "run"
    END = "end"


class GameIO:
    client: Client
    ready: bool
    game_state: GameState = GameState.IDLE

    async def __init__(self, io_config: dict(), game: Game):
        ip = io_config['broker_ip']
        port = io_config['broker_port'] if io_config['broker_port'] else 1883

        client = Client(ip, port, io_config['username'], io_config['password'])

        topics = ["status/ready", "status/game"]

        async with client.unfiltered_messages() as messages:
            await client.subscribe(topics)
            async for msg in messages:
                logging.info(msg)
