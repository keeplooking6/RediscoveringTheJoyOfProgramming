# 一个函数能否被多个装饰器装饰,执行顺序是怎样的
# 从下往上装饰，从上往下执行
import functools
import time


def decorator_01(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("-----")
        value = func(*args,**kwargs)
        return value
    return wrapper

def decorator_02(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        # start_time = time.time()
        print("=======")
        value = func(*args,**kwargs)
        # end_time = time.time()
        # print("消耗时间：",end_time-start_time)
        return value
    return wrapper
@decorator_01
@decorator_02
def test():
    time.sleep(2)
    print("test")

test()
# 等价于
# test = decorator_01(decorator_02(test))
# test()