from connect import connect
from machine import Pin,SPI
import framebuf
import time
from oledLib import OLED_1inch3
from weatherDataJSON import weatherData
import json
from sampleResponse import sampleResponse

d=sampleResponse

fiveDay = [
    {
        'date': f"{ea['datetime'].split('-')[1]}/{ea['datetime'].split('-')[2]}",
        'tempmax': ea['tempmax'],
        'tempmin': ea['tempmin'],
        'conditions': ea['conditions'],
        'precipType': ea['precip'],
        'precipProb': ea['precipprob']
    }for ea in d[1]['daily']
    ]
print(fiveDay)


connect()
OLED = OLED_1inch3()
#d = weatherData()

keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)

def ab():
    OLED.fill(0x0000)
    OLED.text('AB',50,25,OLED.white)
    OLED.show()
    time.sleep(2)
    
def a():
    OLED.fill(0x0000)
    OLED.text('A',50,25,OLED.white)
    OLED.show()
    time.sleep(2)
    
def b():
    OLED.fill(0x0000)
    OLED.text('B',50,25,OLED.white)
    OLED.show()
    time.sleep(2)
    
def default():
    OLED.fill(0x0000)
    OLED.text('booby',50,25,OLED.white)
    OLED.show()

def scrollPause(ms):
    while (keyA.value()!=0 and keyB.value()!=0) and ms>0:
        try:
            time.sleep(0.001)
        except (keyA.value()==0 or keyB.value()==0):
            break
        ms-=1



def mainScreen():
    try:
        OLED.fill(0x0000)
        c = d[0]['current']
        line1 = f"Temp:{c['current']}{' '*(16-len(str(c['current']))-len(str(c['max']))-len(str(c['min']))-7)}{c['max']}/{c['min']}"
        line2 = c['conditions']
        line3 = c['description']
        OLED.text(line1,2,2,OLED.white)
        if len(line2)<15:
            OLED.text(line2,2,21,OLED.white)
        else:
            OLED.text(line2,2,21,OLED.white)
        if len(line3)<15:
            OLED.text(line3,2,40,OLED.white)
        else:
            OLED.fill_rect(0,30,128,64,OLED.black)
            OLED.text(line3[0:16],2,40,OLED.white)
            OLED.show()
            scrollPause(1500)
            while (keyA.value() != 0 and keyB.value() !=0):
                for chunk in range(0,len(line3)-15):
                    print(chunk)
                    OLED.fill_rect(0,30,128,64,OLED.black)
                    OLED.text(line3[chunk:chunk+15],2,40,OLED.white)
                    OLED.show()
                break
            scrollPause(1500)
            mainScreen()
    except:
        next

def fiveDay():
    OLED.fill(0x0000)
    x = 5
    inc = 50
    for ea in d[1]['daily']:
        OLED.text(ea['datetime'].split('-')[2],round(x), 5,OLED.white)
        OLED.text(str(ea['tempmax']),round(x), 30,OLED.white)
        x+=inc
    OLED.show()
    time.sleep(2)



buttonPause = 20

def setKey():
    mainScreen()
    if (keyA.value()==0 or keyB.value()==0):
        if (keyA.value()==0 and keyB.value()==0):
            time.sleep(buttonPause/1000)
            if (keyA.value()==0 and keyB.value()==0):          
                screen = 'mainScreen'
            else:
                next
            
        elif (keyA.value()==0):
            time.sleep(buttonPause/1000)
            if keyA.value()==0:
                screen = 'fiveDay'
            else:
                next
            
        elif (keyB.value()==0):
            time.sleep(buttonPause/1000)
            if keyB.value()==0:
                screen = 'fiveDay'
            else:
                next
        if screen == 'mainScreen':
            mainScreen()
        elif screen == 'fiveDay':
            fiveDay()
            mainScreen()        

if __name__=='__main__':
    while True:
        setKey()
        
