from asyncio import sleep, create_task
from asyncio.tasks import Task
from typing import List
from hardware import servo
from hardware.servo import ServoHAL
from game_sdk.inputs import Joystick
import logging


class TurretControl(Joystick):
    """
        Joystick wich controls the turrets
    """

    MAX_DEFLECTION = 30
    MIN_DEFLECTION = -30
    MAPPING_FACTOR = 1
    T = 0.02
    threshhold = 0.25

    joystick_pos = 0
    servo_pos = 0
    position_task: Task = None

    def __init__(self, seat: int, name: str, pin: int):
        """
            Arguments:
                seat: controller seat
                name: Name of the control
                pin: Pin the servo is connected to
                max_deflection: maximal/minmal deflection of the servo
        """

        super().__init__(seat, name)
        self.servo = ServoHAL(pin)

        logging.info(f"Turret {self.name} initialized")

    async def get_direction(self, seat: int, pos: float):
        """
            Set turretposition whenn the mouseposition changed on

            Arguments:
                seat: number of the seat
                pos: position of the joystick between -1 and 1
        """

        range = self.MAX_DEFLECTION - self.MIN_DEFLECTION

        self.joystick_pos = ((pos + 1) / 2 * range + self.MIN_DEFLECTION) * self.MAPPING_FACTOR

        logging.debug(f"Set position of Turret {self.name} to {self.joystick_pos}")

    async def setPosition(self):
        """
            Loop to set servo position depending on the joystick position
        """

        DT = 0.0025

        while True:
            self.servo_pos = self.servo_pos + (self.joystick_pos - self.servo_pos) / self.T * DT

            if self.servo_pos > self.MAX_DEFLECTION:
                self.servo_pos = self.MAX_DEFLECTION
            elif self.servo_pos < self.MIN_DEFLECTION:
                self.servo_pos = self.MIN_DEFLECTION

            self.servo.setPosition(self.servo_pos)
            await sleep(DT)

    async def init(self, seat: int = 0):
        """
            Set up task to control the servo

            Arguments:
                seat: number of the seat
        """

        if self.position_task:
            if not self.position_task.cancelled:
                self.position_task.cancel()

        self.joystick_pos = ((self.MAX_DEFLECTION - self.MIN_DEFLECTION) / 2 + self.MIN_DEFLECTION) * self.MAPPING_FACTOR
        self.position_task = create_task(self.setPosition())
        logging.debug(f"Init servo at position {self.joystick_pos}")

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


class VerticalTurretControl(TurretControl):

    MAX_DEFLECTION = 20
    MIN_DEFLECTION = -40
    MAPPING_FACTOR = 1
    T = 0.02


class HorizontalTurretControl(TurretControl):
    MAX_DEFLECTION = 30
    MIN_DEFLECTION = -30
    MAPPING_FACTOR = -1
    T = 0.04
