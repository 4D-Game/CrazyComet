# Streamer Setup

## Development

To write code and generate the documentation you need to install the packages listed in `requirements.dev.txt` with `pip`

```bash
pip install -r requirements.dev.txt
```

### Documentation

The Documentation is generated with the help of [mkdocstrings](https://mkdocstrings.github.io/#). To implement a module, class or function into your documentation you have to reference it as follows:

```md
::: library.module

::: library.module.class

::: library.module.function
```

## On Device

For the usage on Device the packages listed in `requirements.txt` should be installed:

```bash
pip install -r requirements.txt
```

Next run `scripts/generate-config` to generate a streamerconfiguration with your gametoken and a device ID at `./srtg.toml`

To activate/update the streamerconfiguration on your device run `scripts/streamer-setup
!!! warning
    This will replace the `/etc/srtg/srtg.toml` from the Surrogate SDK

Next setup the controller service with `scripts/setup`
!!! warning
    This will replace the `controller.service` from the Surrogate SDK
