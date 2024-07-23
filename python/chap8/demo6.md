```py
#集合的相关操作
s={10,20,30,405,60}
'''集合元素的判断操作'''
print(10 in s)#True
print(100 in s)#False
print(10 not in s)#False
print(100 not in s)#True
'''集合元素的新增操作'''
s.add(80) #add一次添加一个元素
print(s)
s.update({200,400,300}) #update一次至少添加一个元素
print(s)
s.update([100,98,8])
s.update((32,34,65))
print(s)

'''集合元素的删除操作'''
s.remove(100)#不存在抛异常
print(s)
#s.remove(500) #KeyError: 500
s.discard(500)#不存在不抛异常
print(s)
s.pop()
s.pop()
#s.pop(405) #TypeError: pop() takes no arguments (1 given) 不可指定参数
print(s)
s.clear()
print(s)```
