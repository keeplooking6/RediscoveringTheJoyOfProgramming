'''
思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass

又支持：

@log('execute')
def f():
    pass
'''

# @log：直接装饰函数，参数是函数本身
# @log('message')：先调用装饰器工厂，返回一个装饰器

from functools import wraps

def log(*args, **kwargs):
    # 如果第一个参数是可调用的(函数，类等），说明是 @log 形式（即f = log(f)）
    # args[0]是为了检查log的第一个参数是不是函数，类
    if len(args) == 1 and callable(args[0]):
        func = args[0]
        return decorator(func)
    else:
        # 否则是 @log('execute') 形式
        # 这里使用lambda函数是因为，要返回的是个函数，而不是立即执行装饰逻辑
        # func在装饰器定义时还不存在，需要在应用装饰器时传入
        return lambda func: decorator(func, *args, **kwargs)
        # 等价于
        #     def decorator_maker(func):
        #         return decorator(func,*args,**kwargs)
        #     return decorator_maker


def decorator(func, *decorator_args, **decorator_kwargs):
    # 这里是有装饰器参数的情况下，使用第一个参数作为消息
    message = decorator_args[0] if decorator_args else None
    message2 = decorator_kwargs if decorator_kwargs else None

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 如果有自定义消息，使用它；否则使用函数名
        if message:
            print(f"{message},-{message2}")
        else:
            print(f"Calling function: {func.__name__}")

        # 调用原函数
        result = func(*args, **kwargs)
        return result

    return wrapper


# 测试两种使用方式
if __name__ == "__main__":
    # 使用方式1: @log
    @log
    def f():
        print("Function f executed")


    # 使用方式2: @log('execute')
    # @log('execute------',a='b')
    # def g():
    #     print("Function g executed")

    # 使用方式2: @log('execute')
    @log('execute------',"ddddd")
    def g():
        print("Function g executed")

    # 测试函数调用
    f()
    # 输出:
    # Calling function: f
    # Function f executed

    g()
    # 输出:
    # execute
    # Function g executed