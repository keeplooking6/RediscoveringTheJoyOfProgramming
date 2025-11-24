"""
查看程序运算所需时间
"""
# 设计的装饰器函数，要返回装饰后的函数（即wrapper）

# *args,**kwargs:
# 即wrapper作为要代替func的新函数，那么func的参数，wrapper也得保持一致
# 且，wrapper也不是只为一个函数服务的
# 所以需要有：wrapper(*args,**kwargs)

import time

def decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        print('2222')
        end_time = time.time()
        print(f"{func.__name__}所需时间:",end_time-start_time)
        return result
    print('1111')

    return wrapper

# @decorator
def compute_time():
    time.sleep(0.3)
# compute_time()

# 去掉注解时，形式为：
compute_time_decorator = decorator(compute_time)
compute_time_decorator()

