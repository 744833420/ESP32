#def  函数和模板
def my_print(str1):
    """
    函数说明：  自己定义的print()函数
    参数：一个字符串
    返回值：None
    """
    print(str1)
#进行调用
my_print("今天天气怎么样，有点小冷")

def my_sum(list1):
    """
    列表数据求和
    参数：一个存储了数字的列表
    """
    sum1 = 0
    if len(list1) == 0:
        return False,sum1
    for i in list1:
        sum1+=i
    return True,sum1

list2 = [1,5,8,4,11,266,4,0]
print(my_sum(list2))


res,sum2=my_sum(list2)
print(res,sum2)

#如果不想接受 某一个返回值  用_ 来接受


_,sum3 = my_sum(list2)
print("_",_)
#练习   优惠满减政策
"""
假设电商平台正在举行优惠购活动，当购物消费达到一定金额就可以享受满减优惠，
如下所示：
·购物金额满100元立减5元
·购物金额满300元立减20元
·购物金额满500元立减40元
·购物金额满1000元立减90元
"""
a = eval(input("请输入你购物金额:"))

def Discounts(a):
    """超市优惠函数 a代表顾客总消费数"""
    if a>=100 and a<300:
        print("你好，我们优惠5元，你应该支付{}元".format(a-5))
    elif a>=300 and a<500:
        print("你好，我们优惠20元，你应该支付{}元".format(a-20))
    elif a>=500 and a<1000:
        print("你好，我们优惠40元，你应该支付{}元".format(a-40))
    elif a>=1000:
        print("你好，我们优惠90元，你应该支付{}元".format(a-90))

Discounts(a) 