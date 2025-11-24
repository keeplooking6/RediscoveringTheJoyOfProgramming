"""
编写装饰器
请编写一个名为 logger 的装饰器。当被装饰的函数被调用时，它应该：
在函数执行前打印：“Calling function [函数名] with arguments [参数] ...”
执行函数。
在函数执行后打印：“Function [函数名] returned [返回值]”

"""
import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling function {func.__name__} with arguments {args},{kwargs}")
        value = func(*args,**kwargs)
        print(f"Function {func.__name__} returned {value}")
        return value
    return wrapper

@logger
def add(a, b):
    return a + b

result = add(3, 5)
# print(add.__name__)