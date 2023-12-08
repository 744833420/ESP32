# 引入模块  eval() 可以将input返回的结果转换成数字类型
from machine import Pin
led1 = Pin(15, Pin.OUT)
led2 = Pin(16, Pin.OUT)
led3 = Pin(10, Pin.OUT)

"""
新建一个Python脚本文件，实现美元和人民币汇率转换程序
"""
"""
china = eval(input("请输入中国财产：(元)"))
change =eval(input("请输入汇率："))

print("你可以得到美元：",china/change,"美元")
"""

f = 1.23456e2
print(f)
# 强制类型转换   类型（）
print(int(f))
print(bool(f))

"""
购物抹零操作
"""
a = eval(input("请输入你的金额："))
print("你的金额抹零实际支付:", int(a))

"""
运算符  //：整除  **：幂运算
"""
# a=eval(input("请输入一个三位数："))
# res=0
#
# res+=a//100
# res+=a%100//10
# res+=a%10

# print("三个数之和为：",res)


# 断路原则
# 非0既为真
x, y = 0, 5
print(x and y)  # 相当于与操作 只要是第一个为假的 后来的就不执行了
print(x or y)  # 相当于或操作   只要是第一个为真 后来的就不看了

# 位运运算
p = 3  # 0011
q = 5  # 0101
print(bin(p & q))

# 通过异或进行数据交换
data1 = "1222"
data2 = "635"
data1 = int(data1)
data2 = int(data2)
data1 = data1 ^ data2
data2 = data1 ^ data2
data1 = data1 ^ data2

print(data1, data2)
