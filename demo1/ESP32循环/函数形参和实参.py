# 位置函数

def sub(y, x=5):  # 如果函数中有缺省值  则缺省值应在其他函数之后
    """x-y 求差"""
    return x - y


print(sub(7))


# 参数的传递方式
# 可变参数   参数列表

def sub1(x=9, y=8, *args, **kwargs):  # 如果函数中有缺省值  则缺省值应在其他函数之后  第三个为参数元组   第四个为字典
    """x-y 求差"""
    if len(args) != 0:
        print(args)
    for key in kwargs:
        print(key, ":", kwargs[key])
    return x - y


print(sub1(1, 1, "张三", 2.13, [1, 2, 3]))

print(sub1(1, 7, name="张三", age=66))
