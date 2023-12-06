#使用LED1~LED4实现流水灯程序·
#连接ESP32管脚和LED模块(Pin15-D1、Pin2-D2、Pin0-D3、Pin4-D4)
#LED1~LED4依次亮起，再依次熄灭，循环这个过程

from machine  import Pin
import time

led_pin=[15,2,0,4,16,17,5,18]
leds=[]  #存储管脚控制对象的列表

# for i in led_pin:
#     leds.append(Pin(i,Pin.OUT))  #配置OUT端口模式
#推导式写法
leds = [Pin(i,Pin.OUT) for i in led_pin]

while True:
    #依次点亮LED灯
    for i in leds:
        i.value(1)
        time.sleep(0.03)
    #依次熄灭LED灯
    for i in leds:
        i.value(0)
        time.sleep(0.03)
    for i in range(3):
        #依次点亮LED灯
        for i in leds:
            i.value(1)
        #依次熄灭LED灯
        time.sleep(0.05)
        for i in leds:
            i.value(0)

    
