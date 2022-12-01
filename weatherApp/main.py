from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
import utime as time
from connect import connect
from weatherData import weatherData

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda = sda, scl = scl, freq=400000)
I2C_ADDR = i2c.scan()[0]
I2C_NUM_ROWS, I2C_NUM_COLS = 2, 16
 
i2c = I2C(0,sda=sda,scl=scl,freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

c = connect()

if c:
    lcd.move_to(0,0)
    lcd.putstr('Connected!')
    time.sleep(1)
else:
    topMessage = 'No Connection'
    time.sleep(1)
    quit()


s=.175
while True:
    topRow, bottomRow = weatherData()
    t = 20
    while t>0:
        lcd.move_to(0,0)
        lcd.putstr(topRow)
        lcd.move_to(0,1)
        lcd.putstr(bottomRow[0:16])
        time.sleep(2)
        for chunk in range(0, len(bottomRow)-16):
            lcd.move_to(0,1)
            lcd.putstr(bottomRow[chunk:chunk+16])
            time.sleep(s)
        time.sleep(2)
        t-=1
    
