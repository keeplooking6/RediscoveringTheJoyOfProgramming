# 斐波那契数列的优化过程
# 斐波那契数列：1，1，2，3，5，8，13...

# 1、初级写法
def fab1(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
print("fab1----------------------")
fab1(5)

# 2.直接使用打印输出斐波那契数列的方式，复用性较差，因为fab函数返回的是None，其他函数无法使用该数列
# 为提高复用性，将数列放入list中
def fab2(max):
    n,a,b = 0,0,1
    fab_list = []
    while n<max:
        fab_list.append(b)
        a,b = b,a+b
        n = n + 1
    return fab_list
print("fab2----------------------")
print(fab2(5))

# 3.该函数在运行过程中的内存占用会随着max的增大而增大，如果要控制内存占用，最好不要使用list保存中间结果
# 而是通过Iterable对象来迭代


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(f"第{n+1}次循环 ")
#         print("当前n的值",n)
#         print("当前返回值b",b)
#         yield b
#         print("再次开始")
#         a, b = b, a + b
#         n = n + 1
#
# for n in fab(5):
#     print(n)