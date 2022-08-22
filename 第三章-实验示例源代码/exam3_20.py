import cv2

# 读取原图像
img = cv2.imread('./src/lena.jpg', 0)

# 显示原图像
cv2.imshow('img', img)

# 高斯模糊
img_rgb = cv2.GaussianBlur(img, (5, 5), 0)
canny_img = cv2.Canny(img_rgb, 1, 10)

# 显示边缘检测图像
cv2.imshow('canny', canny_img)

cv2.waitKey(0)