import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# 取横坐标为0.0到2.0间隔为0.01的数据
t = np.arange(0.0, 2.0, 0.01)
# 要展示的函数为 s=1+sin(2Πt)
s = 1 + np.sin(2 * np.pi * t)

# 根据t和s的定义 绘图
fig, ax = plt.subplots()
ax.plot(t, s)

# 设置各布局的命名
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid() # 绘制方格

plt.show()