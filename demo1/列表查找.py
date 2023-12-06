#列表查找
test_list=["狗","猫","狗","狗","猫"]

#print(test_list.count("狗"))  #返回狗的位置
print(test_list.index("狗",2,5))
print(test_list.count("狗"))

test_list.sort()
print(test_list)


test_list_int=[2,5,8,9,4,5,6,12,2,8,9,10]

test_list_int.sort()  #排序   默认从小到大排序

print(test_list_int)


#加上  reverse = True 就变成了  逆向排序

test_list_int.sort(reverse = True)

print(test_list_int)