"""
测量代码的运行时间是否超过了阈值，计算量大的阈值高，计算量小的阈值低
这意味着：不同的函数需要的装饰器也不同，那需要定义多个装饰器吗？不需要
可以：定义一个定义装饰器的函数，即装饰器生成器：它会根据参数生成不同的装饰器

"""
# 装饰器生成器
# 为继承func的元属性，需要加@functools.wraps(func),否则打印被装饰后的函数的__name__仍然是'wrapper'

import functools
import time

def timer(threshold):
    def decorator(func):
        # 为继承func的元属性，需要加@functools.wraps(func),否则打印被装饰后的函数的__name__仍然是'wrapper'
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            start_time = time.time()
            result = func(*args,**kwargs)
            print("3333")
            end_time = time.time()
            run_time = end_time-start_time
            print(f"{func.__name__}函数运行时间为:",run_time)
            if threshold > run_time:
                print(f"没有超过时间阈值{threshold}")
            else:
                print(f"超过了时间阈值{threshold}")
            return result
        print("2222")
        return wrapper
    print("1111")
    return decorator

@timer(0.2)
def compute_time():
    time.sleep(0.4)
compute_time()

# 去掉注解时，形式为：
# timer是返回装饰器的函数，compute_time是返回装饰器的函数的参数
# compute_time_decorator = timer(0.2)(compute_time)
# compute_time_decorator()

print(compute_time.__name__)
