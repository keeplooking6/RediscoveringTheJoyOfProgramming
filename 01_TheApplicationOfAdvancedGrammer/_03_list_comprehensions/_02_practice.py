"""
有一个列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]。请用一行列表生成式完成以下任务：
a. 生成一个新列表，只包含 numbers 中所有的偶数。
b. 生成一个新列表，其中的元素是 numbers 中每个元素的平方。
c. 生成一个新列表，其中的元素是 numbers 中所有大于5的奇数的平方。
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a.
even_number = [i for i in numbers if i%2 == 0]
print(even_number)

# b.
square_number = [i**2 for i in numbers]
print(square_number)

# c.
greater_than_five_odds_square_number = [i**2 for i in numbers if (i>5 and i%2==1) ]
print(greater_than_five_odds_square_number)

# d.将第c问的列表生成式改为生成器表达式
greater_than_five_odds_square_number_generator = (i**2 for i in numbers if (i>5 and i%2==1))
for i in greater_than_five_odds_square_number_generator:
    print(i)

# 两者内存上的差别：列表生成式会立即在内存中创建整个列表，而生成器表达式不会立即执行，只有在迭代时逐个生成元素，内存中只含有一个数据，
# 极大的节约了内存，尤其适用于处理大规模数据流