```py


# ---------------trying-----------------
# 时间2021/8/17 19:03
#赋值运算符，运算顺序从右到左
i=3+4
print(i)
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('------------支持参数赋值------------')
a=20
a+=30   #相当于a加30再赋值给a
print(a)
a-=10   #相当于a-10再赋值给a
print(a)
a*=2    #相当于a*2再赋值给a
print(type(a))
print(a)
a/=3    #相当于a/3再赋值给a
print(type(a))
print(a)
a//=2   #
print(type(a))
print(a)
a%=3
print(type(a))
print(a)
a,b,c=20,30,40
print('-------------解包赋值-------------')
print(a,b,c)
#a,b=20,30,40   #报错，因为左右变量的个数和值的个数不对应
print('----------交换两个变量的值----------')
a,b=10,20
print('交换之前',a,b)
#交换
a,b=b,a
print('交换之后',a,b)

```
