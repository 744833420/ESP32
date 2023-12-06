#元组  不可修改的列表  使用括号  () 创建 元组 要加 逗号
tuple1 = (1)   #这不是元组
tuple2 = (1,)  #这是元组
print(type(tuple1),type(tuple2))

#元组的创建
#1.利用range() 函数进行有序创建
tuple_range= tuple(range(1,100))
print(type(tuple_range))
#元组  包括 索引 切片 迭代
print(tuple_range[-1])
#像身份证号 学号 不变的内容可用 元组进行保存

