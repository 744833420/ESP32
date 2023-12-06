#列表   索引以及切片均可使用   使用 [] 创建列表
#修改列表的内容     先定位  然后覆盖   增删查改
#创建列表
my_list=[]

my_new_list=["张三",18,10010,1.9,True]

print(my_new_list)

r_list=list(range(1,9))

print(r_list)

my_list.append(1)
print(my_list)
my_list.insert(0,"zlb")
print(my_list)
my_list.extend("sascascascasc")  #类似合并
print(my_list)


#元素删除
my_list.pop(1) #指的1位置的元素  
print(my_list)

my_list.remove("s")#删除c元素  第一个位置
print(my_list)

my_list.clear()
print(my_list)
