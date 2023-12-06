#引号的使用   单引号可以包含双引号 三引号  总的来说 不通的引号只能包含  其他的引号
str1='我们就要结婚了'
print(str1)

str2="我们马上就要有工作了"
print(str2)

str3="我们就要'挣钱'了"
print(str3)

str4='"生小孩"哈哈哈'
print(str4)

str5="""
     鹅鹅鹅，
     曲项向天歌，
     白毛浮丽水。
     红掌拨清波。
"""
print(str5)



#索引  正向索引  反向索引


str6="dclasncaslcl;asnmcaspodhpaoscxasmc "

print(str6[-2])


str7="青岛今天真的寒冷"

for i in range(0,8):
    print(str7[i],end=" ")
print(" ")
for i in str7:
    print(i,end=" ")

#字符串的切片访问
str8="1234567ABCDEFG"

print("\n进行切片操作",str8[0:7:1])
print("\n进行字母切片",str8[7::1])

print(str8[::2])

print(str8[-1::-1])


#字符串可以乘法
str9="张来博  "

print(str9*9)


#format 格式化用法

print("{}+{}={}".format(5,6,5+6))