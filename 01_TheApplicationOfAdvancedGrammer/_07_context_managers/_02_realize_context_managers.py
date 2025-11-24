"""
上下文管理器有类和函数两种写法
1. 实现一个文件对象或网络连接对象，本身含有其他功能，顺带实现了上下文管理器协议的，使用类
2. 如果想实现一个单纯的上下文管理器对象，用函数实现
"""
class MyOpen:
    def __init__(self,filepath):
        print("进入__init__")
        self.filepath = filepath

    def __enter__(self):
        print("进入__enter__")
        # 返回的该值会绑定 as 后的 f 变量
        return self.filepath

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入__exit__")
        if exc_type is ValueError:
            print("Caught a ValueError")
        # 如果要继续执行with中异常后的代码，而不是报错中止执行，那么返回True
        # 如果不想展示报错的红字，就返回True
        return True

with MyOpen('readme.md') as f:
    # 即使发生异常，__exit__方法仍会执行,如果希望处理异常，就在__exit__中操作
    print(f)
    raise ValueError('A ValueError Occured')

print('-----------------')

#     将上面的MyOpen类改成函数，使用yield
from contextlib import contextmanager

@contextmanager
def MyOpen(filepath):
    print("entering MyOpen")
    try:
        # yield之前作为enter方法使用，yield之后作为exit方法使用
        yield filepath
    finally:
        print('exiting MyOpen')

with MyOpen('readme.md') as f:
    print(f'value is {f}')

