```py


s='hello,Python'
'''居中对齐'''
print(s.center(20,'*'))

'''左对齐'''
print(s.ljust(20,'*'))
print(s.ljust(10,'*'))# hello,Python 设置宽度小于原字符串宽度返回原字符串
print(s.ljust(20))#默认用‘ ’填充

'''右对齐'''
print(s.rjust(20,'*'))
print(s.rjust(20))
print(s.rjust(10))

'''右对齐,使用0进行填充'''
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))

```
