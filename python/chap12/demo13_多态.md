```py

#以下三个类都有一个同名的方法 eat()
class Person:
    def eat(self):
        print("人，吃五谷杂粮")

class Cat:
    def eat(self):
        print("猫，喜欢吃鱼")

class Dog:
    def eat(self):
        print("狗，喜欢啃骨头")

def fun(obj): #函数的定义处，obj是形式参数
    obj.eat() #对象名打点调用方法

if __name__ == '__main__':
    per=Person() #创建Person类型对象
    cat=Cat() #创建Cat类型对象
    dog=Dog() #创建Dog类型对象

    #调用fun()函数
    fun(per) #python中的多态不关心对象的数据类型，只关心对象是否具有同名的方法
    fun(cat)
    fun(dog)```
