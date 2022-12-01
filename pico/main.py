import rp2
import network
import ubinascii
import urequests
import machine
import urequests as requests
import time
from secrets import secrets
import socket
import random

wlan = network.WLAN(network.STA_IF)
wlan.connect(secrets['ssid'], secrets['pw'])
wlan.active(True)

attempts = 10
while attempts>0:
    if wlan.isconnected():
        break
    else:
        wlan.active(True)
        attempts -= 1

if wlan.isconnected():
    print(f"Connected")
else:
    print(f"Not Connected")

def blink_onboard_led(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(0,num_blinks):
        led.on()
        time.sleep(random.random()/10)
        led.off()
        time.sleep(random.random()/10)

blink_onboard_led(50)
