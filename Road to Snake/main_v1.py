from machine import Pin,SPI,PWM
import framebuf
import time
from lcd114libs import LCD_1inch14

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = LCD_1inch14()
    #color BRG
    LCD.fill(LCD.white)
 
    LCD.show()   
    
    LCD.hline(1,1,238,LCD.blue)
    LCD.hline(1,133,238,LCD.blue)
    LCD.vline(1,1,133,LCD.blue)
    LCD.vline(238,1,133,LCD.blue)

    
    LCD.show()
    keyA = Pin(15,Pin.IN,Pin.PULL_UP)
    keyB = Pin(17,Pin.IN,Pin.PULL_UP)
    
    key2 = Pin(2 ,Pin.IN,Pin.PULL_UP) #上
    key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)#中
    key4 = Pin(16 ,Pin.IN,Pin.PULL_UP)#左
    key5 = Pin(18 ,Pin.IN,Pin.PULL_UP)#下
    key6 = Pin(20 ,Pin.IN,Pin.PULL_UP)#右
    
    x,y=1,1
    x1,y1=x+20,y+20
    LCD.fill_rect(x,y,x1,y1, LCD.red)
    LCD.show()
    
    while(1):
        if(keyA.value() == 0):
            print('keyA')
             
        if(keyB.value() == 0):
            print('keyB')

        if(key2.value() == 0):#Up
            LCD.fill_rect(x,y,x1,y1,LCD.white)
            y =y-5
            LCD.rect(x,y,x1,y1,LCD.red)
            LCD.show()
            print('key2')   
            
        if(key3.value() == 0):#中
            print('key3')

        if(key4.value() == 0):#左
            LCD.fill_rect(x,y,x1,y1,LCD.white)
            x =x-5
            LCD.rect(x,y,x1,y1,LCD.blue)
            LCD.show()
            print('key4')

        if(key5.value() == 0):#Down
            LCD.fill_rect(x,y,x1,y1,LCD.white)
            y =y+5
            LCD.rect(x,y,x1,y1,LCD.blue)
            LCD.show()
            print('key5')
  
        if(key6.value() == 0):#Right
            LCD.fill_rect(x,y,x1,y1,LCD.white)
            x =x+5
            LCD.rect(x,y,x1,y1,LCD.blue)
            LCD.show()
            print('key6')