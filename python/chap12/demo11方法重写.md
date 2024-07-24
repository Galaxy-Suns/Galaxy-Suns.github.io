```py


class Person:  #默认继承object
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"大家好，我叫{self.name},今年{self.age}了")


#Student类继承Person类
class Student(Person):
    #编写初始化方法
    def __init__(self,name,age,stuno):
        #调用父类的初始化方法
        super().__init__(name,age) #给name age赋值
        self.stuno=stuno #给自己特有属性赋值

    #重写父类的方法
    def show(self):
        #可以调用父类的show方法，也可以重写编写实现方法的代码，显示输出内容
        #调用父类的方法
        super().show()
        #再编写自己个性化的内容
        print(f"我来自马士兵教育，我的学号是{self.stuno}")


class Doctor(Person):
    def __init__(self,name,age,department):
        #调用父类的初始化方法
        Person.__init__(self,name,age) #给name age赋值
        self.department=department #给自己特有属性赋值

    def show(self):
        #重新编写父类的实现代码
        print(f'大家好,我叫{self.name},我今年{self.age}，我的工作科室是{self.department}')

if __name__ == '__main__':
    #创建Student类对象
    stu=Student("陈梅梅",20,1001)
    stu.show()
    #创建Doctor类对象
    dor=Doctor("张一一",32,"外科")
    dor.show()

```
