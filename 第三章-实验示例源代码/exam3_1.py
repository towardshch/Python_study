import random
random.seed(0) # 设置随机种子
names = ['甲111', '乙222', '丙333', '丁444', '戊555', '己666', '庚777', '辛888'] # 姓名
for i in range(5): # 进行五次随机的点名
    index = random.randint(0, 7)
    print(names[index])


