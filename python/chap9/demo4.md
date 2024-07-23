```py
#字符串中大小写转换的方法
s='hello,python'
a=s.upper()  #转成大写后，会产生一个新的字符串对象 全部大写
print(a,id(a))
print(s,id(s))
b=s.lower()  #转换之后，会产生一个新的字符串对象  全部小写
print(b,id(b))
print(s,id(s))
print(b==s)
print(b is s)

s2='hello,Python'
print(s2.swapcase())  #大写转小写，小写转大写

print(s2.title())  #每个单词首字母大写

print(s2.capitalize())  #开头首字母大写```
