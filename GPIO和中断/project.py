from machine import Pin
import time

led_pin = [0]
leds = []  # 存储管脚控制对象的列表

# for i in led_pin:
#     leds.append(Pin(i,Pin.OUT))  #配置OUT端口模式
# 推导式写法
Pin(0,Pin.OUT)
while True:
    # 依次点亮LED灯
    Pin(0,Pin.OUT).value(0)
    time.sleep(1)
    Pin(0,Pin.OUT).value(1)
    time.sleep(1)
