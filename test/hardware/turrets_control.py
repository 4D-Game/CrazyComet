#!/usr/bin/python3

from hardware.turrets import TurretHAL
from controls.turrets import TurretControl


control = TurretControl()

control.get_direction(20, 50)