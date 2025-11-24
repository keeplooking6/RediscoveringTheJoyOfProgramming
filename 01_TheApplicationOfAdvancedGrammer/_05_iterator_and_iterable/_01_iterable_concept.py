# 可迭代对象：列表，元组，集合，字典，字符串，实现了__iter__()或__getItem__()方法的对象【可迭代对象也叫可直接作用于for循环的对象】
my_list = [1,2,3]
my_string = "hello"
my_dict = {"name": "aa"}
print("可迭代对象--------------")
for item in my_list: #不保持迭代状态，存储所有数据，可重复迭代
    print(item)

# 迭代器：含有__iter__()和__next__()方法的对象【迭代器：可以被next()调用并返回下一个值的对象】
# 常见于 生成器，文件对象，通过iter()转换的对象
my_list = [1,2,4]
my_iterator = iter(my_list)
print("迭代器--------------")
print(next(my_iterator)) # 保持迭代状态，逐个生成元素，不可重复迭代
print(next(my_iterator))
print(next(my_iterator))




