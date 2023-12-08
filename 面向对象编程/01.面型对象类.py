# 创建一个类   __id   代表私有访问变量
#self 本质是一个实例对象的标识符   可以修改  最好别修改
class Student:
    """定义一个学生类"""

    def __init__(self, name, age, id_):
        self.name = name
        self.age = age
        # print (self.name,self.age)
        self.__id = id_  #__id 为什么不能再外部进行访问，本质上时python解释器对__id 在内部重命名了

    def study(self, course):
        print("%s正在学习%s" % (self.name, course))
     # __id 只有 类内部函数才能调用

    def p_id(self):
        print(self.__id)
    #以下是私有方法 不能在类外使用
    def __Pid(self):
        print("我是私有方法！别想调用我")


# 函数入口
if __name__ == "__main__":
    xm = Student("柳梦强", 66, 691352485)
    xm.p_id()
    xm.study("坤坤篮球")
    #xm.__id  会报错

