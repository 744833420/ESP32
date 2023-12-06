#字典的创建
"""
使用{} 创建字典   {key1:value1, key2:value2}
"""

dict_test = {"key1":100,"key2":300,"key3":300}  #包含三个元素
dict_test1= {}   #空字典

#实际操作
dict_student = {"姓名:":"张来博","年龄:":22,"性别:":"男"}
print(dict_student["姓名:"])
#运用dict() 函数创建字典
dict_home = dict(姓名=1,年龄=2,性别=3)
print(dict_home)

#键不能为列表
#dict2={["name","age"]:("哒哒"，21)}  #错的
dict2={("哒哒",21):["name","age"]}
print(dict2)
#查询元素  建议使用get()方法进行访问
#创建一个类似班级学号信息表
hezhe = {
          "王海峰":1001,"张来博":1002,"柳梦强":1003,
          "张超然":1004,"岳宇航":1005,"王一然":1006
         }


print(hezhe.get("张来博","当前班级并没有发现该员工"))
print(hezhe.get("六哲","当前班级并没有发现该员工"))

for i in hezhe:
    print(i)   #遍历键值
    
for i in hezhe:
    print(hezhe[i])
for i in hezhe:
    print(i,":",hezhe[i])
    
#将按键和键值进行分开存储

list_key = []
list_val = []

for i in hezhe:
    list_key.append(i)
    list_val.append(hezhe[i])
print(list_key)
print(list_val)

#封装函数 提取键值 以及 元素

print(hezhe.keys())
print(hezhe.values())

for i in hezhe.values():
    print(i,end=" ")

print("\n----------------------------")
#字典的添加 与修改
hezhe["刘斌"]=10086
print(hezhe.get("刘斌"))

hezhe["柳梦强"]=1000000
print(hezhe.get("柳梦强"))

#字典不能直接修改   可以先删除再添加
del hezhe["刘斌"]
print("刘斌" in hezhe)
hezhe["哒哒哒"] = 100999  #添加
print("哒哒哒" in hezhe)

if "王海峰" in hezhe:
    print(hezhe["王海峰"])
if "李锦" not in hezhe:
    hezhe["李锦"] = 66666

print("---------------------------------------")

for i in hezhe:
    print(i,":",hezhe[i])
    





