```py


class Student:  # Student为类的名称（类名）由一个或多个单词组成,每个单词的首字母大写其余小写
    native_pace='吉林'  # 直接写在类的变量，称为类属性
    def __init__(self,name,age): # 初始化方法
        self.name=name # self.name 称为实例属性，进行了一个赋值操作，将局部变量 name 的值赋给实例属性
        self.age=age


    #实例方法
    def cat(self):
        print('学生在吃饭...')

    #静态方法
    @staticmethod
    def method(): #静态方法中（）内不允许写
        print('我使用了 staticmethod 进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def nm(cls):
        print('我是类方法，因为我使用了 classmethod 进行修饰')

#在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')


```
