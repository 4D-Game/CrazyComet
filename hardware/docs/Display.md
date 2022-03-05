# Display and Sound module

The name of the teams and the points of every team as well as the winner is shown on a display. Each successful hit is accentuated by a sound effect. During the game, the melody ["Awakening Game Polychord phase"](https://freesound.org/people/SSS_Samples/sounds/360906/) and at the end, the song ["Jingle_Win_00"](https://freesound.org/people/LittleRobotSoundFactory/sounds/270402/) is played. 

![Display](pictures/display.jpeg){ align=left width="300"}

![Display connection](pictures/displays.jpeg){ align=right width="355" }

## Functionality

The displays are controlled by a Raspberry Pi. For this game two 2.2 TFT SPI 240x320  displays are used. Both displays are connected to the Raspberry Pi via Y-Cables.

The USB sound-card must be connected directly to the USB port Raspberry Pi. Loudspeaker can then be connected to the sound card using a 3.5 mm audio jack. Every Sound-effect used in this game was taken from [freesound.org](https://freesound.org/).

See the software documentation for information about controlling the [displays](https://4d-game.github.io/Gamecontrol/code-references/hardware/display_hal/) or [audio](https://4d-game.github.io/Gamecontrol/code-references/hardware/sound_hal/).

## Technical characteristics

| Name             | Parameter            |
| ---------------- | -------------------- |
| Display Color    | RGB 65K color        |
| Screen Size      | 2.2 inch             |
| Type             | TFT                  |
| Driver IC        | ILI9341              |
| Resolution       | 320*240 (Pixel)      |
| Module Interface | 4-wire SPI interface |
| Active Area      | 33.84x45.12(mm)      |

### Circuit (connection to Raspberry Pi)

![Display circuit](circuit/display.png)

### 3D-Model of Display bracket

![Display bracket](models/display/display_mount.png)


## Components

For a list of all used components see the [components](components.md) section.

## Further informations

All 3D-Models were done with Fusion360 and can be found on GitHub.
