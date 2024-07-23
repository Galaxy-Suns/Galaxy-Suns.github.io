```py
'''字符串的切片操作'''

s='hello,Python'
s1=s[:5]   # hello 由于没有指定起始位置，所以从0开始切
s2=s[6:]   # Python 由于没有指定结束位置，所以切到字符串的最后一个元素
s3='!'
s4=s1+s3+s2 # hello!Python

print(s1)
print(s2)
print(s4)
print('----------------------------------')
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))

print('----------------------切片[start:end:step]-----------------------')
print(s[1:5:1])  # ello 从1开始截到5（不包含5），步长为1
print(s[::2])  # hloPto 默认从0开始，没有写结束，默认到字符串的最后一个元素，步长为2，两个元素之间的索引间隔为2
print(s[::-1]) # nohtyP,olleh 默认从字符串的最后开始，到字符串的开头结束（因为步长负数）
print(s[-6::1])  # Python 从索引为-6开始，到字符串最后结束，步长为1```
