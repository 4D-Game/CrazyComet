from asyncio import sleep, create_task
from asyncio.tasks import Task
from typing import List, Callable
from hardware import servo
from hardware.servo import ServoHAL, ServoInvertedHAL
from game_sdk.controller.inputs import Joystick
import logging


class TurretControl(Joystick):
    """
        Base class, to control one dimension of the turret with a joystick

        Attributes:
            MAX_DEFLECTION: max deflection of the turret in degree
            MIN_DEFLECTION: min deflection of the turret in degree
            MAPPING_FACTOR: used to scale the mapped turret position
            T: Delay of the PT1 element used to controll the turret position
            THRESHHOLD: threshold under which a joystick value is recognized as 0
            servo: Instance of ServoHAL to control a servo
    """

    MAX_DEFLECTION: int = 30
    MIN_DEFLECTION: int = -30
    MAPPING_FACTOR: float = 1
    T: float = 0.02
    THRESHHOLD = 0.25

    _joystick_pos = 0
    _servo_pos = 0
    _position_task: Task = None

    def __init__(self, seat: int, name: str, pin: int, config: dict, rgb_cb: Callable = lambda _: None):
        """
            Arguments:
                seat: controller seat
                name: Name of the control
                pin: Pin the servo is connected to
                offset: Servo offset from the zero position in degree
        """

        super().__init__(seat, name)

        self.servo: ServoHAL = ServoInvertedHAL(pin) if config["inverted"] else ServoHAL(pin)

        self.MIN_DEFLECTION += config["offset"]
        self.MAX_DEFLECTION += config["offset"]

        self.rgb_cb = rgb_cb

        logging.info(f"Turret {self.name} initialized")

    async def get_direction(self, seat: int, pos: float):
        """
            Set turretposition whenn the joystick position changes

            Arguments:
                seat: number of the seat
                pos: position of the joystick between -1 and 1
        """

        range = self.MAX_DEFLECTION - self.MIN_DEFLECTION

        self._joystick_pos = (((pos * self.MAPPING_FACTOR) + 1) / 2 * range + self.MIN_DEFLECTION)
        self.rgb_cb(pos)

        logging.debug(f"Set position of Turret {self.name} to {self._joystick_pos}")

    async def setPosition(self):
        """
            Loop to set servo position depending on the joystick position
        """

        DT = 0.002

        while True:
            self._servo_pos = self._servo_pos + (self._joystick_pos - self._servo_pos) / self.T * DT

            if self._servo_pos > self.MAX_DEFLECTION:
                self._servo_pos = self.MAX_DEFLECTION
            elif self._servo_pos < self.MIN_DEFLECTION:
                self._servo_pos = self.MIN_DEFLECTION

            self.servo.setPosition(self._servo_pos)
            await sleep(DT)

    async def init(self, seat: int = 0):
        """
            Set up task to control the servo

            Arguments:
                seat: number of the seat
        """

        if self._position_task:
            if not self._position_task.cancelled:
                self._position_task.cancel()

        self._joystick_pos = ((self.MAX_DEFLECTION - self.MIN_DEFLECTION) / 2 + self.MIN_DEFLECTION)
        self._position_task = create_task(self.setPosition())
        logging.debug(f"Init servo at position {self._joystick_pos}")

    async def reset(self, seat: int = 0):
        """
            Cancel task to control the servo and reset servo_pos

            Arguments:
                seat: number of the seat
        """

        if self._position_task:
            self._position_task.cancel()
            self._position_task = None

        self._servo_pos = 0
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
    """
        Turret control for the vertical dimension with custom parameters

        Attributes:
            MAX_DEFLECTION: 30° bottom maximum
            MIN_DEFLECTION: -20° top maximum
            MAPPING_FACTOR: 1 (no scaling)
            T: 0.02s (fast movement)
    """

    MAX_DEFLECTION = 30
    MIN_DEFLECTION = -20
    MAPPING_FACTOR = -1
    T = 0.025


class HorizontalTurretControl(TurretControl):
    """
        Turret control for the horizontal dimension with custom parameters

        Attributes:
            MAX_DEFLECTION: 30° right maximum
            MIN_DEFLECTION: -30° left maximum
            MAPPING_FACTOR: -1 (invert)
            T: 0.04s (slower moevement)
    """

    MAX_DEFLECTION = 30
    MIN_DEFLECTION = -30
    MAPPING_FACTOR = 1
    T = 0.035
