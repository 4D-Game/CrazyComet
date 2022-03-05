# CrazyComet Concept

## Basic-principle

Two teams with three players each will be drawn. Each of these players controls a turret with the respective controller.
An object rotating in a circle or bobbing up and down must be shot down with a turret. For every hit the player gets points. The team that has the most points after a certain time has elapsed wins.

## Rotating object

The middle part is constructed with two steppers motors (see hardware documentation) to achieve a rotating and tilting movement. The turret is controlled by a raspberry pi.
## Turrets

The turrets are operating with two servo motors. The lower one creates the horizontal and the upper one the vertical movement. The upper servo motor also controls the position of the laser. The turrets can be controlled by the controller (see controller setting in instructions). Two LEDs are also integrated in this 3D-Print. (Red LED: lights while shooting, Green LED: after hitting the target). The turrets are controlled by another raspberry pi.

## Display

The displays show the points of every team and are controlled by another raspberry pi.

## Usefull Links

In order to work with/on this project the following links might be helpful

- [Game Code](controller/index.md)
- [Hardware](hardware/index.md)
- [4D-Game SDK](sdk/index.md)
- [Documentation](documentation.md)
- [Coding Style](coding-style/python.md)