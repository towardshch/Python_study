import cv2
# 打开图片
image = cv2.imread('./src/lena.jpg')
# 显示图片
cv2.imshow("lena", image)
cv2.waitKey(0) # 等待任意键盘操作关闭图像
# 保存图片
cv2.imwrite('./src/lena2.jpg', image)


