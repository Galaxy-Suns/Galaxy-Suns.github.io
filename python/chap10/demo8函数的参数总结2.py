'''函数的参数总结'''

def fun(a,b=10): # b在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=',a)
    print('b=',b)

def fun2(*args): # 个数可变的位置形参
    print(args)

def fun3(**args): # 个数可变的关键字形参
    print(args)

fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)

def fun4(a,b,*,c,d):  #从 * 之后的参数，在函数调用时，只能采用关键字传参，该 * 采用关键字形参
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

#调用 fun4() 函数
#fun4(10,20,30,40) # 位置实参传递
fun4(a=10,b=20,c=30,d=40) # 关键字实参传递
fun4(10,20,c=30,d=40) # 前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传递
'''需求： c,d只能采用关键字实参传递'''


'''函数定义时的形参顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass
def fun6(*args1,**args2):
    pass
def fun7(a,b=10,*args1,**args2):
    pass