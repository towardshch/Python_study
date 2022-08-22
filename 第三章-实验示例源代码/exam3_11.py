from PIL import Image
# 打开src文件夹下的图片lena.jpg
image = Image.open('./src/lena.jpg')
image.show() # 只有关闭图片后才能进行下一步的保存
# 重新将lena.jpg存入src文件夹中 并命名为lena_copy.jpg
image.save('./src/lena_copy.jpg')

