# Known Issues

## pigpiod

```bash
sudo: unable to resolve host <hostname>: Name or service not known

2021-12-06 13:03:56 initInitialise: bind to port 8888 failed (Address already in use)
Can't initialise pigpio library
```

This issue occurs because of problems with your hostname make sure the hostnames in `/etc/hostname` and `/etc/hosts` are the same.