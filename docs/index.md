# Controller

The *Controller* repository contains the code for the raspberry pi's wich control the different game figures (e.g. the turrets). In the following those Raspberry Pi's are called **Controller**. Each Controller can get an id by setting the `seat` variable in the config.toml.

!!! NOTE
    The id of the controller must also be named in the `seats` variable of your [Gamecontrol](https://4d-game.github.io/Gamecontrol/).

## Structure

The entry point of the game is the `CrazyComet` class in *src/main.py*. This is a subclass of `Game` from `game_sdk.controller` (See the [sdk documentation](https://4d-game.github.io/sdk)). To start the game `CrazyComet.run()` is executed.

Furthermore the *src* folder consist of a *hardware* and *controls* folder wich will be explained below.

### Hardware

This is the hardware abstraction layer. It is used to expose hardware interfaces to the rest of the programm.

As defined in the `HAL` baseclass, every `HAL` class should have the following methods:

- `__init__()`
- `close()`

!!! NOTE
    Every class in the hardware abstraction layer should inherit from `HAL`

### Controls

This folder contains classes wich interact directly with the game (eg. responding to gamepad inputs).

Classes interacting with the gamepad should always be subclasses of an `Input` class (See the [sdk documentation](https://4d-game.github.io/sdk/controller-sdk/code-references/input/)).

To register a `Input` class to the **game sdk** it should be instanciated in the `CrazyComet` class. There it is added to the dictionary `controls` with the desired `KeyCode` or `JoystickCode` as key.

Example:

```python
self.controls = {
    KeyCode.BUT_0: MyControl(seat, 'MyControl', args**)
}
```

