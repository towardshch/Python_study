from PIL import Image
image = Image.open('./src/lena.jpg')
image_grey = image.convert('L') # 灰度图转换
# 拼接图片 左边为原图 右边为转换后的灰度图
size = image.size
height, width = size[0], size[1]
height_, width_ = height, width * 2
target = Image.new('RGB', (width_, height_))
target.paste(image, (0, 0, width, height))
target.paste(image_grey, (width, 0, width_, height_))
# 显示图片
target.show()


