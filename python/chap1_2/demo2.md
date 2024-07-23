```py
# ---------------trying-----------------
# 时间2021/6/2619:08
#转义字符
print('hello\nworld')#\  +   转义字符的首字母 n---newline的首字母表示换行
print('hello\tworld')#每四个字母为一个制表位。如果前面制表位已满，\t空一个制表位。如果前面制表位未满，\t用空格补全制表位
print('helloooo\tworld')
print('hello\rworld')#world将hello进行了覆盖
print('hello\bworld')#\b是退一个格，将o退没了
print('http:\\\\www.baidu.com')#字符串里有\或'或“要用\+ \或'或”替代，不然会干扰
print('老师说：\'大家好\'')

#源字符：不希字符串中的转义字符起作用，就使用源字符，就是在字符串之前加r或R
print(r'hello\nworld')
#注意事项：最后一个字符不能是反斜杠
#print(r'hello\nworld\')
print(r'hello\nworld\\')```
