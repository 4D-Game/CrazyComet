#!/usr/bin/python3

from controls.turrets import TurretControl

control = TurretControl(MouseJoystick)

control.get_direction(10, 10)