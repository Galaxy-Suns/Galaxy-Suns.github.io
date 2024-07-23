# ---------------trying-----------------
# 时间2021/12/8 9:37

d={'name':'张三','name':'李四'}#key不允许重复
print(d)

d={'name':'张三','dickname':'张三'}
print(d)

lst=[10,20,30,40]
lst.insert(1,100)
print(lst)
#d={lst:100}#TypeError: unhashable type: 'list'
