'''动态绑定属性和方法'''

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
print('------------为stu2动态绑定性别属性-------------------')
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)

print('--------------------------------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的，称函数')
stu1.show=show #将函数绑定到对象中，就成为了方法
stu1.show()
#stu2.show()