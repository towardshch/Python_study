import time
print(time.time())
print(time.localtime(time.time()))
# 续行符号应用
print(time.strftime(\
		'%Y年%m月%d日%H时%M分%S秒',\
		time.localtime(time.time())))
# 分隔符号应用
a=3;b=6;c=9;print('和值:',a+b+c);print('均值:',(a+b+c)/3)

