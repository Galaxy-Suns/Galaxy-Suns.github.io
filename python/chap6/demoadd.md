```py
# ---------------trying-----------------
# 时间2021/8/29 16:27
#向列表的末尾添加一个元素
lst=[10,20,30]
print('添加元素之前',lst)
print(id(lst))
lst.append(100)
print('添加元素之后',lst)
print(id(lst))
lst2=['hello','world']
#lst.append(lst2)#将lst2作为一个元素添加到列表的末尾
#lst.extend(lst2)#向列表末尾一次性添加多个元素
print(lst)

#在任意位置上添加一个元素
lst.insert(1,90)
print(lst)

lst3=[True,False,'hello']
#在任意的位置上添加N多个元素
lst[1:]=lst3
print(lst)
```
