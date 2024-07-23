'''字符串的替换与合并'''


s='hello,Python'
print(s.replace('Python','Java'))# hello,Java 用’Java‘替换‘Python'
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))# hello,Java,Java,Python 换两次


lst=['hello','java','Python']
print('|'.join(lst))# hello|java|Python 用’|‘连接lst的内容
print(''.join(lst))

t=('hello','java','Python')
print(''.join(t))

print('*'.join('Python'))