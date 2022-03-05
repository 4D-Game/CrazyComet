#!/usr/bin/env python3
"""Lichtschranke hat ein invertierender Logik:0 wenn ein und 1 wenn aus
Um mehrfache Erkennung von einem Punkt zu vermeiden, wird nur steigende Flanke ausgewertet.
Wird eine Flanke erkannt, wird counter inkrementiert und LED entsprechend ein und ausgeschaltet

"""
import RPi.GPIO as GPIO
import time
 
SENSOR_PIN = 24
LED_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

count = 0
def increment():   #counter incrementieren
    global count
    count+=1
    print(count)

def mein_callback(channel):
    GPIO.output(LED_PIN, GPIO.LOW)
    print('touch')
    increment()   # zählen, wie viel mal Objekt erkannt 
    if count % 2:   #ungerade index LED ein
        GPIO.output(LED_PIN, GPIO.HIGH) 
    else:             #gerade index LED aus 
        GPIO.output(LED_PIN, GPIO.LOW)
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback) #es wird steigende Flanke erkannt
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print ("End")
GPIO.cleanup()