# 封装一个时钟进行封装
from time import sleep


class Clock:
    """封装函数进行封装时间函数"""

    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def run(self):
        self.__s += 1
        if self.__s == 60:
            self.__s = 0
            self.__m += 1
            if self.__m == 60:
                self.__m = 0
                self.__h += 1
                if self.__h == 24:
                    self.__h = 0

    def show(self):
        return "%d:%d:%d" % (self.__h, self.__m, self.__s)


def main():
    clock = Clock(16, 30, 50)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

# 主函数


if __name__ == '__main__':
    main()
