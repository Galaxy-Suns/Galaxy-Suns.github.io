```py


'''类属性'''

class Student:  # Student为类的名称（类名）由一个或多个单词组成,每个单词的首字母大写其余小写
    native_pace='吉林'  # 直接写在类的变量，称为类属性
    def __init__(self,name,age):  #初始化方法
        self.name=name # self.name 称为实例属性，进行了一个赋值操作，将局部变量 name 的值赋给实例属性
        self.age=age

    #实例方法
    def eat(self):
        print('学生在吃饭...')

    #静态方法
    @staticmethod
    def method(): #静态方法中（）内不允许写
        print('我使用了 staticmethod 进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了 classmethod 进行修饰')

#类属性的使用方式
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('------------------类方法的使用方式-----------------------')
Student.cm() # 我是类方法，因为我使用了 classmethod 进行修饰 用类名直接访问
print('------------------静态方法的使用方式-----------------------')
Student.method() #我使用了 staticmethod 进行修饰，所以我是静态方法 用类名直接访问

```
