# 多态的使用
class Pet(object):
    def __init__(self, name, age):
        self.name = name

    def make_voice(self):
        pass  # 空语句

# 子类


class Dog(Pet):
    # def __init__(self, name, age):      #其实这是对父类的重构
    #     super().__init__(name, age)

    def make_voice(self):
        print("%s:我在狗叫" % (self.name))


class Cat(Pet):

    def make_voice(self):
        print("%s:我在猫叫" % (self.name))


if __name__ == "__main__":
    wd = Dog("旺财", 16)
    wd.make_voice()
    wc = Cat("猫咪", 88)
    wc.make_voice()
