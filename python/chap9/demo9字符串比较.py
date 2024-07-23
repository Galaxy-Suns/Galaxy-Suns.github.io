'''字符串的比较操作'''

print('apple'>'app') #True
print('apple'>'banana') #False 比较原始值 相当于比较97>98
print(ord('a'),ord('b')) #a:97 b:98
print(ord('杨'))
print('b'>'a') #True

print(chr(97))
print(chr(26472))

''' == 与 is 的区别
  == 比较的是 value 
  is 比较的是 id 是否相等'''

a=b='Python'
c='Python'
print(a==b) #True
print(b==c) #True

print(a is b) #True
print(a is c) #True
print(id(a)) #39013104
print(id(b)) #39013104
print(id(c)) #39013104

