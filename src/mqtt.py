"""
Created: 11.11.21
by: Lukas Schüttler

Get/Set mqtt client object
"""

import random
from typing import Any, Callable
import paho.mqtt.client as mqtt

client = None
"""
 Singleton for MQTT client object
"""


def connect(on_connect: Callable[[mqtt.Client, Any, Any, Any]] = None):
    """
      Connect to MQTT Broker

      Arguments:
          on_connect: Callbackfunction which is called when the MQTT client is connected
    """

    global client

    # read config
    broker_ip = "localhost"
    broker_port: 1883
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    username: str = None
    password: str = None,

    client = mqtt.Client(client_id)

    if username:
        client.username_pw_set(username, password)

    client.on_connect = on_connect
    client.connect(broker_ip, broker_port)


@client.getter
def getClient():
    """
      get MQTT client object
    """

    return client
