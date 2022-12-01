from connect import connect
from machine import Pin,SPI
import framebuf
import time
from oledLib import OLED_1inch3
from weatherDataJSON import weatherData
import json

#with open('weatherResponse.json','r') as f:
#    d = json.loads(f.read())

connect()
OLED = OLED_1inch3()
d = weatherData()

keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)


if __name__=='__main__':
    OLED.fill(0x0000) 
    keyA = Pin(15,Pin.IN,Pin.PULL_UP)
    keyB = Pin(17,Pin.IN,Pin.PULL_UP)
    
    while(1):
        '''Default screen'''
        if keyA.value() != 0 and keyB.value() !=0:
            OLED.fill(0x0000)
            c = d[0]['current']
            line1 = f"Temp:{c['current']}{' '*(16-len(str(c['current']))-len(str(c['max']))-len(str(c['min']))-7)}{c['max']}/{c['min']}"
            line2 = c['conditions']
            line3 = c['description']
            OLED.text(line1,2,2,OLED.white)
            if len(line2)<15:
                OLED.text(line2,2,21,OLED.white)
            else:
                bah
            if len(line3)<15:
                OLED.text(line3,2,40,OLED.white)
            else:
                OLED.fill_rect(0,30,128,64,OLED.black)
                OLED.text(line3[0:16],2,40,OLED.white)
                OLED.show()
                time.sleep(2)
                for chunk in range(0,len(line3)-15):
                    if (keyA.value() != 0 and keyB.value() !=0 ):
                        OLED.fill_rect(0,30,128,64,OLED.black)
                        OLED.text(line3[chunk:chunk+15],2,40,OLED.white)
                        OLED.show()
                    else:
                        break
                time.sleep(2)
            OLED.show()
        
        '''
        for ea in current:
            s = time.time()+10
            if (keyA.value() != 0 and keyB.value() !=0):
                OLED.fill(OLED.black)
                OLED.text(ea,18,18,OLED.white)
                OLED.show()
                if len(str(current[ea]))<16:
                    OLED.fill_rect(0,30,128,64,OLED.black)
                    OLED.text(str(current[ea]),5,32,OLED.white)
                    OLED.show()
                else:
                    txt = f"{str(current[ea])}"
                    OLED.fill_rect(0,30,128,64,OLED.black)
                    OLED.text(txt[0:16],5,32,OLED.white)
                    OLED.show()
                    time.sleep(2)
                    for chunk in range(0,len(txt)-15):
                        if (keyA.value() != 0 and keyB.value() !=0):
                            OLED.fill_rect(0,30,128,64,OLED.black)
                            OLED.text(txt[chunk:chunk+16],5,32,OLED.white)
                            OLED.show()
                        else:
                            next
                    time.sleep(2)
                time.sleep(3)
        '''               

        '''Key A Pressed'''
        if keyA.value() == 0:
            OLED.fill_rect(0,0,128,64,OLED.white)
            OLED.text("Hey Baby", 20,30,OLED.black)
        else :
            next
        
        '''Key B Pressed'''
        if(keyB.value() == 0):
            OLED.fill_rect(0,0,128,64,OLED.white)
            txt = f"{' '*16}booooooooooooooooooooooobs{' '*16}"
            for chunk in range(0,len(txt)):
                if (keyA.value() != 0):
                    OLED.fill(0x0000)
                    OLED.text(txt[chunk:chunk+16],2,26,OLED.white)
                    OLED.show()
                else :
                    next
            
        if(keyA.value() == 0 and keyB.value() == 0):
            OLED.fill_rect(0,0,128,64,OLED.white)
            OLED.text("oogyboogy",20,32, OLED.black)
        else :
            next
        
        OLED.show()
