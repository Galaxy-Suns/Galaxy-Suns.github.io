'''字符串的劈分操作'''

'''split()方法从左侧开始劈分'''

s='hello world Python'
lst=s.split()
print(lst)  #['hello', 'world', 'Python'] 默认劈分符’ ‘

s1='hello|world|Python'
lst1=s1.split(sep='|') #可以使用参数sep指定劈分符
print(lst1)

print(s1.split(sep='|',maxsplit=1))  # ['hello', 'world|Python'] 劈分一次 maxsplit指定最大劈分次数

print('------------------------------')

'''rsplit()方法从右侧开始劈分'''

print(s.rsplit())

print(s1.rsplit('|'))

print(s1.rsplit(sep='|',maxsplit=1))