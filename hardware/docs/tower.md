
# Tower

The tower is the central element of the playing field. It is used to move the comets around the playing field so every player has a chance to hit them.

![View from the top](pictures/tower_top_view.jpeg)

![View from the side](pictures/tower_side.jpeg)

## Functionality

The tower consists of a base and an arm with a comet at each end. The arm can be rotated horizontally and tilted vertically. Both motions are created with a stepper motor. The stepper motors are controlled with the Raspberry Pi using a Adafruit Motor Shield. In order to avoid tilting too far  to the right or left, 2 end stoppers and physical limitation are built in.

## Technical characteristics

| Mechanical Device  | Action            | State                |
| ------------------ | ----------------- | -------------------- |
| Side stepper motor | Tilting the tower | +-16° right/left max |
| Top stepper motor  | Arm rotation      | Circular movement    |

### 3D-Model

![CAD model of the tower](models/tower/tower_final.png)

![CAD sketch of the tower](models/tower/tower_final_sketch.png)

### Circuit (connection to Raspberry Pi)

![Middle Tower circuit](circuit/tower.png)

For the connection between motors, motor shield and Raspberry Pi see the [Adafruit documentation](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/stacking-hats)

## Components

For a list of all used components see the [components](components.md) section.

## Further information

All 3D-Models were done with Fusion360 and can be found on GitHub.
For information about controlling the tower via controller and software solutions please look [here](https://4d-game.github.io/Gamecontrol/code-references/hardware/stepper_hal/)

