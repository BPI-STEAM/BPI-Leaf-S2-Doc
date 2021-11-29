from machine import Pin, ADC
import time

adc = ADC(Pin(1))#在ADC引脚上创建ADC对象
adc.atten(ADC.ATTN_11DB)#设置11dB衰减输入(测量最大电压约为3.6v)
ADC.width(ADC.WIDTH_13BIT)#ESP32S2仅支持13bit精度

while True:
    print(adc.read())# 获取测量值
    time.sleep(0.5)