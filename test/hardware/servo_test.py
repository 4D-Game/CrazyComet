import RPi.GPIO as GPIO
import time

l = 0
r = 0

lServoPin = 17
rServoPin = 27
GPIO.setmode(GPIO.BCM) 

GPIO.setup(lServoPin, GPIO.OUT)
GPIO.setup(rServoPin, GPIO.OUT)

lPwm = GPIO.PWM(lServoPin, 50)
rPwm = GPIO.PWM(rServoPin, 50)
lPwm.start(5)
rPwm.start(5)

x=0    
while(x<5):
    for i in range(45, 135):
        positionl = 1./18.*(i)+2
        positionr = 1./18.*(180-i)+2
        lPwm.ChangeDutyCycle(positionl)
        rPwm.ChangeDutyCycle(positionr)
        time.sleep(0.005)
    for i in range(135, 45, -1):
        positionl = 1./18.*(i)+2
        positionr = 1./18.*(180-i)+2
        lPwm.ChangeDutyCycle(positionl)
        rPwm.ChangeDutyCycle(positionr)
        time.sleep(0.005)
    x = x + 1

lPwm.stop()
rPwm.stop()
GPIO.cleanup()