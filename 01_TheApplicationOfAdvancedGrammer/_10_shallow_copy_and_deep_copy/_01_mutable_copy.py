"""
可变对象: 可变对象内的元素被修改、删除后仍然是原来的对象，如：字典，集合，列表

深拷贝，浅拷贝，赋值的区别

"""
import copy

a = [1,[1,2,3]]
b = a
c = a.copy()
d = copy.deepcopy(a)
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")
a[0] = 11
print("---修改a[0]后---")
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")
print("---修改a[1][1]后---")
a[1][1] = 22
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")
