a=3
b=a
print('a.id=', id(a)) # 使用id函数查看变量的内存地址
print('b.id=', id(b))
print('a=',a)
print('b=',b)
a=4
print('a.id=', id(a)) # 改变a引用对象后变量引用地址发生改变
print('b.id=', id(b)) # b的引用地址没有改变
print('a=',a)
print('b=',b)