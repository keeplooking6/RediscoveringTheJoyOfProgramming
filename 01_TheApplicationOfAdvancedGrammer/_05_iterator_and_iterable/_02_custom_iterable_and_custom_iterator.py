# 自定义可迭代对象（返回一个迭代器）
class MyIterable:
    def __init__(self,data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)

# 迭代器（返回自身）
class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iterable = MyIterable({"name":"ww","age": 18})
for key,value in my_iterable:
    print(key,value)
# my_iterable = MyIterable([1,2,3])
# for item in my_iterable:
#     print(item)
