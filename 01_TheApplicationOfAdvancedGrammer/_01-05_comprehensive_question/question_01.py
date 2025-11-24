"""
分析以下代码，并写出确切的输出结果。请一步步解释程序的执行流程，特别是装饰器和生成器的部分。
"""

def decorator(func):
    print(f"Decorating {func.__name__}")
    def wrapper(*args, **kwargs):
        print(f"Wrapper is called for {func.__name__}")
        # 该func是生成器，调用时不执行，迭代时才执行
        result = func(*args, **kwargs)
        print(f"Wrapper is finishing for {func.__name__}")
        return result
    return wrapper

@decorator
def my_generator(n):
    for i in range(n):
        print(f"Yielding {i}")
        yield i * 2
# my_generator = decorator(my_generator)
# gen = my_generator(3)
gen = my_generator(3)
print("Generator created")
for value in gen:
    print(f"Got value: {value}")

"""
我的答案：
Decorating my_generator
Wrapper is called for my_generator
Wrapper is finishing for my_generator
Generator created
Yielding 0
Got value: 0
Yielding 1
Got value: 2
Yielding 2
Got value: 4
"""