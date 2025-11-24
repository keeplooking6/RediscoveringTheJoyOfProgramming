"""
设计一个 设置临时环境变量的上下文管理器
在with中临时修改环境变量，退出with后的环境变量会恢复为原来的值
"""
import os
from contextlib import contextmanager

from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

@contextmanager
def set_temporary_env(**kwargs):
    backup = os.environ.get('TEST_VAR')
    value = kwargs.get('TEST_VAR')
    os.environ['TEST_VAR'] = value
    try:
        yield
    finally:
        os.environ['TEST_VAR'] = backup


print(os.environ.get('TEST_VAR'))
with set_temporary_env(TEST_VAR='abaaa'):
    print(os.environ.get('TEST_VAR'))
print(os.environ.get('TEST_VAR'))
