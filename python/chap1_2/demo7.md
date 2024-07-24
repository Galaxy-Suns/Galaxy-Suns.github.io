```py


# ---------------trying-----------------
# 时间2021/7/3 15:09
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)
print(n1+n3)#浮点数(小数）的存储有不精确性（和二进制有关)，要用decimal模块运算
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))


```
