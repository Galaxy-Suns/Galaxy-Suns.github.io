```py


'''多个except结构'''

try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    print('结果为',a/b)
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError: # 捕获异常按照先子类后父类的顺序
    print('只能输入数字串')
print('程序结束')

```
