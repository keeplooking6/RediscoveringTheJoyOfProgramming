# 使用生成器的简单例子
def generator(n):
    for i in range(n):
        print("before yield")
        yield i
        print("after yield")

# 返回一个生成器对象
gen = generator(10)
# 打印所有数据的第一种方式
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# print("-----")
# 打印所有数据的第二种方式
# for i in gen:
#     print(i)