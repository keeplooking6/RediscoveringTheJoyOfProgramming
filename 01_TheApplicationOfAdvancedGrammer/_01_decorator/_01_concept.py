# 目的：不改变原有函数代码的情况下，添加新的功能
# 常用于权限检查,一个函数的运行时间
# 内在知识点：将函数作为参数传入函数
# 将wrapper代替原来的func函数，即wrapper为装饰后的函数

# 形式：
# 在“我是xxx”前后加上对话
def decorator_01_(func):
    def wrapper():
        print("你的名字是？")
        func()
        print("好的")
    return wrapper

def answer():
    print("我是xxx")

answer = decorator_01_(answer)
# 在这里，answer()相当于decorator_01_返回出来的wrapper方法
answer()

# 使用语法糖之后
@decorator_01_
def answer():
    print("我是xxx")

answer()

