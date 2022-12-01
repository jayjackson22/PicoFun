import rp2
import network
import ubinascii
import machine
import urequests as requests
import time
from secrets import secrets
import socket

def blink_onboard_led(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(0,num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)

blink_onboard_led(5)