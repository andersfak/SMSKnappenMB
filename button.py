from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause
import serial

led = LED(5)
button = Button(2)


def pressed():
    led.on()
    

def released():
    #Send the text message

    number = '0706881946'
    text = 'Infodisken!' 
        
    ser = serial.Serial('/dev/ttyUSB0', timeout=5)
    sleep(0.5)
    ser.write(str.encode('AT\r'))
    sleep(0.5)
    ser.write(str.encode('AT+CMGF=%d\r' % 1))
    sleep(0.5)
    ser.write(str.encode('AT+CMGS="%s"\r' % number))
    sleep(0.5)
    ser.write(str.encode('%s\x1a' % text))
    sleep(0.5)      
    print(ser.readlines())
    ser.close()


    j = 0
    while j < 10:
        led.on()
        sleep(0.8)
        led.off()
        sleep(0.8)
        j += 1


button.when_pressed = pressed
button.when_released = released

pause()
