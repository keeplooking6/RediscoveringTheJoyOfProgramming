"""
实现一个计时的上下文管理器，用来测量with块中的内容要运行多久，并在运行完成之后打印出来
"""
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        need_time = end_time - start_time
        print(f"所需时间为{need_time}")
with timer():
    time.sleep(2)