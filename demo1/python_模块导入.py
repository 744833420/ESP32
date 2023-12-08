# 模块导入 用法
# def foo():
#     print("Hello")
# def foo():
#     print("Hello  python")

"""两种调用方法进行调用"""
# import fooh
# 或者
from fooh import foo as fh  # as 起别名
# 主函数  程序入口函数
if __name__ == "__main__":
    fh()  # 调用最后一个函数
