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
        func = args[0] # 即被装饰函数
        # 这里是有装饰器参数的情况下，使用第一个参数作为消息
        message = args[0] if args else None
        message2 = kwargs if kwargs else None

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
    else:
        # 否则是 @log('execute') 形式
        def decorator(func, *args, **kwargs):

            message = args[0] if args else None
            message2 = kwargs if kwargs else None

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
        return decorator

# def decorator(func, *decorator_args, **decorator_kwargs):
#     # 这里是有装饰器参数的情况下，使用第一个参数作为消息
#     message = decorator_args[0] if decorator_args else None
#     message2 = decorator_kwargs if decorator_kwargs else None
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # 如果有自定义消息，使用它；否则使用函数名
#         if message:
#             print(f"{message},-{message2}")
#         else:
#             print(f"Calling function: {func.__name__}")
#
#         # 调用原函数
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper


# 测试两种使用方式
if __name__ == "__main__":
    # 使用方式1: @log
    # @log
    # def f():
    #     print("Function f executed")


    # 使用方式2: @log('execute')
    # @log('execute------',a='b')
    # def g():
    #     print("Function g executed")

    # 使用方式2: @log('execute')
    @log('execute------',"ddddd")
    def g():
        print("Function g executed")

    # g = log('execute------',"ddddd")(g)
    # g()

    # 测试函数调用
    # f()
    # 输出:
    # Calling function: f
    # Function f executed

    g()
    # 输出:
    # execute
    # Function g executed