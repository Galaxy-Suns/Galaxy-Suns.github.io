# ---------------trying-----------------
# 时间2021/8/17 21:04
#布尔运算符
a,b=1,2
print('-------------and 并且---------------')
print(a==1 and b==2)  #True   #True and True --> True
print(a==1 and b<2)   #False   #True and False --> False
print(a!=1 and b==2)  #False   #False and True --> False
print(a!=1 and b!=2)  #False   #False and False --> False

print('-------------or 或者---------------')
print(a==1 or b==2)  #True   #True or True --> True
print(a==1 or b<2)   #True   #True or False --> True
print(a!=1 or b==2)  #True   #False or True --> True
print(a!=1 or b!=2)  #False   #False or False --> False

print('-------------not 对bool类型操作数取反---------------')
f=True
f2=False
print(not f)  #False
print(not f2) #True

print('-------------in 与not in---------------')
s='helloworld'
print('w' in s)  #True
print('k' in s)  #False
print('w' not in s)  #False