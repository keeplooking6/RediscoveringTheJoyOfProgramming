"""
需要处理一个非常大的日志文件 huge_log.txt
使用生成器来高效地（指内存使用方面）查找所有包含 "ERROR" 关键词的日志行
并与一次性将整个文件读入内存的列表方法进行对比
"""
import time


# from .._01_decorator._02_standard_writing_style import decorator
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
# 读取huge_log.txt文件（高效做法）
def read_file():
    with open("huge_log.txt",'r') as f:
        for f_content in f:
            if "ERROR" in f_content:
                yield f_content.strip()

# 使用生成器查找包含 "ERROR" 关键词的日志行
@decorator
def use_generator():
    gen = read_file()
    for g in gen:
        print(g)

# 列表生成式（低效做法）
@decorator
def use_list_comprehensions():
    with open("huge_log.txt",'r') as f:
        all_lines = f.readlines()
    result = [error_lines.strip('\n') for error_lines in all_lines if 'ERROR' in error_lines]
    print(result)

#  数据量太少，看不出差别
use_generator()
print('==========')
use_list_comprehensions()