test={}
print(test) # 创建空字典
test_1={'a':1,'b':2,'c':3} # 直接创建
print(test_1)
test_2=dict(a=1,b=2,c=3) # 使用字典类的构造函数dict函数创建字典
print(test_2)
test_3=dict((('a',1),('b',2))) # 传入可迭代对象创建字典
print(test_3)
test_4=dict(zip(['a','b'],[1,2])) # 传入映射函数创建字典

