"""
将str类型的序列转换为int类型
"""
from functools import reduce

def convert(x):
    digits = {'0':0, '1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[x]

def combine(x,y):
    return x * 10 + y

# num = map(convert,'13672')
# for i in num:
#     print(i)
result = reduce(combine,map(convert,'13672'))
print(result)
print(type(result))