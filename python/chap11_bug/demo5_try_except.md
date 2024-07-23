```py
'''try except'''

try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    print('结果为',a/b)
except ZeroDivisionError:
    print('除数不允许为0')
print('程序结束')```
