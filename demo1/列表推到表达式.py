#列表推导式

bill = [112,155,55,46,1,32,44,655,1854,1313,77]

bill_100=[x for x in bill if x > 100]   #x是要存的元素
#含义如下
bill_200=[]
for i in bill:
    if i>100:
        bill_200.append(i)
print(bill_200)

print(bill_100)