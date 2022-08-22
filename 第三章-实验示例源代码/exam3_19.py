import numpy as np
import cv2,random

# 构建纯黑图片
matrix1= np.mat(np.zeros((300,300),dtype=np.uint8))
# 构建纯白图片
matrix2= np.mat(np.ones((300,300),dtype=np.uint8)) * 255.
# 构建杂色图片
matrix3= np.mat(np.random.randint(0,255,(300,300),dtype=np.uint8))

#显示矩阵对应图像
cv2.imshow("img1",matrix1)
cv2.waitKey(0)
cv2.imshow("img2",matrix2)
cv2.waitKey(0)
cv2.imshow("img3",matrix3)
cv2.waitKey(0)

