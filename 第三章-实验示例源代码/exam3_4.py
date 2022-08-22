import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30, 40], index=list('abcd')) # 创建Series对象
print(s[2])                 #通过下标索引查询
print(s['b'])               #通过标签索引查询
print(s[[0, 2, 3]])         #通过下标索引查询多个元素
print(s[['a', 'b', 'c']])   #通过标签索引查询多个元素
print(s[1:3])               #通过下标索引将对象切片
print(s['b':'d'])           #通过标签索引将对象切片
print(s[s>20])              #通过条件索引查询