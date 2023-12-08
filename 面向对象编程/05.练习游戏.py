"""王者荣耀"""


class Hero(object):
    def __init__(self, name, BloodVolume):
        self.__name = name
        self.__bloodVolume = BloodVolume
        self.__atk = 10  # 初始攻击力为10

    def atk(self):  # 获取攻击力
        return self.__atk

    def add_atk(self, num):  # 升级以后进行增加攻击伤害
        self.__atk += num

    def sub_blood_volume(self, val):  # 受到伤害后血量减少
        self.__bloodVolume -= val
    # 判断是否死亡

    def is_die(self):
        print("%s的血量为%s" % (self.__name, self.__bloodVolume))
        if self.__bloodVolume <= 0:
            return True
        else:
            return False


if __name__ == "__main__":
    cyj = Hero("程咬金", 100)  # 血厚
    lbqh = Hero("鲁班七号", 60)  # 攻击力高
    # 正式对战
    # 第一局
    val = cyj.atk()
    lbqh.sub_blood_volume(val)
    val = lbqh.atk()
    cyj.sub_blood_volume(val)

    res = lbqh.is_die()
    if res:
        print("游戏结束，程咬金获胜")

    lbqh.add_atk(90)  # 鲁班七号增加60攻击力
    val = lbqh.atk()
    cyj.sub_blood_volume(val)
    res = cyj.is_die()
    if res:
        print("游戏结束，鲁班七号获胜")
