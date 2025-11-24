# lambda 表达式：即匿名函数，只使用一次的函数，不用专门定义一个函数
# 格式是 lambda <参数>: 表达式
# 匿名函数可以赋值给变量，然后使用变量调用该函数

# def square(x):
#     return x * x
# 等价于
# square = lambda x: x * x
# print(square(3))

# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
# print(L)
# 等价于
# L = list(filter((lambda n: n%2==1),range(1,20)))
# print(L)
