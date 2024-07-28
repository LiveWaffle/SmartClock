from machine import Pin, I2C 
import machine, onewire, ds18x20, time
import ssd1306
import time

i2c = I2C(0, scl=Pin(15), sda=Pin(2))

dq_pin = machine.pin(35)
dq_sensor = ds18x20.DS18X20(onewire.OneWire(dq_pin))
roms = ds_sensor.scan()



oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Poo', 10, 10)      
oled.show()
