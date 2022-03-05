# Config file

The CrazyComet game adds some more parameters to the `config.toml` as already defined in the [SDK documentation](https://4d-game.github.io/sdk/controller-sdk/config-file/).

**Example**
```toml
seat=1

[CONTROLLER]
input_device="/dev/input/by-id/usb-ShanWan_Trust-GMP-04-event-joystick"

[MQTT]
broker_ip="10.3.141.1"

[CrazyComet]

[CrazyComet.turrets]
[CrazyComet.turrets.vertical]
offset=0
inverted=false

[CrazyComet.turrets.horizontal]
offset=0
inverted=false

[CrazyComet.blaster]
inverted_logic=true
magazine_size=5
```

## CrazyComet

Contains every configuration needed for the CrazyComet game.

### CrazyComet.turrets

Consists of configuration for vertical and horizontal movement of the turrets. The options for both dimensions are similar.

- `float offset`: Offset for the servo during the game. For easier calibration of the zero position.
- `bool inverted`: Defines if the used servo is inverted or not.

### CrazyComet.blaster

Configuration for the blaster logic as well as the sensor used to detect a hit.

- `bool inverted_logic`: Defines if the used sensor has inverted logic (e.g *LOW* == Hit and *HIGH* == no Hit)
- `int magazine_size`: Number of times a player can shoot before a reload (small timeout to avoid continuous shooting)