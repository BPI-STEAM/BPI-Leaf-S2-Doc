from machine import Pin, DAC
import time

dac = DAC(Pin(17))#仅GPIO17,18有DAC

while True:
   #DAC 8bit精度，0-255对应0-3.3V
    for i in range(180,256,1):
       dac.write(i)
       time.sleep_ms(10)
    for i in range(255,180,-1):
       dac.write(i)
       time.sleep_ms(20)