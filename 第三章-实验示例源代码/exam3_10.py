import pandas as pd
# 读src文件夹中的score.xlsx的class1表
data = pd.DataFrame(pd.read_excel('./src/score.xlsx', 'class1'))
print(data)
# 将之前读入的表写入src文件夹中的score2.xlxs文件的class1_表
data.to_excel('./src/score2.xlsx', sheet_name='class1_')