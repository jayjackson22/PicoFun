from machine import Pin,SPI,PWM
import framebuf
import time
from lcd114libs import LCD_1inch14
import random


BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

pwm = PWM(Pin(BL))
pwm.freq(1000)
pwm.duty_u16(32768)#max 65535

LCD = LCD_1inch14()

def dice(lcd,x,y,l):
    LCD=lcd
    d1 = [
        (x,y),
        (x+l,y),
        (x+l,y+l),
        (x,y+l)
    ]
    
    margin = 5
    dotSize = 20
    for ea in range(len(d1)):
        try:
            x1 = d1[ea][0]
            y1 = d1[ea][1]
            x2 = d1[ea+1][0]
            y2 = d1[ea+1][1]
            LCD.line(x1,y1,x2,y2,LCD.blue)
        except:
            x1 = d1[ea][0]
            y1 = d1[ea][1]
            x2 = d1[0][0]
            y2 = d1[0][1]
            LCD.line(x1,y1,x2,y2,LCD.blue)
    def dot1():
        LCD.fill_rect(x+margin,y+margin,dotSize,dotSize,LCD.red)
    def dot2():
        LCD.fill_rect(x+margin,round(y+((y+l)/2)-dotSize),dotSize,dotSize,LCD.red)
    def dot3():
        LCD.fill_rect(x+margin,round(y+l-margin-dotSize),dotSize,dotSize,LCD.red)
    def dot4():
        LCD.fill_rect(x+l-(margin+dotSize),y+margin,dotSize,dotSize,LCD.red)
    def dot5():
        LCD.fill_rect(x+l-(margin+dotSize),round(y+((y+l)/2)-dotSize),dotSize,dotSize,LCD.red)
    def dot6():
        LCD.fill_rect(x+l-(margin+dotSize),round(y+l-margin-dotSize),dotSize,dotSize,LCD.red)
    def dot7():
        LCD.fill_rect(round(x+(l/2)-(dotSize/2)),round(y+(l/2)-(dotSize/2)),dotSize,dotSize,LCD.red)
    def three():
        dot1()
        dot7()
        dot6()
    def numbers(LCD, i):
        if i==1:
            dot7()
        elif i==2:
            dot3()
            dot4()
        elif i==3:
            dot3()
            dot4()
            dot7()
        elif i==4:
            dot1()
            dot3()
            dot4()
            dot6()
        elif i==5:
            dot1()
            dot3()
            dot4()
            dot6()
            dot7()
        elif i==6:
            dot1()
            dot2()
            dot3()
            dot4()
            dot5()
            dot6()
        return LCD
    roll = random.randrange(1,7)
    LCD = numbers(LCD, roll)
    return LCD, roll

