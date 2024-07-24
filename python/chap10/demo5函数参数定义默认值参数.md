```py


'''函数参数定义_默认值参数'''
def fun(a,b=10): # b称为默认值参数
    print(a,b)

# 函数的调用
fun(100) # 100 10
fun(20,30) # 20 30

print('hello')
print('world')

r'''
由于函数 print() 的默认值参数 end='\n',所以输出后自动换行
因此可以解释输入 end='\t' 时不换行输出的原理
使用 end='' 时运用了默认值参数和形参名称传参的原理
'''

print('hello',end='\t')
print('world')


```
