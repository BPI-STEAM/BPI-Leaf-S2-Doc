from machine import Pin
import time 
pin13 = Pin(13,Pin.OUT)
n = 0
while True:
    pin13.value(1)
    time.sleep(0.5)
    pin13.value(0)
    time.sleep(0.5)
    n+=1
    print(n)