from machine import SoftI2C,Pin
import ssd1306 #引入ssd1306模块，ssd1306.py

i2c = SoftI2C(sda=Pin(15), scl=Pin(16))
#设置I2C的SDA与SCL所在的引脚
oled = ssd1306.SSD1306_I2C(128, 64,i2c,addr=0x3c)
#创建一个ssd1306.SSD1306_I2C类的对象，初始化并设置屏幕像素，i2c引脚,i2c地址
#ssd1306.SSD1306类继承了framebuf.FrameBuffer类，其方法即可在此使用
oled.fill(0)#清屏
oled.text("Hello world!", 0,  32)#设置在屏幕中将要显示的文字内容，设置起始像素点坐标
oled.show()#将内容输出到oled屏幕上
