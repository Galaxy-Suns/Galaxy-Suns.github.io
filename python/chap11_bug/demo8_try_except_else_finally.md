```py
'''try except else finally'''

try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
except BaseException as e:
    print('出错了',e)
else:
    print('结果为',a/b)
finally: # 无论是否出错都会执行
    print('谢谢您的使用')```
