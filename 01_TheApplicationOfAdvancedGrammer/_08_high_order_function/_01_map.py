"""
def func(x):
    pass
Iterator = map(func,Iterable)
map函数会把Iterable中的每个元素都用func函数处理一遍，之后会返回一个迭代器，因为迭代器是惰性计算，所以转换为list类型会一次性计算出所有数据
另外：map中的func函数只接收一个参数
"""

def square_num(x):
    return x * x

need_data = map(square_num,[1,2,3,4])
# 一：
# print(next(need_data))
# print(next(need_data))
# print(next(need_data))
# print(next(need_data))
# print(next(need_data))
# 二：
for i in need_data:
    print(i)
# 三：
# print(list(need_data))

