#!/usr/bin/env python3

"""
Created: 10.04.21
by: Lukas Schüttler

Entrypoint for the Streamer programm
"""

import logging
import mqtt
from game import LoopinLouie


def on_connect(client, userdata, flags, rc):
    """
      Function which is executed after MQTT broker is connected
    """

    if rc == 0:
        logging.info("MQTT Broker connected")
        mqtt.client.publish('status/logging', {"seat": None, "severity": "info", "message": "MQTT Broker connected"})
    else:
        logging.warning("Failed to connect to MQTT Broker! Return code %d\n", rc)


if __name__ == "__main__":
    mqtt.connect(on_connect)
    LoopinLouie.run()
