# open()函数第一个参数为文件路径，第二个参数为写入模式
# 'a+'为追加式写入，'w+'为覆盖式写入
fp = open(r'./mytest.txt','a+') 
fp.write("Hello,world")
fp.close()
