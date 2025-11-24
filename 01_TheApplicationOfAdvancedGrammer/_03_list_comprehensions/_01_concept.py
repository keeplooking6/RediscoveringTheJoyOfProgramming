# 生成含有1-10元素的列表
list1 = [x for x in range(1,11)]
print("list1:",list1)

# 生成[1x1, 2x2, 3x3, ..., 10x10]的列表
list2 = [x * x for x in range(1,11)]
print("list2:",list2)

# 在list2表达式的基础上筛选出仅偶数的平方【if的用法】
list3 = [x * x for x in range(1,11) if x%2==0]
print("list3:",list3)

# 使用两层循环，可以生成全排列
list4 = [m + n for m in ['J','Q','K'] for n in ['1','2','3']]
print("list4:",list4)

# 【if-else的用法】
list5 = [x if x%2 == 0 else -x for x in range(1,11)]
print("list5:",list5)

# for循环后的if是筛选条件，for循环前的是表达式

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [L1_element.lower() for L1_element in L1 if isinstance(L1_element,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')