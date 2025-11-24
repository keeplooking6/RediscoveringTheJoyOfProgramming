"""
不可变对象包含可变对象

深拷贝，浅拷贝，赋值的区别

"""
import copy

a = (1,[1,2,3])
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")
a[1][2] = 2
print("---修改a[1][2]后---")
print(f"a:{a},a的地址:{id(a)}")
print(f"b:{b},b的地址:{id(b)}")
print(f"c:{c},c的地址:{id(c)}")
print(f"d:{d},d的地址:{id(d)}")