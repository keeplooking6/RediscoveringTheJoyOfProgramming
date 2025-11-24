#### 1. map函数

```
Iterator = map(func(),Iterable)
```

map函数会把Iterable中的每个元素都用func函数处理一遍，之后会返回一个迭代器，因为迭代器是惰性计算，所以转换为list类型会一次性计算出所有数据

###### 