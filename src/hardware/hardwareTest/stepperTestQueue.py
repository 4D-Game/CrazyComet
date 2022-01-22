#!/usr/bin/env python3

"""
Created: 11/22/21
by: Sonja Lukas
Tower control with 2 stepper
Game part
"""

#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from Adafruit_MotorHAT.Adafruit_MotorHAT_Motors import Adafruit_MotorHAT
from ..hardware.stepperHAL import StepperHAL

import time
import atexit 
import logging
import threading
import asyncio
import queue

class Stepper(): #Control
    """
        Gamecontroll Stepper
    """

    def __init__(self):
        self.stepper1 = StepperHAL("myStepper1",1,20)
        self.stepper2 = StepperHAL("myStepper2",2,20) 

    async def set_start_position(self):
        """
            set start position after each game round 
        """
        await self.set_position(100)

    async def get_score(self):
        """
            Control depending on the score 
            Attribute: 
        """
        # on end:
        # await self.motor_stop() # todo: change in on_end at game_sdk
        pass

    async def set_values(self):
        pass

    async def game_run(self):
        """
            game starts in game sdk
            mapping attributes to rotate()
        """ 
        #start=time.time()
         
        if self.port_number==2: #test put 3 in
            self.thread_queue.put({'rpm': 20, 'step_size': 100, 'direction': Adafruit_MotorHAT.FORWARD})
            self.thread_queue.put({'rpm': 20, 'step_size': 100, 'direction': Adafruit_MotorHAT.BACKWARD})
            self.thread_queue.put({'rpm': 30, 'step_size': 100, 'direction': Adafruit_MotorHAT.FORWARD})
        
        if self.port_number==1:
            self.thread_queue.put({'rpm': 20, 'step_size': 50, 'direction': Adafruit_MotorHAT.FORWARD}) 
            self.thread_queue.put({'rpm': 20, 'step_size': 50, 'direction': Adafruit_MotorHAT.BACKWARD})

        await self.rotate()

        #duration = time.time()-start
        #logging.info(f"set_start_position Duration: {duration}")  
                        
    async def on_exit(self):
        """
            threading stop, motor_release via atexit register 
        """
        await self.set_start_position() 
        self.close()    #todo: check hal.close

async def main():
    await asyncio.gather((Stepper.stepper1.game_run()),(Stepper.stepper2.game_run()))

if __name__ == "__main__":
    asyncio.run(main())