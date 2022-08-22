months=['January', 'February','March','April','May','June','July', \
        'August','September','October','November','December']
# 创建了一个months列表，包含一年中的12个月份
while True:
    month_num=int(input("请输入月份："))
    if month_num!=0:
        print('你输入的月份是%s'%months[month_num-1]) # 根据索引提取列表中对应的元素
    else:
        break
