import numpy as np
a = np.array([1, 2, 3])     #创建一个1x3的array
b = np.linspace(1, 10, 4)   #创建一个1到10 共4个数的等差数列
c = np.random.rand(3, 4)    #创建一个大小为3x4的随机矩阵

print("a:", a)
print("b:", b)
print("c:\n", c)

print("*"*50)

d = np.array([[1, 2, 3], [4, 5, 6]]) # 创建一个内容为1到6的大小为2x3的二维矩阵

d_f = d.flatten() # 将矩阵d拉成一维

d1 = np.array([[1, 2, 3], [4, 5, 6]])       # 创建加法矩阵1
d2 = np.array([[10, 20, 30], [40, 50, 60]]) # 创建加法矩阵2
d_s = np.add(d1, d2) # 进行两个矩阵对应元素的加法

print("d:\n", d)
print("d_f:", d_f)
print("d_s:\n", d_s)
