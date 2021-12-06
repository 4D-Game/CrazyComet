#!/usr/bin/python3

import asyncio
import logging
from game_sdk.key_map.gamepad import JoystickCode, XBoxWireless
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory
from evdev import InputDevice, categorize, ecodes
from controls.turrets import HorizontalTurretControl, TurretControl, VerticalTurretControl


Device.pin_factory = PiGPIOFactory()
logging.getLogger().setLevel(logging.DEBUG)


async def realJoystick():
    try:
        input_dev = InputDevice("/dev/input/event1")

        controls = {
            JoystickCode.LEFT_Y: VerticalTurretControl(1, "horizontal_control", 13),
            JoystickCode.LEFT_X: HorizontalTurretControl(1, "vertical_control", 12)
        }

        for _, control in controls.items():
            await control.init(1)
        await asyncio.sleep(1)

        async for ev in input_dev.async_read_loop():
            mapped_code = XBoxWireless.mapKey(ev.code)

            if mapped_code in controls and ev.type != 0:
                control = controls[mapped_code]
                logging.debug(f"Found control: {control.name}")

                asyncio.create_task(control.set_direction(1, ev.value))

    except KeyboardInterrupt:
        logging.info("Keyboard Interrupt")
    finally:
        for _, control in controls.items():
            await control.close(1)


async def simulateJoystick():
    try:
        control1 = TurretControl(1, "turret_control", 13, 30)
        control2 = TurretControl(1, "turret_control", 12, 30)

        joystick_pos = [-1, 1, -0.3, 0.3]

        await control1.init(1)
        await control2.init(1)
        await asyncio.sleep(1)

        for _ in range(2):
            for i in joystick_pos:
                await control1.get_direction(1, i)
                await control2.get_direction(1, i)
                await asyncio.sleep(2)

    except KeyboardInterrupt:
        logging.info("Keyboard Interrupt")
    finally:
        await control1.close(1)
        await control2.close(1)

asyncio.run(realJoystick())
