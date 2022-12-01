from machine import Pin,SPI,PWM
import framebuf
import time
from lcd114libs import LCD_1inch14
from dice import dice
import random

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
    LCD.fill(0x0000)
    LCD.text("View stats ==>",118,15, LCD.white)
    LCD.text("<== Clear history",5,65, LCD.white)
    LCD.text("Roll the dice ==>",97,110, LCD.white)
    LCD.show()

    keyA = Pin(15,Pin.IN,Pin.PULL_UP)
    keyB = Pin(17,Pin.IN,Pin.PULL_UP)
    
    key2 = Pin(2 ,Pin.IN,Pin.PULL_UP) #上
    key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)#中
    key4 = Pin(16 ,Pin.IN,Pin.PULL_UP)#左
    key5 = Pin(18 ,Pin.IN,Pin.PULL_UP)#下
    key6 = Pin(20 ,Pin.IN,Pin.PULL_UP)#右
    
    history = []

    while(.1):
        if (keyA.value()==0):
            LCD.fill(LCD.white)
            LCD.show()
            histSummary = [
                sum(1 for x in history if x == num)for num in range(2,13)
            ]
            print(histSummary)
            step=5
            stepText=step-3
            barMax = 100
            barMin = 10
            maxCount=max(histSummary) 

            try:                
                countValue = ((barMax-barMin)/maxCount)-10+barMin
            except:
                countValue = 109

            for ea in range(2,13):
                count = sum(1 for x in history if x == ea)
                barY = round(110-(count*countValue))-10
                LCD.text(str(ea), step,120, 0x0000)
                LCD.fill_rect(round(stepText), round(110-(count*countValue)),15,round(count*countValue),LCD.blue)
                LCD.text(str(count), step, barY,0x0000)
                step+=21
                stepText=step-2
                if ea >= 10:
                    step+=2
                    stepText+=2
            LCD.show()
            time.sleep(.75)
        if (keyB.value()==0):
            i=random.randrange(5,20)
            while i>0:
                LCD.fill(0xffff)
                LCD, roll1 = dice(LCD,10,18,100)
                LCD, roll2 = dice(LCD,130,18,100)
                total = roll1+roll2
                LCD.text(str(roll1+roll2),0,0,0x0000)
                LCD.show()
                time.sleep(random.randrange(1,100)/1000)
                i-=1
            history.append(total)
            time.sleep(.75)
        if (key3.value()==0):
            history = []
            LCD.fill(0xffff)
            LCD.text("History cleared",15,65, LCD.blue)
            LCD.show()

# if(keyA.value() == 0):
        #     LCD.fill(0x0000)
        #     for ea in range(0,135,25):
        #         LCD.line(0,ea,240,ea,LCD.blue)
        #         LCD.text(str(ea),5,ea,LCD.white)
        #     for ea in range(0,240,25):
        #         LCD.line(ea,0,ea,135,LCD.blue)
        #         LCD.text(str(ea),ea,5,LCD.white)
        #     LCD.show()
             
        # if(keyB.value() == 0):
        #     LCD.fill(0x0000)
        #     d1 = [
        #         (10,18),
        #         (110,18),
        #         (110,118),
        #         (10,118)
        #     ]
            
        #     for ea in range(len(d1)):
        #         try:
        #             x1 = d1[ea][0]
        #             y1 = d1[ea][1]
        #             x2 = d1[ea+1][0]
        #             y2 = d1[ea+1][1]
        #             LCD.line(x1,y1,x2,y2,LCD.blue)
        #         except:
        #             x1 = d1[ea][0]
        #             y1 = d1[ea][1]
        #             x2 = d1[0][0]
        #             y2 = d1[0][1]
        #             LCD.line(x1,y1,x2,y2,LCD.blue)
        #     LCD.show()

        # if(key2.value() == 0):#Up
        #     LCD.fill_rect(x,y,x1,y1,LCD.white)
        #     y =y-5
        #     LCD.rect(x,y,x1,y1,LCD.red)
        #     LCD.show()
        #     print('key2')   
            
        # if(key3.value() == 0):#中
        #     LCD.fill(0x0000)
        #     dice(10,18,100)
        #     dice(130,18,100)

        # if(key4.value() == 0):#左
        #     LCD.fill_rect(x,y,x1,y1,LCD.white)
        #     x =x-5
        #     LCD.rect(x,y,x1,y1,LCD.blue)
        #     LCD.show()
        #     print('key4')

        # if(key5.value() == 0):#Down
        #     LCD.fill_rect(x,y,x1,y1,LCD.white)
        #     y =y+5
        #     LCD.rect(x,y,x1,y1,LCD.blue)
        #     LCD.show()
        #     print('key5')
  
        # if(key6.value() == 0):#Right
        #     LCD.fill_rect(x,y,x1,y1,LCD.white)
        #     x =x+5
        #     LCD.rect(x,y,x1,y1,LCD.blue)
        #     LCD.show()
        #     print('key6')