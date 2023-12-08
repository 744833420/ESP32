from machine import Pin
# 设置esp32的GPIO15、2、0引脚为输出模式
led1 = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(0, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(16, Pin.OUT)
led6 = Pin(17, Pin.OUT)
led7 = Pin(5, Pin.OUT)
led8 = Pin(18, Pin.OUT)


led1.value(1)  # 高电平
led2.value(0)
led3.value(1)
led4.value(1)  # 高电平
led5.value(0)
led6.value(1)
led7.value(1)  # 高电平
led8.value(1)
