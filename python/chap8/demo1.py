# ---------------trying-----------------
# 时间2021/12/8 16:00
'''不可变序列，可变序列'''
'''可变序列  列表，字典'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
'''不可变序列  字符串，元组'''
s='hello'
print(id(s))
s+='world'
print(id(s))
print(s)