#创建基类
class Person():
    def __init__(self, name,age):
        self._name =name
        self._age =age
    def name(self):
        return self._name
    def age(self):
        return self._age
    #修改姓名  修改名字
    def x_name(self,name):
        self._name = name
    def watch_tv(self):
        print("%s 正在看电视！！！" %(self._name))
#创建子类  学生类
class Student(Person):
    def __init__(self,name,age,ID):
        #调用父类的初始化函数
        super().__init__(name,age)
        self.__ID=ID
    def ID(self):
        return self.__ID
    def study(self):
        print("%s 正在学习"%(self._name))  #调用父类的方法

if __name__ == "__main__":
    stu= Student("柳梦强",19,10086)
    print(stu.name())
    print(stu.age())
    print(stu.ID())
    stu.study()