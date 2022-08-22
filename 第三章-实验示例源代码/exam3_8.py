import pandas as pd
data = {'Course': ['Chinese', 'Math', 'English'], 'Score':[88, 90, 82]}
dfA = pd.DataFrame(data)
print(dfA)
print('*'*16)
dfA.loc[3] = {'Course':'Physics', 'Score':72} # 为dfA新增一条数据 并初始化
print(dfA)


