```py


'''函数参数传递的内存分析'''
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)   #没有 return 的原因是因为在执行后不会携带任何结果（没有将fun()赋值,输出等后续操作）,return可省略
    return

n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)   #将位置传参  arg1 arg2 是函数定义处的形参 n1 n2 是函数调用处的实参

print('n1',n1)
print('n2',n2)

'''在函数的调用过程中，进行参数的传递
如果是不可变对象，形参在函数体的修改不会影响实参的值 arg1的值修改为100，不会影响n1的值
如果是可变对象，形参在函数体的修改会影响实参的值 arg2的修改 .append(10),会影响到n2的值
'''

```
