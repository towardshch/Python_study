import pandas as pd
import numpy as np
data = {'Course': ['Chinese', 'Math', 'English'], 'Score':[88, 90, 82]}
dfA = pd.DataFrame(data)

dfA['grade'] = ['B', 'A', 'B'] # 为dfA添加一列'grade'列 且初始化内容为['B', 'A', 'B']
print(dfA)


