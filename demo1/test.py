# #分支语句  if
# """
#   单分支语句使用示例·判断一个年份是不是闰年，如果
# 是则输出“是闰年”，否则不输出·能被4整除且不能被
# 100整除的年份，或者能被400整除
# """
# year=eval(input("请输入你要判断的年："))
# 
# if((year%4==0)and(year%100!=0)or(year%100==0)):
#     print(str(year)+"年是闰年")
# else:
#     print(str(year)+"年是平年")

num = eval(input("请输入一个数："))
if num>0:
    print(num,"是一个正数")
elif num==0:
    print(num,"是0，既不是正数也不是负数")
else:
    print(num,"是负数")

    