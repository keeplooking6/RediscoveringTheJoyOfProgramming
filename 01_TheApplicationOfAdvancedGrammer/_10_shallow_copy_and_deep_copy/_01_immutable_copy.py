"""
不可变对象: 不可变对象内的元素被修改、删除后是新的对象，如：字符串，元组，数字

深拷贝，浅拷贝，赋值的区别

"""
import copy

a = 1
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")
a = 11
print("---修改a后---")
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")


import copy
a = "我是谁"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")

a = "---"
print("---修改a后---")
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")

