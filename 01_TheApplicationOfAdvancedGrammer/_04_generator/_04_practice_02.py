"""
使用生成器生成关于x的乘法表
"""

def multiplcation_generator(x):
    i = 1
    while True:
        y = i * x
        str = f"{i}*{x}={y}"
        yield str
        i = i + 1


gen = multiplcation_generator(5)
# 打印所有数据的第一种方式
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 打印所有数据的第二种方式
# for i in range(5):
#     print(next(gen))

# 打印所有数据的第三种方式
# for i in gen:
#     print(i)


"""
使用迭代器生成关于x的乘法表
"""

class multi_iterator():
    def __init__(self,x):
        self.x = x
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.y = self.i * self.x
        self.i += 1
        return f"{self.i}*{self.x}={self.y}"

ite = multi_iterator(5)
for i in range(4):
    print(next(ite))