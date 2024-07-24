```py


a=10
b=20
print(dir(a))

print(a+b)
print(a.__add__(b))
print('减法:',a.__sub__(b))
print(f'{a}<{b}吗？',a<b,a.__lt__(b))
print(f'{a}<={b}吗？',a<=b,a.__le__(b))
print(f'{a}={b}吗？',a==b,a.__eq__(b))
print(f'{a}>{b}吗？',a>b,a.__gt__(b))
print(f'{a}>={b}吗？',a>=b,a.__ge__(b))
print(f'{a}!={b}吗？',a!=b,a.__ne__(b))
print(a.__mul__(b)) #a*b
print(a.__truediv__(b)) #非整除
print(a.__mod__(b))
print(a.__floordiv__(b))
print(a.__pow__(2))

```
