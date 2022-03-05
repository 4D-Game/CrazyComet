# Controller Setup

## Setup
### Setup script

To setup everything needed, to run the game there is a setup script, which can be executed with the following command:

```bash
scripts/pi-setup
```

After this you have to activate SPI by adding `dtparam=spi=on` to the *boot/config.txt*. Next the Raspberry Pi needs to be rebooted.

### Manual
#### SDK

The sdk needed to use this program is stored in a submodule. To use it the following commands should be executed:

```bash
git submodule init
git submodule update
```

!!! INFO
    To update the sdk to the latest commit run

    ```bash
    git submodule update --remote --merge
    ```

#### PYTHONPATH
Add the `src` and `lib/sdk` folder to your `PYTHONPATH`

```bash
export PYTHONPATH="$(pwd)/src:$(pwd)/lib/sdk"
```

#### Python Dependencies

In order to install all python dependencies run:

```bash
pip3 install -Ur requirements.txt
```

#### SPI

The Programm uses SPI to control the LED's of the turrets. Enable SPI by adding `dtparam=spi=on` to the *boot/config.txt*. This activates SPI after the next reboot.

## Autostart

The game can be started automatically using `systemd`. Register the *controller.service* by executing the script `scripts/systemd-setup`.

## Documentation

The Documentation is generated with the help of [mkdocstrings](https://mkdocstrings.github.io/#). To implement a module, class or function into your documentation you have to reference it as follows:

```md
::: library.module

::: library.module.class

::: library.module.function
```