#字符串查找函数
name="My name is zhanglaibo"
print(name.count("a"))
print(name.find("name"))
print(name.rindex("is"))  #带r 的时返回最后一次匹配的位置

file_name=input("请输入你的文件全名：")
if file_name.endswith(".txt"):
    print("是记事本文件")
elif file_name.endswith((".xls",".xlsx")):
    print("Excel")
elif file_name.endswith(".py"):
    print("python程序")