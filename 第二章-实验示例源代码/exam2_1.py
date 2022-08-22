import random # 导入random库
'''
猜数游戏程序
游戏虽然好玩，切记不要上瘾
适度游戏益脑，沉迷游戏伤身
合理安排时间，注意自我保护
'''
i = int(input('请输入两位整数:'))
j = random.randint(10, 99) # 在[10, 99]之间生成随机整数
k = 1
while i != j:
    if i < j:
        print('你输入的数字小了，继续加油！')
    else:
        print('你输入的数字大了，继续努力！')
    i = int(input('请输入两位整数:'))
    k = k+1
else:
    print('你输入的数字正确，你好聪明！')
    print('你一共猜了',k,'次！')