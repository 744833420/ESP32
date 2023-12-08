"""
闰年判断·自定义函数(is leap_year),实现判断一个年份是否为闰年,
如果一个年份是4的倍数但不是100的倍数，或者是400的倍数，那么它就
是闰年·调用该函数打印1949年-2024年之间的所有闰年
"""
def is_leap_year(year):
    if  ( year%4==0  and year %100 !=0 )or year % 400 == 0:
        return True
    else:
        return False

print("是闰年" if is_leap_year(100) else "平年" )  #三目运算符

# sum1 = 0
# pingnian_sum =0
# for i in range(1949,2025):
#     #print((i,"年是闰年") if is_leap_year(i) else (i,"年平年") )
#     if is_leap_year(i)==True:
#         sum1 += 1
#     else:
#         pingnian_sum += 1
# print("1949年-2024年闰年一共有{}个\n平年一共有{}个".format(sum1,pingnian_sum))  #一定是.函数


temp_list=[]

for i in range(1949,2025):
    if is_leap_year(i)==True:
        temp_list.append(i)
print(temp_list,len(temp_list))


