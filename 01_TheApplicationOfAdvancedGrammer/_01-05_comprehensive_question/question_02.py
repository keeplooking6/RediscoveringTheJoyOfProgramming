"""
需要处理一个非常大的日志文件 huge_log.txt
使用生成器来高效地（指内存使用方面）查找所有包含 "ERROR" 关键词的日志行
并与一次性将整个文件读入内存的列表方法进行对比
"""

# 读取huge_log.txt文件（高效做法）
def read_file():
    with open("huge_log.txt",'r') as f:
        for f_content in f:
            if "ERROR" in f_content:
                yield f_content.strip()

# 使用生成器查找包含 "ERROR" 关键词的日志行
gen = read_file()
for g in gen:
    print(g)

# 列表生成式（低效做法）
with open("huge_log.txt",'r') as f:
    all_lines = f.readlines()
result = [error_lines.strip('\n') for error_lines in all_lines if 'ERROR' in error_lines]
print(result)

