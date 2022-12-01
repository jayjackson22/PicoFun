#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time
import random

from yaml import BlockSequenceStartToken


redPin = 11
greenPin = 13
bluePin = 15



def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(redPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.setup(bluePin, GPIO.OUT)
def redOn():
    GPIO.output(redPin, GPIO.HIGH)
def redOff():
    GPIO.output(redPin, GPIO.LOW) 
def greenOn():
    GPIO.output(greenPin, GPIO.HIGH)
def greenOff():
    GPIO.output(greenPin, GPIO.LOW)
def blueOn():
    GPIO.output(bluePin, GPIO.HIGH)
def blueOff():
    GPIO.output(bluePin, GPIO.LOW)

delay = .1

def loop():
    while True:
        redOn()
        blueOff()
        greenOff()
        time.sleep(delay)
        redOff()
        blueOn()
        greenOff()
        time.sleep(delay)
        redOff()
        blueOff()
        greenOn()
        time.sleep(delay)
        redOff()
        blueOn()
        greenOff()
        time.sleep(delay)

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

