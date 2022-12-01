import network
from secrets import secrets
import time

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets['ssid'], secrets['pw'])
    n=30
    while n>0 and not wlan.isconnected():
        print('Connecting...', end='\r')
        n-=1
        time.sleep(1)
    if wlan.isconnected():
        conn = True
    else:
        conn = False
    return conn