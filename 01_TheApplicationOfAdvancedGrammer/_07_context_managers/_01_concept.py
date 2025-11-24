"""
记录由原始的open方法-》with open() as f:
"""

# 原始
f = open('readme.md','r',encoding='utf-8')
try:
    print(f.read())
finally:
    f.close()

print("------------")
# 改进
with open('readme.md','r',encoding='utf-8') as f:
    print(f.read())
