"""
切割方式：
1. 按页切割
    - pages = loader.load_and_split()
2. 按语义段落切割
    - 将文档切分为 chunk_size 个字符的块，每个字符块之间会有chunk_overlap个字符重复，降低了分离了重要的上下文的可能性
    - text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200, chunk_overlap=50, add_start_index=True
        )
"""

# 1. 导入所需的特定组件 - 就像当初从flask import Flask一样
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 2. 指定你的PDF文件路径 (放一个你有的PDF到同一目录，比如'resume.pdf')
loader = PyPDFLoader('test.pdf')

# 3. 执行加载和按页切割 - 这是最关键的一步，但它被封装成了一行代码
pages = loader.load_and_split()

print("-----------------页面分割---------------------")


# 4. 查看结果
print(f"总页数: {len(pages)}")
print("第一页内容预览：")
print(pages[0].page_content[:500]) # 打印前500个字符
print("------------------段落分割---------------------")

text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
        )

docs = text_splitter.split_documents(pages)
print(f"分割后的文档块数量{len(docs)}")
print("第一个块的内容预览")
print(docs[0].page_content)
