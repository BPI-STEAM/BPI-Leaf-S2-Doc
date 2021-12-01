from machine import SoftSPI,Pin
from max7219 import Max7219
import time

spi = SoftSPI(baudrate=10000000,
              polarity=1,
              phase=0,
              sck=Pin(3,Pin.OUT),
              mosi=Pin(1,Pin.OUT),
              miso=Pin(4,Pin.OUT))
screen = Max7219(width=8,
                 height=8,
                 spi=spi,
                 cs=Pin(2,Pin.OUT),
                 rotate_180=False)
text= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = []
for x in text:
  list1.append(x)
screen.brightness(1)

while True:
    for i in range(len(list1)):
        screen.fill(0)
        screen.text(list1[i], 0, 0, 1)
        screen.show()
        time.sleep(0.5)