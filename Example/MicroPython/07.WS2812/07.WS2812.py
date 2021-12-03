from machine import Pin
from neopixel import NeoPixel
import time

pin_18 = Pin(18, Pin.OUT)#将GPIO18作为WS2812的信号传输线
np = NeoPixel(pin_18, 1,bpp=3, timing=1)
# 在GPIO18上创建一个NeoPixel对象，设置数量1，bpp=3为RGB模式，4为RGBW模式，timing=1为800kHz，0为400kHz
red,green,blue=25,0,0
np[0] = (red,green,blue) # 设置第一个像素的RGB三色亮度
np.write()# 输出信号给WS2812

while True:
    #彩虹灯循环
    for green in range (1,26):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for red in range (24,-1,-1):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for blue in range (1,26):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for green in range (24,-1,-1):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for red in range (1,26):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for blue in range (24,-1,-1):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)
        