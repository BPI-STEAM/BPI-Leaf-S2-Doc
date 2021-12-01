from machine import TouchPad
from machine import Pin
import time
t = TouchPad(Pin(2))

while True:
    print(t.read())
    time.sleep(0.5)