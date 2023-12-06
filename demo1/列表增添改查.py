#列表的使用
list1=["水星","金星","火星","木星"]
print(list1)
list1.insert(2,"地球")
print(list1)

list1.append("土星") #元素追加
list1.extend(["天王星","海王星"]) #追加 串
print(list1)

list1.remove("金星") #按照名字进行  删除元素
print(list1)

list1.pop(-1)  #从最后进行  删除   不添加 -1  默认从最后进行删除元素
print(list1)

print("水星" in list1)  #判断该元素 是否在列表中
