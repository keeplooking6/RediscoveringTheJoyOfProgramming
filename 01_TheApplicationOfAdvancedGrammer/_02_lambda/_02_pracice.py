"""
有一个列表 data = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]。
a. 使用 sorted 函数和 lambda 表达式，根据年龄（元组的第二个元素）对这个列表进行升序排序。
b. 使用 sorted 函数和 lambda 表达式，根据姓名长度（元组的第一个元素的长度）对这个列表进行降序排序。
"""
data = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]
# a.
ascending_sort = sorted(data,key=lambda x:x[1])
print(ascending_sort)
# 注：sorted函数会遍历可迭代对象，并将key规则应用于每个迭代出来的元素
# lambda x:x[1]等价于
# def some_func(x):
#     return x[1]

# b.
descending_name_length = sorted(data,key=lambda x:len(x[0]),reverse=True)
print(descending_name_length)