import pandas as pd
data = {'Course': ['Chinese', 'Math', 'English'], 'Score':[88, 90, 82]}
dfA = pd.DataFrame(data)
dfA.loc[3] = {'Course':'Physics', 'Score':72}   # 同上例 新增数据
print(dfA)
print('*'*16)
dfA_d1 = dfA.drop(3)                            # 删除下标索引为3的数据
print(dfA_d1)
print('*'*16)
dfA_d2 = dfA.drop('Score', axis=1)              # 删除列标题为'Score'的列
print(dfA_d2)