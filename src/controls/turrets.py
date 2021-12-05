from asyncio import sleep, create_task
from asyncio.tasks import Task
from typing import List
from hardware import servo
from hardware.servo import ServoHAL
from game_sdk.inputs import Joystick
import logging

from sdk.game_sdk.inputs import joystick


class TurretControl(Joystick):
    """
        Joystick wich controls the turrets
    """

    MAX_DEFLECTION = None

    joystick_pos = 0
    servo_pos = 0
    position_task: Task = None

    def __init__(self, seat: int, name: str, pin: int, max_deflection: int):
        """
            Arguments:
                seat: controller seat
                name: Name of the control
                pin: Pin the servo is connected to
                max_deflection: maximal/minmal deflection of the servo
        """

        super().__init__(seat, name)
        self.servo = ServoHAL(pin)
        self.MAX_DEFLECTION = max_deflection

        logging.info(f"Turret {self.name} initialized")

    async def get_direction(self, seat: int, pos: float):
        """
            Set turretposition whenn the mouseposition changed on

            Arguments:
                seat: number of the seat
                pos: position of the joystick between -1 and 1
        """

        self.joystick_pos = pos

    async def setPosition(self):
        """
            Loop to set servo position depending on the joystick position
        """

        MAPPING_FACTOR = 0.2
        MAX_DEFLECTION = self.MAX_DEFLECTION

        while True:
            self.servo_pos += self.joystick_pos * MAPPING_FACTOR

            if self.servo_pos > MAX_DEFLECTION:
                self.servo_pos = MAX_DEFLECTION
            elif self.servo_pos < - MAX_DEFLECTION:
                self.servo_pos = - MAX_DEFLECTION

            self.servo.setPosition(self.servo_pos)
            await sleep(0.02)

    async def init(self, seat: int = 0):
        """
            Set up task to control the servo

            Arguments:
                seat: number of the seat
        """

        if self.position_task:
            if not self.position_task.cancelled:
                self.position_task.cancel()

        self.position_task = create_task(self.setPosition())

    async def reset(self, seat: int = 0):
        """
            Cancel task to control the servo and reset servo_pos

            Arguments:
                seat: number of the seat
        """

        if self.position_task:
            self.position_task.cancel()
            self.position_task = None

        self.servo_pos = 0
        self.servo.setPosition(0)

    async def close(self, seat: int = 0):
        """
            Cancel task to control the servo and close servo connection

            Arguments:
                seat: number of the seat
        """

        await self.reset(seat)
        self.servo.close()
