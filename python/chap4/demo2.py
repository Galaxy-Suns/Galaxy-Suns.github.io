# ---------------trying-----------------
# 时间2021/8/20 12:49
#测试对象的布尔值
print('------------------以下对象的布尔值为False---------------------')
print(bool(False))#False
print(bool(0))#False
print(bool(0.0))#False
print(bool(None))#False
print(bool(''))#False
print(bool(""))#False
print(bool([]))#False    #空列表
print(bool(list()))#False    #空列表
print(bool(tuple()))#False    #空元组
print(bool(()))#False    #空元组
print(bool({}))#False    #空字典
print(bool(dict()))#False    #空字典
print(bool(set()))#False     #空集合
print('-----------------其他对象的布尔值均为True----------------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))
