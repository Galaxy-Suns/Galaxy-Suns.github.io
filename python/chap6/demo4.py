# ---------------trying-----------------
# 时间2021/8/29 16:19
print('p' in 'python')#True
print('k' not in 'python')#True

lst=[10,20,'python','hello']
print(10 in lst)#True
print(100 in lst)#False
print(10 not in lst)#False
print(100 not in lst)#True
print('----------------------------')
for item in lst:
    print(item)