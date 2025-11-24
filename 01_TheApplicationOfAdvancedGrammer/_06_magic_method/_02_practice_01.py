"""
通过将ShoppingCart类里的东西相加，直接打印ShoppingCart类的实例，可以让类的实例像函数一样调用 等方法 来理解类里的魔法方法用途
"""
class ShoppingCart:
    def __init__(self,items):
        self.items = items

    # 自定义两个购物车物品相加的方法
    # items是列表，可以使用‘+’
    def __add__(self,another_cart):
        new_cart = ShoppingCart(self.items+another_cart.items)
        return new_cart

    # 定义类的实例对象的打印结果,即返回对象的描述性信息
    # __str__ 返回结果的类型必须是string
    def __str__(self):
        return f'{self.items}'

    # 定义类的实例的len方法
    def __len__(self):
        return len(self.items)

    # 可以让类的实例像函数一样调用，即直接向实例传参
    def __call__(self, item):
        self.items.append(item)
        return self.items


cart1 = ShoppingCart(['orange','purple'])
cart2 = ShoppingCart(['banana','apple'])
new_cart = cart1 + cart2
# 在未定义__str__魔法方法时，打印两个实例的相加结果，要加.items
print(new_cart.items)
# 在定义了__str__魔法方法时，用以下方法打印两个实例的相加结果
print(new_cart)

# 在未定义类的__len__方法时,会报错该类没有len方法
print(len(new_cart))

new_cart('pear') # 打印结果是__call__方法的返回值
print(len(new_cart))
print(new_cart('peach'))
