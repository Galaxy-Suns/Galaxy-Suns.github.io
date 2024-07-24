```py
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def show(self):
        print(f'我叫:{self.__name}，我今年{self.__age}岁了')

if __name__ == '__main__':
    #程序运行没有报错，但是运行结果不符合实际情况，年龄被赋予不正确的值，所以程序不够安全
    stu=Student('陈梅梅',-23)
    stu.show()



class Student:
    def __init__(self,name):
        self.__name=name
    #使用@property
    @property
    def age(self): #设置只读属性
        return self.__age

    #设置赋值操作
    @age.setter
    def age(self,value):
        if value<0 or value>130:
            print("年龄不在正确的区间范围，设置年龄的范围应在0-130")
            self.__age=18
        else:
            self.__age=value

    def show(self):
        print(f'我叫{self.__name},今年{self.__age}岁了')




if __name__ == '__main__':
    stu=Student("陈梅梅") #创建Student类型对象
    stu.age=-23 #由于使用@property修饰，方法变为属性不用加（）
    print(stu.age)
    stu.show()
```
