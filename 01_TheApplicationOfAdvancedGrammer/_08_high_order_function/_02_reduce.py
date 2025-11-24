"""
def func(x,y):
    pass
reduce(func,sequence) ：将func函数作用于sequence序列，通过将得到的结果继续作用于下一个元素累积计算
- 序列（sequence）：存储了一组有序的元素，字符串，列表，元组
"""
from functools import reduce

# 序列中元素加和
def add_num(x,y):
    return x + y
num_sum = reduce(add_num,[1,2,3,4])
print(num_sum)


# 将序列中元素变为由其组成的整数
def combine(x,y):
    return x * 10 + y
combine_num = reduce(combine,[1,3,5,2])
print(combine_num)

