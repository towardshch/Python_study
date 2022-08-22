import pandas as pd
import numpy as np

num = range(1,7)
#随机生成6行4列60-100间的整数作为二维数据源
dfB = pd.DataFrame(np.random.randint(60, 100,size=(6,4)), index=num, columns=['A','B','C','D'])
print(dfB)