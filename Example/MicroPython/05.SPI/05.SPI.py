from machine import SoftSPI,Pin
from max7219 import Max7219
import time

spi = SoftSPI(baudrate=10000000, #SCK时钟频率
              polarity=1, #时钟线空闲时高电平，有效时低电平
              phase=0, #相位，在第一时钟沿采样数据
              sck=Pin(3,Pin.OUT), #CLK
              mosi=Pin(1,Pin.OUT),#DIN
              miso=Pin(4,Pin.OUT))#max7219三线即可控制，miso可不接
screen = Max7219(width=8,#LED点阵宽
                 height=8,#LED点阵高
                 spi=spi, #设置SPI
                 cs=Pin(2,Pin.OUT),#CS
                 rotate_180=False)
text= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = []
for x in text:
  list1.append(x) #将text中的字符串逐一取出放入list1列表
screen.brightness(1)#设置亮度，最高15

while True:
    for i in range(len(list1)):#获取list1列表内元素的总数并以此数进行for循环
        screen.fill(0)#清屏
        screen.text(list1[i], 0, 0, 1)#设置将要显示的内容及位置
        screen.show()#显示输出
        time.sleep(0.5)