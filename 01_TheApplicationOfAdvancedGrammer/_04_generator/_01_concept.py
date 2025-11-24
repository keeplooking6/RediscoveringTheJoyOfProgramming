# 带yield的函数被称为生成器
# 在for循环中会自动执行next()
# 在循环中遇到该字段时会直接返回yield后的值，在下次循环进入该函数后，直接执行yield后的代码，直到再次遇到yield
from collections.abc import Iterable


# 使用迭代查找找出最小值和最大值，并返回一个tuple
def findMinAndMax(L):
    # 检查L是否可迭代
    if isinstance(L,Iterable) == False:
        return (None,None)
    if not L:
        return (None,None)
    min,max = L[0],L[0]

    # 从第二个元素开始比较
    for x in L[1:]:
        if x<min:
            min = x
        if x>max:
            max = x
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

