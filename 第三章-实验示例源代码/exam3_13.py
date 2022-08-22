from PIL import Image
image = Image.open('./src/lena.jpg')
box = (100, 100, 300, 300) # 从(100, 100)开始的 大小为(300, 300)的框
size = (150, 150) # 目标大小为(150, 150)
region = image.crop(box) # 图片中裁出box大小的部分
region_rotate = region.transpose(Image.ROTATE_180) # 旋转180度 等同于.rotate(180)
image.paste(region_rotate, box) # 将指定区域改变后的图像粘贴回去
image.resize(size) # 改变最后的图片大小
image.show()