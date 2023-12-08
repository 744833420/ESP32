# while 循环

"""
打印9*9乘法表
"""
i = 1
j = 1
while i <= 9:
    while j <= i:
        print(j, "*", i, "=", i * j, end=" ")
        j += 1
    print("\n")
    i += 1
    j = 1
