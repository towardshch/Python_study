url='http://www.something.com'
if url[-3]=='.':
    domain=url[11:-3] # 取列表中索引11到索引倒数第3（不包含倒数第三）的元素
else:
    domain=url[11:-4] # 取列表中索引11到索引倒数第3（不包含倒数第四）的元素
print('Domain name:'+domain)
