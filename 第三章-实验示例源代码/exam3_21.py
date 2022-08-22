import cv2

#读入图片和要寻找的部分
image = cv2.imread('./src/lena.jpg')
template = cv2.imread('./src/lena_mouth.jpg')
cv2.imshow("image", image)
cv2.imshow("template", template)

# 将图像和模板都转换为灰度
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# 模板匹配
result = cv2.matchTemplate(imageGray, templateGray,	cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

# 确定起点和终点的(x，y)坐标边界框
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

# 在图像上绘制边框
cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
cv2.imshow("Output", image)
cv2.waitKey(0)