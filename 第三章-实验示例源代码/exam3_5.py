import pandas as pd
import numpy as np
data = {'Course': ['Chinese', 'Math', 'English'], 'Score':[88, 90, 82]} # 创建课程内容字典
dfA = pd.DataFrame(data)        # 将字典转换为dataframe
print("DataFrame:\n", dfA)      # 输出整个课程dataframe
print("index:", dfA.index)      # 输出dataframe的索引范围
print("columns:", dfA.columns)  # 输出dataframe的列标题
print("values:\n", dfA.values)  # 以数值方式输出dataframe的所有内容