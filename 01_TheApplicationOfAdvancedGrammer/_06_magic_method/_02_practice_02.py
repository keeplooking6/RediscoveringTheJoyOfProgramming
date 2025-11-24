"""
定义一个add类，使用数字构造，构造后的值就是传入的数字，同时该实例也可以进行加法，也可以使用调用或多次调用（得到的结果也是数字相加的结果），
"""
import functools


def current_method(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"进入了{func.__name__} method")
        value = func(*args,**kwargs)
        return value
    return wrapper


class add:
    @current_method
    def __init__(self,num):
        self.num = num

    @current_method
    def __str__(self):
        return f'{self.num}'

    @current_method
    def __add__(self, other_num):
        return self.num + other_num

    @current_method
    def __call__(self,other_num):
        # 直接返回数字是错误的，因为数字是不可调用对象
        # return self.num + other_num

        new_num = self.num + other_num
        return add(new_num)

addTwo = add(2)
print(addTwo)

print(addTwo + 5)

print(addTwo(3))

print(addTwo(3)(5))

print(add(1)(2)(3)(4))