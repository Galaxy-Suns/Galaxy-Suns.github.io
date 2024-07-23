def calc(a,b):   #a和b成为形式参数，简称形参，形参的位置在函数的定义处
    c=a+b
    return c




result=calc(10,20)   #10,20成为实际参数的值，简称实参，实参的位置是函数的调用处 按照形参对应位置传递实参
print(result)


res=calc(b=10,a=20) # = 左侧的变量的名称称为 关键字参数 按照形参名称传递实参，优先于按照形参位置传
print(res)